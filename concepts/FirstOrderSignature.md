# Single-sorted first-order signature

A countable collection of function and relation symbols, each with a specified finite arity; functions and relations are distinct symbol sorts. Constants are nullary function symbols.

**Notation:** Σ=(F_n,R_n)_{n∈ℕ}; Term_Σ(V)=T_F(V); V={v₀,v₁,…}

**Stable ID:** `urn:csabs:concept/FirstOrderSignature`

**Categories:** Logic and proof

**Kind:** Mathematical structure

**Prerequisites:** [Free ranked term algebra with variables](TermAlgebra.md)

## Backlinks

- [First-order formula syntax with named variables](FirstOrderFormula.md) — `requiresConcept`
- [Free ranked term algebra with variables](TermAlgebra.md) — `relatedConcept`

## Mathematical formulation

The selected countable signature is (Fn\_n,Pred\_n)\_{n∈ℕ}, with Fn\_n⊆ℕ and Pred\_n⊆ℕ identifying symbols of arity n. Tags distinguish symbol sorts and arities even when their numerical names coincide.

**Lean formulation** (in its source module context):

```lean
structure FirstOrderSignature where
  functions : Nat → Set Nat
  relations : Nat → Set Nat
```

**Source:** [`Catalog.FirstOrderSignature`](../lean/Catalog/LogicSyntax.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Countable tagged symbol families: functions n and relations n are subsets of Nat, with n the arity. Instantiate Fn n and Pred n as their subtypes. Nullary symbols are allowed; sorts remain distinct.

**Limits:** Compiled carrier and selected interface only. No new graph law or metatheorem is registered as a proof witness. In particular substitution-support, semantic correspondence, soundness, completeness, compactness and normal-form existence are editorial claims here; grammar/rule declarations do not prove them.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Disjoint countable function/relation symbol families indexed by finite arity; constants are nullary functions and equality is a separate logical symbol.

**basisKind:** defined-structure

**basisScope:** Countable, single-sorted signature; each F_n and R_n is a subset of a countable symbol supply, tagged by arity and sort. Empty symbol sets and nullary functions/relations are allowed. Logical equality is distinguished from R_n.

**verificationObligation:** Distinguish raw syntactic equality, alpha equivalence, semantic equivalence and derivability. Retrieve explicitly linked premises; prerequisite links do not inherit axioms.; Lean model bindings may expose only a partial interface; consult their limitations.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-FirstOrderSignature-arity"></a>

### arity

`urn:csabs:operation/FirstOrderSignature-arity`

**signature:** arity:(Σn.F_n)+(Σn.R_n)→ℕ

**description:** Returns the arity tag of a function or relation symbol.

**precondition:** Inputs belong to the indicated carriers.

**totality:** Total on the stated domain.

**outcome:** Returns the arity tag of a function or relation symbol.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-FirstOrderSignature-ranked-symbols"></a>

### ranked-symbols

`urn:csabs:axiom/FirstOrderSignature-ranked-symbols`

**statement:** A signature fixes symbol sorts and arities before constructing expressions.

**formalStatement:** F=Σn∈ℕ.F_n; R=Σn∈ℕ.R_n; F and R are disjoint tagged carriers; arity(in_F(n,f))=n; arity(in_R(n,r))=n.

**assumptions:** Countable, single-sorted signature; each F_n and R_n is a subset of a countable symbol supply, tagged by arity and sort. Empty symbol sets and nullary functions/relations are allowed. Logical equality is distinguished from R_n.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**ruleRole:** defining-rule

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §2.2 First-order languages

**sourceNote:** Repackages the countable symbol vocabulary as disjoint arity-indexed families. Nullary relations are an explicit harmless extension, interpreted as truth values, rather than identified with logical truth constants.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-FirstOrderSignature-arity-determinate"></a>

### arity-determinate

`urn:csabs:law/FirstOrderSignature-arity-determinate`

**statement:** A fixed symbol cannot acquire a different arity in another occurrence.

**formalStatement:** s=t ⇒ arity(s)=arity(t)

**assumptions:** Countable, single-sorted signature; each F_n and R_n is a subset of a countable symbol supply, tagged by arity and sort. Empty symbol sets and nullary functions/relations are allowed. Logical equality is distinguished from R_n.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [ranked-symbols](FirstOrderSignature.md#node-urn-csabs-axiom-FirstOrderSignature-ranked-symbols)

**proofSketch:** Apply the arity projection to equal tagged symbols.

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §2.2 fixed n-place symbol vocabulary

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-FirstOrderSignature-singleton-interpretation"></a>

### singleton-interpretation

`urn:csabs:theorem/FirstOrderSignature-singleton-interpretation`

**statement:** Every such signature has an interpretation on a singleton domain.

**formalStatement:** D={*}; f^M(*,…,*)=* for every f; choose R^M=∅ for each R; equality is identity.

**assumptions:** Countable, single-sorted signature; each F_n and R_n is a subset of a countable symbol supply, tagged by arity and sort. Empty symbol sets and nullary functions/relations are allowed. Logical equality is distinguished from R_n.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [ranked-symbols](FirstOrderSignature.md#node-urn-csabs-axiom-FirstOrderSignature-ranked-symbols); [structure](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-structure)

**proofSketch:** There is a unique map Dⁿ→D for every finite n, including zero. Empty subsets of Dⁿ give relation interpretations. These satisfy all structural requirements.

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §3.2 Definition 3.1

**sourceNote:** Catalog construction from the signature vocabulary and the consulted definition of a structure; no theory axioms are assumed.

**provenanceKind:** derived

## Concept provenance

- [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §2.2 First-order languages; §2.3 Definition 2.4 and discussion of nullary functions

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/FirstOrderSignature",
    "type": "Concept",
    "shortForm": "FirstOrderSignature",
    "fullName": "Single-sorted first-order signature",
    "category": [
      "urn:csabs:category/logic"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A countable collection of function and relation symbols, each with a specified finite arity; functions and relations are distinct symbol sorts. Constants are nullary function symbols.",
    "notation": "Σ=(F_n,R_n)_{n∈ℕ}; Term_Σ(V)=T_F(V); V={v₀,v₁,…}",
    "axiomBasis": "Disjoint countable function/relation symbol families indexed by finite arity; constants are nullary functions and equality is a separate logical symbol.",
    "basisKind": "defined-structure",
    "basisScope": "Countable, single-sorted signature; each F_n and R_n is a subset of a countable symbol supply, tagged by arity and sort. Empty symbol sets and nullary functions/relations are allowed. Logical equality is distinguished from R_n.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "verificationObligation": [
      "Distinguish raw syntactic equality, alpha equivalence, semantic equivalence and derivability. Retrieve explicitly linked premises; prerequisite links do not inherit axioms.",
      "Lean model bindings may expose only a partial interface; consult their limitations."
    ],
    "requiresConcept": [
      "urn:csabs:concept/TermAlgebra"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/FirstOrderSignature-arity"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/FirstOrderSignature-ranked-symbols"
    ],
    "hasLaw": [
      "urn:csabs:law/FirstOrderSignature-arity-determinate"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/FirstOrderSignature-singleton-interpretation"
    ],
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§2.2 First-order languages; §2.3 Definition 2.4 and discussion of nullary functions",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "adapted",
    "leanFormulation": "structure FirstOrderSignature where\n  functions : Nat → Set Nat\n  relations : Nat → Set Nat",
    "formulationSource": "urn:csabs:source/local-lean-LogicSyntax",
    "formulationLocator": "Catalog.FirstOrderSignature",
    "formulationScope": "model",
    "leanModelMapping": "Countable tagged symbol families: functions n and relations n are subsets of Nat, with n the arity. Instantiate Fn n and Pred n as their subtypes. Nullary symbols are allowed; sorts remain distinct.",
    "leanModelLimitations": "Compiled carrier and selected interface only. No new graph law or metatheorem is registered as a proof witness. In particular substitution-support, semantic correspondence, soundness, completeness, compactness and normal-form existence are editorial claims here; grammar/rule declarations do not prove them.",
    "mathematicalFormulation": "The selected countable signature is (Fn_n,Pred_n)_{n∈ℕ}, with Fn_n⊆ℕ and Pred_n⊆ℕ identifying symbols of arity n. Tags distinguish symbol sorts and arities even when their numerical names coincide."
  },
  {
    "id": "urn:csabs:operation/FirstOrderSignature-arity",
    "type": "Operation",
    "name": "arity",
    "signature": "arity:(Σn.F_n)+(Σn.R_n)→ℕ",
    "description": "Returns the arity tag of a function or relation symbol.",
    "concept": "urn:csabs:concept/FirstOrderSignature",
    "precondition": "Inputs belong to the indicated carriers.",
    "totality": "Total on the stated domain.",
    "outcome": "Returns the arity tag of a function or relation symbol."
  },
  {
    "id": "urn:csabs:axiom/FirstOrderSignature-ranked-symbols",
    "type": "Axiom",
    "name": "ranked-symbols",
    "statement": "A signature fixes symbol sorts and arities before constructing expressions.",
    "formalStatement": "F=Σn∈ℕ.F_n; R=Σn∈ℕ.R_n; F and R are disjoint tagged carriers; arity(in_F(n,f))=n; arity(in_R(n,r))=n.",
    "assumptions": [
      "Countable, single-sorted signature; each F_n and R_n is a subset of a countable symbol supply, tagged by arity and sort. Empty symbol sets and nullary functions/relations are allowed. Logical equality is distinguished from R_n."
    ],
    "appliesTo": [
      "urn:csabs:concept/FirstOrderSignature"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "defining-rule",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§2.2 First-order languages",
    "sourceNote": "Repackages the countable symbol vocabulary as disjoint arity-indexed families. Nullary relations are an explicit harmless extension, interpreted as truth values, rather than identified with logical truth constants.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/FirstOrderSignature-arity-determinate",
    "type": "Law",
    "name": "arity-determinate",
    "statement": "A fixed symbol cannot acquire a different arity in another occurrence.",
    "formalStatement": "s=t ⇒ arity(s)=arity(t)",
    "assumptions": [
      "Countable, single-sorted signature; each F_n and R_n is a subset of a countable symbol supply, tagged by arity and sort. Empty symbol sets and nullary functions/relations are allowed. Logical equality is distinguished from R_n."
    ],
    "appliesTo": [
      "urn:csabs:concept/FirstOrderSignature"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/FirstOrderSignature-ranked-symbols"
    ],
    "proofSketch": "Apply the arity projection to equal tagged symbols.",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§2.2 fixed n-place symbol vocabulary",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/FirstOrderSignature-singleton-interpretation",
    "type": "Theorem",
    "name": "singleton-interpretation",
    "statement": "Every such signature has an interpretation on a singleton domain.",
    "formalStatement": "D={*}; f^M(*,…,*)=* for every f; choose R^M=∅ for each R; equality is identity.",
    "assumptions": [
      "Countable, single-sorted signature; each F_n and R_n is a subset of a countable symbol supply, tagged by arity and sort. Empty symbol sets and nullary functions/relations are allowed. Logical equality is distinguished from R_n."
    ],
    "appliesTo": [
      "urn:csabs:concept/FirstOrderSignature"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/FirstOrderSignature-ranked-symbols",
      "urn:csabs:axiom/PredicateLogic-structure"
    ],
    "proofSketch": "There is a unique map Dⁿ→D for every finite n, including zero. Empty subsets of Dⁿ give relation interpretations. These satisfy all structural requirements.",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§3.2 Definition 3.1",
    "sourceNote": "Catalog construction from the signature vocabulary and the consulted definition of a structure; no theory axioms are assumed.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
