# LLVM 21.1.8 pass obligation inventory

Generated from [the mapping manifest](../data/llvm/pass_obligations_21.1.8.json) with
`python3 scripts/llvm_transform_coverage.py --write`. Edit the manifest to change mappings.

Every literal module/CGSCC/function/loop/loopnest pass registration in llvm/lib/Passes/PassRegistry.def; not machine-code passes, out-of-tree plugins or all possible parameter/pipeline expansions.

Registry inventory and catalog obligation mapping only. Not semantic implementation audits, executable pass contracts or verified pass proofs. Extension/runtime families require their named external contracts.

Consulted 2026-11-16; registry SHA-256 `6247e5a7e9447d5dc127e0ac6e82702024d5a79b48d8353383c53c3dcbea63cf`.

The snapshot contains **361 registrations** in **34 families**:

- 249 obligation-mapped entries.
- 9 pipeline entries.
- 103 utility entries.

Counts are registration coverage, not counts of distinct algorithms, semantic completeness or verified passes.
Parameterized registrations count once; their possible options and pipeline expansions are not enumerated.

Every transforming entry also needs [behavior refinement](../concepts/BehaviorRefinement.md),
[guarded rewriting](../concepts/GuardedRewrite.md), output well-formedness and
[analysis preservation](../concepts/AnalysisPreservation.md), where applicable.

## Family contracts

### Local algebra, casts, comparisons and reassociation

Family `scalar-algebra`; kind `transform`.

[GuardedRewrite](../concepts/GuardedRewrite.md), [LLVMIntegerSemantics](../concepts/LLVMIntegerSemantics.md), [LLVMFloatingPointSemantics](../concepts/LLVMFloatingPointSemantics.md), [LLVMPoisonSemantics](../concepts/LLVMPoisonSemantics.md), [LLVMAttributeContract](../concepts/LLVMAttributeContract.md).

- Respect exact width/flags/undef correlations and use-site context; reassociation needs actual numeric permissions.

Registrations: `FUNCTION_PASS:aggressive-instcombine`, `FUNCTION_PASS:div-rem-pairs`, `FUNCTION_PASS:instsimplify`, `FUNCTION_PASS:nary-reassociate`, `FUNCTION_PASS:reassociate`, `FUNCTION_PASS:slsr`, `FUNCTION_PASS:typepromotion`, `FUNCTION_PASS_WITH_PARAMS:instcombine`, `LOOP_PASS:canon-freeze`, `LOOP_PASS:loop-instsimplify`.

### Constant, range, predicate, alignment and address-space facts

Family `constant-range-propagation`; kind `transform`.

[AbstractInterpretation](../concepts/AbstractInterpretation.md), [LLVMAttributeContract](../concepts/LLVMAttributeContract.md), [LLVMIntegerSemantics](../concepts/LLVMIntegerSemantics.md), [ControlFlowRefinement](../concepts/ControlFlowRefinement.md), [PointerProvenance](../concepts/PointerProvenance.md).

- Sound transfer and feasible-edge facts; no unknown-to-zero conversion; inferred promises hold at each attachment point.

Registrations: `MODULE_PASS_WITH_PARAMS:ipsccp`, `FUNCTION_PASS:alignment-from-assumptions`, `FUNCTION_PASS:assume-builder`, `FUNCTION_PASS:assume-simplify`, `FUNCTION_PASS:constraint-elimination`, `FUNCTION_PASS:correlated-propagation`, `FUNCTION_PASS:infer-address-spaces`, `FUNCTION_PASS:infer-alignment`, `FUNCTION_PASS:irce`, `FUNCTION_PASS:lower-constant-intrinsics`, `FUNCTION_PASS:sccp`.

### Value numbering and redundant computation/load elimination

Family `value-numbering`; kind `transform`.

[BehaviorRefinement](../concepts/BehaviorRefinement.md), [SSAForm](../concepts/SSAForm.md), [AliasAnalysis](../concepts/AliasAnalysis.md), [MemorySSA](../concepts/MemorySSA.md), [CallEffectContract](../concepts/CallEffectContract.md), [LLVMPoisonSemantics](../concepts/LLVMPoisonSemantics.md).

- Equivalent memory versions and valid dependence facts; replacement dominates; nondeterministic outcomes and call effects remain compatible.

Registrations: `FUNCTION_PASS:gvn-hoist`, `FUNCTION_PASS:gvn-sink`, `FUNCTION_PASS:newgvn`, `FUNCTION_PASS_WITH_PARAMS:early-cse`, `FUNCTION_PASS_WITH_PARAMS:gvn`.

### Branch/PHI, edge, block and region transformations

Family `cfg-rewrite`; kind `transform`.

[ControlFlowRefinement](../concepts/ControlFlowRefinement.md), [SSAForm](../concepts/SSAForm.md), [Dominance](../concepts/Dominance.md), [LLVMAttributeContract](../concepts/LLVMAttributeContract.md), [ExceptionalControlFlow](../concepts/ExceptionalControlFlow.md), [ConvergentExecution](../concepts/ConvergentExecution.md).

- Preserve edge-selected PHI values, observable paths, termination, blockaddress/callbr constraints and communicating instances.

Registrations: `FUNCTION_PASS:break-crit-edges`, `FUNCTION_PASS:callsite-splitting`, `FUNCTION_PASS:chr`, `FUNCTION_PASS:dfa-jump-threading`, `FUNCTION_PASS:fix-irreducible`, `FUNCTION_PASS:flatten-cfg`, `FUNCTION_PASS:indirectbr-expand`, `FUNCTION_PASS:jump-threading`, `FUNCTION_PASS:jump-table-to-switch`, `FUNCTION_PASS:lower-switch`, `FUNCTION_PASS:mergeicmps`, `FUNCTION_PASS:mergereturn`, `FUNCTION_PASS:select-optimize`, `FUNCTION_PASS:unify-loop-exits`, `FUNCTION_PASS:unreachableblockelim`, `FUNCTION_PASS_WITH_PARAMS:normalize`, `FUNCTION_PASS_WITH_PARAMS:simplifycfg`, `FUNCTION_PASS_WITH_PARAMS:structurizecfg`, `LOOP_PASS:loop-term-fold`, `LOOP_PASS:loop-simplifycfg`.

### Dead instruction, control and loop elimination

Family `dead-code`; kind `transform`.

[BehaviorRefinement](../concepts/BehaviorRefinement.md), [EffectSummary](../concepts/EffectSummary.md), [ControlFlowRefinement](../concepts/ControlFlowRefinement.md), [CallEffectContract](../concepts/CallEffectContract.md), [LLVMPoisonSemantics](../concepts/LLVMPoisonSemantics.md).

- Establish unobservability and appropriate progress assumptions; deleting an infinite effect-free loop still needs a termination contract.

Registrations: `FUNCTION_PASS:adce`, `FUNCTION_PASS:bdce`, `FUNCTION_PASS:dce`, `LOOP_PASS:loop-deletion`.

### Store/load, copy, initialization and memory motion

Family `memory-opt`; kind `transform`.

[ByteMemory](../concepts/ByteMemory.md), [PointerProvenance](../concepts/PointerProvenance.md), [DataLayout](../concepts/DataLayout.md), [AliasAnalysis](../concepts/AliasAnalysis.md), [MemorySSA](../concepts/MemorySSA.md), [LLVMAttributeContract](../concepts/LLVMAttributeContract.md), [AtomicMemoryModel](../concepts/AtomicMemoryModel.md).

- Use byte-range overlap, lifetime and complete clobber facts; preserve volatile/atomic behavior and memcpy/memmove definedness.

Registrations: `FUNCTION_PASS:dse`, `FUNCTION_PASS:interleaved-load-combine`, `FUNCTION_PASS:loop-load-elim`, `FUNCTION_PASS:memcpyopt`, `FUNCTION_PASS:move-auto-init`, `FUNCTION_PASS_WITH_PARAMS:mldst-motion`.

### Stack/register, aggregate and by-reference/by-value representation

Family `storage-representation`; kind `transform`.

[StateRepresentation](../concepts/StateRepresentation.md), [SSAForm](../concepts/SSAForm.md), [Dominance](../concepts/Dominance.md), [ByteMemory](../concepts/ByteMemory.md), [PointerProvenance](../concepts/PointerProvenance.md), [DataLayout](../concepts/DataLayout.md), [CallEffectContract](../concepts/CallEffectContract.md).

- Preserve path-dependent/uninitialized values, byte offsets/padding, escapes and lifetimes; parameter promotion also preserves ABI and new-path access safety.

Registrations: `CGSCC_PASS:argpromotion`, `FUNCTION_PASS:mem2reg`, `FUNCTION_PASS:reg2mem`, `FUNCTION_PASS_WITH_PARAMS:sroa`.

### Loop canonicalization, rotation and loop-closed SSA

Family `loop-structure`; kind `transform`.

[ControlFlowRefinement](../concepts/ControlFlowRefinement.md), [LoopIterationMapping](../concepts/LoopIterationMapping.md), [SSAForm](../concepts/SSAForm.md), [Dominance](../concepts/Dominance.md), [ScalarRecurrence](../concepts/ScalarRecurrence.md).

- Preserve zero-trip behavior, exit values, all exits and analysis scopes; rebuild loop/dominance facts.

Registrations: `FUNCTION_PASS:lcssa`, `FUNCTION_PASS:loop-simplify`, `LOOP_PASS_WITH_PARAMS:loop-rotate`.

