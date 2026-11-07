# Mathematical Abstractions for Computer Science

This is a compact topic index. Authoritative concept records live in [`concepts/`](concepts/); [`catalog.jsonld`](catalog.jsonld) is their generated export. See [`CONCEPTS.md`](CONCEPTS.md) for all current pages, [`README.md`](README.md) for maintenance, and [`docs/IMPORTED_SCHEMA.md`](docs/IMPORTED_SCHEMA.md) for the inherited schema and SPARQL examples. For a task, query the graph by `shortForm` and retrieve only the requested definition, operations, axioms, laws, theorems, or sources. Avoid loading this index as a substitute for a targeted graph query.

The [foundational data-model guide](docs/FOUNDATIONAL_DATA_MODELS.md) defines the broad-core baseline, including explicit instantiations and selected semantic profiles.

## Topic map

### Foundations

Sets and membership; subsets and set operations; power sets; Cartesian products; relations; functions and partial functions; equivalence relations; partitions; cardinality; induction; recursion; pigeonhole principle.

### Logic and proof

Propositional and predicate logic; Boolean algebra; inference systems; induction; Hoare logic; weakest preconditions; classical propositional modal logic K; linear temporal logic with next and strong until on infinite discrete traces; refinement and simulation.

### Algebra

Operations and their laws; semigroups; monoids; groups; rings; semirings; fields; lattices; modules; vector spaces; homomorphisms; quotients; products.

### Measure theory and probability

Measurable spaces and sigma-algebras; nonnegative countably additive measures; probability spaces; measurable functions and random variables; positive-event conditional probability and Bayes rule. Finite discrete Bayesian networks and finite-state, discrete-time, time-homogeneous Markov chains connect probability to DAGs and matrices. General-state kernels, continuous-time processes, integration, densities and conditioning on null events require further interfaces.

### Linear algebra, topology and geometry

Vector spaces over a field; linear maps; exact finite rectangular matrices; algebraic tensor products; finite-dimensional tensors of specified valence. Topological spaces; finite-dimensional Hausdorff second-countable topological manifolds without boundary; smooth manifolds with a chosen C∞ structure. Tensor coordinates require chosen bases; tensor fields and Riemannian metrics are additional structure.

### Order and fixed points

Preorders; partial and total orders; well-founded relations; lattices; monotone maps; closure operators; Galois connections; fixed-point theorems.

### Discrete structures

Graphs and digraphs; trees; paths and reachability; connectivity; combinatorics; recurrences; counting principles; hypergraphs.

### Numeric structures and machine arithmetic

Natural, integer, rational, real, and complex numbers; fixed-width signed and unsigned types; modular integers; bit vectors; checked and saturating arithmetic; floating-point formats, rounding, exceptional values, and error models.

### Programming and data abstractions

Types; functions; state-transition systems; semantics; abstract data types; arrays; sequences; sets; maps; stacks; queues; trees; heaps; graphs; iterators and streams.

### Relational data modelling

Recorded: named relational schemas with attribute domains; finite database relations with set semantics and projection; functional dependencies with separate instance satisfaction and schema implication; candidate keys relative to declared dependencies. Empty relations, zero-attribute tuples, and empty keys have explicit conventions. Selected results include typed tuple-update laws, selection composition, projection over union, FD lossless decomposition, semantic attribute closure, key antichains, and injective key projection. Also recorded: bag relations, typed entity-relationship instances, a finite JSON value profile, labelled property graphs, RDF graphs and RDF datasets. SQL NULL/three-valued logic, inclusion dependencies, normal forms, weak entities and diagram layout need further interfaces.

### Object collections

Recorded: finite sets; duplicate-free ordered collections with partial fresh append; existing sequences, multisets (bags), finite maps, arrays, stacks, queues, deques, and priority queues. Specify element equality separately from object identity in any application. Ordered collections use position rather than a sorting order; their full concatenation is not closed under uniqueness. Finite-insertion and fresh-append induction principles, commuting insertions, append injectivity, and order-sensitive equality are recorded. Also recorded: set-valued multimaps, finite fused iterators, infinite total streams, prefix dictionaries, allocated heap stores and disjoint-set representatives. Object lifetimes, ownership/alias permissions, effectful iteration and collection subtyping need further interfaces.

### Languages and computation

Recorded: arbitrary formal languages of finite words; regular languages; epsilon-free nondeterministic finite automata; total deterministic finite automata; context-free grammars; deterministic one-tape Turing machines. Recognition, generation, language equality, and machine identity are distinct. Selected claims cover language concatenation laws, star induction, regular Boolean closure, DFA/NFA run composition and invariants, NFA subset construction, DFA emptiness by reachability, CFG context closure and derivation induction, deterministic machine outcomes, and decider complementation, with explicit premises and editorial proof sketches. Epsilon-NFAs, pushdown automata, computability reductions, complexity classes, and lambda calculus remain roadmap topics.

### Behavior and transition systems

Recorded: action-labelled transition systems, strong finite partial-trace equivalence, and finite serial state-labelled Kripke structures. These connect to existing transition systems, simulation, bisimulation, safety, and liveness. Recorded principles include finite labelled-path induction, trace residuals and deterministic successor matching, Kripke path invariants and lasso existence, modal necessitation and syntax induction, temporal invariant reasoning, and the least-fixed-point characterization of strong until. Finite traces omit termination and divergence information; weak traces, acceptance-sensitive equivalence, fairness, and probabilistic/timed behavior require explicit variants.

### Parallel and distributed systems

Interleaving and event-order models; shared memory; channels; atomic operations; happens-before; linearizability; consistency models; synchronization; safety and liveness; refinement and simulation.

## Discovery sources

Wikipedia topic lists are indexes for candidate discovery, not normative sources for formal claims. Wikidata supports entity identity and cross-links. Prefer standards, textbooks, original papers, and formal libraries for axioms and theorems.

- [Lists of mathematics topics](https://en.wikipedia.org/wiki/Lists_of_mathematics_topics)
- [Mathematical structure](https://en.wikipedia.org/wiki/Mathematical_structure)
- [List of mathematical logic topics](https://en.wikipedia.org/wiki/List_of_mathematical_logic_topics)
- [List of abstract algebra topics](https://en.wikipedia.org/wiki/List_of_abstract_algebra_topics)
- [List of order theory topics](https://en.wikipedia.org/wiki/List_of_order_theory_topics)
- [List of graph theory topics](https://en.wikipedia.org/wiki/List_of_graph_theory_topics)
- [List of data structures](https://en.wikipedia.org/wiki/List_of_data_structures)
- [Wikidata mathematical structure](https://www.wikidata.org/wiki/Q748349)
