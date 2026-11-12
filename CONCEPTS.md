# Mathematical abstractions

Each linked page contains the definition, assumptions, operations, claims, provenance, typed relationships, and backlinks.

## Browse by subject

Subjects organize navigation. They do not imply specialization or transfer mathematical claims.

- **Algebra**
  - [Boolean algebra](concepts/BooleanAlgebra.md)
  - [Field](concepts/Field.md)
  - [Finite field (Galois field)](concepts/FiniteField.md)
  - [Group](concepts/Group.md)
  - [Idempotent semiring (additively idempotent, unital)](concepts/IdempotentSemiring.md)
  - [Mathematical integers](concepts/Integer.md)
  - [Min-plus semiring (tropical semiring, min convention)](concepts/MinPlusSemiring.md)
  - [Monoid](concepts/Monoid.md)
  - [Unital ring (convention stated)](concepts/Ring.md)
  - [Semigroup](concepts/Semigroup.md)
  - [Semiring](concepts/Semiring.md)
  - [Vector space over a field](concepts/VectorSpace.md)
  - **Linear and multilinear algebra**
    - [Euclidean lattice (discrete integer-span lattice)](concepts/EuclideanLattice.md)
    - [Linear map](concepts/LinearMap.md)
    - [Markov chain (finite-state, discrete-time, time-homogeneous)](concepts/MarkovChain.md)
    - [Finite rectangular matrix over a field](concepts/Matrix.md)
    - [Finitely supported vector](concepts/SparseVector.md)
    - [Tensor of specified valence on a finite-dimensional vector space](concepts/Tensor.md)
    - [Tensor product of vector spaces](concepts/TensorProduct.md)
    - [Vector space over a field](concepts/VectorSpace.md)
    - **Matrix decompositions**
      - [Cholesky decomposition (Hermitian positive definite, lower profile)](concepts/CholeskyDecomposition.md)
      - [Eigendecomposition by a complete eigenbasis (diagonalization)](concepts/EigenDecomposition.md)
      - [Row-pivoted LU decomposition (square PA=LU profile)](concepts/LUDecomposition.md)
      - [Exact structured matrix decomposition witness](concepts/MatrixDecomposition.md)
      - [Full QR decomposition (real or complex, rectangular)](concepts/QRDecomposition.md)
      - [Full singular value decomposition (rectangular real or complex SVD)](concepts/SVD.md)
- **Behavior and transition systems**
  - [Bisimulation](concepts/Bisimulation.md)
  - [Deterministic finite automaton with total transition](concepts/DFA.md)
  - [Finite serial Kripke structure for model checking](concepts/KripkeStructure.md)
  - [Action-labelled transition system with initial states](concepts/LabelledTransitionSystem.md)
  - [Linear temporal logic on infinite discrete traces](concepts/LinearTemporalLogic.md)
  - [Classical propositional modal logic K](concepts/ModalLogic.md)
  - [Nondeterministic finite automaton without epsilon moves](concepts/NFA.md)
  - [Simulation](concepts/Simulation.md)
  - [Strong finite partial-trace equivalence](concepts/TraceEquivalence.md)
  - [Transition System](concepts/TransitionSystem.md)
- **Concurrency and distributed systems**
  - **Behavioral models**
    - [Action-labelled transition system with initial states](concepts/LabelledTransitionSystem.md)
    - [Strong finite partial-trace equivalence](concepts/TraceEquivalence.md)
  - **Correctness properties**
    - [Liveness Property](concepts/LivenessProperty.md)
    - [Safety Property](concepts/SafetyProperty.md)
  - **Ordering and consistency**
    - [Happens Before](concepts/HappensBefore.md)
    - [Linearizability](concepts/Linearizability.md)
    - [Sequential Consistency](concepts/SequentialConsistency.md)
  - **Replication**
    - [State-based CRDT replication algebra](concepts/StateBasedCRDT.md)
  - **Synchronization**
    - **Lock protocols**
      - [Lamport bakery lock protocol](concepts/LamportBakery.md)
    - **Locks**
      - [Lock with compatible access modes](concepts/Lock.md)
      - [Mutex (non-reentrant mutual-exclusion lock)](concepts/Mutex.md)
- **Counting and induction**
  - [Pigeonhole Principle](concepts/PigeonholePrinciple.md)
  - [Structural Induction](concepts/StructuralInduction.md)
- **Cryptography**
  - **Public-key cryptography**
    - [Diffie–Hellman key exchange (prime-order cyclic-group core)](concepts/DiffieHellman.md)
    - [Elliptic curve cryptography group (prime-field short-Weierstrass profile)](concepts/ECC.md)
    - [Elliptic curve Diffie–Hellman (validated full-point profile)](concepts/ECDH.md)
    - [RSA modular-exponentiation primitives (two-prime profile)](concepts/RSA.md)
    - **Lattice-based cryptography**
      - [Closest vector problem (Euclidean search relation)](concepts/CVP.md)
      - [Euclidean lattice (discrete integer-span lattice)](concepts/EuclideanLattice.md)
      - [Learning with errors (finite modular distribution profile)](concepts/LWE.md)
      - [q-ary kernel lattice](concepts/QaryLattice.md)
      - [Short integer solution problem (Euclidean norm profile)](concepts/SIS.md)
      - [Shortest vector problem (Euclidean search relation)](concepts/SVP.md)
  - **Symmetric cryptography**
    - [Nonce-based authenticated encryption with associated data](concepts/AEAD.md)
    - [Advanced Encryption Standard (AES)](concepts/AES.md)
    - [AES-GCM (96-bit nonce, 128-bit tag profile)](concepts/AESGCM.md)
    - [Keyed block cipher](concepts/BlockCipher.md)
    - [Galois/Counter Mode (96-bit IV, 128-bit tag profile)](concepts/GCM.md)
    - [GHASH polynomial accumulator](concepts/GHASH.md)
