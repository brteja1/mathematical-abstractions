---
name: abstraction-discovery
description: Inspect unannotated software, data structures, and APIs to discover candidate mathematical abstractions, identify hidden assumptions and broken algebraic laws, and recommend principled refactorings.
---

# Discover mathematical abstractions in software

Inspect existing software components, algorithms, and data structures to uncover their underlying mathematical abstractions. Identify implicit invariants, detect violated algebraic laws, and recommend principled refactorings grounded in the catalog.

## Inspect code before querying the catalog

For large codebases, **do not read files at random**. Use grep to count first, then read a bounded representative sample. This keeps agent context bounded and results comparable across runs.

### Step 1 — Discover what source extensions the project uses

Before grepping for patterns, find the project's actual source file types so you grep the right files:

```sh
# List source extensions by frequency — use this to build your --include flags
find <target_dir> -type f -not -path '*/.git/*' \
  | sed 's/.*\.//' | sort | uniq -c | sort -rn | head -20
```

Pick the top source-code extensions from that output (ignore build artifacts, data files, lockfiles). Common ones include `.c .cpp .cc .cxx .h .hpp .java .kt .py .go .rs .ts .js .cs .swift .rb .scala .ml` — but always confirm against the project's actual output rather than assuming.

### Step 2 — Count before reading

Run grep over the target scope using the extensions you discovered. Build the `--include` flags from Step 1:

```sh
# Example with discovered extensions (adapt the list):
EXTS=(c cpp cc cxx h hpp java kt py go rs ts js cs swift rb scala)
INCLUDES=$(printf -- '--include="*.%s" ' "${EXTS[@]}")

# Binary combination operations — fold/reduce/merge/combine/append signatures
grep -rn $INCLUDES \
  -E '\b(combine|merge|fold|reduce|append|concat|accumulate)\b' \
  <target_dir> | wc -l

# Comparison / ordering functions
grep -rn $INCLUDES \
  -E '\b(compare|compareTo|cmp|lt|lte|gt|gte|lessThan|greaterThan)\b' \
  <target_dir> | wc -l

# Map / transform / projection operations
grep -rn $INCLUDES \
  -E '\b(map|fmap|transform|project|select|convert)\b' \
  <target_dir> | wc -l

# Identity / neutral / zero / empty initialization
grep -rn $INCLUDES \
  -E '\b(empty|zero|identity|neutral|initial|default)\b' \
  <target_dir> | wc -l
```

Record the raw counts. **Do not read any file yet.** Counts determine which pattern to investigate and how many files to sample.

### Step 3 — Read stratified across the full density range

Rank all matching files by hit density, then split them into three tiers — high, mid, and low — and read from each tier. Reading only the densest files misses the edges of a pattern: low-density files often contain new call-sites, edge-case usage, or partial implementations that change the diagnosis.

Get the full per-file ranked list first:

```sh
grep -rn $INCLUDES -E '<pattern>' <target_dir> \
  | cut -d: -f1 | sort | uniq -c | sort -rn \
  > /tmp/density_ranked.txt
cat /tmp/density_ranked.txt    # inspect the full list before deciding sample size
wc -l /tmp/density_ranked.txt  # total matching files
```

Then apply stratified sampling based on total matching file count:

| Matching files | High-density tier | Mid-density tier | Low-density tier | Total files read |
| --- | --- | --- | --- | --- |
| 1 – 20 | all | — | — | all |
| 21 – 60 | top 10 | middle 5 | bottom 5 | 20 |
| 61 – 150 | top 15 | middle 10 | bottom 5 | 30 |
| 151 – 400 | top 20 | middle 15 | bottom 10 | 45 |
| > 400 | top 25 | middle 20 | bottom 15 | 60 |

Compute tier boundaries from the ranked list:

```sh
TOTAL=$(wc -l < /tmp/density_ranked.txt)
# High tier: lines 1..H  (top of ranked list)
# Mid tier:  lines around TOTAL/2 ± window
# Low tier:  last L lines (bottom of ranked list)
head -<H> /tmp/density_ranked.txt          # high-density files
sed -n "$((TOTAL/2 - W)),$((TOTAL/2 + W))p" /tmp/density_ranked.txt  # mid
tail -<L> /tmp/density_ranked.txt          # low-density files
```

