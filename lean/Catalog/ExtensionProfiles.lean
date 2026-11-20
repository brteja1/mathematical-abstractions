module
public import Catalog.CollectionUtilities
public import Catalog.ReachabilityUtilities
public import Catalog.RetrievalDecisions
@[expose] public section
namespace Catalog
universe u
def informationLE (a b : KleeneLogic) : Prop := a = 1 ∨ a = b
theorem information_monotone (a b c d : KleeneLogic) :
    informationLE a b → informationLE c d →
    informationLE (kleeneAnd a c) (kleeneAnd b d) ∧
    informationLE (kleeneOr a c) (kleeneOr b d) ∧
    informationLE (kleeneNeg a) (kleeneNeg b) := by
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;> unfold informationLE <;> decide
theorem prefix_saturation {A : Type u} (xs : List A) (k : Nat)
    (h : xs.length ≤ k) : xs.take k = xs := List.take_of_length_le h
def replaceSymbol {A : Type u} [DecidableEq A] (a b : A) (xs : List A) : List A :=
  xs.map (fun x => if x = a then b else x)
theorem replaceSymbol_idempotent {A : Type u} [DecidableEq A] (a b : A) (xs : List A) :
    replaceSymbol a b (replaceSymbol a b xs) = replaceSymbol a b xs := by
  simp only [replaceSymbol, List.map_map]
  congr 1
  funext x
  by_cases h : x = a
  · subst x; by_cases hb : b = a <;> simp [hb]
  · simp [h]
def endpointsAccept {V E T K : Type} (srcTypes dstTypes : K → Set T)
    (g : TypedEdgeGraph V E T K) : Prop :=
  ∀ e, g.vertexType (g.source e) ∈ srcTypes (g.edgeType e) ∧
    g.vertexType (g.target e) ∈ dstTypes (g.edgeType e)
theorem endpoints_singleton {V E T K : Type} (s : TypedEdgeSchema T K)
    (g : TypedEdgeGraph V E T K) :
    endpointsAccept (fun k => {s.sourceType k}) (fun k => {s.targetType k}) g ↔
    ∀ e, g.vertexType (g.source e) = s.sourceType (g.edgeType e) ∧
      g.vertexType (g.target e) = s.targetType (g.edgeType e) := Iff.rfl

theorem retrieval_saturation {D : Type u} [LinearOrder D]
    (s : Finset D) (score : RankedRetrieval D) (k : Nat) (_h : s.card ≤ k) :
    (retrievalKeys s score).take k = retrievalKeys s score := by
  classical
  apply List.take_of_length_le
  simpa [retrievalKeys, Finset.card_image_of_injective _ (show Function.Injective
    (fun d : D => toLex (-score d, d)) from fun a b h => congrArg (fun x : ℝ ×ₗ D => (ofLex x).2) h)] using _h

structure EndpointSetSchema (T K : Type) where
  sourceTypes : K → Set T
  targetTypes : K → Set T
  bounds : TypedEdgeSchema T K

def setSchemaConforms {V E T K : Type} [Fintype E] [DecidableEq V] [DecidableEq K]
    (s : EndpointSetSchema T K) (g : TypedEdgeGraph V E T K) : Prop :=
  endpointsAccept s.sourceTypes s.targetTypes g ∧
  (∀ v k, g.vertexType v ∈ s.sourceTypes k → withinBounds
    (Finset.univ.filter (fun e => g.source e = v ∧ g.edgeType e = k)).card
    (s.bounds.outMin k) (s.bounds.outMax k)) ∧
  (∀ v k, g.vertexType v ∈ s.targetTypes k → withinBounds
    (Finset.univ.filter (fun e => g.target e = v ∧ g.edgeType e = k)).card
    (s.bounds.inMin k) (s.bounds.inMax k))
def singletonSchema {T K : Type} (s : TypedEdgeSchema T K) : EndpointSetSchema T K :=
  ⟨fun k => {s.sourceType k}, fun k => {s.targetType k}, s⟩
theorem setSchema_singleton {V E T K : Type} [Fintype E] [DecidableEq V] [DecidableEq K]
    (s : TypedEdgeSchema T K) (g : TypedEdgeGraph V E T K) :
    setSchemaConforms (singletonSchema s) g ↔ schemaConforms s g := Iff.rfl

def symbolRewrite {A : Type u} [DecidableEq A] (a b : A) : Programs.RewriteSystem (List A) :=
  ⟨fun xs ys => ys = replaceSymbol a b xs ∧ ys ≠ xs⟩
theorem symbolRewrite_confluent {A : Type u} [DecidableEq A] (a b : A) :
    Programs.confluent (symbolRewrite a b) := by
  have invariant : ∀ xs ys, (symbolRewrite a b).reduces xs ys →
      replaceSymbol a b xs = replaceSymbol a b ys := by
    intro xs ys h
    induction h with
    | refl => rfl
    | tail h step ih =>
      rcases step with ⟨rfl, _⟩
      exact ih.trans (replaceSymbol_idempotent a b _).symm
  have reach : ∀ xs, (symbolRewrite a b).reduces xs (replaceSymbol a b xs) := by
    intro xs
    by_cases h : replaceSymbol a b xs = xs
    · rw [h]; exact .refl
    · exact .single ⟨rfl, h⟩
  intro xs ys zs hy hz
  refine ⟨replaceSymbol a b ys, reach ys, ?_⟩
  rw [← invariant xs ys hy, invariant xs zs hz]
  exact reach zs

theorem replaceSymbol_eq_replaceAll {A : Type u} [DecidableEq A] (a b : A) (xs : List A) :
    replaceSymbol a b xs = replaceAll [a] (by simp) [b] xs := by
  induction xs with
  | nil => rw [replaceAll.eq_def]; rfl
  | cons x xs ih =>
    rw [replaceAll.eq_def]
    by_cases h : x = a
    · subst x; simpa [replaceSymbol] using congrArg (List.cons b) ih
    · simpa [replaceSymbol, h, Ne.symm h] using congrArg (List.cons x) ih
#catalog_witness information_monotone
#catalog_witness prefix_saturation
#catalog_witness replaceSymbol_idempotent
#catalog_witness endpoints_singleton
#catalog_witness retrieval_saturation
#catalog_witness setSchema_singleton
#catalog_witness symbolRewrite_confluent
#catalog_witness replaceSymbol_eq_replaceAll
end Catalog
