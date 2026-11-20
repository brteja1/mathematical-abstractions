# SKOS Core ontology (relational semantic presentation)

An interpretation of the SKOS Core vocabulary for concepts, schemes, lexical labels, notations, notes, semantic relations, collections and concept mappings, with explicit inference conditions and integrity constraints.

**Notation:** M=(D,C,S,K,O,(P_p)_p,…); M⊨T_SKOS; G⊨_SKOS φ iff every SKOS model of G satisfies φ

**Stable ID:** `urn:csabs:concept/SKOS`

**Categories:** Relational data modelling, Logic and proof

**Kind:** semantic-model

**Prerequisites:** [Predicate Logic](PredicateLogic.md), [Binary relation](Relation.md), [Finite RDF 1.1 graph](RDFGraph.md)

**Related concepts:** [Preorder](Preorder.md), [Equivalence relation](EquivalenceRelation.md)

## Mathematical formulation

Relational interpretation of SKOS Core S1–S46 at the instance level, with the S14 erratum. D is a nonempty resource domain including literal values; class extensions are subsets of D and property extensions subsets of D×D. C=Concept, S=ConceptScheme, K=Collection, O=OrderedCollection; P\_p denotes the extension of property p, with skos: prefix omitted. RDF names denote resources without a unique-name assumption; model equality is resource identity, distinct from RDF term equality and exactMatch. Plain⊆D denotes 2009 RDF plain-literal values; lang:Plain→LanguageTag⊎{none} uses case-insensitive normalized tags; none is a separate language key. LV⊆D denotes literal values. RDF list typing and first/rest/nil interpretation are supplied by the RDF semantic environment; item(l,x) holds when x is a first value at a cell reachable from l by finitely many rest links. No finite-domain, closed-world, acyclicity, total labeling, unique notation, or single-scheme assumption. Empty class/property extensions and empty asserted graphs are allowed. This is an instance-level relational presentation, not an implementation of the complete RDF/RDFS/OWL Full metamodel or a claim of equivalence to it; SKOS-XL is excluded. Schema declarations retain their W3C locators; OWL class/property categories are recorded descriptively rather than reified in this first-order signature. Let T\_SKOS be the conjunction of the defining rules below. A graph G is satisfiable when ∃M, M⊨T\_SKOS∧G; G⊨\_SKOS φ iff ∀M,(M⊨T\_SKOS∧G⇒M⊨φ). Blank nodes are existentially interpreted, not fixed global names. Transitive superrelations need not equal the least transitive closure of asserted broader edges.

**Lean formulation** (in its source module context):

```lean
structure SKOS (D : Type u) [Nonempty D] where
  concept : D → Prop
  broader : D → D → Prop
  narrower : D → D → Prop
  broaderTransitive : D → D → Prop
  related : D → D → Prop
  exactMatch : D → D → Prop
  broaderTyping : ∀ x y, broader x y → concept x ∧ concept y
  transitiveTyping : ∀ x y, broaderTransitive x y → concept x ∧ concept y
  relatedTyping : ∀ x y, related x y → concept x ∧ concept y
  exactTyping : ∀ x y, exactMatch x y → concept x ∧ concept y
  inverseHierarchy : ∀ x y, narrower x y ↔ broader y x
  hierarchyInclusion : ∀ x y, broader x y → broaderTransitive x y
  hierarchyTransitivity : ∀ x y z,
    broaderTransitive x y → broaderTransitive y z → broaderTransitive x z
  relatedSymmetry : ∀ x y, related x y → related y x
  hierarchyDisjointness : ∀ x y, related x y → ¬ broaderTransitive x y
  exactSymmetry : ∀ x y, exactMatch x y → exactMatch y x
  exactTransitivity : ∀ x y z, exactMatch x y → exactMatch y z → exactMatch x z
```

**Source:** [`Catalog.SKOS`](../lean/Catalog/SKOS.lean); consulted 2026-11-19.

**Scope:** partial

**Interpretation:** D is a nonempty domain of interpreted resources with identity equality. concept and the five binary relations interpret the corresponding SKOS extensions. The fields encode selected typing, inverse, inclusion, symmetry, transitivity and disjointness conditions from S19–S27 and S44–S45.

**Limits:** Partial semantic-relation interface only. No labels, schemes, collections, full mapping hierarchy, RDF parser/interpretation, OWL Full metamodel, or general entailment solver. Structure law fields constrain inputs; no model-satisfaction theorem or catalog claim proof witness is registered.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Instance-level relational translations of W3C SKOS Core S1–S46: class typing/disjointness; property domains/ranges, inclusions, inverses, symmetry, transitivity and functionality; label integrity; list-to-member implication. S14 includes untagged labels per the consulted errata.

**basisKind:** defined-structure

**basisScope:** Relational interpretation of SKOS Core S1–S46 at the instance level, with the S14 erratum. D is a nonempty resource domain including literal values; class extensions are subsets of D and property extensions subsets of D×D. C=Concept, S=ConceptScheme, K=Collection, O=OrderedCollection; P_p denotes the extension of property p, with skos: prefix omitted. RDF names denote resources without a unique-name assumption; model equality is resource identity, distinct from RDF term equality and exactMatch. Plain⊆D denotes 2009 RDF plain-literal values; lang:Plain→LanguageTag⊎{none} uses case-insensitive normalized tags; none is a separate language key. LV⊆D denotes literal values. RDF list typing and first/rest/nil interpretation are supplied by the RDF semantic environment; item(l,x) holds when x is a first value at a cell reachable from l by finitely many rest links. No finite-domain, closed-world, acyclicity, total labeling, unique notation, or single-scheme assumption. Empty class/property extensions and empty asserted graphs are allowed. This is an instance-level relational presentation, not an implementation of the complete RDF/RDFS/OWL Full metamodel or a claim of equivalence to it; SKOS-XL is excluded. Schema declarations retain their W3C locators; OWL class/property categories are recorded descriptively rather than reified in this first-order signature.

**verificationObligation:** Supply RDF/RDFS literal and list interpretation explicitly before interpreting concrete RDF graphs.; Model-theoretic entailment and satisfiability are propositions, not decision procedures. An inconsistent graph entails every sentence classically.; Do not infer a partial order, universal reflexivity of exactMatch, resource identity from exactMatch, or closed-world completeness.; No specializationOf link to RDFGraph, Preorder or EquivalenceRelation: graph representation, transitive hierarchy and symmetric-transitive matching do not instantiate those entire interfaces.

**reviewStatus:** Editorial source and mathematical interface review; partial Lean interface; no compiled claim proof witness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-SKOS-class-extension"></a>

### class-extension

`urn:csabs:operation/SKOS-class-extension`