### Loop/code motion and speculation

Family `loop-motion`; kind `transform`.

[SpeculationSafety](../concepts/SpeculationSafety.md), [LoopDependence](../concepts/LoopDependence.md), [AliasAnalysis](../concepts/AliasAnalysis.md), [MemorySSA](../concepts/MemorySSA.md), [LoopIterationMapping](../concepts/LoopIterationMapping.md), [CallEffectContract](../concepts/CallEffectContract.md), [ConvergentExecution](../concepts/ConvergentExecution.md).

- Justify newly executed states and changed multiplicity; no unguarded division/load UB or added divergence, effects or communication changes.

Registrations: `FUNCTION_PASS:loop-sink`, `FUNCTION_PASS:sink`, `FUNCTION_PASS_WITH_PARAMS:speculative-execution`, `LOOP_PASS:loop-versioning-licm`, `LOOP_PASS_WITH_PARAMS:licm`, `LOOP_PASS_WITH_PARAMS:lnicm`.

### Unrolling, fusion/fission, interchange, flattening and versioning

Family `loop-event-rewrite`; kind `transform`.

[LoopIterationMapping](../concepts/LoopIterationMapping.md), [LoopDependence](../concepts/LoopDependence.md), [ScalarRecurrence](../concepts/ScalarRecurrence.md), [IntegerAffineMap](../concepts/IntegerAffineMap.md), [ControlFlowRefinement](../concepts/ControlFlowRefinement.md), [LLVMIntegerSemantics](../concepts/LLVMIntegerSemantics.md).

- Account for complete event domains, tails/multiple exits and guard partitions; preserve all scalar/control/memory dependencies and values.

Registrations: `FUNCTION_PASS:loop-distribute`, `FUNCTION_PASS:loop-fusion`, `FUNCTION_PASS:loop-versioning`, `FUNCTION_PASS_WITH_PARAMS:loop-unroll`, `LOOPNEST_PASS:loop-flatten`, `LOOPNEST_PASS:loop-interchange`, `LOOPNEST_PASS:loop-unroll-and-jam`, `LOOP_PASS:loop-bound-split`, `LOOP_PASS:loop-unroll-full`, `LOOP_PASS_WITH_PARAMS:simple-loop-unswitch`.

### Induction canonicalization and strength reduction

Family `loop-induction`; kind `transform`.

[ScalarRecurrence](../concepts/ScalarRecurrence.md), [LLVMIntegerSemantics](../concepts/LLVMIntegerSemantics.md), [PointerProvenance](../concepts/PointerProvenance.md), [LoopIterationMapping](../concepts/LoopIterationMapping.md).

- Scope-nowrap/range facts and count widths; recurrence lifting and exit comparisons must match modular IR arithmetic.

Registrations: `FUNCTION_PASS:separate-const-offset-from-gep`, `FUNCTION_PASS_WITH_PARAMS:separate-const-offset-from-gep`, `LOOP_PASS:evl-iv-simplify`, `LOOP_PASS:indvars`, `LOOP_PASS:loop-reduce`.

### Loop-to-intrinsic/libcall/idiom replacement

Family `loop-idioms`; kind `transform`.

[LoopIterationMapping](../concepts/LoopIterationMapping.md), [ByteMemory](../concepts/ByteMemory.md), [CallEffectContract](../concepts/CallEffectContract.md), [LLVMIntegerSemantics](../concepts/LLVMIntegerSemantics.md), [PredicatedVectorSemantics](../concepts/PredicatedVectorSemantics.md).

- Use an outcome/representation argument when events are aggregated; establish intrinsic or libcall length, overlap, byte and target contracts.

Registrations: `LOOP_PASS:loop-idiom`, `LOOP_PASS:loop-idiom-vectorize`.

### Loop/SLP vectorization, lane combination, scalarization and interleaving

Family `vector-transforms`; kind `transform`.

[PredicatedVectorSemantics](../concepts/PredicatedVectorSemantics.md), [LoopIterationMapping](../concepts/LoopIterationMapping.md), [LoopDependence](../concepts/LoopDependence.md), [LLVMFloatingPointSemantics](../concepts/LLVMFloatingPointSemantics.md), [LLVMIntegerSemantics](../concepts/LLVMIntegerSemantics.md), [ByteMemory](../concepts/ByteMemory.md), [ConvergentExecution](../concepts/ConvergentExecution.md).

- Respect runtime scalable width, masks/EVL/tails, inactive poison/undef/passthrough, active memory lanes, reduction order and alias runtime guards.

Registrations: `FUNCTION_PASS:complex-deinterleaving`, `FUNCTION_PASS:expand-reductions`, `FUNCTION_PASS:interleaved-access`, `FUNCTION_PASS:load-store-vectorizer`, `FUNCTION_PASS:sandbox-vectorizer`, `FUNCTION_PASS:scalarize-masked-mem-intrin`, `FUNCTION_PASS:slp-vectorizer`, `FUNCTION_PASS:vector-combine`, `FUNCTION_PASS_WITH_PARAMS:loop-vectorize`, `FUNCTION_PASS_WITH_PARAMS:scalarizer`.

### Floating-point conversion and target-library substitution

Family `fp-and-libcalls`; kind `transform`.

[LLVMFloatingPointSemantics](../concepts/LLVMFloatingPointSemantics.md), [LLVMIntegerSemantics](../concepts/LLVMIntegerSemantics.md), [CallEffectContract](../concepts/CallEffectContract.md), [LLVMAttributeContract](../concepts/LLVMAttributeContract.md).

- Respect NaN/infinity/signed-zero/rounding/exception/errno contracts and symbol preemption; library availability is target-specific.

Registrations: `FUNCTION_PASS:float2int`, `FUNCTION_PASS:inject-tli-mappings`, `FUNCTION_PASS:libcalls-shrinkwrap`, `FUNCTION_PASS:partially-inline-libcalls`, `FUNCTION_PASS:replace-with-veclib`.

### Inlining, outlining and extraction

Family `inline-outline`; kind `transform`.

[CallEffectContract](../concepts/CallEffectContract.md), [StateRepresentation](../concepts/StateRepresentation.md), [ControlFlowRefinement](../concepts/ControlFlowRefinement.md), [ExceptionalControlFlow](../concepts/ExceptionalControlFlow.md), [LLVMAttributeContract](../concepts/LLVMAttributeContract.md), [SymbolLinkage](../concepts/SymbolLinkage.md).

- Preserve call arguments/results, stack freshness/lifetime, normal/unwind/deopt continuations, recursion, bundles and symbol identity; extraction can intentionally change the selected program contract.

Registrations: `MODULE_PASS:always-inline`, `MODULE_PASS:extract-blocks`, `MODULE_PASS:hotcoldsplit`, `MODULE_PASS:inliner-ml-advisor-release`, `MODULE_PASS:inliner-wrapper`, `MODULE_PASS:inliner-wrapper-no-mandatory-first`, `MODULE_PASS:iroutliner`, `MODULE_PASS:module-inline`, `MODULE_PASS:partial-inliner`, `MODULE_PASS:scc-oz-module-inliner`, `MODULE_PASS_WITH_PARAMS:loop-extract`, `CGSCC_PASS_WITH_PARAMS:inline`.

### Call signatures, indirect-call promotion and tail recursion

Family `call-and-tail`; kind `transform`.

[CallEffectContract](../concepts/CallEffectContract.md), [SymbolLinkage](../concepts/SymbolLinkage.md), [ControlFlowRefinement](../concepts/ControlFlowRefinement.md), [LLVMAttributeContract](../concepts/LLVMAttributeContract.md).

- Preserve ABI, calling conventions, musttail constraints, stack-observable behavior, fallback dispatch and external callers.

Registrations: `MODULE_PASS:called-value-propagation`, `MODULE_PASS:deadargelim`, `MODULE_PASS:pgo-icall-prom`, `FUNCTION_PASS:tailcallelim`.

### Interprocedural attributes and externally supplied attribute policies

Family `attribute-inference`; kind `transform`.

[LLVMAttributeContract](../concepts/LLVMAttributeContract.md), [AbstractInterpretation](../concepts/AbstractInterpretation.md), [CallEffectContract](../concepts/CallEffectContract.md), [SymbolLinkage](../concepts/SymbolLinkage.md).

- Inference needs universal scoped evidence; forceattrs and externally imposed policies need an explicit caller-supplied truth contract.

Registrations: `MODULE_PASS:attributor`, `MODULE_PASS:attributor-light`, `MODULE_PASS:noinline-nonprevailing`, `MODULE_PASS:forceattrs`, `MODULE_PASS:inferattrs`, `MODULE_PASS:pgo-force-function-attrs`, `MODULE_PASS:rpo-function-attrs`, `CGSCC_PASS:attributor-cgscc`, `CGSCC_PASS:attributor-light-cgscc`, `CGSCC_PASS_WITH_PARAMS:function-attrs`.

### Globals, symbol resolution, LTO, merging and devirtualization

Family `globals-linkage`; kind `transform`.

[SymbolLinkage](../concepts/SymbolLinkage.md), [StateRepresentation](../concepts/StateRepresentation.md), [DataLayout](../concepts/DataLayout.md), [PointerProvenance](../concepts/PointerProvenance.md), [CallEffectContract](../concepts/CallEffectContract.md), [LLVMAttributeContract](../concepts/LLVMAttributeContract.md).

