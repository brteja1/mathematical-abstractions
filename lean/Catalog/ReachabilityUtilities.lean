module

public import Catalog.Graphs
public import Catalog.ProgramStructures
public import Catalog.ReleaseSequenceModels
public import Mathlib.Data.Fintype.Card
public import Mathlib.Order.Extension.Linear
public import Catalog.Audit

@[expose] public section
namespace Catalog
universe u

def boundedReach {V : Type u} (edge : V → V → Prop) : Nat → V → V → Prop
  | 0, a, b => a = b
  | n + 1, a, b => a = b ∨ ∃ c, edge a c ∧ boundedReach edge n c b

theorem boundedReach_closure {V : Type u} (edge : V → V → Prop) (a b : V) :
    (∃ n, boundedReach edge n a b) ↔ Relation.ReflTransGen edge a b := by
  constructor
  · rintro ⟨n, h⟩
    induction n generalizing a with
    | zero => cases h; rfl
    | succ n ih =>
      rcases h with h | ⟨c, hac, hcb⟩
      · cases h; rfl
      · exact (ih c hcb).head hac
  · intro h
    induction h with
    | refl => exact ⟨0, rfl⟩
    | @tail b c hab hbc ih =>
      obtain ⟨n, hn⟩ := ih
      have extend : ∀ n a b c, boundedReach edge n a b → edge b c →
          boundedReach edge (n+1) a c := by
        intro n
        induction n with
        | zero => intro a b c h hbc; cases h; exact Or.inr ⟨c, hbc, rfl⟩
        | succ n ih =>
          rintro a b c (h | ⟨d, had, hdb⟩) hbc
          · cases h; exact Or.inr ⟨c, hbc, Or.inl rfl⟩
          · exact Or.inr ⟨d, had, ih d b c hdb hbc⟩
      exact ⟨n+1, extend n _ _ _ hn hbc⟩

def componentOf {V : Type u} (g : SimpleGraph V) (v : V) : Set V :=
  {w | g.Reachable v w}

theorem graph_components {V : Type u} (g : SimpleGraph V) (v w : V) :
    (componentOf g v = componentOf g w ↔ g.Reachable v w) := by
  constructor
  · intro h
    have : w ∈ componentOf g w := SimpleGraph.Reachable.refl _
    rw [← h] at this
    exact this
  · intro h
    ext x
    exact ⟨fun hx => h.symm.trans hx, fun hx => h.trans hx⟩

theorem dag_reach_order {V : Type u} (g : DAG V) :
    (∀ a, Relation.ReflTransGen g.edge a a) ∧
    (∀ a b c, Relation.ReflTransGen g.edge a b → Relation.ReflTransGen g.edge b c →
      Relation.ReflTransGen g.edge a c) ∧
    (∀ a b, Relation.ReflTransGen g.edge a b → Relation.ReflTransGen g.edge b a → a = b) := by
  refine ⟨fun _ => .refl, fun _ _ _ => Relation.ReflTransGen.trans, ?_⟩
  intro a b hab hba
  rcases Relation.reflTransGen_iff_eq_or_transGen.mp hab with h | h
  · exact h.symm
  · exact False.elim (g.acyclic a (Relation.TransGen.trans_left h hba))

theorem topological_converse {V : Type u} (edge : V → V → Prop)
    (lt : V → V → Prop) (irrefl : ∀ v, ¬ lt v v)
    (trans : ∀ a b c, lt a b → lt b c → lt a c)
    (respects : ∀ a b, edge a b → lt a b) :
    ∀ v, ¬ Relation.TransGen edge v v := by
  have lift : ∀ a b, Relation.TransGen edge a b → lt a b := by
    intro a b h
    induction h with
    | single h => exact respects _ _ h
    | tail _ h ih => exact trans _ _ _ ih (respects _ _ h)
  intro v h
  exact irrefl v (lift v v h)

