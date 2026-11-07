module

public import Mathlib.Computability.DFA
public import Mathlib.Computability.NFA
public import Mathlib.Computability.ContextFreeGrammar
public import Mathlib.Logic.Relation

@[expose] public section

namespace Catalog
universe u v

abbrev FormalLanguage (A : Type u) := Language A
abbrev DFA (A : Type u) (Q : Type v) [Fintype A] [Fintype Q] := _root_.DFA A Q

/-- The catalog fixes one initial state, unlike Mathlib's general set of starts. -/
structure NFA (A : Type u) (Q : Type v) [Fintype A] [Fintype Q]
    extends _root_.NFA A Q where
  single_initial : ∃ q, start = {q}

def RegularLanguage {A : Type u} [Fintype A] (L : Language A) : Prop := L.IsRegular

structure ContextFreeGrammar (A : Type) [Fintype A] where
  grammar : _root_.ContextFreeGrammar A
  finite_nonterminals : Finite grammar.NT

inductive TapeMove where
  | left | right

/-- Deterministic finite-control, one-tape machine with distinguished halting
states. At the left boundary a left move stays at zero. -/
structure TuringMachine (Q Γ : Type) [Fintype Q] [Fintype Γ] where
  start : Q
  accept : Q
  reject : Q
  distinct_halts : accept ≠ reject
  blank : Γ
  inputAlphabet : Finset Γ
  blank_not_input : blank ∉ inputAlphabet
  transition : {q : Q // q ≠ accept ∧ q ≠ reject} → Γ → Q × Γ × TapeMove

structure MachineConfig (Q Γ : Type) where
  state : Q
  head : Nat
  tape : Nat → Γ

def TuringMachine.step {Q Γ : Type} [Fintype Q] [Fintype Γ] [DecidableEq Q]
    (m : TuringMachine Q Γ) (c : MachineConfig Q Γ) : Option (MachineConfig Q Γ) :=
  if h : c.state ≠ m.accept ∧ c.state ≠ m.reject then
    let (q, symbol, move) := m.transition ⟨c.state, h⟩ (c.tape c.head)
    some ⟨q, match move with | .left => c.head - 1 | .right => c.head + 1,
      fun i => if i = c.head then symbol else c.tape i⟩
  else none

def TuringMachine.initial {Q Γ : Type} [Fintype Q] [Fintype Γ]
    (m : TuringMachine Q Γ) (input : List {x : Γ // x ∈ m.inputAlphabet}) : MachineConfig Q Γ :=
  ⟨m.start, 0, fun i => ((input[i]?).map Subtype.val).getD m.blank⟩

end Catalog
