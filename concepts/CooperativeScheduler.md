# Single-thread cooperative scheduler with explicit waiting

A fixed finite family of coroutines shares one execution owner. Dispatch resumes one eligible coroutine; only a yield, wait request, return or failure releases ownership. Waiting tasks require an external wake action before dispatch.

**Notation:** σ=(c:J→S,active∈Option(J),W⊆J); c(j)∈CoroutineState; J finite

**Stable ID:** `urn:csabs:concept/CooperativeScheduler`

**Categories:** Programming-language semantics → Coroutines and cooperative execution, Concurrency and distributed systems → Behavioral models

**Kind:** semantic-model

**Prerequisites:** [Action-labelled transition system with initial states](LabelledTransitionSystem.md), [Asymmetric coroutine with explicit resume/yield lifecycle](AsymmetricCoroutine.md)

**Specializes:** [Action-labelled transition system with initial states](LabelledTransitionSystem.md)

**Related concepts:** [Asymmetric coroutine with explicit resume/yield lifecycle](AsymmetricCoroutine.md), [Safety Property](SafetyProperty.md), [Liveness Property](LivenessProperty.md)

## Backlinks

- [Asymmetric coroutine with explicit resume/yield lifecycle](AsymmetricCoroutine.md) — `relatedConcept`

## Mathematical formulation

σ₀=(j↦Created(k₀ⱼ),None,∅). Dispatch(j,i) requires active=None, j∉W and a local Resume(i) step; it updates c(j) and sets active=Some(j). Owner-only Internal preserves ownership; Yield releases it, Wait releases it and inserts j in W, Return/Raise release it and store terminal state. Wake(j) requires j∈W and only removes j from W. These are all steps.

**Lean formulation** (in its source module context):

```lean
structure CooperativeScheduler (T K I O R E : Type u) [Fintype T] where
  machine : T → AsymmetricCoroutine K I O R E
```

**Source:** [`Catalog.CooperativeScheduler`](../lean/Catalog/Coroutines.lean); consulted 2026-11-14.

**Scope:** model

**Interpretation:** Finite Lean task type T indexes a fixed family of coroutine models. CooperativeState stores a total task-state map, optional active owner and waiting Set. cooperativeInitial, cooperativeRunnable and cooperativeStep implement initialization, eligibility and all seven action rules; cooperativeLTS exposes the labelled system. Function.update changes only the selected task; cooperativeValid states the owner and waiting invariant. Structural equality is used throughout.

**Limits:** Typed fixed-pool operational model only; event identities, event readiness, real IO, fairness, wake delivery, cancellation, dynamic tasks and shared-memory interference require explicit extensions. Waiting is an explicit scheduler request, not every coroutine yield or syntactic await. Only the separately registered reachable-owner-invariant and cooperation-does-not-imply-progress theorems have compiled claim witnesses when verification evidence is fresh. Other claims and runtime correspondence remain separate obligations.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Initial, dispatch, owner-only advancement and wakeup are the complete operational rules. Only one task may be Running in valid states; waiting membership distinguishes blocked from immediately runnable suspended tasks. Scheduling policy and fairness are separate choices.

**basisKind:** defined-operational-semantics

**basisScope:** A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden.

**specializationNote:** Instantiate LabelledTransitionSystem with global states σ, the seven scheduler action families, singleton initial σ₀ and the exact scheduler rules. This is composition of coroutine models, not a specialization of one coroutine. No fairness or parent claim is inherited.

**verificationObligation:** A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden.; Instantiate carriers, structural equality, state granularity and all external effects before applying this model. No fairness or progress guarantee follows from structural validation or the Lean interface.

**reviewStatus:** Editorial source/interface review; Lean model binding is separate from claim proof evidence.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-CooperativeScheduler-initial"></a>

### initial

`urn:csabs:operation/CooperativeScheduler-initial`

**signature:** initial : (J→C)→GlobalState

**description:** Construct an idle pool of dormant coroutines.

**precondition:** J is fixed finite; a body with an entry continuation is supplied for every j∈J.

**totality:** Total constructor, including J=∅.

**postcondition:** σ₀=(j↦Created(k₀ⱼ),None,∅); no task body has run.

