# Prove the implemented capped increment

Write a task-local Lean source defining bump(limit,n) over all natural inputs: if n < limit return n+1, otherwise return n. Include inputs already above the limit. Prove the result equation and that n≤limit implies result≤limit, for the exact function executed in your example, using the catalog's pinned Lean project. Retain reviewed expected proposition text and transitive axiom audit output; no sorry or postulated target law. Execute finite examples through the implementation and independently check them. Then introduce an n+2 bug in a temporary copy and demonstrate a failed proof/check. Keep correct source intact.

Write mapping.md, the source, runnable checks, and answer.md with versions, commands and scope. Do not claim native compiler correctness, use a separate unlinked model as implementation evidence, update dependencies, promote graph records or imply the author is an independent reviewer. Report tooling blockers honestly.