- **Data structures**
  - **Connectivity structures**
    - [Union Find (disjoint-set union with representatives)](concepts/DisjointSet.md)
  - **Intervals**
    - [Nonempty bounded closed interval](concepts/ClosedInterval.md)
  - **Priority collections**
    - [Finite complete binary min-heap](concepts/BinaryHeap.md)
    - [Priority Queue](concepts/PriorityQueue.md)
  - **Sequential collections**
    - [Fixed-length array](concepts/Array.md)
    - [Deque](concepts/Deque.md)
    - [Finite fused sequence iterator](concepts/FiniteIterator.md)
    - [Ordered collection without duplicates](concepts/OrderedSet.md)
    - [Queue abstract data type](concepts/Queue.md)
    - [Finite sequence (List datatype)](concepts/Sequence.md)
    - [Stack abstract data type](concepts/Stack.md)
    - [Infinite discrete stream](concepts/Stream.md)
  - **Sets and mappings**
    - [Finite database relation under set semantics](concepts/DatabaseRelation.md)
    - [Finite set collection](concepts/FiniteSet.md)
    - [Map](concepts/Map.md)
    - [Finite set-valued multimap](concepts/Multimap.md)
    - [Multiset](concepts/Multiset.md)
    - [Ordered collection without duplicates](concepts/OrderedSet.md)
    - [Finite prefix dictionary](concepts/Trie.md)
  - **Tree structures**
    - [B-tree (balanced multiway search tree)](concepts/BTree.md)
    - [Finite complete binary min-heap](concepts/BinaryHeap.md)
    - [Strict binary search tree](concepts/BinarySearchTree.md)
    - [Finite ordered binary tree with node labels](concepts/BinaryTree.md)
    - [Finite ordered rose tree](concepts/RoseTree.md)
    - [Finite prefix dictionary](concepts/Trie.md)
- **Geometry and manifolds**
  - [Euclidean lattice (discrete integer-span lattice)](concepts/EuclideanLattice.md)
  - [Topological manifold (fixed dimension, without boundary)](concepts/Manifold.md)
  - [Smooth manifold (C∞, without boundary)](concepts/SmoothManifold.md)
  - [Tensor of specified valence on a finite-dimensional vector space](concepts/Tensor.md)
- **Graph theory**
  - [Bayesian network (finite discrete variables)](concepts/BayesianNetwork.md)
  - [Finite ordered binary tree with node labels](concepts/BinaryTree.md)
  - [Finite simple graph with chosen bipartition](concepts/BipartiteGraph.md)
  - [Directed acyclic graph](concepts/DAG.md)
  - [Directed Graph](concepts/DirectedGraph.md)
  - [Finite directed multigraph with edge identities](concepts/DirectedMultigraph.md)
  - [Graph](concepts/Graph.md)
  - [Finite simple undirected hypergraph](concepts/Hypergraph.md)
  - [Finite rooted undirected tree](concepts/RootedTree.md)
  - [Tree](concepts/Tree.md)
  - [Finite real-weighted directed multigraph](concepts/WeightedDirectedGraph.md)
- **Information theory**
  - [Channel capacity (finite DMC, vanishing error)](concepts/ChannelCapacity.md)
  - [Conditional entropy (finite discrete profile)](concepts/ConditionalEntropy.md)
  - [Discrete memoryless channel (stationary finite profile)](concepts/DiscreteMemorylessChannel.md)
  - [Mutual information (finite discrete profile)](concepts/MutualInformation.md)
  - [Relative entropy (finite Kullback–Leibler divergence)](concepts/RelativeEntropy.md)
  - [Shannon entropy (finite discrete profile)](concepts/ShannonEntropy.md)
  - [Finite stochastic channel](concepts/StochasticChannel.md)
  - **Coding theory**
    - **Channel coding**
      - [Finite block code (Hamming profile)](concepts/BlockCode.md)
      - [Euclidean dual of a finite-field linear code](concepts/DualCode.md)
      - [Generator matrix of a linear block code (row convention)](concepts/GeneratorMatrix.md)
      - [Hamming space (finite fixed-length words)](concepts/HammingSpace.md)
      - [Linear block code over a finite field](concepts/LinearBlockCode.md)
      - [Nonlinear finite-field block code](concepts/NonlinearBlockCode.md)
      - [Parity-check matrix of a linear block code (row convention)](concepts/ParityCheckMatrix.md)
      - [Syndrome map of a linear block code](concepts/Syndrome.md)
    - **Source coding**
      - [Finite single-letter distortion measure](concepts/DistortionMeasure.md)
      - [Prefix-free binary source code](concepts/PrefixFreeCode.md)
      - [Rate–distortion function (finite iid source, average cost)](concepts/RateDistortion.md)
      - [Uniquely decodable binary source code](concepts/UniquelyDecodableCode.md)
- **Languages and computation**
  - [Context-free grammar of finite words](concepts/ContextFreeGrammar.md)
  - [Deterministic finite automaton with total transition](concepts/DFA.md)
  - [Formal language of finite words](concepts/FormalLanguage.md)
  - [Nondeterministic finite automaton without epsilon moves](concepts/NFA.md)
  - [Regular language over a finite alphabet](concepts/RegularLanguage.md)
  - [Deterministic one-tape Turing machine](concepts/TuringMachine.md)
