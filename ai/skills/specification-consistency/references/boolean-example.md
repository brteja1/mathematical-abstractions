# Boolean requirements and input coverage

This synthetic example demonstrates the workflow without ONTFS, a solver, or network access. It does not modify catalog records or register a Lean witness.

## Specification and mapping

| Local clause | Requirement | Encoding |
| --- | --- | --- |
| R1 | If access is allowed, the requester is authenticated | allowed implies authenticated |
| R2 | If the requester is unauthenticated, access is allowed | not authenticated implies allowed |
| S1 | An unauthenticated request is a required input scenario | authenticated = false |

Both variables have the exact carrier `{false,true}` and ordinary Boolean equality. `authenticated` is an environment input; `allowed` is the system output. There are no additional background assumptions. S1 is a coverage obligation, not an invariant requiring every requester to be unauthenticated. Check it separately from any other required input scenarios.

Retrieve these existing records before using the example as a catalog-guided check:

```sh
python3 scripts/agent_query.py node urn:csabs:operation/PropositionalLogic-basis-evaluate
python3 scripts/agent_query.py node urn:csabs:theorem/PropositionalLogic-finite-truth-table
```

The first maps to `all(rule(v) ...)` below; the second maps to enumerating all four total Boolean valuations. Follow the theorem's `dependsOn` links if relying on its derivation. The code uses classical implication `(not p) or q`; it does not evaluate informal catalog notation as executable syntax.

## Execute from any directory

```sh
python3 - <<'PY'
from itertools import product, combinations

rows = [dict(zip(('authenticated', 'allowed'), bits))
        for bits in product((False, True), repeat=2)]
rules = {
    'R1': lambda v: not v['allowed'] or v['authenticated'],
    'R2': lambda v: v['authenticated'] or v['allowed'],
    'S1': lambda v: not v['authenticated'],
}

def models(ids):
    return [v for v in rows if all(rules[r](v) for r in ids)]

ids = tuple(rules)
print('Complete Boolean valuations:', len(rows))
for pair in combinations(ids, 2):
    found = models(pair)
    assert found, pair
    print('SAT', pair, 'witness:', found[0])

assert not models(ids)
print('UNSAT', ids)
# Every single-clause deletion has a model: inclusion-minimal, not a claim
# about minimum-cardinality cores for arbitrary specifications.
assert all(models(ids[:i] + ids[i + 1:]) for i in range(len(ids)))
print('Conflict is inclusion-minimal')

for authenticated in (False, True):
    outputs = [v['allowed'] for v in models(('R1', 'R2'))
               if v['authenticated'] == authenticated]
    print('Required input authenticated =', authenticated,
          'allowed outputs:', outputs)
    assert bool(outputs) == authenticated

# Candidate repair: require unauthenticated requests to be denied.
# This replaces R2 rather than silently excluding the required input.
rules['R2'] = lambda v: v['authenticated'] or not v['allowed']
assert models(ids)
assert all(any(v['authenticated'] == a for v in models(('R1', 'R2')))
           for a in (False, True))
print('Proposed repair: SAT; both Boolean inputs have permitted outputs')
PY
```

Expected findings: every pair has a model, but R1/R2/S1 together have none. With `authenticated=false`, R2 requires `allowed=true`, and R1 requires `authenticated=true`, contradicting S1. R1/R2 alone have models only for authenticated inputs; a plain existential satisfiability check would miss the input-coverage failure. The proposed repair permits denial for unauthenticated requests and restores output existence for both inputs, while changing the behavior requested by R2. It is a proposal, not authorization to alter a real specification.

This enumeration is complete for the declared two-variable Boolean model. It says nothing about authentication protocols, stateful sessions, concurrency, or whether these clauses capture a real product's intent.
