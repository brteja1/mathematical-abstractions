# Smooth manifold (C∞, without boundary)

A topological manifold equipped with a maximal atlas whose overlapping coordinate changes are smooth with smooth inverses.

**Notation:** (M,τ,n,𝒜_max); ψ∘φ⁻¹∈C∞ on φ(U∩W)

**Stable ID:** `urn:csabs:concept/SmoothManifold`

**Categories:** Geometry and manifolds, Topology

**Kind:** Mathematical structure

**Prerequisites:** [Topological manifold (fixed dimension, without boundary)](Manifold.md)

**Specializes:** [Topological manifold (fixed dimension, without boundary)](Manifold.md)

**Related concepts:** [Tensor of specified valence on a finite-dimensional vector space](Tensor.md)

## Backlinks

- [Topological manifold (fixed dimension, without boundary)](Manifold.md) — `relatedConcept`
- [Tensor of specified valence on a finite-dimensional vector space](Tensor.md) — `relatedConcept`

## Mathematical formulation

A smooth n-manifold is the selected topological n-manifold with covering charts whose overlap maps φ\_j∘φ\_i⁻¹ are C^∞ on their domains. The wrapper records compatibility of a supplied atlas; it does not construct its maximal extension.

**Lean formulation** (in its source module context):

```lean
structure SmoothManifold (n : Nat) (M : Type*) [_root_.TopologicalSpace M]
    [ChartedSpace (EuclideanSpace ℝ (Fin n)) M] : Prop extends Manifold n M where
  compatible : IsManifold (𝓡 n) ((⊤ : ENat) : WithTop ENat) M
```

