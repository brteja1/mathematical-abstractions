# Lean models and theorem witnesses

This Lake project gives every current catalog concept a named Lean interpretation, grouped by subject in `Catalog/`. It uses **Lean 4.35.0** and **Mathlib commit `56a005855ea17e0b0958f73ec801ae140b0a1679`** (release `v4.35.0`). `lake-manifest.json` locks transitive dependencies. Normal catalog retrieval and the viewer still require only Python.

There are currently **220 concept bindings**: 169 carrier/interface models and 51 explicitly partial interpretations. There are **77 registered proof witnesses** for existing laws/theorems, including all 11 recorded binary-tree laws/theorems, 13 information-theory/coding claims, six matrix-decomposition identities and six descriptive-statistics laws. This does **not** mean every recorded operation or all catalog laws/theorems have been translated or proved. An alias to a library structure is a model binding, not a proof of all catalog claims. The [broad-core expansion](../docs/FOUNDATIONAL_DATA_MODELS.md) adds 35 carrier models and 24 individually mapped witnesses. Its remaining operation specifications and derived results are not blanket formalizations.

## Build and verify

Install [Elan](https://github.com/leanprover/elan), then from this directory run:

```sh
lake update
lake exe cache get
lake build
```

`lake update` materializes the pinned dependencies. Review changes to the lock before committing a dependency update; do not replace the pinned revision with `master` or `latest`. The first setup downloads Lean and Mathlib's precompiled artifacts and needs network access and several GB of disk space. Subsequent project builds use the local dependencies.

From the repository root:

```sh
make check-lean  # metadata, coverage, interface/premise hashes; does not compile
make test-lean   # build, type/axiom audit, compiler rejection tests
python3 scripts/lean.py coverage
python3 scripts/lean.py get Group
python3 scripts/lean.py get urn:csabs:theorem/Group-inverse-product
```

`make test-lean` writes the ignored `lean/verification.json`, retaining compiler output, exact toolchain/library revisions, input digest and each witness's actual foundational axioms. A report is fresh only while catalog records, Lean sources, binding metadata, verifier and dependency locks match and the installed dependencies remain clean at their locked revisions. `get` returns proof evidence only from a fresh report; a manifest entry alone means **registered**, not **verified**. These are reproducibility records, not cryptographic attestations.

The [GitHub workflow](../.github/workflows/lean.yml) runs verification on pushes and pull requests and saves the report as a `lean-verification` Actions artifact. A passing Pages deployment is independent of passing Lean verification. The GitHub Pages viewer does not yet display Lean witness status.

## Find a model

Concept records expose `mathematicalFormulation` (readable mathematics), `leanFormulation` (the selected declaration), `formulationScope`, `formulationSource`/`formulationLocator`, and the binding's interpretation and limitations. Witness records expose their expected proposition, expanding named target definitions, and a direct premise mapping. Maintain these fields when changing a binding or module; `make check-lean` compares the excerpts, source locators, scopes and mappings against current Lean sources and metadata. Excerpts use their source module's imports and section context. Local Lean sources document an interpretation, while independent mathematical provenance remains in the existing `source` links.

| Module | Models |
| --- | --- |
| `Catalog/Foundations.lean` | Sets, relations, functions, products, sums, option, empty/unit, partitions and proof principles |
| `Catalog/Algebra.lean` | Semigroups, monoids, groups, rings, fields, finite fields, modules, linear maps, matrices and tensors |
| `Catalog/MatrixDecompositions.lean` | Exact LU, full QR/SVD, field-relative eigendecomposition and positive-definite Cholesky witnesses; six derived identities, with existence/uniqueness claims kept separate; see [scope](../docs/MATRIX_DECOMPOSITIONS.md) |
| `Catalog/GeometricLattices.lean` | Independent real lattice bases, modular kernels and partial SVP/CVP/SIS/LWE interpretations |
| `Catalog/Order.lean` | Preorders, partial/total orders, lattices, Boolean algebras, closure and fixed points |
| `Catalog/DataStructures.lean` | Sequences, arrays, finite sets/maps, multisets, ordered sets, stacks, queues and deques |
| `Catalog/CoreData.lean` | Dependent/refined/quotient types, exact numbers, streams, finite iterators, intervals, sparse vectors, distributions and join-based replication |
| `Catalog/StructuredData.lean` | Multimaps, allocated heap stores, union-find, rose trees, ranked terms, BSTs, binary heaps and prefix dictionaries |
| `Catalog/ObjectOrientation.lean` | Object heaps/aliasing, class lookup/dispatch, method effects, visible-state invariants, behavioral subtyping and heap separation; see [OOP scope](../docs/OBJECT_ORIENTED_MODELS.md) |
| `Catalog/TemplateMetaprogramming.lean` | Kinded partial metafunctions, specialization selection, substitution outcomes, constraints, packs, staged lookup and bounded signed constant evaluation; see [template scope](../docs/TEMPLATE_METAPROGRAMMING.md) |
| `Catalog/GenericProgramming.lean` | Shared generic signatures/binding/instantiation, Java parameterization/capture/erasure/inference and VHDL association/elaboration interfaces; see [scope](../docs/GENERIC_PROGRAMMING.md) |
| `Catalog/GraphData.lean` | Rooted trees, edge-identity multigraphs, real weights, hypergraphs and chosen bipartitions |
| `Catalog/InformationData.lean` | Bag relations, JSON value profile, typed ER instances, property graphs and RDF graphs/datasets |
| `Catalog/BinaryTree.lean` | Finite ordered node-labelled trees, empty/node/view/fold, counts, traversal, mirror and label mapping; witnesses for all recorded binary-tree laws/theorems |
| `Catalog/Numeric.lean` | Naturals, integers, bit vectors, bounded arithmetic and floating-point interfaces |
| `Catalog/Graphs.lean` | Graphs, trees, transition systems, simulation, bisimulation and traces |
| `Catalog/Concurrency.lean` | Compatible-mode locks, non-reentrant mutex owners and a partial bakery-protocol state carrier |
| `Catalog/Semantics.lean` | Hoare logic, invariants, termination, safety/liveness and history interfaces |
| `Catalog/Logic.lean` | Propositional, first-order, modal and temporal syntax and satisfaction |
| `Catalog/LogicSyntax.lean` | Countable signatures, named binders, guarded substitution and classical natural deduction; see [logic coverage](../docs/LOGIC.md) |
| `Catalog/Languages.lean` | Languages, automata, context-free grammars and a Turing-machine interface |
| `Catalog/Database.lean` | Schemas, dependent tuples, finite relations, functional dependencies and keys |
| `Catalog/InformationTheory*.lean` | Finite information measures, concrete operational coding targets, matrices and 13 full witnesses; see [claim-by-claim status](INFORMATION_THEORY.md) |
| `Catalog/Probability.lean` | Measurable/measure/probability spaces, random variables, conditioning and stochastic models |
| `Catalog/DescriptiveStatistics.lean` | Finite-sample arithmetic mean, midpoint median and all-maximizer mode set; six individually mapped witnesses; see [scope](../docs/DESCRIPTIVE_STATISTICS.md) |
| `Catalog/Topology.lean` | Topologies and Euclidean charted manifold interfaces |

`bindings.json` is the authoritative integration manifest keyed by stable graph ID. Each entry records the declaration, module, carrier/equality/assumption mapping, scope, limitations and a hash of the relevant catalog records. Retrieve a binding with the CLI instead of reading the entire manifest. `Catalog.lean` imports every subject and the example/witness modules.

## Work out a new theorem

1. Search existing graph claims and fetch the relevant dossier, then retrieve any truncated premises. Reuse stable IDs when the claim already exists.

   ```sh
   python3 scripts/agent_query.py dossier Group --purpose proof --limit 100
   ```

2. Write a theorem in a subject or proof module and import that module from `Catalog.lean`. [Catalog/Examples.lean](Catalog/Examples.lean) is a compiled worked example deriving inverse involution from the group interface. It deliberately has no catalog witness registration: it demonstrates proof development before promotion into the graph.

   ```lean
   import Catalog.Algebra

   theorem my_inverse_involution {A : Type*} [Catalog.Group A] (a : A) :
       (a⁻¹)⁻¹ = a := by
     have h : a⁻¹ * (a⁻¹)⁻¹ = a⁻¹ * a := by
       rw [mul_inv_cancel, inv_mul_cancel]
     exact mul_left_cancel h
   ```

   Work against explicit structure laws or hypotheses. Do not turn the target theorem into a new `axiom` or assume it as a structure field. Keep drafts outside `Catalog/` until ready; no `sorry` is allowed in the built library. For standalone drafts use `lake env lean path/to/Draft.lean` from `lean/`.

3. For a genuinely new graph claim, add it to the owning Markdown JSON block with the required consulted source provenance, explicit `dependsOn` premises and derivation. A compiled proof does not repair inherited citation gaps or automatically establish that a natural-language statement was translated correctly. The catalog's general editorial review status is not silently changed by adding a Lean binding.

4. Add a `kind: "witness"` entry in `bindings.json`, using the existing witnesses as examples. Supply the stable claim ID, `Catalog.…` symbol, defining module, independently reviewed `expectedType`, carrier/operation/assumption `mapping`, `limitations`, a `premiseMapping` entry for **each** direct `dependsOn` ID, and the permitted foundational axioms. Get the current interface fingerprint with:

   ```sh
   python3 scripts/lean.py fingerprint urn:csabs:theorem/Group-inverse-product
   ```

   Store the returned hash as `catalogHash` after reviewing the mapping. A hash mismatch means the claim, interface, source metadata or premises changed; review the affected mapping before refreshing it. A graph specialization is not an implicit transfer of axioms. Every new concept also needs a model binding; partial models must say so.

   To refresh existing bindings after that review, use:

   ```sh
   make update-lean-bindings LEAN_FLAGS=--dry-run
   make update-lean-bindings
   # Or refresh only selected bindings (stable IDs or concept short forms):
   make update-lean-bindings LEAN_IDS="Graph BipartiteGraph urn:csabs:law/BipartiteGraph-adjacent-colors"
   make check-lean
   make test-lean
   ```

   The target defaults to all registered bindings and changes only stale `catalogHash` fields in `lean/bindings.json`. It reports old/new hashes and rejects invalid binding metadata before writing. It does not review mathematical correspondence, change Lean code or mappings, or generate proof evidence. Selected updates can leave other fingerprints stale; `make check-lean` reports those. Existing verification evidence becomes stale when bindings change; `make test-lean` regenerates it through compilation and axiom auditing.

5. Run `make build`, `make test`, `make test-rdf`, and `make test-lean`. Inspect the witness using `scripts/lean.py get ID`. The proof term is the named compiled theorem; the manifest connects it to the graph, and the report records the check and actual axiom dependencies.

## What verification establishes

The verifier compiles the library with warnings treated as errors, checks that each registered symbol is an actual theorem declaration, and elaborates an example with its independently specified expected type. It uses Lean's transitive axiom collection to reject `sorryAx`, fabricated axioms and other axioms beyond the standard allowlist. It then checks that each witness stays within its own declared subset of that allowlist. The negative compiler tests exercise these rejection paths.

The permitted foundational names are `propext`, `Quot.sound` and `Classical.choice`; actual use is recorded individually. Structure laws such as associativity are explicit hypotheses in the theorem's type, rather than extra global Lean axioms. The type checker verifies the Lean proposition conditional on those hypotheses. It does not decide that the chosen model matches every nuance of an informal definition, establish consistency of all mathematical assumptions, or supply missing bibliographic evidence. See [Lean's axiom documentation](https://lean-lang.org/doc/reference/latest/Axioms/).

Partial interpretations needing further work are:

- `ParametricInstantiation`: simultaneous argument/name binding and a supplied language realization; hygienic syntax substitution and full phase semantics remain obligations.
- `JavaParameterizedType`, `JavaWildcardCapture`: selected well-formedness, substitution and fresh-bound interfaces; actual JLS declaration/subtyping/capture frontends remain obligations.
- `JavaTypeErasure`: a fuel-bounded owner-free type core; adequate fuel, full reifiability, signature and nested-type translation are not established.
- `JavaTypeInference`: semantic constraints and an explicitly sound supplied resolver; Chapter 18 algorithms and their correspondence to compiler behavior are not implemented.
- `VHDLGenericElaboration`: ordered event execution and finite generate lists; actual VHDL evaluation, staticness, conformance and instance semantics remain obligations.

- `TemplateSubstitution`: ordered failure events and a supplied frontend; actual substitution, lexical event generation and immediate-context classification remain obligations.
- `TemplateConstraint`: normalized identity-bearing trees and subsumption; actual normalization, source-origin/parameter-map equality and atomic expression checking remain frontend obligations.

- `ClassTable`: finite ranked single-inheritance hierarchy and bounded lookup; the general fuel-sufficiency and recursive-lookup correspondence proofs are not registered.
- `BehavioralSubtyping`: invariant, method and history-constraint implications; the supplied history relation needs connection to concrete executions, and general signature adapters remain obligations.

- `LamportBakery`: raw flags, tickets and local-state fields; protocol transitions, reachability and correctness are not yet formalized.

- `BTree`: raw rose-tree shapes with finite key-list labels; occupancy, arity, ordering, balance and update specifications are not yet formalized.

- `Set`: a universe-indexed `ZFSet` interpretation in Lean, without a claim to choice-free ZF metatheory or consistency.
- `StructuralInduction`: a representative finitary tree rather than all constructor signatures.
- `FloatingPointType`, `Binary16`, `Binary32`, `Binary64`, `Binary128`: format/value/environment interfaces; correctly rounded arithmetic, exception behavior and bit encodings remain unproved. Client-supplied `round`/`run` functions are not assumed correct.
- `WeakestPrecondition`: the all-executions termination/no-fault predicate must be connected to a concrete operational and scheduler semantics.
- `Linearizability`, `SequentialConsistency`: abstract history predicates require an event-level instantiation and consistency laws.
- `MarkovChain`: normalized finite-state kernel and path weights; infinite-process construction and conditional Markov property remain to be related.
- `SmoothManifold`: compatible smooth covering charts; an explicit maximal-atlas construction is not exposed by the wrapper.
- `TuringMachine`: finite controller, input initialization and deterministic step; eventual-blank tape invariants, outcomes and recognition/decision semantics remain to be completed.

Other models also have declared instantiation conventions: semigroups are nonempty; fields have a totalized inverse at zero; total orders carry decidable comparisons; finite arrays include length zero; stacks use Option to represent undefined empty operations; unsigned integers require positive width; signed overflow is undefined; and priority extraction permits nondeterministic ties. Check each binding before using library results as witnesses.

- `DiffieHellman`, `RSA`, `ECC`, `ECDH`: partial group/action or exponent interfaces; see [cryptography scope](../docs/CRYPTOGRAPHY.md). No new proof witnesses or security proofs.

- `EuclideanLattice`, `QaryLattice`, `SVP`, `CVP`, `SIS`, `LWE`: partial geometric-lattice and relation models; see [lattice scope](../docs/GEOMETRIC_LATTICES.md). No new registered witnesses or hardness proofs.