> [!NOTE]
> The goal is to read as many files as agent context allows; these numbers are **minimums per tier**, not caps. If context permits, extend the high and mid tiers further before stopping. State in the report: total matching files, tier counts read, and any tiers where reading was cut short.

### Step 4 — Identify behavioral patterns from the sample

From the files read, analyze concrete behavior:

- **Signatures and Arity**: Identify binary combination operations `(A, A) -> A`, binary relations `(A, A) -> Bool`, state transitions `(State, Event) -> State`, partial projections, and observers.
- **Identity Elements and Defaults**: Check how empty, zero, or initial cases are initialized and whether an explicit neutral value exists.
- **State Mutation and Observability**: Determine whether objects are persistent, mutable in-place, or stateful; define what constitutes observable equality for results.
- **Error and Edge Handling**: Check boundary conditions, null/empty collections, numeric overflow, rounding, and partiality.

Do not assume a method named `combine` is associative or that a `compare` function forms a total order. Unannotated code often implements an incomplete or subtly broken abstraction.

## Inventory existing abstractions and count their uses

Before identifying duplication or querying the catalog, establish what the codebase already provides. Without this step, **missing abstractions** (the pattern exists only as hand-written copies) and **unused abstractions** (an abstraction exists but is bypassed in favour of copies) are easy to confuse — they look identical from the outside but require opposite remedies.

**Step 1 — List existing abstractions in the codebase:**

Search for interfaces, base classes, type aliases, utility modules, and helper functions that are already intended to capture a reusable pattern. For each, record:

| Field | What to record |
| --- | --- |
| Name / locator | File path, class/interface/function name |
| Intended role | What the abstraction is supposed to do (from name, doc, or type signature) |
| Formal interface | Key signatures, type parameters, constraints |
| Test coverage | Whether there are dedicated unit or property tests for the abstraction itself |

**Step 2 — Count uses vs hand-written copies:**

For each abstraction found, count:
- **Uses**: call-sites that go through the abstraction (import + invoke the shared helper/interface).
- **Hand-written copies**: sites that re-implement the same pattern inline without using the abstraction.

Produce a simple tally:

```
Abstraction          | Uses | Copies | Verdict
---------------------|------|--------|-----------------------------------
EventReducer<S,E>    |   2  |   7    | UNDERUSED — 7 copies bypass it
MergeStrategy        |   0  |   4    | UNUSED — never adopted, 4 copies
SortComparator<T>    |   9  |   0    | WELL-USED — no action needed
```

**Interpret the tally before proceeding:**

| Pattern | Diagnosis | Action |
| --- | --- | --- |
| Many copies, abstraction missing | Missing abstraction | Recommend introducing the abstraction |
| Abstraction exists, many copies bypass it | Underused abstraction | Recommend migrating copies to the existing abstraction; investigate why it was bypassed (API friction, discoverability, missing features) |
| Abstraction exists, zero uses | Unused abstraction | Recommend removing or redesigning it; do not add more copies |
| Abstraction exists, well used, few/no copies | Healthy | No structural action; proceed to algebraic analysis if relevant |

> [!IMPORTANT]
> Do not recommend creating a new abstraction when an underused one already covers the pattern. Fix adoption, not the absence.

## Identify structural duplication before reaching for algebraic labels

Most of the value in abstraction discovery is **structural**, not algebraic. Before querying the catalog for laws, determine whether the code is primarily a *refactoring candidate* rather than a hidden algebraic structure. Forcing an algebraic name onto a duplication problem produces an over-engineered solution.

**Scan for structural duplication first:**