**Source:** [`Catalog.SmoothManifold`](../lean/Catalog/Topology.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Boundaryless Euclidean charts with Mathlib IsManifold at smooth (not analytic) regularity, plus Hausdorff/second countability.

**Limits:** Atlas smooth compatibility is formalized; the maximal compatible atlas is not explicitly constructed by the wrapper.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Use Manifold with a covering atlas of pairwise C∞-compatible charts; identify its smooth structure with the unique maximal compatible atlas.

**basisKind:** defined-structure

**basisScope:** Smooth structures and coordinate changes; tensor fields, tangent bundles and Riemannian metrics require additional interfaces.

**basisInstantiation:** Instantiate Manifold at (M,τ,n). Retain its topological requirements and choose the smooth structure through a covering pairwise C∞-compatible atlas and its maximal extension.

**specializationNote:** Forget the chosen smooth structure, retaining the same topology, carrier and declared dimension.

**verificationObligation:** Charts are real and finite-dimensional, and smooth means C∞. The empty manifold and dimension zero follow the Manifold convention.; A topological manifold does not automatically have a unique or even an existing smooth structure. No metric, connection or orientation is assumed.; Use the stated carriers and equality. Specialization does not automatically transfer operations or claims.

**reviewStatus:** editorial interface review; not machine-proved

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-SmoothManifold-smooth-transition"></a>

### smooth-transition

`urn:csabs:operation/SmoothManifold-smooth-transition`

**signature:** φ(U∩W) → ψ(U∩W); y ↦ ψ(φ⁻¹(y))

**description:** Evaluate the coordinate transition in the chosen smooth atlas.

**precondition:** Both charts are in the chosen smooth structure; y lies in the overlap image.

**postcondition:** Evaluate the coordinate transition in the chosen smooth atlas.

**totality:** total on overlap image; partial on ℝⁿ

## Axioms and defining rules

<a id="node-urn-csabs-axiom-SmoothManifold-compatible-atlas"></a>

### compatible-atlas

`urn:csabs:axiom/SmoothManifold-compatible-atlas`

**statement:** The chosen covering atlas has smooth coordinate transitions in both directions.

**formalStatement:** (U,φ),(W,ψ)∈𝒜 ⇒ ψ∘φ⁻¹:φ(U∩W)→ψ(U∩W) and φ∘ψ⁻¹ are C∞

**assumptions:** (M,τ,n,𝒜_max); ψ∘φ⁻¹∈C∞ on φ(U∩W); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [John M. Lee, Introduction to Smooth Manifolds, second edition, Chapter 1 (author-hosted sample)](https://sites.math.washington.edu/~lee/Books/ISM/c01.pdf); citation: John M. Lee, Introduction to Smooth Manifolds, 2nd ed., Springer, 2013, Chapter 1, pp. 1–31. DOI: 10.1007/978-1-4419-9982-5_1.; accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Chapter 1, Smooth Structures, pp. 12–13

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-SmoothManifold-maximal-structure"></a>

### maximal-structure

`urn:csabs:axiom/SmoothManifold-maximal-structure`

**statement:** The smooth structure includes every chart compatible with all its charts.

**formalStatement:** 𝒜_max={charts (U,φ): (U,φ) is C∞-compatible with every chart in 𝒜_max}

**assumptions:** (M,τ,n,𝒜_max); ψ∘φ⁻¹∈C∞ on φ(U∩W); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [John M. Lee, Introduction to Smooth Manifolds, second edition, Chapter 1 (author-hosted sample)](https://sites.math.washington.edu/~lee/Books/ISM/c01.pdf); citation: John M. Lee, Introduction to Smooth Manifolds, 2nd ed., Springer, 2013, Chapter 1, pp. 1–31. DOI: 10.1007/978-1-4419-9982-5_1.; accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Chapter 1, maximal atlas and smooth structure, p. 13

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** definition

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-SmoothManifold-maximal-extension-unique"></a>

### maximal-extension-unique

`urn:csabs:theorem/SmoothManifold-maximal-extension-unique`

**statement:** A covering smooth atlas determines a unique maximal smooth atlas.

**formalStatement:** 𝒜 a covering pairwise C∞-compatible atlas ⇒ ∃! maximal smooth atlas 𝒜_max⊇𝒜

**assumptions:** (M,τ,n,𝒜_max); ψ∘φ⁻¹∈C∞ on φ(U∩W); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [John M. Lee, Introduction to Smooth Manifolds, second edition, Chapter 1 (author-hosted sample)](https://sites.math.washington.edu/~lee/Books/ISM/c01.pdf); citation: John M. Lee, Introduction to Smooth Manifolds, 2nd ed., Springer, 2013, Chapter 1, pp. 1–31. DOI: 10.1007/978-1-4419-9982-5_1.; accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Chapter 1, Proposition 1.17(a), pp. 13–14

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [compatible-atlas](SmoothManifold.md#node-urn-csabs-axiom-SmoothManifold-compatible-atlas); [maximal-structure](SmoothManifold.md#node-urn-csabs-axiom-SmoothManifold-maximal-structure); [local-charts](Manifold.md#node-urn-csabs-axiom-Manifold-local-charts); [transition](Manifold.md#node-urn-csabs-operation-Manifold-transition)

**proofSketch:** Take all charts compatible with 𝒜. Near any overlap point choose an 𝒜-chart; each transition is locally a composite of two smooth transitions. Hence the extended atlas is smooth, covers M and is maximal. Any maximal smooth atlas containing 𝒜 consists of exactly those charts.

## Concept provenance

- [John M. Lee, Introduction to Smooth Manifolds, second edition, Chapter 1 (author-hosted sample)](https://sites.math.washington.edu/~lee/Books/ISM/c01.pdf); citation: John M. Lee, Introduction to Smooth Manifolds, 2nd ed., Springer, 2013, Chapter 1, pp. 1–31. DOI: 10.1007/978-1-4419-9982-5_1.; accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Chapter 1, Smooth Structures, pp. 12–14; Proposition 1.17

**sourceNote:** Interface adapted to the catalog notation and explicitly restricted to the stated scope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/SmoothManifold",
    "type": "Concept",
    "shortForm": "SmoothManifold",
    "fullName": "Smooth manifold (C∞, without boundary)",
    "category": [
      "urn:csabs:category/geometry",
      "urn:csabs:category/topology"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A topological manifold equipped with a maximal atlas whose overlapping coordinate changes are smooth with smooth inverses.",
    "notation": "(M,τ,n,𝒜_max); ψ∘φ⁻¹∈C∞ on φ(U∩W)",
    "hasOperation": [
      "urn:csabs:operation/SmoothManifold-smooth-transition"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/SmoothManifold-compatible-atlas",
      "urn:csabs:axiom/SmoothManifold-maximal-structure"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/SmoothManifold-maximal-extension-unique"
    ],
    "axiomBasis": "Use Manifold with a covering atlas of pairwise C∞-compatible charts; identify its smooth structure with the unique maximal compatible atlas.",
    "basisKind": "defined-structure",
    "basisScope": "Smooth structures and coordinate changes; tensor fields, tangent bundles and Riemannian metrics require additional interfaces.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "editorial interface review; not machine-proved",
    "requiresConcept": [
      "urn:csabs:concept/Manifold"
    ],
    "verificationObligation": [
      "Charts are real and finite-dimensional, and smooth means C∞. The empty manifold and dimension zero follow the Manifold convention.",
      "A topological manifold does not automatically have a unique or even an existing smooth structure. No metric, connection or orientation is assumed.",
      "Use the stated carriers and equality. Specialization does not automatically transfer operations or claims."
    ],
    "source": [
      "urn:csabs:source/lee-smooth-manifolds-ch1"
    ],
    "sourceLocator": "Chapter 1, Smooth Structures, pp. 12–14; Proposition 1.17",
    "sourceNote": "Interface adapted to the catalog notation and explicitly restricted to the stated scope.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Manifold"
    ],
    "specializationNote": "Forget the chosen smooth structure, retaining the same topology, carrier and declared dimension.",
    "relatedConcept": [
      "urn:csabs:concept/Tensor"
    ],
    "basisInstantiation": "Instantiate Manifold at (M,τ,n). Retain its topological requirements and choose the smooth structure through a covering pairwise C∞-compatible atlas and its maximal extension.",
    "leanFormulation": "structure SmoothManifold (n : Nat) (M : Type*) [_root_.TopologicalSpace M]\n    [ChartedSpace (EuclideanSpace ℝ (Fin n)) M] : Prop extends Manifold n M where\n  compatible : IsManifold (𝓡 n) ((⊤ : ENat) : WithTop ENat) M",
    "formulationSource": "urn:csabs:source/local-lean-Topology",
    "formulationLocator": "Catalog.SmoothManifold",
    "formulationScope": "partial",
    "leanModelMapping": "Boundaryless Euclidean charts with Mathlib IsManifold at smooth (not analytic) regularity, plus Hausdorff/second countability.",
    "leanModelLimitations": "Atlas smooth compatibility is formalized; the maximal compatible atlas is not explicitly constructed by the wrapper.",
    "mathematicalFormulation": "A smooth n-manifold is the selected topological n-manifold with covering charts whose overlap maps φ_j∘φ_i⁻¹ are C^∞ on their domains. The wrapper records compatibility of a supplied atlas; it does not construct its maximal extension."
  },
  {
    "id": "urn:csabs:operation/SmoothManifold-smooth-transition",
    "type": "Operation",
    "name": "smooth-transition",
    "signature": "φ(U∩W) → ψ(U∩W); y ↦ ψ(φ⁻¹(y))",
    "description": "Evaluate the coordinate transition in the chosen smooth atlas.",
    "concept": "urn:csabs:concept/SmoothManifold",
    "precondition": "Both charts are in the chosen smooth structure; y lies in the overlap image.",
    "postcondition": "Evaluate the coordinate transition in the chosen smooth atlas.",
    "totality": "total on overlap image; partial on ℝⁿ"
  },
  {
    "id": "urn:csabs:axiom/SmoothManifold-compatible-atlas",
    "type": "Axiom",
    "name": "compatible-atlas",
    "statement": "The chosen covering atlas has smooth coordinate transitions in both directions.",
    "formalStatement": "(U,φ),(W,ψ)∈𝒜 ⇒ ψ∘φ⁻¹:φ(U∩W)→ψ(U∩W) and φ∘ψ⁻¹ are C∞",
    "appliesTo": [
      "urn:csabs:concept/SmoothManifold"
    ],
    "assumptions": [
      "(M,τ,n,𝒜_max); ψ∘φ⁻¹∈C∞ on φ(U∩W)",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/lee-smooth-manifolds-ch1"
    ],
    "sourceLocator": "Chapter 1, Smooth Structures, pp. 12–13",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/SmoothManifold-maximal-structure",
    "type": "Axiom",
    "name": "maximal-structure",
    "statement": "The smooth structure includes every chart compatible with all its charts.",
    "formalStatement": "𝒜_max={charts (U,φ): (U,φ) is C∞-compatible with every chart in 𝒜_max}",
    "appliesTo": [
      "urn:csabs:concept/SmoothManifold"
    ],
    "assumptions": [
      "(M,τ,n,𝒜_max); ψ∘φ⁻¹∈C∞ on φ(U∩W)",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/lee-smooth-manifolds-ch1"
    ],
    "sourceLocator": "Chapter 1, maximal atlas and smooth structure, p. 13",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "definition"
  },
  {
    "id": "urn:csabs:theorem/SmoothManifold-maximal-extension-unique",
    "type": "Theorem",
    "name": "maximal-extension-unique",
    "statement": "A covering smooth atlas determines a unique maximal smooth atlas.",
    "formalStatement": "𝒜 a covering pairwise C∞-compatible atlas ⇒ ∃! maximal smooth atlas 𝒜_max⊇𝒜",
    "appliesTo": [
      "urn:csabs:concept/SmoothManifold"
    ],
    "assumptions": [
      "(M,τ,n,𝒜_max); ψ∘φ⁻¹∈C∞ on φ(U∩W)",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/lee-smooth-manifolds-ch1"
    ],
    "sourceLocator": "Chapter 1, Proposition 1.17(a), pp. 13–14",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/SmoothManifold-compatible-atlas",
      "urn:csabs:axiom/SmoothManifold-maximal-structure",
      "urn:csabs:axiom/Manifold-local-charts",
      "urn:csabs:operation/Manifold-transition"
    ],
    "proofSketch": "Take all charts compatible with 𝒜. Near any overlap point choose an 𝒜-chart; each transition is locally a composite of two smooth transitions. Hence the extended atlas is smooth, covers M and is maximal. Any maximal smooth atlas containing 𝒜 consists of exactly those charts."
  }
]
```
<!-- graph-record:end -->
