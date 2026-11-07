# Foundational computer-science data models

The catalog covers the **broad computer-science core**: values and types, collection ADTs, trees and graphs, streams, exact and machine numbers, state, and database models. This expansion adds 35 concepts to the existing catalog. The tables below define this baseline; they are not a claim that every data model, semantic variant, implementation technique or mathematical consequence is catalogued.

Each linked concept records its chosen carrier, equality, operations, defining rules, assumptions, derived results and sources. Use [the complete index](../CONCEPTS.md) for other mathematical foundations. The [machine-readable inventory](../data/foundational_models.json) lists the expansion, family coverage and explicit instantiations. That inventory is a navigation checklist; mathematical facts remain in the marked JSON records in `concepts/`.

## Core families

| Family | Existing abstractions reused | Added abstractions |
| --- | --- | --- |
| Values and type constructors | [EmptyType](../concepts/EmptyType.md), [UnitType](../concepts/UnitType.md), [ProductType](../concepts/ProductType.md), [SumType](../concepts/SumType.md), [OptionType](../concepts/OptionType.md), [FunctionType](../concepts/FunctionType.md) | [BooleanType](../concepts/BooleanType.md), [FiniteType](../concepts/FiniteType.md), [DependentPair](../concepts/DependentPair.md), [DependentFunction](../concepts/DependentFunction.md), [Subtype](../concepts/Subtype.md), [QuotientType](../concepts/QuotientType.md) |
| Numeric and indexed data | Naturals, integers, fixed-width/modular/checked/saturating arithmetic, bit vectors, IEEE format interfaces, [Array](../concepts/Array.md), [Matrix](../concepts/Matrix.md), [VectorSpace](../concepts/VectorSpace.md), [Tensor](../concepts/Tensor.md) | [RationalNumber](../concepts/RationalNumber.md), [RealNumber](../concepts/RealNumber.md), [ComplexNumber](../concepts/ComplexNumber.md), [SparseVector](../concepts/SparseVector.md), [ClosedInterval](../concepts/ClosedInterval.md) |
| Collections and access protocols | [Sequence](../concepts/Sequence.md), [FiniteSet](../concepts/FiniteSet.md), [Multiset](../concepts/Multiset.md), [Map](../concepts/Map.md), [OrderedSet](../concepts/OrderedSet.md), [Stack](../concepts/Stack.md), [Queue](../concepts/Queue.md), [Deque](../concepts/Deque.md), [PriorityQueue](../concepts/PriorityQueue.md) | [Multimap](../concepts/Multimap.md), [FiniteIterator](../concepts/FiniteIterator.md), [Stream](../concepts/Stream.md) |
| Trees, dictionaries and syntax | [Tree](../concepts/Tree.md), [BinaryTree](../concepts/BinaryTree.md), structural induction, partitions and equivalence relations | [RootedTree](../concepts/RootedTree.md), [RoseTree](../concepts/RoseTree.md), [TermAlgebra](../concepts/TermAlgebra.md), [BinarySearchTree](../concepts/BinarySearchTree.md), [BinaryHeap](../concepts/BinaryHeap.md), [Trie](../concepts/Trie.md), [DisjointSet](../concepts/DisjointSet.md) |
| Graph data | [Graph](../concepts/Graph.md), [DirectedGraph](../concepts/DirectedGraph.md), [DAG](../concepts/DAG.md) | [DirectedMultigraph](../concepts/DirectedMultigraph.md), [WeightedDirectedGraph](../concepts/WeightedDirectedGraph.md), [Hypergraph](../concepts/Hypergraph.md), [BipartiteGraph](../concepts/BipartiteGraph.md) |
| State, probability and replication | Partial functions, maps, probability spaces, state-transition systems and concurrency properties | [HeapStore](../concepts/HeapStore.md), [FiniteDistribution](../concepts/FiniteDistribution.md), [JoinSemilattice](../concepts/JoinSemilattice.md), [StateBasedCRDT](../concepts/StateBasedCRDT.md) |
| Database and interchange models | [RelationalSchema](../concepts/RelationalSchema.md), [DatabaseRelation](../concepts/DatabaseRelation.md), [FunctionalDependency](../concepts/FunctionalDependency.md), [CandidateKey](../concepts/CandidateKey.md) | [BagRelation](../concepts/BagRelation.md), [EntityRelationshipModel](../concepts/EntityRelationshipModel.md), [DocumentValue](../concepts/DocumentValue.md), [PropertyGraph](../concepts/PropertyGraph.md), [RDFGraph](../concepts/RDFGraph.md), [RDFDataset](../concepts/RDFDataset.md) |

## Familiar names as explicit instantiations

These names reuse existing carriers. They do not introduce duplicate concept or axiom records.