**source:** [Python 3.13 asyncio documentation: Task object and cooperative scheduling](https://docs.python.org/3.13/library/asyncio-task.html#task-object); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff

**sourceNote:** Constructs a fixed-pool scheduler model from the consulted cooperative execution behavior. Explicit dispatch, waiting-set bookkeeping, external wake and nondeterministic selection are abstract modeling choices, not a complete asyncio or Lua implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-CooperativeScheduler-runnable"></a>

### runnable

`urn:csabs:operation/CooperativeScheduler-runnable`

**signature:** runnable : GlobalState→𝒫(J)

**description:** Tasks eligible for selection when the owner slot is free.

**precondition:** The global state is valid. This observes eligibility, not guaranteed dispatch.

**totality:** Total mathematical observation on valid states.

**postcondition:** runnable(σ)={j∉W | ∃k:c(j)=Created(k) or c(j)=Suspended(k)}. A nonempty active slot independently disables Dispatch.

**source:** [Python 3.13 asyncio documentation: Task object and cooperative scheduling](https://docs.python.org/3.13/library/asyncio-task.html#task-object); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff

**sourceNote:** Constructs a fixed-pool scheduler model from the consulted cooperative execution behavior. Explicit dispatch, waiting-set bookkeeping, external wake and nondeterministic selection are abstract modeling choices, not a complete asyncio or Lua implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-CooperativeScheduler-step"></a>

### step

`urn:csabs:operation/CooperativeScheduler-step`

**signature:** step_M : GlobalState×SchedulerAction→𝒫(GlobalState)

**description:** One scheduler action from the complete rule set.

**precondition:** Use reachable valid states for the one-owner safety interpretation; all carriers and per-task body relations are supplied.

**totality:** Total relational image; disabled actions have no successors. No executable scheduling or liveness algorithm is promised.

**postcondition:** SchedulerAction={Dispatch(j,i),Internal,Yield(o),Wait(o),Wake(j),Return(r),Raise(e)}; successors are exactly the defining operational rules.

**source:** [Python 3.13 asyncio documentation: Task object and cooperative scheduling](https://docs.python.org/3.13/library/asyncio-task.html#task-object); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff

**sourceNote:** Constructs a fixed-pool scheduler model from the consulted cooperative execution behavior. Explicit dispatch, waiting-set bookkeeping, external wake and nondeterministic selection are abstract modeling choices, not a complete asyncio or Lua implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-CooperativeScheduler-initial-pool"></a>

### initial-pool

`urn:csabs:axiom/CooperativeScheduler-initial-pool`

**statement:** Initially every task is created, the owner slot is empty and no task is waiting.

**description:** Initially every task is created, the owner slot is empty and no task is waiting.

**formalStatement:** σ₀.c(j)=Created(k₀ⱼ) for every j∈J; σ₀.active=None; σ₀.W=∅.

**assumptions:** A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** editorial defining rule; not a machine-checked claim

**source:** [Python 3.13 asyncio documentation: Task object and cooperative scheduling](https://docs.python.org/3.13/library/asyncio-task.html#task-object); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff

**sourceNote:** Constructs a fixed-pool scheduler model from the consulted cooperative execution behavior. Explicit dispatch, waiting-set bookkeeping, external wake and nondeterministic selection are abstract modeling choices, not a complete asyncio or Lua implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-CooperativeScheduler-dispatch"></a>

### dispatch

`urn:csabs:axiom/CooperativeScheduler-dispatch`

**statement:** Dispatch is possible only from idle ownership to a nonwaiting resumable task, and updates only that task.

**description:** Dispatch is possible only from idle ownership to a nonwaiting resumable task, and updates only that task.

**formalStatement:** σ —Dispatch(j,i)→ σ′ ⇔ active=None ∧ j∉W ∧ ∃s′: c(j) —Resume(i)→ s′ ∧ σ′=(c[j↦s′],Some(j),W).

**assumptions:** A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** editorial defining rule; not a machine-checked claim

**source:** [Python 3.13 asyncio documentation: Task object and cooperative scheduling](https://docs.python.org/3.13/library/asyncio-task.html#task-object); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff

**sourceNote:** Constructs a fixed-pool scheduler model from the consulted cooperative execution behavior. Explicit dispatch, waiting-set bookkeeping, external wake and nondeterministic selection are abstract modeling choices, not a complete asyncio or Lua implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-CooperativeScheduler-owner-advancement"></a>

### owner-advancement

`urn:csabs:axiom/CooperativeScheduler-owner-advancement`

**statement:** Only the active coroutine advances; its handoff reason determines ownership and waiting updates.

**description:** Only the active coroutine advances; its handoff reason determines ownership and waiting updates.

**formalStatement:** If active=Some(j): Internal lifts local Internal to (c[j↦s′],Some(j),W); Yield(o) lifts local Yield(o) to (c[j↦s′],None,W); Wait(o) lifts local Yield(o) to (c[j↦s′],None,W∪{j}); Return(r) and Raise(e) lift their matching local labels to (c[j↦s′],None,W). Each lifted rule requires its local step; these and dispatch/wakeup are the only scheduler rules.

**assumptions:** A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** editorial defining rule; not a machine-checked claim

**source:** [Python 3.13 asyncio documentation: Task object and cooperative scheduling](https://docs.python.org/3.13/library/asyncio-task.html#task-object); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff

**sourceNote:** Constructs a fixed-pool scheduler model from the consulted cooperative execution behavior. Explicit dispatch, waiting-set bookkeeping, external wake and nondeterministic selection are abstract modeling choices, not a complete asyncio or Lua implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-CooperativeScheduler-external-wakeup"></a>

### external-wakeup

`urn:csabs:axiom/CooperativeScheduler-external-wakeup`

**statement:** Waking a waiting task changes eligibility without running it or transferring ownership.

**description:** Waking a waiting task changes eligibility without running it or transferring ownership.

**formalStatement:** σ —Wake(j)→ σ′ ⇔ j∈W ∧ σ′=(c,active,W\{j}).

**assumptions:** A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** editorial defining rule; not a machine-checked claim

**source:** [Python 3.13 asyncio documentation: Task object and cooperative scheduling](https://docs.python.org/3.13/library/asyncio-task.html#task-object); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff

**sourceNote:** Constructs a fixed-pool scheduler model from the consulted cooperative execution behavior. Explicit dispatch, waiting-set bookkeeping, external wake and nondeterministic selection are abstract modeling choices, not a complete asyncio or Lua implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-CooperativeScheduler-waiting-excludes-dispatch"></a>

### waiting-excludes-dispatch

`urn:csabs:law/CooperativeScheduler-waiting-excludes-dispatch`

**statement:** A waiting task cannot be dispatched until a wake action removes its waiting membership.

**description:** A waiting task cannot be dispatched until a wake action removes its waiting membership.

**formalStatement:** j∈W ⇒ step_M(σ,Dispatch(j,i))=∅; from a valid state no rule except Wake(j) removes a waiting j from W.

**assumptions:** A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden.; The state is valid.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** editorial derivation; not a registered machine-checked claim

**source:** [Python 3.13 asyncio documentation: Task object and cooperative scheduling](https://docs.python.org/3.13/library/asyncio-task.html#task-object); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff

**sourceNote:** Editorial consequence of the explicit premises in this chosen model; not a numbered source theorem. Dispatch directly requires j∉W. Only the active task can take a boundary step; a waiting task is suspended and cannot be that active running task. Owner rules retain W or insert the owner; only Wake removes a member.

**provenanceKind:** derived

**dependsOn:** [dispatch](CooperativeScheduler.md#node-urn-csabs-axiom-CooperativeScheduler-dispatch); [owner-advancement](CooperativeScheduler.md#node-urn-csabs-axiom-CooperativeScheduler-owner-advancement); [external-wakeup](CooperativeScheduler.md#node-urn-csabs-axiom-CooperativeScheduler-external-wakeup); [resume-entry](AsymmetricCoroutine.md#node-urn-csabs-axiom-AsymmetricCoroutine-resume-entry); [body-handoff](AsymmetricCoroutine.md#node-urn-csabs-axiom-AsymmetricCoroutine-body-handoff)

**proofSketch:** Dispatch directly requires j∉W. Only the active task can take a boundary step; a waiting task is suspended and cannot be that active running task. Owner rules retain W or insert the owner; only Wake removes a member.

<a id="node-urn-csabs-law-CooperativeScheduler-no-involuntary-switch"></a>

### no-involuntary-switch

`urn:csabs:law/CooperativeScheduler-no-involuntary-switch`

**statement:** A running task retains ownership across internal steps and external wakeups; another dispatch requires an explicit boundary handoff first.

**description:** A running task retains ownership across internal steps and external wakeups; another dispatch requires an explicit boundary handoff first.

**formalStatement:** active=Some(j) ⇒ no Dispatch(k,i) step; Internal and Wake preserve active. Only Yield,Wait,Return,Raise clear the owner slot.

**assumptions:** A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** editorial derivation; not a registered machine-checked claim

**source:** [Python 3.13 asyncio documentation: Task object and cooperative scheduling](https://docs.python.org/3.13/library/asyncio-task.html#task-object); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff

**sourceNote:** Editorial consequence of the explicit premises in this chosen model; not a numbered source theorem. Case-analyze the exhaustive scheduler rules. Dispatch requires an empty slot; Internal copies the current owner; Wake only changes W. Each handoff rule sets active to None.

**provenanceKind:** derived

**dependsOn:** [dispatch](CooperativeScheduler.md#node-urn-csabs-axiom-CooperativeScheduler-dispatch); [owner-advancement](CooperativeScheduler.md#node-urn-csabs-axiom-CooperativeScheduler-owner-advancement); [external-wakeup](CooperativeScheduler.md#node-urn-csabs-axiom-CooperativeScheduler-external-wakeup)

**proofSketch:** Case-analyze the exhaustive scheduler rules. Dispatch requires an empty slot; Internal copies the current owner; Wake only changes W. Each handoff rule sets active to None.

## Theorems

<a id="node-urn-csabs-theorem-CooperativeScheduler-reachable-owner-invariant"></a>

### reachable-owner-invariant

`urn:csabs:theorem/CooperativeScheduler-reachable-owner-invariant`

**statement:** Every finitely reachable scheduler state has exactly its active task running, if any, and all waiting tasks are suspended.

**description:** Every finitely reachable scheduler state has exactly its active task running, if any, and all waiting tasks are suspended.

**formalStatement:** σ₀ →* σ ⇒ (∀j: (∃k:c(j)=Running(k)) ⇔ active=Some(j)) ∧ (∀j∈W:∃k:c(j)=Suspended(k)).

**assumptions:** A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement with a separately mapped Lean witness; only fresh compiler and axiom-audit evidence establishes verification of the displayed Lean proposition.

**source:** [Python 3.13 asyncio documentation: Task object and cooperative scheduling](https://docs.python.org/3.13/library/asyncio-task.html#task-object); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff

**sourceNote:** Editorial consequence of the explicit premises in this chosen model; not a numbered source theorem. Induct on the finite execution. Initialization has no running or waiting task. Dispatch from idle changes one created/suspended nonwaiting task to Running and names it as owner. Internal preserves that phase and owner. Yield/Wait suspend the owner and clear it, with Wait adding the now-suspended owner to W. Return/Raise make it terminal and clear it. Other tasks do not change. Wake removes waiting membership only.

**provenanceKind:** derived

**dependsOn:** [initial-pool](CooperativeScheduler.md#node-urn-csabs-axiom-CooperativeScheduler-initial-pool); [dispatch](CooperativeScheduler.md#node-urn-csabs-axiom-CooperativeScheduler-dispatch); [owner-advancement](CooperativeScheduler.md#node-urn-csabs-axiom-CooperativeScheduler-owner-advancement); [external-wakeup](CooperativeScheduler.md#node-urn-csabs-axiom-CooperativeScheduler-external-wakeup); [resume-entry](AsymmetricCoroutine.md#node-urn-csabs-axiom-AsymmetricCoroutine-resume-entry); [body-handoff](AsymmetricCoroutine.md#node-urn-csabs-axiom-AsymmetricCoroutine-body-handoff)

**proofSketch:** Induct on the finite execution. Initialization has no running or waiting task. Dispatch from idle changes one created/suspended nonwaiting task to Running and names it as owner. Internal preserves that phase and owner. Yield/Wait suspend the owner and clear it, with Wait adding the now-suspended owner to W. Return/Raise make it terminal and clear it. Other tasks do not change. Wake removes waiting membership only.

#### Mathematical formulation

σ₀ →\* σ ⇒ (∀j: (∃k:c(j)=Running(k)) ⇔ active=Some(j)) ∧ (∀j∈W:∃k:c(j)=Suspended(k)).

**Lean formulation** (in its source module context):

```lean
∀ {T K I O R E : Type u} [Fintype T] [DecidableEq T] (m : Catalog.CooperativeScheduler T K I O R E) (s : Catalog.CooperativeState T K R E), Relation.ReflTransGen (fun a b => ∃ label, Catalog.cooperativeStep m a label b) (Catalog.cooperativeInitial m) s → Catalog.cooperativeValid s
```

**Source:** [`Catalog.CoroutineProofs.reachable_owner_invariant`](../lean/Catalog/CoroutineProofs.lean); consulted 2026-11-14.

**Scope:** registered-witness-type

**Interpretation:** Finite T indexes the fixed pool. cooperativeValid expands to: a task has Running state iff active=some task, and every waiting task is Suspended. ReflTransGen of existentially labelled cooperativeStep is exactly finite scheduler reachability from cooperativeInitial; every transition case is proved, not assumed.

**Limits:** Proves a safety invariant of the supplied abstract rules. No scheduler implementation refinement, fairness, termination, real IO, shared-memory or dynamic-task claim follows.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/AsymmetricCoroutine-body-handoff": "running_step_target derives each target phase from the local operational rules. Induction over ReflTransGen lifts preservation to all finitely reachable states.",
  "urn:csabs:axiom/AsymmetricCoroutine-resume-entry": "resume_target derives the Running target from coroutineStep; no global axiom assumes it.",
  "urn:csabs:axiom/CooperativeScheduler-dispatch": "The dispatch branch of cooperativeStep requires no owner and a nonwaiting local Resume step; replace_valid proves its task-map update preserves validity.",
  "urn:csabs:axiom/CooperativeScheduler-external-wakeup": "The Wake branch only removes waiting membership and preserves the task map and active owner.",
  "urn:csabs:axiom/CooperativeScheduler-initial-pool": "cooperativeInitial constructs the singleton starting configuration; initial_valid proves the owner/waiting invariant directly.",
  "urn:csabs:axiom/CooperativeScheduler-owner-advancement": "step_preserves_valid covers Internal, Yield, Wait, Return and Raise separately. Only the owner changes; Wait inserts its now-suspended task in waiting."
}
```

<a id="node-urn-csabs-theorem-CooperativeScheduler-cooperation-does-not-imply-progress"></a>

### cooperation-does-not-imply-progress

`urn:csabs:theorem/CooperativeScheduler-cooperation-does-not-imply-progress`

**statement:** A coroutine that can loop internally forever admits an execution starving an otherwise runnable task.

**description:** A coroutine that can loop internally forever admits an execution starving an otherwise runnable task.

**formalStatement:** If j≠h, σ is reachable and valid, active=Some(j), h∈runnable(σ), c(j)=Running(k), and τⱼ(k,k), then the infinite path σ —Internal→ σ —Internal→ … is permitted and never dispatches h.

**assumptions:** A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden.; The stated reachable state and internal self-loop exist; no fairness restriction is imposed.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement with a separately mapped Lean witness; only fresh compiler and axiom-audit evidence establishes verification of the displayed Lean proposition.

**source:** [Python 3.13 asyncio documentation: Task object and cooperative scheduling](https://docs.python.org/3.13/library/asyncio-task.html#task-object); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation; [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff

**sourceNote:** Editorial consequence of the explicit premises in this chosen model; not a numbered source theorem. Lift the assumed local self-loop through owner-advancement. It leaves the whole global state unchanged, so it can be repeated indefinitely. The idle-owner premise for dispatch never becomes true; h remains eligible but unexecuted. This is a conditional execution witness, not a claim that every body diverges.

**provenanceKind:** derived

**dependsOn:** [owner-advancement](CooperativeScheduler.md#node-urn-csabs-axiom-CooperativeScheduler-owner-advancement); [body-handoff](AsymmetricCoroutine.md#node-urn-csabs-axiom-AsymmetricCoroutine-body-handoff)

**proofSketch:** Lift the assumed local self-loop through owner-advancement. It leaves the whole global state unchanged, so it can be repeated indefinitely. The idle-owner premise for dispatch never becomes true; h remains eligible but unexecuted. This is a conditional execution witness, not a claim that every body diverges.

#### Mathematical formulation

If j≠h, σ is reachable and valid, active=Some(j), h∈runnable(σ), c(j)=Running(k), and τⱼ(k,k), then the infinite path σ —Internal→ σ —Internal→ … is permitted and never dispatches h.

**Lean formulation** (in its source module context):

```lean
∀ {T K I O R E : Type u} [Fintype T] [DecidableEq T] (m : Catalog.CooperativeScheduler T K I O R E) (s : Catalog.CooperativeState T K R E) (j h : T) (k : K), Relation.ReflTransGen (fun a b => ∃ label, Catalog.cooperativeStep m a label b) (Catalog.cooperativeInitial m) s → Catalog.cooperativeValid s → j ≠ h → s.active = some j → h ∈ Catalog.cooperativeRunnable s → s.tasks j = .running k → (m.machine j).internal k k → ∃ run : Nat → Catalog.CooperativeState T K R E, run 0 = s ∧ ∀ n, run n = s ∧ Catalog.cooperativeStep m (run n) .internal (run (n + 1)) ∧ (run n).active = some j ∧ h ∈ Catalog.cooperativeRunnable (run n) ∧ ¬ (∃ k', (run n).tasks h = .running k')
```

**Source:** [`Catalog.CoroutineProofs.cooperation_does_not_imply_progress`](../lean/Catalog/CoroutineProofs.lean); consulted 2026-11-14.

**Scope:** registered-witness-type

**Interpretation:** The expected type explicitly assumes a reachable valid state, distinct active/ready tasks and an internal self-loop. It constructs a constant Nat-indexed path with a valid Internal transition at every index; the other task stays runnable and never Running. No fairness restriction is added. A concrete Bool-task example separately demonstrates the hypotheses are realizable.

**Limits:** Conditional existence of one starving execution; it does not assert that every scheduler or coroutine starves, or that the model satisfies any fairness policy. The assumptions are not global axioms.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/AsymmetricCoroutine-body-handoff": "coroutineStep on Running k with Internal reduces exactly to the hypothesized body relation internal k k. Reachability, validity, distinct tasks, ownership, readiness and the self-loop are explicit theorem hypotheses, as in the graph claim.",
  "urn:csabs:axiom/CooperativeScheduler-owner-advancement": "The Internal branch lifts the supplied local self-loop to a global self-loop; cooperativeUpdate is proved equal to the original state. A Nat-indexed constant run witnesses the infinite execution."
}
```

## Concept provenance

- [Python 3.13 asyncio documentation: Task object and cooperative scheduling](https://docs.python.org/3.13/library/asyncio-task.html#task-object); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation
- [Lua 5.4 Reference Manual: coroutines](https://www.lua.org/manual/5.4/manual.html#2.6); accessedOn: 2026-11-14; sourceRole: consulted primary language/runtime reference; explicit abstract adaptation

**sourceLocator:** Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff

**sourceNote:** Constructs a fixed-pool scheduler model from the consulted cooperative execution behavior. Explicit dispatch, waiting-set bookkeeping, external wake and nondeterministic selection are abstract modeling choices, not a complete asyncio or Lua implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/CooperativeScheduler",
    "type": "Concept",
    "shortForm": "CooperativeScheduler",
    "fullName": "Single-thread cooperative scheduler with explicit waiting",
    "category": [
      "urn:csabs:category/cooperative-execution",
      "urn:csabs:category/concurrent-behavior"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A fixed finite family of coroutines shares one execution owner. Dispatch resumes one eligible coroutine; only a yield, wait request, return or failure releases ownership. Waiting tasks require an external wake action before dispatch.",
    "notation": "σ=(c:J→S,active∈Option(J),W⊆J); c(j)∈CoroutineState; J finite",
    "axiomBasis": "Initial, dispatch, owner-only advancement and wakeup are the complete operational rules. Only one task may be Running in valid states; waiting membership distinguishes blocked from immediately runnable suspended tasks. Scheduling policy and fairness are separate choices.",
    "basisKind": "defined-operational-semantics",
    "basisScope": "A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; Lean model binding is separate from claim proof evidence.",
    "requiresConcept": [
      "urn:csabs:concept/LabelledTransitionSystem",
      "urn:csabs:concept/AsymmetricCoroutine"
    ],
    "specializationOf": [
      "urn:csabs:concept/LabelledTransitionSystem"
    ],
    "hasOperation": [
      "urn:csabs:operation/CooperativeScheduler-initial",
      "urn:csabs:operation/CooperativeScheduler-runnable",
      "urn:csabs:operation/CooperativeScheduler-step"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/CooperativeScheduler-initial-pool",
      "urn:csabs:axiom/CooperativeScheduler-dispatch",
      "urn:csabs:axiom/CooperativeScheduler-owner-advancement",
      "urn:csabs:axiom/CooperativeScheduler-external-wakeup"
    ],
    "hasLaw": [
      "urn:csabs:law/CooperativeScheduler-waiting-excludes-dispatch",
      "urn:csabs:law/CooperativeScheduler-no-involuntary-switch"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/CooperativeScheduler-reachable-owner-invariant",
      "urn:csabs:theorem/CooperativeScheduler-cooperation-does-not-imply-progress"
    ],
    "verificationObligation": [
      "A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden.",
      "Instantiate carriers, structural equality, state granularity and all external effects before applying this model. No fairness or progress guarantee follows from structural validation or the Lean interface."
    ],
    "formulationScope": "model",
    "leanModelMapping": "Finite Lean task type T indexes a fixed family of coroutine models. CooperativeState stores a total task-state map, optional active owner and waiting Set. cooperativeInitial, cooperativeRunnable and cooperativeStep implement initialization, eligibility and all seven action rules; cooperativeLTS exposes the labelled system. Function.update changes only the selected task; cooperativeValid states the owner and waiting invariant. Structural equality is used throughout.",
    "leanModelLimitations": "Typed fixed-pool operational model only; event identities, event readiness, real IO, fairness, wake delivery, cancellation, dynamic tasks and shared-memory interference require explicit extensions. Waiting is an explicit scheduler request, not every coroutine yield or syntactic await. Only the separately registered reachable-owner-invariant and cooperation-does-not-imply-progress theorems have compiled claim witnesses when verification evidence is fresh. Other claims and runtime correspondence remain separate obligations.",
    "formulationSource": "urn:csabs:source/local-lean-Coroutines",
    "formulationLocator": "Catalog.CooperativeScheduler",
    "source": [
      "urn:csabs:source/python313-cooperative-tasks",
      "urn:csabs:source/lua54-coroutines"
    ],
    "sourceLocator": "Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff",
    "sourceNote": "Constructs a fixed-pool scheduler model from the consulted cooperative execution behavior. Explicit dispatch, waiting-set bookkeeping, external wake and nondeterministic selection are abstract modeling choices, not a complete asyncio or Lua implementation.",
    "provenanceKind": "adapted",
    "specializationNote": "Instantiate LabelledTransitionSystem with global states σ, the seven scheduler action families, singleton initial σ₀ and the exact scheduler rules. This is composition of coroutine models, not a specialization of one coroutine. No fairness or parent claim is inherited.",
    "relatedConcept": [
      "urn:csabs:concept/AsymmetricCoroutine",
      "urn:csabs:concept/SafetyProperty",
      "urn:csabs:concept/LivenessProperty"
    ],
    "mathematicalFormulation": "σ₀=(j↦Created(k₀ⱼ),None,∅). Dispatch(j,i) requires active=None, j∉W and a local Resume(i) step; it updates c(j) and sets active=Some(j). Owner-only Internal preserves ownership; Yield releases it, Wait releases it and inserts j in W, Return/Raise release it and store terminal state. Wake(j) requires j∈W and only removes j from W. These are all steps.",
    "leanFormulation": "structure CooperativeScheduler (T K I O R E : Type u) [Fintype T] where\n  machine : T → AsymmetricCoroutine K I O R E"
  },
  {
    "id": "urn:csabs:operation/CooperativeScheduler-initial",
    "type": "Operation",
    "concept": "urn:csabs:concept/CooperativeScheduler",
    "name": "initial",
    "signature": "initial : (J→C)→GlobalState",
    "description": "Construct an idle pool of dormant coroutines.",
    "precondition": "J is fixed finite; a body with an entry continuation is supplied for every j∈J.",
    "totality": "Total constructor, including J=∅.",
    "postcondition": "σ₀=(j↦Created(k₀ⱼ),None,∅); no task body has run.",
    "source": [
      "urn:csabs:source/python313-cooperative-tasks",
      "urn:csabs:source/lua54-coroutines"
    ],
    "sourceLocator": "Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff",
    "sourceNote": "Constructs a fixed-pool scheduler model from the consulted cooperative execution behavior. Explicit dispatch, waiting-set bookkeeping, external wake and nondeterministic selection are abstract modeling choices, not a complete asyncio or Lua implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/CooperativeScheduler-runnable",
    "type": "Operation",
    "concept": "urn:csabs:concept/CooperativeScheduler",
    "name": "runnable",
    "signature": "runnable : GlobalState→𝒫(J)",
    "description": "Tasks eligible for selection when the owner slot is free.",
    "precondition": "The global state is valid. This observes eligibility, not guaranteed dispatch.",
    "totality": "Total mathematical observation on valid states.",
    "postcondition": "runnable(σ)={j∉W | ∃k:c(j)=Created(k) or c(j)=Suspended(k)}. A nonempty active slot independently disables Dispatch.",
    "source": [
      "urn:csabs:source/python313-cooperative-tasks",
      "urn:csabs:source/lua54-coroutines"
    ],
    "sourceLocator": "Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff",
    "sourceNote": "Constructs a fixed-pool scheduler model from the consulted cooperative execution behavior. Explicit dispatch, waiting-set bookkeeping, external wake and nondeterministic selection are abstract modeling choices, not a complete asyncio or Lua implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/CooperativeScheduler-step",
    "type": "Operation",
    "concept": "urn:csabs:concept/CooperativeScheduler",
    "name": "step",
    "signature": "step_M : GlobalState×SchedulerAction→𝒫(GlobalState)",
    "description": "One scheduler action from the complete rule set.",
    "precondition": "Use reachable valid states for the one-owner safety interpretation; all carriers and per-task body relations are supplied.",
    "totality": "Total relational image; disabled actions have no successors. No executable scheduling or liveness algorithm is promised.",
    "postcondition": "SchedulerAction={Dispatch(j,i),Internal,Yield(o),Wait(o),Wake(j),Return(r),Raise(e)}; successors are exactly the defining operational rules.",
    "source": [
      "urn:csabs:source/python313-cooperative-tasks",
      "urn:csabs:source/lua54-coroutines"
    ],
    "sourceLocator": "Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff",
    "sourceNote": "Constructs a fixed-pool scheduler model from the consulted cooperative execution behavior. Explicit dispatch, waiting-set bookkeeping, external wake and nondeterministic selection are abstract modeling choices, not a complete asyncio or Lua implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/CooperativeScheduler-initial-pool",
    "type": "Axiom",
    "name": "initial-pool",
    "statement": "Initially every task is created, the owner slot is empty and no task is waiting.",
    "description": "Initially every task is created, the owner slot is empty and no task is waiting.",
    "formalStatement": "σ₀.c(j)=Created(k₀ⱼ) for every j∈J; σ₀.active=None; σ₀.W=∅.",
    "assumptions": [
      "A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden."
    ],
    "appliesTo": [
      "urn:csabs:concept/CooperativeScheduler"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "editorial defining rule; not a machine-checked claim",
    "source": [
      "urn:csabs:source/python313-cooperative-tasks",
      "urn:csabs:source/lua54-coroutines"
    ],
    "sourceLocator": "Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff",
    "sourceNote": "Constructs a fixed-pool scheduler model from the consulted cooperative execution behavior. Explicit dispatch, waiting-set bookkeeping, external wake and nondeterministic selection are abstract modeling choices, not a complete asyncio or Lua implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/CooperativeScheduler-dispatch",
    "type": "Axiom",
    "name": "dispatch",
    "statement": "Dispatch is possible only from idle ownership to a nonwaiting resumable task, and updates only that task.",
    "description": "Dispatch is possible only from idle ownership to a nonwaiting resumable task, and updates only that task.",
    "formalStatement": "σ —Dispatch(j,i)→ σ′ ⇔ active=None ∧ j∉W ∧ ∃s′: c(j) —Resume(i)→ s′ ∧ σ′=(c[j↦s′],Some(j),W).",
    "assumptions": [
      "A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden."
    ],
    "appliesTo": [
      "urn:csabs:concept/CooperativeScheduler"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "editorial defining rule; not a machine-checked claim",
    "source": [
      "urn:csabs:source/python313-cooperative-tasks",
      "urn:csabs:source/lua54-coroutines"
    ],
    "sourceLocator": "Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff",
    "sourceNote": "Constructs a fixed-pool scheduler model from the consulted cooperative execution behavior. Explicit dispatch, waiting-set bookkeeping, external wake and nondeterministic selection are abstract modeling choices, not a complete asyncio or Lua implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/CooperativeScheduler-owner-advancement",
    "type": "Axiom",
    "name": "owner-advancement",
    "statement": "Only the active coroutine advances; its handoff reason determines ownership and waiting updates.",
    "description": "Only the active coroutine advances; its handoff reason determines ownership and waiting updates.",
    "formalStatement": "If active=Some(j): Internal lifts local Internal to (c[j↦s′],Some(j),W); Yield(o) lifts local Yield(o) to (c[j↦s′],None,W); Wait(o) lifts local Yield(o) to (c[j↦s′],None,W∪{j}); Return(r) and Raise(e) lift their matching local labels to (c[j↦s′],None,W). Each lifted rule requires its local step; these and dispatch/wakeup are the only scheduler rules.",
    "assumptions": [
      "A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden."
    ],
    "appliesTo": [
      "urn:csabs:concept/CooperativeScheduler"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "editorial defining rule; not a machine-checked claim",
    "source": [
      "urn:csabs:source/python313-cooperative-tasks",
      "urn:csabs:source/lua54-coroutines"
    ],
    "sourceLocator": "Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff",
    "sourceNote": "Constructs a fixed-pool scheduler model from the consulted cooperative execution behavior. Explicit dispatch, waiting-set bookkeeping, external wake and nondeterministic selection are abstract modeling choices, not a complete asyncio or Lua implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/CooperativeScheduler-external-wakeup",
    "type": "Axiom",
    "name": "external-wakeup",
    "statement": "Waking a waiting task changes eligibility without running it or transferring ownership.",
    "description": "Waking a waiting task changes eligibility without running it or transferring ownership.",
    "formalStatement": "σ —Wake(j)→ σ′ ⇔ j∈W ∧ σ′=(c,active,W\\{j}).",
    "assumptions": [
      "A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden."
    ],
    "appliesTo": [
      "urn:csabs:concept/CooperativeScheduler"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "editorial defining rule; not a machine-checked claim",
    "source": [
      "urn:csabs:source/python313-cooperative-tasks",
      "urn:csabs:source/lua54-coroutines"
    ],
    "sourceLocator": "Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff",
    "sourceNote": "Constructs a fixed-pool scheduler model from the consulted cooperative execution behavior. Explicit dispatch, waiting-set bookkeeping, external wake and nondeterministic selection are abstract modeling choices, not a complete asyncio or Lua implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/CooperativeScheduler-waiting-excludes-dispatch",
    "type": "Law",
    "name": "waiting-excludes-dispatch",
    "statement": "A waiting task cannot be dispatched until a wake action removes its waiting membership.",
    "description": "A waiting task cannot be dispatched until a wake action removes its waiting membership.",
    "formalStatement": "j∈W ⇒ step_M(σ,Dispatch(j,i))=∅; from a valid state no rule except Wake(j) removes a waiting j from W.",
    "assumptions": [
      "A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden.",
      "The state is valid."
    ],
    "appliesTo": [
      "urn:csabs:concept/CooperativeScheduler"
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "editorial derivation; not a registered machine-checked claim",
    "source": [
      "urn:csabs:source/python313-cooperative-tasks",
      "urn:csabs:source/lua54-coroutines"
    ],
    "sourceLocator": "Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff",
    "sourceNote": "Editorial consequence of the explicit premises in this chosen model; not a numbered source theorem. Dispatch directly requires j∉W. Only the active task can take a boundary step; a waiting task is suspended and cannot be that active running task. Owner rules retain W or insert the owner; only Wake removes a member.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/CooperativeScheduler-dispatch",
      "urn:csabs:axiom/CooperativeScheduler-owner-advancement",
      "urn:csabs:axiom/CooperativeScheduler-external-wakeup",
      "urn:csabs:axiom/AsymmetricCoroutine-resume-entry",
      "urn:csabs:axiom/AsymmetricCoroutine-body-handoff"
    ],
    "proofSketch": "Dispatch directly requires j∉W. Only the active task can take a boundary step; a waiting task is suspended and cannot be that active running task. Owner rules retain W or insert the owner; only Wake removes a member."
  },
  {
    "id": "urn:csabs:law/CooperativeScheduler-no-involuntary-switch",
    "type": "Law",
    "name": "no-involuntary-switch",
    "statement": "A running task retains ownership across internal steps and external wakeups; another dispatch requires an explicit boundary handoff first.",
    "description": "A running task retains ownership across internal steps and external wakeups; another dispatch requires an explicit boundary handoff first.",
    "formalStatement": "active=Some(j) ⇒ no Dispatch(k,i) step; Internal and Wake preserve active. Only Yield,Wait,Return,Raise clear the owner slot.",
    "assumptions": [
      "A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden."
    ],
    "appliesTo": [
      "urn:csabs:concept/CooperativeScheduler"
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "editorial derivation; not a registered machine-checked claim",
    "source": [
      "urn:csabs:source/python313-cooperative-tasks",
      "urn:csabs:source/lua54-coroutines"
    ],
    "sourceLocator": "Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff",
    "sourceNote": "Editorial consequence of the explicit premises in this chosen model; not a numbered source theorem. Case-analyze the exhaustive scheduler rules. Dispatch requires an empty slot; Internal copies the current owner; Wake only changes W. Each handoff rule sets active to None.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/CooperativeScheduler-dispatch",
      "urn:csabs:axiom/CooperativeScheduler-owner-advancement",
      "urn:csabs:axiom/CooperativeScheduler-external-wakeup"
    ],
    "proofSketch": "Case-analyze the exhaustive scheduler rules. Dispatch requires an empty slot; Internal copies the current owner; Wake only changes W. Each handoff rule sets active to None."
  },
  {
    "id": "urn:csabs:theorem/CooperativeScheduler-reachable-owner-invariant",
    "type": "Theorem",
    "name": "reachable-owner-invariant",
    "statement": "Every finitely reachable scheduler state has exactly its active task running, if any, and all waiting tasks are suspended.",
    "description": "Every finitely reachable scheduler state has exactly its active task running, if any, and all waiting tasks are suspended.",
    "formalStatement": "σ₀ →* σ ⇒ (∀j: (∃k:c(j)=Running(k)) ⇔ active=Some(j)) ∧ (∀j∈W:∃k:c(j)=Suspended(k)).",
    "assumptions": [
      "A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden."
    ],
    "appliesTo": [
      "urn:csabs:concept/CooperativeScheduler"
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement with a separately mapped Lean witness; only fresh compiler and axiom-audit evidence establishes verification of the displayed Lean proposition.",
    "source": [
      "urn:csabs:source/python313-cooperative-tasks",
      "urn:csabs:source/lua54-coroutines"
    ],
    "sourceLocator": "Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff",
    "sourceNote": "Editorial consequence of the explicit premises in this chosen model; not a numbered source theorem. Induct on the finite execution. Initialization has no running or waiting task. Dispatch from idle changes one created/suspended nonwaiting task to Running and names it as owner. Internal preserves that phase and owner. Yield/Wait suspend the owner and clear it, with Wait adding the now-suspended owner to W. Return/Raise make it terminal and clear it. Other tasks do not change. Wake removes waiting membership only.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/CooperativeScheduler-initial-pool",
      "urn:csabs:axiom/CooperativeScheduler-dispatch",
      "urn:csabs:axiom/CooperativeScheduler-owner-advancement",
      "urn:csabs:axiom/CooperativeScheduler-external-wakeup",
      "urn:csabs:axiom/AsymmetricCoroutine-resume-entry",
      "urn:csabs:axiom/AsymmetricCoroutine-body-handoff"
    ],
    "proofSketch": "Induct on the finite execution. Initialization has no running or waiting task. Dispatch from idle changes one created/suspended nonwaiting task to Running and names it as owner. Internal preserves that phase and owner. Yield/Wait suspend the owner and clear it, with Wait adding the now-suspended owner to W. Return/Raise make it terminal and clear it. Other tasks do not change. Wake removes waiting membership only.",
    "mathematicalFormulation": "σ₀ →* σ ⇒ (∀j: (∃k:c(j)=Running(k)) ⇔ active=Some(j)) ∧ (∀j∈W:∃k:c(j)=Suspended(k)).",
    "leanFormulation": "∀ {T K I O R E : Type u} [Fintype T] [DecidableEq T] (m : Catalog.CooperativeScheduler T K I O R E) (s : Catalog.CooperativeState T K R E), Relation.ReflTransGen (fun a b => ∃ label, Catalog.cooperativeStep m a label b) (Catalog.cooperativeInitial m) s → Catalog.cooperativeValid s",
    "formulationSource": "urn:csabs:source/local-lean-CoroutineProofs",
    "formulationLocator": "Catalog.CoroutineProofs.reachable_owner_invariant",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite T indexes the fixed pool. cooperativeValid expands to: a task has Running state iff active=some task, and every waiting task is Suspended. ReflTransGen of existentially labelled cooperativeStep is exactly finite scheduler reachability from cooperativeInitial; every transition case is proved, not assumed.",
    "leanModelLimitations": "Proves a safety invariant of the supplied abstract rules. No scheduler implementation refinement, fairness, termination, real IO, shared-memory or dynamic-task claim follows.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/AsymmetricCoroutine-body-handoff\": \"running_step_target derives each target phase from the local operational rules. Induction over ReflTransGen lifts preservation to all finitely reachable states.\", \"urn:csabs:axiom/AsymmetricCoroutine-resume-entry\": \"resume_target derives the Running target from coroutineStep; no global axiom assumes it.\", \"urn:csabs:axiom/CooperativeScheduler-dispatch\": \"The dispatch branch of cooperativeStep requires no owner and a nonwaiting local Resume step; replace_valid proves its task-map update preserves validity.\", \"urn:csabs:axiom/CooperativeScheduler-external-wakeup\": \"The Wake branch only removes waiting membership and preserves the task map and active owner.\", \"urn:csabs:axiom/CooperativeScheduler-initial-pool\": \"cooperativeInitial constructs the singleton starting configuration; initial_valid proves the owner/waiting invariant directly.\", \"urn:csabs:axiom/CooperativeScheduler-owner-advancement\": \"step_preserves_valid covers Internal, Yield, Wait, Return and Raise separately. Only the owner changes; Wait inserts its now-suspended task in waiting.\"}"
  },
  {
    "id": "urn:csabs:theorem/CooperativeScheduler-cooperation-does-not-imply-progress",
    "type": "Theorem",
    "name": "cooperation-does-not-imply-progress",
    "statement": "A coroutine that can loop internally forever admits an execution starving an otherwise runnable task.",
    "description": "A coroutine that can loop internally forever admits an execution starving an otherwise runnable task.",
    "formalStatement": "If j≠h, σ is reachable and valid, active=Some(j), h∈runnable(σ), c(j)=Running(k), and τⱼ(k,k), then the infinite path σ —Internal→ σ —Internal→ … is permitted and never dispatches h.",
    "assumptions": [
      "A fixed finite pool J, possibly empty, runs on one logical thread; each j has an AsymmetricCoroutine body with shared typed carriers. Global state is σ=(c:J→S,active:Option(J),W⊆J). State equality retains every local state, active owner and waiting membership. W marks suspended tasks requiring external wakeup. Validity means Running(c(j)) iff active=Some(j), and j∈W implies Suspended(c(j)). Waiting need not have a future wakeup. Dispatch choice and body steps may be nondeterministic; no fairness, bounded response, termination or freedom from deadlock is assumed. No task creation/removal, nested resume, cancellation, exception injection, parallel execution or shared-memory mutation is modeled. Wake is an external administrative action that does not execute a task. Internal labels are not hidden.",
      "The stated reachable state and internal self-loop exist; no fairness restriction is imposed."
    ],
    "appliesTo": [
      "urn:csabs:concept/CooperativeScheduler"
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement with a separately mapped Lean witness; only fresh compiler and axiom-audit evidence establishes verification of the displayed Lean proposition.",
    "source": [
      "urn:csabs:source/python313-cooperative-tasks",
      "urn:csabs:source/lua54-coroutines"
    ],
    "sourceLocator": "Python 3.13 asyncio Task object: one Task at a time and waiting on a Future; Lua 5.4 §2.6: explicit yield/resume handoff",
    "sourceNote": "Editorial consequence of the explicit premises in this chosen model; not a numbered source theorem. Lift the assumed local self-loop through owner-advancement. It leaves the whole global state unchanged, so it can be repeated indefinitely. The idle-owner premise for dispatch never becomes true; h remains eligible but unexecuted. This is a conditional execution witness, not a claim that every body diverges.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/CooperativeScheduler-owner-advancement",
      "urn:csabs:axiom/AsymmetricCoroutine-body-handoff"
    ],
    "proofSketch": "Lift the assumed local self-loop through owner-advancement. It leaves the whole global state unchanged, so it can be repeated indefinitely. The idle-owner premise for dispatch never becomes true; h remains eligible but unexecuted. This is a conditional execution witness, not a claim that every body diverges.",
    "mathematicalFormulation": "If j≠h, σ is reachable and valid, active=Some(j), h∈runnable(σ), c(j)=Running(k), and τⱼ(k,k), then the infinite path σ —Internal→ σ —Internal→ … is permitted and never dispatches h.",
    "leanFormulation": "∀ {T K I O R E : Type u} [Fintype T] [DecidableEq T] (m : Catalog.CooperativeScheduler T K I O R E) (s : Catalog.CooperativeState T K R E) (j h : T) (k : K), Relation.ReflTransGen (fun a b => ∃ label, Catalog.cooperativeStep m a label b) (Catalog.cooperativeInitial m) s → Catalog.cooperativeValid s → j ≠ h → s.active = some j → h ∈ Catalog.cooperativeRunnable s → s.tasks j = .running k → (m.machine j).internal k k → ∃ run : Nat → Catalog.CooperativeState T K R E, run 0 = s ∧ ∀ n, run n = s ∧ Catalog.cooperativeStep m (run n) .internal (run (n + 1)) ∧ (run n).active = some j ∧ h ∈ Catalog.cooperativeRunnable (run n) ∧ ¬ (∃ k', (run n).tasks h = .running k')",
    "formulationSource": "urn:csabs:source/local-lean-CoroutineProofs",
    "formulationLocator": "Catalog.CoroutineProofs.cooperation_does_not_imply_progress",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "The expected type explicitly assumes a reachable valid state, distinct active/ready tasks and an internal self-loop. It constructs a constant Nat-indexed path with a valid Internal transition at every index; the other task stays runnable and never Running. No fairness restriction is added. A concrete Bool-task example separately demonstrates the hypotheses are realizable.",
    "leanModelLimitations": "Conditional existence of one starving execution; it does not assert that every scheduler or coroutine starves, or that the model satisfies any fairness policy. The assumptions are not global axioms.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/AsymmetricCoroutine-body-handoff\": \"coroutineStep on Running k with Internal reduces exactly to the hypothesized body relation internal k k. Reachability, validity, distinct tasks, ownership, readiness and the self-loop are explicit theorem hypotheses, as in the graph claim.\", \"urn:csabs:axiom/CooperativeScheduler-owner-advancement\": \"The Internal branch lifts the supplied local self-loop to a global self-loop; cooperativeUpdate is proved equal to the original state. A Nat-indexed constant run witnesses the infinite execution.\"}"
  }
]
```
<!-- graph-record:end -->
