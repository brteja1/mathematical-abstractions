module

public import Catalog.Database
public import Catalog.StructuredData
public import Catalog.CoreData
public import Catalog.GraphData

@[expose] public section

namespace Catalog
universe u v w

abbrev BagRelation (s : RelationalSchema) := _root_.Multiset (Catalog.NamedTuple s)

abbrev DecimalRational := {q : Rat // ∃ (m e : Int), q = (m : Rat) * (10 : Rat) ^ e}

/-- Interoperable JSON value profile: scalar Unicode strings, exact finite
decimal numbers, ordered arrays, unique object keys and extensional objects.
Object member order, numeric spelling and whitespace are not observations. -/
inductive DocumentValue where
  | null : DocumentValue
  | boolean : Bool → DocumentValue
  | number : DecimalRational → DocumentValue
  | string : String → DocumentValue
  | array : List DocumentValue → DocumentValue
  | object (keys : Finset String) : ({k // k ∈ keys} → DocumentValue) → DocumentValue

/-- Typed ER instances with global entity identity, possibly overlapping entity
sets, n-ary roles, scalar entity/relationship attributes and referential integrity.
Weak entities, inheritance and cardinality constraints require extra predicates. -/
structure EntityRelationshipModel (EK RK ID : Type u) [Fintype EK] [Fintype RK]
    (arity : RK → Nat) (role : (r : RK) → Fin (arity r) → EK)
    (Attr : EK → Type u) (Val : (k : EK) → Attr k → Type v)
    (RAttr : RK → Type u) (RVal : (r : RK) → RAttr r → Type v)
    [∀ k, Fintype (Attr k)] [∀ r, Fintype (RAttr r)] where
  positive_arity : ∀ r, 0 < arity r
  entities : EK → Finset ID
  attributes : (k : EK) → {e // e ∈ entities k} → (a : Attr k) → Val k a
  relationships : (r : RK) → Finset (Fin (arity r) → ID)
  integrity : ∀ r, ∀ row ∈ relationships r, ∀ i, row i ∈ entities (role r i)
  relationshipAttributes : (r : RK) → {row // row ∈ relationships r} → (a : RAttr r) → RVal r a

/-- Finite single-label, single-valued-property LPG profile. Vertex and edge
identities are separate sorts, so parallel edges remain distinct. -/
structure PropertyGraph (V : Type u) (E : Type v) (Value : Type w)
    [Fintype V] [Fintype E] extends DirectedMultigraph V E where
  vertexLabel : V → String
  edgeLabel : E → String
  vertexProperties : V → Catalog.Map String Value
  edgeProperties : E → Catalog.Map String Value

/-- I and L must be instantiated by validated IRI and RDF literal carriers.
Blank node identity is a scoped sort B; this is not a parser or entailment engine. -/
inductive RDFTerm (I : Type u) (B : Type v) (L : Type w) where
  | iri : I → RDFTerm I B L
  | blank : B → RDFTerm I B L
  | literal : L → RDFTerm I B L

abbrev RDFTriple (I : Type u) (B : Type v) (L : Type w) := (I ⊕ B) × I × RDFTerm I B L
abbrev RDFGraph (I : Type u) (B : Type v) (L : Type w) := Finset (RDFTriple I B L)

/-- Absence of a named graph differs from a present but empty named graph. -/
structure RDFDataset (I : Type u) (B : Type v) (L : Type w) where
  defaultGraph : RDFGraph I B L
  namedGraphs : Catalog.Map (I ⊕ B) (RDFGraph I B L)

namespace InformationDataProofs

theorem bag_union_commutes {s : RelationalSchema} (r t : BagRelation s) : r + t = t + r :=
  add_comm r t

theorem document_boolean_injective (a b : Bool) :
    DocumentValue.boolean a = DocumentValue.boolean b ↔ a = b := by
  constructor
  · intro h; cases h; rfl
  · intro h; cases h; rfl

theorem rdf_iri_not_blank {I : Type u} {B : Type v} {L : Type w} (i : I) (b : B) :
    (RDFTerm.iri i : RDFTerm I B L) ≠ RDFTerm.blank b := by
  intro h
  cases h

end InformationDataProofs
end Catalog
