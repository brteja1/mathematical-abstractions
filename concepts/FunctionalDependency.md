# Functional dependency on a relational schema

An attribute agreement constraint requiring agreement on one attribute set to force agreement on another in every pair of rows.

**Notation:** r⊨X→Y iff ∀s,t∈r:(s|X=t|X ⇒ s|Y=t|Y)

**Stable ID:** `urn:csabs:concept/FunctionalDependency`

**Categories:** Relational data modelling, Logic and proof

**Kind:** principle

**Prerequisites:** [Finite database relation under set semantics](DatabaseRelation.md), [Predicate Logic](PredicateLogic.md)

**Related concepts:** [Candidate key relative to functional dependencies](CandidateKey.md), [Total function](Function.md), [Closure Operator](ClosureOperator.md)

## Backlinks

- [Candidate key relative to functional dependencies](CandidateKey.md) — `requiresConcept`
- [Finite database relation under set semantics](DatabaseRelation.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected defining presentation: An FD requires equal determinant values to imply equal dependent values. Schema implication ranges over all finite instances satisfying the premise FDs. Attribute closure collects all individually determined attributes.

**basisKind:** defined-structure

**basisScope:** X,Y,Z⊆U for a fixed schema. Relations use identity equality, no NULL and set semantics. Empty and singleton relations satisfy every FD; observed satisfaction alone does not assert a schema-wide constraint.

**verificationObligation:** X,Y,Z⊆U for a fixed schema. Relations use identity equality, no NULL and set semantics. Empty and singleton relations satisfy every FD; observed satisfaction alone does not assert a schema-wide constraint.

**reviewStatus:** editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-FunctionalDependency-satisfies"></a>

### satisfies

`urn:csabs:operation/FunctionalDependency-satisfies`

**signature:** satisfies : Rel(Σ)×FD(U)→Prop

**description:** Checks the pairwise row constraint mathematically.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Checks the pairwise row constraint mathematically.

<a id="node-urn-csabs-operation-FunctionalDependency-entails"></a>

### entails

`urn:csabs:operation/FunctionalDependency-entails`

**signature:** entails : 𝒫(FD(U))×FD(U)→Prop

**description:** Quantifies over finite instances satisfying the premises, rather than only the current data.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Quantifies over finite instances satisfying the premises, rather than only the current data.

<a id="node-urn-csabs-operation-FunctionalDependency-attributeClosure"></a>

### attributeClosure

`urn:csabs:operation/FunctionalDependency-attributeClosure`

**signature:** cl_F : 𝒫(U)→𝒫(U)

**description:** Returns attributes semantically determined by the input under F; this definition is not an algorithm.

**precondition:** X,Y,Z⊆U for a fixed schema. Relations use identity equality, no NULL and set semantics. Empty and singleton relations satisfy every FD; observed satisfaction alone does not assert a schema-wide constraint.

**postcondition:** Returns attributes semantically determined by the input under F; this definition is not an algorithm.

**totality:** total mathematical operation on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-FunctionalDependency-satisfaction"></a>

### satisfaction

`urn:csabs:axiom/FunctionalDependency-satisfaction`

**statement:** An FD requires equal determinant values to imply equal dependent values.

**description:** An FD requires equal determinant values to imply equal dependent values.

**formalStatement:** FD(U)=𝒫(U)×𝒫(U); r⊨X→Y iff ∀s,t∈r:(s|X=t|X⇒s|Y=t|Y)

**assumptions:** X,Y,Z⊆U for a fixed schema. Relations use identity equality, no NULL and set semantics. Empty and singleton relations satisfy every FD; observed satisfaction alone does not assert a schema-wide constraint.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §8.2, Definitions 8.2.1 and 8.2.3, pp. 163–164

**sourceNote:** Separates satisfaction by one instance from logical implication over all finite instances; inference rules below are derived from pairwise semantics. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-FunctionalDependency-implication"></a>

### implication

`urn:csabs:axiom/FunctionalDependency-implication`

**statement:** Schema implication ranges over all finite instances satisfying the premise FDs.

**description:** Schema implication ranges over all finite instances satisfying the premise FDs.

**formalStatement:** F⊨X→Y iff ∀r∈Rel(Σ):((∀f∈F:r⊨f)⇒r⊨X→Y)

**assumptions:** X,Y,Z⊆U for a fixed schema. Relations use identity equality, no NULL and set semantics. Empty and singleton relations satisfy every FD; observed satisfaction alone does not assert a schema-wide constraint.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §8.2, Definitions 8.2.1 and 8.2.3, pp. 163–164

**sourceNote:** Separates satisfaction by one instance from logical implication over all finite instances; inference rules below are derived from pairwise semantics. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-FunctionalDependency-closure-definition"></a>

### closure-definition

`urn:csabs:axiom/FunctionalDependency-closure-definition`

**statement:** Attribute closure collects all individually determined attributes.

**description:** Attribute closure collects all individually determined attributes.

**formalStatement:** cl_F(X)={a∈U:F⊨X→{a}}

**assumptions:** X,Y,Z⊆U for a fixed schema. Relations use identity equality, no NULL and set semantics. Empty and singleton relations satisfy every FD; observed satisfaction alone does not assert a schema-wide constraint.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §8.2, attribute closure preceding Lemma 8.2.6, p. 165

**sourceNote:** Specifies additional equations for the selected abstract interface; local conventions are explicit.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-FunctionalDependency-union-decomposition"></a>

### union-decomposition

`urn:csabs:law/FunctionalDependency-union-decomposition`

**statement:** A common determinant determines a union exactly when it determines both parts.

**description:** A common determinant determines a union exactly when it determines both parts.

**formalStatement:** F⊨X→(Y∪Z) iff (F⊨X→Y ∧ F⊨X→Z)

**assumptions:** X,Y,Z⊆U for a fixed schema. Relations use identity equality, no NULL and set semantics. Empty and singleton relations satisfy every FD; observed satisfaction alone does not assert a schema-wide constraint.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §8.2, Definitions 8.2.1 and 8.2.3, pp. 163–164

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Agreement on a union is agreement on each part. Apply the pairwise FD definition in every F-model.

**dependsOn:** [satisfaction](FunctionalDependency.md#node-urn-csabs-axiom-FunctionalDependency-satisfaction); [implication](FunctionalDependency.md#node-urn-csabs-axiom-FunctionalDependency-implication)

## Theorems

<a id="node-urn-csabs-theorem-FunctionalDependency-armstrong-soundness"></a>

### armstrong-soundness

`urn:csabs:theorem/FunctionalDependency-armstrong-soundness`

**statement:** Reflexivity, augmentation, and transitivity are sound FD inference rules.

**description:** Reflexivity, augmentation, and transitivity are sound FD inference rules.

**formalStatement:** Y⊆X⇒⊨X→Y; X→Y⊨XZ→YZ; {X→Y,Y→Z}⊨X→Z; XZ=X∪Z

**assumptions:** X,Y,Z⊆U for a fixed schema. Relations use identity equality, no NULL and set semantics. Empty and singleton relations satisfy every FD; observed satisfaction alone does not assert a schema-wide constraint.

**ruleRole:** derived-result

**proofSketch:** For any two rows, restrict agreement to a subset, add the unchanged Z agreement, or compose the two implications respectively. Quantify over instances. No completeness claim is made.

**dependsOn:** [satisfaction](FunctionalDependency.md#node-urn-csabs-axiom-FunctionalDependency-satisfaction); [implication](FunctionalDependency.md#node-urn-csabs-axiom-FunctionalDependency-implication)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §8.2, Definitions 8.2.1 and 8.2.3, pp. 163–164

**sourceNote:** Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-DatabaseRelation-fd-lossless-decomposition"></a>

### fd-lossless-decomposition

`urn:csabs:theorem/DatabaseRelation-fd-lossless-decomposition`

**statement:** An FD gives a lossless decomposition into two projections.

**description:** An FD gives a lossless decomposition into two projections.

**formalStatement:** r⊨X→Y ∧ Z=U∖(X∪Y) ⇒ r=π_{X∪Y}(r) ⋈ π_{X∪Z}(r)

**assumptions:** Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §8.2, Proposition 8.2.2, p. 164; §4.4 natural join

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Every original row yields compatible projections. Conversely a joined row combines projections of s,t∈r agreeing on X. The FD forces agreement on Y, so the joined row equals t on all U and belongs to r.

**dependsOn:** [set-interface](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-set-interface); [projection](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-projection); [relational-algebra](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-relational-algebra); [satisfaction](FunctionalDependency.md#node-urn-csabs-axiom-FunctionalDependency-satisfaction)

<a id="node-urn-csabs-theorem-FunctionalDependency-closure-operator"></a>

### closure-operator

`urn:csabs:theorem/FunctionalDependency-closure-operator`

**statement:** Semantic attribute closure is extensive, monotone and idempotent.

**description:** Semantic attribute closure is extensive, monotone and idempotent.

**formalStatement:** X⊆cl_F(X); X⊆Y⇒cl_F(X)⊆cl_F(Y); cl_F(cl_F(X))=cl_F(X)

**assumptions:** X,Y,Z⊆U for a fixed schema. Relations use identity equality, no NULL and set semantics. Empty and singleton relations satisfy every FD; observed satisfaction alone does not assert a schema-wide constraint.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §8.2, Definitions 8.2.1 and 8.2.3, pp. 163–164

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed. The resulting function cl_F instantiates the existing ClosureOperator interface on the carrier 𝒫(U) ordered by inclusion; FunctionalDependency itself is not a specialization of ClosureOperator.

**provenanceKind:** derived

**proofSketch:** Reflexivity gives extensivity. Agreement on Y implies agreement on X for X⊆Y, giving monotonicity. If two F-model rows agree on X, they agree on every member of cl_F(X); any attribute determined by that closure is therefore already determined by X. This proves one idempotence inclusion, with extensivity giving the other.

**dependsOn:** [satisfaction](FunctionalDependency.md#node-urn-csabs-axiom-FunctionalDependency-satisfaction); [implication](FunctionalDependency.md#node-urn-csabs-axiom-FunctionalDependency-implication); [closure-definition](FunctionalDependency.md#node-urn-csabs-axiom-FunctionalDependency-closure-definition)

## Concept provenance

- [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §8.2, Definitions 8.2.1 and 8.2.3, pp. 163–164

**sourceNote:** Separates satisfaction by one instance from logical implication over all finite instances; inference rules below are derived from pairwise semantics.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/FunctionalDependency",
    "type": "Concept",
    "shortForm": "FunctionalDependency",
    "fullName": "Functional dependency on a relational schema",
    "category": [
      "urn:csabs:category/data-modelling",
      "urn:csabs:category/logic"
    ],
    "kind": "urn:csabs:kind/principle",
    "definition": "An attribute agreement constraint requiring agreement on one attribute set to force agreement on another in every pair of rows.",
    "notation": "r⊨X→Y iff ∀s,t∈r:(s|X=t|X ⇒ s|Y=t|Y)",
    "hasOperation": [
      "urn:csabs:operation/FunctionalDependency-satisfies",
      "urn:csabs:operation/FunctionalDependency-entails",
      "urn:csabs:operation/FunctionalDependency-attributeClosure"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/FunctionalDependency-satisfaction",
      "urn:csabs:axiom/FunctionalDependency-implication",
      "urn:csabs:axiom/FunctionalDependency-closure-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/FunctionalDependency-union-decomposition"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/FunctionalDependency-armstrong-soundness",
      "urn:csabs:theorem/DatabaseRelation-fd-lossless-decomposition",
      "urn:csabs:theorem/FunctionalDependency-closure-operator"
    ],
    "requiresConcept": [
      "urn:csabs:concept/DatabaseRelation",
      "urn:csabs:concept/PredicateLogic"
    ],
    "relatedConcept": [
      "urn:csabs:concept/CandidateKey",
      "urn:csabs:concept/Function",
      "urn:csabs:concept/ClosureOperator"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Selected defining presentation: An FD requires equal determinant values to imply equal dependent values. Schema implication ranges over all finite instances satisfying the premise FDs. Attribute closure collects all individually determined attributes.",
    "basisKind": "defined-structure",
    "basisScope": "X,Y,Z⊆U for a fixed schema. Relations use identity equality, no NULL and set semantics. Empty and singleton relations satisfy every FD; observed satisfaction alone does not assert a schema-wide constraint.",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§8.2, Definitions 8.2.1 and 8.2.3, pp. 163–164",
    "sourceNote": "Separates satisfaction by one instance from logical implication over all finite instances; inference rules below are derived from pairwise semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof",
    "verificationObligation": [
      "X,Y,Z⊆U for a fixed schema. Relations use identity equality, no NULL and set semantics. Empty and singleton relations satisfy every FD; observed satisfaction alone does not assert a schema-wide constraint."
    ]
  },
  {
    "id": "urn:csabs:operation/FunctionalDependency-satisfies",
    "type": "Operation",
    "name": "satisfies",
    "signature": "satisfies : Rel(Σ)×FD(U)→Prop",
    "description": "Checks the pairwise row constraint mathematically.",
    "concept": "urn:csabs:concept/FunctionalDependency",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Checks the pairwise row constraint mathematically."
  },
  {
    "id": "urn:csabs:operation/FunctionalDependency-entails",
    "type": "Operation",
    "name": "entails",
    "signature": "entails : 𝒫(FD(U))×FD(U)→Prop",
    "description": "Quantifies over finite instances satisfying the premises, rather than only the current data.",
    "concept": "urn:csabs:concept/FunctionalDependency",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Quantifies over finite instances satisfying the premises, rather than only the current data."
  },
  {
    "id": "urn:csabs:operation/FunctionalDependency-attributeClosure",
    "type": "Operation",
    "name": "attributeClosure",
    "signature": "cl_F : 𝒫(U)→𝒫(U)",
    "description": "Returns attributes semantically determined by the input under F; this definition is not an algorithm.",
    "concept": "urn:csabs:concept/FunctionalDependency",
    "precondition": "X,Y,Z⊆U for a fixed schema. Relations use identity equality, no NULL and set semantics. Empty and singleton relations satisfy every FD; observed satisfaction alone does not assert a schema-wide constraint.",
    "postcondition": "Returns attributes semantically determined by the input under F; this definition is not an algorithm.",
    "totality": "total mathematical operation on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/FunctionalDependency-satisfaction",
    "type": "Axiom",
    "name": "satisfaction",
    "statement": "An FD requires equal determinant values to imply equal dependent values.",
    "description": "An FD requires equal determinant values to imply equal dependent values.",
    "formalStatement": "FD(U)=𝒫(U)×𝒫(U); r⊨X→Y iff ∀s,t∈r:(s|X=t|X⇒s|Y=t|Y)",
    "assumptions": [
      "X,Y,Z⊆U for a fixed schema. Relations use identity equality, no NULL and set semantics. Empty and singleton relations satisfy every FD; observed satisfaction alone does not assert a schema-wide constraint."
    ],
    "appliesTo": [
      "urn:csabs:concept/FunctionalDependency"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§8.2, Definitions 8.2.1 and 8.2.3, pp. 163–164",
    "sourceNote": "Separates satisfaction by one instance from logical implication over all finite instances; inference rules below are derived from pairwise semantics. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/FunctionalDependency-implication",
    "type": "Axiom",
    "name": "implication",
    "statement": "Schema implication ranges over all finite instances satisfying the premise FDs.",
    "description": "Schema implication ranges over all finite instances satisfying the premise FDs.",
    "formalStatement": "F⊨X→Y iff ∀r∈Rel(Σ):((∀f∈F:r⊨f)⇒r⊨X→Y)",
    "assumptions": [
      "X,Y,Z⊆U for a fixed schema. Relations use identity equality, no NULL and set semantics. Empty and singleton relations satisfy every FD; observed satisfaction alone does not assert a schema-wide constraint."
    ],
    "appliesTo": [
      "urn:csabs:concept/FunctionalDependency"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§8.2, Definitions 8.2.1 and 8.2.3, pp. 163–164",
    "sourceNote": "Separates satisfaction by one instance from logical implication over all finite instances; inference rules below are derived from pairwise semantics. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/FunctionalDependency-closure-definition",
    "type": "Axiom",
    "name": "closure-definition",
    "statement": "Attribute closure collects all individually determined attributes.",
    "description": "Attribute closure collects all individually determined attributes.",
    "formalStatement": "cl_F(X)={a∈U:F⊨X→{a}}",
    "assumptions": [
      "X,Y,Z⊆U for a fixed schema. Relations use identity equality, no NULL and set semantics. Empty and singleton relations satisfy every FD; observed satisfaction alone does not assert a schema-wide constraint."
    ],
    "appliesTo": [
      "urn:csabs:concept/FunctionalDependency"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§8.2, attribute closure preceding Lemma 8.2.6, p. 165",
    "sourceNote": "Specifies additional equations for the selected abstract interface; local conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/FunctionalDependency-union-decomposition",
    "type": "Law",
    "name": "union-decomposition",
    "statement": "A common determinant determines a union exactly when it determines both parts.",
    "description": "A common determinant determines a union exactly when it determines both parts.",
    "formalStatement": "F⊨X→(Y∪Z) iff (F⊨X→Y ∧ F⊨X→Z)",
    "assumptions": [
      "X,Y,Z⊆U for a fixed schema. Relations use identity equality, no NULL and set semantics. Empty and singleton relations satisfy every FD; observed satisfaction alone does not assert a schema-wide constraint."
    ],
    "appliesTo": [
      "urn:csabs:concept/FunctionalDependency"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§8.2, Definitions 8.2.1 and 8.2.3, pp. 163–164",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Agreement on a union is agreement on each part. Apply the pairwise FD definition in every F-model.",
    "dependsOn": [
      "urn:csabs:axiom/FunctionalDependency-satisfaction",
      "urn:csabs:axiom/FunctionalDependency-implication"
    ]
  },
  {
    "id": "urn:csabs:theorem/FunctionalDependency-armstrong-soundness",
    "type": "Theorem",
    "name": "armstrong-soundness",
    "statement": "Reflexivity, augmentation, and transitivity are sound FD inference rules.",
    "description": "Reflexivity, augmentation, and transitivity are sound FD inference rules.",
    "formalStatement": "Y⊆X⇒⊨X→Y; X→Y⊨XZ→YZ; {X→Y,Y→Z}⊨X→Z; XZ=X∪Z",
    "assumptions": [
      "X,Y,Z⊆U for a fixed schema. Relations use identity equality, no NULL and set semantics. Empty and singleton relations satisfy every FD; observed satisfaction alone does not assert a schema-wide constraint."
    ],
    "appliesTo": [
      "urn:csabs:concept/FunctionalDependency"
    ],
    "ruleRole": "derived-result",
    "proofSketch": "For any two rows, restrict agreement to a subset, add the unchanged Z agreement, or compose the two implications respectively. Quantify over instances. No completeness claim is made.",
    "dependsOn": [
      "urn:csabs:axiom/FunctionalDependency-satisfaction",
      "urn:csabs:axiom/FunctionalDependency-implication"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§8.2, Definitions 8.2.1 and 8.2.3, pp. 163–164",
    "sourceNote": "Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/FunctionalDependency-closure-operator",
    "type": "Theorem",
    "name": "closure-operator",
    "statement": "Semantic attribute closure is extensive, monotone and idempotent.",
    "description": "Semantic attribute closure is extensive, monotone and idempotent.",
    "formalStatement": "X⊆cl_F(X); X⊆Y⇒cl_F(X)⊆cl_F(Y); cl_F(cl_F(X))=cl_F(X)",
    "assumptions": [
      "X,Y,Z⊆U for a fixed schema. Relations use identity equality, no NULL and set semantics. Empty and singleton relations satisfy every FD; observed satisfaction alone does not assert a schema-wide constraint."
    ],
    "appliesTo": [
      "urn:csabs:concept/FunctionalDependency"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§8.2, Definitions 8.2.1 and 8.2.3, pp. 163–164",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed. The resulting function cl_F instantiates the existing ClosureOperator interface on the carrier 𝒫(U) ordered by inclusion; FunctionalDependency itself is not a specialization of ClosureOperator.",
    "provenanceKind": "derived",
    "proofSketch": "Reflexivity gives extensivity. Agreement on Y implies agreement on X for X⊆Y, giving monotonicity. If two F-model rows agree on X, they agree on every member of cl_F(X); any attribute determined by that closure is therefore already determined by X. This proves one idempotence inclusion, with extensivity giving the other.",
    "dependsOn": [
      "urn:csabs:axiom/FunctionalDependency-satisfaction",
      "urn:csabs:axiom/FunctionalDependency-implication",
      "urn:csabs:axiom/FunctionalDependency-closure-definition"
    ]
  }
]
```
<!-- graph-record:end -->