- **Logic and proof**
  - [Boolean algebra](concepts/BooleanAlgebra.md)
  - [First-order formula syntax with named variables](concepts/FirstOrderFormula.md)
  - [Classical first-order natural deduction with equality](concepts/FirstOrderNaturalDeduction.md)
  - [Single-sorted first-order signature](concepts/FirstOrderSignature.md)
  - [Functional dependency on a relational schema](concepts/FunctionalDependency.md)
  - [Finite serial Kripke structure for model checking](concepts/KripkeStructure.md)
  - [Linear temporal logic on infinite discrete traces](concepts/LinearTemporalLogic.md)
  - [Classical propositional modal logic K](concepts/ModalLogic.md)
  - [Predicate Logic](concepts/PredicateLogic.md)
  - [Finite propositional formula syntax](concepts/PropositionalFormula.md)
  - [Propositional Logic](concepts/PropositionalLogic.md)
  - [Classical propositional natural deduction](concepts/PropositionalNaturalDeduction.md)
- **Measure theory**
  - [Measurable function](concepts/MeasurableFunction.md)
  - [Measurable space (sigma-algebra on a carrier)](concepts/MeasurableSpace.md)
  - [Measure space (nonnegative countably additive measure)](concepts/MeasureSpace.md)
  - [Probability space (normalized measure)](concepts/ProbabilitySpace.md)
  - [Random variable (measurable random element)](concepts/RandomVariable.md)
- **Numeric computation**
  - [Arbitrary Precision Integer](concepts/ArbitraryPrecisionInteger.md)
  - [IEEE 754 binary128](concepts/Binary128.md)
  - [IEEE 754 binary16](concepts/Binary16.md)
  - [IEEE 754 binary32](concepts/Binary32.md)
  - [IEEE 754 binary64](concepts/Binary64.md)
  - [Fixed-width bit vector](concepts/BitVector.md)
  - [Checked Integer](concepts/CheckedInteger.md)
  - [Exact complex number](concepts/ComplexNumber.md)
  - [Field](concepts/Field.md)
  - [Finite field (Galois field)](concepts/FiniteField.md)
  - [Fixed-width signed integer](concepts/FixedWidthSignedInteger.md)
  - [Fixed-width unsigned integer](concepts/FixedWidthUnsignedInteger.md)
  - [Floating-point type](concepts/FloatingPointType.md)
  - [Mathematical integers](concepts/Integer.md)
  - [Modular Integer](concepts/ModularInteger.md)
  - [Natural Number](concepts/NaturalNumber.md)
  - [Exact rational number](concepts/RationalNumber.md)
  - [Exact real number](concepts/RealNumber.md)
  - [Saturating Integer](concepts/SaturatingInteger.md)
- **Order and fixed points**
  - [Closure Operator](concepts/ClosureOperator.md)
  - [Complete Lattice](concepts/CompleteLattice.md)
  - [Fixed Point](concepts/FixedPoint.md)
  - [Galois Connection](concepts/GaloisConnection.md)
  - [Idempotent semiring (additively idempotent, unital)](concepts/IdempotentSemiring.md)
  - [Join semilattice](concepts/JoinSemilattice.md)
  - [Lattice](concepts/Lattice.md)
  - [Min-plus semiring (tropical semiring, min convention)](concepts/MinPlusSemiring.md)
  - [Monotone Function](concepts/MonotoneFunction.md)
  - [Partial Order](concepts/PartialOrder.md)
  - [Preorder](concepts/Preorder.md)
  - [Total Order](concepts/TotalOrder.md)
  - [Well Founded Relation](concepts/WellFoundedRelation.md)
- **Probability and stochastic models**
  - [Bayesian network (finite discrete variables)](concepts/BayesianNetwork.md)
  - [Conditional probability given a positive-probability event](concepts/ConditionalProbability.md)
  - [Finitely supported probability distribution](concepts/FiniteDistribution.md)
  - [Markov chain (finite-state, discrete-time, time-homogeneous)](concepts/MarkovChain.md)
  - [Probability space (normalized measure)](concepts/ProbabilitySpace.md)
  - [Random variable (measurable random element)](concepts/RandomVariable.md)
