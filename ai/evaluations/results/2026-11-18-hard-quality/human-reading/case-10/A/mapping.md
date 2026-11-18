# Implementation mapping — revision 1

Authority: `TASK.md`, transcribed into `spec.md` revision 1, clauses S1–S8.
Hashes of this baseline and reviewed sources are in `evidence.json`. Scope is the
six public sequential functions; no formal refinement or concurrency claim.

## Interpretation

Abstract state is a finite partial map B: nonempty strings ⇀ {(s,e) in Z² | s<e}.
Concrete state is private `_Calendar` with immutable tuple rows. Its invariant:
IDs are unique and sorted, endpoint pairs are valid. The abstraction function
maps each `(id,s,e)` row to B[id]=(s,e). Equality compares bindings, witnessed by
`bookings`, rather than Python object identity. `empty` establishes the invariant;
`reserve` preserves it by checking conflicts and sorting; `merge` uses a fresh
local dictionary and emits sorted unique rows. No input state is ever written.

Python integers supply exact endpoint order and exact count addition. All loops
range over finite bookings/endpoints, never over endpoint magnitudes. There is
no fixed capacity. Ordinary interpreter resource limits remain; no resource
availability, timing or threading guarantee is added. The concrete tuple shape
of `occupied` is a design choice specifying the contract's span result. There
are no unresolved semantic choices.

## Focused catalog correspondence

Backend: read-only standard-library `python3 catalog/scripts/catalog.py`.
`check` reported 264 concepts, 2484 nodes, no errors. Focused `get ... --sections
operations` queries retrieved the records below. ONTFS helper failed because
its projection was missing; no projection was generated or catalog modified.
No catalog theorem, inherited axiom, or Lean witness is relied on.

| Record and source locator | Applicability and limitations |
| --- | --- |
| `urn:csabs:concept/Map`, `catalog/concepts/Map.md`, definition and mathematicalFormulation | Finite partial function, lookup-extensional equality; K is IDs and V is valid endpoint pairs. `urn:csabs:operation/Map-basis-empty` maps to `empty`. `Map-lookup` is internal ID search, observed externally through `bookings`. `Map-set` describes binding insertion only on the absent-or-equal subdomain of `reserve`; general overwrite is forbidden by S3. No delete API is mapped. Review is editorial; provenanceStatus is `legacy-source-missing`. |
| `urn:csabs:concept/ArbitraryPrecisionInteger`, `catalog/concepts/ArbitraryPrecisionInteger.md`, mathematicalFormulation | Carrier Z has no fixed width; `urn:csabs:operation/ArbitraryPrecisionInteger-add` maps to grouped deltas and active-count accumulation in `peak`. Exact comparisons/clipping use Python integers; resource limits are separate. Editorial review, `legacy-source-missing`. |
| `urn:csabs:concept/ClosedInterval`, `catalog/concepts/ClosedInterval.md`, basisScope and mathematicalFormulation | Examined and rejected as an interval oracle: closed intervals allow singleton intervals and include the upper endpoint. S1, S6, S7 directly supply the required half-open semantics. This record's adapted source locator is `Set.Icc and membership definition`; no closed-interval claim or proof is transferred. |

The finite-map formulation is `lookup(B,k)=B(k)` with extensional equality;
insertion changes only that key. Merge's compatibility restriction, persistence,
clipped half-open union, and maximum count come directly from the normative
product contract. These explicit finite definitions suffice here without a new
catalog abstraction or proof artifact. Catalog citation gaps remain unchanged.

## Obligations and conformance evidence

All rows are supported by code inspection and the indicated passing tests within
their finite scope. Test names below omit the common `test_` prefix. Every test
constructs states via `empty`/`reserve`/`merge` and observes only through
`bookings`, `occupied`, and `peak`; none inspects the private representation.

| ID / clause | Public symbol and implementation obligation | Executed evidence in `test_calendar.py` |
| --- | --- | --- |
| O1 / S1,S2 | `empty`: establish empty valid map; independent constructions have no shared mutable state | `empty_and_ordering`, exhaustive model comparisons |
| O2 / S3 | `reserve`: preserve other IDs; exact replay is observationally unchanged; invalid order or unequal reuse raises ValueError | `replay_and_distinct_ids`, `errors_preserve_all_observations`, seeded histories |
| O3 / S4 | `merge`: compatible union preserves every ID once; reject any disagreement; compatible identity, associativity, commutativity, idempotence | `merge_laws_on_jointly_compatible_states`, late conflict in both directions, seeded histories |
| O4 / S5 | `bookings`: immutable tuple rows, unique IDs sorted by Python string order | `empty_and_ordering`, exhaustive/seeded reference-map rows |
| O5 / S6 | `occupied`: clip, discard empty intersections, sort and coalesce overlaps and adjacency; equal window empty, reversed window ValueError | clipping/nesting/gap examples, exhaustive windows, error tests |
| O6 / S7 | `peak`: aggregate +1 at starts and -1 at ends, then measure; preserve separate contributions of distinct IDs | endpoint-tie examples, duplicate intervals, exhaustive unit-cell counts |
| O7 / S8 | All functions: no writes to old states on success/error, observers have no effects | frozen tuple representation inspection; every stored version reobserved after each seeded operation; explicit late merge failures |
| O8 / S1,S8 | All functions: signed arbitrary-size integers, no artificial capacity; finite-input algorithms | negative and positive 10**150 endpoints and 300 simultaneous bookings; inspection for casts, bounds, and endpoint-range loops |

For O5, the processed-span invariant is that accumulated spans are the canonical
union of all clipped intervals processed so far. Sorting means only the final
span can join the next interval; using `<=` coalesces adjacency. For O6, after
applying a coordinate's combined delta, active equals the count at that
coordinate and until the next endpoint. Measuring after grouping prevents a
false peak where ends meet starts. Multiplicity is per ID, independent of union
coverage. Finite iteration and sorting support termination under available
resources, without a complexity promise in the public contract.

Exhaustive tests cover all assignments of ten valid endpoint pairs from
{-2,-1,0,1,2} to 0–3 fixed IDs (1,111 calendars), each queried with 28 ordered
windows from {-3,...,3}. The independent oracle counts integer unit cells, then
collects occupied runs; integer endpoints make this exact on those finite inputs.
Seed 20261118 drives 250 branching reserve/merge operations and checks all saved
versions after every operation, including failures. Large-endpoint examples use
direct expected tuples rather than iterating over huge ranges.

Result: all 9 unittest methods passed; exact command/output in `test-results.txt`.
Inspection found no contract mismatch. This is finite executable and static
evidence, not a universal implementation proof. No Lean build or abstract proof
is claimed; out-of-domain types, thread behavior, resource exhaustion, and
performance are outside this review. No required in-scope behavior is knowingly
left unimplemented.
