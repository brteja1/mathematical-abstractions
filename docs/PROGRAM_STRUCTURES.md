# Program structures, analyses and effects

These entries describe mathematical interfaces independently of compiler or runtime implementations. They retain exact carrier equality and explicit definedness. Sources and claim-specific locators are recorded directly in each concept page.

| Requested abstraction | Catalog record | Selected interpretation |
| --- | --- | --- |
| ControlFlowGraph | [ControlFlowGraph](../concepts/ControlFlowGraph.md) | Finite directed graph with distinct unique source and sink boundaries. Unreachable components and infinite executions remain possible. |
| MonotoneDataflow | [MonotoneDataflow](../concepts/MonotoneDataflow.md) | Forward equations over a complete lattice with boundary contributions and monotone edge transfers. |
| IntervalDomain | [IntervalDomain](../concepts/IntervalDomain.md) | Convex integer sets, including empty and unbounded intervals; inclusion order, hull joins and exact integer abstract addition. |
| RewriteSystem | [RewriteSystem](../concepts/RewriteSystem.md) | Arbitrary one-step relation, finite reflexive transitive closure and normal forms. |
| ObservationalRefinement | [BehaviorRefinement](../concepts/BehaviorRefinement.md) | Existing observable behavior inclusion, with its stable ID preserved. Search `ObservationalRefinement` to find it. |
| EffectAlgebra | [EffectAlgebra](../concepts/EffectAlgebra.md) | Program side effects: total alternatives, ordered sequencing and identity, with distribution. |
| SingleParentForest | [SingleParentForest](../concepts/SingleParentForest.md) | Finite acyclic partial parent function, with zero or more roots and unordered children. |

## Semantic boundaries

A single exit is a structural convention, not a termination guarantee. The CFG profile permits internal infinite paths, including paths with no route to exit. Entry and exit are synthetic distinct nodes, even for an empty body. The entry has no incoming edges and exit has no outgoing edges; every other vertex has at least one predecessor and successor. These are explicit normalization requirements. This entry does not model dominance-based SESE regions or implicitly collapse exceptions into normal returns.

Monotonicity yields a mathematical least dataflow solution on the complete product lattice. Finite height is a sufficient condition for the usual ascending iteration to stabilize. Infinite-height domains such as integer intervals require further convergence arguments. A widening solver may return an inductive upper approximation rather than the least fixed point. Soundness relative to executions remains an independent obligation, described by [AbstractInterpretation](../concepts/AbstractInterpretation.md).

`IntervalDomain` differs from [ClosedInterval](../concepts/ClosedInterval.md), whose values are nonempty bounded endpoint pairs. For example, joining `[0,1]` and `[4,5]` produces `[0,5]`, whereas their meet is empty. Mathematical integer addition has no machine overflow. The domain has no widening operation in this addition; implementers must choose and justify one separately.

`RewriteSystem` imposes no termination, confluence or contextual semantic-preservation property. [GuardedRewrite](../concepts/GuardedRewrite.md) supplies a separate program-rewrite contract. Observational refinement uses target-behavior inclusion in source behaviors under the same inputs and observation convention; reducing nondeterminism is permitted. Contextual replacement needs an explicit context quantifier, and divergence must be represented by the supplied semantics.

`EffectAlgebra` follows the user's intended program-side-effect meaning. Its total effect-quantale profile specializes the partial formulation of Wilshaw and Hutton, Definition 3.8. It is distinct from quantum-logical effect algebras. Sequencing need not commute, and its identity need not be the least element. No iteration, parallel operator, additive bottom, absorbing top or effect-inference algorithm is assumed. An instance can track read/write/allocation/free/I/O events; relating those effects to execution requires a sound interpretation. [EffectSummary](../concepts/EffectSummary.md) remains the conservative resource-summary contract.

For example, sets of finite event words form an instance: alternative is union, sequencing is language concatenation and identity is the singleton containing the empty word. The words `write(x);read(x)` and `read(x);write(x)` remain distinct. A simpler set-of-events instance uses union for both operations and the empty set as identity; that intentionally forgets order and cannot justify swapping operations.

`SingleParentForest` orients edges from a child to its parent and uses `None` at roots. A self-parent root representation needs translation. A parent function can still contain cycles, so acyclicity is an explicit requirement. A component can be converted into a [RootedTree](../concepts/RootedTree.md) by forgetting orientation and retaining its root; the existing undirected rooted-tree record is not made a literal specialization of a directed forest.

## Lean scope

[ProgramStructures.lean](../lean/Catalog/ProgramStructures.lean) supplies six model bindings and readable source excerpts. CFG and effect-algebra structures encode the selected defining constraints. Dataflow has a complete-lattice transfer interface and equation operator; the interval model is a convex-set carrier. Rewrite closure and normal forms are defined separately, and the forest structure enforces finite acyclicity.

No new theorem witnesses are registered. In particular, the catalog's least-solution, abstract-addition soundness, finite-maximal-path and unique-root derivations are editorial mathematical arguments. Lean compilation checks the selected typed models; it does not certify a dataflow solver, optimizer, effect analysis or runtime implementation.
