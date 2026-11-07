module

public import Mathlib.Order.Closure
public import Mathlib.Order.GaloisConnection.Defs
public import Mathlib.Order.BooleanAlgebra.Defs
public import Mathlib.Order.WellFoundedSet

@[expose] public section

namespace Catalog
universe u v

abbrev Preorder (A : Type u) := _root_.Preorder A
abbrev PartialOrder (A : Type u) := _root_.PartialOrder A
abbrev TotalOrder (A : Type u) := LinearOrder A
abbrev Lattice (A : Type u) := _root_.Lattice A
abbrev CompleteLattice (A : Type u) := _root_.CompleteLattice A
abbrev BooleanAlgebra (A : Type u) := _root_.BooleanAlgebra A
abbrev ClosureOperator (A : Type u) [_root_.PartialOrder A] := _root_.ClosureOperator A
abbrev MonotoneFunction (A : Type u) (B : Type v)
    [_root_.Preorder A] [_root_.Preorder B] := A →o B

def GaloisConnection {A : Type u} {B : Type v}
    [_root_.PartialOrder A] [_root_.PartialOrder B] (l : A → B) (r : B → A) : Prop :=
  _root_.GaloisConnection l r

def FixedPoint {A : Type u} (f : A → A) (x : A) : Prop := f x = x
def WellFoundedRelation {A : Type u} (r : A → A → Prop) : Prop := WellFounded r

end Catalog