- **Programming-language semantics**
  - [Bisimulation](concepts/Bisimulation.md)
  - [Fixed-width bit vector](concepts/BitVector.md)
  - [Fixed-width signed integer](concepts/FixedWidthSignedInteger.md)
  - [Fixed-width unsigned integer](concepts/FixedWidthUnsignedInteger.md)
  - [Floating-point type](concepts/FloatingPointType.md)
  - [Finite allocated heap store](concepts/HeapStore.md)
  - [Hoare Triple](concepts/HoareTriple.md)
  - [Action-labelled transition system with initial states](concepts/LabelledTransitionSystem.md)
  - [Loop Invariant](concepts/LoopInvariant.md)
  - [Partial function](concepts/PartialFunction.md)
  - [Simulation](concepts/Simulation.md)
  - [Termination Variant](concepts/TerminationVariant.md)
  - [Transition System](concepts/TransitionSystem.md)
  - [Deterministic one-tape Turing machine](concepts/TuringMachine.md)
  - [Weakest Precondition](concepts/WeakestPrecondition.md)
  - **Generic programming**
    - [Resolved generic argument binding with ordered defaults](concepts/GenericArgumentBinding.md)
    - [Finite kinded generic parameter signature](concepts/GenericSignature.md)
    - [Contextual parametric declaration instantiation](concepts/ParametricInstantiation.md)
    - **Java generics**
      - [Java bounded parameterized types and nominal subtyping](concepts/JavaParameterizedType.md)
      - [Java type erasure and selected reifiability rules](concepts/JavaTypeErasure.md)
      - [Java generic inference constraints and resolution obligations](concepts/JavaTypeInference.md)
      - [Java wildcard capture with fresh bounded variables](concepts/JavaWildcardCapture.md)
    - **Template metaprogramming**
      - [Checked signed-integer constant-evaluation fragment](concepts/CompileTimeEvaluation.md)
      - [Definition/instantiation lookup for dependent calls](concepts/DependentNameLookup.md)
      - [Normalized template constraints with atomic identity](concepts/TemplateConstraint.md)
      - [Kinded partial template metafunction](concepts/TemplateMetafunction.md)
      - [Ordered template packs and structural expansion](concepts/TemplateParameterPack.md)
      - [Class template partial-specialization selection](concepts/TemplateSpecialization.md)
      - [Ordered substitution with immediate-context failure](concepts/TemplateSubstitution.md)
    - **VHDL generics**
      - [VHDL generic elaboration and static structural generation](concepts/VHDLGenericElaboration.md)
      - [VHDL generic interfaces and whole-formal association](concepts/VHDLGenericInterface.md)
  - **Object-oriented semantics**
    - [Behavioral subtyping with explicit history constraints](concepts/BehavioralSubtyping.md)
    - [Single-inheritance class table and dynamic dispatch](concepts/ClassTable.md)
    - [Exclusive finite-heap separation predicates](concepts/HeapSeparation.md)
    - [Relational method contract with write effects](concepts/MethodContract.md)
    - [Sequential object heap with reference identity](concepts/ObjectHeap.md)
    - [Visible-state object invariant protocol](concepts/ObjectInvariant.md)
- **Relational data modelling**
  - [Finite database relation under bag semantics](concepts/BagRelation.md)
  - [Candidate key relative to functional dependencies](concepts/CandidateKey.md)
  - [Finite database relation under set semantics](concepts/DatabaseRelation.md)
  - [Finite JSON document value (interoperable profile)](concepts/DocumentValue.md)
  - [Finite typed entity-relationship instance](concepts/EntityRelationshipModel.md)
  - [Functional dependency on a relational schema](concepts/FunctionalDependency.md)
  - [Finite labelled property graph (single-valued profile)](concepts/PropertyGraph.md)
  - [Finite RDF 1.1 dataset](concepts/RDFDataset.md)
  - [Finite RDF 1.1 graph](concepts/RDFGraph.md)
  - [Named relational schema with attribute domains](concepts/RelationalSchema.md)
- **Set theory and foundations**
  - [Cartesian product](concepts/CartesianProduct.md)
  - [Equivalence relation](concepts/EquivalenceRelation.md)
  - [Finite set collection](concepts/FiniteSet.md)
  - [Total function](concepts/Function.md)
  - [Partial function](concepts/PartialFunction.md)
  - [Partition of a set](concepts/Partition.md)
  - [Power set](concepts/PowerSet.md)
  - [Binary relation](concepts/Relation.md)
  - [Set](concepts/Set.md)
- **Topology**
  - [Topological manifold (fixed dimension, without boundary)](concepts/Manifold.md)
  - [Smooth manifold (C∞, without boundary)](concepts/SmoothManifold.md)
  - [Topological space (topology on a carrier)](concepts/TopologicalSpace.md)
- **Types and semantics**
  - [Finite ordered binary tree with node labels](concepts/BinaryTree.md)
  - [Two-valued Boolean type](concepts/BooleanType.md)
  - [Dependent function (Pi type)](concepts/DependentFunction.md)
  - [Dependent pair (Sigma type)](concepts/DependentPair.md)
  - [Empty type](concepts/EmptyType.md)
  - [Finite carrier with exhaustive enumeration](concepts/FiniteType.md)
  - [Function type](concepts/FunctionType.md)
  - [Option Type](concepts/OptionType.md)
  - [Product Type](concepts/ProductType.md)
  - [Quotient by an equivalence relation](concepts/QuotientType.md)
  - [Named relational schema with attribute domains](concepts/RelationalSchema.md)
  - [Predicate-restricted subtype](concepts/Subtype.md)
  - [Sum Type](concepts/SumType.md)
  - [Free ranked term algebra with variables](concepts/TermAlgebra.md)
  - [Unit type](concepts/UnitType.md)

## Alphabetical index