| Signal | What to look for | Likely remedy |
| --- | --- | --- |
| Copy-paste logic | Near-identical blocks differing only in a type, field name, or constant | Extract a shared helper or parameterize |
| Parallel argument lists | Multiple functions that always receive the same cluster of arguments | Introduce a value object or record type |
| Repeated conditional branching | The same `if/switch` structure reproduced across unrelated call sites | Consolidate into a single dispatch point or strategy |
| Mirrored data transformations | Two or more pipelines that apply the same sequence of steps to different types | Extract a common pipeline or adapter |
| Redundant state copies | Mutable fields that are always kept in sync manually | Derive one from the other, or unify into a single source of truth |

**Decision rule — stop here if the dominant pattern is duplication:**

> If three or more of the signals above are present, the highest-value action is a refactoring recommendation (extract, parameterize, unify). Do **not** proceed to algebraic classification until the structural cleanup is at least outlined, because labeling duplicated code as a `Monoid` does not eliminate the duplication.

**Move to algebraic analysis only when:**

- The code already has a stable, non-duplicated shape (or after sketching the structural refactoring above), **and**
- At least one binary operation `(A, A) → A`, comparison `(A, A) → Bool/Int`, or structure-preserving mapping `F[A] → F[B]` is present across the deduplicated surface.

Record the structural findings explicitly in the discovery report even when they do not lead to an algebraic label.

## Retrieve candidate abstractions dynamically

The catalog dependency is located relative to this skill file's directory: starting from `<skill_dir>` (the directory containing this `SKILL.md`), the catalog root is three levels up at `<skill_dir>/../../..`. This relative structure is preserved whether cloned or extracted from an archive or zip without requiring git.

First verify catalog availability with Python's standard library:

```sh
python3 <skill_dir>/../../../scripts/catalog.py check
```

Instead of hardcoding axiom assumptions in the skill, query candidate concepts dynamically from the catalog. The skill focuses on the following core list of candidate concepts that commonly govern software patterns:

- **Reducers / Combination**: `Monoid`, `Semigroup`
- **Comparisons / Sorting**: `Preorder`, `TotalOrder` (Total Preorder without antisymmetry)
- **Bounds / Reconciliation / CRDTs**: `Lattice`, `JoinSemilattice`
- **Mapping / Transformations**: Functor (archetype for structure-preserving mapping)*

Query the authoritative operations, axioms, and laws for the candidate concept dynamically:

```sh
# Query a specific candidate concept dynamically:
python3 <skill_dir>/../../../scripts/catalog.py get <Concept> --sections operations axioms laws

# Or batch-query the commonly helpful discovery set:
for concept in Monoid Semigroup Preorder TotalOrder Lattice JoinSemilattice; do
  python3 <skill_dir>/../../../scripts/catalog.py get "$concept" --sections operations axioms laws
done
```

Search by operational behavior and mathematical role:

| Operational Pattern | Candidate Catalog Concepts | Key Verification Focus from Retrieved Axioms |
| --- | --- | --- |
| Binary reduction / folding `(A, A) -> A` | `Semigroup`, `Monoid` | Check associativity (`Semigroup-associative`, `Monoid-associative`), identity (`monoid-identity`), identity uniqueness |
| Comparison / Sorting / Priority `(A, A) -> Int` | `Preorder`, `TotalOrder` (Total Preorder) | Check reflexivity (`Preorder-reflexive`), transitivity (`Preorder-transitive`), totality (`TotalOrder-comparable`), equivalence kernel (`Preorder-core`) |
| Bounds / Least-upper / Greatest-lower / Merge | `Lattice`, `JoinSemilattice` | Check meet GLB bound (`Lattice-meet-bound`), join LUB bound (`Lattice-join-bound`), absorption (`Lattice-core`), idempotence, commutativity |
| Structure-preserving mapping `(A -> B) -> F[B]` | Functor (mapping archetype)* | Check identity preservation (`map(id) == id`), composition preservation (`map(f ∘ g) == map(f) ∘ map(g)`) |
| State transitions / Protocols `(S, E) -> S` | `LabelledTransitionSystem`, `KripkeStructure` | Determinism, reachability, enabled actions, deadlocks |
| Set / Map / Collection indexing | `Set`, `Multiset`, `Sequence`, `Multimap` | Extensionality, membership, duplicate handling, ordering |
| Resource / Access management | `Lock`, `Mutex` | Mutual exclusion, compatible holders, release ownership |

