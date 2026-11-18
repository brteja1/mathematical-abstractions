# Check a release policy

Review these independent proposed policies. All symbols are ordinary Boolean values; there are no unstated environment assumptions.

Policy A: `enabled` is a required input, supporting both true and false. `served` is an output. A1: if served, enabled must be true. A2: if enabled is false, served must be true.

Policy B: `p` and `q` are outputs. B1: at least one of p or q must be true. B2: p must be false. B3: q must be false.

Policy C: `ready` is an input supporting both values and `accepted` is an output. C1: accepted if and only if ready.

Determine which policies can serve every required input and which requirements conflict. Provide reproducible evidence, minimal conflicting clause sets where applicable, and a proposed repair that makes each faulty policy usable. Do not silently change a clause or exclude an input. Save the review in `answer.md` and the runnable checks in `checks.py`; run the checks. Do not change the catalog.
