# Keyed block cipher

A family of permutations on fixed-length bit strings, indexed by a nonempty key carrier, with explicit inverse maps.

**Notation:** B_n={0,1}^n; E,D : K×B_n → B_n.

**Stable ID:** `urn:csabs:concept/BlockCipher`

**Categories:** Cryptography → Symmetric cryptography

**Kind:** Mathematical structure

**Prerequisites:** [Fixed-width bit vector](BitVector.md)

## Backlinks

- [Advanced Encryption Standard (AES)](AES.md) — `requiresConcept`
- [Advanced Encryption Standard (AES)](AES.md) — `specializationOf`
- [Galois/Counter Mode (96-bit IV, 128-bit tag profile)](GCM.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Fixed block and key carriers; mutually inverse keyed maps.

**basisKind:** defined-structure

**basisScope:** n≥1; K nonempty; equality is exact bit-string equality. Deterministic total maps on typed blocks; no padding, variable-length messages, authentication or pseudorandomness follows from invertibility.

**verificationObligation:** Map byte and bit order, exact lengths, equality, errors and key handling explicitly. Functional equations alone do not establish computational security or resistance to side channels.

**reviewStatus:** Editorial specification; no cryptographic security proof or compiled claim witness.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-BlockCipher-encrypt"></a>

### encrypt

`urn:csabs:operation/BlockCipher-encrypt`

**signature:** E : K×B_n → B_n

**description:** Apply the forward permutation.

**precondition:** k∈K; x∈B_n.

**postcondition:** E(k,x)∈B_n.

**totality:** total on the stated precondition; outside the domain return an input error without partial output

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Section 5.1

**sourceNote:** Abstract keyed permutation interface; block size generalized from GCM’s 128-bit requirement.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BlockCipher-decrypt"></a>

### decrypt

`urn:csabs:operation/BlockCipher-decrypt`

**signature:** D : K×B_n → B_n

**description:** Apply the inverse permutation.

**precondition:** k∈K; y∈B_n.

**postcondition:** D(k,y)∈B_n.

**totality:** total on the stated precondition; outside the domain return an input error without partial output

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Section 5.1

**sourceNote:** Abstract keyed permutation interface; block size generalized from GCM’s 128-bit requirement.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-BlockCipher-inverse"></a>

### inverse

`urn:csabs:axiom/BlockCipher-inverse`

**statement:** Each keyed forward and inverse map undo one another.

**formalStatement:** D(k,E(k,x))=x ∧ E(k,D(k,y))=y.

**assumptions:** n≥1; K nonempty; equality is exact bit-string equality. Deterministic total maps on typed blocks; no padding, variable-length messages, authentication or pseudorandomness follows from invertibility.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Section 5.1

**sourceNote:** Abstract keyed permutation interface; block size generalized from GCM’s 128-bit requirement.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-BlockCipher-injective"></a>

### injective

`urn:csabs:theorem/BlockCipher-injective`

**statement:** For a fixed key, encryption is injective.

**formalStatement:** E(k,x)=E(k,y) ⇒ x=y.

**assumptions:** n≥1; K nonempty; equality is exact bit-string equality. Deterministic total maps on typed blocks; no padding, variable-length messages, authentication or pseudorandomness follows from invertibility.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Section 5.1

**sourceNote:** Editorial derivation from the linked premises. Abstract keyed permutation interface; block size generalized from GCM’s 128-bit requirement.

**provenanceKind:** derived

**dependsOn:** [inverse](BlockCipher.md#node-urn-csabs-axiom-BlockCipher-inverse)

**proofSketch:** Apply D(k,−) to the equality and simplify both sides using the inverse equation.

## Concept provenance

- [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Section 5.1

**sourceNote:** Abstract keyed permutation interface; block size generalized from GCM’s 128-bit requirement.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/BlockCipher",
    "type": "Concept",
    "shortForm": "BlockCipher",
    "fullName": "Keyed block cipher",
    "definition": "A family of permutations on fixed-length bit strings, indexed by a nonempty key carrier, with explicit inverse maps.",
    "notation": "B_n={0,1}^n; E,D : K×B_n → B_n.",
    "category": [
      "urn:csabs:category/symmetric-cryptography"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "requiresConcept": [
      "urn:csabs:concept/BitVector"
    ],
    "axiomBasis": "Fixed block and key carriers; mutually inverse keyed maps.",
    "basisKind": "defined-structure",
    "basisScope": "n≥1; K nonempty; equality is exact bit-string equality. Deterministic total maps on typed blocks; no padding, variable-length messages, authentication or pseudorandomness follows from invertibility.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial specification; no cryptographic security proof or compiled claim witness.",
    "verificationObligation": [
      "Map byte and bit order, exact lengths, equality, errors and key handling explicitly. Functional equations alone do not establish computational security or resistance to side channels."
    ],
    "hasOperation": [
      "urn:csabs:operation/BlockCipher-encrypt",
      "urn:csabs:operation/BlockCipher-decrypt"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/BlockCipher-inverse"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/BlockCipher-injective"
    ],
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Section 5.1",
    "sourceNote": "Abstract keyed permutation interface; block size generalized from GCM’s 128-bit requirement.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BlockCipher-encrypt",
    "type": "Operation",
    "name": "encrypt",
    "signature": "E : K×B_n → B_n",
    "description": "Apply the forward permutation.",
    "precondition": "k∈K; x∈B_n.",
    "postcondition": "E(k,x)∈B_n.",
    "totality": "total on the stated precondition; outside the domain return an input error without partial output",
    "concept": "urn:csabs:concept/BlockCipher",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Section 5.1",
    "sourceNote": "Abstract keyed permutation interface; block size generalized from GCM’s 128-bit requirement.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BlockCipher-decrypt",
    "type": "Operation",
    "name": "decrypt",
    "signature": "D : K×B_n → B_n",
    "description": "Apply the inverse permutation.",
    "precondition": "k∈K; y∈B_n.",
    "postcondition": "D(k,y)∈B_n.",
    "totality": "total on the stated precondition; outside the domain return an input error without partial output",
    "concept": "urn:csabs:concept/BlockCipher",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Section 5.1",
    "sourceNote": "Abstract keyed permutation interface; block size generalized from GCM’s 128-bit requirement.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/BlockCipher-inverse",
    "type": "Axiom",
    "name": "inverse",
    "statement": "Each keyed forward and inverse map undo one another.",
    "formalStatement": "D(k,E(k,x))=x ∧ E(k,D(k,y))=y.",
    "assumptions": [
      "n≥1; K nonempty; equality is exact bit-string equality. Deterministic total maps on typed blocks; no padding, variable-length messages, authentication or pseudorandomness follows from invertibility."
    ],
    "appliesTo": [
      "urn:csabs:concept/BlockCipher"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Section 5.1",
    "sourceNote": "Abstract keyed permutation interface; block size generalized from GCM’s 128-bit requirement.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/BlockCipher-injective",
    "type": "Theorem",
    "name": "injective",
    "statement": "For a fixed key, encryption is injective.",
    "formalStatement": "E(k,x)=E(k,y) ⇒ x=y.",
    "assumptions": [
      "n≥1; K nonempty; equality is exact bit-string equality. Deterministic total maps on typed blocks; no padding, variable-length messages, authentication or pseudorandomness follows from invertibility."
    ],
    "appliesTo": [
      "urn:csabs:concept/BlockCipher"
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Section 5.1",
    "sourceNote": "Editorial derivation from the linked premises. Abstract keyed permutation interface; block size generalized from GCM’s 128-bit requirement.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/BlockCipher-inverse"
    ],
    "proofSketch": "Apply D(k,−) to the equality and simplify both sides using the inverse equation."
  }
]
```
<!-- graph-record:end -->
