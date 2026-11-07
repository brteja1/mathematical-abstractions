# Deterministic one-tape Turing machine

A finite controller reads and writes an unbounded one-sided tape, moving its head one cell per step until it accepts, rejects, or runs forever.

**Notation:** M=(Q,Σ,Γ,δ,q₀,qacc,qrej); δ:(Q∖{qacc,qrej})×Γ→Q×Γ×{L,R}

**Stable ID:** `urn:csabs:concept/TuringMachine`

**Categories:** Languages and computation, Programming-language semantics

**Kind:** semantic-model

**Prerequisites:** [Formal language of finite words](FormalLanguage.md), [Transition System](TransitionSystem.md), [Partial function](PartialFunction.md)

**Related concepts:** [Deterministic finite automaton with total transition](DFA.md)

## Interface and scope

**axiomBasis:** Selected defining presentation: The finite control and alphabets determine a total table on nonhalting states. The finite transition table gives a unique next configuration outside the two halting states. Recognition means eventual acceptance; a decider halts on every input. Input is written once at the left end and the remaining tape is blank.

**basisKind:** defined-structure

**basisScope:** Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀,qacc,qrej∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded. States and symbols use identity equality; machine identity differs from accepted-language equality.

**verificationObligation:** Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀,qacc,qrej∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded. States and symbols use identity equality; machine identity differs from accepted-language equality.

**reviewStatus:** editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-TuringMachine-step"></a>

### step

`urn:csabs:operation/TuringMachine-step`

**signature:** step_M : Config(M) ⇀ Config(M)

**description:** Updates the scanned cell, control state, and head position.

**precondition:** Current control state is neither qacc nor qrej.

**totality:** partial: defined on exactly the nonhalting configurations

**postcondition:** Updates the scanned cell, control state, and head position.

<a id="node-urn-csabs-operation-TuringMachine-outcome"></a>

### outcome

`urn:csabs:operation/TuringMachine-outcome`

**signature:** outcome_M : Σ* ⇀ {accept,reject}

**description:** Returns the halting outcome if it occurs; divergence is outside its defined domain.

**precondition:** The run on the input halts.

**totality:** partial: defined exactly for halting inputs; no general decision procedure for definedness is asserted

**postcondition:** Returns the halting outcome if it occurs; divergence is outside its defined domain.

<a id="node-urn-csabs-operation-TuringMachine-initialConfiguration"></a>

### initialConfiguration

`urn:csabs:operation/TuringMachine-initialConfiguration`

**signature:** init_M : Σ*→Config(M)

**description:** Places w in cells 0 through |w|−1, blanks elsewhere, with head 0 and control q₀.

**precondition:** Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀,qacc,qrej∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded. States and symbols use identity equality; machine identity differs from accepted-language equality.

**postcondition:** Places w in cells 0 through |w|−1, blanks elsewhere, with head 0 and control q₀.

**totality:** total mathematical operation on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-TuringMachine-finite-control"></a>

### finite-control

`urn:csabs:axiom/TuringMachine-finite-control`

**statement:** The finite control and alphabets determine a total table on nonhalting states.

**description:** The model includes a distinguished blank and two distinct halting states.

**formalStatement:** Q,Σ,Γ finite; q₀,qacc,qrej∈Q; qacc≠qrej; blank∈Γ; Σ⊆Γ∖{blank}; δ:(Q∖{qacc,qrej})×Γ→Q×Γ×{L,R}

