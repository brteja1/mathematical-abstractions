# Asymmetric coroutine with explicit resume/yield lifecycle

A resumable computation retains a continuation, receives input from a fixed direct caller, and returns control to that caller by yielding, returning or failing. A small-step lifecycle distinguishes suspended and running execution.

**Notation:** C=(K,I,O,R,E,k₀,accept,τ,Y,Ret,Err); S=Created(K)+Suspended(K)+Running(K)+Returned(R)+Failed(E)

**Stable ID:** `urn:csabs:concept/AsymmetricCoroutine`

**Categories:** Programming-language semantics → Coroutines and cooperative execution, Concurrency and distributed systems → Behavioral models

**Kind:** semantic-model

**Prerequisites:** [Action-labelled transition system with initial states](LabelledTransitionSystem.md), [Partial function](PartialFunction.md)

**Specializes:** [Action-labelled transition system with initial states](LabelledTransitionSystem.md)

**Related concepts:** [Single-thread cooperative scheduler with explicit waiting](CooperativeScheduler.md), [Finite fused sequence iterator](FiniteIterator.md)

## Backlinks

- [Single-thread cooperative scheduler with explicit waiting](CooperativeScheduler.md) — `relatedConcept`
- [Single-thread cooperative scheduler with explicit waiting](CooperativeScheduler.md) — `requiresConcept`

## Mathematical formulation

Created(k) or Suspended(k) —Resume(i)→ Running(accept(k,i)); Running(k) —Internal→ Running(k′) iff τ(k,k′); —Yield(o)→ Suspended(k′) iff Y(k,o,k′); —Return(r)→ Returned(r) iff Ret(k,r); —Raise(e)→ Failed(e) iff Err(k,e). No other steps. Initial state is Created(k₀).

**Lean formulation** (in its source module context):

```lean
structure AsymmetricCoroutine (K I O R E : Type u) where
  entry : K
  accept : K → I → K
  internal : K → K → Prop
  yields : K → O → K → Prop
  returns : K → R → Prop
  raises : K → E → Prop
```

**Source:** [`Catalog.AsymmetricCoroutine`](../lean/Catalog/Coroutines.lean); consulted 2026-11-14.

**Scope:** model

**Interpretation:** K,I,O,R,E are Lean types; CoroutineState is the tagged lifecycle carrier. entry selects the created state, accept injects resume input, and internal/yields/returns/raises are body relations. coroutineStep gives exactly the six lifecycle rules; coroutineLTS exposes the singleton initial state; coroutineOutcomes observes a resume, finite internal closure and one boundary event. Equality is Lean structural equality.

**Limits:** Body semantics and retained heap/stack contents must be supplied by the instantiation. No language frontend, nested caller stack, shared-memory interference, cancellation, throw/close, fairness, divergence classification or complete runtime conformance is encoded. Only the separately registered successive-resumes-require-yield theorem has a compiled claim witness when verification evidence is fresh. Other graph claims and runtime correspondence remain separate obligations.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** The complete step relation consists only of the resume, internal, yield, return and failure rules below. Creation does not execute the body. A resume outcome is a finite internal segment followed by one handoff boundary; existence of such an outcome is not assumed.

**basisKind:** defined-operational-semantics

**basisScope:** One coroutine and its fixed direct caller; no nested coroutine-to-coroutine resume, external mutation, preemption, cancellation, close, exception injection or stack-unwinding semantics. K stores all local control/data state; I,O,R,E are input, yielded, return and uncaught-error carriers with structural equality, allowed to be empty except the chosen entry k₀∈K. Created, Suspended, Running, Returned and Failed are disjoint tags. Internal steps may be nondeterministic, deadlock or diverge. All labels remain observable, including internal; hiding is a separate model. Resume accepts an input in both Created and Suspended, following the Lua-style initial-argument convention; Python generator priming needs an adapter. Invalid actions have no successor rather than an implicit runtime exception.

**specializationNote:** Instantiate the parent with state sum S, labels Resume(i), Internal, Yield(o), Return(r), Raise(e), singleton initial state Created(k₀), and exactly the recorded step rules. The parent finite traces retain internal labels. No parent claims are inherited.

**verificationObligation:** One coroutine and its fixed direct caller; no nested coroutine-to-coroutine resume, external mutation, preemption, cancellation, close, exception injection or stack-unwinding semantics. K stores all local control/data state; I,O,R,E are input, yielded, return and uncaught-error carriers with structural equality, allowed to be empty except the chosen entry k₀∈K. Created, Suspended, Running, Returned and Failed are disjoint tags. Internal steps may be nondeterministic, deadlock or diverge. All labels remain observable, including internal; hiding is a separate model. Resume accepts an input in both Created and Suspended, following the Lua-style initial-argument convention; Python generator priming needs an adapter. Invalid actions have no successor rather than an implicit runtime exception.; Instantiate carriers, structural equality, state granularity and all external effects before applying this model. No fairness or progress guarantee follows from structural validation or the Lean interface.

**reviewStatus:** Editorial source/interface review; Lean model binding is separate from claim proof evidence.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-AsymmetricCoroutine-create"></a>

### create

`urn:csabs:operation/AsymmetricCoroutine-create`

**signature:** create : C→S

**description:** Create a dormant coroutine at its entry continuation.

**precondition:** A body model C with k₀∈K is supplied.

**totality:** Total mathematical constructor; no body code executes.

**postcondition:** create(C)=Created(k₀).