**signature:** classExtension : Interpretation×SKOSClass→𝒫(D)

**description:** Returns the interpreted extension of Concept, ConceptScheme, Collection or OrderedCollection.

**precondition:** M interprets the selected class.

**totality:** Total mathematical query on the stated domain; no algorithm or decidability guarantee.

**outcome:** The corresponding subset of D.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference

**sourceLocator:** §§3.3,4.3,9.3

**sourceNote:** Abstract query interface adapted from SKOS interpretation and entailment semantics.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-SKOS-property-extension"></a>

### property-extension

`urn:csabs:operation/SKOS-property-extension`

**signature:** propertyExtension : Interpretation×SKOSProperty→𝒫(D×D)

**description:** Returns the interpreted relation of any Core property, including label, notation and documentation properties.

**precondition:** M interprets the selected property.

**totality:** Total mathematical query on the stated domain; no algorithm or decidability guarantee.

**outcome:** The corresponding relation on resources, subject to the relevant basis rules.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference

**sourceLocator:** §§4.3–10.4

**sourceNote:** Abstract query interface adapted from SKOS interpretation and entailment semantics.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-SKOS-satisfies"></a>

### satisfies

`urn:csabs:operation/SKOS-satisfies`

**signature:** satisfies : Interpretation×RDFGraph→Prop

**description:** Tests satisfaction mathematically under the supplied RDF interpretation, rather than checking literal triple membership.

**precondition:** Fixed interpretation of IRIs, literals, RDF typing/list vocabulary and SKOS terms; blank-node assignment is existential.

**totality:** Total mathematical query on the stated domain; no algorithm or decidability guarantee.

**outcome:** True iff M satisfies T_SKOS and some blank-node assignment makes every asserted triple true.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference

**sourceLocator:** §§1.3–1.5

**sourceNote:** Abstract query interface adapted from SKOS interpretation and entailment semantics.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-SKOS-satisfiable"></a>

### satisfiable

`urn:csabs:operation/SKOS-satisfiable`

**signature:** satisfiable : RDFGraph→Prop

**description:** Asks whether any interpretation satisfies the graph and the stated SKOS instance constraints.

**precondition:** The RDF semantic environment and profile are fixed.

**totality:** Total mathematical query on the stated domain; no algorithm or decidability guarantee.

**outcome:** ∃M, satisfies(M,G). Missing labels/types are not by themselves violations.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference

**sourceLocator:** §§1.4–1.5

**sourceNote:** Abstract query interface adapted from SKOS interpretation and entailment semantics.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-SKOS-entails"></a>

### entails

`urn:csabs:operation/SKOS-entails`

**signature:** entails : RDFGraph×Sentence→Prop

**description:** Defines model-theoretic consequence for the stated profile.

**precondition:** The sentence and graph use the fixed interpreted vocabulary; this is not a full OWL Full reasoner.

**totality:** Total mathematical query on the stated domain; no algorithm or decidability guarantee.

**outcome:** ∀M, satisfies(M,G)⇒M⊨φ. Unsatisfiable inputs entail every sentence classically.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference

**sourceLocator:** §§1.4–1.5

**sourceNote:** Abstract query interface adapted from SKOS interpretation and entailment semantics.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-SKOS-class-integrity"></a>

### class-integrity

`urn:csabs:axiom/SKOS-class-integrity`

**statement:** Concepts, schemes and collections have disjoint extensions; ordered collections are collections.

**formalStatement:** C,S,K,O⊆D; C∩S=C∩K=S∩K=∅; O⊆K.

**description:** The four vocabulary terms denote classes (S1,S2,S28); O specializes K. Disjointness concerns interpreted resources, not disjoint IRI strings.

**assumptions:** The carriers, equality and semantic environment are those of the SKOS basisScope.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference

**sourceLocator:** §3.3 S1; §4.3 S2; §4.4 S9; §§9.3–9.4 S28–S29, S37

**sourceNote:** Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.

**provenanceKind:** adapted

**reviewStatus:** Editorial formulation; no machine-checked claim witness.

**ruleRole:** structure-constraint

<a id="node-urn-csabs-axiom-SKOS-scheme-relations"></a>

### scheme-relations

`urn:csabs:axiom/SKOS-scheme-relations`

**statement:** Top-concept properties are inverse and imply scheme membership, with explicit endpoint typing.

**formalStatement:** P_inScheme⊆D×S; P_hasTopConcept⊆S×C; P_topConceptOf=(P_hasTopConcept)⁻¹; P_topConceptOf⊆P_inScheme.

**description:** S3 declares object properties. No domain of inScheme is imposed; labels and membership do not force Concept typing. A top concept need not lack broader neighbors; scheme membership does not propagate along broader.

**assumptions:** The carriers, equality and semantic environment are those of the SKOS basisScope.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference

**sourceLocator:** §§4.3–4.6 S3–S8; notes 4.6.1–4.6.5

**sourceNote:** Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.

**provenanceKind:** adapted

**reviewStatus:** Editorial formulation; no machine-checked claim witness.

**ruleRole:** structure-constraint

<a id="node-urn-csabs-axiom-SKOS-lexical-labels"></a>

### lexical-labels

`urn:csabs:axiom/SKOS-lexical-labels`

**statement:** Lexical labels have plain-literal values and are included in rdfs:label.

**formalStatement:** For p∈{prefLabel,altLabel,hiddenLabel}: P_p⊆D×Plain and P_p⊆P_rdfs:label.

**description:** S10 declares annotation properties; their subjects need not be concepts.

**assumptions:** The carriers, equality and semantic environment are those of the SKOS basisScope.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference

**sourceLocator:** §5.3 S10–S12; §5.6.1

**sourceNote:** Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.

**provenanceKind:** adapted

**reviewStatus:** Editorial formulation; no machine-checked claim witness.

**ruleRole:** structure-constraint

<a id="node-urn-csabs-axiom-SKOS-label-integrity"></a>

### label-integrity

`urn:csabs:axiom/SKOS-label-integrity`

**statement:** Label roles are pairwise disjoint, with at most one preferred label for each language key, including no tag.

**formalStatement:** P_prefLabel∩P_altLabel=P_prefLabel∩P_hiddenLabel=P_altLabel∩P_hiddenLabel=∅; ∀x a b, (P_prefLabel(x,a)∧P_prefLabel(x,b)∧lang(a)=lang(b))⇒a=b.

**description:** No preferred-label existence or global uniqueness across subjects is required. Language variants have separate keys; untagged labels use none.