/-- A comparison is forced by every linear extension exactly when it is original. -/
theorem order_all_extensions {A : Type u} (r : A → A → Prop) [IsPartialOrder A r]
    (a b : A) : r a b ↔ ∀ s : A → A → Prop, IsLinearOrder A s → r ≤ s → s a b := by
  constructor
  · exact fun hab _ _ hrs => hrs _ _ hab
  · intro h
    by_contra hab
    let t x y := r x y ∨ r x b ∧ r a y
    have ht : IsPartialOrder A t := by
      refine { refl := fun x => Or.inl (refl x), trans := ?_, antisymm := ?_ }
      · rintro x y z (hxy | ⟨hxb, hay⟩) (hyz | ⟨hyb, haz⟩)
        · exact Or.inl (_root_.trans hxy hyz)
        · exact Or.inr ⟨_root_.trans hxy hyb, haz⟩
        · exact Or.inr ⟨hxb, _root_.trans hay hyz⟩
        · exact Or.inr ⟨hxb, haz⟩
      · rintro x y (hxy | ⟨hxb, hay⟩) (hyx | ⟨hyb, hax⟩)
        · exact antisymm hxy hyx
        · exact (hab (_root_.trans hax (_root_.trans hxy hyb))).elim
        · exact (hab (_root_.trans hay (_root_.trans hyx hxb))).elim
        · exact (hab (_root_.trans hay hyb)).elim
    obtain ⟨s, hs, hts⟩ := @extend_partialOrder A t ht
    have hrs : r ≤ s := fun _ _ h => hts _ _ (Or.inl h)
    have hba : s b a := hts _ _ (Or.inr ⟨refl b, refl a⟩)
    have : a = b := hs.antisymm a b (h s hs hrs) hba
    subst b
    exact hab (refl a)

theorem dag_all_extensions {V : Type u} (g : DAG V) (a b : V) :
    Relation.ReflTransGen g.edge a b ↔
    ∀ s : V → V → Prop, IsLinearOrder V s → Relation.ReflTransGen g.edge ≤ s → s a b := by
  have hp := dag_reach_order g
  have : IsPartialOrder V (Relation.ReflTransGen g.edge) :=
    { refl := hp.1, trans := hp.2.1, antisymm := hp.2.2 }
  exact order_all_extensions _ a b

namespace Programs

def parentEdge {V : Type u} [Fintype V] (f : SingleParentForest V) (v w : V) : Prop :=
  f.parent v = some w

theorem forest_descendant_order {V : Type u} [Fintype V] (f : SingleParentForest V) :
    (∀ a, Relation.ReflTransGen (parentEdge f) a a) ∧
    (∀ a b c, Relation.ReflTransGen (parentEdge f) a b →
      Relation.ReflTransGen (parentEdge f) b c → Relation.ReflTransGen (parentEdge f) a c) ∧
    (∀ a b, Relation.ReflTransGen (parentEdge f) a b →
      Relation.ReflTransGen (parentEdge f) b a → a = b) :=
  dag_reach_order ⟨parentEdge f, f.acyclic⟩

theorem forest_termination {V : Type u} [Fintype V] (f : SingleParentForest V) :
    WellFounded (fun w v => parentEdge f v w) := by
  let r := fun w v => Relation.TransGen (parentEdge f) v w
  have : IsTrans V r := ⟨fun _ _ _ h h' => h'.trans h⟩
  have : Std.Irrefl r := ⟨f.acyclic⟩
  exact (Finite.wellFounded_of_trans_of_irrefl r).mono
    (fun _ _ h => Relation.TransGen.single h)

theorem forest_root_exists {V : Type u} [Fintype V] (f : SingleParentForest V) (v : V) :
    ∃ r, f.parent r = none ∧ Relation.ReflTransGen (parentEdge f) v r := by
  induction v using (forest_termination f).induction with
  | h v ih =>
    cases hp : f.parent v with
    | none => exact ⟨v, hp, .refl⟩
    | some w =>
      obtain ⟨r, hr, hwr⟩ := ih w hp
      exact ⟨r, hr, hwr.head hp⟩

theorem forest_root_unique {V : Type u} [Fintype V] (f : SingleParentForest V)
    (v r s : V) (hr : f.parent r = none) (hs : f.parent s = none)
    (hvr : Relation.ReflTransGen (parentEdge f) v r)
    (hvs : Relation.ReflTransGen (parentEdge f) v s) : r = s := by
  induction hvr using Relation.ReflTransGen.head_induction_on with
  | refl =>
    exact (Relation.reflTransGen_iff_eq (fun b hb => by
      simp [parentEdge, hr] at hb)).mp hvs |>.symm
  | @head v w hvw _ ih =>
    rcases hvs.cases_head with h | ⟨w', hvw', hws⟩
    · subst s; simp [parentEdge, hs] at hvw
    · have : w = w' := Option.some.inj (hvw.symm.trans hvw')
      subst w'
      exact ih hws

