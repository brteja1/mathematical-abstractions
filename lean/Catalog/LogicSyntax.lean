module

public import Catalog.Logic

@[expose] public section

namespace Catalog
universe u v

/-- Countable tagged symbol supplies; the index is the symbol's finite arity. -/
structure FirstOrderSignature where
  functions : Nat → Set Nat
  relations : Nat → Set Nat

def PropFormula.substitute {AP : Type u} (σ : AP → PropFormula AP) :
    PropFormula AP → PropFormula AP
  | .atom a => σ a
  | .bottom => .bottom
  | .neg p => .neg (substitute σ p)
  | .conj p q => .conj (substitute σ p) (substitute σ q)

def PropFormula.atoms {AP : Type u} : PropFormula AP → Set AP
  | .atom a => {a}
  | .bottom => ∅
  | .neg p => atoms p
  | .conj p q => atoms p ∪ atoms q

/-- Raw named binders: equality retains the name, without an alpha quotient. -/
inductive NamedFirstOrderFormula (Fn : Nat → Type u) (Pred : Nat → Type v) where
  | atom (n : Nat) : Pred n → (Fin n → FirstOrderTerm Fn) → NamedFirstOrderFormula Fn Pred
  | equal : FirstOrderTerm Fn → FirstOrderTerm Fn → NamedFirstOrderFormula Fn Pred
  | bottom : NamedFirstOrderFormula Fn Pred
  | neg : NamedFirstOrderFormula Fn Pred → NamedFirstOrderFormula Fn Pred
  | conj : NamedFirstOrderFormula Fn Pred → NamedFirstOrderFormula Fn Pred → NamedFirstOrderFormula Fn Pred
  | all : Nat → NamedFirstOrderFormula Fn Pred → NamedFirstOrderFormula Fn Pred

def FirstOrderTerm.variables {Fn : Nat → Type u} : FirstOrderTerm Fn → Set Nat
  | .var x => {x}
  | .app _ _ args => {x | ∃ i, x ∈ (args i).variables}

def FirstOrderTerm.substitute {Fn : Nat → Type u} (t : FirstOrderTerm Fn) (x : Nat) :
    FirstOrderTerm Fn → FirstOrderTerm Fn
  | .var y => if y = x then t else .var y
  | .app n f args => .app n f (fun i => substitute t x (args i))

def NamedFirstOrderFormula.freeVariables {Fn : Nat → Type u} {Pred : Nat → Type v} :
    NamedFirstOrderFormula Fn Pred → Set Nat
  | .atom _ _ args => {x | ∃ i, x ∈ (args i).variables}
  | .equal s t => s.variables ∪ t.variables
  | .bottom => ∅
  | .neg p => p.freeVariables
  | .conj p q => p.freeVariables ∪ q.freeVariables
  | .all x p => p.freeVariables \ {x}

/-- A partial interface: rawSubstitute is used only with this free-for predicate. -/
def NamedFirstOrderFormula.freeFor {Fn : Nat → Type u} {Pred : Nat → Type v}
    (t : FirstOrderTerm Fn) (x : Nat) : NamedFirstOrderFormula Fn Pred → Prop
  | .atom _ _ _ => True
  | .equal _ _ => True
  | .bottom => True
  | .neg p => p.freeFor t x
  | .conj p q => p.freeFor t x ∧ q.freeFor t x
  | .all y p => y = x ∨ ((x ∈ p.freeVariables → y ∉ t.variables) ∧ p.freeFor t x)

/-- Internal raw replacement. Clients must establish freeFor to exclude capture. -/
def NamedFirstOrderFormula.rawSubstitute {Fn : Nat → Type u} {Pred : Nat → Type v}
    (t : FirstOrderTerm Fn) (x : Nat) : NamedFirstOrderFormula Fn Pred → NamedFirstOrderFormula Fn Pred
  | .atom n r args => .atom n r (fun i => FirstOrderTerm.substitute t x (args i))
  | .equal s u => .equal (FirstOrderTerm.substitute t x s) (FirstOrderTerm.substitute t x u)
  | .bottom => .bottom
  | .neg p => .neg (p.rawSubstitute t x)
  | .conj p q => .conj (p.rawSubstitute t x) (q.rawSubstitute t x)
  | .all y p => if y = x then .all y p else .all y (p.rawSubstitute t x)

