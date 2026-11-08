# Modular Integer

An integer residue class modulo an explicit integer modulus n≥2.

**Notation:** ℤ/nℤ; [a]=[b] iff n divides a−b

**Stable ID:** `urn:csabs:concept/ModularInteger`

**Categories:** Numeric computation

**Kind:** Mathematical structure

**Prerequisites:** [Unital ring (convention stated)](Ring.md), [Field](Field.md)

## Backlinks

- [Finite field (Galois field)](FiniteField.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected presentation: An integer residue class modulo an explicit integer modulus n≥2. Governing rules: Residue equivalence and operations are induced from integers modulo a fixed n≥2.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-ModularInteger-add"></a>

### add

`urn:csabs:operation/ModularInteger-add`

**signature:** + : (ℤ/nℤ)²→ℤ/nℤ

**description:** Adds residue classes.

<a id="node-urn-csabs-operation-ModularInteger-multiply"></a>

### multiply

`urn:csabs:operation/ModularInteger-multiply`

**signature:** × : (ℤ/nℤ)²→ℤ/nℤ

**description:** Multiplies residue classes.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ModularInteger-quotient"></a>

### quotient

`urn:csabs:axiom/ModularInteger-quotient`

**statement:** Residue equivalence and operations are induced from integers modulo a fixed n≥2.

**formalStatement:** a~b iff n divides a−b; [a]+[b]=[a+b]; [a]·[b]=[ab]; −[a]=[−a]

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-law-ModularInteger-core"></a>

### law/ModularInteger-core

`urn:csabs:law/ModularInteger-core`

**statement:** The residue ring is a field exactly when the modulus is prime.

**formalStatement:** ℤ/nℤ is a field iff n prime

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [quotient](ModularInteger.md#node-urn-csabs-axiom-ModularInteger-quotient)

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-theorem-ModularInteger-operations-well-defined"></a>

### operations-well-defined

`urn:csabs:theorem/ModularInteger-operations-well-defined`

**statement:** Changing integer representatives does not change residue addition or multiplication.

**formalStatement:** a≡a′ mod n ∧ b≡b′ mod n ⇒ a+b≡a′+b′ mod n ∧ ab≡a′b′ mod n

**proofSketch:** Sums and products of congruent integers differ by multiples of n.

**assumptions:** The explicit basis, carriers, and side conditions stated for ModularInteger apply.

**dependsOn:** [quotient](ModularInteger.md#node-urn-csabs-axiom-ModularInteger-quotient)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

Historical source gap retained; see `provenanceStatus` and the frozen baseline.

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ModularInteger",
    "type": "Concept",
    "shortForm": "ModularInteger",
    "fullName": "Modular Integer",
    "category": [
      "urn:csabs:category/numeric-computation"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "An integer residue class modulo an explicit integer modulus n≥2.",
    "notation": "ℤ/nℤ; [a]=[b] iff n divides a−b",
    "hasOperation": [
      "urn:csabs:operation/ModularInteger-add",
      "urn:csabs:operation/ModularInteger-multiply"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ModularInteger-quotient"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:law/ModularInteger-core",
      "urn:csabs:theorem/ModularInteger-operations-well-defined"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Ring",
      "urn:csabs:concept/Field"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: An integer residue class modulo an explicit integer modulus n≥2. Governing rules: Residue equivalence and operations are induced from integers modulo a fixed n≥2.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:operation/ModularInteger-add",
    "type": "Operation",
    "name": "add",
    "signature": "+ : (ℤ/nℤ)²→ℤ/nℤ",
    "description": "Adds residue classes.",
    "concept": "urn:csabs:concept/ModularInteger"
  },
  {
    "id": "urn:csabs:operation/ModularInteger-multiply",
    "type": "Operation",
    "name": "multiply",
    "signature": "× : (ℤ/nℤ)²→ℤ/nℤ",
    "description": "Multiplies residue classes.",
    "concept": "urn:csabs:concept/ModularInteger"
  },
  {
    "id": "urn:csabs:axiom/ModularInteger-quotient",
    "type": "Axiom",
    "name": "quotient",
    "statement": "Residue equivalence and operations are induced from integers modulo a fixed n≥2.",
    "formalStatement": "a~b iff n divides a−b; [a]+[b]=[a+b]; [a]·[b]=[ab]; −[a]=[−a]",
    "appliesTo": [
      "urn:csabs:concept/ModularInteger"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/ModularInteger-core",
    "type": "Theorem",
    "statement": "The residue ring is a field exactly when the modulus is prime.",
    "formalStatement": "ℤ/nℤ is a field iff n prime",
    "appliesTo": [
      "urn:csabs:concept/ModularInteger"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/ModularInteger-quotient"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/ModularInteger-operations-well-defined",
    "type": "Theorem",
    "name": "operations-well-defined",
    "statement": "Changing integer representatives does not change residue addition or multiplication.",
    "formalStatement": "a≡a′ mod n ∧ b≡b′ mod n ⇒ a+b≡a′+b′ mod n ∧ ab≡a′b′ mod n",
    "proofSketch": "Sums and products of congruent integers differ by multiples of n.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for ModularInteger apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/ModularInteger"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ModularInteger-quotient"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