noncomputable def forestRootOf {V : Type u} [Fintype V] (f : SingleParentForest V) (v : V) : V :=
  Classical.choose (forest_root_exists f v)

theorem forest_root_equation {V : Type u} [Fintype V] (f : SingleParentForest V) (v : V) :
    f.parent (forestRootOf f v) = none ∧
    Relation.ReflTransGen (parentEdge f) v (forestRootOf f v) ∧
    (∀ w, f.parent v = some w → forestRootOf f v = forestRootOf f w) ∧
    (f.parent v = none → forestRootOf f v = v) := by
  obtain ⟨hr, hvr⟩ := Classical.choose_spec (forest_root_exists f v)
  refine ⟨hr, hvr, ?_, ?_⟩
  · intro w hw
    obtain ⟨hs, hws⟩ := Classical.choose_spec (forest_root_exists f w)
    exact forest_root_unique f v _ _ hr hs hvr (hws.head hw)
  · intro hv
    exact forest_root_unique f v _ v hr hv hvr .refl

def confluent {A : Type u} (r : RewriteSystem A) : Prop :=
  ∀ a b c, r.reduces a b → r.reduces a c → ∃ d, r.reduces b d ∧ r.reduces c d

def terminating {A : Type u} (r : RewriteSystem A) : Prop :=
  WellFounded (fun b a => r.step a b)

theorem normalForm_reduces_eq {A : Type u} (r : RewriteSystem A) (a b : A)
    (ha : r.normalForm a) (hab : r.reduces a b) : a = b :=
  ((Relation.reflTransGen_iff_eq (fun b h => ha ⟨b, h⟩)).mp hab).symm

