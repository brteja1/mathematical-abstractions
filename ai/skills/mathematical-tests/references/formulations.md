# Mathematical formulations and Lean evidence

Use this reference when a selected catalog record provides readable mathematics or a Lean formulation. Resolve `<catalog>` to the checkout containing these skills. The concept Markdown JSON remains authoritative; page prose, the viewer and ONTFS are projections of those records.

Read only the section needed for the current decision. Ordinary interface mapping starts with focused concept/operation records; it does not require this whole guide, a theorem list or a Lean excerpt. Axioms/laws are fetched for a selected property, theorems only when their results or proofs are needed, and typed evidence only when it affects the task.

## Read the interpretation before reusing an equation

| Field | How to use it |
| --- | --- |
| `mathematicalFormulation` | Readable carrier definitions, equations and conventions for the selected interpretation. This is mathematical text, not executable Lean or a complete specification of every variant. |
| `leanFormulation` | Opt-in via `--view lean` or `full`: the selected concept declaration or registered witness proposition. A named target can be expanded to a `def ... : Prop`; stating that proposition does not prove it. |
| `formulationScope` | `model` selects an interpretation, `partial` leaves explicit interface obligations, and `registered-witness-type` displays a registered proposition. None is a current compiler-status flag. |
| `leanModelMapping`, `leanModelLimitations` | Carrier, equality, operations and assumptions mapped to Lean, plus omitted behavior. Apply these limits to both readable and typed formulations. |
| `formulationSource`, `formulationLocator` | Direct local Source record and Lean symbol. Consult the module's imports, namespaces, universe parameters, section variables and referenced definitions; excerpts need that context. |
| `leanPremiseMapping` | On witness claims, a JSON-encoded mapping of each direct `dependsOn` ID to its formal premise. Decode it as data and compare it with the claim's dependencies and current binding. |
| `formalStatement`, `assumptions`, `dependsOn`, `appliesTo` | The catalog claim and its applicability/derivation. An embedded Lean interpretation does not replace these or the target's normative clauses. |

Compare the readable mathematics, typed interpretation and intended target contract. Record any difference in carriers, equality, guards, result encoding or quantifier scope. Do not silently choose whichever version makes a test or proof succeed. A `partial` model can guide the portion it represents; missing operations or laws remain obligations, not inferred facts. A complete selected model also does not cover every catalog theorem.

## Retrieve the formulation and both kinds of source

Dependency-free queries read current authoritative records:

```sh
python3 <catalog>/scripts/agent_query.py node Stack
python3 <catalog>/scripts/agent_query.py node urn:csabs:law/stack-push-pop --view lean
python3 <catalog>/scripts/agent_query.py neighbors Stack --relations formulationSource --depth 1 --limit 4
python3 <catalog>/scripts/lean.py get urn:csabs:law/stack-push-pop
```

For a task that needs the Stack push/pop property and its typed correspondence, choose the needed command below; these are alternatives at successive retrieval stages, not a checklist to preload:

```sh
<catalog>/.venv/bin/python <catalog>/ai/skills/mathematical-tests/scripts/query.py node Stack --max-chars 12000
<catalog>/.venv/bin/python <catalog>/ai/skills/mathematical-tests/scripts/query.py node urn:csabs:law/stack-push-pop --view lean --max-chars 12000
<catalog>/.venv/bin/python <catalog>/ai/skills/mathematical-tests/scripts/query.py sources Stack --kind formulation --limit 2 --max-chars 4000
<catalog>/.venv/bin/python <catalog>/ai/skills/mathematical-tests/scripts/query.py sources urn:csabs:law/stack-push-pop --kind citation --limit 2 --max-chars 4000
```

`--kind citation` is the default and follows only `source`. `--kind formulation` follows only `formulationSource`. Neither inherits a concept's sources for a claim. A local Lean source supports that interpretation, not independent mathematical provenance or a security/hardness assertion. Keep `legacy-source-missing` visible even when a claim has a compiled witness. Full declarations and premise mappings can make records larger: follow `requiredChars`, pagination and depth boundaries rather than clipping equations or assumptions. See [retrieval.md](retrieval.md) for projection freshness and budgets.

## Check proof status only when relying on a proof

Use `scripts/lean.py get ID` to inspect the current binding's `kind`, `expectedType`, `mapping`, `limitations`, `premiseMapping` and `catalogHash`. Read toolchain/library pins from `lean/bindings.json` and the Lean lock files; do not infer them from an excerpt. For a witness, report it as compiled and audited only when `verificationFresh` is true and `witnessEvidence` is present. A model can have a fresh project report without being a theorem witness. If a claim has no registered binding, retain its mathematical statement without inventing a proof.

`make check-lean` checks metadata and drift; `make test-lean` compiles and audits witnesses using the pinned project. Run the latter when the task needs fresh evidence and it is unavailable, or report the evidence as unavailable. Ordinary mapping and test design do not require rebuilding Lean just to read formulas. Fingerprint failures require correspondence review; do not refresh hashes to suppress them. See [the Lean guide](../../../../lean/README.md) for the verification workflow. A verified abstract proposition still needs a justified mapping to a specification or concrete implementation.

## Select domain-specific obligations

| Selected concepts | Distinction that affects downstream work |
| --- | --- |
| Stack and partial functions | `some(s,x)` encodes a defined state/value result; `none` encodes undefinedness. A product's exception, sentinel or mutation policy needs a separate mapping. |
| Floating-point formats | Format/value carriers and supplied `round`/`run` functions do not establish correct rounding, flag behavior or arithmetic identities. |
| Entropy, channels and codes | Preserve finite alphabets, exact normalization, log base, zero-mass conventions and any infinity encoding. Information expressions, operational coding targets and proved coding results are distinct. |
| AES/GCM, RSA, ECC and key exchange | A permutation, exponent map, point-group interface or functional round trip does not establish algorithm correspondence, input validation, nonce discipline or computational security. |
| Euclidean/q-ary lattices, SVP/CVP, SIS/LWE | Independent real bases and modular kernels are different presentations; preserve the chosen norm, rank, approximation factor and admissibility guards. Witness relations do not supply sampling experiments, algorithms or hardness proofs. |
| BTree, LamportBakery and histories | A raw shape/state carrier does not supply balance, transitions, reachability or protocol correctness. Linearizability/consistency predicates need their event/history instantiation. |

Retrieve the actual relevant records rather than inferring scope from this table. For example, `BTree` exposes a raw rose-tree shape and `LamportBakery` exposes state fields; their omitted invariants cannot serve as established test or proof premises.