**source:** [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Python 3.13 language reference: yield expressions and generator-iterator methods](https://docs.python.org/3.13/reference/expressions.html#yield-expressions); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard

**sourceNote:** Adapts the consulted resume/yield lifecycle to typed carriers and an explicit internal-step relation. Selects a fixed direct caller and Lua-style input on first resume. Leaves cleanup, nested caller stacks and Python-specific invalid-call exceptions outside scope.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-AsymmetricCoroutine-step"></a>

### step

`urn:csabs:operation/AsymmetricCoroutine-step`

**signature:** step_C : S×Action→𝒫(S)

**description:** Allowed one-step lifecycle successors.

**precondition:** State and action use the selected typed carriers.

**totality:** Total set-valued relation image; disabled actions yield ∅. Not an executable decision procedure.

**postcondition:** step_C(s,a)={t | s —a→ t} using only the recorded lifecycle rules.

**source:** [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Python 3.13 language reference: yield expressions and generator-iterator methods](https://docs.python.org/3.13/reference/expressions.html#yield-expressions); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard

**sourceNote:** Adapts the consulted resume/yield lifecycle to typed carriers and an explicit internal-step relation. Selects a fixed direct caller and Lua-style input on first resume. Leaves cleanup, nested caller stacks and Python-specific invalid-call exceptions outside scope.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-AsymmetricCoroutine-resume-outcomes"></a>

### resumeOutcomes

`urn:csabs:operation/AsymmetricCoroutine-resume-outcomes`

**signature:** out_C : S×I→𝒫(Boundary×S)

**description:** All finite observations of a resume up to its first yield, return or uncaught failure.

**precondition:** The state may be arbitrary; successful resume is possible only from Created or Suspended. Boundary={Yield(o),Return(r),Raise(e)}.

**totality:** Total set-valued specification. Empty outcomes may mean invalid resume, deadlock or absence of a finite boundary; it does not imply runtime termination.

**postcondition:** (a,t)∈out_C(s,i) iff ∃k,k′: s —Resume(i)→ Running(k) ∧ τ*(k,k′) ∧ Running(k′) —a→ t ∧ a∈Boundary.

**source:** [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Python 3.13 language reference: yield expressions and generator-iterator methods](https://docs.python.org/3.13/reference/expressions.html#yield-expressions); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard

**sourceNote:** Adapts the consulted resume/yield lifecycle to typed carriers and an explicit internal-step relation. Selects a fixed direct caller and Lua-style input on first resume. Leaves cleanup, nested caller stacks and Python-specific invalid-call exceptions outside scope.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-AsymmetricCoroutine-resume-entry"></a>

### resume-entry

`urn:csabs:axiom/AsymmetricCoroutine-resume-entry`

**statement:** Creation is dormant and resume enters a created or suspended continuation with caller-supplied input.

**description:** Creation is dormant and resume enters a created or suspended continuation with caller-supplied input.

**formalStatement:** I₀={Created(k₀)}; Created(k) —Resume(i)→ Running(accept(k,i)); Suspended(k) —Resume(i)→ Running(accept(k,i)); these are the only Resume-labelled steps.

**assumptions:** One coroutine and its fixed direct caller; no nested coroutine-to-coroutine resume, external mutation, preemption, cancellation, close, exception injection or stack-unwinding semantics. K stores all local control/data state; I,O,R,E are input, yielded, return and uncaught-error carriers with structural equality, allowed to be empty except the chosen entry k₀∈K. Created, Suspended, Running, Returned and Failed are disjoint tags. Internal steps may be nondeterministic, deadlock or diverge. All labels remain observable, including internal; hiding is a separate model. Resume accepts an input in both Created and Suspended, following the Lua-style initial-argument convention; Python generator priming needs an adapter. Invalid actions have no successor rather than an implicit runtime exception.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** editorial defining rule; not a machine-checked claim

**source:** [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Python 3.13 language reference: yield expressions and generator-iterator methods](https://docs.python.org/3.13/reference/expressions.html#yield-expressions); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard

**sourceNote:** Adapts the consulted resume/yield lifecycle to typed carriers and an explicit internal-step relation. Selects a fixed direct caller and Lua-style input on first resume. Leaves cleanup, nested caller stacks and Python-specific invalid-call exceptions outside scope.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-AsymmetricCoroutine-body-handoff"></a>

### body-handoff

`urn:csabs:axiom/AsymmetricCoroutine-body-handoff`

**statement:** Only running bodies take internal steps or hand control back to the caller; boundary events distinguish yield, return and failure.

**description:** Only running bodies take internal steps or hand control back to the caller; boundary events distinguish yield, return and failure.

**formalStatement:** Running(k) —Internal→ Running(k′) ⇔ τ(k,k′); Running(k) —Yield(o)→ Suspended(k′) ⇔ Y(k,o,k′); Running(k) —Return(r)→ Returned(r′) ⇔ r′=r ∧ Ret(k,r); Running(k) —Raise(e)→ Failed(e′) ⇔ e′=e ∧ Err(k,e). Together with resume-entry these are all steps.

**assumptions:** One coroutine and its fixed direct caller; no nested coroutine-to-coroutine resume, external mutation, preemption, cancellation, close, exception injection or stack-unwinding semantics. K stores all local control/data state; I,O,R,E are input, yielded, return and uncaught-error carriers with structural equality, allowed to be empty except the chosen entry k₀∈K. Created, Suspended, Running, Returned and Failed are disjoint tags. Internal steps may be nondeterministic, deadlock or diverge. All labels remain observable, including internal; hiding is a separate model. Resume accepts an input in both Created and Suspended, following the Lua-style initial-argument convention; Python generator priming needs an adapter. Invalid actions have no successor rather than an implicit runtime exception.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** editorial defining rule; not a machine-checked claim

**source:** [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Python 3.13 language reference: yield expressions and generator-iterator methods](https://docs.python.org/3.13/reference/expressions.html#yield-expressions); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard

**sourceNote:** Adapts the consulted resume/yield lifecycle to typed carriers and an explicit internal-step relation. Selects a fixed direct caller and Lua-style input on first resume. Leaves cleanup, nested caller stacks and Python-specific invalid-call exceptions outside scope.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-AsymmetricCoroutine-finite-resume-observation"></a>

### finite-resume-observation

`urn:csabs:axiom/AsymmetricCoroutine-finite-resume-observation`

**statement:** A completed resume observation is exactly a resume followed by finitely many internal steps and one boundary handoff.

**description:** A completed resume observation is exactly a resume followed by finitely many internal steps and one boundary handoff.

**formalStatement:** (a,t)∈out_C(s,i) ⇔ a∈Boundary ∧ ∃k,k′:s —Resume(i)→ Running(k) ∧ τ*(k,k′) ∧ Running(k′) —a→ t; τ* is reflexive-transitive closure.

**assumptions:** One coroutine and its fixed direct caller; no nested coroutine-to-coroutine resume, external mutation, preemption, cancellation, close, exception injection or stack-unwinding semantics. K stores all local control/data state; I,O,R,E are input, yielded, return and uncaught-error carriers with structural equality, allowed to be empty except the chosen entry k₀∈K. Created, Suspended, Running, Returned and Failed are disjoint tags. Internal steps may be nondeterministic, deadlock or diverge. All labels remain observable, including internal; hiding is a separate model. Resume accepts an input in both Created and Suspended, following the Lua-style initial-argument convention; Python generator priming needs an adapter. Invalid actions have no successor rather than an implicit runtime exception.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** editorial defining rule; not a machine-checked claim

**source:** [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Python 3.13 language reference: yield expressions and generator-iterator methods](https://docs.python.org/3.13/reference/expressions.html#yield-expressions); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard

**sourceNote:** Adapts the consulted resume/yield lifecycle to typed carriers and an explicit internal-step relation. Selects a fixed direct caller and Lua-style input on first resume. Leaves cleanup, nested caller stacks and Python-specific invalid-call exceptions outside scope.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-AsymmetricCoroutine-terminal-no-successor"></a>

### terminal-no-successor

`urn:csabs:law/AsymmetricCoroutine-terminal-no-successor`

**statement:** Returned and failed states have no outgoing lifecycle step.

**description:** Returned and failed states have no outgoing lifecycle step.

**formalStatement:** ∀r,e,a: step_C(Returned(r),a)=∅ ∧ step_C(Failed(e),a)=∅

**assumptions:** One coroutine and its fixed direct caller; no nested coroutine-to-coroutine resume, external mutation, preemption, cancellation, close, exception injection or stack-unwinding semantics. K stores all local control/data state; I,O,R,E are input, yielded, return and uncaught-error carriers with structural equality, allowed to be empty except the chosen entry k₀∈K. Created, Suspended, Running, Returned and Failed are disjoint tags. Internal steps may be nondeterministic, deadlock or diverge. All labels remain observable, including internal; hiding is a separate model. Resume accepts an input in both Created and Suspended, following the Lua-style initial-argument convention; Python generator priming needs an adapter. Invalid actions have no successor rather than an implicit runtime exception.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** editorial derivation; not a registered machine-checked claim

**source:** [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Python 3.13 language reference: yield expressions and generator-iterator methods](https://docs.python.org/3.13/reference/expressions.html#yield-expressions); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard

**sourceNote:** Editorial consequence of the explicit premises in this chosen model; not a numbered source theorem. Every rule has Created, Suspended or Running as its source. Disjointness of state tags excludes Returned and Failed.

**provenanceKind:** derived

**dependsOn:** [resume-entry](AsymmetricCoroutine.md#node-urn-csabs-axiom-AsymmetricCoroutine-resume-entry); [body-handoff](AsymmetricCoroutine.md#node-urn-csabs-axiom-AsymmetricCoroutine-body-handoff)

**proofSketch:** Every rule has Created, Suspended or Running as its source. Disjointness of state tags excludes Returned and Failed.

<a id="node-urn-csabs-law-AsymmetricCoroutine-running-no-reentry"></a>

### running-no-reentry

`urn:csabs:law/AsymmetricCoroutine-running-no-reentry`

**statement:** A running coroutine cannot be resumed again within this protocol.

**description:** A running coroutine cannot be resumed again within this protocol.

**formalStatement:** ∀k,i: step_C(Running(k),Resume(i))=∅

**assumptions:** One coroutine and its fixed direct caller; no nested coroutine-to-coroutine resume, external mutation, preemption, cancellation, close, exception injection or stack-unwinding semantics. K stores all local control/data state; I,O,R,E are input, yielded, return and uncaught-error carriers with structural equality, allowed to be empty except the chosen entry k₀∈K. Created, Suspended, Running, Returned and Failed are disjoint tags. Internal steps may be nondeterministic, deadlock or diverge. All labels remain observable, including internal; hiding is a separate model. Resume accepts an input in both Created and Suspended, following the Lua-style initial-argument convention; Python generator priming needs an adapter. Invalid actions have no successor rather than an implicit runtime exception.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** editorial derivation; not a registered machine-checked claim

**source:** [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Python 3.13 language reference: yield expressions and generator-iterator methods](https://docs.python.org/3.13/reference/expressions.html#yield-expressions); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard

**sourceNote:** Editorial consequence of the explicit premises in this chosen model; not a numbered source theorem. Only Created and Suspended admit Resume. Running admits internal, yield, return or failure labels, which are disjoint from Resume.

**provenanceKind:** derived

**dependsOn:** [resume-entry](AsymmetricCoroutine.md#node-urn-csabs-axiom-AsymmetricCoroutine-resume-entry); [body-handoff](AsymmetricCoroutine.md#node-urn-csabs-axiom-AsymmetricCoroutine-body-handoff)

**proofSketch:** Only Created and Suspended admit Resume. Running admits internal, yield, return or failure labels, which are disjoint from Resume.

## Theorems

<a id="node-urn-csabs-theorem-AsymmetricCoroutine-successive-resumes-require-yield"></a>

### successive-resumes-require-yield

`urn:csabs:theorem/AsymmetricCoroutine-successive-resumes-require-yield`

**statement:** Any two successive resume actions along a legal finite execution have a yield handoff between them.

**description:** Any two successive resume actions along a legal finite execution have a yield handoff between them.

**formalStatement:** For a finite path from Created(k₀), consecutive occurrences of Resume in its label word have a Yield occurrence strictly between them.

**assumptions:** One coroutine and its fixed direct caller; no nested coroutine-to-coroutine resume, external mutation, preemption, cancellation, close, exception injection or stack-unwinding semantics. K stores all local control/data state; I,O,R,E are input, yielded, return and uncaught-error carriers with structural equality, allowed to be empty except the chosen entry k₀∈K. Created, Suspended, Running, Returned and Failed are disjoint tags. Internal steps may be nondeterministic, deadlock or diverge. All labels remain observable, including internal; hiding is a separate model. Resume accepts an input in both Created and Suspended, following the Lua-style initial-argument convention; Python generator priming needs an adapter. Invalid actions have no successor rather than an implicit runtime exception.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement with a separately mapped Lean witness; only fresh compiler and axiom-audit evidence establishes verification of the displayed Lean proposition.

**source:** [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Python 3.13 language reference: yield expressions and generator-iterator methods](https://docs.python.org/3.13/reference/expressions.html#yield-expressions); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard

**sourceNote:** Editorial consequence of the explicit premises in this chosen model; not a numbered source theorem. After the first Resume the phase is Running. Internal steps preserve it. To enable a later Resume the phase must become Created or Suspended. No rule re-creates a state; only Yield reaches Suspended. Return and Raise terminate all further steps. Induction over the intervening finite path establishes the claim.

**provenanceKind:** derived

**dependsOn:** [resume-entry](AsymmetricCoroutine.md#node-urn-csabs-axiom-AsymmetricCoroutine-resume-entry); [body-handoff](AsymmetricCoroutine.md#node-urn-csabs-axiom-AsymmetricCoroutine-body-handoff); [finite-paths](LabelledTransitionSystem.md#node-urn-csabs-axiom-LabelledTransitionSystem-finite-paths)

**proofSketch:** After the first Resume the phase is Running. Internal steps preserve it. To enable a later Resume the phase must become Created or Suspended. No rule re-creates a state; only Yield reaches Suspended. Return and Raise terminate all further steps. Induction over the intervening finite path establishes the claim.

#### Mathematical formulation

For a finite path from Created(k₀), consecutive occurrences of Resume in its label word have a Yield occurrence strictly between them.

**Lean formulation** (in its source module context):

```lean
∀ {K I O R E : Type u} (m : Catalog.AsymmetricCoroutine K I O R E) (leading middle trailing : List (Catalog.CoroutineAction I O R E)) (i j : I) (last : Catalog.CoroutineState K R E), Catalog.LabelledPath (Catalog.coroutineLTS m) (.created m.entry) (leading ++ (.resume i :: (middle ++ (.resume j :: trailing)))) last → ∃ o, Catalog.CoroutineAction.yieldValue o ∈ middle
```

**Source:** [`Catalog.CoroutineProofs.successive_resumes_require_yield`](../lean/Catalog/CoroutineProofs.lean); consulted 2026-11-14.

**Scope:** registered-witness-type

**Interpretation:** Lean tagged states/actions preserve continuation and input/output carriers. The independently reviewed expected type quantifies over a complete finite path and two Resume positions. It proves a yield exists in the intervening word, even without requiring these positions to be consecutive resumes. Equality and list membership are structural.

**Limits:** Proves the stated finite-trace property of coroutineStep, not language-runtime correspondence, infinite progress, cancellation, nested transfer or hidden-action equivalence.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/AsymmetricCoroutine-body-handoff": "coroutineStep enumerates all internal and boundary transitions. Unresumable and step_without_yield show that a no-yield segment cannot enable another Resume.",
  "urn:csabs:axiom/AsymmetricCoroutine-resume-entry": "coroutineStep permits Resume only from Created or Suspended and targets Running(accept k i); coroutineLTS starts in Created(entry).",
  "urn:csabs:axiom/LabelledTransitionSystem-finite-paths": "LabelledPath represents every finite labelled path including nil. path_split separates leading, middle and trailing subpaths without an extra trace axiom."
}
```

## Concept provenance

- [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation
- [Python 3.13 language reference: yield expressions and generator-iterator methods](https://docs.python.org/3.13/reference/expressions.html#yield-expressions); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard

**sourceNote:** Adapts the consulted resume/yield lifecycle to typed carriers and an explicit internal-step relation. Selects a fixed direct caller and Lua-style input on first resume. Leaves cleanup, nested caller stacks and Python-specific invalid-call exceptions outside scope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/AsymmetricCoroutine",
    "type": "Concept",
    "shortForm": "AsymmetricCoroutine",
    "fullName": "Asymmetric coroutine with explicit resume/yield lifecycle",
    "category": [
      "urn:csabs:category/cooperative-execution",
      "urn:csabs:category/concurrent-behavior"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A resumable computation retains a continuation, receives input from a fixed direct caller, and returns control to that caller by yielding, returning or failing. A small-step lifecycle distinguishes suspended and running execution.",
    "notation": "C=(K,I,O,R,E,k₀,accept,τ,Y,Ret,Err); S=Created(K)+Suspended(K)+Running(K)+Returned(R)+Failed(E)",
    "axiomBasis": "The complete step relation consists only of the resume, internal, yield, return and failure rules below. Creation does not execute the body. A resume outcome is a finite internal segment followed by one handoff boundary; existence of such an outcome is not assumed.",
    "basisKind": "defined-operational-semantics",
    "basisScope": "One coroutine and its fixed direct caller; no nested coroutine-to-coroutine resume, external mutation, preemption, cancellation, close, exception injection or stack-unwinding semantics. K stores all local control/data state; I,O,R,E are input, yielded, return and uncaught-error carriers with structural equality, allowed to be empty except the chosen entry k₀∈K. Created, Suspended, Running, Returned and Failed are disjoint tags. Internal steps may be nondeterministic, deadlock or diverge. All labels remain observable, including internal; hiding is a separate model. Resume accepts an input in both Created and Suspended, following the Lua-style initial-argument convention; Python generator priming needs an adapter. Invalid actions have no successor rather than an implicit runtime exception.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; Lean model binding is separate from claim proof evidence.",
    "requiresConcept": [
      "urn:csabs:concept/LabelledTransitionSystem",
      "urn:csabs:concept/PartialFunction"
    ],
    "specializationOf": [
      "urn:csabs:concept/LabelledTransitionSystem"
    ],
    "hasOperation": [
      "urn:csabs:operation/AsymmetricCoroutine-create",
      "urn:csabs:operation/AsymmetricCoroutine-step",
      "urn:csabs:operation/AsymmetricCoroutine-resume-outcomes"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/AsymmetricCoroutine-resume-entry",
      "urn:csabs:axiom/AsymmetricCoroutine-body-handoff",
      "urn:csabs:axiom/AsymmetricCoroutine-finite-resume-observation"
    ],
    "hasLaw": [
      "urn:csabs:law/AsymmetricCoroutine-terminal-no-successor",
      "urn:csabs:law/AsymmetricCoroutine-running-no-reentry"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/AsymmetricCoroutine-successive-resumes-require-yield"
    ],
    "verificationObligation": [
      "One coroutine and its fixed direct caller; no nested coroutine-to-coroutine resume, external mutation, preemption, cancellation, close, exception injection or stack-unwinding semantics. K stores all local control/data state; I,O,R,E are input, yielded, return and uncaught-error carriers with structural equality, allowed to be empty except the chosen entry k₀∈K. Created, Suspended, Running, Returned and Failed are disjoint tags. Internal steps may be nondeterministic, deadlock or diverge. All labels remain observable, including internal; hiding is a separate model. Resume accepts an input in both Created and Suspended, following the Lua-style initial-argument convention; Python generator priming needs an adapter. Invalid actions have no successor rather than an implicit runtime exception.",
      "Instantiate carriers, structural equality, state granularity and all external effects before applying this model. No fairness or progress guarantee follows from structural validation or the Lean interface."
    ],
    "formulationScope": "model",
    "leanModelMapping": "K,I,O,R,E are Lean types; CoroutineState is the tagged lifecycle carrier. entry selects the created state, accept injects resume input, and internal/yields/returns/raises are body relations. coroutineStep gives exactly the six lifecycle rules; coroutineLTS exposes the singleton initial state; coroutineOutcomes observes a resume, finite internal closure and one boundary event. Equality is Lean structural equality.",
    "leanModelLimitations": "Body semantics and retained heap/stack contents must be supplied by the instantiation. No language frontend, nested caller stack, shared-memory interference, cancellation, throw/close, fairness, divergence classification or complete runtime conformance is encoded. Only the separately registered successive-resumes-require-yield theorem has a compiled claim witness when verification evidence is fresh. Other graph claims and runtime correspondence remain separate obligations.",
    "formulationSource": "urn:csabs:source/local-lean-Coroutines",
    "formulationLocator": "Catalog.AsymmetricCoroutine",
    "source": [
      "urn:csabs:source/lua54-coroutines",
      "urn:csabs:source/python313-generators"
    ],
    "sourceLocator": "Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard",
    "sourceNote": "Adapts the consulted resume/yield lifecycle to typed carriers and an explicit internal-step relation. Selects a fixed direct caller and Lua-style input on first resume. Leaves cleanup, nested caller stacks and Python-specific invalid-call exceptions outside scope.",
    "provenanceKind": "adapted",
    "specializationNote": "Instantiate the parent with state sum S, labels Resume(i), Internal, Yield(o), Return(r), Raise(e), singleton initial state Created(k₀), and exactly the recorded step rules. The parent finite traces retain internal labels. No parent claims are inherited.",
    "relatedConcept": [
      "urn:csabs:concept/CooperativeScheduler",
      "urn:csabs:concept/FiniteIterator"
    ],
    "mathematicalFormulation": "Created(k) or Suspended(k) —Resume(i)→ Running(accept(k,i)); Running(k) —Internal→ Running(k′) iff τ(k,k′); —Yield(o)→ Suspended(k′) iff Y(k,o,k′); —Return(r)→ Returned(r) iff Ret(k,r); —Raise(e)→ Failed(e) iff Err(k,e). No other steps. Initial state is Created(k₀).",
    "leanFormulation": "structure AsymmetricCoroutine (K I O R E : Type u) where\n  entry : K\n  accept : K → I → K\n  internal : K → K → Prop\n  yields : K → O → K → Prop\n  returns : K → R → Prop\n  raises : K → E → Prop"
  },
  {
    "id": "urn:csabs:operation/AsymmetricCoroutine-create",
    "type": "Operation",
    "concept": "urn:csabs:concept/AsymmetricCoroutine",
    "name": "create",
    "signature": "create : C→S",
    "description": "Create a dormant coroutine at its entry continuation.",
    "precondition": "A body model C with k₀∈K is supplied.",
    "totality": "Total mathematical constructor; no body code executes.",
    "postcondition": "create(C)=Created(k₀).",
    "source": [
      "urn:csabs:source/lua54-coroutines",
      "urn:csabs:source/python313-generators"
    ],
    "sourceLocator": "Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard",
    "sourceNote": "Adapts the consulted resume/yield lifecycle to typed carriers and an explicit internal-step relation. Selects a fixed direct caller and Lua-style input on first resume. Leaves cleanup, nested caller stacks and Python-specific invalid-call exceptions outside scope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/AsymmetricCoroutine-step",
    "type": "Operation",
    "concept": "urn:csabs:concept/AsymmetricCoroutine",
    "name": "step",
    "signature": "step_C : S×Action→𝒫(S)",
    "description": "Allowed one-step lifecycle successors.",
    "precondition": "State and action use the selected typed carriers.",
    "totality": "Total set-valued relation image; disabled actions yield ∅. Not an executable decision procedure.",
    "postcondition": "step_C(s,a)={t | s —a→ t} using only the recorded lifecycle rules.",
    "source": [
      "urn:csabs:source/lua54-coroutines",
      "urn:csabs:source/python313-generators"
    ],
    "sourceLocator": "Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard",
    "sourceNote": "Adapts the consulted resume/yield lifecycle to typed carriers and an explicit internal-step relation. Selects a fixed direct caller and Lua-style input on first resume. Leaves cleanup, nested caller stacks and Python-specific invalid-call exceptions outside scope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/AsymmetricCoroutine-resume-outcomes",
    "type": "Operation",
    "concept": "urn:csabs:concept/AsymmetricCoroutine",
    "name": "resumeOutcomes",
    "signature": "out_C : S×I→𝒫(Boundary×S)",
    "description": "All finite observations of a resume up to its first yield, return or uncaught failure.",
    "precondition": "The state may be arbitrary; successful resume is possible only from Created or Suspended. Boundary={Yield(o),Return(r),Raise(e)}.",
    "totality": "Total set-valued specification. Empty outcomes may mean invalid resume, deadlock or absence of a finite boundary; it does not imply runtime termination.",
    "postcondition": "(a,t)∈out_C(s,i) iff ∃k,k′: s —Resume(i)→ Running(k) ∧ τ*(k,k′) ∧ Running(k′) —a→ t ∧ a∈Boundary.",
    "source": [
      "urn:csabs:source/lua54-coroutines",
      "urn:csabs:source/python313-generators"
    ],
    "sourceLocator": "Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard",
    "sourceNote": "Adapts the consulted resume/yield lifecycle to typed carriers and an explicit internal-step relation. Selects a fixed direct caller and Lua-style input on first resume. Leaves cleanup, nested caller stacks and Python-specific invalid-call exceptions outside scope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/AsymmetricCoroutine-resume-entry",
    "type": "Axiom",
    "name": "resume-entry",
    "statement": "Creation is dormant and resume enters a created or suspended continuation with caller-supplied input.",
    "description": "Creation is dormant and resume enters a created or suspended continuation with caller-supplied input.",
    "formalStatement": "I₀={Created(k₀)}; Created(k) —Resume(i)→ Running(accept(k,i)); Suspended(k) —Resume(i)→ Running(accept(k,i)); these are the only Resume-labelled steps.",
    "assumptions": [
      "One coroutine and its fixed direct caller; no nested coroutine-to-coroutine resume, external mutation, preemption, cancellation, close, exception injection or stack-unwinding semantics. K stores all local control/data state; I,O,R,E are input, yielded, return and uncaught-error carriers with structural equality, allowed to be empty except the chosen entry k₀∈K. Created, Suspended, Running, Returned and Failed are disjoint tags. Internal steps may be nondeterministic, deadlock or diverge. All labels remain observable, including internal; hiding is a separate model. Resume accepts an input in both Created and Suspended, following the Lua-style initial-argument convention; Python generator priming needs an adapter. Invalid actions have no successor rather than an implicit runtime exception."
    ],
    "appliesTo": [
      "urn:csabs:concept/AsymmetricCoroutine"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "editorial defining rule; not a machine-checked claim",
    "source": [
      "urn:csabs:source/lua54-coroutines",
      "urn:csabs:source/python313-generators"
    ],
    "sourceLocator": "Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard",
    "sourceNote": "Adapts the consulted resume/yield lifecycle to typed carriers and an explicit internal-step relation. Selects a fixed direct caller and Lua-style input on first resume. Leaves cleanup, nested caller stacks and Python-specific invalid-call exceptions outside scope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/AsymmetricCoroutine-body-handoff",
    "type": "Axiom",
    "name": "body-handoff",
    "statement": "Only running bodies take internal steps or hand control back to the caller; boundary events distinguish yield, return and failure.",
    "description": "Only running bodies take internal steps or hand control back to the caller; boundary events distinguish yield, return and failure.",
    "formalStatement": "Running(k) —Internal→ Running(k′) ⇔ τ(k,k′); Running(k) —Yield(o)→ Suspended(k′) ⇔ Y(k,o,k′); Running(k) —Return(r)→ Returned(r′) ⇔ r′=r ∧ Ret(k,r); Running(k) —Raise(e)→ Failed(e′) ⇔ e′=e ∧ Err(k,e). Together with resume-entry these are all steps.",
    "assumptions": [
      "One coroutine and its fixed direct caller; no nested coroutine-to-coroutine resume, external mutation, preemption, cancellation, close, exception injection or stack-unwinding semantics. K stores all local control/data state; I,O,R,E are input, yielded, return and uncaught-error carriers with structural equality, allowed to be empty except the chosen entry k₀∈K. Created, Suspended, Running, Returned and Failed are disjoint tags. Internal steps may be nondeterministic, deadlock or diverge. All labels remain observable, including internal; hiding is a separate model. Resume accepts an input in both Created and Suspended, following the Lua-style initial-argument convention; Python generator priming needs an adapter. Invalid actions have no successor rather than an implicit runtime exception."
    ],
    "appliesTo": [
      "urn:csabs:concept/AsymmetricCoroutine"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "editorial defining rule; not a machine-checked claim",
    "source": [
      "urn:csabs:source/lua54-coroutines",
      "urn:csabs:source/python313-generators"
    ],
    "sourceLocator": "Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard",
    "sourceNote": "Adapts the consulted resume/yield lifecycle to typed carriers and an explicit internal-step relation. Selects a fixed direct caller and Lua-style input on first resume. Leaves cleanup, nested caller stacks and Python-specific invalid-call exceptions outside scope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/AsymmetricCoroutine-finite-resume-observation",
    "type": "Axiom",
    "name": "finite-resume-observation",
    "statement": "A completed resume observation is exactly a resume followed by finitely many internal steps and one boundary handoff.",
    "description": "A completed resume observation is exactly a resume followed by finitely many internal steps and one boundary handoff.",
    "formalStatement": "(a,t)∈out_C(s,i) ⇔ a∈Boundary ∧ ∃k,k′:s —Resume(i)→ Running(k) ∧ τ*(k,k′) ∧ Running(k′) —a→ t; τ* is reflexive-transitive closure.",
    "assumptions": [
      "One coroutine and its fixed direct caller; no nested coroutine-to-coroutine resume, external mutation, preemption, cancellation, close, exception injection or stack-unwinding semantics. K stores all local control/data state; I,O,R,E are input, yielded, return and uncaught-error carriers with structural equality, allowed to be empty except the chosen entry k₀∈K. Created, Suspended, Running, Returned and Failed are disjoint tags. Internal steps may be nondeterministic, deadlock or diverge. All labels remain observable, including internal; hiding is a separate model. Resume accepts an input in both Created and Suspended, following the Lua-style initial-argument convention; Python generator priming needs an adapter. Invalid actions have no successor rather than an implicit runtime exception."
    ],
    "appliesTo": [
      "urn:csabs:concept/AsymmetricCoroutine"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "editorial defining rule; not a machine-checked claim",
    "source": [
      "urn:csabs:source/lua54-coroutines",
      "urn:csabs:source/python313-generators"
    ],
    "sourceLocator": "Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard",
    "sourceNote": "Adapts the consulted resume/yield lifecycle to typed carriers and an explicit internal-step relation. Selects a fixed direct caller and Lua-style input on first resume. Leaves cleanup, nested caller stacks and Python-specific invalid-call exceptions outside scope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/AsymmetricCoroutine-terminal-no-successor",
    "type": "Law",
    "name": "terminal-no-successor",
    "statement": "Returned and failed states have no outgoing lifecycle step.",
    "description": "Returned and failed states have no outgoing lifecycle step.",
    "formalStatement": "∀r,e,a: step_C(Returned(r),a)=∅ ∧ step_C(Failed(e),a)=∅",
    "assumptions": [
      "One coroutine and its fixed direct caller; no nested coroutine-to-coroutine resume, external mutation, preemption, cancellation, close, exception injection or stack-unwinding semantics. K stores all local control/data state; I,O,R,E are input, yielded, return and uncaught-error carriers with structural equality, allowed to be empty except the chosen entry k₀∈K. Created, Suspended, Running, Returned and Failed are disjoint tags. Internal steps may be nondeterministic, deadlock or diverge. All labels remain observable, including internal; hiding is a separate model. Resume accepts an input in both Created and Suspended, following the Lua-style initial-argument convention; Python generator priming needs an adapter. Invalid actions have no successor rather than an implicit runtime exception."
    ],
    "appliesTo": [
      "urn:csabs:concept/AsymmetricCoroutine"
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "editorial derivation; not a registered machine-checked claim",
    "source": [
      "urn:csabs:source/lua54-coroutines",
      "urn:csabs:source/python313-generators"
    ],
    "sourceLocator": "Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard",
    "sourceNote": "Editorial consequence of the explicit premises in this chosen model; not a numbered source theorem. Every rule has Created, Suspended or Running as its source. Disjointness of state tags excludes Returned and Failed.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/AsymmetricCoroutine-resume-entry",
      "urn:csabs:axiom/AsymmetricCoroutine-body-handoff"
    ],
    "proofSketch": "Every rule has Created, Suspended or Running as its source. Disjointness of state tags excludes Returned and Failed."
  },
  {
    "id": "urn:csabs:law/AsymmetricCoroutine-running-no-reentry",
    "type": "Law",
    "name": "running-no-reentry",
    "statement": "A running coroutine cannot be resumed again within this protocol.",
    "description": "A running coroutine cannot be resumed again within this protocol.",
    "formalStatement": "∀k,i: step_C(Running(k),Resume(i))=∅",
    "assumptions": [
      "One coroutine and its fixed direct caller; no nested coroutine-to-coroutine resume, external mutation, preemption, cancellation, close, exception injection or stack-unwinding semantics. K stores all local control/data state; I,O,R,E are input, yielded, return and uncaught-error carriers with structural equality, allowed to be empty except the chosen entry k₀∈K. Created, Suspended, Running, Returned and Failed are disjoint tags. Internal steps may be nondeterministic, deadlock or diverge. All labels remain observable, including internal; hiding is a separate model. Resume accepts an input in both Created and Suspended, following the Lua-style initial-argument convention; Python generator priming needs an adapter. Invalid actions have no successor rather than an implicit runtime exception."
    ],
    "appliesTo": [
      "urn:csabs:concept/AsymmetricCoroutine"
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "editorial derivation; not a registered machine-checked claim",
    "source": [
      "urn:csabs:source/lua54-coroutines",
      "urn:csabs:source/python313-generators"
    ],
    "sourceLocator": "Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard",
    "sourceNote": "Editorial consequence of the explicit premises in this chosen model; not a numbered source theorem. Only Created and Suspended admit Resume. Running admits internal, yield, return or failure labels, which are disjoint from Resume.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/AsymmetricCoroutine-resume-entry",
      "urn:csabs:axiom/AsymmetricCoroutine-body-handoff"
    ],
    "proofSketch": "Only Created and Suspended admit Resume. Running admits internal, yield, return or failure labels, which are disjoint from Resume."
  },
  {
    "id": "urn:csabs:theorem/AsymmetricCoroutine-successive-resumes-require-yield",
    "type": "Theorem",
    "name": "successive-resumes-require-yield",
    "statement": "Any two successive resume actions along a legal finite execution have a yield handoff between them.",
    "description": "Any two successive resume actions along a legal finite execution have a yield handoff between them.",
    "formalStatement": "For a finite path from Created(k₀), consecutive occurrences of Resume in its label word have a Yield occurrence strictly between them.",
    "assumptions": [
      "One coroutine and its fixed direct caller; no nested coroutine-to-coroutine resume, external mutation, preemption, cancellation, close, exception injection or stack-unwinding semantics. K stores all local control/data state; I,O,R,E are input, yielded, return and uncaught-error carriers with structural equality, allowed to be empty except the chosen entry k₀∈K. Created, Suspended, Running, Returned and Failed are disjoint tags. Internal steps may be nondeterministic, deadlock or diverge. All labels remain observable, including internal; hiding is a separate model. Resume accepts an input in both Created and Suspended, following the Lua-style initial-argument convention; Python generator priming needs an adapter. Invalid actions have no successor rather than an implicit runtime exception."
    ],
    "appliesTo": [
      "urn:csabs:concept/AsymmetricCoroutine"
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement with a separately mapped Lean witness; only fresh compiler and axiom-audit evidence establishes verification of the displayed Lean proposition.",
    "source": [
      "urn:csabs:source/lua54-coroutines",
      "urn:csabs:source/python313-generators"
    ],
    "sourceLocator": "Lua 5.4 §§2.6,6.2: create/resume/yield/status; Python 3.13 §§6.2.9–6.2.9.1: retained state, caller handoff, send priming and running-generator guard",
    "sourceNote": "Editorial consequence of the explicit premises in this chosen model; not a numbered source theorem. After the first Resume the phase is Running. Internal steps preserve it. To enable a later Resume the phase must become Created or Suspended. No rule re-creates a state; only Yield reaches Suspended. Return and Raise terminate all further steps. Induction over the intervening finite path establishes the claim.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/AsymmetricCoroutine-resume-entry",
      "urn:csabs:axiom/AsymmetricCoroutine-body-handoff",
      "urn:csabs:axiom/LabelledTransitionSystem-finite-paths"
    ],
    "proofSketch": "After the first Resume the phase is Running. Internal steps preserve it. To enable a later Resume the phase must become Created or Suspended. No rule re-creates a state; only Yield reaches Suspended. Return and Raise terminate all further steps. Induction over the intervening finite path establishes the claim.",
    "mathematicalFormulation": "For a finite path from Created(k₀), consecutive occurrences of Resume in its label word have a Yield occurrence strictly between them.",
    "leanFormulation": "∀ {K I O R E : Type u} (m : Catalog.AsymmetricCoroutine K I O R E) (leading middle trailing : List (Catalog.CoroutineAction I O R E)) (i j : I) (last : Catalog.CoroutineState K R E), Catalog.LabelledPath (Catalog.coroutineLTS m) (.created m.entry) (leading ++ (.resume i :: (middle ++ (.resume j :: trailing)))) last → ∃ o, Catalog.CoroutineAction.yieldValue o ∈ middle",
    "formulationSource": "urn:csabs:source/local-lean-CoroutineProofs",
    "formulationLocator": "Catalog.CoroutineProofs.successive_resumes_require_yield",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Lean tagged states/actions preserve continuation and input/output carriers. The independently reviewed expected type quantifies over a complete finite path and two Resume positions. It proves a yield exists in the intervening word, even without requiring these positions to be consecutive resumes. Equality and list membership are structural.",
    "leanModelLimitations": "Proves the stated finite-trace property of coroutineStep, not language-runtime correspondence, infinite progress, cancellation, nested transfer or hidden-action equivalence.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/AsymmetricCoroutine-body-handoff\": \"coroutineStep enumerates all internal and boundary transitions. Unresumable and step_without_yield show that a no-yield segment cannot enable another Resume.\", \"urn:csabs:axiom/AsymmetricCoroutine-resume-entry\": \"coroutineStep permits Resume only from Created or Suspended and targets Running(accept k i); coroutineLTS starts in Created(entry).\", \"urn:csabs:axiom/LabelledTransitionSystem-finite-paths\": \"LabelledPath represents every finite labelled path including nil. path_split separates leading, middle and trailing subpaths without an extra trace axiom.\"}"
  }
]
```
<!-- graph-record:end -->
