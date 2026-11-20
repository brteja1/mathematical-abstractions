# Stochastic processes

The process framework reuses the existing probability spaces, measurable spaces and random variables. The definitions use the installed Mathlib revision `56a005855ea17e0b0958f73ec801ae140b0a1679`, consulted on 2026-11-20; each concept and claim records its own source and declaration locator.

| Concept | Selected interface | Main boundary |
| --- | --- | --- |
| [StochasticProcess](../concepts/StochasticProcess.md) | A family X:T→Ω→E with every coordinate measurable on a common probability space | Coordinate measurability does not impose joint measurability or path regularity |
| [Filtration](../concepts/Filtration.md) | Increasing sub-sigma-algebras of an ambient measurable space, indexed by preordered time | No completeness or right-continuity assumption; no probability measure needed |
| [AdaptedProcess](../concepts/AdaptedProcess.md) | Xₜ is measurable with respect to the information 𝓕ₜ available at t | Adaptedness alone does not imply progressive measurability |
| [StoppingTime](../concepts/StoppingTime.md) | τ:Ω→ℕ∪{∞}, with {τ≤n} in 𝓕ₙ | Infinity means never stopping; finiteness and boundedness are additional conditions |
| [Martingale](../concepts/Martingale.md) | Real, discrete-time adapted integrable process with E[Xₘ\|𝓕ₙ]=Xₙ almost surely for n≤m | No convergence or optional-stopping theorem is assumed |

`AdaptedProcess` specializes `StochasticProcess`; `Martingale` specializes `AdaptedProcess` at T=ℕ and real Borel values. The existing [MarkovChain](../concepts/MarkovChain.md) specializes `StochasticProcess` at integer time and a finite discrete state space. This describes its mathematical process semantics; its existing partial Lean kernel model still does not construct an infinite sample process. A stochastic transition channel alone is not a process, and neither a filtration nor a stopping time is a subtype of a process.

For fixed parameters, process equality is pointwise in time and outcome. Almost-sure coordinate equality and equality in distribution are different relations. The martingale conditional-mean equation uses almost-sure equality; it does not identify process representatives pointwise. Conditional expectation is specified by its integrals over events in 𝓕ₙ and is unique only up to null sets. No positive-probability-event division is used.

The finite-dimensional-law operation uses the finite product sigma-algebra. Repeated times and an empty list of times are allowed. An empty list gives the one-point empty product. General processes allow empty time sets; existence with a supplied value e∈E is proved without assuming an inhabitant of an empty value space.

## Lean evidence

[Catalog/StochasticProcesses.lean](../lean/Catalog/StochasticProcesses.lean) contains five model bindings and five separate model-satisfaction theorems. Each theorem constructs an inhabitant whose type includes the complete selected defining constraints:

- A constant family for any index type, probability space and supplied value.
- The constant ambient filtration for any preordered time type.
- A constant family adapted to any supplied filtration.
- The deterministic stopping rule τ=0 for any integer-time filtration.
- A constant real martingale on any supplied probability space and integer-time filtration.

These constructions establish nonvacuity of the chosen bases. They do not prove the existence of Brownian motion, Poisson processes, random walks with prescribed independent increments, or nonconstant martingales. No such concepts or results are included in this addition.

For real Borel values, Mathlib's strongly measurable adaptedness matches the readable measurable-adaptedness condition. Mathlib's martingale definition includes the conditional-mean identity at equal times; `Martingale.integrable` derives integrability from that diagonal identity. The binding records this correspondence explicitly.

Run `make check-lean` for metadata correspondence and `make test-lean` for compilation, expected-type checking and transitive axiom audits. Only a fresh ignored `lean/verification.json` establishes the current registered witness status. Source provenance and correspondence with readable mathematics remain separate review obligations.

## Retrieval

```sh
python3 scripts/catalog.py list --category stochastic-processes
python3 scripts/catalog.py get StochasticProcess --sections operations axioms
python3 scripts/catalog.py get Martingale --sections dependencies sources
python3 scripts/lean.py get urn:csabs:theorem/Martingale-model-satisfaction
```
