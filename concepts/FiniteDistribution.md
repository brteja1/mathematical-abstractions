# Finitely supported probability distribution

An exactly normalized nonnegative mass function with finite support on a value carrier.

**Notation:** Dist_fin(A)={p:A→ℝ≥0 | supp(p) finite, Σa p(a)=1}

**Stable ID:** `urn:csabs:concept/FiniteDistribution`

**Categories:** Probability and stochastic models

**Kind:** Abstract data type

**Prerequisites:** [Probability space (normalized measure)](ProbabilitySpace.md), [Finitely supported vector](SparseVector.md), [Finite set collection](FiniteSet.md)

## Interface and scope

**axiomBasis:** supp(p)={a | p(a)≠0} is finite; p(a)≥0; Σa∈supp(p) p(a)=1; dirac(a)(x)=1 if x=a, else 0; push(f,p)(b)=Σ{a∈supp(p) | f(a)=b}p(a); equality is pointwise

**basisKind:** extensional-structural-definition

**basisScope:** Ambient A may be infinite. No distribution exists on empty A. Exact real probabilities; no random generator, floating-point error or independent sampling assumption. Equality is pointwise mass equality.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-FiniteDistribution-mass"></a>

### mass

`urn:csabs:operation/FiniteDistribution-mass`

**signature:** mass : Dist_fin(A)×A→ℝ≥0

**description:** Returns exact mass at a.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Ambient A may be infinite. No distribution exists on empty A. Exact real probabilities; no random generator, floating-point error or independent sampling assumption. Equality is pointwise mass equality.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns exact mass at a.