| Concept | Categories |
| --- | --- |
| [Nonce-based authenticated encryption with associated data](concepts/AEAD.md) | Cryptography → Symmetric cryptography |
| [Advanced Encryption Standard (AES)](concepts/AES.md) | Cryptography → Symmetric cryptography |
| [AES-GCM (96-bit nonce, 128-bit tag profile)](concepts/AESGCM.md) | Cryptography → Symmetric cryptography |
| [Arbitrary Precision Integer](concepts/ArbitraryPrecisionInteger.md) | Numeric computation |
| [Fixed-length array](concepts/Array.md) | Data structures → Sequential collections |
| [B-tree (balanced multiway search tree)](concepts/BTree.md) | Data structures → Tree structures |
| [Finite database relation under bag semantics](concepts/BagRelation.md) | Relational data modelling |
| [Bayesian network (finite discrete variables)](concepts/BayesianNetwork.md) | Probability and stochastic models, Graph theory |
| [Behavioral subtyping with explicit history constraints](concepts/BehavioralSubtyping.md) | Programming-language semantics → Object-oriented semantics |
| [IEEE 754 binary128](concepts/Binary128.md) | Numeric computation |
| [IEEE 754 binary16](concepts/Binary16.md) | Numeric computation |
| [IEEE 754 binary32](concepts/Binary32.md) | Numeric computation |
| [IEEE 754 binary64](concepts/Binary64.md) | Numeric computation |
| [Finite complete binary min-heap](concepts/BinaryHeap.md) | Data structures → Tree structures, Data structures → Priority collections |
| [Strict binary search tree](concepts/BinarySearchTree.md) | Data structures → Tree structures |
| [Finite ordered binary tree with node labels](concepts/BinaryTree.md) | Data structures → Tree structures, Types and semantics, Graph theory |
| [Finite simple graph with chosen bipartition](concepts/BipartiteGraph.md) | Graph theory |
| [Bisimulation](concepts/Bisimulation.md) | Programming-language semantics, Behavior and transition systems |
| [Fixed-width bit vector](concepts/BitVector.md) | Numeric computation, Programming-language semantics |
| [Keyed block cipher](concepts/BlockCipher.md) | Cryptography → Symmetric cryptography |
| [Finite block code (Hamming profile)](concepts/BlockCode.md) | Information theory → Coding theory → Channel coding |
| [Boolean algebra](concepts/BooleanAlgebra.md) | Logic and proof, Algebra |
| [Two-valued Boolean type](concepts/BooleanType.md) | Types and semantics |
| [Closest vector problem (Euclidean search relation)](concepts/CVP.md) | Cryptography → Public-key cryptography → Lattice-based cryptography |
| [Candidate key relative to functional dependencies](concepts/CandidateKey.md) | Relational data modelling |
| [Cartesian product](concepts/CartesianProduct.md) | Set theory and foundations |
| [Channel capacity (finite DMC, vanishing error)](concepts/ChannelCapacity.md) | Information theory |
| [Checked Integer](concepts/CheckedInteger.md) | Numeric computation |
| [Cholesky decomposition (Hermitian positive definite, lower profile)](concepts/CholeskyDecomposition.md) | Algebra → Linear and multilinear algebra → Matrix decompositions |
| [Single-inheritance class table and dynamic dispatch](concepts/ClassTable.md) | Programming-language semantics → Object-oriented semantics |
| [Nonempty bounded closed interval](concepts/ClosedInterval.md) | Data structures → Intervals |
| [Closure Operator](concepts/ClosureOperator.md) | Order and fixed points |
| [Checked signed-integer constant-evaluation fragment](concepts/CompileTimeEvaluation.md) | Programming-language semantics → Generic programming → Template metaprogramming |
| [Complete Lattice](concepts/CompleteLattice.md) | Order and fixed points |
| [Exact complex number](concepts/ComplexNumber.md) | Numeric computation |
| [Conditional entropy (finite discrete profile)](concepts/ConditionalEntropy.md) | Information theory |
| [Conditional probability given a positive-probability event](concepts/ConditionalProbability.md) | Probability and stochastic models |
| [Context-free grammar of finite words](concepts/ContextFreeGrammar.md) | Languages and computation |
| [Directed acyclic graph](concepts/DAG.md) | Graph theory |
| [Deterministic finite automaton with total transition](concepts/DFA.md) | Languages and computation, Behavior and transition systems |
| [Finite database relation under set semantics](concepts/DatabaseRelation.md) | Relational data modelling, Data structures → Sets and mappings |
| [Dependent function (Pi type)](concepts/DependentFunction.md) | Types and semantics |
| [Definition/instantiation lookup for dependent calls](concepts/DependentNameLookup.md) | Programming-language semantics → Generic programming → Template metaprogramming |
| [Dependent pair (Sigma type)](concepts/DependentPair.md) | Types and semantics |
| [Deque](concepts/Deque.md) | Data structures → Sequential collections |
| [Diffie–Hellman key exchange (prime-order cyclic-group core)](concepts/DiffieHellman.md) | Cryptography → Public-key cryptography |
| [Directed Graph](concepts/DirectedGraph.md) | Graph theory |
| [Finite directed multigraph with edge identities](concepts/DirectedMultigraph.md) | Graph theory |
| [Discrete memoryless channel (stationary finite profile)](concepts/DiscreteMemorylessChannel.md) | Information theory |
| [Union Find (disjoint-set union with representatives)](concepts/DisjointSet.md) | Data structures → Connectivity structures |
| [Finite single-letter distortion measure](concepts/DistortionMeasure.md) | Information theory → Coding theory → Source coding |
| [Finite JSON document value (interoperable profile)](concepts/DocumentValue.md) | Relational data modelling |
| [Euclidean dual of a finite-field linear code](concepts/DualCode.md) | Information theory → Coding theory → Channel coding |
| [Elliptic curve cryptography group (prime-field short-Weierstrass profile)](concepts/ECC.md) | Cryptography → Public-key cryptography |
| [Elliptic curve Diffie–Hellman (validated full-point profile)](concepts/ECDH.md) | Cryptography → Public-key cryptography |
| [Eigendecomposition by a complete eigenbasis (diagonalization)](concepts/EigenDecomposition.md) | Algebra → Linear and multilinear algebra → Matrix decompositions |
| [Empty type](concepts/EmptyType.md) | Types and semantics |
| [Finite typed entity-relationship instance](concepts/EntityRelationshipModel.md) | Relational data modelling |
| [Equivalence relation](concepts/EquivalenceRelation.md) | Set theory and foundations |
| [Euclidean lattice (discrete integer-span lattice)](concepts/EuclideanLattice.md) | Geometry and manifolds, Algebra → Linear and multilinear algebra, Cryptography → Public-key cryptography → Lattice-based cryptography |
| [Field](concepts/Field.md) | Algebra, Numeric computation |
| [Finitely supported probability distribution](concepts/FiniteDistribution.md) | Probability and stochastic models |
| [Finite field (Galois field)](concepts/FiniteField.md) | Algebra, Numeric computation |
| [Finite fused sequence iterator](concepts/FiniteIterator.md) | Data structures → Sequential collections |
| [Finite set collection](concepts/FiniteSet.md) | Data structures → Sets and mappings, Set theory and foundations |
| [Finite carrier with exhaustive enumeration](concepts/FiniteType.md) | Types and semantics |
| [First-order formula syntax with named variables](concepts/FirstOrderFormula.md) | Logic and proof |
| [Classical first-order natural deduction with equality](concepts/FirstOrderNaturalDeduction.md) | Logic and proof |
| [Single-sorted first-order signature](concepts/FirstOrderSignature.md) | Logic and proof |
| [Fixed Point](concepts/FixedPoint.md) | Order and fixed points |
| [Fixed-width signed integer](concepts/FixedWidthSignedInteger.md) | Numeric computation, Programming-language semantics |
| [Fixed-width unsigned integer](concepts/FixedWidthUnsignedInteger.md) | Numeric computation, Programming-language semantics |
| [Floating-point type](concepts/FloatingPointType.md) | Numeric computation, Programming-language semantics |
| [Formal language of finite words](concepts/FormalLanguage.md) | Languages and computation |
| [Total function](concepts/Function.md) | Set theory and foundations |
| [Function type](concepts/FunctionType.md) | Types and semantics |
| [Functional dependency on a relational schema](concepts/FunctionalDependency.md) | Relational data modelling, Logic and proof |
| [Galois/Counter Mode (96-bit IV, 128-bit tag profile)](concepts/GCM.md) | Cryptography → Symmetric cryptography |
| [GHASH polynomial accumulator](concepts/GHASH.md) | Cryptography → Symmetric cryptography |
| [Galois Connection](concepts/GaloisConnection.md) | Order and fixed points |
| [Generator matrix of a linear block code (row convention)](concepts/GeneratorMatrix.md) | Information theory → Coding theory → Channel coding |
| [Resolved generic argument binding with ordered defaults](concepts/GenericArgumentBinding.md) | Programming-language semantics → Generic programming |
| [Finite kinded generic parameter signature](concepts/GenericSignature.md) | Programming-language semantics → Generic programming |
| [Graph](concepts/Graph.md) | Graph theory |
| [Group](concepts/Group.md) | Algebra |
| [Hamming space (finite fixed-length words)](concepts/HammingSpace.md) | Information theory → Coding theory → Channel coding |
| [Happens Before](concepts/HappensBefore.md) | Concurrency and distributed systems → Ordering and consistency |
| [Exclusive finite-heap separation predicates](concepts/HeapSeparation.md) | Programming-language semantics → Object-oriented semantics |
| [Finite allocated heap store](concepts/HeapStore.md) | Programming-language semantics |
| [Hoare Triple](concepts/HoareTriple.md) | Programming-language semantics |
| [Finite simple undirected hypergraph](concepts/Hypergraph.md) | Graph theory |
| [Idempotent semiring (additively idempotent, unital)](concepts/IdempotentSemiring.md) | Algebra, Order and fixed points |
| [Mathematical integers](concepts/Integer.md) | Numeric computation, Algebra |
| [Java bounded parameterized types and nominal subtyping](concepts/JavaParameterizedType.md) | Programming-language semantics → Generic programming → Java generics |
| [Java type erasure and selected reifiability rules](concepts/JavaTypeErasure.md) | Programming-language semantics → Generic programming → Java generics |
| [Java generic inference constraints and resolution obligations](concepts/JavaTypeInference.md) | Programming-language semantics → Generic programming → Java generics |
| [Java wildcard capture with fresh bounded variables](concepts/JavaWildcardCapture.md) | Programming-language semantics → Generic programming → Java generics |
| [Join semilattice](concepts/JoinSemilattice.md) | Order and fixed points |
| [Finite serial Kripke structure for model checking](concepts/KripkeStructure.md) | Behavior and transition systems, Logic and proof |
| [Row-pivoted LU decomposition (square PA=LU profile)](concepts/LUDecomposition.md) | Algebra → Linear and multilinear algebra → Matrix decompositions |
| [Learning with errors (finite modular distribution profile)](concepts/LWE.md) | Cryptography → Public-key cryptography → Lattice-based cryptography |
| [Action-labelled transition system with initial states](concepts/LabelledTransitionSystem.md) | Behavior and transition systems, Programming-language semantics, Concurrency and distributed systems → Behavioral models |
| [Lamport bakery lock protocol](concepts/LamportBakery.md) | Concurrency and distributed systems → Synchronization → Lock protocols |
| [Lattice](concepts/Lattice.md) | Order and fixed points |
| [Linear block code over a finite field](concepts/LinearBlockCode.md) | Information theory → Coding theory → Channel coding |
| [Linear map](concepts/LinearMap.md) | Algebra → Linear and multilinear algebra |
| [Linear temporal logic on infinite discrete traces](concepts/LinearTemporalLogic.md) | Logic and proof, Behavior and transition systems |
| [Linearizability](concepts/Linearizability.md) | Concurrency and distributed systems → Ordering and consistency |
| [Liveness Property](concepts/LivenessProperty.md) | Concurrency and distributed systems → Correctness properties |
| [Lock with compatible access modes](concepts/Lock.md) | Concurrency and distributed systems → Synchronization → Locks |
| [Loop Invariant](concepts/LoopInvariant.md) | Programming-language semantics |
| [Topological manifold (fixed dimension, without boundary)](concepts/Manifold.md) | Geometry and manifolds, Topology |
| [Map](concepts/Map.md) | Data structures → Sets and mappings |
| [Markov chain (finite-state, discrete-time, time-homogeneous)](concepts/MarkovChain.md) | Probability and stochastic models, Algebra → Linear and multilinear algebra |
| [Finite rectangular matrix over a field](concepts/Matrix.md) | Algebra → Linear and multilinear algebra |
| [Exact structured matrix decomposition witness](concepts/MatrixDecomposition.md) | Algebra → Linear and multilinear algebra → Matrix decompositions |
| [Measurable function](concepts/MeasurableFunction.md) | Measure theory |
| [Measurable space (sigma-algebra on a carrier)](concepts/MeasurableSpace.md) | Measure theory |
| [Measure space (nonnegative countably additive measure)](concepts/MeasureSpace.md) | Measure theory |
| [Relational method contract with write effects](concepts/MethodContract.md) | Programming-language semantics → Object-oriented semantics |
| [Min-plus semiring (tropical semiring, min convention)](concepts/MinPlusSemiring.md) | Algebra, Order and fixed points |
| [Classical propositional modal logic K](concepts/ModalLogic.md) | Logic and proof, Behavior and transition systems |
| [Modular Integer](concepts/ModularInteger.md) | Numeric computation |
| [Monoid](concepts/Monoid.md) | Algebra |
| [Monotone Function](concepts/MonotoneFunction.md) | Order and fixed points |
| [Finite set-valued multimap](concepts/Multimap.md) | Data structures → Sets and mappings |
| [Multiset](concepts/Multiset.md) | Data structures → Sets and mappings |
| [Mutex (non-reentrant mutual-exclusion lock)](concepts/Mutex.md) | Concurrency and distributed systems → Synchronization → Locks |
| [Mutual information (finite discrete profile)](concepts/MutualInformation.md) | Information theory |
| [Nondeterministic finite automaton without epsilon moves](concepts/NFA.md) | Languages and computation, Behavior and transition systems |
| [Natural Number](concepts/NaturalNumber.md) | Numeric computation |
| [Nonlinear finite-field block code](concepts/NonlinearBlockCode.md) | Information theory → Coding theory → Channel coding |
| [Sequential object heap with reference identity](concepts/ObjectHeap.md) | Programming-language semantics → Object-oriented semantics |
| [Visible-state object invariant protocol](concepts/ObjectInvariant.md) | Programming-language semantics → Object-oriented semantics |
| [Option Type](concepts/OptionType.md) | Types and semantics |
| [Ordered collection without duplicates](concepts/OrderedSet.md) | Data structures → Sets and mappings, Data structures → Sequential collections |
| [Contextual parametric declaration instantiation](concepts/ParametricInstantiation.md) | Programming-language semantics → Generic programming |
| [Parity-check matrix of a linear block code (row convention)](concepts/ParityCheckMatrix.md) | Information theory → Coding theory → Channel coding |
| [Partial function](concepts/PartialFunction.md) | Set theory and foundations, Programming-language semantics |
| [Partial Order](concepts/PartialOrder.md) | Order and fixed points |
| [Partition of a set](concepts/Partition.md) | Set theory and foundations |
| [Pigeonhole Principle](concepts/PigeonholePrinciple.md) | Counting and induction |
| [Power set](concepts/PowerSet.md) | Set theory and foundations |
| [Predicate Logic](concepts/PredicateLogic.md) | Logic and proof |
| [Prefix-free binary source code](concepts/PrefixFreeCode.md) | Information theory → Coding theory → Source coding |
| [Preorder](concepts/Preorder.md) | Order and fixed points |
| [Priority Queue](concepts/PriorityQueue.md) | Data structures → Priority collections |
| [Probability space (normalized measure)](concepts/ProbabilitySpace.md) | Probability and stochastic models, Measure theory |
| [Product Type](concepts/ProductType.md) | Types and semantics |
| [Finite labelled property graph (single-valued profile)](concepts/PropertyGraph.md) | Relational data modelling |
| [Finite propositional formula syntax](concepts/PropositionalFormula.md) | Logic and proof |
| [Propositional Logic](concepts/PropositionalLogic.md) | Logic and proof |
| [Classical propositional natural deduction](concepts/PropositionalNaturalDeduction.md) | Logic and proof |
| [Full QR decomposition (real or complex, rectangular)](concepts/QRDecomposition.md) | Algebra → Linear and multilinear algebra → Matrix decompositions |
| [q-ary kernel lattice](concepts/QaryLattice.md) | Cryptography → Public-key cryptography → Lattice-based cryptography |
| [Queue abstract data type](concepts/Queue.md) | Data structures → Sequential collections |
| [Quotient by an equivalence relation](concepts/QuotientType.md) | Types and semantics |
| [Finite RDF 1.1 dataset](concepts/RDFDataset.md) | Relational data modelling |
| [Finite RDF 1.1 graph](concepts/RDFGraph.md) | Relational data modelling |
| [RSA modular-exponentiation primitives (two-prime profile)](concepts/RSA.md) | Cryptography → Public-key cryptography |
| [Random variable (measurable random element)](concepts/RandomVariable.md) | Probability and stochastic models, Measure theory |
| [Rate–distortion function (finite iid source, average cost)](concepts/RateDistortion.md) | Information theory → Coding theory → Source coding |
| [Exact rational number](concepts/RationalNumber.md) | Numeric computation |
| [Exact real number](concepts/RealNumber.md) | Numeric computation |
| [Regular language over a finite alphabet](concepts/RegularLanguage.md) | Languages and computation |
| [Binary relation](concepts/Relation.md) | Set theory and foundations |
| [Named relational schema with attribute domains](concepts/RelationalSchema.md) | Relational data modelling, Types and semantics |
| [Relative entropy (finite Kullback–Leibler divergence)](concepts/RelativeEntropy.md) | Information theory |
| [Unital ring (convention stated)](concepts/Ring.md) | Algebra |
| [Finite rooted undirected tree](concepts/RootedTree.md) | Graph theory |
| [Finite ordered rose tree](concepts/RoseTree.md) | Data structures → Tree structures |
| [Short integer solution problem (Euclidean norm profile)](concepts/SIS.md) | Cryptography → Public-key cryptography → Lattice-based cryptography |
| [Full singular value decomposition (rectangular real or complex SVD)](concepts/SVD.md) | Algebra → Linear and multilinear algebra → Matrix decompositions |
| [Shortest vector problem (Euclidean search relation)](concepts/SVP.md) | Cryptography → Public-key cryptography → Lattice-based cryptography |
| [Safety Property](concepts/SafetyProperty.md) | Concurrency and distributed systems → Correctness properties |
| [Saturating Integer](concepts/SaturatingInteger.md) | Numeric computation |
| [Semigroup](concepts/Semigroup.md) | Algebra |
| [Semiring](concepts/Semiring.md) | Algebra |
| [Finite sequence (List datatype)](concepts/Sequence.md) | Data structures → Sequential collections |
| [Sequential Consistency](concepts/SequentialConsistency.md) | Concurrency and distributed systems → Ordering and consistency |
| [Set](concepts/Set.md) | Set theory and foundations |
| [Shannon entropy (finite discrete profile)](concepts/ShannonEntropy.md) | Information theory |
| [Simulation](concepts/Simulation.md) | Programming-language semantics, Behavior and transition systems |
| [Smooth manifold (C∞, without boundary)](concepts/SmoothManifold.md) | Geometry and manifolds, Topology |
| [Finitely supported vector](concepts/SparseVector.md) | Algebra → Linear and multilinear algebra |
| [Stack abstract data type](concepts/Stack.md) | Data structures → Sequential collections |
| [State-based CRDT replication algebra](concepts/StateBasedCRDT.md) | Concurrency and distributed systems → Replication |
| [Finite stochastic channel](concepts/StochasticChannel.md) | Information theory |
| [Infinite discrete stream](concepts/Stream.md) | Data structures → Sequential collections |
| [Structural Induction](concepts/StructuralInduction.md) | Counting and induction |
| [Predicate-restricted subtype](concepts/Subtype.md) | Types and semantics |
| [Sum Type](concepts/SumType.md) | Types and semantics |
| [Syndrome map of a linear block code](concepts/Syndrome.md) | Information theory → Coding theory → Channel coding |
| [Normalized template constraints with atomic identity](concepts/TemplateConstraint.md) | Programming-language semantics → Generic programming → Template metaprogramming |
| [Kinded partial template metafunction](concepts/TemplateMetafunction.md) | Programming-language semantics → Generic programming → Template metaprogramming |
| [Ordered template packs and structural expansion](concepts/TemplateParameterPack.md) | Programming-language semantics → Generic programming → Template metaprogramming |
| [Class template partial-specialization selection](concepts/TemplateSpecialization.md) | Programming-language semantics → Generic programming → Template metaprogramming |
| [Ordered substitution with immediate-context failure](concepts/TemplateSubstitution.md) | Programming-language semantics → Generic programming → Template metaprogramming |
| [Tensor of specified valence on a finite-dimensional vector space](concepts/Tensor.md) | Algebra → Linear and multilinear algebra, Geometry and manifolds |
| [Tensor product of vector spaces](concepts/TensorProduct.md) | Algebra → Linear and multilinear algebra |
| [Free ranked term algebra with variables](concepts/TermAlgebra.md) | Types and semantics |
| [Termination Variant](concepts/TerminationVariant.md) | Programming-language semantics |
| [Topological space (topology on a carrier)](concepts/TopologicalSpace.md) | Topology |
| [Total Order](concepts/TotalOrder.md) | Order and fixed points |
| [Strong finite partial-trace equivalence](concepts/TraceEquivalence.md) | Behavior and transition systems, Concurrency and distributed systems → Behavioral models |
| [Transition System](concepts/TransitionSystem.md) | Programming-language semantics, Behavior and transition systems |
| [Tree](concepts/Tree.md) | Graph theory |
| [Finite prefix dictionary](concepts/Trie.md) | Data structures → Tree structures, Data structures → Sets and mappings |
| [Deterministic one-tape Turing machine](concepts/TuringMachine.md) | Languages and computation, Programming-language semantics |
| [Uniquely decodable binary source code](concepts/UniquelyDecodableCode.md) | Information theory → Coding theory → Source coding |
| [Unit type](concepts/UnitType.md) | Types and semantics |
| [VHDL generic elaboration and static structural generation](concepts/VHDLGenericElaboration.md) | Programming-language semantics → Generic programming → VHDL generics |
| [VHDL generic interfaces and whole-formal association](concepts/VHDLGenericInterface.md) | Programming-language semantics → Generic programming → VHDL generics |
| [Vector space over a field](concepts/VectorSpace.md) | Algebra → Linear and multilinear algebra, Algebra |
| [Weakest Precondition](concepts/WeakestPrecondition.md) | Programming-language semantics |
| [Finite real-weighted directed multigraph](concepts/WeightedDirectedGraph.md) | Graph theory |
| [Well Founded Relation](concepts/WellFoundedRelation.md) | Order and fixed points |