- Account for interposition/ODR/COMDAT/used roots/address identity, external aliases/callbacks and ABI; renaming/internalizing requires the declared link environment.

Registrations: `MODULE_PASS:canonicalize-aliases`, `MODULE_PASS:constmerge`, `MODULE_PASS:elim-avail-extern`, `MODULE_PASS:function-import`, `MODULE_PASS:global-merge-func`, `MODULE_PASS:globalopt`, `MODULE_PASS:globalsplit`, `MODULE_PASS:lower-ifunc`, `MODULE_PASS:simplify-type-tests`, `MODULE_PASS:lowertypetests`, `MODULE_PASS:fatlto-cleanup`, `MODULE_PASS:mergefunc`, `MODULE_PASS:rel-lookup-table-converter`, `MODULE_PASS:rewrite-symbols`, `MODULE_PASS:wholeprogramdevirt`, `MODULE_PASS_WITH_PARAMS:global-merge`, `MODULE_PASS_WITH_PARAMS:globaldce`, `MODULE_PASS_WITH_PARAMS:internalize`.

### Atomic instruction lowering

Family `atomic-lowering`; kind `transform`.

[AtomicMemoryModel](../concepts/AtomicMemoryModel.md), [ByteMemory](../concepts/ByteMemory.md), [CallEffectContract](../concepts/CallEffectContract.md), [StateRepresentation](../concepts/StateRepresentation.md).

- Preserve allowed executions, RMW indivisibility, success/failure orderings and scope; lower-atomic requires an explicit non-preemptible/single-thread environment, not generic concurrent equivalence.

Registrations: `FUNCTION_PASS:atomic-expand`, `FUNCTION_PASS:lower-atomic`.

### Exception and nonlocal control preparation/lowering

Family `exception-lowering`; kind `transform`.

[ExceptionalControlFlow](../concepts/ExceptionalControlFlow.md), [CallEffectContract](../concepts/CallEffectContract.md), [ControlFlowRefinement](../concepts/ControlFlowRefinement.md), [LLVMAttributeContract](../concepts/LLVMAttributeContract.md).

- Match the selected personality/target ABI, cleanup/funclet and continuation semantics; lower-invoke uses an explicit unwindless contract.

Registrations: `FUNCTION_PASS:callbr-prepare`, `FUNCTION_PASS:dwarf-eh-prepare`, `FUNCTION_PASS:lower-invoke`, `FUNCTION_PASS:sjlj-eh-prepare`, `FUNCTION_PASS:wasm-eh-prepare`, `FUNCTION_PASS_WITH_PARAMS:win-eh-prepare`.

### Coroutine frame, split, elision and cleanup

Family `coroutine-lowering`; kind `transform`.

[AsymmetricCoroutine](../concepts/AsymmetricCoroutine.md), [StateRepresentation](../concepts/StateRepresentation.md), [CallEffectContract](../concepts/CallEffectContract.md), [ControlFlowRefinement](../concepts/ControlFlowRefinement.md), [ByteMemory](../concepts/ByteMemory.md).

- Preserve frame escape/lifetime, suspension/resumption/destruction protocol, promises, allocation and exceptional paths under the chosen coroutine ABI.

Registrations: `MODULE_PASS:coro-cleanup`, `MODULE_PASS:coro-early`, `CGSCC_PASS:coro-annotation-elide`, `CGSCC_PASS_WITH_PARAMS:coro-split`, `FUNCTION_PASS:coro-elide`.

### Garbage-collection roots, safepoints, statepoints and relocation

Family `gc-runtime`; kind `transform`.

[RuntimeInstrumentation](../concepts/RuntimeInstrumentation.md), [StateRepresentation](../concepts/StateRepresentation.md), [PointerProvenance](../concepts/PointerProvenance.md), [CallEffectContract](../concepts/CallEffectContract.md), [ByteMemory](../concepts/ByteMemory.md).

- Preserve live root/derived-pointer identity across relocation, collector protocol and stack-map state; dropping relocates requires the exact lowering phase contract.

Registrations: `MODULE_PASS:rewrite-statepoints-for-gc`, `MODULE_PASS:shadow-stack-gc-lowering`, `FUNCTION_PASS:gc-lowering`, `FUNCTION_PASS:place-safepoints`, `FUNCTION_PASS:strip-gc-relocates`.

### Target/runtime/ABI preparation and intrinsic expansion

Family `runtime-lowering`; kind `transform`.

[StateRepresentation](../concepts/StateRepresentation.md), [DataLayout](../concepts/DataLayout.md), [CallEffectContract](../concepts/CallEffectContract.md), [LLVMIntegerSemantics](../concepts/LLVMIntegerSemantics.md), [LLVMFloatingPointSemantics](../concepts/LLVMFloatingPointSemantics.md), [ControlFlowRefinement](../concepts/ControlFlowRefinement.md), [PredicatedVectorSemantics](../concepts/PredicatedVectorSemantics.md).

- Instantiate the target and intrinsic/runtime semantics; preserve arithmetic, layouts, matrix/lane correspondence, initialization and calling convention. Cost models and target legality are separate from correctness.

Registrations: `MODULE_PASS:declare-runtime-libcalls`, `MODULE_PASS:expand-variadics`, `MODULE_PASS:lower-emutls`, `MODULE_PASS:lower-global-dtors`, `MODULE_PASS:pre-isel-intrinsic-lowering`, `FUNCTION_PASS:codegenprepare`, `FUNCTION_PASS:expand-large-div-rem`, `FUNCTION_PASS:expand-fp`, `FUNCTION_PASS:expand-memcmp`, `FUNCTION_PASS:lower-expect`, `FUNCTION_PASS_WITH_PARAMS:hardware-loops`, `FUNCTION_PASS_WITH_PARAMS:lower-matrix-intrinsics`.

### Guards, deoptimization and check selection

Family `guard-deopt`; kind `transform`.

[ControlFlowRefinement](../concepts/ControlFlowRefinement.md), [LLVMAttributeContract](../concepts/LLVMAttributeContract.md), [CallEffectContract](../concepts/CallEffectContract.md), [SpeculationSafety](../concepts/SpeculationSafety.md).

- Retain deopt state/continuations and widened-condition definedness; removing checks or allow-check operations needs their documented policy and admitted-input contract.

Registrations: `FUNCTION_PASS:guard-widening`, `FUNCTION_PASS:lower-guard-intrinsic`, `FUNCTION_PASS:lower-widenable-condition`, `FUNCTION_PASS:make-guards-explicit`, `FUNCTION_PASS_WITH_PARAMS:lower-allow-check`, `LOOP_PASS:guard-widening`, `LOOP_PASS:loop-predication`.

### Sanitizer, tracing, coverage, profiling and instrumentation lowering

Family `instrumentation`; kind `transform`.

[RuntimeInstrumentation](../concepts/RuntimeInstrumentation.md), [ByteMemory](../concepts/ByteMemory.md), [CallEffectContract](../concepts/CallEffectContract.md), [AtomicMemoryModel](../concepts/AtomicMemoryModel.md), [LLVMAttributeContract](../concepts/LLVMAttributeContract.md).

- Separate projection of internal events from requested public diagnostics/profile outputs; justify helper runtime safety, counter atomicity, initialization and valid-input behavior.

Registrations: `MODULE_PASS:ctx-instr-gen`, `MODULE_PASS:ctx-prof-flatten`, `MODULE_PASS:ctx-prof-flatten-prethinlink`, `MODULE_PASS:dfsan`, `MODULE_PASS:insert-gcov-profiling`, `MODULE_PASS:instrprof`, `MODULE_PASS:ctx-instr-lower`, `MODULE_PASS:memprof-context-disambiguation`, `MODULE_PASS:memprof-module`, `MODULE_PASS:nsan`, `MODULE_PASS:pgo-instr-gen`, `MODULE_PASS:pgo-instr-use`, `MODULE_PASS:pseudo-probe`, `MODULE_PASS:pseudo-probe-update`, `MODULE_PASS:rtsan`, `MODULE_PASS:sample-profile`, `MODULE_PASS:sancov-module`, `MODULE_PASS:sanmd-module`, `MODULE_PASS:tsan-module`, `MODULE_PASS:tysan`, `MODULE_PASS_WITH_PARAMS:asan`, `MODULE_PASS_WITH_PARAMS:cg-profile`, `MODULE_PASS_WITH_PARAMS:hwasan`, `MODULE_PASS_WITH_PARAMS:memprof-use`, `MODULE_PASS_WITH_PARAMS:msan`, `FUNCTION_PASS:count-visits`, `FUNCTION_PASS:memprof`, `FUNCTION_PASS:pgo-memop-opt`, `FUNCTION_PASS:tsan`, `FUNCTION_PASS_WITH_PARAMS:ee-instrument`.

### Bounds/CFI and stack/security/runtime checks

Family `security-instrumentation`; kind `transform`.

[RuntimeInstrumentation](../concepts/RuntimeInstrumentation.md), [StateRepresentation](../concepts/StateRepresentation.md), [CallEffectContract](../concepts/CallEffectContract.md), [ExceptionalControlFlow](../concepts/ExceptionalControlFlow.md), [SymbolLinkage](../concepts/SymbolLinkage.md).

- Specify violation diagnostics, helper ABI, protected metadata/layout and admitted valid behavior; security enforcement is an additional property, not ordinary equality on all executions.

