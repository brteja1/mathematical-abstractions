# LLVM and MLIR transformation verification

The catalog describes reusable obligations for compiler transformations. The
versioned reference is the supplied checkout at
`/linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8`.
Concept records cite consulted files and their `llvmorg-21.1.8` upstream URLs.
No LLVM/MLIR sources were modified. These abstractions support specifying and
discharging obligations; they are not a complete semantics or an automatic
verifier for arbitrary passes.

## Concepts and concrete interfaces

Paths below are relative to the supplied LLVM checkout.

| Concept | Mathematical role | Concrete reference |
| --- | --- | --- |
| [BehaviorRefinement](../concepts/BehaviorRefinement.md) | Target behavior inclusion, source first | `llvm/docs/UndefinedBehavior.rst`; Alive2 refinement checks |
| [GuardedRewrite](../concepts/GuardedRewrite.md) | Guarded contextual replacement | `mlir/docs/PatternRewriter.md`, `RewritePattern::matchAndRewrite`, `PatternRewriter` |
| [Dominance](../concepts/Dominance.md) | Every entry path to a reachable node passes its dominator | `llvm/include/llvm/IR/Dominators.h`, `DominatorTree`; MLIR needs region-specific hierarchical dominance |
| [SSAForm](../concepts/SSAForm.md) | Unique definitions, typing and use-site availability | `mlir/docs/LangRef.md`, blocks, regions, `IsolatedFromAbove`; LLVM PHI incoming-edge uses |
| [EffectSummary](../concepts/EffectSummary.md) | Conservative resource effects, unknown versus empty | `mlir/include/mlir/Interfaces/SideEffectInterfaces.td`, `MemoryEffectsOpInterface` |
| [SpeculationSafety](../concepts/SpeculationSafety.md) | Defined, terminating, silent evaluation on newly executed paths | `ConditionallySpeculatable`; `mlir/docs/Rationale/SideEffectsAndSpeculation.md` |
| [LLVMPoisonSemantics](../concepts/LLVMPoisonSemantics.md) | Scalar concrete/undef/poison values and dynamic freeze choices | `llvm/docs/LangRef.rst`, Undefined Values, Poison Values, freeze |
| [DialectConversion](../concepts/DialectConversion.md) | Legality with separate representation and semantic obligations | `mlir/include/mlir/Transforms/DialectConversion.h`, `ConversionTarget`, `TypeConverter` |
| [TranslationValidation](../concepts/TranslationValidation.md) | Evidence for one source/target pair with explicit scope | [Alive2 official documentation](https://github.com/AliveToolkit/alive2/blob/master/README.md) |
| [AbstractInterpretation](../concepts/AbstractInterpretation.md) | Sound abstract transfer and inductive facts for guards | `mlir/docs/Tutorials/DataFlowAnalysis.md` |
| [IntegerAffineMap](../concepts/IntegerAffineMap.md) | Exact integer maps with dimension/symbol binding | `mlir/docs/Dialects/Affine.md` |
| [LoopDependence](../concepts/LoopDependence.md) | Conflicting dynamic accesses and legal schedule ordering | `mlir/include/mlir/Dialect/Affine/Analysis/AffineAnalysis.h`, `checkMemrefAccessDependence` |
| [AnalysisPreservation](../concepts/AnalysisPreservation.md) | Analysis validity after IR mutation | `llvm/docs/NewPassManager.rst`, `PreservedAnalyses`, analysis invalidation |

The extended core LLVM profiles add the following concepts. Their records link
directly to the consulted 21.1.8 language reference, analysis interfaces and
runtime documentation.

| Concept | Required distinction or obligation |
| --- | --- |
| [DataLayout](../concepts/DataLayout.md) | Store size versus allocation stride, ABI alignment, padding, field offsets, endianness and pointer/index widths |
| [PointerProvenance](../concepts/PointerProvenance.md) | Allocation association, capture, lifetime, non-integral pointers and address arithmetic versus dereference |
| [ByteMemory](../concepts/ByteMemory.md) | Typed encoding over untyped bytes, overlapping accesses, padding, initialization, volatile operations and frame conditions |
| [AliasAnalysis](../concepts/AliasAnalysis.md) | Pointer-plus-size queries, context-sensitive NoAlias, conservative Mod/Ref and unknown results |
| [MemorySSA](../concepts/MemorySSA.md) | Whole-memory versions, may-reach PHIs, ordering definitions, clobber queries and freshness |
| [ControlFlowRefinement](../concepts/ControlFlowRefinement.md) | Edge-specific PHIs, safe-source path/outcome correspondence, target progress, stuttering rank and indirect/EH control |
| [LoopIterationMapping](../concepts/LoopIterationMapping.md) | Event domains, guarded versions, zero-trip loops, tails and multiple exits |
| [ScalarRecurrence](../concepts/ScalarRecurrence.md) | Scoped induction/nowrap facts, modular versus exact arithmetic and unknown versus zero trip counts |
| [LLVMIntegerSemantics](../concepts/LLVMIntegerSemantics.md) | Fixed-width arithmetic, casts, comparisons, overflow/exact flags, poison shifts and division UB |
| [LLVMFloatingPointSemantics](../concepts/LLVMFloatingPointSemantics.md) | Default/constrained environments, NaNs/infinities/signed zeros, contraction and reassociation permissions |
| [PredicatedVectorSemantics](../concepts/PredicatedVectorSemantics.md) | Runtime scalable width, mask/EVL, per-intrinsic inactive-lane policy, lane poison and active-only memory |
| [AtomicMemoryModel](../concepts/AtomicMemoryModel.md) | Reads-from, per-location modification order, synchronization scopes, fences, RMW and races |
| [CallEffectContract](../concepts/CallEffectContract.md) | ABI, effects, independent return/unwind guarantees, external/library calls, inlining and tail calls |
| [ExceptionalControlFlow](../concepts/ExceptionalControlFlow.md) | Return/unwind/divergence/UB, personality, handlers, cleanups and nonlocal continuations |
| [ConvergentExecution](../concepts/ConvergentExecution.md) | Communicating dynamic instances and participants beyond ordinary memory effects |
| [StateRepresentation](../concepts/StateRepresentation.md) | Storage/register, aggregate and runtime-frame invariants with operation correspondence |
| [SymbolLinkage](../concepts/SymbolLinkage.md) | Link environments, interposition, ODR, exports, address identity and whole-program roots |
| [LLVMAttributeContract](../concepts/LLVMAttributeContract.md) | Scope-valid inferred/copied attributes, semantic metadata, ABI obligations and operand bundles |
| [RuntimeInstrumentation](../concepts/RuntimeInstrumentation.md) | Instrumentation trace projection, helper-runtime safety, public diagnostics and runtime protocols |

Existing [BitVector](../concepts/BitVector.md),
[FloatingPointType](../concepts/FloatingPointType.md),
[HoareTriple](../concepts/HoareTriple.md),
[Simulation](../concepts/Simulation.md),
[TerminationVariant](../concepts/TerminationVariant.md),
[JoinSemilattice](../concepts/JoinSemilattice.md) and graph concepts are reused.
Strong one-step simulation needs a separate stuttering/observation argument for
passes that remove steps. Finite partial-trace equivalence alone does not establish
preservation of termination or divergence.

The new hierarchy places refinement, flat CFG dominance and dynamic memory
dependence under binary relations. Integer maps specialize functions, with an
explicit expression interpretation; constants and floor/modulo prevent treating
them as linear maps. The subject sits under programming semantics. Prerequisites
and related concepts transfer no axioms.

## Choose obligations by pass family

| Transformation | Principal obligations |
| --- | --- |
| InstCombine, folding, canonicalization | Guarded contextual refinement; bit width and flags; per-use undef and poison; typing and dominance |
| DCE, CSE | Observable effects, termination/control, aliases, replacement availability and nondeterministic correlations |
| LICM, speculative execution | Newly executed reachable states, available operands, immediate UB, divergence, memory conflicts and execution multiplicity |
| Loop interchange, tiling, fusion | Event correspondence, empty/boundary iterations, scalar/control and memory dependencies, schedule order and index overflow |
| Reassociation, vectorization | Actual numeric laws, floating-point flags/rounding, inactive lanes, reduction order and memory ordering |
| Lowering, bufferization | Representation, zero/one/many type conversion, aliases/ownership/lifetime, materializations, layouts, shapes and ABI |
| Any mutating pass | Correct invalidation/update of analyses; well-formed output; compatible obligations for pipeline composition |

## Verification contract and retrieval

Keep the pass-specific contract beside the implementation using the
[implementation mapping skill](../ai/skills/implementation-mapping/SKILL.md).
Map normative clauses and catalog IDs to concrete APIs, carriers, equality,
representation and definedness before making a conformance claim. Retrieve small
interfaces first:

```sh
python3 scripts/catalog.py get BehaviorRefinement --sections operations axioms laws
python3 scripts/catalog.py get LLVMPoisonSemantics --sections operations axioms
python3 scripts/agent_query.py dossier GuardedRewrite --purpose proof --limit 80
python3 scripts/agent_query.py node urn:csabs:law/BehaviorRefinement-transitive
```

Record the exact source/target IR, compiler/dialect version, target triple and
data layout, admissible inputs, observation equality and assumptions. Where
relevant, map address spaces, alignment, pointer provenance, aliases, lifetimes,
shapes, index bounds, arithmetic flags, fast-math and attributes such as `noundef`.
Specify observable divergence, exceptions, I/O, atomics and synchronization.

For a rewrite, justify its guard, contextual refinement and output well-formedness.
Failed matching must leave IR unchanged. Prove driver termination separately when
required; pattern benefit and a bounded-recursion declaration supply no proof.
Confluence is needed when the contract promises a unique normal form.

For CFG refinement on source-safe states, require target progress as well as
step matching: a related target must be final or able to step. Otherwise a
vacuous step implication could hide a newly stuck target. Silent zero-source-step
matches also need a well-founded rank, and observations/initial/final states must
correspond. These proof obligations are adapted from the consulted
[CompCert backward-simulation interface](https://compcert.org/doc/html/compcert.common.Smallstep.html),
alongside LLVM-specific control and PHI constraints; the Lean model intentionally
encodes only a partial diagram.

For lowering, give explicit state/input/output representation relations.
Legalization, verifier success and successful materialization do not establish
semantic correspondence. For loops, memory-dependence preservation is one
obligation; scalar/control dependencies, computations and the event domain must
also be preserved. Conservatively model aliases and distinguish unsupported
analysis from proven independence.

Retain tool version, semantic subset, bounds, evidence and verdict. Pipeline
composition requires aligned intermediate semantics and assumptions. Update or
invalidate cached analyses before another pass consumes them.

## Core LLVM examples and correctness boundaries

Examples of transforms requiring these obligations include InstCombine/InstSimplify,
SCCP/IPSCCP/range propagation, EarlyCSE/GVN/NewGVN, DCE/ADCE/BDCE/DSE,
SimplifyCFG/jump threading/critical-edge and switch transformations,
mem2reg/reg2mem/SROA, memcpy and load/store optimization, LICM/sinking/speculation,
induction/strength reduction, loop canonicalization, unrolling, rotation,
unswitching, fusion/distribution/interchange/flattening, idioms, loop/SLP
vectorization and scalarization. Inlining/outlining, signature/tail-call changes,
attribute inference, global optimization/deadness/merging, devirtualization and
LTO/linkage transforms also require explicit obligations.

Other transform classes include atomics/EH/coroutine/GC lowerings, target and
library expansions, guards/deoptimization, profiling/sanitizers/security checks,
parallel and Objective-C runtime transforms, debug/metadata policies and pipeline
wrappers. Each needs an explicit contract for its intended behavior. For example,
`lower-atomic` needs the
documented non-preemptible execution assumption; `lower-invoke` needs an unwindless
contract; `forceattrs` needs justification of its imposed promises. Security
instrumentation can intentionally add diagnostics. Extraction/renaming/debug
stripping may change the chosen observations. Verification must establish the
applicable obligations under these conditions; the profiles do not assert every
pass preserves arbitrary source behavior in every environment.

Before checking an actual pass, instantiate a contract for its concrete mutation,
options and semantic subset. A profile helps select obligations; it is not
an executable pass precondition or an audit of every implementation branch.
Target DXIL/kernel, OpenMP/Objective-C and runtime lowerings require their own
external specifications. The generic coroutine lifecycle concept is related
context, not a complete LLVM coroutine ABI model.

## Small obligations that catch mistakes

**Overflow flags have a direction.** Removing `nsw` from ordinary scalar addition
is a refinement; adding it requires a no-overflow justification on relevant
defined executions. For `i4`, `7 + 1` wraps to `1000` without flags and produces
poison with `nsw`. A consuming context can expose immediate UB. Use `BitVector`
with the LLVM profile rather than the catalog signed-integer undefined-overflow
model. The [Alive2 README](https://github.com/AliveToolkit/alive2/blob/master/README.md)
has the corresponding remove/add-`nsw` validation example.

**Empty memory effects do not justify division hoisting.** The LLVM UB manual
shows a source branching on `c`, computing `udiv 3, v` only when true and returning
zero otherwise. Hoisting division before the branch introduces immediate UB at
`c=false, v=0`, where the source returns zero. Justify defined evaluation on the
newly executed paths.

**Freeze constrains correlations.** Undef-dependent uses can observe different
choices. Uses of one dynamically executed freeze result observe its one chosen
value; different freeze instructions can choose differently. Duplicating or
merging computations therefore needs choice-correlation reasoning alongside
ordinary algebraic identities.

**Analysis failure is inconclusive.** MLIR's `DependenceResult` separates `Failure`
from `NoDependence`. Unsupported accesses do not justify loop independence.
Keeping a CFG unchanged may preserve CFG-only analyses while value/effect analyses
still require invalidation.

**Ranges and versions both matter.** A two-byte store at offset zero can overlap
a one-byte access at offset one. Pointer inequality, differing access types or
one MemorySSA candidate alone do not establish independence or loaded-value
equality. A MemoryPhi merges may-reach memory versions, and an acquire load can
be a MemoryDef because it introduces ordering.

**Unknown trip count is not an empty loop.** ScalarEvolution's small constant
trip-count query uses zero for unknown/nonconstant results. Treating that result
as an exact zero can erase a live loop. Exit count plus one also needs a wide
enough representation and the correct entry/exit assumptions.

**Atomic and convergent behavior need execution context.** Relaxed/monotonic
atomics have per-location modification order without a universal order across
locations. Acquire/release synchronization needs the actual reads-from and scope
conditions. A convergent call can additionally depend on which threads execute
together, even when its ordinary memory-effect summary is empty.

**Masks and fast-math are specific permissions.** An inactive lane is not always
zero or even an ordinary value; its intrinsic can prescribe undef, poison or a
passthrough. A `contract` flag permits appropriate FP contraction and does not
authorize arbitrary reassociation. Default FP assumptions cannot substitute for
constrained-intrinsic rounding and observable exception behavior.

## Evidence and remaining scope

[`lean/Catalog/CompilerTransforms.lean`](../lean/Catalog/CompilerTransforms.lean)
and [`lean/Catalog/LLVMTransforms.lean`](../lean/Catalog/LLVMTransforms.lean)
provide 32 explicitly partial concept bindings with readable formulations and
stated limits. They define selected relations/carriers and expose typed SSA,
effect, analysis, execution and representation assumptions. Structure laws are
client hypotheses; they do not prove that LLVM/MLIR implementations satisfy
them. No new law/theorem proof witnesses or concrete pass proofs are registered.

The graph now has explicit pointer/memory, concurrency, vector/inactive-lane,
floating-point/fast-math, ABI and runtime contract profiles. Their Lean models
remain partial interfaces rather than complete executable LLVM semantics.
Complete memory/FP/weak-memory evaluators, dialect operational semantics,
bufferization ownership and affine/dependence solvers remain formalization
obligations. Source consultation, graph/SHACL checks, inventory completeness and
successful model compilation establish different things; none alone proves a
pass implementation refines its specification.

Alive2 is a possible per-instance LLVM validator, requiring a compatible revision
and supported IR. Its documentation excludes interprocedural transforms, and its
[author abstract](https://web.ist.utl.pt/nuno.lopes/pubs.php?id=alive2-pldi21)
explains that bounds can miss bugs. This change does not install or run Alive2 or
translate arbitrary MLIR dialects into its semantics. Bounded acceptance, lit,
FileCheck and execution tests do not establish universal unbounded refinement.
