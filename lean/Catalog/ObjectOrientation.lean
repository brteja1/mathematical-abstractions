module

public import Catalog.StructuredData
public import Catalog.Semantics

@[expose] public section

namespace Catalog.OOP
universe u v w x

abbrev Ref := Option PNat
abbrev Value (Primitive : Type u) := Sum Primitive Ref
abbrev ObjectRecord (Class : Type u) (Field : Type v) (Primitive : Type w) :=
  Class × Catalog.Map Field (Value Primitive)
abbrev ObjectHeap (Class : Type u) (Field : Type v) (Primitive : Type w) :=
  Catalog.HeapStore (ObjectRecord Class Field Primitive)

namespace ObjectHeap
def classOf {C : Type u} {F : Type v} {P : Type w}
    (h : ObjectHeap C F P) (r : Ref) : Option C :=
  match r with
  | none => none
  | some a => match h.lookup a with
    | none => none
    | some object => some object.1

def readField {C : Type u} {F : Type v} {P : Type w}
    (h : ObjectHeap C F P) (r : Ref) (f : F) : Option (Value P) :=
  match r with
  | none => none
  | some a => match h.lookup a with
    | none => none
    | some object => object.2.lookup f

noncomputable def writeField {C : Type u} {F : Type v} {P : Type w}
    (h : ObjectHeap C F P) (r : Ref) (f : F) (value : Value P) :
    Option (ObjectHeap C F P) :=
  match r with
  | none => none
  | some a => match h.lookup a with
    | none => none
    | some object => match object.2.lookup f with
      | none => none
      | some _ => some (Catalog.finiteMapSet h a (object.1, Catalog.finiteMapSet object.2 f value))

def sameRef (r s : Ref) : Bool := decide (r = s)

def aliases {C : Type u} {F : Type v} {P : Type w}
    (h : ObjectHeap C F P) (r s : Ref) : Prop :=
  ∃ a, (h.lookup a).isSome ∧ r = some a ∧ s = some a
end ObjectHeap

/-- Rank certifies acyclicity; it is auxiliary evidence, not a class observation. -/
structure ClassTable (n : Nat) (Selector : Type u) (Body : Type v) where
  root : Fin (n + 1)
  parent : Fin (n + 1) → Option (Fin (n + 1))
  root_parent : parent root = none
  has_parent : ∀ c, c ≠ root → (parent c).isSome
  rank : Fin (n + 1) → Nat
  parent_decreases : ∀ c d, parent c = some d → rank d < rank c
  methods : Fin (n + 1) → Catalog.Map Selector Body

namespace ClassTable
def ancestorsAux {n : Nat} {M : Type u} {B : Type v}
    (table : ClassTable n M B) : Nat → Fin (n + 1) → List (Fin (n + 1))
  | 0, _ => []
  | fuel + 1, c => c :: match table.parent c with
    | none => []
    | some p => ancestorsAux table fuel p

def ancestors {n : Nat} {M : Type u} {B : Type v}
    (table : ClassTable n M B) (c : Fin (n + 1)) := table.ancestorsAux (n + 1) c

def nominalSubtype {n : Nat} {M : Type u} {B : Type v}
    (table : ClassTable n M B) (c d : Fin (n + 1)) : Prop := d ∈ table.ancestors c

def lookupAux {n : Nat} {M : Type u} {B : Type v}
    (table : ClassTable n M B) : Nat → Fin (n + 1) → M → Option B
  | 0, _, _ => none
  | fuel + 1, c, m => match (table.methods c).lookup m with
    | some body => some body
    | none => match table.parent c with
      | none => none
      | some p => lookupAux table fuel p m

def lookup {n : Nat} {M : Type u} {B : Type v}
    (table : ClassTable n M B) (c : Fin (n + 1)) (m : M) : Option B :=
  table.lookupAux (n + 1) c m

def dispatch {n : Nat} {M : Type u} {B : Type v} {F : Type w} {P : Type x}
    (table : ClassTable n M B) (h : ObjectHeap (Fin (n + 1)) F P)
    (r : Ref) (m : M) : Option B :=
  match ObjectHeap.classOf h r with
  | none => none
  | some c => table.lookup c m
end ClassTable

abbrev Store (Location : Type u) (Val : Type v) := Location → Val
abbrev Outcome (Result : Type u) (Exception : Type v) := Sum Result Exception

structure MethodTrace (L : Type u) (V : Type v) (O : Type w) where
  after : Store L V
  outcome : O
  writes : Set L

structure MethodContract (L : Type u) (V : Type v) (I : Type w) (O : Type x) where
  pre : Store L V → I → Prop
  post : Store L V → I → Store L V → O → Prop
  writable : Store L V → I → Set L