**source:** [Mathlib pinned definitions: Probability/ProbabilityMassFunction/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/ProbabilityMassFunction/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** PMF, PMF.ext, hasSum_coe_one and support_nonempty; restricted here to finite support; Finsupp finite support carrier and extensional evaluation

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-FiniteDistribution-dirac"></a>

### dirac

`urn:csabs:operation/FiniteDistribution-dirac`

**signature:** dirac : A→Dist_fin(A)

**description:** Mass one at a, zero elsewhere.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Ambient A may be infinite. No distribution exists on empty A. Exact real probabilities; no random generator, floating-point error or independent sampling assumption. Equality is pointwise mass equality.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Mass one at a, zero elsewhere.

**source:** [Mathlib pinned definitions: Probability/ProbabilityMassFunction/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/ProbabilityMassFunction/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** PMF, PMF.ext, hasSum_coe_one and support_nonempty; restricted here to finite support; Finsupp finite support carrier and extensional evaluation

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-FiniteDistribution-pushforward"></a>

### pushforward

`urn:csabs:operation/FiniteDistribution-pushforward`

**signature:** push : (A→B)×Dist_fin(A)→Dist_fin(B)

**description:** push(f,p)(b)=Σ{a∈supp(p) | f(a)=b}p(a).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Ambient A may be infinite. No distribution exists on empty A. Exact real probabilities; no random generator, floating-point error or independent sampling assumption. Equality is pointwise mass equality.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** push(f,p)(b)=Σ{a∈supp(p) | f(a)=b}p(a).

**source:** [Mathlib pinned definitions: Probability/ProbabilityMassFunction/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/ProbabilityMassFunction/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** PMF, PMF.ext, hasSum_coe_one and support_nonempty; restricted here to finite support; Finsupp finite support carrier and extensional evaluation

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-FiniteDistribution-normalized-support"></a>

### normalized-support

`urn:csabs:axiom/FiniteDistribution-normalized-support`

**statement:** Defining requirement: supp(p)={a | p(a)≠0} is finite; p(a)≥0; Σa∈supp(p) p(a)=1

**formalStatement:** supp(p)={a | p(a)≠0} is finite; p(a)≥0; Σa∈supp(p) p(a)=1

**assumptions:** Ambient A may be infinite. No distribution exists on empty A. Exact real probabilities; no random generator, floating-point error or independent sampling assumption. Equality is pointwise mass equality.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Probability/ProbabilityMassFunction/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/ProbabilityMassFunction/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** PMF, PMF.ext, hasSum_coe_one and support_nonempty; restricted here to finite support; Finsupp finite support carrier and extensional evaluation

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-FiniteDistribution-dirac-equation"></a>

### dirac-equation

`urn:csabs:axiom/FiniteDistribution-dirac-equation`

**statement:** Defining requirement: dirac(a)(x)=1 if x=a, else 0

**formalStatement:** dirac(a)(x)=1 if x=a, else 0

**assumptions:** Ambient A may be infinite. No distribution exists on empty A. Exact real probabilities; no random generator, floating-point error or independent sampling assumption. Equality is pointwise mass equality.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Probability/ProbabilityMassFunction/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/ProbabilityMassFunction/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** PMF, PMF.ext, hasSum_coe_one and support_nonempty; restricted here to finite support; Finsupp finite support carrier and extensional evaluation

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-FiniteDistribution-push-equation"></a>

### push-equation

`urn:csabs:axiom/FiniteDistribution-push-equation`

**statement:** Defining requirement: push(f,p)(b)=Σ{a∈supp(p) | f(a)=b}p(a); equality is pointwise

**formalStatement:** push(f,p)(b)=Σ{a∈supp(p) | f(a)=b}p(a); equality is pointwise

**assumptions:** Ambient A may be infinite. No distribution exists on empty A. Exact real probabilities; no random generator, floating-point error or independent sampling assumption. Equality is pointwise mass equality.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Probability/ProbabilityMassFunction/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/ProbabilityMassFunction/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** PMF, PMF.ext, hasSum_coe_one and support_nonempty; restricted here to finite support; Finsupp finite support carrier and extensional evaluation

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-FiniteDistribution-nonempty-support"></a>

### nonempty-support

`urn:csabs:law/FiniteDistribution-nonempty-support`

**statement:** supp(p)≠∅

**formalStatement:** supp(p)≠∅

**assumptions:** Ambient A may be infinite. No distribution exists on empty A. Exact real probabilities; no random generator, floating-point error or independent sampling assumption. Equality is pointwise mass equality.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [normalized-support](FiniteDistribution.md#node-urn-csabs-axiom-FiniteDistribution-normalized-support)

**proofSketch:** If support were empty its sum would be zero, contradicting normalization 1.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Probability/ProbabilityMassFunction/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/ProbabilityMassFunction/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** PMF, PMF.ext, hasSum_coe_one and support_nonempty; restricted here to finite support; Finsupp finite support carrier and extensional evaluation

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-FiniteDistribution-push-identity"></a>

### push-identity

`urn:csabs:theorem/FiniteDistribution-push-identity`

**statement:** push(id,p)=p

**formalStatement:** push(id,p)=p

**assumptions:** Ambient A may be infinite. No distribution exists on empty A. Exact real probabilities; no random generator, floating-point error or independent sampling assumption. Equality is pointwise mass equality.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [normalized-support](FiniteDistribution.md#node-urn-csabs-axiom-FiniteDistribution-normalized-support); [push-equation](FiniteDistribution.md#node-urn-csabs-axiom-FiniteDistribution-push-equation)

**proofSketch:** For each b only a=b can contribute, giving p(b), including zero outside support; use pointwise equality.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Probability/ProbabilityMassFunction/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/ProbabilityMassFunction/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** PMF, PMF.ext, hasSum_coe_one and support_nonempty; restricted here to finite support; Finsupp finite support carrier and extensional evaluation

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Mathlib pinned definitions: Probability/ProbabilityMassFunction/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/ProbabilityMassFunction/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference
- [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** PMF, PMF.ext, hasSum_coe_one and support_nonempty; restricted here to finite support; Finsupp finite support carrier and extensional evaluation

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/FiniteDistribution",
    "type": "Concept",
    "shortForm": "FiniteDistribution",
    "fullName": "Finitely supported probability distribution",
    "category": [
      "urn:csabs:category/probability"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "An exactly normalized nonnegative mass function with finite support on a value carrier.",
    "notation": "Dist_fin(A)={p:A→ℝ≥0 | supp(p) finite, Σa p(a)=1}",
    "requiresConcept": [
      "urn:csabs:concept/ProbabilitySpace",
      "urn:csabs:concept/SparseVector",
      "urn:csabs:concept/FiniteSet"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/FiniteDistribution-mass",
      "urn:csabs:operation/FiniteDistribution-dirac",
      "urn:csabs:operation/FiniteDistribution-pushforward"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/FiniteDistribution-normalized-support",
      "urn:csabs:axiom/FiniteDistribution-dirac-equation",
      "urn:csabs:axiom/FiniteDistribution-push-equation"
    ],
    "hasLaw": [
      "urn:csabs:law/FiniteDistribution-nonempty-support"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/FiniteDistribution-push-identity"
    ],
    "axiomBasis": "supp(p)={a | p(a)≠0} is finite; p(a)≥0; Σa∈supp(p) p(a)=1; dirac(a)(x)=1 if x=a, else 0; push(f,p)(b)=Σ{a∈supp(p) | f(a)=b}p(a); equality is pointwise",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Ambient A may be infinite. No distribution exists on empty A. Exact real probabilities; no random generator, floating-point error or independent sampling assumption. Equality is pointwise mass equality.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/mathlib-pmf-core",
      "urn:csabs:source/mathlib-finsupp-core"
    ],
    "sourceLocator": "PMF, PMF.ext, hasSum_coe_one and support_nonempty; restricted here to finite support; Finsupp finite support carrier and extensional evaluation",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/FiniteDistribution-mass",
    "type": "Operation",
    "name": "mass",
    "signature": "mass : Dist_fin(A)×A→ℝ≥0",
    "description": "Returns exact mass at a.",
    "concept": "urn:csabs:concept/FiniteDistribution",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Ambient A may be infinite. No distribution exists on empty A. Exact real probabilities; no random generator, floating-point error or independent sampling assumption. Equality is pointwise mass equality.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns exact mass at a.",
    "source": [
      "urn:csabs:source/mathlib-pmf-core",
      "urn:csabs:source/mathlib-finsupp-core"
    ],
    "sourceLocator": "PMF, PMF.ext, hasSum_coe_one and support_nonempty; restricted here to finite support; Finsupp finite support carrier and extensional evaluation",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/FiniteDistribution-dirac",
    "type": "Operation",
    "name": "dirac",
    "signature": "dirac : A→Dist_fin(A)",
    "description": "Mass one at a, zero elsewhere.",
    "concept": "urn:csabs:concept/FiniteDistribution",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Ambient A may be infinite. No distribution exists on empty A. Exact real probabilities; no random generator, floating-point error or independent sampling assumption. Equality is pointwise mass equality.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Mass one at a, zero elsewhere.",
    "source": [
      "urn:csabs:source/mathlib-pmf-core",
      "urn:csabs:source/mathlib-finsupp-core"
    ],
    "sourceLocator": "PMF, PMF.ext, hasSum_coe_one and support_nonempty; restricted here to finite support; Finsupp finite support carrier and extensional evaluation",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/FiniteDistribution-pushforward",
    "type": "Operation",
    "name": "pushforward",
    "signature": "push : (A→B)×Dist_fin(A)→Dist_fin(B)",
    "description": "push(f,p)(b)=Σ{a∈supp(p) | f(a)=b}p(a).",
    "concept": "urn:csabs:concept/FiniteDistribution",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Ambient A may be infinite. No distribution exists on empty A. Exact real probabilities; no random generator, floating-point error or independent sampling assumption. Equality is pointwise mass equality.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "push(f,p)(b)=Σ{a∈supp(p) | f(a)=b}p(a).",
    "source": [
      "urn:csabs:source/mathlib-pmf-core",
      "urn:csabs:source/mathlib-finsupp-core"
    ],
    "sourceLocator": "PMF, PMF.ext, hasSum_coe_one and support_nonempty; restricted here to finite support; Finsupp finite support carrier and extensional evaluation",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/FiniteDistribution-normalized-support",
    "type": "Axiom",
    "name": "normalized-support",
    "statement": "Defining requirement: supp(p)={a | p(a)≠0} is finite; p(a)≥0; Σa∈supp(p) p(a)=1",
    "formalStatement": "supp(p)={a | p(a)≠0} is finite; p(a)≥0; Σa∈supp(p) p(a)=1",
    "assumptions": [
      "Ambient A may be infinite. No distribution exists on empty A. Exact real probabilities; no random generator, floating-point error or independent sampling assumption. Equality is pointwise mass equality.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteDistribution"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-pmf-core",
      "urn:csabs:source/mathlib-finsupp-core"
    ],
    "sourceLocator": "PMF, PMF.ext, hasSum_coe_one and support_nonempty; restricted here to finite support; Finsupp finite support carrier and extensional evaluation",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/FiniteDistribution-dirac-equation",
    "type": "Axiom",
    "name": "dirac-equation",
    "statement": "Defining requirement: dirac(a)(x)=1 if x=a, else 0",
    "formalStatement": "dirac(a)(x)=1 if x=a, else 0",
    "assumptions": [
      "Ambient A may be infinite. No distribution exists on empty A. Exact real probabilities; no random generator, floating-point error or independent sampling assumption. Equality is pointwise mass equality.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteDistribution"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-pmf-core",
      "urn:csabs:source/mathlib-finsupp-core"
    ],
    "sourceLocator": "PMF, PMF.ext, hasSum_coe_one and support_nonempty; restricted here to finite support; Finsupp finite support carrier and extensional evaluation",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/FiniteDistribution-push-equation",
    "type": "Axiom",
    "name": "push-equation",
    "statement": "Defining requirement: push(f,p)(b)=Σ{a∈supp(p) | f(a)=b}p(a); equality is pointwise",
    "formalStatement": "push(f,p)(b)=Σ{a∈supp(p) | f(a)=b}p(a); equality is pointwise",
    "assumptions": [
      "Ambient A may be infinite. No distribution exists on empty A. Exact real probabilities; no random generator, floating-point error or independent sampling assumption. Equality is pointwise mass equality.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteDistribution"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-pmf-core",
      "urn:csabs:source/mathlib-finsupp-core"
    ],
    "sourceLocator": "PMF, PMF.ext, hasSum_coe_one and support_nonempty; restricted here to finite support; Finsupp finite support carrier and extensional evaluation",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/FiniteDistribution-nonempty-support",
    "type": "Law",
    "name": "nonempty-support",
    "statement": "supp(p)≠∅",
    "formalStatement": "supp(p)≠∅",
    "assumptions": [
      "Ambient A may be infinite. No distribution exists on empty A. Exact real probabilities; no random generator, floating-point error or independent sampling assumption. Equality is pointwise mass equality.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteDistribution"
    ],
    "dependsOn": [
      "urn:csabs:axiom/FiniteDistribution-normalized-support"
    ],
    "proofSketch": "If support were empty its sum would be zero, contradicting normalization 1.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-pmf-core",
      "urn:csabs:source/mathlib-finsupp-core"
    ],
    "sourceLocator": "PMF, PMF.ext, hasSum_coe_one and support_nonempty; restricted here to finite support; Finsupp finite support carrier and extensional evaluation",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/FiniteDistribution-push-identity",
    "type": "Theorem",
    "name": "push-identity",
    "statement": "push(id,p)=p",
    "formalStatement": "push(id,p)=p",
    "assumptions": [
      "Ambient A may be infinite. No distribution exists on empty A. Exact real probabilities; no random generator, floating-point error or independent sampling assumption. Equality is pointwise mass equality.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteDistribution"
    ],
    "dependsOn": [
      "urn:csabs:axiom/FiniteDistribution-normalized-support",
      "urn:csabs:axiom/FiniteDistribution-push-equation"
    ],
    "proofSketch": "For each b only a=b can contribute, giving p(b), including zero outside support; use pointwise equality.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-pmf-core",
      "urn:csabs:source/mathlib-finsupp-core"
    ],
    "sourceLocator": "PMF, PMF.ext, hasSum_coe_one and support_nonempty; restricted here to finite support; Finsupp finite support carrier and extensional evaluation",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
