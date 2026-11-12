# Candidate key relative to functional dependencies

An inclusion-minimal attribute set whose agreement identifies an entire row in every instance permitted by the declared functional dependencies.

**Notation:** Key_F(K) iff F⊨K→U ∧ ∀J⊊K: F⊭J→U

**Stable ID:** `urn:csabs:concept/CandidateKey`

**Categories:** Relational data modelling

**Kind:** principle

**Prerequisites:** [Functional dependency on a relational schema](FunctionalDependency.md)

**Related concepts:** [Named relational schema with attribute domains](RelationalSchema.md), [Map](Map.md)

## Backlinks

- [Functional dependency on a relational schema](FunctionalDependency.md) — `relatedConcept`

## Mathematical formulation

Relative to an FD theory F, K is a candidate key iff F⊨K→Attr and ∀J⊊K,F⊭J→Attr, where entailment quantifies over all finite instances satisfying F. Minimality is by inclusion, not minimum cardinality.

**Lean formulation** (in its source module context):

```lean
def CandidateKey {s : RelationalSchema} (F : _root_.Set (FD s))
    (K : _root_.Set s.Attribute) : Prop :=
  impliesFD F (K, _root_.Set.univ) ∧
    ∀ J, J ⊂ K → ¬ impliesFD F (J, _root_.Set.univ)
```

