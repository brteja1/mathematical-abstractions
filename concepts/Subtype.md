# Predicate-restricted subtype

Values of a carrier A satisfying a fixed predicate P, with evidence irrelevant to value equality.

**Notation:** {a:A | P(a)}

**Stable ID:** `urn:csabs:concept/Subtype`

**Categories:** Types and semantics

**Kind:** Numeric data type

**Prerequisites:** [Set](Set.md), [Predicate Logic](PredicateLogic.md)

## Backlinks

- [Behavioral subtyping with explicit history constraints](BehavioralSubtyping.md) — `relatedConcept`
- [Java wildcard capture with fresh bounded variables](JavaWildcardCapture.md) — `relatedConcept`

## Mathematical formulation

{a:A | P(a)} consists of pairs (a,h) with h:P(a). Equality is determined by the underlying a, with proof components irrelevant; the carrier may be empty.

**Lean formulation** (in its source module context):

```lean
abbrev Subtype (A : Type u) (P : A → Prop) := {a : A // P a}
```

**Source:** [`Catalog.Subtype`](../lean/Catalog/CoreData.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Lean Subtype P, with proof-irrelevant P: A→Prop. {a:A | P(a)}. P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.

**Limits:** Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** value(pack(a,h))=a; ∀x:Subtype(A,P), P(value(x)); x=y ⇔ value(x)=value(y)

**basisKind:** extensional-structural-definition

**basisScope:** P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Subtype-pack"></a>

### pack

`urn:csabs:operation/Subtype-pack`

**signature:** pack : (a:A)→P(a)→Subtype(A,P)

**description:** Packages a value with its predicate evidence.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Packages a value with its predicate evidence.

**source:** [Mathlib pinned definitions: Data/Subtype.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Subtype.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Subtype carrier/property and value coercion; Subtype.heq_iff_coe_eq

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Subtype-value"></a>

### value

`urn:csabs:operation/Subtype-value`

**signature:** value : Subtype(A,P)→A

**description:** Forgets evidence.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Forgets evidence.

**source:** [Mathlib pinned definitions: Data/Subtype.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Subtype.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Subtype carrier/property and value coercion; Subtype.heq_iff_coe_eq

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Subtype-property"></a>

### property

`urn:csabs:operation/Subtype-property`

**signature:** property : (x:Subtype(A,P))→P(value(x))

**description:** Eliminates the stored evidence.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Eliminates the stored evidence.

**source:** [Mathlib pinned definitions: Data/Subtype.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Subtype.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Subtype carrier/property and value coercion; Subtype.heq_iff_coe_eq

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Subtype-pack-beta"></a>

### pack-beta

`urn:csabs:axiom/Subtype-pack-beta`

**statement:** Defining requirement: value(pack(a,h))=a

**formalStatement:** value(pack(a,h))=a

**assumptions:** P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Data/Subtype.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Subtype.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Subtype carrier/property and value coercion; Subtype.heq_iff_coe_eq

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Subtype-soundness"></a>

### soundness

`urn:csabs:axiom/Subtype-soundness`

**statement:** Defining requirement: ∀x:Subtype(A,P), P(value(x))

**formalStatement:** ∀x:Subtype(A,P), P(value(x))

**assumptions:** P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Data/Subtype.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Subtype.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Subtype carrier/property and value coercion; Subtype.heq_iff_coe_eq

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Subtype-value-equality"></a>

### value-equality

`urn:csabs:axiom/Subtype-value-equality`

**statement:** Defining requirement: x=y ⇔ value(x)=value(y)

**formalStatement:** x=y ⇔ value(x)=value(y)

**assumptions:** P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Data/Subtype.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Subtype.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Subtype carrier/property and value coercion; Subtype.heq_iff_coe_eq

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-Subtype-value-injective"></a>

### value-injective

`urn:csabs:law/Subtype-value-injective`

**statement:** value(x)=value(y) ⇒ x=y

**formalStatement:** value(x)=value(y) ⇒ x=y

**assumptions:** P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [value-equality](Subtype.md#node-urn-csabs-axiom-Subtype-value-equality)

**proofSketch:** Use the backward direction of value-equality.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Data/Subtype.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Subtype.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Subtype carrier/property and value coercion; Subtype.heq_iff_coe_eq

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type} {P : A → Prop} (x y : Catalog.Subtype A P), x.val = y.val → x = y
```

**Source:** [`Catalog.CoreDataProofs.subtype_value_injective`](../lean/Catalog/CoreData.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Subtype P uses proof-irrelevant predicate evidence; value is .val. Subtype.ext identifies values with equal underlying carriers, independently of proof witnesses.

**Limits:** Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/Subtype-value-equality": "Interpreted premise: x=y ⇔ value(x)=value(y). Subtype P uses proof-irrelevant predicate evidence; value is .val. Subtype.ext identifies values with equal underlying carriers, independently of proof witnesses."
}
```

## Theorems

<a id="node-urn-csabs-theorem-Subtype-empty-subtype"></a>

### empty-subtype

`urn:csabs:theorem/Subtype-empty-subtype`

**statement:** (∀a:A, ¬P(a)) ⇒ Subtype(A,P) has no values

**formalStatement:** (∀a:A, ¬P(a)) ⇒ Subtype(A,P) has no values

**assumptions:** P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [soundness](Subtype.md#node-urn-csabs-axiom-Subtype-soundness)

**proofSketch:** An inhabitant would yield P(value(x)) by soundness.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Data/Subtype.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Subtype.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Subtype carrier/property and value coercion; Subtype.heq_iff_coe_eq

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Mathlib pinned definitions: Data/Subtype.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Subtype.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Subtype carrier/property and value coercion; Subtype.heq_iff_coe_eq

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Subtype",
    "type": "Concept",
    "shortForm": "Subtype",
    "fullName": "Predicate-restricted subtype",
    "category": [
      "urn:csabs:category/types"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "Values of a carrier A satisfying a fixed predicate P, with evidence irrelevant to value equality.",
    "notation": "{a:A | P(a)}",
    "requiresConcept": [
      "urn:csabs:concept/Set",
      "urn:csabs:concept/PredicateLogic"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/Subtype-pack",
      "urn:csabs:operation/Subtype-value",
      "urn:csabs:operation/Subtype-property"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Subtype-pack-beta",
      "urn:csabs:axiom/Subtype-soundness",
      "urn:csabs:axiom/Subtype-value-equality"
    ],
    "hasLaw": [
      "urn:csabs:law/Subtype-value-injective"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Subtype-empty-subtype"
    ],
    "axiomBasis": "value(pack(a,h))=a; ∀x:Subtype(A,P), P(value(x)); x=y ⇔ value(x)=value(y)",
    "basisKind": "extensional-structural-definition",
    "basisScope": "P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/mathlib-subtype-core"
    ],
    "sourceLocator": "Subtype carrier/property and value coercion; Subtype.heq_iff_coe_eq",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev Subtype (A : Type u) (P : A → Prop) := {a : A // P a}",
    "formulationSource": "urn:csabs:source/local-lean-CoreData",
    "formulationLocator": "Catalog.Subtype",
    "formulationScope": "model",
    "leanModelMapping": "Lean Subtype P, with proof-irrelevant P: A→Prop. {a:A | P(a)}. P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.",
    "leanModelLimitations": "Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.",
    "mathematicalFormulation": "{a:A | P(a)} consists of pairs (a,h) with h:P(a). Equality is determined by the underlying a, with proof components irrelevant; the carrier may be empty."
  },
  {
    "id": "urn:csabs:operation/Subtype-pack",
    "type": "Operation",
    "name": "pack",
    "signature": "pack : (a:A)→P(a)→Subtype(A,P)",
    "description": "Packages a value with its predicate evidence.",
    "concept": "urn:csabs:concept/Subtype",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Packages a value with its predicate evidence.",
    "source": [
      "urn:csabs:source/mathlib-subtype-core"
    ],
    "sourceLocator": "Subtype carrier/property and value coercion; Subtype.heq_iff_coe_eq",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Subtype-value",
    "type": "Operation",
    "name": "value",
    "signature": "value : Subtype(A,P)→A",
    "description": "Forgets evidence.",
    "concept": "urn:csabs:concept/Subtype",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Forgets evidence.",
    "source": [
      "urn:csabs:source/mathlib-subtype-core"
    ],
    "sourceLocator": "Subtype carrier/property and value coercion; Subtype.heq_iff_coe_eq",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Subtype-property",
    "type": "Operation",
    "name": "property",
    "signature": "property : (x:Subtype(A,P))→P(value(x))",
    "description": "Eliminates the stored evidence.",
    "concept": "urn:csabs:concept/Subtype",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Eliminates the stored evidence.",
    "source": [
      "urn:csabs:source/mathlib-subtype-core"
    ],
    "sourceLocator": "Subtype carrier/property and value coercion; Subtype.heq_iff_coe_eq",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Subtype-pack-beta",
    "type": "Axiom",
    "name": "pack-beta",
    "statement": "Defining requirement: value(pack(a,h))=a",
    "formalStatement": "value(pack(a,h))=a",
    "assumptions": [
      "P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/Subtype"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-subtype-core"
    ],
    "sourceLocator": "Subtype carrier/property and value coercion; Subtype.heq_iff_coe_eq",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Subtype-soundness",
    "type": "Axiom",
    "name": "soundness",
    "statement": "Defining requirement: ∀x:Subtype(A,P), P(value(x))",
    "formalStatement": "∀x:Subtype(A,P), P(value(x))",
    "assumptions": [
      "P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/Subtype"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-subtype-core"
    ],
    "sourceLocator": "Subtype carrier/property and value coercion; Subtype.heq_iff_coe_eq",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Subtype-value-equality",
    "type": "Axiom",
    "name": "value-equality",
    "statement": "Defining requirement: x=y ⇔ value(x)=value(y)",
    "formalStatement": "x=y ⇔ value(x)=value(y)",
    "assumptions": [
      "P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/Subtype"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-subtype-core"
    ],
    "sourceLocator": "Subtype carrier/property and value coercion; Subtype.heq_iff_coe_eq",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/Subtype-value-injective",
    "type": "Law",
    "name": "value-injective",
    "statement": "value(x)=value(y) ⇒ x=y",
    "formalStatement": "value(x)=value(y) ⇒ x=y",
    "assumptions": [
      "P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/Subtype"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Subtype-value-equality"
    ],
    "proofSketch": "Use the backward direction of value-equality.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-subtype-core"
    ],
    "sourceLocator": "Subtype carrier/property and value coercion; Subtype.heq_iff_coe_eq",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type} {P : A → Prop} (x y : Catalog.Subtype A P), x.val = y.val → x = y",
    "formulationSource": "urn:csabs:source/local-lean-CoreData",
    "formulationLocator": "Catalog.CoreDataProofs.subtype_value_injective",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Subtype P uses proof-irrelevant predicate evidence; value is .val. Subtype.ext identifies values with equal underlying carriers, independently of proof witnesses.",
    "leanModelLimitations": "Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/Subtype-value-equality\": \"Interpreted premise: x=y ⇔ value(x)=value(y). Subtype P uses proof-irrelevant predicate evidence; value is .val. Subtype.ext identifies values with equal underlying carriers, independently of proof witnesses.\"}"
  },
  {
    "id": "urn:csabs:theorem/Subtype-empty-subtype",
    "type": "Theorem",
    "name": "empty-subtype",
    "statement": "(∀a:A, ¬P(a)) ⇒ Subtype(A,P) has no values",
    "formalStatement": "(∀a:A, ¬P(a)) ⇒ Subtype(A,P) has no values",
    "assumptions": [
      "P:A→Prop is a mathematical predicate; construction requires evidence of P, not a promise of a runtime decision procedure. The carrier may be empty.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/Subtype"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Subtype-soundness"
    ],
    "proofSketch": "An inhabitant would yield P(value(x)) by soundness.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-subtype-core"
    ],
    "sourceLocator": "Subtype carrier/property and value coercion; Subtype.heq_iff_coe_eq",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
