# Verify a capped reservation merge and use it

Reservations track a budget usage `x` between 0 and a positive natural cap `C`, inclusive. Combining usage should compute `min(C, x+y)`. This task proposes an associative merge with identity 0 and ordinary equality. Required inputs include both 0 and C; an empty or singleton carrier will not model the task.

Find reusable mathematical definitions and proofs in the supplied catalog and pinned Lean/Mathlib environment before inventing a new abstraction. Fill any necessary definition/model/proof gap. Prove for arbitrary positive C that the operation stays in the carrier, is associative, and has a two-sided identity; compile the proofs and audit their axiom dependencies. A structure declaration assuming those laws is not the requested evidence.

Keep all new artifacts with this task; do not promote anything into the catalog or change dependency pins. Record actual consulted sources and exact propositions. Then implement `combine(cap, a, b)` in Python with invalid inputs raising `ValueError`, exercise boundaries and regrouping, and explain the mapping and any remaining implementation-proof gap. Save Lean sources, `checks.py`, and `answer.md`, including actual compiler output or an honest tool blocker.