**assumptions:** Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀,qacc,qrej∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded. States and symbols use identity equality; machine identity differs from accepted-language equality.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 5](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/18c8cd00b14d48dc5865f3bdc41abd76_MIT18_404f20_lec5.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8, 10–11: tape convention, TM definition, recognizers and deciders

**sourceNote:** Makes halting states absorbing outcomes with no outgoing machine steps. A left move at cell zero stays there; the consulted one-sided tape presentation is used. Table entries at halting states are omitted because they are never executed.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-TuringMachine-machine-step"></a>

### machine-step

`urn:csabs:axiom/TuringMachine-machine-step`

**statement:** The finite transition table gives a unique next configuration outside the two halting states.

**description:** The finite transition table gives a unique next configuration outside the two halting states.

**formalStatement:** Config=(q,t,h), h∈ℕ, t:ℕ→Γ eventually blank; δ(q,t(h))=(q′,b,d) ⇒ step(q,t,h)=(q′,t[h↦b], if d=R then h+1 else max(0,h−1)); step undefined at qacc,qrej

**assumptions:** Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 5](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/18c8cd00b14d48dc5865f3bdc41abd76_MIT18_404f20_lec5.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8, 10–11: tape convention, TM definition, recognizers and deciders

**sourceNote:** Makes halting states absorbing outcomes with no outgoing machine steps. A left move at cell zero stays there; the consulted one-sided tape presentation is used. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-TuringMachine-recognition-decision"></a>

### recognition-decision

`urn:csabs:axiom/TuringMachine-recognition-decision`

**statement:** Recognition means eventual acceptance; a decider halts on every input.

**description:** Recognition means eventual acceptance; a decider halts on every input.

**formalStatement:** L(M)={w:the unique run from init(w) reaches qacc}; Decider(M) iff ∀w∈Σ*:run_M(w) reaches qacc or qrej

**assumptions:** Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 5](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/18c8cd00b14d48dc5865f3bdc41abd76_MIT18_404f20_lec5.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8, 10–11: tape convention, TM definition, recognizers and deciders

**sourceNote:** Makes halting states absorbing outcomes with no outgoing machine steps. A left move at cell zero stays there; the consulted one-sided tape presentation is used. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-TuringMachine-initial-configuration"></a>

### initial-configuration

`urn:csabs:axiom/TuringMachine-initial-configuration`

**statement:** Input is written once at the left end and the remaining tape is blank.

**description:** Input is written once at the left end and the remaining tape is blank.

**formalStatement:** init_M(w)=(q₀,t_w,0); t_w(i)=w_i if i<|w|, otherwise blank

**assumptions:** Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀,qacc,qrej∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded. States and symbols use identity equality; machine identity differs from accepted-language equality.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 5](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/18c8cd00b14d48dc5865f3bdc41abd76_MIT18_404f20_lec5.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Lecture 5, slides 8–10: one-sided tape and input conventions

**sourceNote:** Specifies additional equations for the selected abstract interface; local conventions are explicit.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-TuringMachine-step-determinism"></a>

### step-determinism

`urn:csabs:law/TuringMachine-step-determinism`

**statement:** Each nonhalting configuration has exactly one successor; halting configurations have none.

**description:** Each nonhalting configuration has exactly one successor; halting configurations have none.

**formalStatement:** q∉{qacc,qrej}⇒∃!c′:step_M(q,t,h)=c′; q∈{qacc,qrej}⇒step_M(q,t,h) undefined

**assumptions:** Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀,qacc,qrej∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded. States and symbols use identity equality; machine identity differs from accepted-language equality.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 5](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/18c8cd00b14d48dc5865f3bdc41abd76_MIT18_404f20_lec5.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8, 10–11: tape convention, TM definition, recognizers and deciders

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** The table is a total function on nonhalting control and scanned symbols. A finite tape update and the boundary movement rule determine one successor. The step definition explicitly excludes halting states.

**dependsOn:** [finite-control](TuringMachine.md#node-urn-csabs-axiom-TuringMachine-finite-control); [machine-step](TuringMachine.md#node-urn-csabs-axiom-TuringMachine-machine-step); [recognition-decision](TuringMachine.md#node-urn-csabs-axiom-TuringMachine-recognition-decision); [initial-configuration](TuringMachine.md#node-urn-csabs-axiom-TuringMachine-initial-configuration)

## Theorems

<a id="node-urn-csabs-theorem-TuringMachine-decider-complement"></a>

### decider-complement

`urn:csabs:theorem/TuringMachine-decider-complement`

**statement:** Swapping the two halting outcomes of a decider decides the complementary language.

**description:** Swapping the two halting outcomes of a decider decides the complementary language.

**formalStatement:** Decider(M)⇒∃M′:Decider(M′) ∧ L(M′)=Σ*∖L(M)

**assumptions:** Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded.

**ruleRole:** derived-result

**proofSketch:** Preserve all transitions and swap which halting state is called accepting and rejecting. Every run still halts, so its former nonaccepting outcome is exactly its new accepting outcome. Without total halting, divergence would remain unaccepted.

**dependsOn:** [finite-control](TuringMachine.md#node-urn-csabs-axiom-TuringMachine-finite-control); [machine-step](TuringMachine.md#node-urn-csabs-axiom-TuringMachine-machine-step); [recognition-decision](TuringMachine.md#node-urn-csabs-axiom-TuringMachine-recognition-decision)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 5](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/18c8cd00b14d48dc5865f3bdc41abd76_MIT18_404f20_lec5.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8, 10–11: tape convention, TM definition, recognizers and deciders

**sourceNote:** Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-TuringMachine-run-trichotomy"></a>

### run-trichotomy

`urn:csabs:theorem/TuringMachine-run-trichotomy`

**statement:** Each input is accepted, rejected by halting, or has a unique infinite run, with exactly one of these outcomes.

**description:** Each input is accepted, rejected by halting, or has a unique infinite run, with exactly one of these outcomes.

**formalStatement:** ∀w∈Σ*: exactly one of [run_M(w) reaches qacc; run_M(w) reaches qrej; run_M(w) never halts]

**assumptions:** Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀,qacc,qrej∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded. States and symbols use identity equality; machine identity differs from accepted-language equality.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 5](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/18c8cd00b14d48dc5865f3bdc41abd76_MIT18_404f20_lec5.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8, 10–11: tape convention, TM definition, recognizers and deciders

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Step determinism gives a unique finite prefix at every stage before halting. Halting states have no successors and are distinct, so the two halting outcomes cannot both occur. If neither is ever reached, totality supplies a successor at every finite stage and recursion gives an infinite run.

**dependsOn:** [finite-control](TuringMachine.md#node-urn-csabs-axiom-TuringMachine-finite-control); [machine-step](TuringMachine.md#node-urn-csabs-axiom-TuringMachine-machine-step); [recognition-decision](TuringMachine.md#node-urn-csabs-axiom-TuringMachine-recognition-decision); [initial-configuration](TuringMachine.md#node-urn-csabs-axiom-TuringMachine-initial-configuration); [step-determinism](TuringMachine.md#node-urn-csabs-law-TuringMachine-step-determinism); [induction-schema](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-induction-schema)

<a id="node-urn-csabs-theorem-TuringMachine-outcome-domain"></a>

### outcome-domain

`urn:csabs:theorem/TuringMachine-outcome-domain`

**statement:** The partial outcome function is total precisely for deciders.

**description:** The partial outcome function is total precisely for deciders.

**formalStatement:** dom(outcome_M)=Σ* iff Decider(M)

**assumptions:** Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀,qacc,qrej∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded. States and symbols use identity equality; machine identity differs from accepted-language equality.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 5](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/18c8cd00b14d48dc5865f3bdc41abd76_MIT18_404f20_lec5.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8, 10–11: tape convention, TM definition, recognizers and deciders

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** By definition outcome is defined exactly when the run halts. The decider definition requires this for every input; the trichotomy separates nonhalting inputs from either halting outcome.

**dependsOn:** [recognition-decision](TuringMachine.md#node-urn-csabs-axiom-TuringMachine-recognition-decision); [run-trichotomy](TuringMachine.md#node-urn-csabs-theorem-TuringMachine-run-trichotomy); [outcome](TuringMachine.md#node-urn-csabs-operation-TuringMachine-outcome)

## Concept provenance

- [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 5](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/18c8cd00b14d48dc5865f3bdc41abd76_MIT18_404f20_lec5.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8, 10–11: tape convention, TM definition, recognizers and deciders

**sourceNote:** Makes halting states absorbing outcomes with no outgoing machine steps. A left move at cell zero stays there; the consulted one-sided tape presentation is used.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/TuringMachine",
    "type": "Concept",
    "shortForm": "TuringMachine",
    "fullName": "Deterministic one-tape Turing machine",
    "category": [
      "urn:csabs:category/languages-computation",
      "urn:csabs:category/programming-semantics"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A finite controller reads and writes an unbounded one-sided tape, moving its head one cell per step until it accepts, rejects, or runs forever.",
    "notation": "M=(Q,Σ,Γ,δ,q₀,qacc,qrej); δ:(Q∖{qacc,qrej})×Γ→Q×Γ×{L,R}",
    "hasOperation": [
      "urn:csabs:operation/TuringMachine-step",
      "urn:csabs:operation/TuringMachine-outcome",
      "urn:csabs:operation/TuringMachine-initialConfiguration"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/TuringMachine-finite-control",
      "urn:csabs:axiom/TuringMachine-machine-step",
      "urn:csabs:axiom/TuringMachine-recognition-decision",
      "urn:csabs:axiom/TuringMachine-initial-configuration"
    ],
    "hasLaw": [
      "urn:csabs:law/TuringMachine-step-determinism"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/TuringMachine-decider-complement",
      "urn:csabs:theorem/TuringMachine-run-trichotomy",
      "urn:csabs:theorem/TuringMachine-outcome-domain"
    ],
    "requiresConcept": [
      "urn:csabs:concept/FormalLanguage",
      "urn:csabs:concept/TransitionSystem",
      "urn:csabs:concept/PartialFunction"
    ],
    "relatedConcept": [
      "urn:csabs:concept/DFA"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Selected defining presentation: The finite control and alphabets determine a total table on nonhalting states. The finite transition table gives a unique next configuration outside the two halting states. Recognition means eventual acceptance; a decider halts on every input. Input is written once at the left end and the remaining tape is blank.",
    "basisKind": "defined-structure",
    "basisScope": "Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀,qacc,qrej∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded. States and symbols use identity equality; machine identity differs from accepted-language equality.",
    "source": [
      "urn:csabs:source/sipser-turing-machines"
    ],
    "sourceLocator": "Slides 8, 10–11: tape convention, TM definition, recognizers and deciders",
    "sourceNote": "Makes halting states absorbing outcomes with no outgoing machine steps. A left move at cell zero stays there; the consulted one-sided tape presentation is used.",
    "provenanceKind": "adapted",
    "reviewStatus": "editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof",
    "verificationObligation": [
      "Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀,qacc,qrej∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded. States and symbols use identity equality; machine identity differs from accepted-language equality."
    ]
  },
  {
    "id": "urn:csabs:operation/TuringMachine-step",
    "type": "Operation",
    "name": "step",
    "signature": "step_M : Config(M) ⇀ Config(M)",
    "description": "Updates the scanned cell, control state, and head position.",
    "concept": "urn:csabs:concept/TuringMachine",
    "precondition": "Current control state is neither qacc nor qrej.",
    "totality": "partial: defined on exactly the nonhalting configurations",
    "postcondition": "Updates the scanned cell, control state, and head position."
  },
  {
    "id": "urn:csabs:operation/TuringMachine-outcome",
    "type": "Operation",
    "name": "outcome",
    "signature": "outcome_M : Σ* ⇀ {accept,reject}",
    "description": "Returns the halting outcome if it occurs; divergence is outside its defined domain.",
    "concept": "urn:csabs:concept/TuringMachine",
    "precondition": "The run on the input halts.",
    "totality": "partial: defined exactly for halting inputs; no general decision procedure for definedness is asserted",
    "postcondition": "Returns the halting outcome if it occurs; divergence is outside its defined domain."
  },
  {
    "id": "urn:csabs:operation/TuringMachine-initialConfiguration",
    "type": "Operation",
    "name": "initialConfiguration",
    "signature": "init_M : Σ*→Config(M)",
    "description": "Places w in cells 0 through |w|−1, blanks elsewhere, with head 0 and control q₀.",
    "concept": "urn:csabs:concept/TuringMachine",
    "precondition": "Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀,qacc,qrej∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded. States and symbols use identity equality; machine identity differs from accepted-language equality.",
    "postcondition": "Places w in cells 0 through |w|−1, blanks elsewhere, with head 0 and control q₀.",
    "totality": "total mathematical operation on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/TuringMachine-finite-control",
    "type": "Axiom",
    "name": "finite-control",
    "statement": "The finite control and alphabets determine a total table on nonhalting states.",
    "description": "The model includes a distinguished blank and two distinct halting states.",
    "formalStatement": "Q,Σ,Γ finite; q₀,qacc,qrej∈Q; qacc≠qrej; blank∈Γ; Σ⊆Γ∖{blank}; δ:(Q∖{qacc,qrej})×Γ→Q×Γ×{L,R}",
    "assumptions": [
      "Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀,qacc,qrej∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded. States and symbols use identity equality; machine identity differs from accepted-language equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/TuringMachine"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-turing-machines"
    ],
    "sourceLocator": "Slides 8, 10–11: tape convention, TM definition, recognizers and deciders",
    "sourceNote": "Makes halting states absorbing outcomes with no outgoing machine steps. A left move at cell zero stays there; the consulted one-sided tape presentation is used. Table entries at halting states are omitted because they are never executed.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/TuringMachine-machine-step",
    "type": "Axiom",
    "name": "machine-step",
    "statement": "The finite transition table gives a unique next configuration outside the two halting states.",
    "description": "The finite transition table gives a unique next configuration outside the two halting states.",
    "formalStatement": "Config=(q,t,h), h∈ℕ, t:ℕ→Γ eventually blank; δ(q,t(h))=(q′,b,d) ⇒ step(q,t,h)=(q′,t[h↦b], if d=R then h+1 else max(0,h−1)); step undefined at qacc,qrej",
    "assumptions": [
      "Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded."
    ],
    "appliesTo": [
      "urn:csabs:concept/TuringMachine"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-turing-machines"
    ],
    "sourceLocator": "Slides 8, 10–11: tape convention, TM definition, recognizers and deciders",
    "sourceNote": "Makes halting states absorbing outcomes with no outgoing machine steps. A left move at cell zero stays there; the consulted one-sided tape presentation is used. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/TuringMachine-recognition-decision",
    "type": "Axiom",
    "name": "recognition-decision",
    "statement": "Recognition means eventual acceptance; a decider halts on every input.",
    "description": "Recognition means eventual acceptance; a decider halts on every input.",
    "formalStatement": "L(M)={w:the unique run from init(w) reaches qacc}; Decider(M) iff ∀w∈Σ*:run_M(w) reaches qacc or qrej",
    "assumptions": [
      "Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded."
    ],
    "appliesTo": [
      "urn:csabs:concept/TuringMachine"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-turing-machines"
    ],
    "sourceLocator": "Slides 8, 10–11: tape convention, TM definition, recognizers and deciders",
    "sourceNote": "Makes halting states absorbing outcomes with no outgoing machine steps. A left move at cell zero stays there; the consulted one-sided tape presentation is used. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/TuringMachine-initial-configuration",
    "type": "Axiom",
    "name": "initial-configuration",
    "statement": "Input is written once at the left end and the remaining tape is blank.",
    "description": "Input is written once at the left end and the remaining tape is blank.",
    "formalStatement": "init_M(w)=(q₀,t_w,0); t_w(i)=w_i if i<|w|, otherwise blank",
    "assumptions": [
      "Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀,qacc,qrej∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded. States and symbols use identity equality; machine identity differs from accepted-language equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/TuringMachine"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-turing-machines"
    ],
    "sourceLocator": "Lecture 5, slides 8–10: one-sided tape and input conventions",
    "sourceNote": "Specifies additional equations for the selected abstract interface; local conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/TuringMachine-step-determinism",
    "type": "Law",
    "name": "step-determinism",
    "statement": "Each nonhalting configuration has exactly one successor; halting configurations have none.",
    "description": "Each nonhalting configuration has exactly one successor; halting configurations have none.",
    "formalStatement": "q∉{qacc,qrej}⇒∃!c′:step_M(q,t,h)=c′; q∈{qacc,qrej}⇒step_M(q,t,h) undefined",
    "assumptions": [
      "Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀,qacc,qrej∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded. States and symbols use identity equality; machine identity differs from accepted-language equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/TuringMachine"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-turing-machines"
    ],
    "sourceLocator": "Slides 8, 10–11: tape convention, TM definition, recognizers and deciders",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "The table is a total function on nonhalting control and scanned symbols. A finite tape update and the boundary movement rule determine one successor. The step definition explicitly excludes halting states.",
    "dependsOn": [
      "urn:csabs:axiom/TuringMachine-finite-control",
      "urn:csabs:axiom/TuringMachine-machine-step",
      "urn:csabs:axiom/TuringMachine-recognition-decision",
      "urn:csabs:axiom/TuringMachine-initial-configuration"
    ]
  },
  {
    "id": "urn:csabs:theorem/TuringMachine-decider-complement",
    "type": "Theorem",
    "name": "decider-complement",
    "statement": "Swapping the two halting outcomes of a decider decides the complementary language.",
    "description": "Swapping the two halting outcomes of a decider decides the complementary language.",
    "formalStatement": "Decider(M)⇒∃M′:Decider(M′) ∧ L(M′)=Σ*∖L(M)",
    "assumptions": [
      "Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded."
    ],
    "appliesTo": [
      "urn:csabs:concept/TuringMachine"
    ],
    "ruleRole": "derived-result",
    "proofSketch": "Preserve all transitions and swap which halting state is called accepting and rejecting. Every run still halts, so its former nonaccepting outcome is exactly its new accepting outcome. Without total halting, divergence would remain unaccepted.",
    "dependsOn": [
      "urn:csabs:axiom/TuringMachine-finite-control",
      "urn:csabs:axiom/TuringMachine-machine-step",
      "urn:csabs:axiom/TuringMachine-recognition-decision"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-turing-machines"
    ],
    "sourceLocator": "Slides 8, 10–11: tape convention, TM definition, recognizers and deciders",
    "sourceNote": "Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/TuringMachine-run-trichotomy",
    "type": "Theorem",
    "name": "run-trichotomy",
    "statement": "Each input is accepted, rejected by halting, or has a unique infinite run, with exactly one of these outcomes.",
    "description": "Each input is accepted, rejected by halting, or has a unique infinite run, with exactly one of these outcomes.",
    "formalStatement": "∀w∈Σ*: exactly one of [run_M(w) reaches qacc; run_M(w) reaches qrej; run_M(w) never halts]",
    "assumptions": [
      "Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀,qacc,qrej∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded. States and symbols use identity equality; machine identity differs from accepted-language equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/TuringMachine"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-turing-machines"
    ],
    "sourceLocator": "Slides 8, 10–11: tape convention, TM definition, recognizers and deciders",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Step determinism gives a unique finite prefix at every stage before halting. Halting states have no successors and are distinct, so the two halting outcomes cannot both occur. If neither is ever reached, totality supplies a successor at every finite stage and recursion gives an infinite run.",
    "dependsOn": [
      "urn:csabs:axiom/TuringMachine-finite-control",
      "urn:csabs:axiom/TuringMachine-machine-step",
      "urn:csabs:axiom/TuringMachine-recognition-decision",
      "urn:csabs:axiom/TuringMachine-initial-configuration",
      "urn:csabs:law/TuringMachine-step-determinism",
      "urn:csabs:axiom/NaturalNumber-induction-schema"
    ]
  },
  {
    "id": "urn:csabs:theorem/TuringMachine-outcome-domain",
    "type": "Theorem",
    "name": "outcome-domain",
    "statement": "The partial outcome function is total precisely for deciders.",
    "description": "The partial outcome function is total precisely for deciders.",
    "formalStatement": "dom(outcome_M)=Σ* iff Decider(M)",
    "assumptions": [
      "Finite Q,Γ,Σ; Σ⊆Γ∖{blank}; qacc≠qrej and q₀,qacc,qrej∈Q. Tape cells indexed by ℕ are initially the input followed by blanks. Exact symbolic computation has no finite-memory overflow; runtime and tape use are unbounded. States and symbols use identity equality; machine identity differs from accepted-language equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/TuringMachine"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-turing-machines"
    ],
    "sourceLocator": "Slides 8, 10–11: tape convention, TM definition, recognizers and deciders",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "By definition outcome is defined exactly when the run halts. The decider definition requires this for every input; the trichotomy separates nonhalting inputs from either halting outcome.",
    "dependsOn": [
      "urn:csabs:axiom/TuringMachine-recognition-decision",
      "urn:csabs:theorem/TuringMachine-run-trichotomy",
      "urn:csabs:operation/TuringMachine-outcome"
    ]
  }
]
```
<!-- graph-record:end -->