namespace MethodContract
def allows {L : Type u} {V : Type v} {I : Type w} {O : Type x}
    (contract : MethodContract L V I O) (before : Store L V) (input : I)
    (trace : MethodTrace L V O) : Prop :=
  contract.pre before input ∧ contract.post before input trace.after trace.outcome ∧
  trace.writes ⊆ contract.writable before input ∧
  ∀ l, l ∉ trace.writes → trace.after l = before l

def satisfies {L : Type u} {V : Type v} {I : Type w} {O : Type x}
    (contract : MethodContract L V I O)
    (exec : Store L V → I → MethodTrace L V O → Prop) : Prop :=
  ∀ before input trace, contract.pre before input → exec before input trace →
    contract.allows before input trace

def covered {L : Type u} {V : Type v} {I : Type w} {O : Type x}
    (contract : MethodContract L V I O) : Prop :=
  ∀ before input, contract.pre before input → ∃ trace, contract.allows before input trace
end MethodContract

/-- Receiver-preserving visible-boundary protocol, with explicit establishment
and preservation hypotheses. No invariant is asserted at hidden instructions. -/
structure ObjectInvariant (C : Type u) (F : Type v) (P : Type w) where
  predicate : ObjectHeap C F P → PNat → Prop
  initial : ObjectHeap C F P × PNat → Prop
  boundary : (ObjectHeap C F P × PNat) → (ObjectHeap C F P × PNat) → Prop
  receiver_stable : ∀ a b, boundary a b → a.2 = b.2
  establishes : ∀ h a, initial (h, a) → (h.lookup a).isSome ∧ predicate h a
  preserves : ∀ h a k b, (h.lookup a).isSome ∧ predicate h a →
    boundary (h, a) (k, b) → (k.lookup b).isSome ∧ predicate k b

namespace ObjectInvariant
def holds {C : Type u} {F : Type v} {P : Type w}
    (protocol : ObjectInvariant C F P) (h : ObjectHeap C F P) (a : PNat) : Prop :=
  (h.lookup a).isSome ∧ protocol.predicate h a

def reachable {C : Type u} {F : Type v} {P : Type w}
    (protocol : ObjectInvariant C F P) (target : ObjectHeap C F P × PNat) : Prop :=
  ∃ start, protocol.initial start ∧ Relation.ReflTransGen protocol.boundary start target
end ObjectInvariant

/-- All history pairs are explicit in this specification, not inferred from
nominal inheritance or inferred from an implementation's method names. -/
structure BehavioralSpec (S : Type u) (M : Type v) (I : Type w) (O : Type x) where
  invariant : S → Prop
  available : Set M
  pre : M → S → I → Prop
  post : M → S → I → S → O → Prop
  constraint : S → S → Prop
  historyPair : S → S → Prop
  history_valid : ∀ s t, historyPair s t → invariant s ∧ invariant t ∧ constraint s t
  method_preserves : ∀ m s i t o, m ∈ available → invariant s → pre m s i →
    post m s i t o → invariant t

def BehavioralSubtyping {S T : Type u} {MS MT : Type v} {I : Type w} {O : Type x}
    (sub : BehavioralSpec S MS I O) (sup : BehavioralSpec T MT I O)
    (abstract : S → T) (rename : MT → MS) : Prop :=
  (∀ s, sub.invariant s → sup.invariant (abstract s)) ∧
  (∀ m, m ∈ sup.available → rename m ∈ sub.available) ∧
  (∀ m s i, m ∈ sup.available → sub.invariant s → sup.pre m (abstract s) i →
    sub.pre (rename m) s i ∧ ∀ t o, sub.post (rename m) s i t o →
      sub.invariant t ∧ sup.post m (abstract s) i (abstract t) o) ∧
  (∀ s t, sub.invariant s → sub.invariant t → sub.constraint s t →
    sup.constraint (abstract s) (abstract t))

abbrev HeapSeparation (V : Type u) := Catalog.HeapStore V → Prop

namespace HeapSeparation
def disjoint {V : Type u} (h k : Catalog.HeapStore V) : Prop :=
  ∀ a, (h.lookup a).isSome → k.lookup a = none

/-- Relational graph of partial merge; overlap is excluded even for equal values. -/
def merges {V : Type u} (h k out : Catalog.HeapStore V) : Prop :=
  disjoint h k ∧ ∀ a, out.lookup a = match h.lookup a with
    | some value => some value
    | none => k.lookup a

def emp {V : Type u} : HeapSeparation V := fun h => ∀ a, h.lookup a = none

def pointsTo {V : Type u} (a : PNat) (value : V) : HeapSeparation V :=
  fun h => ∀ b, h.lookup b = if b = a then some value else none

def star {V : Type u} (p q : HeapSeparation V) : HeapSeparation V :=
  fun h => ∃ left right, merges left right h ∧ p left ∧ q right
end HeapSeparation

end Catalog.OOP
