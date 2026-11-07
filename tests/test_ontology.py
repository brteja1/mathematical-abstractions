"""Exercise ONTFS exports and constraints when the optional backend is present."""
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from markdown_graph import ROOT, load_graph
sys.path.insert(0, str(ROOT / 'deps/ONTFS'))
AVAILABLE = all(importlib.util.find_spec(m) for m in ['ontfs', 'rdflib', 'pyshacl'])


@unittest.skipUnless(AVAILABLE, 'ONTFS and its SHACL dependencies are not installed')
class OntologyTests(unittest.TestCase):
    def setUp(self):
        from ontology import build, backend
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.directory = Path(self.tmp.name)
        build(self.directory)
        self.store = backend()(str(self.directory))

    def test_catalog_rdf_triples_preserved(self):
        from rdflib import Graph
        doc = load_graph()
        original = Graph().parse(data=json.dumps(doc), format='json-ld')
        self.assertTrue(set(original) <= set(self.store.graph.graph))

    def test_projection_conforms(self):
        from ontology import check
        result = check(self.directory)
        self.assertTrue(result['conforms'])
        self.assertTrue(result['shapes_loaded'])
        self.assertEqual(result['concepts'], sum(n['type'] == 'Concept' for n in load_graph()['@graph']))

    def test_specialization_does_not_assert_axiom_inheritance(self):
        from rdflib import URIRef, OWL, RDF
        from ontology import CA
        for name in ['specializationOf', 'requiresConcept', 'relatedConcept', 'dependsOn']:
            self.assertNotIn((URIRef(CA + name), RDF.type, OWL.TransitiveProperty), self.store.graph.graph)
        self.assertNotIn((URIRef(CA + 'relatedConcept'), RDF.type, OWL.SymmetricProperty), self.store.graph.graph)

    def test_incorrect_specialization_target_rejected_by_proposal(self):
        from ontology import CA
        doc = load_graph()
        group = next(n for n in doc['@graph'] if n.get('shortForm') == 'Group')
        operation = next(n for n in doc['@graph'] if n['type'] == 'Operation')
        proposal = self.store.propose_link(group['id'], CA + 'specializationOf', operation['id'])
        result = self.store.validate_proposal(proposal['id'])
        self.assertFalse(result['valid'])
        self.assertTrue(result['violations'])

    def test_bounded_context_and_markdown_document_links(self):
        from ontology import CA
        from rdflib import URIRef
        group = next(n for n in load_graph()['@graph'] if n.get('shortForm') == 'Group')
        self.assertLessEqual(len(self.store.context(group['id'], limit=4)['facts']), 4)
        docs = list(self.store.graph.graph.objects(URIRef(group['id']), URIRef(CA + 'document')))
        self.assertEqual(len(docs), 1)
        self.assertEqual(self.store.graph.to_path(docs[0]), str(ROOT / 'concepts/Group.md'))

    def test_export_refuses_to_overwrite_edits(self):
        from ontology import build
        target = self.directory / '.ontfs.ttl'
        target.write_text(target.read_text() + '\n# local experiment\n')
        with self.assertRaisesRegex(ValueError, 'unexported edits'):
            build(self.directory)

    def test_rebuild_is_semantically_idempotent(self):
        from ontology import build, backend
        from rdflib.compare import isomorphic
        old = self.store.graph.graph
        build(self.directory)
        self.assertTrue(isomorphic(old, backend()(str(self.directory)).graph.graph))


if __name__ == '__main__':
    unittest.main()
