# Learning with errors (finite modular distribution profile)

A family of noisy modular linear sample distributions, with search and decision experiments defined by one secret shared across independent samples.

**Notation:** s∈(ℤ/qℤ)^n; a←U((ℤ/qℤ)^n); e←χ; (a,b)=(a,⟨a,s⟩+e mod q).

**Stable ID:** `urn:csabs:concept/LWE`

**Categories:** Cryptography → Public-key cryptography → Lattice-based cryptography

**Kind:** semantic-model

**Prerequisites:** [Modular Integer](ModularInteger.md), [Finitely supported probability distribution](FiniteDistribution.md)

**Related concepts:** [q-ary kernel lattice](QaryLattice.md), [Closest vector problem (Euclidean search relation)](CVP.md), [Short integer solution problem (Euclidean norm profile)](SIS.md)

## Mathematical formulation

For n>0,q≥2, secret s and input a in (ℤ/qℤ)^n, and error e∈ℤ/qℤ, encode(s,a,e)=Σ\_i a\_i s\_i+e. The interface stores a normalized finite error law; uniform independent sampling and the fixed-secret experiment remain separate.

**Lean formulation** (in its source module context):

```lean
structure LWE (n q : Nat) where
  dimension_positive : 0 < n
  modulus_valid : 2 ≤ q
  errorLaw : FiniteDistribution (ZMod q)
```

