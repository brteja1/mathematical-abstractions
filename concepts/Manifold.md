# Topological manifold (fixed dimension, without boundary)

A Hausdorff, second-countable topological space locally homeomorphic to open subsets of ℝⁿ for a specified finite dimension n.

**Notation:** (M,τ,n); n∈ℕ; ∀p∈M ∃ chart φ:U≅V, p∈U∈τ, V⊆ℝⁿ open

**Stable ID:** `urn:csabs:concept/Manifold`

**Categories:** Geometry and manifolds, Topology

**Kind:** Mathematical structure

**Prerequisites:** [Topological space (topology on a carrier)](TopologicalSpace.md), [Partial function](PartialFunction.md)

**Specializes:** [Topological space (topology on a carrier)](TopologicalSpace.md)

**Related concepts:** [Smooth manifold (C∞, without boundary)](SmoothManifold.md)

## Backlinks

- [Smooth manifold (C∞, without boundary)](SmoothManifold.md) — `requiresConcept`
- [Smooth manifold (C∞, without boundary)](SmoothManifold.md) — `specializationOf`

## Interface and scope

**axiomBasis:** Underlying TopologicalSpace; Hausdorff separation; a countable basis; and a covering atlas of homeomorphisms into open subsets of ℝⁿ.

**basisKind:** defined-structure

**basisScope:** Finite fixed-dimensional topological manifolds without boundary and chart transformations; no differentiable structure or metric is supplied.

**basisInstantiation:** Instantiate TopologicalSpace at (M,τ). Add the stated Hausdorff, countable-basis and chart-cover requirements at the declared n.

**specializationNote:** Forget dimension and chart data; retain M and its topology.

**verificationObligation:** n=0 is permitted. The empty manifold is permitted at any declared n; its dimension cannot be inferred from the empty carrier.; Do not assume a global chart or an ambient Euclidean embedding. Manifolds with boundary or corners require explicit variants.; Use the stated carriers and equality. Specialization does not automatically transfer operations or claims.

**reviewStatus:** editorial interface review; not machine-proved

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Manifold-coordinate"></a>

### coordinate

`urn:csabs:operation/Manifold-coordinate`

**signature:** U → V⊆ℝⁿ; p ↦ φ(p)

**description:** Evaluate a selected chart at a point in its open domain.

**precondition:** (U,φ) is a chart and p∈U.

**postcondition:** Evaluate a selected chart at a point in its open domain.

**totality:** total on U; partial on M

<a id="node-urn-csabs-operation-Manifold-inverse-coordinate"></a>

### inverse-coordinate

`urn:csabs:operation/Manifold-inverse-coordinate`

**signature:** V → U; y ↦ φ⁻¹(y)

**description:** Recover a point from coordinates in the chart image.

**precondition:** y∈V=φ(U).

**postcondition:** Recover a point from coordinates in the chart image.

**totality:** total on V; partial on ℝⁿ

<a id="node-urn-csabs-operation-Manifold-transition"></a>

### transition

`urn:csabs:operation/Manifold-transition`

**signature:** φ(U∩W) → ψ(U∩W); y ↦ ψ(φ⁻¹(y))

**description:** Change coordinates only on the overlap of two chart domains.

**precondition:** φ:U≅V and ψ:W≅Z are charts; y∈φ(U∩W).

**postcondition:** Change coordinates only on the overlap of two chart domains.

**totality:** total on the overlap image; partial on ℝⁿ

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Manifold-hausdorff"></a>

### hausdorff

`urn:csabs:axiom/Manifold-hausdorff`

**statement:** Distinct points have disjoint open neighborhoods.

**formalStatement:** p,q∈M and p≠q ⇒ ∃U,V∈τ:p∈U ∧ q∈V ∧ U∩V=∅

