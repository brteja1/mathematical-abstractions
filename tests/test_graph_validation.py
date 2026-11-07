"""Mutation tests ensure sanity checks reject structural regressions."""
import copy
import json
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from validate_graph import validate
ROOT=Path(__file__).resolve().parents[1]

class GraphValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.document=json.loads((ROOT/'catalog.jsonld').read_text())

    def setUp(self):
        self.doc=copy.deepcopy(self.document)
        self.concept=next(n for n in self.doc['@graph'] if n.get('type')=='Concept')

    def test_current_graph_valid(self):
        self.assertEqual(validate(self.doc),[])

    def test_missing_basis_rejected(self):
        self.concept.pop('axiomBasis')
        self.assertTrue(any('axiomBasis' in e for e in validate(self.doc)))

    def test_wrong_claim_kind_rejected(self):
        self.concept['hasAxiom'].append(self.concept['hasTheorem'][0])
        self.assertTrue(any('wrong target type for hasAxiom' in e for e in validate(self.doc)))

    def test_dangling_derivation_rejected(self):
        claim=next(n for n in self.doc['@graph'] if n.get('type')=='Theorem')
        claim['dependsOn']=['urn:missing']
        self.assertTrue(any('dangling dependsOn' in e for e in validate(self.doc)))

    def test_cyclic_derivation_rejected(self):
        claims=[n for n in self.doc['@graph'] if n.get('type')=='Theorem'][:2]
        claims[0]['dependsOn']=[claims[1]['id']];claims[1]['dependsOn']=[claims[0]['id']]
        self.assertTrue(any('Cyclic claim dependency' in e for e in validate(self.doc)))

    def test_cyclic_specialization_rejected(self):
        concepts={n['shortForm']:n for n in self.doc['@graph'] if n.get('type')=='Concept'}
        # Group → Monoid → Semigroup already exists; close the longer cycle.
        concepts['Semigroup']['specializationOf']=[concepts['Group']['id']]
        self.assertTrue(any('Cyclic specialization' in e for e in validate(self.doc)))

    def test_self_specialization_rejected(self):
        self.concept['specializationOf']=[self.concept['id']]
        self.assertTrue(any('Cyclic specialization' in e for e in validate(self.doc)))

    def test_duplicate_specialization_rejected(self):
        parent=next(n['id'] for n in self.doc['@graph']
                    if n.get('type')=='Concept' and n['id']!=self.concept['id'])
        self.concept['specializationOf']=[parent,parent]
        self.assertTrue(any('duplicate specializationOf' in e for e in validate(self.doc)))

    def test_empty_operation_interface_needs_explanation(self):
        self.concept['hasOperation']=[]
        self.assertTrue(any('missing operations or' in e for e in validate(self.doc)))

    def test_duplicate_ids_rejected(self):
        self.doc['@graph'].append(copy.deepcopy(self.concept))
        self.assertTrue(any('Duplicate ID' in e for e in validate(self.doc)))

    def test_formal_rule_required(self):
        ax=next(n for n in self.doc['@graph'] if n.get('type')=='Axiom');ax.pop('formalStatement')
        self.assertTrue(any('formalStatement' in e for e in validate(self.doc)))

    def test_new_entry_without_source_rejected(self):
        n=copy.deepcopy(self.concept)
        n.update(id='urn:test:new-concept',shortForm='NewConcept')
        n.pop('source',None)
        self.doc['@graph'].append(n)
        self.assertTrue(any('urn:test:new-concept: missing required source' in e for e in validate(self.doc)))

    def test_existing_citation_cannot_be_removed(self):
        next(n for n in self.doc['@graph'] if n.get('type')=='Concept' and n.get('source')).pop('source')
        self.assertTrue(any('missing required source' in e for e in validate(self.doc)))

    def test_new_claim_requires_precise_provenance(self):
        original=next(n for n in self.doc['@graph'] if n.get('type')=='Theorem' and n.get('source'))
        n=copy.deepcopy(original);n['id']='urn:test:new-theorem'
        for key in ['sourceLocator','sourceNote','provenanceKind']:n.pop(key,None)
        self.doc['@graph'].append(n)
        self.assertTrue(any('missing provenance field sourceLocator' in e for e in validate(self.doc)))
        n.update(sourceLocator='Named result in the cited reference',sourceNote='Adapted statement; local notation differs.',provenanceKind='adapted')
        self.assertFalse(any('urn:test:new-theorem:' in e for e in validate(self.doc)))

    def test_new_axiom_needs_a_source(self):
        n=copy.deepcopy(next(n for n in self.doc['@graph'] if n.get('type')=='Axiom'))
        n['id']='urn:test:new-axiom';n.pop('source',None)
        self.doc['@graph'].append(n)
        self.assertTrue(any('urn:test:new-axiom: missing required source' in e for e in validate(self.doc)))

    def test_legacy_gap_cannot_be_hidden(self):
        n=next(n for n in self.doc['@graph'] if n.get('provenanceStatus')=='legacy-source-missing')
        n.pop('provenanceStatus')
        self.assertTrue(any('legacy source gap must be disclosed' in e for e in validate(self.doc)))

    def test_new_source_needs_metadata(self):
        self.doc['@graph'].append({'id':'urn:test:new-source','type':'Source','label':'Example','url':'https://example.org/'})
        self.assertTrue(any('new Source missing accessedOn' in e for e in validate(self.doc)))

    def test_new_source_date_must_be_iso_date(self):
        self.doc['@graph'].append({'id':'urn:test:dated-source','type':'Source',
                                  'label':'Example','url':'https://example.org/',
                                  'accessedOn':'not-a-date','sourceRole':'definition'})
        self.assertTrue(any('accessedOn must be YYYY-MM-DD' in e for e in validate(self.doc)))

    def test_baseline_cannot_be_extended_to_exempt_new_claims(self):
        from unittest.mock import patch
        real_read = Path.read_text
        def read(path, *args, **kwargs):
            text = real_read(path, *args, **kwargs)
            if path.name == 'provenance_legacy.json':
                baseline = json.loads(text)
                baseline['missingSourceIds'].append('urn:test:illicit-exemption')
                return json.dumps(baseline)
            return text
        with patch.object(Path, 'read_text', read):
            self.assertTrue(any('baseline cannot be extended' in e for e in validate(self.doc)))

if __name__=='__main__':unittest.main()
