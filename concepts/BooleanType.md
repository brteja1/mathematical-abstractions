# Two-valued Boolean type

The free enumeration with exactly two distinct values, false and true, with total case analysis and Boolean negation.

**Notation:** Bool = {false,true}

**Stable ID:** `urn:csabs:concept/BooleanType`

**Categories:** Types and semantics

**Kind:** Numeric data type

**Specializes:** [Boolean algebra](BooleanAlgebra.md)

## Backlinks

- [Finite simple graph with chosen bipartition](BipartiteGraph.md) — `requiresConcept`
- [Finite JSON document value (interoperable profile)](DocumentValue.md) — `requiresConcept`

## Mathematical formulation

Bool={false,true}; neg(false)=true and neg(true)=false. This is a two-constructor value type, with constructor equality, distinct from the universe Prop of propositions.

**Lean formulation** (in its source module context):

```lean
abbrev BooleanType := Bool
```

**Source:** [`Catalog.BooleanType`](../lean/Catalog/CoreData.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Bool = {false,true}. Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.

**Limits:** Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** false≠true ∧ ∀b:Bool, b=false ∨ b=true; case(x,y,false)=x ∧ case(x,y,true)=y; not(false)=true ∧ not(true)=false

**basisKind:** extensional-structural-definition

**basisScope:** Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.

**specializationNote:** Instantiate BooleanAlgebra with carrier Bool, bottom=false, top=true, join=or, meet=and and complement=not. The truth tables supply the structure; this edge transfers no claims automatically.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-BooleanType-false"></a>

### false

`urn:csabs:operation/BooleanType-false`

**signature:** false : Bool

**description:** Constructs false.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Constructs false.

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BooleanType-true"></a>

### true

`urn:csabs:operation/BooleanType-true`

**signature:** true : Bool

**description:** Constructs true.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Constructs true.

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BooleanType-case"></a>

### case

`urn:csabs:operation/BooleanType-case`

**signature:** case : C×C×Bool→C

**description:** case(x,y,false)=x; case(x,y,true)=y.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** case(x,y,false)=x; case(x,y,true)=y.

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BooleanType-not"></a>

### not

`urn:csabs:operation/BooleanType-not`

**signature:** not : Bool→Bool

**description:** not(false)=true; not(true)=false.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** not(false)=true; not(true)=false.

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-BooleanType-enumeration"></a>

### enumeration

`urn:csabs:axiom/BooleanType-enumeration`

**statement:** Defining requirement: false≠true ∧ ∀b:Bool, b=false ∨ b=true

**formalStatement:** false≠true ∧ ∀b:Bool, b=false ∨ b=true

**assumptions:** Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-BooleanType-case-beta"></a>

### case-beta

`urn:csabs:axiom/BooleanType-case-beta`

**statement:** Defining requirement: case(x,y,false)=x ∧ case(x,y,true)=y

**formalStatement:** case(x,y,false)=x ∧ case(x,y,true)=y

**assumptions:** Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-BooleanType-not-equations"></a>

### not-equations

`urn:csabs:axiom/BooleanType-not-equations`

**statement:** Defining requirement: not(false)=true ∧ not(true)=false

**formalStatement:** not(false)=true ∧ not(true)=false

**assumptions:** Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-BooleanType-double-negation"></a>

### double-negation

`urn:csabs:law/BooleanType-double-negation`

**statement:** ∀b:Bool, not(not(b))=b

**formalStatement:** ∀b:Bool, not(not(b))=b

**assumptions:** Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [enumeration](BooleanType.md#node-urn-csabs-axiom-BooleanType-enumeration); [not-equations](BooleanType.md#node-urn-csabs-axiom-BooleanType-not-equations)

**proofSketch:** Split on the two enumeration cases and compute negation twice.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (b : Catalog.BooleanType), !(!b) = b
```

**Source:** [`Catalog.CoreDataProofs.bool_not_not`](../lean/Catalog/CoreData.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Bool has the two disjoint constructors false/true; not is Lean Bool.not; equality is Boolean value equality. Case elimination supplies enumeration and not-equations.

**Limits:** Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/BooleanType-enumeration": "Interpreted premise: false≠true ∧ ∀b:Bool, b=false ∨ b=true. Bool has the two disjoint constructors false/true; not is Lean Bool.not; equality is Boolean value equality. Case elimination supplies enumeration and not-equations.",
  "urn:csabs:axiom/BooleanType-not-equations": "Interpreted premise: not(false)=true ∧ not(true)=false. Bool has the two disjoint constructors false/true; not is Lean Bool.not; equality is Boolean value equality. Case elimination supplies enumeration and not-equations."
}
```

## Theorems

<a id="node-urn-csabs-theorem-BooleanType-case-uniqueness"></a>

### case-uniqueness

`urn:csabs:theorem/BooleanType-case-uniqueness`

**statement:** (f(false)=x ∧ f(true)=y) ⇒ ∀b, f(b)=case(x,y,b)

**formalStatement:** (f(false)=x ∧ f(true)=y) ⇒ ∀b, f(b)=case(x,y,b)

**assumptions:** Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [enumeration](BooleanType.md#node-urn-csabs-axiom-BooleanType-enumeration); [case-beta](BooleanType.md#node-urn-csabs-axiom-BooleanType-case-beta)

**proofSketch:** Case split on b and use both beta equations.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/BooleanType",
    "type": "Concept",
    "shortForm": "BooleanType",
    "fullName": "Two-valued Boolean type",
    "category": [
      "urn:csabs:category/types"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "The free enumeration with exactly two distinct values, false and true, with total case analysis and Boolean negation.",
    "notation": "Bool = {false,true}",
    "requiresConcept": [],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/BooleanType-false",
      "urn:csabs:operation/BooleanType-true",
      "urn:csabs:operation/BooleanType-case",
      "urn:csabs:operation/BooleanType-not"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/BooleanType-enumeration",
      "urn:csabs:axiom/BooleanType-case-beta",
      "urn:csabs:axiom/BooleanType-not-equations"
    ],
    "hasLaw": [
      "urn:csabs:law/BooleanType-double-negation"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/BooleanType-case-uniqueness"
    ],
    "axiomBasis": "false≠true ∧ ∀b:Bool, b=false ∨ b=true; case(x,y,false)=x ∧ case(x,y,true)=y; not(false)=true ∧ not(true)=false",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/BooleanAlgebra"
    ],
    "specializationNote": "Instantiate BooleanAlgebra with carrier Bool, bottom=false, top=true, join=or, meet=and and complement=not. The truth tables supply the structure; this edge transfers no claims automatically.",
    "leanFormulation": "abbrev BooleanType := Bool",
    "formulationSource": "urn:csabs:source/local-lean-CoreData",
    "formulationLocator": "Catalog.BooleanType",
    "formulationScope": "model",
    "leanModelMapping": "Bool = {false,true}. Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.",
    "leanModelLimitations": "Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.",
    "mathematicalFormulation": "Bool={false,true}; neg(false)=true and neg(true)=false. This is a two-constructor value type, with constructor equality, distinct from the universe Prop of propositions."
  },
  {
    "id": "urn:csabs:operation/BooleanType-false",
    "type": "Operation",
    "name": "false",
    "signature": "false : Bool",
    "description": "Constructs false.",
    "concept": "urn:csabs:concept/BooleanType",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Constructs false.",
    "source": [
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BooleanType-true",
    "type": "Operation",
    "name": "true",
    "signature": "true : Bool",
    "description": "Constructs true.",
    "concept": "urn:csabs:concept/BooleanType",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Constructs true.",
    "source": [
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BooleanType-case",
    "type": "Operation",
    "name": "case",
    "signature": "case : C×C×Bool→C",
    "description": "case(x,y,false)=x; case(x,y,true)=y.",
    "concept": "urn:csabs:concept/BooleanType",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "case(x,y,false)=x; case(x,y,true)=y.",
    "source": [
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BooleanType-not",
    "type": "Operation",
    "name": "not",
    "signature": "not : Bool→Bool",
    "description": "not(false)=true; not(true)=false.",
    "concept": "urn:csabs:concept/BooleanType",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "not(false)=true; not(true)=false.",
    "source": [
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/BooleanType-enumeration",
    "type": "Axiom",
    "name": "enumeration",
    "statement": "Defining requirement: false≠true ∧ ∀b:Bool, b=false ∨ b=true",
    "formalStatement": "false≠true ∧ ∀b:Bool, b=false ∨ b=true",
    "assumptions": [
      "Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BooleanType"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/BooleanType-case-beta",
    "type": "Axiom",
    "name": "case-beta",
    "statement": "Defining requirement: case(x,y,false)=x ∧ case(x,y,true)=y",
    "formalStatement": "case(x,y,false)=x ∧ case(x,y,true)=y",
    "assumptions": [
      "Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BooleanType"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/BooleanType-not-equations",
    "type": "Axiom",
    "name": "not-equations",
    "statement": "Defining requirement: not(false)=true ∧ not(true)=false",
    "formalStatement": "not(false)=true ∧ not(true)=false",
    "assumptions": [
      "Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BooleanType"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/BooleanType-double-negation",
    "type": "Law",
    "name": "double-negation",
    "statement": "∀b:Bool, not(not(b))=b",
    "formalStatement": "∀b:Bool, not(not(b))=b",
    "assumptions": [
      "Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/BooleanType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BooleanType-enumeration",
      "urn:csabs:axiom/BooleanType-not-equations"
    ],
    "proofSketch": "Split on the two enumeration cases and compute negation twice.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (b : Catalog.BooleanType), !(!b) = b",
    "formulationSource": "urn:csabs:source/local-lean-CoreData",
    "formulationLocator": "Catalog.CoreDataProofs.bool_not_not",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Bool has the two disjoint constructors false/true; not is Lean Bool.not; equality is Boolean value equality. Case elimination supplies enumeration and not-equations.",
    "leanModelLimitations": "Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/BooleanType-enumeration\": \"Interpreted premise: false≠true ∧ ∀b:Bool, b=false ∨ b=true. Bool has the two disjoint constructors false/true; not is Lean Bool.not; equality is Boolean value equality. Case elimination supplies enumeration and not-equations.\", \"urn:csabs:axiom/BooleanType-not-equations\": \"Interpreted premise: not(false)=true ∧ not(true)=false. Bool has the two disjoint constructors false/true; not is Lean Bool.not; equality is Boolean value equality. Case elimination supplies enumeration and not-equations.\"}"
  },
  {
    "id": "urn:csabs:theorem/BooleanType-case-uniqueness",
    "type": "Theorem",
    "name": "case-uniqueness",
    "statement": "(f(false)=x ∧ f(true)=y) ⇒ ∀b, f(b)=case(x,y,b)",
    "formalStatement": "(f(false)=x ∧ f(true)=y) ⇒ ∀b, f(b)=case(x,y,b)",
    "assumptions": [
      "Value equality is tagged equality. These are Boolean values, not arbitrary propositions, three-valued SQL logic or bit vectors.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/BooleanType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BooleanType-enumeration",
      "urn:csabs:axiom/BooleanType-case-beta"
    ],
    "proofSketch": "Case split on b and use both beta equations.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