Registrations: `MODULE_PASS:cross-dso-cfi`, `MODULE_PASS:jmc-instrumenter`, `FUNCTION_PASS:kcfi`, `FUNCTION_PASS:safe-stack`, `FUNCTION_PASS:stack-protector`, `FUNCTION_PASS_WITH_PARAMS:cfguard`, `FUNCTION_PASS_WITH_PARAMS:bounds-checking`.

### OpenMP, parallel runtime and accelerator boundary transforms

Family `parallel-runtime`; kind `transform`.

[AtomicMemoryModel](../concepts/AtomicMemoryModel.md), [ConvergentExecution](../concepts/ConvergentExecution.md), [RuntimeInstrumentation](../concepts/RuntimeInstrumentation.md), [CallEffectContract](../concepts/CallEffectContract.md), [SymbolLinkage](../concepts/SymbolLinkage.md).

- Bind the actual parallel/runtime/target specification, thread/team and allocation semantics; do not infer correctness from sequential effects or these generic interfaces alone.

Registrations: `MODULE_PASS:hipstdpar-interpose-alloc`, `MODULE_PASS:hipstdpar-select-accelerator-code`, `MODULE_PASS:openmp-opt`, `MODULE_PASS:openmp-opt-postlink`, `CGSCC_PASS:openmp-opt-cgscc`.

### Objective-C reference-counting runtime transforms

Family `objc-runtime`; kind `transform`.

[StateRepresentation](../concepts/StateRepresentation.md), [ByteMemory](../concepts/ByteMemory.md), [CallEffectContract](../concepts/CallEffectContract.md), [RuntimeInstrumentation](../concepts/RuntimeInstrumentation.md).

- Retain ownership/autorelease/weak-reference/exception and object-lifetime invariants from the external Objective-C runtime contract.

Registrations: `MODULE_PASS:objc-arc-apelim`, `FUNCTION_PASS:objc-arc`, `FUNCTION_PASS:objc-arc-contract`, `FUNCTION_PASS:objc-arc-expand`.

### Target dialect/ABI extensions in the core registry

Family `target-extension`; kind `transform`.

[DataLayout](../concepts/DataLayout.md), [StateRepresentation](../concepts/StateRepresentation.md), [LLVMAttributeContract](../concepts/LLVMAttributeContract.md), [CallEffectContract](../concepts/CallEffectContract.md), [PredicatedVectorSemantics](../concepts/PredicatedVectorSemantics.md).

- Bind the external DXIL/kernel ABI specification and exact intrinsic/metadata semantics; generic model compilation does not establish target conformance.

Registrations: `MODULE_PASS:dxil-upgrade`, `FUNCTION_PASS:kernel-info`.

### Constant placement and prefetch hints

Family `prefetch-layout`; kind `transform`.

[SpeculationSafety](../concepts/SpeculationSafety.md), [PointerProvenance](../concepts/PointerProvenance.md), [ByteMemory](../concepts/ByteMemory.md), [LLVMAttributeContract](../concepts/LLVMAttributeContract.md).

- Respect target intrinsic definedness, address-space/provenance and new-path operands; profitability/profile hints do not justify semantic changes.

Registrations: `FUNCTION_PASS:consthoist`, `FUNCTION_PASS:loop-data-prefetch`.

### Metadata, naming, debug and embedding policies

Family `metadata-debug`; kind `transform`.

[LLVMAttributeContract](../concepts/LLVMAttributeContract.md), [SymbolLinkage](../concepts/SymbolLinkage.md), [StateRepresentation](../concepts/StateRepresentation.md).

- Choose whether debug/symbol/embedded artifacts are observations; retain semantic metadata, operand bundles and externally visible identities unless the policy explicitly changes them.

Registrations: `MODULE_PASS:annotation2metadata`, `MODULE_PASS:assign-guid`, `MODULE_PASS:debugify`, `MODULE_PASS:metarenamer`, `MODULE_PASS:name-anon-globals`, `MODULE_PASS:strip`, `MODULE_PASS:strip-dead-debug-info`, `MODULE_PASS:strip-dead-prototypes`, `MODULE_PASS:strip-debug-declare`, `MODULE_PASS:strip-nondebug`, `MODULE_PASS:strip-nonlinetable-debuginfo`, `MODULE_PASS:strip-dead-cg-profile`, `MODULE_PASS_WITH_PARAMS:embed-bitcode`, `FUNCTION_PASS:add-discriminators`, `FUNCTION_PASS:declare-to-assign`, `FUNCTION_PASS:instnamer`, `FUNCTION_PASS:redundant-dbg-inst-elim`.

### Parameterized pipeline wrappers

Family `pipeline`; kind `pipeline`.

[BehaviorRefinement](../concepts/BehaviorRefinement.md), [AnalysisPreservation](../concepts/AnalysisPreservation.md), [LLVMAttributeContract](../concepts/LLVMAttributeContract.md).

- Expand the actual target/options-dependent pipeline; compose only compatible intermediate contracts and update/invalidate analyses after each mutation.

Registrations: `MODULE_PASS_WITH_PARAMS:default`, `MODULE_PASS_WITH_PARAMS:thinlto-pre-link`, `MODULE_PASS_WITH_PARAMS:thinlto`, `MODULE_PASS_WITH_PARAMS:lto-pre-link`, `MODULE_PASS_WITH_PARAMS:lto`, `MODULE_PASS_WITH_PARAMS:fatlto-pre-link`, `FUNCTION_PASS:extra-vector-passes`, `FUNCTION_PASS_WITH_PARAMS:function-simplification`, `LOOP_PASS:extra-simple-loop-unswitch-passes`.

### Analysis recomputation

Family `analysis-maintenance`; kind `utility`.

[AnalysisPreservation](../concepts/AnalysisPreservation.md), [AbstractInterpretation](../concepts/AbstractInterpretation.md).

- Validate recomputed facts against the current IR and dependency state.

Registrations: `MODULE_PASS:invalidate<all>`, `MODULE_PASS:recompute-globalsaa`, `CGSCC_PASS:invalidate<all>`, `FUNCTION_PASS:invalidate<all>`, `LOOP_PASS:invalidate<all>`.

### Evaluation, examples, diagnostics and intentional failure tests

Family `diagnostic-tools`; kind `utility`.

[AnalysisPreservation](../concepts/AnalysisPreservation.md), [LLVMAttributeContract](../concepts/LLVMAttributeContract.md).

- Retain tooling expectations; deliberate crash/error entries are negative-test utilities, not optimizing transforms.

Registrations: `MODULE_PASS:check-debugify`, `MODULE_PASS:dot-callgraph`, `MODULE_PASS:print<ctx-prof-analysis>`, `MODULE_PASS:no-op-module`, `MODULE_PASS:print`, `MODULE_PASS:print-callgraph`, `MODULE_PASS:print-callgraph-sccs`, `MODULE_PASS:print-ir-similarity`, `MODULE_PASS:print-lcg`, `MODULE_PASS:print-lcg-dot`, `MODULE_PASS:print-must-be-executed-contexts`, `MODULE_PASS:print-profile-summary`, `MODULE_PASS:print-stack-safety`, `MODULE_PASS:print<dxil-metadata>`, `MODULE_PASS:print<dxil-resources>`, `MODULE_PASS:print<inline-advisor>`, `MODULE_PASS:print<ir2vec>`, `MODULE_PASS:print<ir2vec-vocab>`, `MODULE_PASS:print<module-debuginfo>`, `MODULE_PASS:print<reg-usage>`, `MODULE_PASS:trigger-crash-module`, `MODULE_PASS:trigger-verifier-error`, `MODULE_PASS:verify`, `MODULE_PASS:view-callgraph`, `MODULE_PASS_WITH_PARAMS:print<structural-hash>`, `CGSCC_PASS:no-op-cgscc`, `FUNCTION_PASS:aa-eval`, `FUNCTION_PASS:annotation-remarks`, `FUNCTION_PASS:dot-cfg`, `FUNCTION_PASS:dot-cfg-only`, `FUNCTION_PASS:dot-dom`, `FUNCTION_PASS:dot-dom-only`, `FUNCTION_PASS:dot-post-dom`, `FUNCTION_PASS:dot-post-dom-only`, `FUNCTION_PASS:helloworld`, `FUNCTION_PASS:instcount`, `FUNCTION_PASS:no-op-function`, `FUNCTION_PASS:pa-eval`, `FUNCTION_PASS:print`, `FUNCTION_PASS:print-alias-sets`, `FUNCTION_PASS:print-cfg-sccs`, `FUNCTION_PASS:print-memderefs`, `FUNCTION_PASS:print-mustexecute`, `FUNCTION_PASS:print-predicateinfo`, `FUNCTION_PASS:print<assumptions>`, `FUNCTION_PASS:print<block-freq>`, `FUNCTION_PASS:print<branch-prob>`, `FUNCTION_PASS:print<cost-model>`, `FUNCTION_PASS:print<cycles>`, `FUNCTION_PASS:print<da>`, `FUNCTION_PASS:print<debug-ata>`, `FUNCTION_PASS:print<delinearization>`, `FUNCTION_PASS:print<demanded-bits>`, `FUNCTION_PASS:print<domfrontier>`, `FUNCTION_PASS:print<domtree>`, `FUNCTION_PASS:print<func-properties>`, `FUNCTION_PASS:print<inline-cost>`, `FUNCTION_PASS:print<inliner-size-estimator>`, `FUNCTION_PASS:print<lazy-value-info>`, `FUNCTION_PASS:print<loops>`, `FUNCTION_PASS:print<memoryssa-walker>`, `FUNCTION_PASS:print<phi-values>`, `FUNCTION_PASS:print<postdomtree>`, `FUNCTION_PASS:print<regions>`, `FUNCTION_PASS:print<scalar-evolution>`, `FUNCTION_PASS:print<stack-safety-local>`, `FUNCTION_PASS:print<uniformity>`, `FUNCTION_PASS:transform-warning`, `FUNCTION_PASS:trigger-crash-function`, `FUNCTION_PASS:trigger-verifier-error`, `FUNCTION_PASS:verify`, `FUNCTION_PASS:verify<cycles>`, `FUNCTION_PASS:verify<domtree>`, `FUNCTION_PASS:verify<loops>`, `FUNCTION_PASS:verify<memoryssa>`, `FUNCTION_PASS:verify<regions>`, `FUNCTION_PASS:verify<safepoint-ir>`, `FUNCTION_PASS:verify<scalar-evolution>`, `FUNCTION_PASS:view-cfg`, `FUNCTION_PASS:view-cfg-only`, `FUNCTION_PASS:view-dom`, `FUNCTION_PASS:view-dom-only`, `FUNCTION_PASS:view-post-dom`, `FUNCTION_PASS:view-post-dom-only`, `FUNCTION_PASS_WITH_PARAMS:lint`, `FUNCTION_PASS_WITH_PARAMS:print<access-info>`, `FUNCTION_PASS_WITH_PARAMS:print<da>`, `FUNCTION_PASS_WITH_PARAMS:print<memoryssa>`, `FUNCTION_PASS_WITH_PARAMS:print<stack-lifetime>`, `LOOPNEST_PASS:no-op-loopnest`, `LOOP_PASS:dot-ddg`, `LOOP_PASS:no-op-loop`, `LOOP_PASS:print`, `LOOP_PASS:print<ddg>`, `LOOP_PASS:print<hash-recognize>`, `LOOP_PASS:print<iv-users>`, `LOOP_PASS:print<loop-cache-cost>`, `LOOP_PASS:print<loopnest>`.