| Familiar model | Catalog instantiation | What must be chosen |
| --- | --- | --- |
| String / finite word | `Sequence(Alphabet)` | Byte, Unicode scalar, code-unit or grapheme alphabet; normalization and equality policy. Generic sequences do not choose an encoding. |
| Byte / octet | `FixedWidthUnsignedInteger` with width 8 | Arithmetic/overflow convention; byte sequences are `Sequence(Byte)`. |
| Result / either / tagged error | `SumType(Success,Error)` | Explicit success/error tags; `OptionType` instead models absence without an error payload. |
| Record / named tuple | Tuple carrier of `RelationalSchema` | Finite field names, field domains, extensional field equality; optional fields need explicit option domains. |
| Fixed-length vector | `Array(A,n)` | Indexed value data; a linear-algebra vector additionally needs field operations and a basis/coordinate interpretation. |
| Sparse matrix | `SparseVector(F,I×J)` | Field F and row/column index carriers; multiplication needs compatible dimensions and a separately specified contraction. |
| Forest | `Sequence(RoseTree(A))` | Ordered, possibly empty list of nonempty labelled trees; unordered forests need a multiset/set variant. |
| Key/value store | `Map(K,V)` | Finite snapshot semantics; persistence, transactions, failures and concurrency require extra behavior models. |
| Hierarchical data | `RoseTree` or `DocumentValue` | Ordered homogeneous labelled nodes versus tagged arrays/objects with unique named members. |
| Network database view | `EntityRelationshipModel` with binary roles | Typed entities and relationships; navigational cursors, access paths and historical CODASYL owner/member constraints require separate refinements. |

Linked lists, dynamic arrays, hash maps/sets, ring buffers and balanced search trees require representation or invariant refinements of these interfaces. They do not need another value carrier merely because their storage differs. If pointer identity, sharing, aliasing or allocation is observable, use explicit address identities and `HeapStore`; do not equate heap graphs with immutable tree values.

## Selected conventions

- Set, bag and sequence equality differ. `Multimap` is set-valued; `BagRelation` preserves duplicate row counts. `Trie` observes full-word bindings and prefix selection, without prescribing compressed or uncompressed node layout.
- `Stream` is infinite and total. `FiniteIterator` is a finite immutable cursor that remains exhausted after returning `None`; it retains its original sequence and cursor position in equality.
- `BinarySearchTree` excludes duplicate keys. `BinaryHeap` permits ties, retains level-order shape and specifies allowed update outcomes without fixing an algorithm. Its invariant does not assert a complexity bound.
- Graph edge identity, orientation and multiplicity are explicit. `Hypergraph` selects the convention of undirected edges of cardinality at least two. `BipartiteGraph` retains a chosen coloring. Weighted graphs allow negative real weights.
- Rational, real and complex numbers are exact mathematical carriers. Real equality/order need not be decidable. Floating-point bindings remain explicitly partial interfaces; exact arithmetic laws are not automatically floating-point laws.
- `DocumentValue` selects finite JSON values with unique object keys, Unicode scalar strings and exact finite decimal numbers. This is an interoperable semantic profile adapted from RFC 8259, not a parser for every accepted syntax.
- `PropertyGraph` chooses single labels and single-valued properties. RDF uses RDF 1.1 position restrictions, literal term equality and scoped blank identities. Dataset absence differs from a present empty graph; default graphs are not implicitly unions.
- `StateBasedCRDT` supplies a merge algebra and inflationary updates. Delivery, fairness and eventual convergence of a running network need separate assumptions and proofs.

Further variants include open/unbounded intervals, lazy/effectful iterators, arbitrary-precision decimal arithmetic policies, SQL NULL/three-valued logic, inclusion dependencies/normal forms, weak ER entities, graph meta-properties, binders and substitution, balanced-tree refinements, persistent storage and transaction protocols. Add them when their observable mathematical interface is specified, after searching for existing meanings.

## Retrieval and Lean evidence

```sh
python3 scripts/catalog.py list --category data-modelling
python3 scripts/catalog.py get BinaryHeap --sections operations axioms laws theorems sources
python3 scripts/agent_query.py dossier RDFDataset --purpose tests --limit 40
python3 ai/skills/mathematical-tests/scripts/query.py search 'prefix'
```

Inspect `truncated` and budget/depth boundaries before using a dossier. Shared rules have explicit `appliesTo` links and instantiation notes; neither prerequisites nor specializations imply axiom inheritance. New concept records have direct consulted-source provenance. Reused historical claims can still carry explicitly marked citation gaps; this expansion does not erase those gaps.

All 35 additions have compiled Lean carrier bindings in `CoreData`, `StructuredData`, `GraphData` or `InformationData`. Selected claims add 24 individually mapped compiled witnesses, bringing the repository total to 52. Other derived results retain editorial proof sketches with explicit premises. Carrier coverage is not proof coverage: consult [Lean mappings and limitations](../lean/README.md), and run `make test-lean` for fresh evidence. A model binding does not assert that every recorded operation has a Lean wrapper or every claim has a proof.
