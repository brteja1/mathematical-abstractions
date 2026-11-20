# SKOS Core formalism

[SKOS](../concepts/SKOS.md) records an instance-level relational presentation of
the [W3C SKOS Reference](https://www.w3.org/TR/2009/REC-skos-reference-20090818/),
Core conditions S1–S46. The consulted
[errata](https://www.w3.org/2006/07/SWD/SKOS/reference/20090811-errata)
clarifies that preferred-label uniqueness also applies to labels without a
language tag. Every defining rule and derived law links directly to its source
and section. The consultation date is 2026-11-19.

## Interpretation and scope

An interpretation has a nonempty domain of resources, unary class extensions
and binary property extensions. Literal values are resources in this domain.
The entry uses the existing PredicateLogic, Relation and RDFGraph concepts.
Graph terms and semantic resources have different equality conventions: distinct
IRIs need not denote distinct resources, and blank nodes are existentially
interpreted. Label comparison uses interpreted plain-literal values and
normalized language tags, with a separate key for an absent tag.

The class and property conditions form a theory T. A graph G is satisfiable when
some interpretation satisfies both T and G. A sentence follows from G when it
holds in every such interpretation. These operations define semantic predicates,
not a decision procedure. An inconsistent graph has no models and classically
entails every sentence.

This presentation captures the Core instance constraints. It records the W3C
class/property declarations descriptively, without reifying their OWL metamodel
semantics. It does not implement all RDF/RDFS/OWL Full semantics or establish a
translation-equivalence theorem. SKOS-XL (S47 onward) is outside this entry.
RDF literal interpretation and RDF list typing/first/rest/nil semantics must be
supplied when interpreting concrete graphs. The catalog's finite RDFGraph is
an assertion carrier; interpretation domains and property extensions need not
be finite.

## Defining basis

| W3C conditions | Catalog rule | Meaning captured |
| --- | --- | --- |
| S1–S2, S9, S28–S29, S37 | class-integrity | Four classes, ordered-collection inclusion, concept/scheme/collection disjointness |
| S3–S8 | scheme-relations | Scheme range, top-concept endpoint typing, inverse and membership inclusion |
| S10–S12 | lexical-labels | Label-property declarations, plain-literal range, inclusion in rdfs:label |
| S13–S14 plus erratum | label-integrity | Pairwise disjoint label roles; preferred-label uniqueness per language key |
| S15–S17 | notations-and-notes | Literal notation values and note subproperty relationships |
| S18–S26 | semantic-relations | Concept endpoints, property inclusions, inverses, symmetry and specified transitivity |
| S27 | hierarchy-association-disjointness | No overlap of related and broaderTransitive |
| S30–S36 | collection-relations | Membership range, ordered-list typing, semantic functionality and list-item implication |
| S38–S45 | mapping-relations | Mapping subproperties, inverse relationships, symmetry and exact-match transitivity |
| S46 | mapping-disjointness | Exact mapping disjoint from broad and associative mapping |

Four separate derived laws have explicit premise links and editorial proof
sketches: broader-path inference, reflexivity on the support of exactMatch,
exact/narrow mapping disjointness, and indirect hierarchy/association conflict.
They have no registered machine-checked witnesses.

## Consequences and boundaries

* `a broader b` and `b broader c` imply `a broaderTransitive c`. They do not
  alone imply `a broader c`. A transitive superrelation may contain additional
  pairs; it is not defined to be exactly the closure of the asserted edges.
* `a exactMatch b` implies its reverse and self-pairs at a and b. It does not
  identify a and b or transfer their labels. Reflexivity on all concepts is not
  required, so this property is not registered as an EquivalenceRelation.
* Neither cycles nor multiple broader paths violate SKOS by themselves. The
  hierarchy is therefore not registered as a Preorder or PartialOrder.
* A resource may have no preferred label. Two distinct preferred plain-literal
  values under the same language key violate label integrity. A shared label
  on different subjects is allowed. Labeling a resource does not type it as a
  Concept.
* `inScheme` has a scheme range but no Concept domain. A concept may belong to
  zero or several schemes. Broader links do not transfer scheme membership;
  mapping properties are not restricted to different schemes by an integrity
  condition.
* `memberList` functionality equates list-head denotations. Two distinct blank
  node identifiers alone do not demonstrate a violation. List well-formedness
  and treating each head as a unique finite sequence are additional policies.
  Ordinary members need not all occur in the member list.
* Extra application policies, such as acyclic hierarchies, required labels or
  globally unique notation codes, require separate assumptions.

These statements concern the modeled SKOS vocabulary. They do not alter the
catalog's own RDF schema or make its specialization links SKOS broader links.
SKOS depends on an RDF representation; it is not a specialization of the
RDFGraph abstract data type.

## Lean and validation

[`Catalog.SKOS`](../lean/Catalog/SKOS.lean) is a partial interface for concept
typing, broader/narrower, broaderTransitive, related and exactMatch. It encodes
selected conditions as structure fields. Those assumed fields do not prove a
concrete model satisfies the complete SKOS theory. Labels, schemes, collections,
the remaining mappings, RDF interpretation and complete OWL semantics are
omitted. No catalog claim is bound to a proof witness by this addition.

Use `make check-lean` for excerpt/binding consistency and `make test-lean` for
compiler and axiom-audit evidence. Structural catalog, SHACL and SPARQL checks
are separate from semantic correctness or proof of correspondence to W3C SKOS.

```sh
python3 scripts/catalog.py get SKOS
python3 scripts/catalog.py get SKOS --sections operations axioms laws
python3 scripts/agent_query.py node urn:csabs:law/SKOS-broader-path
```
