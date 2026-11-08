# Lean models and theorem witnesses

This Lake project gives every current catalog concept a named Lean interpretation, grouped by subject in `Catalog/`. It uses **Lean 4.35.0** and **Mathlib commit `56a005855ea17e0b0958f73ec801ae140b0a1679`** (release `v4.35.0`). `lake-manifest.json` locks transitive dependencies. Normal catalog retrieval and the viewer still require only Python.

There are currently **147 concept bindings**: 134 carrier/interface models and 13 explicitly partial interpretations. There are **52 registered proof witnesses** for existing laws/theorems, including all 11 recorded binary-tree laws/theorems. This does **not** mean every recorded operation or all 365 laws/theorems have been translated or proved. An alias to a library structure is a model binding, not a proof of all catalog claims. The [broad-core expansion](../docs/FOUNDATIONAL_DATA_MODELS.md) adds 35 carrier models and 24 individually mapped witnesses. Its remaining operation specifications and derived results are not blanket formalizations.

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

| Module | Models |
| --- | --- |
| `Catalog/Foundations.lean` | Sets, relations, functions, products, sums, option, empty/unit, partitions and proof principles |
| `Catalog/Algebra.lean` | Semigroups, monoids, groups, rings, fields, modules, linear maps, matrices and tensors |
| `Catalog/Order.lean` | Preorders, partial/total orders, lattices, Boolean algebras, closure and fixed points |
| `Catalog/DataStructures.lean` | Sequences, arrays, finite sets/maps, multisets, ordered sets, stacks, queues and deques |
| `Catalog/CoreData.lean` | Dependent/refined/quotient types, exact numbers, streams, finite iterators, intervals, sparse vectors, distributions and join-based replication |
| `Catalog/StructuredData.lean` | Multimaps, allocated heap stores, union-find, rose trees, ranked terms, BSTs, binary heaps and prefix dictionaries |
| `Catalog/GraphData.lean` | Rooted trees, edge-identity multigraphs, real weights, hypergraphs and chosen bipartitions |
| `Catalog/InformationData.lean` | Bag relations, JSON value profile, typed ER instances, property graphs and RDF graphs/datasets |
| `Catalog/BinaryTree.lean` | Finite ordered node-labelled trees, empty/node/view/fold, counts, traversal, mirror and label mapping; witnesses for all recorded binary-tree laws/theorems |
| `Catalog/Numeric.lean` | Naturals, integers, bit vectors, bounded arithmetic and floating-point interfaces |
| `Catalog/Graphs.lean` | Graphs, trees, transition systems, simulation, bisimulation and traces |
| `Catalog/Semantics.lean` | Hoare logic, invariants, termination, safety/liveness and history interfaces |
| `Catalog/Logic.lean` | Propositional, first-order, modal and temporal syntax and satisfaction |
| `Catalog/LogicSyntax.lean` | Countable signatures, named binders, guarded substitution and classical natural deduction; see [logic coverage](../docs/LOGIC.md) |
| `Catalog/Languages.lean` | Languages, automata, context-free grammars and a Turing-machine interface |
| `Catalog/Database.lean` | Schemas, dependent tuples, finite relations, functional dependencies and keys |
| `Catalog/Probability.lean` | Measurable/measure/probability spaces, random variables, conditioning and stochastic models |
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

5. Run `make build`, `make test`, `make test-rdf`, and `make test-lean`. Inspect the witness using `scripts/lean.py get ID`. The proof term is the named compiled theorem; the manifest connects it to the graph, and the report records the check and actual axiom dependencies.

## What verification establishes

The verifier compiles the library with warnings treated as errors, checks that each registered symbol is an actual theorem declaration, and elaborates an example with its independently specified expected type. It uses Lean's transitive axiom collection to reject `sorryAx`, fabricated axioms and other axioms beyond the standard allowlist. It then checks that each witness stays within its own declared subset of that allowlist. The negative compiler tests exercise these rejection paths.

The permitted foundational names are `propext`, `Quot.sound` and `Classical.choice`; actual use is recorded individually. Structure laws such as associativity are explicit hypotheses in the theorem's type, rather than extra global Lean axioms. The type checker verifies the Lean proposition conditional on those hypotheses. It does not decide that the chosen model matches every nuance of an informal definition, establish consistency of all mathematical assumptions, or supply missing bibliographic evidence. See [Lean's axiom documentation](https://lean-lang.org/doc/reference/latest/Axioms/).

Partial interpretations needing further work are:

- `Set`: a universe-indexed `ZFSet` interpretation in Lean, without a claim to choice-free ZF metatheory or consistency.
- `StructuralInduction`: a representative finitary tree rather than all constructor signatures.
- `FloatingPointType`, `Binary16`, `Binary32`, `Binary64`, `Binary128`: format/value/environment interfaces; correctly rounded arithmetic, exception behavior and bit encodings remain unproved. Client-supplied `round`/`run` functions are not assumed correct.
- `WeakestPrecondition`: the all-executions termination/no-fault predicate must be connected to a concrete operational and scheduler semantics.
- `Linearizability`, `SequentialConsistency`: abstract history predicates require an event-level instantiation and consistency laws.
- `MarkovChain`: normalized finite-state kernel and path weights; infinite-process construction and conditional Markov property remain to be related.
- `SmoothManifold`: compatible smooth covering charts; an explicit maximal-atlas construction is not exposed by the wrapper.
- `TuringMachine`: finite controller, input initialization and deterministic step; eventual-blank tape invariants, outcomes and recognition/decision semantics remain to be completed.

Other models also have declared instantiation conventions: semigroups are nonempty; fields have a totalized inverse at zero; total orders carry decidable comparisons; finite arrays include length zero; stacks use Option to represent undefined empty operations; unsigned integers require positive width; signed overflow is undefined; and priority extraction permits nondeterministic ties. Check each binding before using library results as witnesses.