theorem confluent_unique_normalForm {A : Type u} (r : RewriteSystem A)
    (hc : confluent r) (a b c : A) (hab : r.reduces a b) (hac : r.reduces a c)
    (hb : r.normalForm b) (hc' : r.normalForm c) : b = c := by
  obtain ⟨d, hbd, hcd⟩ := hc a b c hab hac
  exact (normalForm_reduces_eq r b d hb hbd).trans (normalForm_reduces_eq r c d hc' hcd).symm

theorem terminating_normalForm {A : Type u} (r : RewriteSystem A)
    (ht : terminating r) (a : A) : ∃ b, r.reduces a b ∧ r.normalForm b := by
  classical
  induction a using ht.induction with
  | h a ih =>
    by_cases hn : r.normalForm a
    · exact ⟨a, .refl, hn⟩
    · obtain ⟨b, hab⟩ := not_not.mp hn
      obtain ⟨c, hbc, hc⟩ := ih b hab
      exact ⟨c, hbc.head hab, hc⟩

theorem convergent_unique_normalForm {A : Type u} (r : RewriteSystem A)
    (ht : terminating r) (hc : confluent r) (a : A) :
    ∃! b, r.reduces a b ∧ r.normalForm b := by
  obtain ⟨b, hab, hb⟩ := terminating_normalForm r ht a
  exact ⟨b, ⟨hab, hb⟩, fun c h => confluent_unique_normalForm r hc a c b h.1 hab h.2 hb⟩

def emptyRewrite (A : Type u) : RewriteSystem A := ⟨fun _ _ => False⟩

theorem rewrite_model (A : Type u) : terminating (emptyRewrite A) ∧ confluent (emptyRewrite A) := by
  refine ⟨⟨fun a => Acc.intro a (fun _ h => h.elim)⟩, ?_⟩
  intro a b c hab hac
  have hb := normalForm_reduces_eq (emptyRewrite A) a b (by simp [RewriteSystem.normalForm, emptyRewrite]) hab
  have hc := normalForm_reduces_eq (emptyRewrite A) a c (by simp [RewriteSystem.normalForm, emptyRewrite]) hac
  subst b; subst c
  exact ⟨a, .refl, .refl⟩
end Programs

def terminal {S : Type u} (next : S → S → Prop) (s : S) : Prop := ¬ ∃ t, next s t
def goal {S : Type u} (g : Set S) (s : S) : Prop := s ∈ g
def deadlock {S : Type u} (next : S → S → Prop) (g : Set S) (s : S) : Prop :=
  terminal next s ∧ ¬ goal g s

theorem terminal_enabled {S : Type u} (next : S → S → Prop) (s : S) :
    terminal next s ↔ ¬ ∃ t, next s t := Iff.rfl

def tracePrecedes {S : Type u} (p q : S → Prop) (xs : List S) : Prop :=
  ∀ i, ∀ hi : i < xs.length, q xs[i] → ∃ j, ∃ hj : j < xs.length, j < i ∧ p xs[j]

theorem tracePrecedes_initial {S : Type u} (p q : S → Prop) (a : S) (xs : List S)
    (h : tracePrecedes p q (a :: xs)) : ¬ q a := by
  intro hq
  obtain ⟨j, _, hj, _⟩ := h 0 (by simp) hq
  exact Nat.not_lt_zero j hj

def subtypeSchemaConforms {V E T K : Type} [Fintype E] [DecidableEq V] [DecidableEq K]
    (sub : T → T → Prop) (s : TypedEdgeSchema T K) (g : TypedEdgeGraph V E T K) : Prop :=
  (∀ e, sub (g.vertexType (g.source e)) (s.sourceType (g.edgeType e)) ∧
        sub (g.vertexType (g.target e)) (s.targetType (g.edgeType e))) ∧
  (∀ v k, sub (g.vertexType v) (s.sourceType k) → withinBounds
    (Finset.univ.filter (fun e => g.source e = v ∧ g.edgeType e = k)).card (s.outMin k) (s.outMax k)) ∧
  (∀ v k, sub (g.vertexType v) (s.targetType k) → withinBounds
    (Finset.univ.filter (fun e => g.target e = v ∧ g.edgeType e = k)).card (s.inMin k) (s.inMax k))

theorem subtype_exact {V E T K : Type} [Fintype E] [DecidableEq V] [DecidableEq K]
    (s : TypedEdgeSchema T K) (g : TypedEdgeGraph V E T K) :
    subtypeSchemaConforms Eq s g ↔ schemaConforms s g := Iff.rfl

theorem subtype_model : subtypeSchemaConforms Eq unitSchema unitGraph := schema_model_satisfaction

def subtypeExampleSchema : TypedEdgeSchema (Fin 2) Unit :=
  ⟨fun _ => 1, fun _ => 1, fun _ => 0, fun _ => none, fun _ => 0, fun _ => none⟩

def subtypeExampleGraph : TypedEdgeGraph Unit Unit (Fin 2) Unit :=
  ⟨fun _ => (), fun _ => (), fun _ => 0, fun _ => ()⟩

theorem subtype_strict_model :
    subtypeSchemaConforms (· ≤ ·) subtypeExampleSchema subtypeExampleGraph ∧
    ¬ schemaConforms subtypeExampleSchema subtypeExampleGraph := by
  simp [subtypeSchemaConforms, schemaConforms, subtypeExampleSchema,
    subtypeExampleGraph, withinBounds]

#catalog_witness boundedReach_closure
#catalog_witness graph_components
#catalog_witness dag_reach_order
#catalog_witness topological_converse
#catalog_witness order_all_extensions
#catalog_witness dag_all_extensions
#catalog_witness Programs.forest_termination
#catalog_witness Programs.forest_descendant_order
#catalog_witness Programs.forest_root_exists
#catalog_witness Programs.forest_root_unique
#catalog_witness Programs.forest_root_equation
#catalog_witness Programs.normalForm_reduces_eq
#catalog_witness Programs.confluent_unique_normalForm
#catalog_witness Programs.terminating_normalForm
#catalog_witness Programs.convergent_unique_normalForm
#catalog_witness Programs.rewrite_model
#catalog_witness terminal_enabled
#catalog_witness tracePrecedes_initial
#catalog_witness subtype_exact
#catalog_witness subtype_model
#catalog_witness subtype_strict_model
end Catalog