/-- The definedness guard is part of the public substitution interface. -/
def NamedFirstOrderFormula.substitute {Fn : Nat → Type u} {Pred : Nat → Type v}
    (p : NamedFirstOrderFormula Fn Pred) (t : FirstOrderTerm Fn) (x : Nat)
    (_h : p.freeFor t x) : NamedFirstOrderFormula Fn Pred := p.rawSubstitute t x

/-- Finitary classical derivability; the constructors are rules, not global axioms. -/
inductive PropositionalDerivable {AP : Type u} : Set (PropFormula AP) → PropFormula AP → Prop
  | hyp {Γ p} : p ∈ Γ → PropositionalDerivable Γ p
  | weaken {Γ Δ p} : PropositionalDerivable Γ p → Γ ⊆ Δ → PropositionalDerivable Δ p
  | conjI {Γ p q} : PropositionalDerivable Γ p → PropositionalDerivable Γ q → PropositionalDerivable Γ (.conj p q)
  | conjL {Γ p q} : PropositionalDerivable Γ (.conj p q) → PropositionalDerivable Γ p
  | conjR {Γ p q} : PropositionalDerivable Γ (.conj p q) → PropositionalDerivable Γ q
  | negI {Γ p} : PropositionalDerivable (insert p Γ) .bottom → PropositionalDerivable Γ (.neg p)
  | negE {Γ p} : PropositionalDerivable Γ p → PropositionalDerivable Γ (.neg p) → PropositionalDerivable Γ .bottom
  | falseE {Γ p} : PropositionalDerivable Γ .bottom → PropositionalDerivable Γ p
  | reductio {Γ p} : PropositionalDerivable (insert (.neg p) Γ) .bottom → PropositionalDerivable Γ p

/-- Named-variable natural deduction, with substitution and eigenvariable guards. -/
inductive FirstOrderDerivable {Fn : Nat → Type u} {Pred : Nat → Type v} :
    Set (NamedFirstOrderFormula Fn Pred) → NamedFirstOrderFormula Fn Pred → Prop
  | hyp {Γ p} : p ∈ Γ → FirstOrderDerivable Γ p
  | weaken {Γ Δ p} : FirstOrderDerivable Γ p → Γ ⊆ Δ → FirstOrderDerivable Δ p
  | conjI {Γ p q} : FirstOrderDerivable Γ p → FirstOrderDerivable Γ q → FirstOrderDerivable Γ (.conj p q)
  | conjL {Γ p q} : FirstOrderDerivable Γ (.conj p q) → FirstOrderDerivable Γ p
  | conjR {Γ p q} : FirstOrderDerivable Γ (.conj p q) → FirstOrderDerivable Γ q
  | negI {Γ p} : FirstOrderDerivable (insert p Γ) .bottom → FirstOrderDerivable Γ (.neg p)
  | negE {Γ p} : FirstOrderDerivable Γ p → FirstOrderDerivable Γ (.neg p) → FirstOrderDerivable Γ .bottom
  | falseE {Γ p} : FirstOrderDerivable Γ .bottom → FirstOrderDerivable Γ p
  | reductio {Γ p} : FirstOrderDerivable (insert (.neg p) Γ) .bottom → FirstOrderDerivable Γ p
  | allI {Γ p x} : FirstOrderDerivable Γ p → (∀ q ∈ Γ, x ∉ q.freeVariables) → FirstOrderDerivable Γ (.all x p)
  | allE {Γ p x t} : FirstOrderDerivable Γ (.all x p) → p.freeFor t x → FirstOrderDerivable Γ (p.rawSubstitute t x)
  | eqI {Γ t} : FirstOrderDerivable Γ (.equal t t)
  | eqE {Γ} {p : NamedFirstOrderFormula Fn Pred} {x s t} : FirstOrderDerivable Γ (.equal s t) →
      FirstOrderDerivable Γ (p.rawSubstitute s x) → p.freeFor s x → p.freeFor t x →
      FirstOrderDerivable Γ (p.rawSubstitute t x)

end Catalog
