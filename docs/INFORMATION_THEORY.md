# Information theory and coding

The catalog has 19 abstractions for finite information theory, binary source coding, and finite-alphabet channel codes. The authoritative definitions, operations, claims and direct sources are in the linked concept records. The subject hierarchy is Information theory → Coding theory → Source coding / Channel coding; subject membership does not transfer axioms.

## Concepts and interfaces

| Area | Records | Interface and conventions |
| --- | --- | --- |
| Information measures | [ShannonEntropy](../concepts/ShannonEntropy.md), [ConditionalEntropy](../concepts/ConditionalEntropy.md), [RelativeEntropy](../concepts/RelativeEntropy.md), [MutualInformation](../concepts/MutualInformation.md) | Finite normalized laws; bits; zero mass contributes zero; KL can be infinite. Conditional entropy averages over positive-mass conditioning events. |
| Channels | [StochasticChannel](../concepts/StochasticChannel.md), [DiscreteMemorylessChannel](../concepts/DiscreteMemorylessChannel.md), [ChannelCapacity](../concepts/ChannelCapacity.md) | Normalized finite kernels, stationary conditional product extension, asymptotic average block error. No channel input constraint or feedback. |
| Lossless source coding | [UniquelyDecodableCode](../concepts/UniquelyDecodableCode.md), [PrefixFreeCode](../concepts/PrefixFreeCode.md) | Symbol-to-bit-string maps and concatenation; positive codeword lengths, including singleton sources. |
| Lossy source coding | [DistortionMeasure](../concepts/DistortionMeasure.md), [RateDistortion](../concepts/RateDistortion.md) | Finite nonnegative costs need not be metrics. Average separable distortion; infeasible information infima are positive infinity. The operational theorem is stated for D strictly above the minimum feasible distortion. |
| General channel coding | [HammingSpace](../concepts/HammingSpace.md), [BlockCode](../concepts/BlockCode.md) | Nonempty fixed-length codebook, chosen encoder bijection, supplied decoder with failure, all nearest words on ties, distance distribution and Hamming balls. Minimum distance is undefined for singleton codebooks. |
| Linear coding | [LinearBlockCode](../concepts/LinearBlockCode.md), [GeneratorMatrix](../concepts/GeneratorMatrix.md), [ParityCheckMatrix](../concepts/ParityCheckMatrix.md), [Syndrome](../concepts/Syndrome.md), [DualCode](../concepts/DualCode.md) | Exact finite-field arithmetic; row-vector encoding c=mG; checks and syndromes Hcᵀ; ordinary bilinear dual, not Hermitian. The zero-dimensional code is permitted. |
| Nonlinear coding | [NonlinearBlockCode](../concepts/NonlinearBlockCode.md) | A finite-field codebook failing the subspace criterion, with an explicit nonlinearity witness. General distance and packing results still apply. |

Codebooks are sets, while encoders and decoders are functions chosen for them. A nonlinear decoder does not make its codebook nonlinear. Linearity depends on the chosen field structure and origin; a translated linear code can be nonlinear under this convention. Codes over arbitrary symbol alphabets have Hamming geometry without an intrinsic notion of field linearity.

Linear and nonlinear codes specialize BlockCode under explicit alphabet identifications. Generator/check matrices are representations associated with a linear code, and duality is a construction on codes; these are not specialization edges. DMC retains the one-use stochastic kernel and adds its product extension. PrefixFreeCode retains the source encoding interface and adds the prefix condition; the unique-decoding theorem is linked explicitly.

## Theorems and derived laws

The records include 24 theorems and five derived laws. Familiar results include:

