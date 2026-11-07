module

public import Mathlib.Data.Set.Basic

@[expose] public section

namespace Catalog
universe u v w

inductive PropFormula (AP : Type u) where
  | atom : AP → PropFormula AP
  | bottom : PropFormula AP
  | neg : PropFormula AP → PropFormula AP
  | conj : PropFormula AP → PropFormula AP → PropFormula AP

def PropositionalLogic {AP : Type u} (valuation : AP → Bool) : PropFormula AP → Bool
  | .atom p => valuation p
  | .bottom => false
  | .neg p => !(PropositionalLogic valuation p)
  | .conj p q => PropositionalLogic valuation p && PropositionalLogic valuation q

inductive ModalFormula (AP : Type u) where
  | atom : AP → ModalFormula AP
  | bottom : ModalFormula AP
  | neg : ModalFormula AP → ModalFormula AP
  | conj : ModalFormula AP → ModalFormula AP → ModalFormula AP
  | box : ModalFormula AP → ModalFormula AP

def ModalLogic {AP : Type u} {W : Type v} (r : W → W → Prop)
    (valuation : W → AP → Prop) : ModalFormula AP → W → Prop
  | .atom p, s => valuation s p
  | .bottom, _ => False
  | .neg p, s => ¬ ModalLogic r valuation p s
  | .conj p q, s => ModalLogic r valuation p s ∧ ModalLogic r valuation q s
  | .box p, s => ∀ t, r s t → ModalLogic r valuation p t

inductive TemporalFormula (AP : Type u) where
  | atom : AP → TemporalFormula AP
  | bottom : TemporalFormula AP
  | neg : TemporalFormula AP → TemporalFormula AP
  | conj : TemporalFormula AP → TemporalFormula AP → TemporalFormula AP
  | next : TemporalFormula AP → TemporalFormula AP
  | until : TemporalFormula AP → TemporalFormula AP → TemporalFormula AP

def LinearTemporalLogic {AP : Type u} (trace : Nat → AP → Prop) :
    TemporalFormula AP → Nat → Prop
  | .atom p, i => trace i p
  | .bottom, _ => False
  | .neg p, i => ¬ LinearTemporalLogic trace p i
  | .conj p q, i => LinearTemporalLogic trace p i ∧ LinearTemporalLogic trace q i
  | .next p, i => LinearTemporalLogic trace p (i + 1)
  | .until p q, i => ∃ j, i ≤ j ∧ LinearTemporalLogic trace q j ∧
      ∀ k, i ≤ k → k < j → LinearTemporalLogic trace p k

/-- Arity-indexed symbols and de Bruijn variables prevent malformed applications. -/
inductive FirstOrderTerm (Fn : Nat → Type u) where
  | var : Nat → FirstOrderTerm Fn
  | app (n : Nat) : Fn n → (Fin n → FirstOrderTerm Fn) → FirstOrderTerm Fn

inductive FirstOrderFormula (Fn : Nat → Type u) (Pred : Nat → Type v) where
  | atom (n : Nat) : Pred n → (Fin n → FirstOrderTerm Fn) → FirstOrderFormula Fn Pred
  | equal : FirstOrderTerm Fn → FirstOrderTerm Fn → FirstOrderFormula Fn Pred
  | bottom : FirstOrderFormula Fn Pred
  | neg : FirstOrderFormula Fn Pred → FirstOrderFormula Fn Pred
  | conj : FirstOrderFormula Fn Pred → FirstOrderFormula Fn Pred → FirstOrderFormula Fn Pred
  | all : FirstOrderFormula Fn Pred → FirstOrderFormula Fn Pred

def evalTerm {Fn : Nat → Type u} {D : Type w}
    (functions : ∀ n, Fn n → (Fin n → D) → D) (env : Nat → D) : FirstOrderTerm Fn → D
  | .var n => env n
  | .app n f args => functions n f (fun i => evalTerm functions env (args i))

def extendEnv {D : Type w} (env : Nat → D) (x : D) : Nat → D
  | 0 => x
  | n + 1 => env n

def PredicateLogic {Fn : Nat → Type u} {Pred : Nat → Type v} {D : Type w} [Nonempty D]
    (functions : ∀ n, Fn n → (Fin n → D) → D)
    (predicates : ∀ n, Pred n → (Fin n → D) → Prop) :
    FirstOrderFormula Fn Pred → (Nat → D) → Prop
  | .atom n p args, env => predicates n p (fun i => evalTerm functions env (args i))
  | .equal s t, env => evalTerm functions env s = evalTerm functions env t
  | .bottom, _ => False
  | .neg p, env => ¬ PredicateLogic functions predicates p env
  | .conj p q, env => PredicateLogic functions predicates p env ∧ PredicateLogic functions predicates q env
  | .all p, env => ∀ x, PredicateLogic functions predicates p (extendEnv env x)

end Catalog
