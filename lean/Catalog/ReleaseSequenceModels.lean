module

public import Mathlib.Data.List.Lex
public import Mathlib.Data.List.TakeDrop
public import Mathlib.Order.Sum.Order
public import Mathlib.Order.Prod.Lex.Basic
public import Mathlib.Order.Extension.Linear
public import Mathlib.Data.Finset.Card
public import Mathlib.Tactic

@[expose] public section

namespace Catalog

def versionChar (c : Nat) : Prop :=
  c = 45 ∨ (48 ≤ c ∧ c ≤ 57) ∨ (65 ≤ c ∧ c ≤ 90) ∨ (97 ≤ c ∧ c ≤ 122)

abbrev VersionText := {s : List Nat // s ≠ [] ∧ (∀ c ∈ s, versionChar c)}

abbrev VersionWord := {s : List Nat // s ≠ [] ∧ (∀ c ∈ s, versionChar c) ∧
  ∃ c ∈ s, ¬(48 ≤ c ∧ c ≤ 57)}

abbrev VersionIdentifier := Nat ⊕ₗ VersionWord

abbrev VersionPre := WithTop {s : List VersionIdentifier // s ≠ []}

abbrev VersionKey := Nat ×ₗ Nat ×ₗ Nat ×ₗ VersionPre

structure SemanticVersionOrder where
  key : VersionKey
  build : List VersionText

def versionLE (a b : SemanticVersionOrder) : Prop := a.key ≤ b.key

theorem version_model_satisfaction :
    (∀ a : SemanticVersionOrder, versionLE a a) ∧
    (∀ a b c, versionLE a b → versionLE b c → versionLE a c) ∧
    (∀ a b, versionLE a b ∨ versionLE b a) ∧
    (∀ a b, versionLE a b → versionLE b a → a.key = b.key) := by
  exact ⟨fun _ => le_rfl, fun _ _ _ => le_trans, fun _ _ => le_total _ _,
    fun _ _ => le_antisymm⟩

theorem version_build_invariance (k : VersionKey) (a b : List VersionText) :
    versionLE ⟨k, a⟩ ⟨k, b⟩ ∧ versionLE ⟨k, b⟩ ⟨k, a⟩ := ⟨le_rfl, le_rfl⟩

def deleteSpan (xs : List A) (i j : Nat) : List A := xs.take i ++ xs.drop j

theorem delete_span_length (xs : List A) (i j : Nat) (hij : i ≤ j)
    (hj : j ≤ xs.length) : (deleteSpan xs i j).length = xs.length - (j - i) := by
  simp [deleteSpan, List.length_take, List.length_drop, Nat.min_eq_left (le_trans hij hj)]
  omega

theorem delete_span_empty (xs : List A) (i : Nat) : deleteSpan xs i i = xs :=
  List.take_append_drop i xs

theorem delete_span_full (xs : List A) : deleteSpan xs 0 xs.length = [] := by
  simp [deleteSpan]

def replaceAll [DecidableEq A] (p : List A) (hp : p ≠ []) (r : List A)
    (xs : List A) : List A :=
  match xs with
  | [] => []
  | a :: tail =>
    if p <+: (a :: tail) then
      r ++ replaceAll p hp r ((a :: tail).drop p.length)
    else a :: replaceAll p hp r tail
termination_by xs.length
decreasing_by
  all_goals have hpos : 0 < p.length := List.length_pos_iff.mpr hp
  all_goals simp only [List.length_drop, List.length_cons]; omega

theorem replace_self [DecidableEq A] (p : List A) (hp : p ≠ []) (xs : List A) :
    replaceAll p hp p xs = xs := by
  rw [replaceAll.eq_def]
  split
  · rfl
  · rename_i a tail
    split
    · rename_i h
      rw [replace_self p hp]
      obtain ⟨t, ht⟩ := h
      rw [← ht]
      simp
    · rw [replace_self p hp]
termination_by xs.length
decreasing_by
  all_goals have hpos : 0 < p.length := List.length_pos_iff.mpr hp
  all_goals simp_all only [List.length_cons]
  all_goals try rw [List.length_drop]
  all_goals try simp only [List.length_cons] at *
  all_goals omega

theorem sequence_edit_model_satisfaction :
    replaceAll [1, 1] (by decide) [2] [1, 1, 1] = [2, 1] ∧
    replaceAll [1] (by decide) [1, 1] [1] = [1, 1] ∧
    deleteSpan [0, 1, 2, 3] 1 3 = [0, 3] := by
  simp [replaceAll.eq_def, deleteSpan]

theorem replace_equations [DecidableEq A] (p : List A) (hp : p ≠ []) (r : List A) :
    replaceAll p hp r [] = [] ∧
    (∀ a xs, p <+: (a :: xs) → replaceAll p hp r (a :: xs) =
      r ++ replaceAll p hp r ((a :: xs).drop p.length)) ∧
    (∀ a xs, ¬ p <+: (a :: xs) → replaceAll p hp r (a :: xs) =
      a :: replaceAll p hp r xs) := by
  refine ⟨?_, ?_, ?_⟩
  · rw [replaceAll.eq_def]
  · intro a xs h; rw [replaceAll.eq_def]; simp only [ite_eq_left h]
  · intro a xs h; rw [replaceAll.eq_def]; simp only [ite_eq_right h]

theorem replace_length_equal [DecidableEq A] (p : List A) (hp : p ≠ [])
    (r xs : List A) (hr : r.length = p.length) :
    (replaceAll p hp r xs).length = xs.length := by
  cases xs with
  | nil => rw [replaceAll.eq_def]
  | cons a tail =>
      rw [replaceAll.eq_def]
      dsimp only
      split
      · rename_i h
        rw [List.length_append, replace_length_equal p hp r _ hr]
        have hle := h.length_le
        simp only [List.length_drop, List.length_cons] at *
        omega
      · rw [List.length_cons, replace_length_equal p hp r tail hr]
        rfl
termination_by xs.length
decreasing_by
  all_goals have hpos : 0 < p.length := List.length_pos_iff.mpr hp
  all_goals simp only [List.length_drop, List.length_cons]; omega

structure MealyTransducer (Q I O : Type) [Fintype Q] [Fintype I] [Fintype O] where
  initial : Q
  next : Q → I → Q
  emit : Q → I → O

def mealyRun [Fintype Q] [Fintype I] [Fintype O] (m : MealyTransducer Q I O)
    (q : Q) : List I → Q × List O
  | [] => (q, [])
  | a :: xs => let z := mealyRun m (m.next q a) xs; (z.1, m.emit q a :: z.2)

theorem mealy_length [Fintype Q] [Fintype I] [Fintype O]
    (m : MealyTransducer Q I O) (q : Q) (xs : List I) :
    (mealyRun m q xs).2.length = xs.length := by
  induction xs generalizing q with
  | nil => rfl
  | cons a xs ih => simp [mealyRun, ih]

theorem mealy_append [Fintype Q] [Fintype I] [Fintype O]
    (m : MealyTransducer Q I O) (q : Q) (xs ys : List I) :
    mealyRun m q (xs ++ ys) =
      ((mealyRun m (mealyRun m q xs).1 ys).1,
       (mealyRun m q xs).2 ++ (mealyRun m (mealyRun m q xs).1 ys).2) := by
  induction xs generalizing q with
  | nil => rfl
  | cons a xs ih => simpa [mealyRun] using congrArg (fun z : Q × List O =>
      (z.1, m.emit q a :: z.2)) (ih (m.next q a))

def boolMealy : MealyTransducer Bool Bool Bool := ⟨false, fun _ a => a, fun q a => q != a⟩

theorem mealy_model_satisfaction :
    mealyRun boolMealy false [true, false] = (false, [true, true]) := by decide

theorem mealy_equations [Fintype Q] [Fintype I] [Fintype O]
    (m : MealyTransducer Q I O) (q : Q) :
    mealyRun m q [] = (q, []) ∧
    (∀ a xs, mealyRun m q (a :: xs) =
      ((mealyRun m (m.next q a) xs).1, m.emit q a :: (mealyRun m (m.next q a) xs).2)) :=
  ⟨rfl, fun _ _ => rfl⟩

structure MooreTransducer (Q I O : Type) [Fintype Q] [Fintype I] [Fintype O] where
  initial : Q
  next : Q → I → Q
  emit : Q → O

def mooreRun [Fintype Q] [Fintype I] [Fintype O] (m : MooreTransducer Q I O)
    (q : Q) : List I → Q × List O
  | [] => (q, [m.emit q])
  | a :: xs => let z := mooreRun m (m.next q a) xs; (z.1, m.emit q :: z.2)

theorem moore_length [Fintype Q] [Fintype I] [Fintype O]
    (m : MooreTransducer Q I O) (q : Q) (xs : List I) :
    (mooreRun m q xs).2.length = xs.length + 1 := by
  induction xs generalizing q with
  | nil => rfl
  | cons a xs ih => simp [mooreRun, ih]

def mooreAsMealy [Fintype Q] [Fintype I] [Fintype O] (m : MooreTransducer Q I O) :
    MealyTransducer Q I O := ⟨m.initial, m.next, fun q a => m.emit (m.next q a)⟩

theorem moore_mealy_alignment [Fintype Q] [Fintype I] [Fintype O]
    (m : MooreTransducer Q I O) (q : Q) (xs : List I) :
    (mooreRun m q xs).2 = m.emit q :: (mealyRun (mooreAsMealy m) q xs).2 := by
  induction xs generalizing q with
  | nil => rfl
  | cons a xs ih =>
      simpa only [mooreRun, mealyRun, mooreAsMealy] using
        congrArg (List.cons (m.emit q)) (ih (m.next q a))

def boolMoore : MooreTransducer Bool Bool Bool := ⟨false, fun _ a => a, id⟩

theorem moore_model_satisfaction :
    mooreRun boolMoore false [true, false] = (false, [false, true, false]) := by decide

theorem moore_equations [Fintype Q] [Fintype I] [Fintype O]
    (m : MooreTransducer Q I O) (q : Q) :
    mooreRun m q [] = (q, [m.emit q]) ∧
    (∀ a xs, mooreRun m q (a :: xs) =
      ((mooreRun m (m.next q a) xs).1, m.emit q :: (mooreRun m (m.next q a) xs).2)) :=
  ⟨rfl, fun _ _ => rfl⟩

abbrev FirstHitDecisionTable (X V : Type) := List ((X → Bool) × V)

def firstHit (rs : FirstHitDecisionTable X V) (x : X) : Option V :=
  match rs with
  | [] => none
  | (g,v) :: tail => if g x then some v else firstHit tail x

theorem first_hit_append (a b : FirstHitDecisionTable X V) (x : X) :
    firstHit (a ++ b) x = (firstHit a x).or (firstHit b x) := by
  induction a with
  | nil => rfl
  | cons r tail ih => rcases r with ⟨g,v⟩; cases h : g x <;> simp [firstHit, h, ih]

theorem first_hit_none (rs : FirstHitDecisionTable X V) (x : X) :
    firstHit rs x = none ↔ ∀ r ∈ rs, r.1 x = false := by
  induction rs with
  | nil => simp [firstHit]
  | cons r rs ih => rcases r with ⟨g,v⟩; cases h : g x <;> simp [firstHit, h, ih]

theorem first_hit_model_satisfaction :
    firstHit [(fun _ : Bool => true, 1), (fun _ => true, 2)] false = some 1 ∧
    firstHit ([] : FirstHitDecisionTable Bool Nat) false = none := by decide

theorem first_hit_selection (before after : FirstHitDecisionTable X V)
    (g : X → Bool) (v : V) (x : X)
    (hbefore : ∀ r ∈ before, r.1 x = false) (hg : g x = true) :
    firstHit (before ++ (g,v) :: after) x = some v := by
  rw [first_hit_append, (first_hit_none before x).mpr hbefore]
  simp [firstHit, hg]

structure TypedEdgeSchema (T K : Type) where
  sourceType : K → T
  targetType : K → T
  outMin : K → Nat
  outMax : K → Option Nat
  inMin : K → Nat
  inMax : K → Option Nat

structure TypedEdgeGraph (V E T K : Type) where
  source : E → V
  target : E → V
  vertexType : V → T
  edgeType : E → K

def withinBounds (n lo : Nat) (hi : Option Nat) : Prop :=
  lo ≤ n ∧ ∀ h ∈ hi, n ≤ h

def schemaConforms [Fintype E] [DecidableEq V] [DecidableEq K]
    (s : TypedEdgeSchema T K) (g : TypedEdgeGraph V E T K) : Prop :=
  (∀ e, g.vertexType (g.source e) = s.sourceType (g.edgeType e) ∧
        g.vertexType (g.target e) = s.targetType (g.edgeType e)) ∧
  (∀ v k, g.vertexType v = s.sourceType k → withinBounds
    (Finset.univ.filter (fun e => g.source e = v ∧ g.edgeType e = k)).card
    (s.outMin k) (s.outMax k)) ∧
  (∀ v k, g.vertexType v = s.targetType k → withinBounds
    (Finset.univ.filter (fun e => g.target e = v ∧ g.edgeType e = k)).card
    (s.inMin k) (s.inMax k))

def unitSchema : TypedEdgeSchema Unit Unit :=
  ⟨fun _ => (), fun _ => (), fun _ => 1, fun _ => some 1, fun _ => 1, fun _ => some 1⟩

def unitGraph : TypedEdgeGraph Unit Unit Unit Unit :=
  ⟨fun _ => (), fun _ => (), fun _ => (), fun _ => ()⟩

theorem schema_model_satisfaction : schemaConforms unitSchema unitGraph := by
  simp [schemaConforms, unitSchema, unitGraph, withinBounds]

theorem bounds_relax (n lo lo' : Nat) (hi hi' : Option Nat)
    (hlo : lo' ≤ lo) (hhi : ∀ h' ∈ hi', ∃ h ∈ hi, h ≤ h') :
    withinBounds n lo hi → withinBounds n lo' hi' := by
  intro hn
  refine ⟨le_trans hlo hn.1, ?_⟩
  intro h' hh'
  obtain ⟨h, hh, hle⟩ := hhi h' hh'
  exact le_trans (hn.2 h hh) hle

def leapYear (y : Nat) : Prop := y % 4 = 0 ∧ (y % 100 ≠ 0 ∨ y % 400 = 0)

instance (y : Nat) : Decidable (leapYear y) := inferInstanceAs (Decidable (_ ∧ _))

def monthDays (y m : Nat) : Nat :=
  if m = 2 then if leapYear y then 29 else 28
  else if m = 4 ∨ m = 6 ∨ m = 9 ∨ m = 11 then 30 else 31

def validDate (y m d : Nat) : Prop :=
  1 ≤ y ∧ 1 ≤ m ∧ m ≤ 12 ∧ 1 ≤ d ∧ d ≤ monthDays y m

instance (y m d : Nat) : Decidable (validDate y m d) :=
  inferInstanceAs (Decidable (_ ∧ _))

abbrev CalendarDate := {t : Nat × Nat × Nat // validDate t.1 t.2.1 t.2.2}

def dateKey (d : CalendarDate) : Nat ×ₗ Nat ×ₗ Nat :=
  toLex (d.val.1, toLex (d.val.2.1, d.val.2.2))

def dateLE (a b : CalendarDate) : Prop := dateKey a ≤ dateKey b

theorem date_model_satisfaction :
    validDate 2000 2 29 ∧ ¬ validDate 1900 2 29 ∧
    validDate 2026 11 20 ∧ ¬ validDate 2026 4 31 := by decide

theorem date_order_laws :
    (∀ a : CalendarDate, dateLE a a) ∧
    (∀ a b c, dateLE a b → dateLE b c → dateLE a c) ∧
    (∀ a b, dateLE a b ∨ dateLE b a) ∧
    (∀ a b, dateLE a b → dateLE b a → a = b) := by
  refine ⟨fun _ => le_rfl, fun _ _ _ => le_trans, fun _ _ => le_total _ _, ?_⟩
  intro a b hab hba
  have h := le_antisymm hab hba
  apply Subtype.ext
  exact congrArg (fun k : Nat ×ₗ Nat ×ₗ Nat =>
    ((ofLex k).1, (ofLex (ofLex k).2).1, (ofLex (ofLex k).2).2)) h

structure OrderLinearExtension (A : Type) (r : A → A → Prop) where
  relation : A → A → Prop
  linear : IsLinearOrder A relation
  preserves : ∀ a b, r a b → relation a b

theorem szpilrajn (A : Type) (r : A → A → Prop) [IsPartialOrder A r] :
    Nonempty (OrderLinearExtension A r) := by
  obtain ⟨s, hs, hrs⟩ := extend_partialOrder r
  exact ⟨⟨s, hs, fun a b h => hrs a b h⟩⟩

theorem linear_extension_model_satisfaction :
    Nonempty (OrderLinearExtension Nat (fun a b => a = b)) := by
  exact ⟨⟨(· ≤ ·), inferInstance, fun _ _ h => le_of_eq h⟩⟩

end Catalog
