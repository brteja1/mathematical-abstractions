# Concrete Lean information-theory formulations

All 29 laws/theorems from the information-theory expansion now have explicit Lean propositions in [InformationTheoryStatements.lean](Catalog/InformationTheoryStatements.lean), under `Catalog.Information.Targets`. Thirteen have complete registered proof witnesses under `Catalog.Information.Verified`. The remaining 16 are concrete proof targets, not asserted truths in Lean. No target is declared as a new global axiom or filled with `sorry`.

A proposition and a proof are different artifacts. `def chainRule : Prop := ...` specifies a claim, and Lean checks that its expression has type `Prop`. The theorem `Verified.chainRule : Targets.chainRule` contains a proof that Lean checks. A prose proof sketch in the catalog does neither by itself. The witness manifest keeps an independently expanded expected type rather than accepting whatever proposition a target name might later denote.

## Carriers and operations

| Catalog meaning | Concrete formulation |
| --- | --- |
| Exact finite probability law | `Law A`: real-valued masses, nonnegativity and finite normalization |
| Joint and marginal laws | `joint`, `marginalX`, `marginalY`; normalization proved from the primitive laws |
| Stochastic output and block channel | `outputMass`, `output`, `blockKernel`, `blockLaw`; normalization derived, not assumed as a target conclusion |
| iid source | `iidLaw p n`, with finite product masses and proved normalization |
| Discrete information | Existing finite sums in bits; conditional entropy via joint/marginal log ratios; zero-mass summands vanish |
| Relative entropy | `Option Real`: `none` denotes positive infinity on support mismatch; `some d` is the exact finite sum |
| Operational source/channel codes | `SourceCode`, `ChannelCode`, positive message counts, explicit encoders/decoders and actual average block-error sums |
| Rates and limits | `bitRate`, `UpperLimit`, `LowerLimit`, `Vanishes`; sequences use length `n+1`, so no zero-block division is used by coding claims |
| Channel capacity | `operationalCapacity`: supremum of nonnegative achievable rates; not substituted with the information expression |
| Lossy coding | `LossyCode`, `lossyCost`, `kernelCost`, `informationRD`, `operationalRD`; extended nonnegative reals encode infeasible infima as infinity |
| Hamming geometry | `Fin n → X`, `hammingBall`, `nearest`, `pairDistances`, guarded `dmin` |
| Minimum-distance definedness | `dmin` returns `none` for fewer than two words. Internal `pairMinimum` is used only with the explicit nontrivial-code conditions in targets. |
| Linear/nonlinear codes | Exact submodules and their failed closure criterion over a specified finite field; pointwise word equality |
| Generator/check matrices | `generatorMatrix`, `parityMatrix`; compiled `generator_coordinates` and `parity_coordinates` identify the abstract maps with mG and Hyᵀ |
| Duality | `dualSpace`, with a proved bridge to Mathlib's ordinary bilinear orthogonal complement, including in characteristic two |

The Shannon targets specify the iid law, encoder/decoder types, message rate, quantifiers and error/distortion limits. They do not take Shannon's conclusion as an extra hypothesis. The rate–distortion target retains D>Dmin. The convexity target states the nontrivial open-interval mixing inequality; endpoint inequalities are reflexive. KL's target states nonnegativity of every finite result and the complete zero iff equal-law characterization; infinity is represented explicitly.

## Claim-by-claim status

The target names below are in `Catalog.Information.Targets`. A full witness has the same final name in `Catalog.Information.Verified`. [information-claims.json](information-claims.json) is a navigation registry; [bindings.json](bindings.json) and fresh verification evidence control witness status.

