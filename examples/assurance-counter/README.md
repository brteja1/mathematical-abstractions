# Actual-source refinement pilot

`Counter.lean` implements capped increment over unbounded natural numbers and
proves its output relation and conditional bound. The same function supplies
208 values checked by the independent Python oracle in `checks.py`.

Run the four ledger checks and final admission command in the
[shared guide](../../ai/skills/spec-driven-development/references/assurance.md#runnable-profile).
Use `make test-assurance` for the pilot, deliberate implementation defects,
invalid proof witnesses and freshness regressions. Local reports in `.assurance/`
are ignored; no compiled verification result is committed as permanent evidence.
See `spec.md` for assumptions and the explicitly limited agent review receipts.
