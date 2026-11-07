module

public import Catalog.Graphs
public import Mathlib.Basic.Real.Basic
public import Mathlib.Algebra.BigOperators.Group.List.Basic

@[expose] public section

namespace Catalog
universe u v

structure RootedTree (V : Type u) [Fintype V] where
  graph : SimpleGraph V
  root : V
  tree : graph.IsTree

def RootedTree.forget {V : Type u} [Fintype V] (t : RootedTree V) : Catalog.Tree V :=
  ⟨t.graph, ⟨t.root⟩, t.tree⟩

/-- Edge identity is independent of the endpoint pair; loops and parallel edges
are allowed, and both vertex and edge carriers are finite. -/
structure DirectedMultigraph (V : Type u) (E : Type v) [Fintype V] [Fintype E] where
  source : E → V
  target : E → V

def DirectedMultigraph.path {V : Type u} {E : Type v} [Fintype V] [Fintype E]
    (g : DirectedMultigraph V E) : V → List E → V → Prop
  | s, [], t => s = t
  | s, e :: rest, t => g.source e = s ∧ g.path (g.target e) rest t

structure WeightedDirectedGraph (V : Type u) (E : Type v) [Fintype V] [Fintype E]
    extends DirectedMultigraph V E where
  weight : E → Real

noncomputable def WeightedDirectedGraph.pathWeight {V : Type u} {E : Type v} [Fintype V] [Fintype E]
    (g : WeightedDirectedGraph V E) (edges : List E) : Real := (edges.map g.weight).sum

/-- Finite simple undirected hypergraphs with edges of size at least two,
matching the selected NIST convention. Empty/singleton edges are excluded. -/
structure Hypergraph (V : Type u) [Fintype V] where
  edges : Finset (Finset V)
  arity : ∀ e ∈ edges, 2 ≤ e.card

structure BipartiteGraph (V : Type u) [Fintype V] where
  graph : SimpleGraph V
  color : V → Bool
  proper : ∀ u v, graph.Adj u v → color u ≠ color v

namespace GraphDataProofs

theorem single_edge_path {V : Type u} {E : Type v} [Fintype V] [Fintype E]
    (g : DirectedMultigraph V E) (e : E) : g.path (g.source e) [e] (g.target e) := ⟨rfl, rfl⟩

theorem path_weight_append {V : Type u} {E : Type v} [Fintype V] [Fintype E]
    (g : WeightedDirectedGraph V E) (p q : List E) :
    g.pathWeight (p ++ q) = g.pathWeight p + g.pathWeight q := by
  simp [WeightedDirectedGraph.pathWeight, List.sum_append]

theorem hyperedge_nonempty {V : Type u} [Fintype V] (g : Hypergraph V)
    (e : Finset V) (h : e ∈ g.edges) : e.Nonempty := Finset.card_pos.mp (by have := g.arity e h; omega)

theorem bipartite_adjacent_colors {V : Type u} [Fintype V] (g : BipartiteGraph V)
    (x y : V) (h : g.graph.Adj x y) : g.color x ≠ g.color y := g.proper x y h

end GraphDataProofs
end Catalog
