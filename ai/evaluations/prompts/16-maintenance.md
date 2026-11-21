# Repair assurance freshness after changes

Create a small task-local source/contract/checker example and a reproducible local evidence record. The initial requirement says plusOne(n)=n+1 on all natural inputs. Produce passing finite test evidence, retaining its input/checker hashes and scope. Next revise the implementation to add two without revising the requirement, add a new helper file and leave the old success record present.

Write and run a freshness/impact checker that refuses to treat old success as current. Re-execution must detect the behavior defect; it must not merely update stored hashes. Cover a later requirement or checker change as well. Record obligations and dependencies, missing or stale evidence and outstanding decisions in mapping.md and answer.md. Clearly distinguish finite tests from universal proof, and disclose untracked environment inputs. Keep all work task-local; do not edit catalog or dependency pins.