## Complete registration index

Source: [LLVM 21.1.8 PassRegistry.def](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/lib/Passes/PassRegistry.def).

| Macro | Pass spelling | Family | Source line |
| --- | --- | --- | --- |
| `MODULE_PASS` | `always-inline` | `inline-outline` | 52 |
| `MODULE_PASS` | `annotation2metadata` | `metadata-debug` | 53 |
| `MODULE_PASS` | `assign-guid` | `metadata-debug` | 54 |
| `MODULE_PASS` | `attributor` | `attribute-inference` | 55 |
| `MODULE_PASS` | `attributor-light` | `attribute-inference` | 56 |
| `MODULE_PASS` | `called-value-propagation` | `call-and-tail` | 57 |
| `MODULE_PASS` | `canonicalize-aliases` | `globals-linkage` | 58 |
| `MODULE_PASS` | `check-debugify` | `diagnostic-tools` | 59 |
| `MODULE_PASS` | `constmerge` | `globals-linkage` | 60 |
| `MODULE_PASS` | `coro-cleanup` | `coroutine-lowering` | 61 |
| `MODULE_PASS` | `coro-early` | `coroutine-lowering` | 62 |
| `MODULE_PASS` | `cross-dso-cfi` | `security-instrumentation` | 63 |
| `MODULE_PASS` | `ctx-instr-gen` | `instrumentation` | 64 |
| `MODULE_PASS` | `ctx-prof-flatten` | `instrumentation` | 66 |
| `MODULE_PASS` | `ctx-prof-flatten-prethinlink` | `instrumentation` | 68 |
| `MODULE_PASS` | `noinline-nonprevailing` | `attribute-inference` | 70 |
| `MODULE_PASS` | `deadargelim` | `call-and-tail` | 71 |
| `MODULE_PASS` | `debugify` | `metadata-debug` | 72 |
| `MODULE_PASS` | `declare-runtime-libcalls` | `runtime-lowering` | 73 |
| `MODULE_PASS` | `dfsan` | `instrumentation` | 74 |
| `MODULE_PASS` | `dot-callgraph` | `diagnostic-tools` | 75 |
| `MODULE_PASS` | `dxil-upgrade` | `target-extension` | 76 |
| `MODULE_PASS` | `elim-avail-extern` | `globals-linkage` | 77 |
| `MODULE_PASS` | `extract-blocks` | `inline-outline` | 78 |
| `MODULE_PASS` | `expand-variadics` | `runtime-lowering` | 79 |
| `MODULE_PASS` | `forceattrs` | `attribute-inference` | 81 |
| `MODULE_PASS` | `function-import` | `globals-linkage` | 82 |
| `MODULE_PASS` | `global-merge-func` | `globals-linkage` | 83 |
| `MODULE_PASS` | `globalopt` | `globals-linkage` | 84 |
| `MODULE_PASS` | `globalsplit` | `globals-linkage` | 85 |
| `MODULE_PASS` | `hipstdpar-interpose-alloc` | `parallel-runtime` | 86 |
| `MODULE_PASS` | `hipstdpar-select-accelerator-code` | `parallel-runtime` | 87 |
| `MODULE_PASS` | `hotcoldsplit` | `inline-outline` | 89 |
| `MODULE_PASS` | `inferattrs` | `attribute-inference` | 90 |
| `MODULE_PASS` | `inliner-ml-advisor-release` | `inline-outline` | 91 |
| `MODULE_PASS` | `inliner-wrapper` | `inline-outline` | 94 |
| `MODULE_PASS` | `inliner-wrapper-no-mandatory-first` | `inline-outline` | 95 |
| `MODULE_PASS` | `insert-gcov-profiling` | `instrumentation` | 97 |
| `MODULE_PASS` | `instrprof` | `instrumentation` | 98 |
| `MODULE_PASS` | `ctx-instr-lower` | `instrumentation` | 99 |
| `MODULE_PASS` | `print<ctx-prof-analysis>` | `diagnostic-tools` | 100 |
| `MODULE_PASS` | `invalidate<all>` | `analysis-maintenance` | 101 |
| `MODULE_PASS` | `iroutliner` | `inline-outline` | 102 |
| `MODULE_PASS` | `jmc-instrumenter` | `security-instrumentation` | 103 |
| `MODULE_PASS` | `lower-emutls` | `runtime-lowering` | 104 |
| `MODULE_PASS` | `lower-global-dtors` | `runtime-lowering` | 105 |
| `MODULE_PASS` | `lower-ifunc` | `globals-linkage` | 106 |
| `MODULE_PASS` | `simplify-type-tests` | `globals-linkage` | 107 |
| `MODULE_PASS` | `lowertypetests` | `globals-linkage` | 108 |
| `MODULE_PASS` | `fatlto-cleanup` | `globals-linkage` | 109 |
| `MODULE_PASS` | `pgo-force-function-attrs` | `attribute-inference` | 110 |
| `MODULE_PASS` | `memprof-context-disambiguation` | `instrumentation` | 114 |
| `MODULE_PASS` | `memprof-module` | `instrumentation` | 115 |
| `MODULE_PASS` | `mergefunc` | `globals-linkage` | 116 |
| `MODULE_PASS` | `metarenamer` | `metadata-debug` | 117 |
| `MODULE_PASS` | `module-inline` | `inline-outline` | 118 |
| `MODULE_PASS` | `name-anon-globals` | `metadata-debug` | 119 |
| `MODULE_PASS` | `no-op-module` | `diagnostic-tools` | 120 |
| `MODULE_PASS` | `nsan` | `instrumentation` | 121 |
| `MODULE_PASS` | `objc-arc-apelim` | `objc-runtime` | 122 |
| `MODULE_PASS` | `openmp-opt` | `parallel-runtime` | 123 |
| `MODULE_PASS` | `openmp-opt-postlink` | `parallel-runtime` | 124 |
| `MODULE_PASS` | `partial-inliner` | `inline-outline` | 126 |
| `MODULE_PASS` | `pgo-icall-prom` | `call-and-tail` | 127 |
| `MODULE_PASS` | `pgo-instr-gen` | `instrumentation` | 128 |
| `MODULE_PASS` | `pgo-instr-use` | `instrumentation` | 129 |
| `MODULE_PASS` | `pre-isel-intrinsic-lowering` | `runtime-lowering` | 130 |
| `MODULE_PASS` | `print` | `diagnostic-tools` | 131 |
| `MODULE_PASS` | `print-callgraph` | `diagnostic-tools` | 132 |
| `MODULE_PASS` | `print-callgraph-sccs` | `diagnostic-tools` | 133 |
| `MODULE_PASS` | `print-ir-similarity` | `diagnostic-tools` | 134 |
| `MODULE_PASS` | `print-lcg` | `diagnostic-tools` | 135 |
| `MODULE_PASS` | `print-lcg-dot` | `diagnostic-tools` | 136 |
| `MODULE_PASS` | `print-must-be-executed-contexts` | `diagnostic-tools` | 137 |
| `MODULE_PASS` | `print-profile-summary` | `diagnostic-tools` | 139 |
| `MODULE_PASS` | `print-stack-safety` | `diagnostic-tools` | 140 |
| `MODULE_PASS` | `print<dxil-metadata>` | `diagnostic-tools` | 141 |
| `MODULE_PASS` | `print<dxil-resources>` | `diagnostic-tools` | 142 |
| `MODULE_PASS` | `print<inline-advisor>` | `diagnostic-tools` | 143 |
| `MODULE_PASS` | `print<ir2vec>` | `diagnostic-tools` | 144 |
| `MODULE_PASS` | `print<ir2vec-vocab>` | `diagnostic-tools` | 145 |
| `MODULE_PASS` | `print<module-debuginfo>` | `diagnostic-tools` | 146 |
| `MODULE_PASS` | `print<reg-usage>` | `diagnostic-tools` | 147 |
| `MODULE_PASS` | `pseudo-probe` | `instrumentation` | 148 |
| `MODULE_PASS` | `pseudo-probe-update` | `instrumentation` | 149 |
| `MODULE_PASS` | `recompute-globalsaa` | `analysis-maintenance` | 150 |
| `MODULE_PASS` | `rel-lookup-table-converter` | `globals-linkage` | 151 |
| `MODULE_PASS` | `rewrite-statepoints-for-gc` | `gc-runtime` | 152 |
| `MODULE_PASS` | `rewrite-symbols` | `globals-linkage` | 153 |
| `MODULE_PASS` | `rpo-function-attrs` | `attribute-inference` | 154 |
| `MODULE_PASS` | `rtsan` | `instrumentation` | 155 |
| `MODULE_PASS` | `sample-profile` | `instrumentation` | 156 |
| `MODULE_PASS` | `sancov-module` | `instrumentation` | 157 |
| `MODULE_PASS` | `sanmd-module` | `instrumentation` | 158 |
| `MODULE_PASS` | `scc-oz-module-inliner` | `inline-outline` | 159 |
| `MODULE_PASS` | `shadow-stack-gc-lowering` | `gc-runtime` | 162 |
| `MODULE_PASS` | `strip` | `metadata-debug` | 163 |
| `MODULE_PASS` | `strip-dead-debug-info` | `metadata-debug` | 164 |
| `MODULE_PASS` | `strip-dead-prototypes` | `metadata-debug` | 165 |
| `MODULE_PASS` | `strip-debug-declare` | `metadata-debug` | 166 |
| `MODULE_PASS` | `strip-nondebug` | `metadata-debug` | 167 |
| `MODULE_PASS` | `strip-nonlinetable-debuginfo` | `metadata-debug` | 168 |
| `MODULE_PASS` | `strip-dead-cg-profile` | `metadata-debug` | 169 |
| `MODULE_PASS` | `trigger-crash-module` | `diagnostic-tools` | 170 |
| `MODULE_PASS` | `trigger-verifier-error` | `diagnostic-tools` | 171 |
| `MODULE_PASS` | `tsan-module` | `instrumentation` | 172 |
| `MODULE_PASS` | `tysan` | `instrumentation` | 173 |
| `MODULE_PASS` | `verify` | `diagnostic-tools` | 174 |
| `MODULE_PASS` | `view-callgraph` | `diagnostic-tools` | 175 |
| `MODULE_PASS` | `wholeprogramdevirt` | `globals-linkage` | 176 |
| `MODULE_PASS_WITH_PARAMS` | `asan` | `instrumentation` | 182 |
| `MODULE_PASS_WITH_PARAMS` | `cg-profile` | `instrumentation` | 186 |
| `MODULE_PASS_WITH_PARAMS` | `global-merge` | `globals-linkage` | 190 |
| `MODULE_PASS_WITH_PARAMS` | `embed-bitcode` | `metadata-debug` | 198 |
| `MODULE_PASS_WITH_PARAMS` | `globaldce` | `globals-linkage` | 202 |
| `MODULE_PASS_WITH_PARAMS` | `hwasan` | `instrumentation` | 206 |
| `MODULE_PASS_WITH_PARAMS` | `internalize` | `globals-linkage` | 210 |
| `MODULE_PASS_WITH_PARAMS` | `ipsccp` | `constant-range-propagation` | 224 |
| `MODULE_PASS_WITH_PARAMS` | `loop-extract` | `inline-outline` | 227 |
| `MODULE_PASS_WITH_PARAMS` | `memprof-use` | `instrumentation` | 235 |
| `MODULE_PASS_WITH_PARAMS` | `msan` | `instrumentation` | 239 |
| `MODULE_PASS_WITH_PARAMS` | `print<structural-hash>` | `diagnostic-tools` | 243 |
| `MODULE_PASS_WITH_PARAMS` | `default` | `pipeline` | 250 |
| `MODULE_PASS_WITH_PARAMS` | `thinlto-pre-link` | `pipeline` | 256 |
| `MODULE_PASS_WITH_PARAMS` | `thinlto` | `pipeline` | 262 |
| `MODULE_PASS_WITH_PARAMS` | `lto-pre-link` | `pipeline` | 268 |
| `MODULE_PASS_WITH_PARAMS` | `lto` | `pipeline` | 280 |
| `MODULE_PASS_WITH_PARAMS` | `fatlto-pre-link` | `pipeline` | 286 |
| `CGSCC_PASS` | `argpromotion` | `storage-representation` | 307 |
| `CGSCC_PASS` | `attributor-cgscc` | `attribute-inference` | 308 |
| `CGSCC_PASS` | `attributor-light-cgscc` | `attribute-inference` | 309 |
| `CGSCC_PASS` | `invalidate<all>` | `analysis-maintenance` | 310 |
| `CGSCC_PASS` | `no-op-cgscc` | `diagnostic-tools` | 311 |
| `CGSCC_PASS` | `openmp-opt-cgscc` | `parallel-runtime` | 312 |
| `CGSCC_PASS` | `coro-annotation-elide` | `coroutine-lowering` | 313 |
| `CGSCC_PASS_WITH_PARAMS` | `coro-split` | `coroutine-lowering` | 319 |
| `CGSCC_PASS_WITH_PARAMS` | `function-attrs` | `attribute-inference` | 323 |
| `CGSCC_PASS_WITH_PARAMS` | `inline` | `inline-outline` | 329 |
| `FUNCTION_PASS` | `aa-eval` | `diagnostic-tools` | 395 |
| `FUNCTION_PASS` | `adce` | `dead-code` | 396 |
| `FUNCTION_PASS` | `add-discriminators` | `metadata-debug` | 397 |
| `FUNCTION_PASS` | `aggressive-instcombine` | `scalar-algebra` | 398 |
| `FUNCTION_PASS` | `alignment-from-assumptions` | `constant-range-propagation` | 399 |
| `FUNCTION_PASS` | `annotation-remarks` | `diagnostic-tools` | 400 |
| `FUNCTION_PASS` | `assume-builder` | `constant-range-propagation` | 401 |
| `FUNCTION_PASS` | `assume-simplify` | `constant-range-propagation` | 402 |
| `FUNCTION_PASS` | `atomic-expand` | `atomic-lowering` | 403 |
| `FUNCTION_PASS` | `bdce` | `dead-code` | 404 |
| `FUNCTION_PASS` | `break-crit-edges` | `cfg-rewrite` | 405 |
| `FUNCTION_PASS` | `callbr-prepare` | `exception-lowering` | 406 |
| `FUNCTION_PASS` | `callsite-splitting` | `cfg-rewrite` | 407 |
| `FUNCTION_PASS` | `chr` | `cfg-rewrite` | 408 |
| `FUNCTION_PASS` | `codegenprepare` | `runtime-lowering` | 409 |
| `FUNCTION_PASS` | `complex-deinterleaving` | `vector-transforms` | 410 |
| `FUNCTION_PASS` | `consthoist` | `prefetch-layout` | 411 |
| `FUNCTION_PASS` | `constraint-elimination` | `constant-range-propagation` | 412 |
| `FUNCTION_PASS` | `coro-elide` | `coroutine-lowering` | 413 |
| `FUNCTION_PASS` | `correlated-propagation` | `constant-range-propagation` | 414 |
| `FUNCTION_PASS` | `count-visits` | `instrumentation` | 415 |
| `FUNCTION_PASS` | `dce` | `dead-code` | 416 |
| `FUNCTION_PASS` | `declare-to-assign` | `metadata-debug` | 417 |
| `FUNCTION_PASS` | `dfa-jump-threading` | `cfg-rewrite` | 418 |
| `FUNCTION_PASS` | `div-rem-pairs` | `scalar-algebra` | 419 |
| `FUNCTION_PASS` | `dot-cfg` | `diagnostic-tools` | 420 |
| `FUNCTION_PASS` | `dot-cfg-only` | `diagnostic-tools` | 421 |
| `FUNCTION_PASS` | `dot-dom` | `diagnostic-tools` | 422 |
| `FUNCTION_PASS` | `dot-dom-only` | `diagnostic-tools` | 423 |
| `FUNCTION_PASS` | `dot-post-dom` | `diagnostic-tools` | 424 |
| `FUNCTION_PASS` | `dot-post-dom-only` | `diagnostic-tools` | 425 |
| `FUNCTION_PASS` | `dse` | `memory-opt` | 426 |
| `FUNCTION_PASS` | `dwarf-eh-prepare` | `exception-lowering` | 427 |
| `FUNCTION_PASS` | `expand-large-div-rem` | `runtime-lowering` | 428 |
| `FUNCTION_PASS` | `expand-fp` | `runtime-lowering` | 429 |
| `FUNCTION_PASS` | `expand-memcmp` | `runtime-lowering` | 430 |
| `FUNCTION_PASS` | `expand-reductions` | `vector-transforms` | 431 |
| `FUNCTION_PASS` | `extra-vector-passes` | `pipeline` | 432 |
| `FUNCTION_PASS` | `fix-irreducible` | `cfg-rewrite` | 434 |
| `FUNCTION_PASS` | `flatten-cfg` | `cfg-rewrite` | 435 |
| `FUNCTION_PASS` | `float2int` | `fp-and-libcalls` | 436 |
| `FUNCTION_PASS` | `gc-lowering` | `gc-runtime` | 437 |
| `FUNCTION_PASS` | `guard-widening` | `guard-deopt` | 438 |
| `FUNCTION_PASS` | `gvn-hoist` | `value-numbering` | 439 |
| `FUNCTION_PASS` | `gvn-sink` | `value-numbering` | 440 |
| `FUNCTION_PASS` | `helloworld` | `diagnostic-tools` | 441 |
| `FUNCTION_PASS` | `indirectbr-expand` | `cfg-rewrite` | 442 |
| `FUNCTION_PASS` | `infer-address-spaces` | `constant-range-propagation` | 443 |
| `FUNCTION_PASS` | `infer-alignment` | `constant-range-propagation` | 444 |
| `FUNCTION_PASS` | `inject-tli-mappings` | `fp-and-libcalls` | 445 |
| `FUNCTION_PASS` | `instcount` | `diagnostic-tools` | 446 |
| `FUNCTION_PASS` | `instnamer` | `metadata-debug` | 447 |
| `FUNCTION_PASS` | `instsimplify` | `scalar-algebra` | 448 |
| `FUNCTION_PASS` | `interleaved-access` | `vector-transforms` | 449 |
| `FUNCTION_PASS` | `interleaved-load-combine` | `memory-opt` | 450 |
| `FUNCTION_PASS` | `invalidate<all>` | `analysis-maintenance` | 451 |
| `FUNCTION_PASS` | `irce` | `constant-range-propagation` | 452 |
| `FUNCTION_PASS` | `jump-threading` | `cfg-rewrite` | 453 |
| `FUNCTION_PASS` | `jump-table-to-switch` | `cfg-rewrite` | 454 |
| `FUNCTION_PASS` | `kcfi` | `security-instrumentation` | 455 |
| `FUNCTION_PASS` | `kernel-info` | `target-extension` | 456 |
| `FUNCTION_PASS` | `lcssa` | `loop-structure` | 457 |
| `FUNCTION_PASS` | `libcalls-shrinkwrap` | `fp-and-libcalls` | 458 |
| `FUNCTION_PASS` | `load-store-vectorizer` | `vector-transforms` | 459 |
| `FUNCTION_PASS` | `loop-data-prefetch` | `prefetch-layout` | 460 |
| `FUNCTION_PASS` | `loop-distribute` | `loop-event-rewrite` | 461 |
| `FUNCTION_PASS` | `loop-fusion` | `loop-event-rewrite` | 462 |
| `FUNCTION_PASS` | `loop-load-elim` | `memory-opt` | 463 |
| `FUNCTION_PASS` | `loop-simplify` | `loop-structure` | 464 |
| `FUNCTION_PASS` | `loop-sink` | `loop-motion` | 465 |
| `FUNCTION_PASS` | `loop-versioning` | `loop-event-rewrite` | 466 |
| `FUNCTION_PASS` | `lower-atomic` | `atomic-lowering` | 467 |
| `FUNCTION_PASS` | `lower-constant-intrinsics` | `constant-range-propagation` | 468 |
| `FUNCTION_PASS` | `lower-expect` | `runtime-lowering` | 469 |
| `FUNCTION_PASS` | `lower-guard-intrinsic` | `guard-deopt` | 470 |
| `FUNCTION_PASS` | `lower-invoke` | `exception-lowering` | 471 |
| `FUNCTION_PASS` | `lower-switch` | `cfg-rewrite` | 472 |
| `FUNCTION_PASS` | `lower-widenable-condition` | `guard-deopt` | 473 |
| `FUNCTION_PASS` | `make-guards-explicit` | `guard-deopt` | 474 |
| `FUNCTION_PASS` | `mem2reg` | `storage-representation` | 475 |
| `FUNCTION_PASS` | `memcpyopt` | `memory-opt` | 476 |
| `FUNCTION_PASS` | `memprof` | `instrumentation` | 477 |
| `FUNCTION_PASS` | `mergeicmps` | `cfg-rewrite` | 478 |
| `FUNCTION_PASS` | `mergereturn` | `cfg-rewrite` | 479 |
| `FUNCTION_PASS` | `move-auto-init` | `memory-opt` | 480 |
| `FUNCTION_PASS` | `nary-reassociate` | `scalar-algebra` | 481 |
| `FUNCTION_PASS` | `newgvn` | `value-numbering` | 482 |
| `FUNCTION_PASS` | `no-op-function` | `diagnostic-tools` | 483 |
| `FUNCTION_PASS` | `objc-arc` | `objc-runtime` | 484 |
| `FUNCTION_PASS` | `objc-arc-contract` | `objc-runtime` | 485 |
| `FUNCTION_PASS` | `objc-arc-expand` | `objc-runtime` | 486 |
| `FUNCTION_PASS` | `pa-eval` | `diagnostic-tools` | 487 |
| `FUNCTION_PASS` | `partially-inline-libcalls` | `fp-and-libcalls` | 488 |
| `FUNCTION_PASS` | `pgo-memop-opt` | `instrumentation` | 489 |
| `FUNCTION_PASS` | `place-safepoints` | `gc-runtime` | 490 |
| `FUNCTION_PASS` | `print` | `diagnostic-tools` | 491 |
| `FUNCTION_PASS` | `print-alias-sets` | `diagnostic-tools` | 493 |
| `FUNCTION_PASS` | `print-cfg-sccs` | `diagnostic-tools` | 494 |
| `FUNCTION_PASS` | `print-memderefs` | `diagnostic-tools` | 495 |
| `FUNCTION_PASS` | `print-mustexecute` | `diagnostic-tools` | 496 |
| `FUNCTION_PASS` | `print-predicateinfo` | `diagnostic-tools` | 497 |
| `FUNCTION_PASS` | `print<assumptions>` | `diagnostic-tools` | 498 |
| `FUNCTION_PASS` | `print<block-freq>` | `diagnostic-tools` | 499 |
| `FUNCTION_PASS` | `print<branch-prob>` | `diagnostic-tools` | 500 |
| `FUNCTION_PASS` | `print<cost-model>` | `diagnostic-tools` | 501 |
| `FUNCTION_PASS` | `print<cycles>` | `diagnostic-tools` | 502 |
| `FUNCTION_PASS` | `print<da>` | `diagnostic-tools` | 503 |
| `FUNCTION_PASS` | `print<debug-ata>` | `diagnostic-tools` | 504 |
| `FUNCTION_PASS` | `print<delinearization>` | `diagnostic-tools` | 505 |
| `FUNCTION_PASS` | `print<demanded-bits>` | `diagnostic-tools` | 506 |
| `FUNCTION_PASS` | `print<domfrontier>` | `diagnostic-tools` | 507 |
| `FUNCTION_PASS` | `print<domtree>` | `diagnostic-tools` | 508 |
| `FUNCTION_PASS` | `print<func-properties>` | `diagnostic-tools` | 509 |
| `FUNCTION_PASS` | `print<inline-cost>` | `diagnostic-tools` | 510 |
| `FUNCTION_PASS` | `print<inliner-size-estimator>` | `diagnostic-tools` | 511 |
| `FUNCTION_PASS` | `print<lazy-value-info>` | `diagnostic-tools` | 513 |
| `FUNCTION_PASS` | `print<loops>` | `diagnostic-tools` | 514 |
| `FUNCTION_PASS` | `print<memoryssa-walker>` | `diagnostic-tools` | 515 |
| `FUNCTION_PASS` | `print<phi-values>` | `diagnostic-tools` | 516 |
| `FUNCTION_PASS` | `print<postdomtree>` | `diagnostic-tools` | 517 |
| `FUNCTION_PASS` | `print<regions>` | `diagnostic-tools` | 518 |
| `FUNCTION_PASS` | `print<scalar-evolution>` | `diagnostic-tools` | 519 |
| `FUNCTION_PASS` | `print<stack-safety-local>` | `diagnostic-tools` | 520 |
| `FUNCTION_PASS` | `print<uniformity>` | `diagnostic-tools` | 521 |
| `FUNCTION_PASS` | `reassociate` | `scalar-algebra` | 522 |
| `FUNCTION_PASS` | `redundant-dbg-inst-elim` | `metadata-debug` | 523 |
| `FUNCTION_PASS` | `replace-with-veclib` | `fp-and-libcalls` | 524 |
| `FUNCTION_PASS` | `reg2mem` | `storage-representation` | 525 |
| `FUNCTION_PASS` | `safe-stack` | `security-instrumentation` | 526 |
| `FUNCTION_PASS` | `sandbox-vectorizer` | `vector-transforms` | 527 |
| `FUNCTION_PASS` | `scalarize-masked-mem-intrin` | `vector-transforms` | 528 |
| `FUNCTION_PASS` | `sccp` | `constant-range-propagation` | 529 |
| `FUNCTION_PASS` | `select-optimize` | `cfg-rewrite` | 530 |
| `FUNCTION_PASS` | `separate-const-offset-from-gep` | `loop-induction` | 531 |
| `FUNCTION_PASS` | `sink` | `loop-motion` | 533 |
| `FUNCTION_PASS` | `sjlj-eh-prepare` | `exception-lowering` | 534 |
| `FUNCTION_PASS` | `slp-vectorizer` | `vector-transforms` | 535 |
| `FUNCTION_PASS` | `slsr` | `scalar-algebra` | 536 |
| `FUNCTION_PASS` | `stack-protector` | `security-instrumentation` | 537 |
| `FUNCTION_PASS` | `strip-gc-relocates` | `gc-runtime` | 538 |
| `FUNCTION_PASS` | `tailcallelim` | `call-and-tail` | 539 |
| `FUNCTION_PASS` | `transform-warning` | `diagnostic-tools` | 540 |
| `FUNCTION_PASS` | `trigger-crash-function` | `diagnostic-tools` | 541 |
| `FUNCTION_PASS` | `trigger-verifier-error` | `diagnostic-tools` | 542 |
| `FUNCTION_PASS` | `tsan` | `instrumentation` | 543 |
| `FUNCTION_PASS` | `typepromotion` | `scalar-algebra` | 544 |
| `FUNCTION_PASS` | `unify-loop-exits` | `cfg-rewrite` | 545 |
| `FUNCTION_PASS` | `unreachableblockelim` | `cfg-rewrite` | 546 |
| `FUNCTION_PASS` | `vector-combine` | `vector-transforms` | 547 |
| `FUNCTION_PASS` | `verify` | `diagnostic-tools` | 548 |
| `FUNCTION_PASS` | `verify<cycles>` | `diagnostic-tools` | 549 |
| `FUNCTION_PASS` | `verify<domtree>` | `diagnostic-tools` | 550 |
| `FUNCTION_PASS` | `verify<loops>` | `diagnostic-tools` | 551 |
| `FUNCTION_PASS` | `verify<memoryssa>` | `diagnostic-tools` | 552 |
| `FUNCTION_PASS` | `verify<regions>` | `diagnostic-tools` | 553 |
| `FUNCTION_PASS` | `verify<safepoint-ir>` | `diagnostic-tools` | 554 |
| `FUNCTION_PASS` | `verify<scalar-evolution>` | `diagnostic-tools` | 555 |
| `FUNCTION_PASS` | `view-cfg` | `diagnostic-tools` | 556 |
| `FUNCTION_PASS` | `view-cfg-only` | `diagnostic-tools` | 557 |
| `FUNCTION_PASS` | `view-dom` | `diagnostic-tools` | 558 |
| `FUNCTION_PASS` | `view-dom-only` | `diagnostic-tools` | 559 |
| `FUNCTION_PASS` | `view-post-dom` | `diagnostic-tools` | 560 |
| `FUNCTION_PASS` | `view-post-dom-only` | `diagnostic-tools` | 561 |
| `FUNCTION_PASS` | `wasm-eh-prepare` | `exception-lowering` | 562 |
| `FUNCTION_PASS_WITH_PARAMS` | `cfguard` | `security-instrumentation` | 568 |
| `FUNCTION_PASS_WITH_PARAMS` | `early-cse` | `value-numbering` | 572 |
| `FUNCTION_PASS_WITH_PARAMS` | `ee-instrument` | `instrumentation` | 576 |
| `FUNCTION_PASS_WITH_PARAMS` | `function-simplification` | `pipeline` | 580 |
| `FUNCTION_PASS_WITH_PARAMS` | `gvn` | `value-numbering` | 586 |
| `FUNCTION_PASS_WITH_PARAMS` | `hardware-loops` | `runtime-lowering` | 591 |
| `FUNCTION_PASS_WITH_PARAMS` | `instcombine` | `scalar-algebra` | 598 |
| `FUNCTION_PASS_WITH_PARAMS` | `lint` | `diagnostic-tools` | 603 |
| `FUNCTION_PASS_WITH_PARAMS` | `loop-unroll` | `loop-event-rewrite` | 607 |
| `FUNCTION_PASS_WITH_PARAMS` | `loop-vectorize` | `vector-transforms` | 614 |
| `FUNCTION_PASS_WITH_PARAMS` | `lower-allow-check` | `guard-deopt` | 620 |
| `FUNCTION_PASS_WITH_PARAMS` | `lower-matrix-intrinsics` | `runtime-lowering` | 624 |
| `FUNCTION_PASS_WITH_PARAMS` | `normalize` | `cfg-rewrite` | 628 |
| `FUNCTION_PASS_WITH_PARAMS` | `mldst-motion` | `memory-opt` | 634 |
| `FUNCTION_PASS_WITH_PARAMS` | `print<access-info>` | `diagnostic-tools` | 640 |
| `FUNCTION_PASS_WITH_PARAMS` | `print<da>` | `diagnostic-tools` | 650 |
| `FUNCTION_PASS_WITH_PARAMS` | `print<memoryssa>` | `diagnostic-tools` | 656 |
| `FUNCTION_PASS_WITH_PARAMS` | `print<stack-lifetime>` | `diagnostic-tools` | 662 |
| `FUNCTION_PASS_WITH_PARAMS` | `scalarizer` | `vector-transforms` | 668 |
| `FUNCTION_PASS_WITH_PARAMS` | `separate-const-offset-from-gep` | `loop-induction` | 674 |
| `FUNCTION_PASS_WITH_PARAMS` | `simplifycfg` | `cfg-rewrite` | 678 |
| `FUNCTION_PASS_WITH_PARAMS` | `speculative-execution` | `loop-motion` | 690 |
| `FUNCTION_PASS_WITH_PARAMS` | `sroa` | `storage-representation` | 696 |
| `FUNCTION_PASS_WITH_PARAMS` | `structurizecfg` | `cfg-rewrite` | 700 |
| `FUNCTION_PASS_WITH_PARAMS` | `win-eh-prepare` | `exception-lowering` | 706 |
| `FUNCTION_PASS_WITH_PARAMS` | `bounds-checking` | `security-instrumentation` | 712 |
| `LOOPNEST_PASS` | `loop-flatten` | `loop-event-rewrite` | 724 |
| `LOOPNEST_PASS` | `loop-interchange` | `loop-event-rewrite` | 725 |
| `LOOPNEST_PASS` | `loop-unroll-and-jam` | `loop-event-rewrite` | 726 |
| `LOOPNEST_PASS` | `no-op-loopnest` | `diagnostic-tools` | 727 |
| `LOOP_PASS` | `canon-freeze` | `scalar-algebra` | 745 |
| `LOOP_PASS` | `dot-ddg` | `diagnostic-tools` | 746 |
| `LOOP_PASS` | `evl-iv-simplify` | `loop-induction` | 747 |
| `LOOP_PASS` | `guard-widening` | `guard-deopt` | 748 |
| `LOOP_PASS` | `extra-simple-loop-unswitch-passes` | `pipeline` | 749 |
| `LOOP_PASS` | `indvars` | `loop-induction` | 751 |
| `LOOP_PASS` | `invalidate<all>` | `analysis-maintenance` | 752 |
| `LOOP_PASS` | `loop-bound-split` | `loop-event-rewrite` | 753 |
| `LOOP_PASS` | `loop-deletion` | `dead-code` | 754 |
| `LOOP_PASS` | `loop-idiom` | `loop-idioms` | 755 |
| `LOOP_PASS` | `loop-idiom-vectorize` | `loop-idioms` | 756 |
| `LOOP_PASS` | `loop-instsimplify` | `scalar-algebra` | 757 |
| `LOOP_PASS` | `loop-predication` | `guard-deopt` | 758 |
| `LOOP_PASS` | `loop-reduce` | `loop-induction` | 759 |
| `LOOP_PASS` | `loop-term-fold` | `cfg-rewrite` | 760 |
| `LOOP_PASS` | `loop-simplifycfg` | `cfg-rewrite` | 761 |
| `LOOP_PASS` | `loop-unroll-full` | `loop-event-rewrite` | 762 |
| `LOOP_PASS` | `loop-versioning-licm` | `loop-motion` | 763 |
| `LOOP_PASS` | `no-op-loop` | `diagnostic-tools` | 764 |
| `LOOP_PASS` | `print` | `diagnostic-tools` | 765 |
| `LOOP_PASS` | `print<ddg>` | `diagnostic-tools` | 766 |
| `LOOP_PASS` | `print<hash-recognize>` | `diagnostic-tools` | 767 |
| `LOOP_PASS` | `print<iv-users>` | `diagnostic-tools` | 768 |
| `LOOP_PASS` | `print<loop-cache-cost>` | `diagnostic-tools` | 769 |
| `LOOP_PASS` | `print<loopnest>` | `diagnostic-tools` | 770 |
| `LOOP_PASS_WITH_PARAMS` | `licm` | `loop-motion` | 776 |
| `LOOP_PASS_WITH_PARAMS` | `lnicm` | `loop-motion` | 779 |
| `LOOP_PASS_WITH_PARAMS` | `loop-rotate` | `loop-structure` | 782 |
| `LOOP_PASS_WITH_PARAMS` | `simple-loop-unswitch` | `loop-event-rewrite` | 790 |
