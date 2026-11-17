module

public import Mathlib.Order.CompleteLattice.Basic
public import Mathlib.Data.Int.Basic
public import Mathlib.Data.Fintype.Basic
public import Mathlib.Logic.Relation

@[expose] public section

namespace Catalog.Programs
universe u v

structure ControlFlowGraph (V : Type u) [Fintype V] where
  edge : V → V → Prop
  entry : V
  exit : V
  distinct : entry ≠ exit
  uniqueSource : ∀ v, (¬ ∃ u, edge u v) ↔ v = entry
  uniqueSink : ∀ v, (¬ ∃ w, edge v w) ↔ v = exit

structure MonotoneDataflow (V : Type u) (L : Type v) [Fintype V] [CompleteLattice L] where
  edge : V → V → Prop
  boundary : V → L
  transfer : V → V → L → L
  monotone : ∀ u v, edge u v → Monotone (transfer u v)

noncomputable def MonotoneDataflow.step {V : Type u} {L : Type v}
    [Fintype V] [CompleteLattice L] (d : MonotoneDataflow V L) (x : V → L) : V → L :=
  fun v => d.boundary v ⊔ ⨆ u, ⨆ (_ : d.edge u v), d.transfer u v (x u)

/-- Extensional integer intervals include empty and unbounded convex sets. -/
def IntervalDomain :=
  {s : Set Int // ∀ a ∈ s, ∀ b ∈ s, ∀ c : Int, a ≤ c → c ≤ b → c ∈ s}

structure RewriteSystem (A : Type u) where
  step : A → A → Prop

def RewriteSystem.reduces {A : Type u} (r : RewriteSystem A) : A → A → Prop :=
  Relation.ReflTransGen r.step

def RewriteSystem.normalForm {A : Type u} (r : RewriteSystem A) (a : A) : Prop :=
  ¬ ∃ b, r.step a b

structure EffectAlgebra (E : Type u) where
  join : E → E → E
  sequence : E → E → E
  identity : E
  joinAssoc : ∀ a b c, join (join a b) c = join a (join b c)
  joinComm : ∀ a b, join a b = join b a
  joinIdem : ∀ a, join a a = a
  seqAssoc : ∀ a b c, sequence (sequence a b) c = sequence a (sequence b c)
  leftIdentity : ∀ a, sequence identity a = a
  rightIdentity : ∀ a, sequence a identity = a
  leftDistrib : ∀ a b c, sequence a (join b c) = join (sequence a b) (sequence a c)
  rightDistrib : ∀ a b c, sequence (join a b) c = join (sequence a c) (sequence b c)

def EffectAlgebra.subeffect {E : Type u} (e : EffectAlgebra E) (a b : E) : Prop :=
  e.join a b = b

/-- Finite acyclic functional graph, oriented child to parent. -/
structure SingleParentForest (V : Type u) [Fintype V] where
  parent : V → Option V
  acyclic : ∀ v, ¬ Relation.TransGen (fun x y => parent x = some y) v v

end Catalog.Programs