**Source:** [`Catalog.CandidateKey`](../lean/Catalog/Database.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Minimal superkey relative to explicit FD theory, with semantic implication over all finite instances.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected defining presentation: A candidate key is an inclusion-minimal superkey.

**basisKind:** defined-structure

**basisScope:** U is finite, possibly empty; F is a set of FDs over the fixed schema. Empty keys are allowed. Minimality uses proper subsets. No SQL primary-key selection or NULL convention is added.

**verificationObligation:** U is finite, possibly empty; F is a set of FDs over the fixed schema. Empty keys are allowed. Minimality uses proper subsets. No SQL primary-key selection or NULL convention is added.

**reviewStatus:** editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-CandidateKey-isSuperkey"></a>

### isSuperkey

`urn:csabs:operation/CandidateKey-isSuperkey`

**signature:** isSuperkey_F : 𝒫(U)→Prop

**description:** Tests semantic determination of all attributes under F.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Tests semantic determination of all attributes under F.

<a id="node-urn-csabs-operation-CandidateKey-isCandidateKey"></a>

### isCandidateKey

`urn:csabs:operation/CandidateKey-isCandidateKey`

**signature:** isCandidateKey_F : 𝒫(U)→Prop

**description:** Tests superkeyhood and inclusion minimality.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Tests superkeyhood and inclusion minimality.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-CandidateKey-key-definition"></a>

### key-definition

`urn:csabs:axiom/CandidateKey-key-definition`

**statement:** A candidate key is an inclusion-minimal superkey.

**description:** A candidate key is an inclusion-minimal superkey.

**formalStatement:** Super_F(K) iff F⊨K→U; Key_F(K) iff Super_F(K) ∧ ∀J⊊K:¬Super_F(J)

**assumptions:** U is finite, possibly empty; F is a set of FDs over the fixed schema. Empty keys are allowed. Minimality uses proper subsets. No SQL primary-key selection or NULL convention is added.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §11.2, p. 257, superkeys and keys before Definition 11.2.11

**sourceNote:** Records the source key as a candidate key, with inclusion-minimal rather than minimum-cardinality meaning. It is not inferred solely from an observed instance. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-CandidateKey-superkey-upward-closure"></a>

### superkey-upward-closure

`urn:csabs:law/CandidateKey-superkey-upward-closure`

**statement:** Every superset of a superkey is a superkey.

**description:** Every superset of a superkey is a superkey.

**formalStatement:** Super_F(K) ∧ K⊆J⊆U ⇒ Super_F(J)

**assumptions:** U is finite, possibly empty; F is a set of FDs over the fixed schema. Empty keys are allowed. Minimality uses proper subsets. No SQL primary-key selection or NULL convention is added.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §11.2, p. 257, superkeys and keys before Definition 11.2.11

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Two rows agreeing on J agree on K and therefore on U in every F-model.

**dependsOn:** [key-definition](CandidateKey.md#node-urn-csabs-axiom-CandidateKey-key-definition); [satisfaction](FunctionalDependency.md#node-urn-csabs-axiom-FunctionalDependency-satisfaction); [implication](FunctionalDependency.md#node-urn-csabs-axiom-FunctionalDependency-implication)

<a id="node-urn-csabs-law-CandidateKey-key-antichain"></a>

### key-antichain

`urn:csabs:law/CandidateKey-key-antichain`

**statement:** Distinct candidate keys cannot properly contain one another.

**description:** Distinct candidate keys cannot properly contain one another.

**formalStatement:** Key_F(K) ∧ Key_F(J) ∧ K⊆J ⇒ K=J

**assumptions:** U is finite, possibly empty; F is a set of FDs over the fixed schema. Empty keys are allowed. Minimality uses proper subsets. No SQL primary-key selection or NULL convention is added.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §11.2, p. 257, superkeys and keys before Definition 11.2.11

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** If inclusion were proper, J would have the proper superkey subset K, contradicting its defining minimality.

**dependsOn:** [key-definition](CandidateKey.md#node-urn-csabs-axiom-CandidateKey-key-definition)

## Theorems

<a id="node-urn-csabs-theorem-CandidateKey-key-existence"></a>

### key-existence

`urn:csabs:theorem/CandidateKey-key-existence`

**statement:** Every superkey contains a candidate key.

**description:** Every superkey contains a candidate key.

**formalStatement:** Super_F(K) ⇒ ∃J⊆K:Key_F(J)

**assumptions:** U is finite, possibly empty; F is a set of FDs over the fixed schema. Empty keys are allowed. Minimality uses proper subsets. No SQL primary-key selection or NULL convention is added.

**ruleRole:** derived-result

**proofSketch:** The collection of superkey subsets of K is finite and nonempty because it contains K. Choose one of least cardinality; a proper superkey subset would contradict that choice. U is always a superkey by FD reflexivity.

**dependsOn:** [key-definition](CandidateKey.md#node-urn-csabs-axiom-CandidateKey-key-definition); [implication](FunctionalDependency.md#node-urn-csabs-axiom-FunctionalDependency-implication); [armstrong-soundness](FunctionalDependency.md#node-urn-csabs-theorem-FunctionalDependency-armstrong-soundness)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §11.2, p. 257, superkeys and keys before Definition 11.2.11

**sourceNote:** Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-CandidateKey-key-projection-injective"></a>

### key-projection-injective

`urn:csabs:theorem/CandidateKey-key-projection-injective`

**statement:** A candidate key projects distinct rows to distinct key tuples in every permitted instance.

**description:** A candidate key projects distinct rows to distinct key tuples in every permitted instance.

**formalStatement:** Key_F(K) ∧ r⊨F ∧ s,t∈r ∧ s|K=t|K ⇒ s=t

**assumptions:** U is finite, possibly empty; F is a set of FDs over the fixed schema. Empty keys are allowed. Minimality uses proper subsets. No SQL primary-key selection or NULL convention is added.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §11.2, p. 257, superkeys and keys before Definition 11.2.11

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Keyhood implies F⊨K→U. Apply it to the permitted instance and the two rows, then use componentwise tuple equality.

**dependsOn:** [key-definition](CandidateKey.md#node-urn-csabs-axiom-CandidateKey-key-definition); [implication](FunctionalDependency.md#node-urn-csabs-axiom-FunctionalDependency-implication); [satisfaction](FunctionalDependency.md#node-urn-csabs-axiom-FunctionalDependency-satisfaction); [tuple-extensionality](RelationalSchema.md#node-urn-csabs-axiom-RelationalSchema-tuple-extensionality)

## Concept provenance

- [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §11.2, p. 257, superkeys and keys before Definition 11.2.11

**sourceNote:** Records the source key as a candidate key, with inclusion-minimal rather than minimum-cardinality meaning. It is not inferred solely from an observed instance.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/CandidateKey",
    "type": "Concept",
    "shortForm": "CandidateKey",
    "fullName": "Candidate key relative to functional dependencies",
    "category": [
      "urn:csabs:category/data-modelling"
    ],
    "kind": "urn:csabs:kind/principle",
    "definition": "An inclusion-minimal attribute set whose agreement identifies an entire row in every instance permitted by the declared functional dependencies.",
    "notation": "Key_F(K) iff F⊨K→U ∧ ∀J⊊K: F⊭J→U",
    "hasOperation": [
      "urn:csabs:operation/CandidateKey-isSuperkey",
      "urn:csabs:operation/CandidateKey-isCandidateKey"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/CandidateKey-key-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/CandidateKey-superkey-upward-closure",
      "urn:csabs:law/CandidateKey-key-antichain"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/CandidateKey-key-existence",
      "urn:csabs:theorem/CandidateKey-key-projection-injective"
    ],
    "requiresConcept": [
      "urn:csabs:concept/FunctionalDependency"
    ],
    "relatedConcept": [
      "urn:csabs:concept/RelationalSchema",
      "urn:csabs:concept/Map"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Selected defining presentation: A candidate key is an inclusion-minimal superkey.",
    "basisKind": "defined-structure",
    "basisScope": "U is finite, possibly empty; F is a set of FDs over the fixed schema. Empty keys are allowed. Minimality uses proper subsets. No SQL primary-key selection or NULL convention is added.",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§11.2, p. 257, superkeys and keys before Definition 11.2.11",
    "sourceNote": "Records the source key as a candidate key, with inclusion-minimal rather than minimum-cardinality meaning. It is not inferred solely from an observed instance.",
    "provenanceKind": "adapted",
    "reviewStatus": "editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof",
    "verificationObligation": [
      "U is finite, possibly empty; F is a set of FDs over the fixed schema. Empty keys are allowed. Minimality uses proper subsets. No SQL primary-key selection or NULL convention is added."
    ],
    "leanFormulation": "def CandidateKey {s : RelationalSchema} (F : _root_.Set (FD s))\n    (K : _root_.Set s.Attribute) : Prop :=\n  impliesFD F (K, _root_.Set.univ) ∧\n    ∀ J, J ⊂ K → ¬ impliesFD F (J, _root_.Set.univ)",
    "formulationSource": "urn:csabs:source/local-lean-Database",
    "formulationLocator": "Catalog.CandidateKey",
    "formulationScope": "model",
    "leanModelMapping": "Minimal superkey relative to explicit FD theory, with semantic implication over all finite instances.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "Relative to an FD theory F, K is a candidate key iff F⊨K→Attr and ∀J⊊K,F⊭J→Attr, where entailment quantifies over all finite instances satisfying F. Minimality is by inclusion, not minimum cardinality."
  },
  {
    "id": "urn:csabs:operation/CandidateKey-isSuperkey",
    "type": "Operation",
    "name": "isSuperkey",
    "signature": "isSuperkey_F : 𝒫(U)→Prop",
    "description": "Tests semantic determination of all attributes under F.",
    "concept": "urn:csabs:concept/CandidateKey",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Tests semantic determination of all attributes under F."
  },
  {
    "id": "urn:csabs:operation/CandidateKey-isCandidateKey",
    "type": "Operation",
    "name": "isCandidateKey",
    "signature": "isCandidateKey_F : 𝒫(U)→Prop",
    "description": "Tests superkeyhood and inclusion minimality.",
    "concept": "urn:csabs:concept/CandidateKey",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Tests superkeyhood and inclusion minimality."
  },
  {
    "id": "urn:csabs:axiom/CandidateKey-key-definition",
    "type": "Axiom",
    "name": "key-definition",
    "statement": "A candidate key is an inclusion-minimal superkey.",
    "description": "A candidate key is an inclusion-minimal superkey.",
    "formalStatement": "Super_F(K) iff F⊨K→U; Key_F(K) iff Super_F(K) ∧ ∀J⊊K:¬Super_F(J)",
    "assumptions": [
      "U is finite, possibly empty; F is a set of FDs over the fixed schema. Empty keys are allowed. Minimality uses proper subsets. No SQL primary-key selection or NULL convention is added."
    ],
    "appliesTo": [
      "urn:csabs:concept/CandidateKey"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§11.2, p. 257, superkeys and keys before Definition 11.2.11",
    "sourceNote": "Records the source key as a candidate key, with inclusion-minimal rather than minimum-cardinality meaning. It is not inferred solely from an observed instance. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/CandidateKey-superkey-upward-closure",
    "type": "Law",
    "name": "superkey-upward-closure",
    "statement": "Every superset of a superkey is a superkey.",
    "description": "Every superset of a superkey is a superkey.",
    "formalStatement": "Super_F(K) ∧ K⊆J⊆U ⇒ Super_F(J)",
    "assumptions": [
      "U is finite, possibly empty; F is a set of FDs over the fixed schema. Empty keys are allowed. Minimality uses proper subsets. No SQL primary-key selection or NULL convention is added."
    ],
    "appliesTo": [
      "urn:csabs:concept/CandidateKey"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§11.2, p. 257, superkeys and keys before Definition 11.2.11",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Two rows agreeing on J agree on K and therefore on U in every F-model.",
    "dependsOn": [
      "urn:csabs:axiom/CandidateKey-key-definition",
      "urn:csabs:axiom/FunctionalDependency-satisfaction",
      "urn:csabs:axiom/FunctionalDependency-implication"
    ]
  },
  {
    "id": "urn:csabs:law/CandidateKey-key-antichain",
    "type": "Law",
    "name": "key-antichain",
    "statement": "Distinct candidate keys cannot properly contain one another.",
    "description": "Distinct candidate keys cannot properly contain one another.",
    "formalStatement": "Key_F(K) ∧ Key_F(J) ∧ K⊆J ⇒ K=J",
    "assumptions": [
      "U is finite, possibly empty; F is a set of FDs over the fixed schema. Empty keys are allowed. Minimality uses proper subsets. No SQL primary-key selection or NULL convention is added."
    ],
    "appliesTo": [
      "urn:csabs:concept/CandidateKey"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§11.2, p. 257, superkeys and keys before Definition 11.2.11",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "If inclusion were proper, J would have the proper superkey subset K, contradicting its defining minimality.",
    "dependsOn": [
      "urn:csabs:axiom/CandidateKey-key-definition"
    ]
  },
  {
    "id": "urn:csabs:theorem/CandidateKey-key-existence",
    "type": "Theorem",
    "name": "key-existence",
    "statement": "Every superkey contains a candidate key.",
    "description": "Every superkey contains a candidate key.",
    "formalStatement": "Super_F(K) ⇒ ∃J⊆K:Key_F(J)",
    "assumptions": [
      "U is finite, possibly empty; F is a set of FDs over the fixed schema. Empty keys are allowed. Minimality uses proper subsets. No SQL primary-key selection or NULL convention is added."
    ],
    "appliesTo": [
      "urn:csabs:concept/CandidateKey"
    ],
    "ruleRole": "derived-result",
    "proofSketch": "The collection of superkey subsets of K is finite and nonempty because it contains K. Choose one of least cardinality; a proper superkey subset would contradict that choice. U is always a superkey by FD reflexivity.",
    "dependsOn": [
      "urn:csabs:axiom/CandidateKey-key-definition",
      "urn:csabs:axiom/FunctionalDependency-implication",
      "urn:csabs:theorem/FunctionalDependency-armstrong-soundness"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§11.2, p. 257, superkeys and keys before Definition 11.2.11",
    "sourceNote": "Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/CandidateKey-key-projection-injective",
    "type": "Theorem",
    "name": "key-projection-injective",
    "statement": "A candidate key projects distinct rows to distinct key tuples in every permitted instance.",
    "description": "A candidate key projects distinct rows to distinct key tuples in every permitted instance.",
    "formalStatement": "Key_F(K) ∧ r⊨F ∧ s,t∈r ∧ s|K=t|K ⇒ s=t",
    "assumptions": [
      "U is finite, possibly empty; F is a set of FDs over the fixed schema. Empty keys are allowed. Minimality uses proper subsets. No SQL primary-key selection or NULL convention is added."
    ],
    "appliesTo": [
      "urn:csabs:concept/CandidateKey"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§11.2, p. 257, superkeys and keys before Definition 11.2.11",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Keyhood implies F⊨K→U. Apply it to the permitted instance and the two rows, then use componentwise tuple equality.",
    "dependsOn": [
      "urn:csabs:axiom/CandidateKey-key-definition",
      "urn:csabs:axiom/FunctionalDependency-implication",
      "urn:csabs:axiom/FunctionalDependency-satisfaction",
      "urn:csabs:axiom/RelationalSchema-tuple-extensionality"
    ]
  }
]
```
<!-- graph-record:end -->