**Source:** [`Catalog.LWE`](../lean/Catalog/GeometricLattices.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Positive dimension, modulus q>=2, normalized FiniteDistribution on ZMod q; encode computes the exact modular dot product plus supplied error.

**Limits:** Uniform input sampling, independent errors, one reused secret, joint sample distributions, search/decision experiments and probability/security witnesses are not constructed.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Normalized modular error distribution, independent sample rule and fixed-secret search/decision experiments.

**basisKind:** defined-structure

**basisScope:** n≥1 and integer q≥2, possibly composite; χ is a normalized probability mass function on ℤ/qℤ with exact real probabilities. Integer errors may be reduced modulo q to obtain χ. Sample counts m≥0 are finite. For a fixed s, draws of a and e are independent across and within samples. Search/decision experiments choose s uniformly once and reuse it for all m samples; samples are conditionally independent given s, generally not independent after averaging over s. Equality is residue and coordinate equality; no norm bound or Gaussian form is assumed. Arbitrary χ and parameters need not give hardness or unique secret recovery.

**verificationObligation:** Map exact carriers, equality, matrix orientation, norm, parameter ranges, randomness and error behavior before software use. Complexity statements require finite input encodings. Problem definitions and algebraic correctness do not establish hardness or security.

**reviewStatus:** Editorial mathematics; no compiled claim witness or cryptographic hardness proof.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-LWE-sample-law"></a>

### sample-law

`urn:csabs:operation/LWE-sample-law`

**source:** [Oded Regev: On Lattices, Learning with Errors, Random Linear Codes, and Cryptography (2009-05-02 author manuscript)](https://cims.nyu.edu/~regev/papers/qcrypto.pdf); accessedOn: 2026-11-11; sourceRole: original research paper; [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Regev §1, pp. 1–3 (modular-error formulation); Peikert §4.2.1, Definitions 4.2.1–4.2.3

**sourceNote:** Uses χ on the finite residue ring as in Regev, permitting wrapped integer-error distributions. Generic composite q is a definition-level extension; no source reduction theorem is asserted for every q or χ.

**provenanceKind:** adapted

**signature:** sampleLaw : ((ℤ/qℤ)^n)×Dist_fin(ℤ/qℤ) → Dist_fin((ℤ/qℤ)^n×ℤ/qℤ)

**description:** Specify one LWE sample for a supplied secret.

**precondition:** Valid n,q and normalized χ; fixed secret s.

**postcondition:** Draw uniform a and independent e←χ; return (a,⟨a,s⟩+e). This is a distribution, not an implementation of a random generator.

**totality:** Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted.

<a id="node-urn-csabs-operation-LWE-search-experiment"></a>

### search-experiment

`urn:csabs:operation/LWE-search-experiment`

**source:** [Oded Regev: On Lattices, Learning with Errors, Random Linear Codes, and Cryptography (2009-05-02 author manuscript)](https://cims.nyu.edu/~regev/papers/qcrypto.pdf); accessedOn: 2026-11-11; sourceRole: original research paper; [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Regev §1, pp. 1–3 (modular-error formulation); Peikert §4.2.1, Definitions 4.2.1–4.2.3

**sourceNote:** Uses χ on the finite residue ring as in Regev, permitting wrapped integer-error distributions. Generic composite q is a definition-level extension; no source reduction theorem is asserted for every q or χ.

**provenanceKind:** adapted

**signature:** searchExperiment : (n,q,χ,m) → Dist_fin(Secret×Samples_m)

**description:** Specify the hidden-secret recovery experiment.

**precondition:** m≥0 and valid distribution parameters.

**postcondition:** Choose uniform s once; draw m conditionally independent samples from sampleLaw(s,χ). A search algorithm sees only Samples_m and succeeds when its output equals s; the hidden s is retained only to define success.

**totality:** Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted.

<a id="node-urn-csabs-operation-LWE-decision-law"></a>

### decision-law

`urn:csabs:operation/LWE-decision-law`

**source:** [Oded Regev: On Lattices, Learning with Errors, Random Linear Codes, and Cryptography (2009-05-02 author manuscript)](https://cims.nyu.edu/~regev/papers/qcrypto.pdf); accessedOn: 2026-11-11; sourceRole: original research paper; [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Regev §1, pp. 1–3 (modular-error formulation); Peikert §4.2.1, Definitions 4.2.1–4.2.3

**sourceNote:** Uses χ on the finite residue ring as in Regev, permitting wrapped integer-error distributions. Generic composite q is a definition-level extension; no source reduction theorem is asserted for every q or χ.

**provenanceKind:** adapted

**signature:** decisionLaw : (n,q,χ,m)×{0,1} → Dist_fin(Samples_m)

**description:** Specify the two distributions to be distinguished.

**precondition:** Valid parameters and branch c∈{0,1}.

**postcondition:** At c=0 return the marginal sample list from searchExperiment; at c=1 return m independent uniform pairs. No particular distinguisher or advantage threshold is assumed.

**totality:** Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-LWE-sample"></a>

### sample

`urn:csabs:axiom/LWE-sample`

**source:** [Oded Regev: On Lattices, Learning with Errors, Random Linear Codes, and Cryptography (2009-05-02 author manuscript)](https://cims.nyu.edu/~regev/papers/qcrypto.pdf); accessedOn: 2026-11-11; sourceRole: original research paper; [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Regev §1, pp. 1–3 (modular-error formulation); Peikert §4.2.1, Definitions 4.2.1–4.2.3

**sourceNote:** Uses χ on the finite residue ring as in Regev, permitting wrapped integer-error distributions. Generic composite q is a definition-level extension; no source reduction theorem is asserted for every q or χ.

**provenanceKind:** adapted

**statement:** Each pair is a deterministic affine image of independent uniform input and error draws.

**formalStatement:** χ:ℤ/qℤ→ℝ_{≥0}, Σ_eχ(e)=1; a←U((ℤ/qℤ)^n), e←χ independently; b=⟨a,s⟩+e.

**assumptions:** n≥1 and integer q≥2, possibly composite; χ is a normalized probability mass function on ℤ/qℤ with exact real probabilities. Integer errors may be reduced modulo q to obtain χ. Sample counts m≥0 are finite. For a fixed s, draws of a and e are independent across and within samples. Search/decision experiments choose s uniformly once and reuse it for all m samples; samples are conditionally independent given s, generally not independent after averaging over s. Equality is residue and coordinate equality; no norm bound or Gaussian form is assumed. Arbitrary χ and parameters need not give hardness or unique secret recovery.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

<a id="node-urn-csabs-axiom-LWE-experiment"></a>

### experiment

`urn:csabs:axiom/LWE-experiment`

**source:** [Oded Regev: On Lattices, Learning with Errors, Random Linear Codes, and Cryptography (2009-05-02 author manuscript)](https://cims.nyu.edu/~regev/papers/qcrypto.pdf); accessedOn: 2026-11-11; sourceRole: original research paper; [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Regev §1, pp. 1–3 (modular-error formulation); Peikert §4.2.1, Definitions 4.2.1–4.2.3

**sourceNote:** Uses χ on the finite residue ring as in Regev, permitting wrapped integer-error distributions. Generic composite q is a definition-level extension; no source reduction theorem is asserted for every q or χ.

**provenanceKind:** adapted

**statement:** The uniform secret is chosen once for the whole real experiment.

**formalStatement:** s←U((ℤ/qℤ)^n); ((a_i,e_i))_{i=1}^m independent given s; b_i=⟨a_i,s⟩+e_i; search success ⇔ ŝ=s; decision compares this sample-list marginal with U(((ℤ/qℤ)^n×ℤ/qℤ)^m).

**assumptions:** n≥1 and integer q≥2, possibly composite; χ is a normalized probability mass function on ℤ/qℤ with exact real probabilities. Integer errors may be reduced modulo q to obtain χ. Sample counts m≥0 are finite. For a fixed s, draws of a and e are independent across and within samples. Search/decision experiments choose s uniformly once and reuse it for all m samples; samples are conditionally independent given s, generally not independent after averaging over s. Equality is residue and coordinate equality; no norm bound or Gaussian form is assumed. Arbitrary χ and parameters need not give hardness or unique secret recovery.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-LWE-sample-mass"></a>

### sample-mass

`urn:csabs:theorem/LWE-sample-mass`

**source:** [Oded Regev: On Lattices, Learning with Errors, Random Linear Codes, and Cryptography (2009-05-02 author manuscript)](https://cims.nyu.edu/~regev/papers/qcrypto.pdf); accessedOn: 2026-11-11; sourceRole: original research paper; [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Regev §1, pp. 1–3 (modular-error formulation); Peikert §4.2.1, Definitions 4.2.1–4.2.3

**sourceNote:** Editorial derivation from the linked premises. Uses χ on the finite residue ring as in Regev, permitting wrapped integer-error distributions. Generic composite q is a definition-level extension; no source reduction theorem is asserted for every q or χ.

**provenanceKind:** derived

**statement:** The pair probability is a translated error mass times the uniform input mass.

**formalStatement:** For fixed s, Pr[(a,b)]=(1/q^n)χ(b−⟨a,s⟩); Σ_{a,b}Pr[(a,b)]=1.

**dependsOn:** [sample](LWE.md#node-urn-csabs-axiom-LWE-sample)

**proofSketch:** For specified a,b exactly one residue e=b−⟨a,s⟩ produces b. Independence multiplies q^(−n) by χ(e). Translation permutes the residues, so summing over b gives 1 for each a, and summing over the q^n choices of a normalizes.

**assumptions:** n≥1 and integer q≥2, possibly composite; χ is a normalized probability mass function on ℤ/qℤ with exact real probabilities. Integer errors may be reduced modulo q to obtain χ. Sample counts m≥0 are finite. For a fixed s, draws of a and e are independent across and within samples. Search/decision experiments choose s uniformly once and reuse it for all m samples; samples are conditionally independent given s, generally not independent after averaging over s. Equality is residue and coordinate equality; no norm bound or Gaussian form is assumed. Arbitrary χ and parameters need not give hardness or unique secret recovery.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

<a id="node-urn-csabs-theorem-LWE-uniform-noise"></a>

### uniform-noise

`urn:csabs:theorem/LWE-uniform-noise`

**source:** [Oded Regev: On Lattices, Learning with Errors, Random Linear Codes, and Cryptography (2009-05-02 author manuscript)](https://cims.nyu.edu/~regev/papers/qcrypto.pdf); accessedOn: 2026-11-11; sourceRole: original research paper; [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Regev §1, pp. 1–3 (modular-error formulation); Peikert §4.2.1, Definitions 4.2.1–4.2.3

**sourceNote:** Editorial derivation from the linked premises. Uses χ on the finite residue ring as in Regev, permitting wrapped integer-error distributions. Generic composite q is a definition-level extension; no source reduction theorem is asserted for every q or χ.

**provenanceKind:** derived

**statement:** Uniform modular error makes every sample uniform and independent of the secret.

**formalStatement:** (∀e, χ(e)=1/q) ⇒ ∀s, sampleLaw(s,χ)=U((ℤ/qℤ)^n×ℤ/qℤ); decisionLaw(…,0)=decisionLaw(…,1).

**dependsOn:** [sample-mass](LWE.md#node-urn-csabs-theorem-LWE-sample-mass); [experiment](LWE.md#node-urn-csabs-axiom-LWE-experiment)

**proofSketch:** Substitute χ(e)=1/q into sample-mass to obtain the constant probability q^(−(n+1)), independent of s. Conditional products for m samples are the same uniform law for every s, so marginalizing s preserves it, including the empty-list case m=0.

**assumptions:** n≥1 and integer q≥2, possibly composite; χ is a normalized probability mass function on ℤ/qℤ with exact real probabilities. Integer errors may be reduced modulo q to obtain χ. Sample counts m≥0 are finite. For a fixed s, draws of a and e are independent across and within samples. Search/decision experiments choose s uniformly once and reuse it for all m samples; samples are conditionally independent given s, generally not independent after averaging over s. Equality is residue and coordinate equality; no norm bound or Gaussian form is assumed. Arbitrary χ and parameters need not give hardness or unique secret recovery.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

## Concept provenance

- [Oded Regev: On Lattices, Learning with Errors, Random Linear Codes, and Cryptography (2009-05-02 author manuscript)](https://cims.nyu.edu/~regev/papers/qcrypto.pdf); accessedOn: 2026-11-11; sourceRole: original research paper
- [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Regev §1, pp. 1–3 (modular-error formulation); Peikert §4.2.1, Definitions 4.2.1–4.2.3

**sourceNote:** Uses χ on the finite residue ring as in Regev, permitting wrapped integer-error distributions. Generic composite q is a definition-level extension; no source reduction theorem is asserted for every q or χ.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/LWE",
    "type": "Concept",
    "shortForm": "LWE",
    "fullName": "Learning with errors (finite modular distribution profile)",
    "definition": "A family of noisy modular linear sample distributions, with search and decision experiments defined by one secret shared across independent samples.",
    "notation": "s∈(ℤ/qℤ)^n; a←U((ℤ/qℤ)^n); e←χ; (a,b)=(a,⟨a,s⟩+e mod q).",
    "category": [
      "urn:csabs:category/lattice-cryptography"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/ModularInteger",
      "urn:csabs:concept/FiniteDistribution"
    ],
    "axiomBasis": "Normalized modular error distribution, independent sample rule and fixed-secret search/decision experiments.",
    "basisKind": "defined-structure",
    "basisScope": "n≥1 and integer q≥2, possibly composite; χ is a normalized probability mass function on ℤ/qℤ with exact real probabilities. Integer errors may be reduced modulo q to obtain χ. Sample counts m≥0 are finite. For a fixed s, draws of a and e are independent across and within samples. Search/decision experiments choose s uniformly once and reuse it for all m samples; samples are conditionally independent given s, generally not independent after averaging over s. Equality is residue and coordinate equality; no norm bound or Gaussian form is assumed. Arbitrary χ and parameters need not give hardness or unique secret recovery.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematics; no compiled claim witness or cryptographic hardness proof.",
    "verificationObligation": [
      "Map exact carriers, equality, matrix orientation, norm, parameter ranges, randomness and error behavior before software use. Complexity statements require finite input encodings. Problem definitions and algebraic correctness do not establish hardness or security."
    ],
    "source": [
      "urn:csabs:source/regev-lwe-2009",
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Regev §1, pp. 1–3 (modular-error formulation); Peikert §4.2.1, Definitions 4.2.1–4.2.3",
    "sourceNote": "Uses χ on the finite residue ring as in Regev, permitting wrapped integer-error distributions. Generic composite q is a definition-level extension; no source reduction theorem is asserted for every q or χ.",
    "provenanceKind": "adapted",
    "relatedConcept": [
      "urn:csabs:concept/QaryLattice",
      "urn:csabs:concept/CVP",
      "urn:csabs:concept/SIS"
    ],
    "hasOperation": [
      "urn:csabs:operation/LWE-sample-law",
      "urn:csabs:operation/LWE-search-experiment",
      "urn:csabs:operation/LWE-decision-law"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/LWE-sample",
      "urn:csabs:axiom/LWE-experiment"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/LWE-sample-mass",
      "urn:csabs:theorem/LWE-uniform-noise"
    ],
    "hasLaw": [],
    "leanFormulation": "structure LWE (n q : Nat) where\n  dimension_positive : 0 < n\n  modulus_valid : 2 ≤ q\n  errorLaw : FiniteDistribution (ZMod q)",
    "formulationSource": "urn:csabs:source/local-lean-GeometricLattices",
    "formulationLocator": "Catalog.LWE",
    "formulationScope": "partial",
    "leanModelMapping": "Positive dimension, modulus q>=2, normalized FiniteDistribution on ZMod q; encode computes the exact modular dot product plus supplied error.",
    "leanModelLimitations": "Uniform input sampling, independent errors, one reused secret, joint sample distributions, search/decision experiments and probability/security witnesses are not constructed.",
    "mathematicalFormulation": "For n>0,q≥2, secret s and input a in (ℤ/qℤ)^n, and error e∈ℤ/qℤ, encode(s,a,e)=Σ_i a_i s_i+e. The interface stores a normalized finite error law; uniform independent sampling and the fixed-secret experiment remain separate."
  },
  {
    "id": "urn:csabs:operation/LWE-sample-law",
    "type": "Operation",
    "name": "sample-law",
    "source": [
      "urn:csabs:source/regev-lwe-2009",
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Regev §1, pp. 1–3 (modular-error formulation); Peikert §4.2.1, Definitions 4.2.1–4.2.3",
    "sourceNote": "Uses χ on the finite residue ring as in Regev, permitting wrapped integer-error distributions. Generic composite q is a definition-level extension; no source reduction theorem is asserted for every q or χ.",
    "provenanceKind": "adapted",
    "signature": "sampleLaw : ((ℤ/qℤ)^n)×Dist_fin(ℤ/qℤ) → Dist_fin((ℤ/qℤ)^n×ℤ/qℤ)",
    "description": "Specify one LWE sample for a supplied secret.",
    "precondition": "Valid n,q and normalized χ; fixed secret s.",
    "postcondition": "Draw uniform a and independent e←χ; return (a,⟨a,s⟩+e). This is a distribution, not an implementation of a random generator.",
    "concept": "urn:csabs:concept/LWE",
    "totality": "Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted."
  },
  {
    "id": "urn:csabs:operation/LWE-search-experiment",
    "type": "Operation",
    "name": "search-experiment",
    "source": [
      "urn:csabs:source/regev-lwe-2009",
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Regev §1, pp. 1–3 (modular-error formulation); Peikert §4.2.1, Definitions 4.2.1–4.2.3",
    "sourceNote": "Uses χ on the finite residue ring as in Regev, permitting wrapped integer-error distributions. Generic composite q is a definition-level extension; no source reduction theorem is asserted for every q or χ.",
    "provenanceKind": "adapted",
    "signature": "searchExperiment : (n,q,χ,m) → Dist_fin(Secret×Samples_m)",
    "description": "Specify the hidden-secret recovery experiment.",
    "precondition": "m≥0 and valid distribution parameters.",
    "postcondition": "Choose uniform s once; draw m conditionally independent samples from sampleLaw(s,χ). A search algorithm sees only Samples_m and succeeds when its output equals s; the hidden s is retained only to define success.",
    "concept": "urn:csabs:concept/LWE",
    "totality": "Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted."
  },
  {
    "id": "urn:csabs:operation/LWE-decision-law",
    "type": "Operation",
    "name": "decision-law",
    "source": [
      "urn:csabs:source/regev-lwe-2009",
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Regev §1, pp. 1–3 (modular-error formulation); Peikert §4.2.1, Definitions 4.2.1–4.2.3",
    "sourceNote": "Uses χ on the finite residue ring as in Regev, permitting wrapped integer-error distributions. Generic composite q is a definition-level extension; no source reduction theorem is asserted for every q or χ.",
    "provenanceKind": "adapted",
    "signature": "decisionLaw : (n,q,χ,m)×{0,1} → Dist_fin(Samples_m)",
    "description": "Specify the two distributions to be distinguished.",
    "precondition": "Valid parameters and branch c∈{0,1}.",
    "postcondition": "At c=0 return the marginal sample list from searchExperiment; at c=1 return m independent uniform pairs. No particular distinguisher or advantage threshold is assumed.",
    "concept": "urn:csabs:concept/LWE",
    "totality": "Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted."
  },
  {
    "id": "urn:csabs:axiom/LWE-sample",
    "type": "Axiom",
    "name": "sample",
    "source": [
      "urn:csabs:source/regev-lwe-2009",
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Regev §1, pp. 1–3 (modular-error formulation); Peikert §4.2.1, Definitions 4.2.1–4.2.3",
    "sourceNote": "Uses χ on the finite residue ring as in Regev, permitting wrapped integer-error distributions. Generic composite q is a definition-level extension; no source reduction theorem is asserted for every q or χ.",
    "provenanceKind": "adapted",
    "statement": "Each pair is a deterministic affine image of independent uniform input and error draws.",
    "formalStatement": "χ:ℤ/qℤ→ℝ_{≥0}, Σ_eχ(e)=1; a←U((ℤ/qℤ)^n), e←χ independently; b=⟨a,s⟩+e.",
    "appliesTo": [
      "urn:csabs:concept/LWE"
    ],
    "assumptions": [
      "n≥1 and integer q≥2, possibly composite; χ is a normalized probability mass function on ℤ/qℤ with exact real probabilities. Integer errors may be reduced modulo q to obtain χ. Sample counts m≥0 are finite. For a fixed s, draws of a and e are independent across and within samples. Search/decision experiments choose s uniformly once and reuse it for all m samples; samples are conditionally independent given s, generally not independent after averaging over s. Equality is residue and coordinate equality; no norm bound or Gaussian form is assumed. Arbitrary χ and parameters need not give hardness or unique secret recovery."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  },
  {
    "id": "urn:csabs:axiom/LWE-experiment",
    "type": "Axiom",
    "name": "experiment",
    "source": [
      "urn:csabs:source/regev-lwe-2009",
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Regev §1, pp. 1–3 (modular-error formulation); Peikert §4.2.1, Definitions 4.2.1–4.2.3",
    "sourceNote": "Uses χ on the finite residue ring as in Regev, permitting wrapped integer-error distributions. Generic composite q is a definition-level extension; no source reduction theorem is asserted for every q or χ.",
    "provenanceKind": "adapted",
    "statement": "The uniform secret is chosen once for the whole real experiment.",
    "formalStatement": "s←U((ℤ/qℤ)^n); ((a_i,e_i))_{i=1}^m independent given s; b_i=⟨a_i,s⟩+e_i; search success ⇔ ŝ=s; decision compares this sample-list marginal with U(((ℤ/qℤ)^n×ℤ/qℤ)^m).",
    "appliesTo": [
      "urn:csabs:concept/LWE"
    ],
    "assumptions": [
      "n≥1 and integer q≥2, possibly composite; χ is a normalized probability mass function on ℤ/qℤ with exact real probabilities. Integer errors may be reduced modulo q to obtain χ. Sample counts m≥0 are finite. For a fixed s, draws of a and e are independent across and within samples. Search/decision experiments choose s uniformly once and reuse it for all m samples; samples are conditionally independent given s, generally not independent after averaging over s. Equality is residue and coordinate equality; no norm bound or Gaussian form is assumed. Arbitrary χ and parameters need not give hardness or unique secret recovery."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  },
  {
    "id": "urn:csabs:theorem/LWE-sample-mass",
    "type": "Theorem",
    "name": "sample-mass",
    "source": [
      "urn:csabs:source/regev-lwe-2009",
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Regev §1, pp. 1–3 (modular-error formulation); Peikert §4.2.1, Definitions 4.2.1–4.2.3",
    "sourceNote": "Editorial derivation from the linked premises. Uses χ on the finite residue ring as in Regev, permitting wrapped integer-error distributions. Generic composite q is a definition-level extension; no source reduction theorem is asserted for every q or χ.",
    "provenanceKind": "derived",
    "statement": "The pair probability is a translated error mass times the uniform input mass.",
    "formalStatement": "For fixed s, Pr[(a,b)]=(1/q^n)χ(b−⟨a,s⟩); Σ_{a,b}Pr[(a,b)]=1.",
    "dependsOn": [
      "urn:csabs:axiom/LWE-sample"
    ],
    "proofSketch": "For specified a,b exactly one residue e=b−⟨a,s⟩ produces b. Independence multiplies q^(−n) by χ(e). Translation permutes the residues, so summing over b gives 1 for each a, and summing over the q^n choices of a normalizes.",
    "appliesTo": [
      "urn:csabs:concept/LWE"
    ],
    "assumptions": [
      "n≥1 and integer q≥2, possibly composite; χ is a normalized probability mass function on ℤ/qℤ with exact real probabilities. Integer errors may be reduced modulo q to obtain χ. Sample counts m≥0 are finite. For a fixed s, draws of a and e are independent across and within samples. Search/decision experiments choose s uniformly once and reuse it for all m samples; samples are conditionally independent given s, generally not independent after averaging over s. Equality is residue and coordinate equality; no norm bound or Gaussian form is assumed. Arbitrary χ and parameters need not give hardness or unique secret recovery."
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  },
  {
    "id": "urn:csabs:theorem/LWE-uniform-noise",
    "type": "Theorem",
    "name": "uniform-noise",
    "source": [
      "urn:csabs:source/regev-lwe-2009",
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Regev §1, pp. 1–3 (modular-error formulation); Peikert §4.2.1, Definitions 4.2.1–4.2.3",
    "sourceNote": "Editorial derivation from the linked premises. Uses χ on the finite residue ring as in Regev, permitting wrapped integer-error distributions. Generic composite q is a definition-level extension; no source reduction theorem is asserted for every q or χ.",
    "provenanceKind": "derived",
    "statement": "Uniform modular error makes every sample uniform and independent of the secret.",
    "formalStatement": "(∀e, χ(e)=1/q) ⇒ ∀s, sampleLaw(s,χ)=U((ℤ/qℤ)^n×ℤ/qℤ); decisionLaw(…,0)=decisionLaw(…,1).",
    "dependsOn": [
      "urn:csabs:theorem/LWE-sample-mass",
      "urn:csabs:axiom/LWE-experiment"
    ],
    "proofSketch": "Substitute χ(e)=1/q into sample-mass to obtain the constant probability q^(−(n+1)), independent of s. Conditional products for m samples are the same uniform law for every s, so marginalizing s preserves it, including the empty-list case m=0.",
    "appliesTo": [
      "urn:csabs:concept/LWE"
    ],
    "assumptions": [
      "n≥1 and integer q≥2, possibly composite; χ is a normalized probability mass function on ℤ/qℤ with exact real probabilities. Integer errors may be reduced modulo q to obtain χ. Sample counts m≥0 are finite. For a fixed s, draws of a and e are independent across and within samples. Search/decision experiments choose s uniformly once and reuse it for all m samples; samples are conditionally independent given s, generally not independent after averaging over s. Equality is residue and coordinate equality; no norm bound or Gaussian form is assumed. Arbitrary χ and parameters need not give hardness or unique secret recovery."
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  }
]
```
<!-- graph-record:end -->