**assumptions:** (M,τ,n); n∈ℕ; ∀p∈M ∃ chart φ:U≅V, p∈U∈τ, V⊆ℝⁿ open; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [John M. Lee, Introduction to Smooth Manifolds, second edition, Chapter 1 (author-hosted sample)](https://sites.math.washington.edu/~lee/Books/ISM/c01.pdf); citation: John M. Lee, Introduction to Smooth Manifolds, 2nd ed., Springer, 2013, Chapter 1, pp. 1–31. DOI: 10.1007/978-1-4419-9982-5_1.; accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Chapter 1, p. 3

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-Manifold-second-countable"></a>

### second-countable

`urn:csabs:axiom/Manifold-second-countable`

**statement:** The topology has a countable basis.

**formalStatement:** ∃countable ℬ⊆τ:∀U∈τ,∀p∈U,∃B∈ℬ:p∈B⊆U

**assumptions:** (M,τ,n); n∈ℕ; ∀p∈M ∃ chart φ:U≅V, p∈U∈τ, V⊆ℝⁿ open; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [John M. Lee, Introduction to Smooth Manifolds, second edition, Chapter 1 (author-hosted sample)](https://sites.math.washington.edu/~lee/Books/ISM/c01.pdf); citation: John M. Lee, Introduction to Smooth Manifolds, 2nd ed., Springer, 2013, Chapter 1, pp. 1–31. DOI: 10.1007/978-1-4419-9982-5_1.; accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Chapter 1, p. 3

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-Manifold-local-charts"></a>

### local-charts

`urn:csabs:axiom/Manifold-local-charts`

**statement:** Chart domains cover M, and charts are homeomorphisms onto open subsets of ℝⁿ.

**formalStatement:** ⋃_{(U,φ)∈𝒜}U=M; each U open in M and φ:U→V⊆ℝⁿ is bijective, φ and φ⁻¹ continuous, V open

**assumptions:** (M,τ,n); n∈ℕ; ∀p∈M ∃ chart φ:U≅V, p∈U∈τ, V⊆ℝⁿ open; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [John M. Lee, Introduction to Smooth Manifolds, second edition, Chapter 1 (author-hosted sample)](https://sites.math.washington.edu/~lee/Books/ISM/c01.pdf); citation: John M. Lee, Introduction to Smooth Manifolds, 2nd ed., Springer, 2013, Chapter 1, pp. 1–31. DOI: 10.1007/978-1-4419-9982-5_1.; accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Chapter 1, pp. 3–4

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-Manifold-chart-inverses"></a>

### chart-inverses

`urn:csabs:theorem/Manifold-chart-inverses`

**statement:** Chart evaluation and inversion are inverse on their domains.

**formalStatement:** p∈U ⇒ φ⁻¹(φ(p))=p; y∈φ(U) ⇒ φ(φ⁻¹(y))=y

**assumptions:** (M,τ,n); n∈ℕ; ∀p∈M ∃ chart φ:U≅V, p∈U∈τ, V⊆ℝⁿ open; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [John M. Lee, Introduction to Smooth Manifolds, second edition, Chapter 1 (author-hosted sample)](https://sites.math.washington.edu/~lee/Books/ISM/c01.pdf); citation: John M. Lee, Introduction to Smooth Manifolds, 2nd ed., Springer, 2013, Chapter 1, pp. 1–31. DOI: 10.1007/978-1-4419-9982-5_1.; accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Chapter 1, Coordinate Charts, p. 4

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [local-charts](Manifold.md#node-urn-csabs-axiom-Manifold-local-charts); [coordinate](Manifold.md#node-urn-csabs-operation-Manifold-coordinate); [inverse-coordinate](Manifold.md#node-urn-csabs-operation-Manifold-inverse-coordinate)

**proofSketch:** A chart is a bijection with the recorded inverse; apply the two inverse-function identities on their domains.

<a id="node-urn-csabs-theorem-Manifold-transition-cocycle"></a>

### transition-cocycle

`urn:csabs:theorem/Manifold-transition-cocycle`

**statement:** Coordinate changes compose consistently on triple overlaps.

**formalStatement:** on φ(U∩W∩Z): (χ∘ψ⁻¹)∘(ψ∘φ⁻¹)=χ∘φ⁻¹

**assumptions:** (M,τ,n); n∈ℕ; ∀p∈M ∃ chart φ:U≅V, p∈U∈τ, V⊆ℝⁿ open; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [John M. Lee, Introduction to Smooth Manifolds, second edition, Chapter 1 (author-hosted sample)](https://sites.math.washington.edu/~lee/Books/ISM/c01.pdf); citation: John M. Lee, Introduction to Smooth Manifolds, 2nd ed., Springer, 2013, Chapter 1, pp. 1–31. DOI: 10.1007/978-1-4419-9982-5_1.; accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Chapter 1, transition maps, pp. 12–13 (derived overlap identity)

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [chart-inverses](Manifold.md#node-urn-csabs-theorem-Manifold-chart-inverses); [transition](Manifold.md#node-urn-csabs-operation-Manifold-transition)

**proofSketch:** On the triple overlap every intermediate value is in the appropriate chart image. Cancel ψ⁻¹∘ψ and reassociate ordinary function composition.

## Concept provenance

- [John M. Lee, Introduction to Smooth Manifolds, second edition, Chapter 1 (author-hosted sample)](https://sites.math.washington.edu/~lee/Books/ISM/c01.pdf); citation: John M. Lee, Introduction to Smooth Manifolds, 2nd ed., Springer, 2013, Chapter 1, pp. 1–31. DOI: 10.1007/978-1-4419-9982-5_1.; accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Chapter 1, Topological Manifolds, pp. 2–4

**sourceNote:** Interface adapted to the catalog notation and explicitly restricted to the stated scope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Manifold",
    "type": "Concept",
    "shortForm": "Manifold",
    "fullName": "Topological manifold (fixed dimension, without boundary)",
    "category": [
      "urn:csabs:category/geometry",
      "urn:csabs:category/topology"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A Hausdorff, second-countable topological space locally homeomorphic to open subsets of ℝⁿ for a specified finite dimension n.",
    "notation": "(M,τ,n); n∈ℕ; ∀p∈M ∃ chart φ:U≅V, p∈U∈τ, V⊆ℝⁿ open",
    "hasOperation": [
      "urn:csabs:operation/Manifold-coordinate",
      "urn:csabs:operation/Manifold-inverse-coordinate",
      "urn:csabs:operation/Manifold-transition"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Manifold-hausdorff",
      "urn:csabs:axiom/Manifold-second-countable",
      "urn:csabs:axiom/Manifold-local-charts"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/Manifold-chart-inverses",
      "urn:csabs:theorem/Manifold-transition-cocycle"
    ],
    "axiomBasis": "Underlying TopologicalSpace; Hausdorff separation; a countable basis; and a covering atlas of homeomorphisms into open subsets of ℝⁿ.",
    "basisKind": "defined-structure",
    "basisScope": "Finite fixed-dimensional topological manifolds without boundary and chart transformations; no differentiable structure or metric is supplied.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "editorial interface review; not machine-proved",
    "requiresConcept": [
      "urn:csabs:concept/TopologicalSpace",
      "urn:csabs:concept/PartialFunction"
    ],
    "verificationObligation": [
      "n=0 is permitted. The empty manifold is permitted at any declared n; its dimension cannot be inferred from the empty carrier.",
      "Do not assume a global chart or an ambient Euclidean embedding. Manifolds with boundary or corners require explicit variants.",
      "Use the stated carriers and equality. Specialization does not automatically transfer operations or claims."
    ],
    "source": [
      "urn:csabs:source/lee-smooth-manifolds-ch1"
    ],
    "sourceLocator": "Chapter 1, Topological Manifolds, pp. 2–4",
    "sourceNote": "Interface adapted to the catalog notation and explicitly restricted to the stated scope.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/TopologicalSpace"
    ],
    "specializationNote": "Forget dimension and chart data; retain M and its topology.",
    "relatedConcept": [
      "urn:csabs:concept/SmoothManifold"
    ],
    "basisInstantiation": "Instantiate TopologicalSpace at (M,τ). Add the stated Hausdorff, countable-basis and chart-cover requirements at the declared n."
  },
  {
    "id": "urn:csabs:operation/Manifold-coordinate",
    "type": "Operation",
    "name": "coordinate",
    "signature": "U → V⊆ℝⁿ; p ↦ φ(p)",
    "description": "Evaluate a selected chart at a point in its open domain.",
    "concept": "urn:csabs:concept/Manifold",
    "precondition": "(U,φ) is a chart and p∈U.",
    "postcondition": "Evaluate a selected chart at a point in its open domain.",
    "totality": "total on U; partial on M"
  },
  {
    "id": "urn:csabs:operation/Manifold-inverse-coordinate",
    "type": "Operation",
    "name": "inverse-coordinate",
    "signature": "V → U; y ↦ φ⁻¹(y)",
    "description": "Recover a point from coordinates in the chart image.",
    "concept": "urn:csabs:concept/Manifold",
    "precondition": "y∈V=φ(U).",
    "postcondition": "Recover a point from coordinates in the chart image.",
    "totality": "total on V; partial on ℝⁿ"
  },
  {
    "id": "urn:csabs:operation/Manifold-transition",
    "type": "Operation",
    "name": "transition",
    "signature": "φ(U∩W) → ψ(U∩W); y ↦ ψ(φ⁻¹(y))",
    "description": "Change coordinates only on the overlap of two chart domains.",
    "concept": "urn:csabs:concept/Manifold",
    "precondition": "φ:U≅V and ψ:W≅Z are charts; y∈φ(U∩W).",
    "postcondition": "Change coordinates only on the overlap of two chart domains.",
    "totality": "total on the overlap image; partial on ℝⁿ"
  },
  {
    "id": "urn:csabs:axiom/Manifold-hausdorff",
    "type": "Axiom",
    "name": "hausdorff",
    "statement": "Distinct points have disjoint open neighborhoods.",
    "formalStatement": "p,q∈M and p≠q ⇒ ∃U,V∈τ:p∈U ∧ q∈V ∧ U∩V=∅",
    "appliesTo": [
      "urn:csabs:concept/Manifold"
    ],
    "assumptions": [
      "(M,τ,n); n∈ℕ; ∀p∈M ∃ chart φ:U≅V, p∈U∈τ, V⊆ℝⁿ open",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/lee-smooth-manifolds-ch1"
    ],
    "sourceLocator": "Chapter 1, p. 3",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/Manifold-second-countable",
    "type": "Axiom",
    "name": "second-countable",
    "statement": "The topology has a countable basis.",
    "formalStatement": "∃countable ℬ⊆τ:∀U∈τ,∀p∈U,∃B∈ℬ:p∈B⊆U",
    "appliesTo": [
      "urn:csabs:concept/Manifold"
    ],
    "assumptions": [
      "(M,τ,n); n∈ℕ; ∀p∈M ∃ chart φ:U≅V, p∈U∈τ, V⊆ℝⁿ open",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/lee-smooth-manifolds-ch1"
    ],
    "sourceLocator": "Chapter 1, p. 3",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/Manifold-local-charts",
    "type": "Axiom",
    "name": "local-charts",
    "statement": "Chart domains cover M, and charts are homeomorphisms onto open subsets of ℝⁿ.",
    "formalStatement": "⋃_{(U,φ)∈𝒜}U=M; each U open in M and φ:U→V⊆ℝⁿ is bijective, φ and φ⁻¹ continuous, V open",
    "appliesTo": [
      "urn:csabs:concept/Manifold"
    ],
    "assumptions": [
      "(M,τ,n); n∈ℕ; ∀p∈M ∃ chart φ:U≅V, p∈U∈τ, V⊆ℝⁿ open",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/lee-smooth-manifolds-ch1"
    ],
    "sourceLocator": "Chapter 1, pp. 3–4",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:theorem/Manifold-chart-inverses",
    "type": "Theorem",
    "name": "chart-inverses",
    "statement": "Chart evaluation and inversion are inverse on their domains.",
    "formalStatement": "p∈U ⇒ φ⁻¹(φ(p))=p; y∈φ(U) ⇒ φ(φ⁻¹(y))=y",
    "appliesTo": [
      "urn:csabs:concept/Manifold"
    ],
    "assumptions": [
      "(M,τ,n); n∈ℕ; ∀p∈M ∃ chart φ:U≅V, p∈U∈τ, V⊆ℝⁿ open",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/lee-smooth-manifolds-ch1"
    ],
    "sourceLocator": "Chapter 1, Coordinate Charts, p. 4",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/Manifold-local-charts",
      "urn:csabs:operation/Manifold-coordinate",
      "urn:csabs:operation/Manifold-inverse-coordinate"
    ],
    "proofSketch": "A chart is a bijection with the recorded inverse; apply the two inverse-function identities on their domains."
  },
  {
    "id": "urn:csabs:theorem/Manifold-transition-cocycle",
    "type": "Theorem",
    "name": "transition-cocycle",
    "statement": "Coordinate changes compose consistently on triple overlaps.",
    "formalStatement": "on φ(U∩W∩Z): (χ∘ψ⁻¹)∘(ψ∘φ⁻¹)=χ∘φ⁻¹",
    "appliesTo": [
      "urn:csabs:concept/Manifold"
    ],
    "assumptions": [
      "(M,τ,n); n∈ℕ; ∀p∈M ∃ chart φ:U≅V, p∈U∈τ, V⊆ℝⁿ open",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/lee-smooth-manifolds-ch1"
    ],
    "sourceLocator": "Chapter 1, transition maps, pp. 12–13 (derived overlap identity)",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:theorem/Manifold-chart-inverses",
      "urn:csabs:operation/Manifold-transition"
    ],
    "proofSketch": "On the triple overlap every intermediate value is in the appropriate chart image. Cancel ψ⁻¹∘ψ and reassociate ordinary function composition."
  }
]
```
<!-- graph-record:end -->
