# Semantic duplicate triage

Machine proposals for catalog maintenance. No records or human review receipts were changed.

| Scope | Count |
| --- | ---: |
| Actionable audit candidates | 5538 |
| Selected for this experiment | 10 |
| Not selected / not semantically reviewed | 5528 |
| Model-reviewed in this selection | 10 |
| Selected, awaiting review | 0 |
| Primary reviewer failures | 0 |
| Proposed duplicates | 0 |
| Suggested distinctions | 10 |
| Unresolved judgments | 0 |
| Automatically suppressed candidates | 0 |
| Pending independent reviews | 0 |
| Failed independent reviews | 0 |

**Reviewer:** current-assistant / session-model-version-not-exposed (assistant-session).

**Calibration:** No independent accuracy claim; automatic suppression disabled in DT-1.

## Proposed duplicate actions

No proposed duplicate actions or unresolved judgments in the reviewed subset.

<details><summary>Suggested distinctions — retain separate records (machine judgments)</summary>

| Records | Classification | Decisive comparison |
| --- | --- | --- |
| [merge-idempotent](../../../concepts/StateBasedCRDT.md#node-urn-csabs-law-StateBasedCRDT-merge-idempotent) ↔ [merge-commutative](../../../concepts/StateBasedCRDT.md#node-urn-csabs-theorem-StateBasedCRDT-merge-commutative) | distinct | Repeated-state absorption and argument-order independence are different laws. Both concern merge, but one constrains merge(s,s) and the other compares merge(s,t) with merge(t,s); retain both. |
| [distributivity](../../../concepts/EffectAlgebra.md#node-urn-csabs-axiom-EffectAlgebra-distributivity) ↔ [sequencing-monoid](../../../concepts/EffectAlgebra.md#node-urn-csabs-axiom-EffectAlgebra-sequencing-monoid) | distinct | Distributivity links sequencing to join, whereas the monoid rules give sequencing associativity and the no-effect identity. These are complementary interface obligations, not duplicate statements. |
| [product-beta-first](../../../concepts/ProductType.md#node-urn-csabs-axiom-product-beta-first) ↔ [product-beta-second](../../../concepts/ProductType.md#node-urn-csabs-axiom-product-beta-second) | distinct | These are the two projection beta rules. The first returns the A component and the second the B component; deleting either would lose an explicit constructor/observer obligation. |
| [case-inl](../../../concepts/SumType.md#node-urn-csabs-axiom-case-inl) ↔ [case-inr](../../../concepts/SumType.md#node-urn-csabs-axiom-case-inr) | distinct | The elimination equations cover different disjoint constructors of a sum. One specifies the inl/f branch and the other the inr/g branch, so they are separate required cases. |
| [free-frame](../../../concepts/HeapStore.md#node-urn-csabs-axiom-HeapStore-free-frame) ↔ [write-frame](../../../concepts/HeapStore.md#node-urn-csabs-axiom-HeapStore-write-frame) | distinct | The shared frame shape explains the high text score, but freeing makes the selected address unallocated while writing stores Some(v). Both preserve other addresses and express different heap effects. |
| [rounded-operations](../../../concepts/Binary128.md#node-urn-csabs-axiom-Binary128-rounded-operations) ↔ [rounded-operations](../../../concepts/Binary16.md#node-urn-csabs-axiom-Binary16-rounded-operations) | semantic_variant | The arithmetic-rule wording is shared, but it is instantiated over different floating-point grids: binary128 has precision 113, while binary16 has precision 11. Retain the format-specific applications; a common parameterized rule could be factored in a separate catalog change. |
| [rounded-operations](../../../concepts/Binary128.md#node-urn-csabs-axiom-Binary128-rounded-operations) ↔ [rounded-operations](../../../concepts/Binary32.md#node-urn-csabs-axiom-Binary32-rounded-operations) | semantic_variant | The arithmetic-rule wording is shared, but it is instantiated over different floating-point grids: binary128 has precision 113, while binary32 has precision 24. Retain the format-specific applications; a common parameterized rule could be factored in a separate catalog change. |
| [rounded-operations](../../../concepts/Binary128.md#node-urn-csabs-axiom-Binary128-rounded-operations) ↔ [rounded-operations](../../../concepts/Binary64.md#node-urn-csabs-axiom-Binary64-rounded-operations) | semantic_variant | The arithmetic-rule wording is shared, but it is instantiated over different floating-point grids: binary128 has precision 113, while binary64 has precision 53. Retain the format-specific applications; a common parameterized rule could be factored in a separate catalog change. |
| [special-values](../../../concepts/Binary128.md#node-urn-csabs-axiom-Binary128-special-values) ↔ [special-values](../../../concepts/Binary16.md#node-urn-csabs-axiom-Binary16-special-values) | semantic_variant | The special-value policy is common, but these records apply it to binary128 and binary16 carriers. Keep the carrier-specific applications; review any future extraction of a shared format-parameterized policy separately. |
| [special-values](../../../concepts/Binary128.md#node-urn-csabs-axiom-Binary128-special-values) ↔ [special-values](../../../concepts/Binary32.md#node-urn-csabs-axiom-Binary32-special-values) | semantic_variant | The special-value policy is common, but these records apply it to binary128 and binary32 carriers. Keep the carrier-specific applications; review any future extraction of a shared format-parameterized policy separately. |

</details>

## Pending work

0 selected pairs await review; 5528 additional candidates were not selected.

The detailed machine evidence is in [proposals.json](proposals.json). Distinctions are collapsed for readability, not accepted or suppressed.

Model identity/version are declared provenance. Citation validation checks that quoted text exists; it does not prove the judgment. Source gaps remain unchanged.