**assumptions:** The carriers, equality and semantic environment are those of the SKOS basisScope.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference; [W3C SKOS Reference Errata](https://www.w3.org/2006/07/SWD/SKOS/reference/20090811-errata); accessedOn: 2026-11-19; sourceRole: consulted-normative-clarification

**sourceLocator:** §5.4 S13–S14; errata S14 (2 August 2011)

**sourceNote:** Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.

**provenanceKind:** adapted

**reviewStatus:** Editorial formulation; no machine-checked claim witness.

**ruleRole:** structure-constraint

<a id="node-urn-csabs-axiom-SKOS-notations-and-notes"></a>

### notations-and-notes

`urn:csabs:axiom/SKOS-notations-and-notes`

**statement:** Notation takes literal values; specialized documentation properties imply note.

**formalStatement:** P_notation⊆D×LV; for p∈{changeNote,definition,editorialNote,example,historyNote,scopeNote}, P_p⊆P_note; P_note⊆D×D.

**description:** S15 declares a datatype property, S16 annotation properties. Note values may be resources or literals; no Concept domain, notation cardinality or notation uniqueness is imposed. Custom datatype use is a convention.

**assumptions:** The carriers, equality and semantic environment are those of the SKOS basisScope.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference

**sourceLocator:** §6.3 S15; §§6.5.2–6.5.5; §7.3 S16–S17 and §7.5

**sourceNote:** Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.

**provenanceKind:** adapted

**reviewStatus:** Editorial formulation; no machine-checked claim witness.

**ruleRole:** structure-constraint

<a id="node-urn-csabs-axiom-SKOS-semantic-relations"></a>

### semantic-relations

`urn:csabs:axiom/SKOS-semantic-relations`

**statement:** Hierarchy and association use concept endpoints, specified inclusions and inverses, symmetry and transitivity.

**formalStatement:** P_semanticRelation⊆C×C; P_broader⊆P_broaderTransitive⊆P_semanticRelation; P_narrower⊆P_narrowerTransitive⊆P_semanticRelation; P_related⊆P_semanticRelation; P_narrower=(P_broader)⁻¹; P_narrowerTransitive=(P_broaderTransitive)⁻¹; P_related=(P_related)⁻¹; P_broaderTransitive∘P_broaderTransitive⊆P_broaderTransitive; P_narrowerTransitive∘P_narrowerTransitive⊆P_narrowerTransitive.

**description:** S18 declares object properties. Neither broader nor related is required to be transitive. Hierarchical cycles, self-links and multiple paths are permitted; antisymmetry and reflexivity are not required. Transitivity constrains the superrelations without defining them as least closures.

**assumptions:** The carriers, equality and semantic environment are those of the SKOS basisScope.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference

**sourceLocator:** §8.3 S18–S26; §§8.6.4–8.6.9

**sourceNote:** Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.

**provenanceKind:** adapted

**reviewStatus:** Editorial formulation; no machine-checked claim witness.

**ruleRole:** structure-constraint

<a id="node-urn-csabs-axiom-SKOS-hierarchy-association-disjointness"></a>

### hierarchy-association-disjointness

`urn:csabs:axiom/SKOS-hierarchy-association-disjointness`

**statement:** Associative links cannot also be transitive broader links.

**formalStatement:** P_related∩P_broaderTransitive=∅.

**description:** Clashes can follow from inferred, not merely asserted, hierarchical links.

**assumptions:** The carriers, equality and semantic environment are those of the SKOS basisScope.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference

**sourceLocator:** §8.4 S27; §8.6.10

**sourceNote:** Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.

**provenanceKind:** adapted

**reviewStatus:** Editorial formulation; no machine-checked claim witness.

**ruleRole:** structure-constraint

<a id="node-urn-csabs-axiom-SKOS-collection-relations"></a>

### collection-relations

`urn:csabs:axiom/SKOS-collection-relations`

**statement:** Collection membership has a union range; ordered list membership implies ordinary membership.

**formalStatement:** P_member⊆K×(C∪K); P_memberList⊆O×List; ∀c l m,(P_memberList(c,l)∧P_memberList(c,m))⇒l=m; ∀c l x,(P_memberList(c,l)∧item(l,x))⇒P_member(c,x).

**description:** List⊆D is the supplied rdf:List extension, and item is defined in basisScope. S30 declares object properties. Functionality identifies denotations of list heads; two RDF list names need not be distinct. No list existence, list well-formedness, unique sequence, converse membership equality, or prohibition of nested collections is assumed.

**assumptions:** The carriers, equality and semantic environment are those of the SKOS basisScope.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference

**sourceLocator:** §9.3 S30–S36; §§9.6.2–9.6.3

**sourceNote:** Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.

**provenanceKind:** adapted

**reviewStatus:** Editorial formulation; no machine-checked claim witness.

**ruleRole:** structure-constraint

<a id="node-urn-csabs-axiom-SKOS-mapping-relations"></a>

### mapping-relations

`urn:csabs:axiom/SKOS-mapping-relations`

**statement:** Mapping relations refine semantic relations and their specified hierarchy/association properties.

**formalStatement:** P_mappingRelation⊆P_semanticRelation; for p∈{closeMatch,broadMatch,narrowMatch,relatedMatch}: P_p⊆P_mappingRelation; P_broadMatch⊆P_broader; P_narrowMatch⊆P_narrower; P_relatedMatch⊆P_related; P_exactMatch⊆P_closeMatch; P_narrowMatch=(P_broadMatch)⁻¹; for p∈{relatedMatch,closeMatch,exactMatch}: P_p=(P_p)⁻¹; P_exactMatch∘P_exactMatch⊆P_exactMatch.

**description:** S38 declares object properties. Cross-scheme use is a convention, not a formal restriction. closeMatch and broadMatch are not required to be transitive; exactMatch is not identity, equivalentClass or equivalentProperty, and does not propagate arbitrary properties.

**assumptions:** The carriers, equality and semantic environment are those of the SKOS basisScope.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference

**sourceLocator:** §10.3 S38–S45; §§10.6.1, 10.6.3–10.6.8

**sourceNote:** Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.

**provenanceKind:** adapted

**reviewStatus:** Editorial formulation; no machine-checked claim witness.

**ruleRole:** structure-constraint

<a id="node-urn-csabs-axiom-SKOS-mapping-disjointness"></a>

### mapping-disjointness

`urn:csabs:axiom/SKOS-mapping-disjointness`

**statement:** Exact mappings cannot also be broad or associative mappings.

**formalStatement:** P_exactMatch∩P_broadMatch=∅; P_exactMatch∩P_relatedMatch=∅.

**description:** The inverse/symmetry rules also imply disjointness from narrowMatch.

**assumptions:** The carriers, equality and semantic environment are those of the SKOS basisScope.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference

**sourceLocator:** §10.4 S46

**sourceNote:** Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.

**provenanceKind:** adapted

**reviewStatus:** Editorial formulation; no machine-checked claim witness.

**ruleRole:** structure-constraint

## Laws

<a id="node-urn-csabs-law-SKOS-broader-path"></a>

### broader-path

`urn:csabs:law/SKOS-broader-path`

**statement:** Two broader edges imply a transitive broader edge, with typed endpoints.

**formalStatement:** ∀a b c,(P_broader(a,b)∧P_broader(b,c))⇒(P_broaderTransitive(a,c)∧a∈C∧c∈C).

**description:** A consequence of the hierarchy basis, not an axiom imposing transitivity on broader.

**assumptions:** The carriers, equality and semantic environment are those of the SKOS basisScope.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference

**sourceLocator:** §8.3 S19–S26; §8.6.6 Example 35

**sourceNote:** Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.

**provenanceKind:** derived

**reviewStatus:** Editorial formulation; no machine-checked claim witness.

**dependsOn:** [semantic-relations](SKOS.md#node-urn-csabs-axiom-SKOS-semantic-relations)

**proofSketch:** Include each broader edge in broaderTransitive, compose by its transitivity, and apply semanticRelation endpoint typing.

<a id="node-urn-csabs-law-SKOS-exact-match-support-reflexivity"></a>

### exact-match-support-reflexivity

`urn:csabs:law/SKOS-exact-match-support-reflexivity`

**statement:** An exact mapping forces a self mapping at each incident resource.

**formalStatement:** ∀a b,P_exactMatch(a,b)⇒(P_exactMatch(a,a)∧P_exactMatch(b,b)).

**description:** Reflexivity on the support of exactMatch does not imply reflexivity on all concepts.

**assumptions:** The carriers, equality and semantic environment are those of the SKOS basisScope.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference

**sourceLocator:** §10.6.6 Example 69; S44–S45

**sourceNote:** Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.

**provenanceKind:** derived

**reviewStatus:** Editorial formulation; no machine-checked claim witness.

**dependsOn:** [mapping-relations](SKOS.md#node-urn-csabs-axiom-SKOS-mapping-relations)

**proofSketch:** Symmetry gives the reverse pair; transitivity on each order of the pair gives both self pairs.

<a id="node-urn-csabs-law-SKOS-exact-narrow-disjointness"></a>

### exact-narrow-disjointness

`urn:csabs:law/SKOS-exact-narrow-disjointness`

**statement:** Exact and narrow mappings have no common ordered pair.

**formalStatement:** P_exactMatch∩P_narrowMatch=∅.

**description:** Derived inverse-direction integrity condition.

**assumptions:** The carriers, equality and semantic environment are those of the SKOS basisScope.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference

**sourceLocator:** §10.4 note following S46

**sourceNote:** Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.

**provenanceKind:** derived

**reviewStatus:** Editorial formulation; no machine-checked claim witness.

**dependsOn:** [mapping-relations](SKOS.md#node-urn-csabs-axiom-SKOS-mapping-relations); [mapping-disjointness](SKOS.md#node-urn-csabs-axiom-SKOS-mapping-disjointness)

**proofSketch:** A common pair reverses to an exact pair by symmetry and a broadMatch pair by inverse, contradicting S46.

<a id="node-urn-csabs-law-SKOS-indirect-association-clash"></a>

### indirect-association-clash

`urn:csabs:law/SKOS-indirect-association-clash`

**statement:** A broader path and a related edge between its endpoints cannot coexist in a model.

**formalStatement:** ¬∃a b c,(P_broader(a,b)∧P_broader(b,c)∧P_related(a,c)).

**description:** Explains why checking only asserted direct-edge clashes misses an inconsistency.

**assumptions:** The carriers, equality and semantic environment are those of the SKOS basisScope.

**source:** [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference

**sourceLocator:** §8.5 Examples 27–28

**sourceNote:** Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.

**provenanceKind:** derived

**reviewStatus:** Editorial formulation; no machine-checked claim witness.

**dependsOn:** [semantic-relations](SKOS.md#node-urn-csabs-axiom-SKOS-semantic-relations); [hierarchy-association-disjointness](SKOS.md#node-urn-csabs-axiom-SKOS-hierarchy-association-disjointness)

**proofSketch:** Inclusion and transitivity produce broaderTransitive(a,c); its overlap with related violates S27.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [W3C SKOS Simple Knowledge Organization System Reference (18 August 2009)](https://www.w3.org/TR/2009/REC-skos-reference-20090818/); accessedOn: 2026-11-19; sourceRole: consulted-normative-definition-and-integrity-reference
- [W3C SKOS Reference Errata](https://www.w3.org/2006/07/SWD/SKOS/reference/20090811-errata); accessedOn: 2026-11-19; sourceRole: consulted-normative-clarification

**sourceLocator:** §§1.3–1.5, 3–10 (S1–S46); errata entry S14 (2 August 2011)

**sourceNote:** Adapts the normative SKOS Core instance constraints to set/relation notation, retaining open-world and non-unique-name semantics; deliberately excludes full OWL Full metamodel semantics and SKOS-XL.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/SKOS",
    "type": "Concept",
    "shortForm": "SKOS",
    "fullName": "SKOS Core ontology (relational semantic presentation)",
    "category": [
      "urn:csabs:category/data-modelling",
      "urn:csabs:category/logic"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "An interpretation of the SKOS Core vocabulary for concepts, schemes, lexical labels, notations, notes, semantic relations, collections and concept mappings, with explicit inference conditions and integrity constraints.",
    "notation": "M=(D,C,S,K,O,(P_p)_p,…); M⊨T_SKOS; G⊨_SKOS φ iff every SKOS model of G satisfies φ",
    "requiresConcept": [
      "urn:csabs:concept/PredicateLogic",
      "urn:csabs:concept/Relation",
      "urn:csabs:concept/RDFGraph"
    ],
    "relatedConcept": [
      "urn:csabs:concept/Preorder",
      "urn:csabs:concept/EquivalenceRelation"
    ],
    "axiomBasis": "Instance-level relational translations of W3C SKOS Core S1–S46: class typing/disjointness; property domains/ranges, inclusions, inverses, symmetry, transitivity and functionality; label integrity; list-to-member implication. S14 includes untagged labels per the consulted errata.",
    "basisKind": "defined-structure",
    "basisScope": "Relational interpretation of SKOS Core S1–S46 at the instance level, with the S14 erratum. D is a nonempty resource domain including literal values; class extensions are subsets of D and property extensions subsets of D×D. C=Concept, S=ConceptScheme, K=Collection, O=OrderedCollection; P_p denotes the extension of property p, with skos: prefix omitted. RDF names denote resources without a unique-name assumption; model equality is resource identity, distinct from RDF term equality and exactMatch. Plain⊆D denotes 2009 RDF plain-literal values; lang:Plain→LanguageTag⊎{none} uses case-insensitive normalized tags; none is a separate language key. LV⊆D denotes literal values. RDF list typing and first/rest/nil interpretation are supplied by the RDF semantic environment; item(l,x) holds when x is a first value at a cell reachable from l by finitely many rest links. No finite-domain, closed-world, acyclicity, total labeling, unique notation, or single-scheme assumption. Empty class/property extensions and empty asserted graphs are allowed. This is an instance-level relational presentation, not an implementation of the complete RDF/RDFS/OWL Full metamodel or a claim of equivalence to it; SKOS-XL is excluded. Schema declarations retain their W3C locators; OWL class/property categories are recorded descriptively rather than reified in this first-order signature.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source and mathematical interface review; partial Lean interface; no compiled claim proof witness asserted.",
    "verificationObligation": [
      "Supply RDF/RDFS literal and list interpretation explicitly before interpreting concrete RDF graphs.",
      "Model-theoretic entailment and satisfiability are propositions, not decision procedures. An inconsistent graph entails every sentence classically.",
      "Do not infer a partial order, universal reflexivity of exactMatch, resource identity from exactMatch, or closed-world completeness.",
      "No specializationOf link to RDFGraph, Preorder or EquivalenceRelation: graph representation, transitive hierarchy and symmetric-transitive matching do not instantiate those entire interfaces."
    ],
    "mathematicalFormulation": "Relational interpretation of SKOS Core S1–S46 at the instance level, with the S14 erratum. D is a nonempty resource domain including literal values; class extensions are subsets of D and property extensions subsets of D×D. C=Concept, S=ConceptScheme, K=Collection, O=OrderedCollection; P_p denotes the extension of property p, with skos: prefix omitted. RDF names denote resources without a unique-name assumption; model equality is resource identity, distinct from RDF term equality and exactMatch. Plain⊆D denotes 2009 RDF plain-literal values; lang:Plain→LanguageTag⊎{none} uses case-insensitive normalized tags; none is a separate language key. LV⊆D denotes literal values. RDF list typing and first/rest/nil interpretation are supplied by the RDF semantic environment; item(l,x) holds when x is a first value at a cell reachable from l by finitely many rest links. No finite-domain, closed-world, acyclicity, total labeling, unique notation, or single-scheme assumption. Empty class/property extensions and empty asserted graphs are allowed. This is an instance-level relational presentation, not an implementation of the complete RDF/RDFS/OWL Full metamodel or a claim of equivalence to it; SKOS-XL is excluded. Schema declarations retain their W3C locators; OWL class/property categories are recorded descriptively rather than reified in this first-order signature. Let T_SKOS be the conjunction of the defining rules below. A graph G is satisfiable when ∃M, M⊨T_SKOS∧G; G⊨_SKOS φ iff ∀M,(M⊨T_SKOS∧G⇒M⊨φ). Blank nodes are existentially interpreted, not fixed global names. Transitive superrelations need not equal the least transitive closure of asserted broader edges.",
    "source": [
      "urn:csabs:source/w3c-skos-reference",
      "urn:csabs:source/w3c-skos-errata"
    ],
    "sourceLocator": "§§1.3–1.5, 3–10 (S1–S46); errata entry S14 (2 August 2011)",
    "sourceNote": "Adapts the normative SKOS Core instance constraints to set/relation notation, retaining open-world and non-unique-name semantics; deliberately excludes full OWL Full metamodel semantics and SKOS-XL.",
    "provenanceKind": "adapted",
    "formulationSource": "urn:csabs:source/local-lean-skos",
    "formulationLocator": "Catalog.SKOS",
    "formulationScope": "partial",
    "leanFormulation": "structure SKOS (D : Type u) [Nonempty D] where\n  concept : D → Prop\n  broader : D → D → Prop\n  narrower : D → D → Prop\n  broaderTransitive : D → D → Prop\n  related : D → D → Prop\n  exactMatch : D → D → Prop\n  broaderTyping : ∀ x y, broader x y → concept x ∧ concept y\n  transitiveTyping : ∀ x y, broaderTransitive x y → concept x ∧ concept y\n  relatedTyping : ∀ x y, related x y → concept x ∧ concept y\n  exactTyping : ∀ x y, exactMatch x y → concept x ∧ concept y\n  inverseHierarchy : ∀ x y, narrower x y ↔ broader y x\n  hierarchyInclusion : ∀ x y, broader x y → broaderTransitive x y\n  hierarchyTransitivity : ∀ x y z,\n    broaderTransitive x y → broaderTransitive y z → broaderTransitive x z\n  relatedSymmetry : ∀ x y, related x y → related y x\n  hierarchyDisjointness : ∀ x y, related x y → ¬ broaderTransitive x y\n  exactSymmetry : ∀ x y, exactMatch x y → exactMatch y x\n  exactTransitivity : ∀ x y z, exactMatch x y → exactMatch y z → exactMatch x z",
    "leanModelMapping": "D is a nonempty domain of interpreted resources with identity equality. concept and the five binary relations interpret the corresponding SKOS extensions. The fields encode selected typing, inverse, inclusion, symmetry, transitivity and disjointness conditions from S19–S27 and S44–S45.",
    "leanModelLimitations": "Partial semantic-relation interface only. No labels, schemes, collections, full mapping hierarchy, RDF parser/interpretation, OWL Full metamodel, or general entailment solver. Structure law fields constrain inputs; no model-satisfaction theorem or catalog claim proof witness is registered.",
    "hasAxiom": [
      "urn:csabs:axiom/SKOS-class-integrity",
      "urn:csabs:axiom/SKOS-scheme-relations",
      "urn:csabs:axiom/SKOS-lexical-labels",
      "urn:csabs:axiom/SKOS-label-integrity",
      "urn:csabs:axiom/SKOS-notations-and-notes",
      "urn:csabs:axiom/SKOS-semantic-relations",
      "urn:csabs:axiom/SKOS-hierarchy-association-disjointness",
      "urn:csabs:axiom/SKOS-collection-relations",
      "urn:csabs:axiom/SKOS-mapping-relations",
      "urn:csabs:axiom/SKOS-mapping-disjointness"
    ],
    "hasLaw": [
      "urn:csabs:law/SKOS-broader-path",
      "urn:csabs:law/SKOS-exact-match-support-reflexivity",
      "urn:csabs:law/SKOS-exact-narrow-disjointness",
      "urn:csabs:law/SKOS-indirect-association-clash"
    ],
    "hasOperation": [
      "urn:csabs:operation/SKOS-class-extension",
      "urn:csabs:operation/SKOS-property-extension",
      "urn:csabs:operation/SKOS-satisfies",
      "urn:csabs:operation/SKOS-satisfiable",
      "urn:csabs:operation/SKOS-entails"
    ],
    "hasTheorem": []
  },
  {
    "id": "urn:csabs:operation/SKOS-class-extension",
    "type": "Operation",
    "name": "class-extension",
    "signature": "classExtension : Interpretation×SKOSClass→𝒫(D)",
    "description": "Returns the interpreted extension of Concept, ConceptScheme, Collection or OrderedCollection.",
    "concept": "urn:csabs:concept/SKOS",
    "precondition": "M interprets the selected class.",
    "totality": "Total mathematical query on the stated domain; no algorithm or decidability guarantee.",
    "outcome": "The corresponding subset of D.",
    "source": [
      "urn:csabs:source/w3c-skos-reference"
    ],
    "sourceLocator": "§§3.3,4.3,9.3",
    "sourceNote": "Abstract query interface adapted from SKOS interpretation and entailment semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/SKOS-property-extension",
    "type": "Operation",
    "name": "property-extension",
    "signature": "propertyExtension : Interpretation×SKOSProperty→𝒫(D×D)",
    "description": "Returns the interpreted relation of any Core property, including label, notation and documentation properties.",
    "concept": "urn:csabs:concept/SKOS",
    "precondition": "M interprets the selected property.",
    "totality": "Total mathematical query on the stated domain; no algorithm or decidability guarantee.",
    "outcome": "The corresponding relation on resources, subject to the relevant basis rules.",
    "source": [
      "urn:csabs:source/w3c-skos-reference"
    ],
    "sourceLocator": "§§4.3–10.4",
    "sourceNote": "Abstract query interface adapted from SKOS interpretation and entailment semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/SKOS-satisfies",
    "type": "Operation",
    "name": "satisfies",
    "signature": "satisfies : Interpretation×RDFGraph→Prop",
    "description": "Tests satisfaction mathematically under the supplied RDF interpretation, rather than checking literal triple membership.",
    "concept": "urn:csabs:concept/SKOS",
    "precondition": "Fixed interpretation of IRIs, literals, RDF typing/list vocabulary and SKOS terms; blank-node assignment is existential.",
    "totality": "Total mathematical query on the stated domain; no algorithm or decidability guarantee.",
    "outcome": "True iff M satisfies T_SKOS and some blank-node assignment makes every asserted triple true.",
    "source": [
      "urn:csabs:source/w3c-skos-reference"
    ],
    "sourceLocator": "§§1.3–1.5",
    "sourceNote": "Abstract query interface adapted from SKOS interpretation and entailment semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/SKOS-satisfiable",
    "type": "Operation",
    "name": "satisfiable",
    "signature": "satisfiable : RDFGraph→Prop",
    "description": "Asks whether any interpretation satisfies the graph and the stated SKOS instance constraints.",
    "concept": "urn:csabs:concept/SKOS",
    "precondition": "The RDF semantic environment and profile are fixed.",
    "totality": "Total mathematical query on the stated domain; no algorithm or decidability guarantee.",
    "outcome": "∃M, satisfies(M,G). Missing labels/types are not by themselves violations.",
    "source": [
      "urn:csabs:source/w3c-skos-reference"
    ],
    "sourceLocator": "§§1.4–1.5",
    "sourceNote": "Abstract query interface adapted from SKOS interpretation and entailment semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/SKOS-entails",
    "type": "Operation",
    "name": "entails",
    "signature": "entails : RDFGraph×Sentence→Prop",
    "description": "Defines model-theoretic consequence for the stated profile.",
    "concept": "urn:csabs:concept/SKOS",
    "precondition": "The sentence and graph use the fixed interpreted vocabulary; this is not a full OWL Full reasoner.",
    "totality": "Total mathematical query on the stated domain; no algorithm or decidability guarantee.",
    "outcome": "∀M, satisfies(M,G)⇒M⊨φ. Unsatisfiable inputs entail every sentence classically.",
    "source": [
      "urn:csabs:source/w3c-skos-reference"
    ],
    "sourceLocator": "§§1.4–1.5",
    "sourceNote": "Abstract query interface adapted from SKOS interpretation and entailment semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/SKOS-class-integrity",
    "type": "Axiom",
    "name": "class-integrity",
    "statement": "Concepts, schemes and collections have disjoint extensions; ordered collections are collections.",
    "formalStatement": "C,S,K,O⊆D; C∩S=C∩K=S∩K=∅; O⊆K.",
    "description": "The four vocabulary terms denote classes (S1,S2,S28); O specializes K. Disjointness concerns interpreted resources, not disjoint IRI strings.",
    "assumptions": [
      "The carriers, equality and semantic environment are those of the SKOS basisScope."
    ],
    "appliesTo": [
      "urn:csabs:concept/SKOS"
    ],
    "source": [
      "urn:csabs:source/w3c-skos-reference"
    ],
    "sourceLocator": "§3.3 S1; §4.3 S2; §4.4 S9; §§9.3–9.4 S28–S29, S37",
    "sourceNote": "Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial formulation; no machine-checked claim witness.",
    "ruleRole": "structure-constraint"
  },
  {
    "id": "urn:csabs:axiom/SKOS-scheme-relations",
    "type": "Axiom",
    "name": "scheme-relations",
    "statement": "Top-concept properties are inverse and imply scheme membership, with explicit endpoint typing.",
    "formalStatement": "P_inScheme⊆D×S; P_hasTopConcept⊆S×C; P_topConceptOf=(P_hasTopConcept)⁻¹; P_topConceptOf⊆P_inScheme.",
    "description": "S3 declares object properties. No domain of inScheme is imposed; labels and membership do not force Concept typing. A top concept need not lack broader neighbors; scheme membership does not propagate along broader.",
    "assumptions": [
      "The carriers, equality and semantic environment are those of the SKOS basisScope."
    ],
    "appliesTo": [
      "urn:csabs:concept/SKOS"
    ],
    "source": [
      "urn:csabs:source/w3c-skos-reference"
    ],
    "sourceLocator": "§§4.3–4.6 S3–S8; notes 4.6.1–4.6.5",
    "sourceNote": "Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial formulation; no machine-checked claim witness.",
    "ruleRole": "structure-constraint"
  },
  {
    "id": "urn:csabs:axiom/SKOS-lexical-labels",
    "type": "Axiom",
    "name": "lexical-labels",
    "statement": "Lexical labels have plain-literal values and are included in rdfs:label.",
    "formalStatement": "For p∈{prefLabel,altLabel,hiddenLabel}: P_p⊆D×Plain and P_p⊆P_rdfs:label.",
    "description": "S10 declares annotation properties; their subjects need not be concepts.",
    "assumptions": [
      "The carriers, equality and semantic environment are those of the SKOS basisScope."
    ],
    "appliesTo": [
      "urn:csabs:concept/SKOS"
    ],
    "source": [
      "urn:csabs:source/w3c-skos-reference"
    ],
    "sourceLocator": "§5.3 S10–S12; §5.6.1",
    "sourceNote": "Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial formulation; no machine-checked claim witness.",
    "ruleRole": "structure-constraint"
  },
  {
    "id": "urn:csabs:axiom/SKOS-label-integrity",
    "type": "Axiom",
    "name": "label-integrity",
    "statement": "Label roles are pairwise disjoint, with at most one preferred label for each language key, including no tag.",
    "formalStatement": "P_prefLabel∩P_altLabel=P_prefLabel∩P_hiddenLabel=P_altLabel∩P_hiddenLabel=∅; ∀x a b, (P_prefLabel(x,a)∧P_prefLabel(x,b)∧lang(a)=lang(b))⇒a=b.",
    "description": "No preferred-label existence or global uniqueness across subjects is required. Language variants have separate keys; untagged labels use none.",
    "assumptions": [
      "The carriers, equality and semantic environment are those of the SKOS basisScope."
    ],
    "appliesTo": [
      "urn:csabs:concept/SKOS"
    ],
    "source": [
      "urn:csabs:source/w3c-skos-reference",
      "urn:csabs:source/w3c-skos-errata"
    ],
    "sourceLocator": "§5.4 S13–S14; errata S14 (2 August 2011)",
    "sourceNote": "Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial formulation; no machine-checked claim witness.",
    "ruleRole": "structure-constraint"
  },
  {
    "id": "urn:csabs:axiom/SKOS-notations-and-notes",
    "type": "Axiom",
    "name": "notations-and-notes",
    "statement": "Notation takes literal values; specialized documentation properties imply note.",
    "formalStatement": "P_notation⊆D×LV; for p∈{changeNote,definition,editorialNote,example,historyNote,scopeNote}, P_p⊆P_note; P_note⊆D×D.",
    "description": "S15 declares a datatype property, S16 annotation properties. Note values may be resources or literals; no Concept domain, notation cardinality or notation uniqueness is imposed. Custom datatype use is a convention.",
    "assumptions": [
      "The carriers, equality and semantic environment are those of the SKOS basisScope."
    ],
    "appliesTo": [
      "urn:csabs:concept/SKOS"
    ],
    "source": [
      "urn:csabs:source/w3c-skos-reference"
    ],
    "sourceLocator": "§6.3 S15; §§6.5.2–6.5.5; §7.3 S16–S17 and §7.5",
    "sourceNote": "Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial formulation; no machine-checked claim witness.",
    "ruleRole": "structure-constraint"
  },
  {
    "id": "urn:csabs:axiom/SKOS-semantic-relations",
    "type": "Axiom",
    "name": "semantic-relations",
    "statement": "Hierarchy and association use concept endpoints, specified inclusions and inverses, symmetry and transitivity.",
    "formalStatement": "P_semanticRelation⊆C×C; P_broader⊆P_broaderTransitive⊆P_semanticRelation; P_narrower⊆P_narrowerTransitive⊆P_semanticRelation; P_related⊆P_semanticRelation; P_narrower=(P_broader)⁻¹; P_narrowerTransitive=(P_broaderTransitive)⁻¹; P_related=(P_related)⁻¹; P_broaderTransitive∘P_broaderTransitive⊆P_broaderTransitive; P_narrowerTransitive∘P_narrowerTransitive⊆P_narrowerTransitive.",
    "description": "S18 declares object properties. Neither broader nor related is required to be transitive. Hierarchical cycles, self-links and multiple paths are permitted; antisymmetry and reflexivity are not required. Transitivity constrains the superrelations without defining them as least closures.",
    "assumptions": [
      "The carriers, equality and semantic environment are those of the SKOS basisScope."
    ],
    "appliesTo": [
      "urn:csabs:concept/SKOS"
    ],
    "source": [
      "urn:csabs:source/w3c-skos-reference"
    ],
    "sourceLocator": "§8.3 S18–S26; §§8.6.4–8.6.9",
    "sourceNote": "Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial formulation; no machine-checked claim witness.",
    "ruleRole": "structure-constraint"
  },
  {
    "id": "urn:csabs:axiom/SKOS-hierarchy-association-disjointness",
    "type": "Axiom",
    "name": "hierarchy-association-disjointness",
    "statement": "Associative links cannot also be transitive broader links.",
    "formalStatement": "P_related∩P_broaderTransitive=∅.",
    "description": "Clashes can follow from inferred, not merely asserted, hierarchical links.",
    "assumptions": [
      "The carriers, equality and semantic environment are those of the SKOS basisScope."
    ],
    "appliesTo": [
      "urn:csabs:concept/SKOS"
    ],
    "source": [
      "urn:csabs:source/w3c-skos-reference"
    ],
    "sourceLocator": "§8.4 S27; §8.6.10",
    "sourceNote": "Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial formulation; no machine-checked claim witness.",
    "ruleRole": "structure-constraint"
  },
  {
    "id": "urn:csabs:axiom/SKOS-collection-relations",
    "type": "Axiom",
    "name": "collection-relations",
    "statement": "Collection membership has a union range; ordered list membership implies ordinary membership.",
    "formalStatement": "P_member⊆K×(C∪K); P_memberList⊆O×List; ∀c l m,(P_memberList(c,l)∧P_memberList(c,m))⇒l=m; ∀c l x,(P_memberList(c,l)∧item(l,x))⇒P_member(c,x).",
    "description": "List⊆D is the supplied rdf:List extension, and item is defined in basisScope. S30 declares object properties. Functionality identifies denotations of list heads; two RDF list names need not be distinct. No list existence, list well-formedness, unique sequence, converse membership equality, or prohibition of nested collections is assumed.",
    "assumptions": [
      "The carriers, equality and semantic environment are those of the SKOS basisScope."
    ],
    "appliesTo": [
      "urn:csabs:concept/SKOS"
    ],
    "source": [
      "urn:csabs:source/w3c-skos-reference"
    ],
    "sourceLocator": "§9.3 S30–S36; §§9.6.2–9.6.3",
    "sourceNote": "Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial formulation; no machine-checked claim witness.",
    "ruleRole": "structure-constraint"
  },
  {
    "id": "urn:csabs:axiom/SKOS-mapping-relations",
    "type": "Axiom",
    "name": "mapping-relations",
    "statement": "Mapping relations refine semantic relations and their specified hierarchy/association properties.",
    "formalStatement": "P_mappingRelation⊆P_semanticRelation; for p∈{closeMatch,broadMatch,narrowMatch,relatedMatch}: P_p⊆P_mappingRelation; P_broadMatch⊆P_broader; P_narrowMatch⊆P_narrower; P_relatedMatch⊆P_related; P_exactMatch⊆P_closeMatch; P_narrowMatch=(P_broadMatch)⁻¹; for p∈{relatedMatch,closeMatch,exactMatch}: P_p=(P_p)⁻¹; P_exactMatch∘P_exactMatch⊆P_exactMatch.",
    "description": "S38 declares object properties. Cross-scheme use is a convention, not a formal restriction. closeMatch and broadMatch are not required to be transitive; exactMatch is not identity, equivalentClass or equivalentProperty, and does not propagate arbitrary properties.",
    "assumptions": [
      "The carriers, equality and semantic environment are those of the SKOS basisScope."
    ],
    "appliesTo": [
      "urn:csabs:concept/SKOS"
    ],
    "source": [
      "urn:csabs:source/w3c-skos-reference"
    ],
    "sourceLocator": "§10.3 S38–S45; §§10.6.1, 10.6.3–10.6.8",
    "sourceNote": "Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial formulation; no machine-checked claim witness.",
    "ruleRole": "structure-constraint"
  },
  {
    "id": "urn:csabs:axiom/SKOS-mapping-disjointness",
    "type": "Axiom",
    "name": "mapping-disjointness",
    "statement": "Exact mappings cannot also be broad or associative mappings.",
    "formalStatement": "P_exactMatch∩P_broadMatch=∅; P_exactMatch∩P_relatedMatch=∅.",
    "description": "The inverse/symmetry rules also imply disjointness from narrowMatch.",
    "assumptions": [
      "The carriers, equality and semantic environment are those of the SKOS basisScope."
    ],
    "appliesTo": [
      "urn:csabs:concept/SKOS"
    ],
    "source": [
      "urn:csabs:source/w3c-skos-reference"
    ],
    "sourceLocator": "§10.4 S46",
    "sourceNote": "Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial formulation; no machine-checked claim witness.",
    "ruleRole": "structure-constraint"
  },
  {
    "id": "urn:csabs:law/SKOS-broader-path",
    "type": "Law",
    "name": "broader-path",
    "statement": "Two broader edges imply a transitive broader edge, with typed endpoints.",
    "formalStatement": "∀a b c,(P_broader(a,b)∧P_broader(b,c))⇒(P_broaderTransitive(a,c)∧a∈C∧c∈C).",
    "description": "A consequence of the hierarchy basis, not an axiom imposing transitivity on broader.",
    "assumptions": [
      "The carriers, equality and semantic environment are those of the SKOS basisScope."
    ],
    "appliesTo": [
      "urn:csabs:concept/SKOS"
    ],
    "source": [
      "urn:csabs:source/w3c-skos-reference"
    ],
    "sourceLocator": "§8.3 S19–S26; §8.6.6 Example 35",
    "sourceNote": "Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial formulation; no machine-checked claim witness.",
    "dependsOn": [
      "urn:csabs:axiom/SKOS-semantic-relations"
    ],
    "proofSketch": "Include each broader edge in broaderTransitive, compose by its transitivity, and apply semanticRelation endpoint typing."
  },
  {
    "id": "urn:csabs:law/SKOS-exact-match-support-reflexivity",
    "type": "Law",
    "name": "exact-match-support-reflexivity",
    "statement": "An exact mapping forces a self mapping at each incident resource.",
    "formalStatement": "∀a b,P_exactMatch(a,b)⇒(P_exactMatch(a,a)∧P_exactMatch(b,b)).",
    "description": "Reflexivity on the support of exactMatch does not imply reflexivity on all concepts.",
    "assumptions": [
      "The carriers, equality and semantic environment are those of the SKOS basisScope."
    ],
    "appliesTo": [
      "urn:csabs:concept/SKOS"
    ],
    "source": [
      "urn:csabs:source/w3c-skos-reference"
    ],
    "sourceLocator": "§10.6.6 Example 69; S44–S45",
    "sourceNote": "Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial formulation; no machine-checked claim witness.",
    "dependsOn": [
      "urn:csabs:axiom/SKOS-mapping-relations"
    ],
    "proofSketch": "Symmetry gives the reverse pair; transitivity on each order of the pair gives both self pairs."
  },
  {
    "id": "urn:csabs:law/SKOS-exact-narrow-disjointness",
    "type": "Law",
    "name": "exact-narrow-disjointness",
    "statement": "Exact and narrow mappings have no common ordered pair.",
    "formalStatement": "P_exactMatch∩P_narrowMatch=∅.",
    "description": "Derived inverse-direction integrity condition.",
    "assumptions": [
      "The carriers, equality and semantic environment are those of the SKOS basisScope."
    ],
    "appliesTo": [
      "urn:csabs:concept/SKOS"
    ],
    "source": [
      "urn:csabs:source/w3c-skos-reference"
    ],
    "sourceLocator": "§10.4 note following S46",
    "sourceNote": "Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial formulation; no machine-checked claim witness.",
    "dependsOn": [
      "urn:csabs:axiom/SKOS-mapping-relations",
      "urn:csabs:axiom/SKOS-mapping-disjointness"
    ],
    "proofSketch": "A common pair reverses to an exact pair by symmetry and a broadMatch pair by inverse, contradicting S46."
  },
  {
    "id": "urn:csabs:law/SKOS-indirect-association-clash",
    "type": "Law",
    "name": "indirect-association-clash",
    "statement": "A broader path and a related edge between its endpoints cannot coexist in a model.",
    "formalStatement": "¬∃a b c,(P_broader(a,b)∧P_broader(b,c)∧P_related(a,c)).",
    "description": "Explains why checking only asserted direct-edge clashes misses an inconsistency.",
    "assumptions": [
      "The carriers, equality and semantic environment are those of the SKOS basisScope."
    ],
    "appliesTo": [
      "urn:csabs:concept/SKOS"
    ],
    "source": [
      "urn:csabs:source/w3c-skos-reference"
    ],
    "sourceLocator": "§8.5 Examples 27–28",
    "sourceNote": "Relational presentation of the cited conditions; no extra closed-world or hierarchy constraint is added.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial formulation; no machine-checked claim witness.",
    "dependsOn": [
      "urn:csabs:axiom/SKOS-semantic-relations",
      "urn:csabs:axiom/SKOS-hierarchy-association-disjointness"
    ],
    "proofSketch": "Inclusion and transitivity produce broaderTransitive(a,c); its overlap with related violates S27."
  }
]
```
<!-- graph-record:end -->