*\*Note: `Functor` is the standard mathematical archetype for structure-preserving container transformations (`map`/`fmap`). When analyzing mapping APIs, verify its governing identity and composition laws directly against the retrieved container concept.*

Start with focused concept and operation records. Retrieve axioms and laws only for candidate invariants under test. Do not preload complete claim closures or full dossiers.

## Test algebraic laws and detect violations

Evaluate the dynamically retrieved axioms and governing laws against the code's actual semantics:

1. **Monoid & Semigroup Laws (Associativity & Identity)**:
   - Verify associativity `(x · y) · z == x · (y · z)` under batching, parallel reduction, or stream chunking.
   - Verify identity `e · x == x · e == x` on empty collections, neutral defaults, or singleton cases.
2. **Total Preorder Laws (Comparators & Sorting)**:
   - Verify reflexivity `compare(x, x) == 0`.
   - Verify transitivity `compare(a, b) <= 0 ∧ compare(b, c) <= 0 ⇒ compare(a, c) <= 0`.
   - Verify totality: every valid input pair produces a deterministic comparison.
   - Distinct elements with equivalent keys may tie (`compare(a, b) == 0` without `a == b`).
3. **Lattice & Semilattice Laws (Bounds, Absorption & Merge)**:
   - Verify meet (greatest lower bound) and join (least upper bound).
   - Verify absorption `x ∧ (x ∨ y) == x` and `x ∨ (x ∧ y) == x`.
   - Verify idempotence `x ⊔ x == x` and commutativity `x ⊔ y == y ⊔ x` for CRDTs and state reconciliation.
4. **Functor Mapping Laws**:
   - Verify identity preservation: `map(id) == id`.
   - Verify composition preservation: `map(f ∘ g) == map(f) ∘ map(g)`.
   - Ensure `map` does not mutate external state or conditionally drop/reorder elements.
5. **Idempotence & Transition Invariants**: Test retry loops, caching, and state transitions (`(State, Event) -> State`) for reachability and invariant preservation.

When a law is violated, construct a minimal concrete counterexample showing the inputs, the expected mathematical outcome, and the actual software behavior.

Read [references/discovery-guide.md](references/discovery-guide.md) for detailed mapping tables and code smells, and [references/metrics-example.md](references/metrics-example.md) for a worked example on telemetry aggregation.

## Deliver the discovery report and refactoring plan

Produce a structured report detailing:

- **Target Component**: File, class, function, or API locator.
- **Abstraction Inventory**: Table of existing abstractions with use counts and copy counts. Classify each as well-used, underused, unused, or missing.
- **Structural Duplication Assessment**: List of duplication signals found (copy-paste logic, parallel argument lists, mirrored pipelines, etc.) with concrete locations. If this is the dominant finding, state it clearly and prioritize the structural refactoring recommendation over any algebraic label.
- **Discovered Abstraction**: Matching catalog concepts with stable IDs (`urn:csabs:concept/...`), or `none — refactoring candidate` when structural duplication dominates.
- **Carrier & Operation Mapping**: Concrete types and methods mapped to catalog carriers and signatures.
- **Law Assessment**: Table of checked laws (associativity, identity, commutativity, etc.), marked as satisfied, conditionally satisfied, or violated.
- **Counterexamples**: Explicit inputs that trigger law violations or unexpected edge behavior.
- **Refactoring Recommendations**: Specific architectural changes — structural cleanup first (extract, parameterize, unify), then algebraic alignment (e.g., introducing an explicit identity element, adjusting floating-point aggregation, or making merge operations idempotent).

Connect the discovery findings to downstream skills:
- Use [implementation-mapping](../implementation-mapping/SKILL.md) to formalize the updated API contract.
- Use [implementation-conformance](../implementation-conformance/SKILL.md) to review refactored code against the revised obligations.
- Use [mathematical-tests](../mathematical-tests/SKILL.md) to generate regression property tests based on discovered laws.
