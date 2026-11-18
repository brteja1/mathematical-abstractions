# Worked example: obtain a model, then resume a watermark task

Suppose a task needs a merge of unbounded natural-number replica watermarks, ordered by `≤`, such that merging three replicas never regresses any input. Search `join`, `semilattice`, `merge` and related operations first. The catalog already has `JoinSemilattice`; do **not** create a WatermarkSemilattice concept just because the application has a new name. This example illustrates filling a concrete-model/proof gap. A genuinely missing concept follows the same proof path and additionally needs a new sourced definition.

## Consulted sources and mapping

The following local sources were consulted on 2026-11-18 for this example. These references document the example; they do not change existing graph provenance:

- [JoinSemilattice](../../../../concepts/JoinSemilattice.md): partial-order constraints, binary upper bounds and leastness. Its inherited partial-order axiom records have legacy citation gaps; this example does not remove them.
- Mathlib revision `56a005855ea17e0b0958f73ec801ae140b0a1679`, `Mathlib/Order/Lattice.lean`, section constructing a lattice from a linear order (`le_sup_left := le_max_left`, `le_sup_right := le_max_right`, `sup_le := max_le`), and `Mathlib/Order/Lattice/Nat.lean`: natural-number lattice interpretation. These installed files supply the interpretation, not a proof of a software API.
- [Catalog.Audit](../../../../lean/Catalog/Audit.lean): `#catalog_witness` implementation and foundational axiom allowlist.

The carrier is `Nat`, equality is Lean equality, order is natural-number `≤`, and the total binary operation is `max`. No overflow, rounding, sentinel, negative values, network behavior or fairness is modeled. The basis is the catalog's order-based basis, including reflexivity, transitivity, antisymmetry, upper bounds and leastness. Extra results such as replicated-protocol convergence are outside this example.

| Catalog constraint ID | Concrete obligation in `JoinBasis Nat (· ≤ ·) merge` |
| --- | --- |
| `urn:csabs:axiom/PartialOrder-reflexive` | First conjunct: `∀ a, a ≤ a`. |
| `urn:csabs:axiom/PartialOrder-transitive` | Second conjunct: compose two natural-number inequalities. |
| `urn:csabs:axiom/PartialOrder-antisymmetric` | Third conjunct: mutual inequalities imply natural-number equality. |
| `urn:csabs:axiom/JoinSemilattice-upper-bounds` | Fourth conjunct: each argument is at most its merge. |
| `urn:csabs:axiom/JoinSemilattice-leastness` | Fifth conjunct: a shared upper bound bounds the merge. |

The [executable Lean file](watermark.lean) proves `natural_model_satisfies` without a hypothesis assuming the basis. Its `merge_three_covers` theorem uses the proved upper-bound constraints. Nontrivial examples exercise distinct values; they complement, rather than replace, the universal proofs. The expected-type checks and audits cover both relied-on theorems.

## Execute in the pinned environment

From the catalog root, check installed dependencies against the lock and build the existing audit module:

```sh
python3 -c "import sys; sys.path.insert(0, 'scripts'); import lean; lean.check_dependencies()"
cd lean
lake build Catalog.Audit
lake env lean --version
lake env lean -DwarningAsError=true ../ai/skills/abstraction-acquisition/references/watermark.lean
```

Require exit code zero and a `CATALOG_WITNESS` line for each of `AcquisitionExample.natural_model_satisfies` and `AcquisitionExample.merge_three_covers`. Record the axioms listed by each line; do not assume an empty list in advance. Retain compiler output, versions and hashes of the proof file, audit source, toolchain and lockfiles; recheck dependencies and unchanged input hashes after execution. This is task-local compiler evidence, not catalog witness registration or a fresh catalog verification report.

The repository's Lean rejection tests also exercise this file and demonstrate that a `min` implementation cannot discharge the same basis, while `sorry` and fabricated axioms are rejected. Run `make test-lean` for these checks.

## Choose persistence and resume

After preparing the proofs and provenance, offer **Promote to catalog (default)** or **Keep with this task** and wait for the user's selection, as required by [the acquisition skill](../SKILL.md). For promotion, propose concrete-model satisfaction and downstream Theorem records under the existing concept, their direct source/premise mappings and witness bindings. Do not register a proof against an Axiom ID or create a duplicate concept. For local retention, keep the Lean file and evidence beside the problem. This instructional example itself is intentionally not promoted.

Resume the task by mapping the actual API's merge to `max`, and its input validation, equality and numeric representation to the model. A contract permitting arbitrary nonnegative integers could implement this operation with an appropriate integer type; a bounded or floating-point API needs its own semantic review. Derive tests from `merge_three_covers`, including zero, distinct inputs and repeated values, then run them against the target implementation. The Lean theorem does not prove that the implementation uses `max` correctly or that the distributed protocol converges.