| Result | Owning concept | Principal restrictions |
| --- | --- | --- |
| Entropy bounds and uniform maximizer | ShannonEntropy | Finite nonempty alphabet, exact law |
| Shannon fixed-length source coding | ShannonEntropy | iid finite source, average block error tending to zero |
| Entropy chain rule; conditioning reduces entropy | ConditionalEntropy | Finite joint laws; reduction holds on average, not for every conditioning value |
| Gibbs inequality | RelativeEntropy | Same alphabet; infinity on support mismatch |
| Mutual-information entropy identities and data processing | MutualInformation | Data processing requires the explicit Markov factorization |
| Fano inequality | ConditionalEntropy | At least two possible source symbols; stated deterministic estimator |
| Shannon noisy-channel coding | ChannelCapacity | Finite stationary memoryless channel; unconstrained input; asymptotic vanishing average error |
| Kraft–McMillan and expected-length bounds | UniquelyDecodableCode / PrefixFreeCode | Binary codes, positive integer lengths; expected-length construction assumes positive source masses |
| Shannon rate–distortion theorem | RateDistortion | Finite iid source, bounded costs, expected average distortion, D>Dmin |
| Hamming ball volume and metric laws | HammingSpace | Symbol substitutions in a fixed-length word space |
| Minimum-distance unique decoding; Hamming and Singleton bounds | BlockCode | At least two codewords; linearity is not needed |
| Cardinality and distance–weight identity | LinearBlockCode | Field-linear subspace; minimum-weight identity requires positive dimension |
| Generator bijection, generator/check orthogonality | GeneratorMatrix / ParityCheckMatrix | Explicit full ranks and row convention |
| Syndrome/coset theorem | Syndrome | Fixed full-rank parity-check matrix and its kernel |
| Dual dimension and double dual | DualCode | Nondegenerate ordinary finite-field dot product |

The general decoding, Hamming and Singleton results have one shared structured record each, with explicit applicability to linear and nonlinear codes. Their conditions still apply when retrieved through a specialization. For a singleton source, the positive-length convention gives an optimal one-bit word although H=0, so the expected-length upper bound is ≤H+1. Strict <H+1 is stated only for full-support sources with at least two symbols.

## Small examples

Over F₂, C={000,111} is a one-dimensional linear code: n=3, k=1, d=3. One row generator and a check matrix are

```text
G = [1 1 1]          H = [1 1 0]
                        [0 1 1]
```

There are two codewords and four words per radius-one Hamming ball; 2×4=2³ meets the Hamming bound. For received y=101, Hyᵀ=(1,1)ᵀ, the same syndrome as error e=010. Unique nearest decoding recovers 111. At radius two, the two decoding balls overlap, as the distance theorem predicts.

D={000,011,101} is a nonlinear binary code: 011+101=110 is absent. Its size three cannot equal 2^k for an integer dimension k. Its minimum distance is two. At y=001 all three codewords are at distance one, so a decoder needs an explicit tie/failure policy. A nonlinear code need not contain zero; even a nonzero singleton is nonlinear under the fixed-origin convention.

These examples illustrate the interfaces; they are not universal proofs or registered Lean witnesses.

## Retrieval and evidence

```sh
python3 scripts/catalog.py list --category information-theory
python3 scripts/catalog.py get LinearBlockCode --sections operations axioms laws theorems
python3 scripts/agent_query.py node urn:csabs:theorem/BlockCode-hamming-bound
python3 scripts/agent_query.py dossier ChannelCapacity --purpose proof --limit 80
```

Check truncation and fetch omitted premises. Sources were consulted on 2026-11-11: Polyanskiy's MIT 6.441 chapters 1, 2, 5–7, 14, 16, 23–24; Böcherer's *Lecture Notes on Channel Coding* (2016); and Guruswami's CMU *Notes 1* (2010). Each new claim cites its source directly with a locator, adaptation note and derivation premises. The q-ary volume/packing argument explicitly adapts the consulted binary counting argument.

[InformationTheory.lean](../lean/Catalog/InformationTheory.lean) supplies the exact finite-law and code core. The [concrete Lean formulations](../lean/INFORMATION_THEORY.md) now cover all 29 laws/theorems as quantified propositions, including operational source/channel codes, average block-error sums, positive-length code sequences, rate limits and the constrained rate–distortion infimum. Thirteen full claims have registered proof witnesses, with independently expanded expected types and explicit premise mappings. The other 16 remain unproved targets; Kraft–McMillan has an additional compiled proof of necessity only. A target of type `Prop` is not a theorem witness.

The finite-field models now include concrete generator/check matrices with proved coordinate bridges, normalized channel output/product laws, and constructed dual submodules. Model bindings disclose any remaining partial interfaces. A fresh Lean verification report is required to call registered witnesses verified; catalog source provenance and mathematical correspondence remain separate obligations.

This profile does not yet introduce concrete families such as Hamming, Reed–Solomon, BCH, LDPC or polar codes, or continuous signal-space/neural encoders. It supplies the interfaces and bounds on which those separate constructions can build.