| Catalog claim | Target name | Proof coverage |
| --- | --- | --- |
| [Entropy bounds and maximizing distribution](../concepts/ShannonEntropy.md) | `entropyBounds` | Statement only |
| [Shannon fixed-length source coding theorem](../concepts/ShannonEntropy.md) | `sourceCoding` | Statement only |
| [Entropy chain rule](../concepts/ConditionalEntropy.md) | `chainRule` | Full witness |
| [Conditioning reduces entropy](../concepts/ConditionalEntropy.md) | `conditioningReduces` | Statement only |
| [Fano inequality](../concepts/ConditionalEntropy.md) | `fano` | Statement only |
| [Gibbs inequality](../concepts/RelativeEntropy.md) | `gibbs` | Statement only |
| [Mutual information entropy identities](../concepts/MutualInformation.md) | `informationIdentity` | Statement only |
| [Data processing inequality](../concepts/MutualInformation.md) | `dataProcessing` | Statement only |
| [Channel output normalization](../concepts/StochasticChannel.md) | `outputNormalized` | Full witness |
| [Product channel normalization](../concepts/DiscreteMemorylessChannel.md) | `productNormalized` | Full witness |
| [Shannon noisy-channel coding theorem](../concepts/ChannelCapacity.md) | `channelCoding` | Statement only |
| [Prefix-free codes are uniquely decodable](../concepts/PrefixFreeCode.md) | `prefixUnique` | Full witness |
| [Kraft–McMillan theorem](../concepts/UniquelyDecodableCode.md) | `kraftMcMillan` | Necessity proved; converse open |
| [Shannon expected-length bounds](../concepts/PrefixFreeCode.md) | `sourceLength` | Statement only |
| [Expected separable distortion](../concepts/DistortionMeasure.md) | `expectedBlock` | Full witness |
| [Rate–distortion monotonicity and convexity](../concepts/RateDistortion.md) | `rateDistortionConvex` | Statement only |
| [Shannon rate–distortion theorem](../concepts/RateDistortion.md) | `lossyCoding` | Statement only |
| [Hamming metric laws](../concepts/HammingSpace.md) | `hammingMetric` | Full witness |
| [Hamming ball volume](../concepts/HammingSpace.md) | `hammingVolume` | Statement only |
| [Minimum-distance unique-decoding theorem](../concepts/BlockCode.md) | `uniqueRadius` | Statement only |
| [Hamming sphere-packing bound](../concepts/BlockCode.md) | `hammingBound` | Statement only |
| [Singleton bound](../concepts/BlockCode.md) | `singletonBound` | Statement only |
| [Linear-code cardinality](../concepts/LinearBlockCode.md) | `linearCardinality` | Full witness |
| [Minimum distance equals minimum nonzero weight](../concepts/LinearBlockCode.md) | `distanceWeight` | Full witness |
| [Nonlinearity witness characterization](../concepts/NonlinearBlockCode.md) | `nonlinearWitness` | Full witness |
| [Generator encoding is a linear bijection](../concepts/GeneratorMatrix.md) | `generatorIsomorphism` | Full witness |
| [Generator and parity-check orthogonality](../concepts/ParityCheckMatrix.md) | `checkOrthogonality` | Full witness |
| [Syndrome and coset theorem](../concepts/Syndrome.md) | `syndromeCoset` | Full witness |
| [Dual-code dimension and double dual](../concepts/DualCode.md) | `dualDimension` | Full witness |

The complete witnesses include the entropy chain rule; arbitrary-joint-law expected block distortion; Hamming metric laws; unique decoding from prefix-freeness; finite-field code cardinality and rate; distance–weight equivalence; nonlinear closure witnesses; generator bijection; both directions of full-rank generator/check orthogonality; syndrome/coset invariance; and dual-code dimension and involution. Normalized channel output and product laws complete the set.

The `kraft_necessity` lemma reuses pinned Mathlib's Kraft–McMillan inequality after proving the bridge from symbol encodings to codeword sets. It proves only necessity. The catalog's combined theorem also includes a constructive converse, so no full-claim witness is registered for it. Similarly, an entropy chain-rule proof is not a proof of Fano, data processing or the asymptotic Shannon theorems.

## Build and inspect

```sh
make check-lean
make test-lean
python3 scripts/lean.py get urn:csabs:law/ConditionalEntropy-chain-rule
python3 scripts/lean.py get urn:csabs:theorem/DualCode-dimension-involution
```

`make test-lean` compiles the imported statements, helpers, witnesses and [finite examples](Catalog/InformationTheoryExamples.lean), elaborates the independently recorded expected types, and audits witness axiom dependencies. The examples construct a normalized fair-bit source, compute a Hamming distance, and instantiate the nonlinear-witness theorem on {000,011,101} over F₂.

Only a fresh ignored `verification.json` supports a verified-witness report. Statement-only targets do not count as witnesses, passing finite examples do not prove general targets, and compilation does not independently establish the catalog-to-Lean correspondence or an implementation refinement. The existing Lean/Mathlib dependency pins are unchanged.
