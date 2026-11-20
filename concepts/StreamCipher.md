# Synchronous stream cipher (bounded XOR-keystream profile)

A deterministic key- and nonce-indexed bit keystream combined with a finite plaintext by pointwise XOR; decryption uses the same keystream segment.

**Notation:** G:K×N×Fin(L)→Bool; E(k,ν,o,m)[i]=m[i]⊕G(k,ν,o+i); D=E.

**Stable ID:** `urn:csabs:concept/StreamCipher`

**Categories:** Cryptography → Symmetric cryptography

**Kind:** Mathematical structure

**Prerequisites:** [Fixed-width bit vector](BitVector.md)

**Related concepts:** [Keyed block cipher](BlockCipher.md), [Nonce-based authenticated encryption with associated data](AEAD.md), [Galois/Counter Mode (96-bit IV, 128-bit tag profile)](GCM.md)

## Mathematical formulation

G:K×N×Fin(L)→Bool; E(k,ν,o,m)[i]=m[i]⊕G(k,ν,o+i); D=E. Bounded synchronous XOR profile. K and N are nonempty key and nonce carriers with exact equality; L∈ℕ is the available bit capacity per key/nonce stream. B\_n={0,1}^{Fin(n)} has extensional equality, including its unique empty value at n=0. G:K×N×Fin(L)→{0,1} is deterministic and independent of plaintext and ciphertext. Offsets o and lengths n are natural numbers satisfying o+n≤L; operations are total on this admissible domain and undefined outside it, with no modular wraparound or padding. Inputs and outputs have the same bit length. The same key, nonce and offset are required for inversion. Nonce allocation and nonoverlapping stream-position use across encryptions are caller obligations, not enforced by the value model. The profile excludes self-synchronizing ciphers and makes no pseudorandomness, confidentiality, authentication or side-channel assertion.

**Lean formulation** (in its source module context):

```lean
abbrev StreamCipher (K N : Type) (capacity : Nat) := K → N → Fin capacity → Bool
```

**Source:** [`Catalog.StreamCipher`](../lean/Catalog/StreamCipher.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.

**Limits:** Random-access denotation of a bounded synchronous generator, not an implementation of ChaCha20 or a general self-synchronizing cipher. No nonce history, state allocation, block serialization, key sampling or security game. The example generator is intentionally insecure. Nonempty K,N are an instantiation requirement; the generic Lean type does not carry Nonempty fields.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Deterministic plaintext-independent bounded keystream; exact bit-vector carrier and domain; pointwise XOR encryption and decryption using the same segment.

**basisKind:** defined-structure

**basisScope:** Bounded synchronous XOR profile. K and N are nonempty key and nonce carriers with exact equality; L∈ℕ is the available bit capacity per key/nonce stream. B_n={0,1}^{Fin(n)} has extensional equality, including its unique empty value at n=0. G:K×N×Fin(L)→{0,1} is deterministic and independent of plaintext and ciphertext. Offsets o and lengths n are natural numbers satisfying o+n≤L; operations are total on this admissible domain and undefined outside it, with no modular wraparound or padding. Inputs and outputs have the same bit length. The same key, nonce and offset are required for inversion. Nonce allocation and nonoverlapping stream-position use across encryptions are caller obligations, not enforced by the value model. The profile excludes self-synchronizing ciphers and makes no pseudorandomness, confidentiality, authentication or side-channel assertion.

**verificationObligation:** Map key/nonce encoding, bit order, initial counters, capacity and offset units to the concrete algorithm. Reject exhaustion rather than wrapping counters.; Keep encryption stream positions disjoint for a fixed key/nonce across messages; nonce uniqueness across writers and restarts is a typical stronger protocol rule. Unique nonces alone do not establish security for arbitrary G.; The concrete demonstration generator is deliberately insecure. Functional inversion is independent of pseudorandomness; this cipher alone supplies no tag, integrity, replay protection or wrong-key rejection.

**reviewStatus:** Editorial mathematical interface review; only individually registered witnesses have compiler evidence.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-StreamCipher-keystream"></a>

### keystream

`urn:csabs:operation/StreamCipher-keystream`

**signature:** G : K×N×Fin(L)→Bool

**description:** Return the deterministic keystream bit at the specified position, independently of message data.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** Return the deterministic keystream bit at the specified position, independently of message data.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [Nir and Langley, RFC 8439: ChaCha20 and Poly1305 for IETF Protocols (June 2018)](https://www.rfc-editor.org/rfc/rfc8439.html); accessedOn: 2026-11-20; sourceRole: Consulted primary specification, sections 2.4, 2.4.1 and 4: synchronous keystream XOR encryption/decryption, equal lengths and keystream reuse. Adapted to an abstract bounded bit keystream rather than a ChaCha20 implementation.

**sourceLocator:** Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-StreamCipher-xor"></a>

### xor

`urn:csabs:operation/StreamCipher-xor`

**signature:** xor_n : B_n×B_n→B_n

**description:** Combine equal-length bit vectors pointwise with Boolean XOR.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** Combine equal-length bit vectors pointwise with Boolean XOR.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [Nir and Langley, RFC 8439: ChaCha20 and Poly1305 for IETF Protocols (June 2018)](https://www.rfc-editor.org/rfc/rfc8439.html); accessedOn: 2026-11-20; sourceRole: Consulted primary specification, sections 2.4, 2.4.1 and 4: synchronous keystream XOR encryption/decryption, equal lengths and keystream reuse. Adapted to an abstract bounded bit keystream rather than a ChaCha20 implementation.

**sourceLocator:** Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-StreamCipher-encrypt"></a>

### encrypt

`urn:csabs:operation/StreamCipher-encrypt`

**signature:** E : {(k,ν,o,n,m) | k∈K, ν∈N, o,n∈ℕ, o+n≤L, m∈B_n}→B_n

**description:** XOR each plaintext bit with the corresponding bit at stream offset o; return exactly n ciphertext bits.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** XOR each plaintext bit with the corresponding bit at stream offset o; return exactly n ciphertext bits.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [Nir and Langley, RFC 8439: ChaCha20 and Poly1305 for IETF Protocols (June 2018)](https://www.rfc-editor.org/rfc/rfc8439.html); accessedOn: 2026-11-20; sourceRole: Consulted primary specification, sections 2.4, 2.4.1 and 4: synchronous keystream XOR encryption/decryption, equal lengths and keystream reuse. Adapted to an abstract bounded bit keystream rather than a ChaCha20 implementation.

**sourceLocator:** Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-StreamCipher-decrypt"></a>

### decrypt

`urn:csabs:operation/StreamCipher-decrypt`

**signature:** D : {(k,ν,o,n,c) | k∈K, ν∈N, o,n∈ℕ, o+n≤L, c∈B_n}→B_n

**description:** Apply the same XOR transform to ciphertext with the matching key, nonce and offset; every admissible bit string is accepted without authentication.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** Apply the same XOR transform to ciphertext with the matching key, nonce and offset; every admissible bit string is accepted without authentication.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [Nir and Langley, RFC 8439: ChaCha20 and Poly1305 for IETF Protocols (June 2018)](https://www.rfc-editor.org/rfc/rfc8439.html); accessedOn: 2026-11-20; sourceRole: Consulted primary specification, sections 2.4, 2.4.1 and 4: synchronous keystream XOR encryption/decryption, equal lengths and keystream reuse. Adapted to an abstract bounded bit keystream rather than a ChaCha20 implementation.

**sourceLocator:** Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-StreamCipher-bounded-keystream"></a>

### bounded-keystream

`urn:csabs:axiom/StreamCipher-bounded-keystream`

**statement:** A fixed key/nonce selects a deterministic plaintext-independent keystream on exactly the available positions.

**description:** A fixed key/nonce selects a deterministic plaintext-independent keystream on exactly the available positions.

**formalStatement:** K,N nonempty; L∈ℕ; G:K×N×Fin(L)→{0,1}; B_n={0,1}^{Fin(n)}; admitted (o,n) satisfy o+n≤L.

**assumptions:** Bounded synchronous XOR profile. K and N are nonempty key and nonce carriers with exact equality; L∈ℕ is the available bit capacity per key/nonce stream. B_n={0,1}^{Fin(n)} has extensional equality, including its unique empty value at n=0. G:K×N×Fin(L)→{0,1} is deterministic and independent of plaintext and ciphertext. Offsets o and lengths n are natural numbers satisfying o+n≤L; operations are total on this admissible domain and undefined outside it, with no modular wraparound or padding. Inputs and outputs have the same bit length. The same key, nonce and offset are required for inversion. Nonce allocation and nonoverlapping stream-position use across encryptions are caller obligations, not enforced by the value model. The profile excludes self-synchronizing ciphers and makes no pseudorandomness, confidentiality, authentication or side-channel assertion.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [Nir and Langley, RFC 8439: ChaCha20 and Poly1305 for IETF Protocols (June 2018)](https://www.rfc-editor.org/rfc/rfc8439.html); accessedOn: 2026-11-20; sourceRole: Consulted primary specification, sections 2.4, 2.4.1 and 4: synchronous keystream XOR encryption/decryption, equal lengths and keystream reuse. Adapted to an abstract bounded bit keystream rather than a ChaCha20 implementation.

**sourceLocator:** Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-StreamCipher-xor-transform"></a>

### xor-transform

`urn:csabs:axiom/StreamCipher-xor-transform`

**statement:** Encryption and decryption are the same length-preserving pointwise XOR transform.

**description:** Encryption and decryption are the same length-preserving pointwise XOR transform.

**formalStatement:** For every admissible (k,ν,o,n), E(k,ν,o,m)[i]=m[i]⊕G(k,ν,o+i) and D(k,ν,o,c)[i]=c[i]⊕G(k,ν,o+i), i∈Fin(n).

**assumptions:** Bounded synchronous XOR profile. K and N are nonempty key and nonce carriers with exact equality; L∈ℕ is the available bit capacity per key/nonce stream. B_n={0,1}^{Fin(n)} has extensional equality, including its unique empty value at n=0. G:K×N×Fin(L)→{0,1} is deterministic and independent of plaintext and ciphertext. Offsets o and lengths n are natural numbers satisfying o+n≤L; operations are total on this admissible domain and undefined outside it, with no modular wraparound or padding. Inputs and outputs have the same bit length. The same key, nonce and offset are required for inversion. Nonce allocation and nonoverlapping stream-position use across encryptions are caller obligations, not enforced by the value model. The profile excludes self-synchronizing ciphers and makes no pseudorandomness, confidentiality, authentication or side-channel assertion.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [Nir and Langley, RFC 8439: ChaCha20 and Poly1305 for IETF Protocols (June 2018)](https://www.rfc-editor.org/rfc/rfc8439.html); accessedOn: 2026-11-20; sourceRole: Consulted primary specification, sections 2.4, 2.4.1 and 4: synchronous keystream XOR encryption/decryption, equal lengths and keystream reuse. Adapted to an abstract bounded bit keystream rather than a ChaCha20 implementation.

**sourceLocator:** Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-StreamCipher-roundtrip"></a>

### roundtrip

`urn:csabs:law/StreamCipher-roundtrip`

**statement:** Applying the same segment twice recovers the original message.

**description:** Applying the same segment twice recovers the original message.

**formalStatement:** D(k,ν,o,E(k,ν,o,m))=m and E(k,ν,o,D(k,ν,o,c))=c for every admissible segment.

**assumptions:** Bounded synchronous XOR profile. K and N are nonempty key and nonce carriers with exact equality; L∈ℕ is the available bit capacity per key/nonce stream. B_n={0,1}^{Fin(n)} has extensional equality, including its unique empty value at n=0. G:K×N×Fin(L)→{0,1} is deterministic and independent of plaintext and ciphertext. Offsets o and lengths n are natural numbers satisfying o+n≤L; operations are total on this admissible domain and undefined outside it, with no modular wraparound or padding. Inputs and outputs have the same bit length. The same key, nonce and offset are required for inversion. Nonce allocation and nonoverlapping stream-position use across encryptions are caller obligations, not enforced by the value model. The profile excludes self-synchronizing ciphers and makes no pseudorandomness, confidentiality, authentication or side-channel assertion.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [Nir and Langley, RFC 8439: ChaCha20 and Poly1305 for IETF Protocols (June 2018)](https://www.rfc-editor.org/rfc/rfc8439.html); accessedOn: 2026-11-20; sourceRole: Consulted primary specification, sections 2.4, 2.4.1 and 4: synchronous keystream XOR encryption/decryption, equal lengths and keystream reuse. Adapted to an abstract bounded bit keystream rather than a ChaCha20 implementation.

**sourceLocator:** Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).

**sourceNote:** Derived from the directly linked defining premises; At every index (m[i]⊕s[i])⊕s[i]=m[i]. Function extensionality yields bit-vector equality. Encryption and decryption share the same transform, giving both inverse equations.

**provenanceKind:** derived

**dependsOn:** [bounded-keystream](StreamCipher.md#node-urn-csabs-axiom-StreamCipher-bounded-keystream); [xor-transform](StreamCipher.md#node-urn-csabs-axiom-StreamCipher-xor-transform)

**proofSketch:** At every index (m[i]⊕s[i])⊕s[i]=m[i]. Function extensionality yields bit-vector equality. Encryption and decryption share the same transform, giving both inverse equations.

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {K N : Type} {capacity : Nat} (g : Catalog.StreamCipher K N capacity) (k : K) (nonce : N) (offset n : Nat) (fits : offset + n ≤ capacity) (m : Catalog.CryptoBits n), Catalog.streamCrypt g k nonce offset n fits (Catalog.streamCrypt g k nonce offset n fits m) = m
```

**Source:** [`Catalog.stream_roundtrip`](../lean/Catalog/StreamCipher.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.

**Limits:** Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/StreamCipher-bounded-keystream": "Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.",
  "urn:csabs:axiom/StreamCipher-xor-transform": "Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example."
}
```

<a id="node-urn-csabs-law-StreamCipher-empty-message"></a>

### empty-message

`urn:csabs:law/StreamCipher-empty-message`

**statement:** The admissible empty message encrypts and decrypts to itself.

**description:** The admissible empty message encrypts and decrypts to itself.

**formalStatement:** For 0≤o≤L, E(k,ν,o,ε)=D(k,ν,o,ε)=ε.

**assumptions:** Bounded synchronous XOR profile. K and N are nonempty key and nonce carriers with exact equality; L∈ℕ is the available bit capacity per key/nonce stream. B_n={0,1}^{Fin(n)} has extensional equality, including its unique empty value at n=0. G:K×N×Fin(L)→{0,1} is deterministic and independent of plaintext and ciphertext. Offsets o and lengths n are natural numbers satisfying o+n≤L; operations are total on this admissible domain and undefined outside it, with no modular wraparound or padding. Inputs and outputs have the same bit length. The same key, nonce and offset are required for inversion. Nonce allocation and nonoverlapping stream-position use across encryptions are caller obligations, not enforced by the value model. The profile excludes self-synchronizing ciphers and makes no pseudorandomness, confidentiality, authentication or side-channel assertion.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [Nir and Langley, RFC 8439: ChaCha20 and Poly1305 for IETF Protocols (June 2018)](https://www.rfc-editor.org/rfc/rfc8439.html); accessedOn: 2026-11-20; sourceRole: Consulted primary specification, sections 2.4, 2.4.1 and 4: synchronous keystream XOR encryption/decryption, equal lengths and keystream reuse. Adapted to an abstract bounded bit keystream rather than a ChaCha20 implementation.

**sourceLocator:** Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).

**sourceNote:** Derived from the directly linked defining premises; There is no index in Fin(0); all functions Fin(0)→Bool are extensionally equal, including at offset L.

**provenanceKind:** derived

**dependsOn:** [bounded-keystream](StreamCipher.md#node-urn-csabs-axiom-StreamCipher-bounded-keystream); [xor-transform](StreamCipher.md#node-urn-csabs-axiom-StreamCipher-xor-transform)

**proofSketch:** There is no index in Fin(0); all functions Fin(0)→Bool are extensionally equal, including at offset L.

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {K N : Type} {capacity : Nat} (g : Catalog.StreamCipher K N capacity) (k : K) (nonce : N) (offset : Nat) (fits : offset + 0 ≤ capacity) (m : Catalog.CryptoBits 0), Catalog.streamCrypt g k nonce offset 0 fits m = m
```

**Source:** [`Catalog.stream_empty`](../lean/Catalog/StreamCipher.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.

**Limits:** Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/StreamCipher-bounded-keystream": "Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.",
  "urn:csabs:axiom/StreamCipher-xor-transform": "Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example."
}
```

## Theorems

<a id="node-urn-csabs-theorem-StreamCipher-model-satisfaction"></a>

### model-satisfaction

`urn:csabs:theorem/StreamCipher-model-satisfaction`

**statement:** The bounded Boolean function model realizes the selected keystream and XOR basis, including distinct one-bit outcomes.

**description:** The bounded Boolean function model realizes the selected keystream and XOR basis, including distinct one-bit outcomes.

**formalStatement:** The typed G and streamCrypt satisfy the displayed equation at every admissible index. With K=N=Bool, L=2 and m=[false], the explicit example at nonce=false, o=0 yields [true] for key=true and [false] for key=false.

**assumptions:** Bounded synchronous XOR profile. K and N are nonempty key and nonce carriers with exact equality; L∈ℕ is the available bit capacity per key/nonce stream. B_n={0,1}^{Fin(n)} has extensional equality, including its unique empty value at n=0. G:K×N×Fin(L)→{0,1} is deterministic and independent of plaintext and ciphertext. Offsets o and lengths n are natural numbers satisfying o+n≤L; operations are total on this admissible domain and undefined outside it, with no modular wraparound or padding. Inputs and outputs have the same bit length. The same key, nonce and offset are required for inversion. Nonce allocation and nonoverlapping stream-position use across encryptions are caller obligations, not enforced by the value model. The profile excludes self-synchronizing ciphers and makes no pseudorandomness, confidentiality, authentication or side-channel assertion.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [Nir and Langley, RFC 8439: ChaCha20 and Poly1305 for IETF Protocols (June 2018)](https://www.rfc-editor.org/rfc/rfc8439.html); accessedOn: 2026-11-20; sourceRole: Consulted primary specification, sections 2.4, 2.4.1 and 4: synchronous keystream XOR encryption/decryption, equal lengths and keystream reuse. Adapted to an abstract bounded bit keystream rather than a ChaCha20 implementation.

**sourceLocator:** Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).

**sourceNote:** Derived from the directly linked defining premises; The function types provide the exact carriers and deterministic generator; the fits proof supplies a valid stream address. Unfold streamCrypt for the XOR equation and reduce the explicit Bool example. No target law is an assumed structure field.

**provenanceKind:** derived

**dependsOn:** [bounded-keystream](StreamCipher.md#node-urn-csabs-axiom-StreamCipher-bounded-keystream); [xor-transform](StreamCipher.md#node-urn-csabs-axiom-StreamCipher-xor-transform)

**proofSketch:** The function types provide the exact carriers and deterministic generator; the fits proof supplies a valid stream address. Unfold streamCrypt for the XOR equation and reduce the explicit Bool example. No target law is an assumed structure field.

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
(∀ {K N : Type} {capacity : Nat} (g : Catalog.StreamCipher K N capacity) (k : K) (nonce : N) (offset n : Nat) (fits : offset + n ≤ capacity) (m : Catalog.CryptoBits n) (i : Fin n), Catalog.streamCrypt g k nonce offset n fits m i = xor (m i) (g k nonce ⟨offset + i.val, Nat.lt_of_lt_of_le (Nat.add_lt_add_left i.isLt offset) fits⟩)) ∧ Catalog.streamCrypt Catalog.exampleStreamCipher true false 0 1 (by decide) (fun _ => false) 0 = true ∧ Catalog.streamCrypt Catalog.exampleStreamCipher false false 0 1 (by decide) (fun _ => false) 0 = false
```

**Source:** [`Catalog.stream_model_satisfaction`](../lean/Catalog/StreamCipher.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.

**Limits:** Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/StreamCipher-bounded-keystream": "Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.",
  "urn:csabs:axiom/StreamCipher-xor-transform": "Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example."
}
```

<a id="node-urn-csabs-theorem-StreamCipher-keystream-reuse-leakage"></a>

### keystream-reuse-leakage

`urn:csabs:theorem/StreamCipher-keystream-reuse-leakage`

**statement:** Two messages encrypted with the same key, nonce and offset expose their bitwise XOR.

**description:** Two messages encrypted with the same key, nonce and offset expose their bitwise XOR.

**formalStatement:** E(k,ν,o,a)⊕E(k,ν,o,b)=a⊕b for equally long admissible a,b.

**assumptions:** Bounded synchronous XOR profile. K and N are nonempty key and nonce carriers with exact equality; L∈ℕ is the available bit capacity per key/nonce stream. B_n={0,1}^{Fin(n)} has extensional equality, including its unique empty value at n=0. G:K×N×Fin(L)→{0,1} is deterministic and independent of plaintext and ciphertext. Offsets o and lengths n are natural numbers satisfying o+n≤L; operations are total on this admissible domain and undefined outside it, with no modular wraparound or padding. Inputs and outputs have the same bit length. The same key, nonce and offset are required for inversion. Nonce allocation and nonoverlapping stream-position use across encryptions are caller obligations, not enforced by the value model. The profile excludes self-synchronizing ciphers and makes no pseudorandomness, confidentiality, authentication or side-channel assertion.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [Nir and Langley, RFC 8439: ChaCha20 and Poly1305 for IETF Protocols (June 2018)](https://www.rfc-editor.org/rfc/rfc8439.html); accessedOn: 2026-11-20; sourceRole: Consulted primary specification, sections 2.4, 2.4.1 and 4: synchronous keystream XOR encryption/decryption, equal lengths and keystream reuse. Adapted to an abstract bounded bit keystream rather than a ChaCha20 implementation.

**sourceLocator:** Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).

**sourceNote:** Derived from the directly linked defining premises; At each position the repeated keystream bit cancels: (a⊕s)⊕(b⊕s)=a⊕b. This proves the exact leakage identity for overlapping identical segments, independently of generator security.

**provenanceKind:** derived

**dependsOn:** [bounded-keystream](StreamCipher.md#node-urn-csabs-axiom-StreamCipher-bounded-keystream); [xor-transform](StreamCipher.md#node-urn-csabs-axiom-StreamCipher-xor-transform)

**proofSketch:** At each position the repeated keystream bit cancels: (a⊕s)⊕(b⊕s)=a⊕b. This proves the exact leakage identity for overlapping identical segments, independently of generator security.

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {K N : Type} {capacity : Nat} (g : Catalog.StreamCipher K N capacity) (k : K) (nonce : N) (offset n : Nat) (fits : offset + n ≤ capacity) (a b : Catalog.CryptoBits n), Catalog.streamXor (Catalog.streamCrypt g k nonce offset n fits a) (Catalog.streamCrypt g k nonce offset n fits b) = Catalog.streamXor a b
```

**Source:** [`Catalog.stream_reused_keystream`](../lean/Catalog/StreamCipher.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.

**Limits:** Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/StreamCipher-bounded-keystream": "Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.",
  "urn:csabs:axiom/StreamCipher-xor-transform": "Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example."
}
```

<a id="node-urn-csabs-theorem-StreamCipher-malleability"></a>

### malleability

`urn:csabs:theorem/StreamCipher-malleability`

**statement:** XOR changes to ciphertext cause the same XOR changes in the decrypted plaintext.

**description:** XOR changes to ciphertext cause the same XOR changes in the decrypted plaintext.

**formalStatement:** D(k,ν,o,E(k,ν,o,m)⊕Δ)=m⊕Δ for Δ∈B_n and admissible (o,n).

**assumptions:** Bounded synchronous XOR profile. K and N are nonempty key and nonce carriers with exact equality; L∈ℕ is the available bit capacity per key/nonce stream. B_n={0,1}^{Fin(n)} has extensional equality, including its unique empty value at n=0. G:K×N×Fin(L)→{0,1} is deterministic and independent of plaintext and ciphertext. Offsets o and lengths n are natural numbers satisfying o+n≤L; operations are total on this admissible domain and undefined outside it, with no modular wraparound or padding. Inputs and outputs have the same bit length. The same key, nonce and offset are required for inversion. Nonce allocation and nonoverlapping stream-position use across encryptions are caller obligations, not enforced by the value model. The profile excludes self-synchronizing ciphers and makes no pseudorandomness, confidentiality, authentication or side-channel assertion.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [Nir and Langley, RFC 8439: ChaCha20 and Poly1305 for IETF Protocols (June 2018)](https://www.rfc-editor.org/rfc/rfc8439.html); accessedOn: 2026-11-20; sourceRole: Consulted primary specification, sections 2.4, 2.4.1 and 4: synchronous keystream XOR encryption/decryption, equal lengths and keystream reuse. Adapted to an abstract bounded bit keystream rather than a ChaCha20 implementation.

**sourceLocator:** Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).

**sourceNote:** Derived from the directly linked defining premises; Cancel the two identical keystream bits at every position: (m⊕s⊕Δ)⊕s=m⊕Δ. Authentication requires an additional construction; no probabilistic security statement is inferred.

**provenanceKind:** derived

**dependsOn:** [bounded-keystream](StreamCipher.md#node-urn-csabs-axiom-StreamCipher-bounded-keystream); [xor-transform](StreamCipher.md#node-urn-csabs-axiom-StreamCipher-xor-transform)

**proofSketch:** Cancel the two identical keystream bits at every position: (m⊕s⊕Δ)⊕s=m⊕Δ. Authentication requires an additional construction; no probabilistic security statement is inferred.

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {K N : Type} {capacity : Nat} (g : Catalog.StreamCipher K N capacity) (k : K) (nonce : N) (offset n : Nat) (fits : offset + n ≤ capacity) (m delta : Catalog.CryptoBits n), Catalog.streamCrypt g k nonce offset n fits (Catalog.streamXor (Catalog.streamCrypt g k nonce offset n fits m) delta) = Catalog.streamXor m delta
```

**Source:** [`Catalog.stream_malleability`](../lean/Catalog/StreamCipher.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.

**Limits:** Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/StreamCipher-bounded-keystream": "Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.",
  "urn:csabs:axiom/StreamCipher-xor-transform": "Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example."
}
```

## Concept provenance

- [Nir and Langley, RFC 8439: ChaCha20 and Poly1305 for IETF Protocols (June 2018)](https://www.rfc-editor.org/rfc/rfc8439.html); accessedOn: 2026-11-20; sourceRole: Consulted primary specification, sections 2.4, 2.4.1 and 4: synchronous keystream XOR encryption/decryption, equal lengths and keystream reuse. Adapted to an abstract bounded bit keystream rather than a ChaCha20 implementation.

**sourceLocator:** Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/StreamCipher",
    "type": "Concept",
    "shortForm": "StreamCipher",
    "fullName": "Synchronous stream cipher (bounded XOR-keystream profile)",
    "definition": "A deterministic key- and nonce-indexed bit keystream combined with a finite plaintext by pointwise XOR; decryption uses the same keystream segment.",
    "notation": "G:K×N×Fin(L)→Bool; E(k,ν,o,m)[i]=m[i]⊕G(k,ν,o+i); D=E.",
    "category": [
      "urn:csabs:category/symmetric-cryptography"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "synonyms": [
      "Synchronous XOR stream cipher",
      "Nonce-indexed keystream cipher"
    ],
    "axiomBasis": "Deterministic plaintext-independent bounded keystream; exact bit-vector carrier and domain; pointwise XOR encryption and decryption using the same segment.",
    "basisKind": "defined-structure",
    "basisScope": "Bounded synchronous XOR profile. K and N are nonempty key and nonce carriers with exact equality; L∈ℕ is the available bit capacity per key/nonce stream. B_n={0,1}^{Fin(n)} has extensional equality, including its unique empty value at n=0. G:K×N×Fin(L)→{0,1} is deterministic and independent of plaintext and ciphertext. Offsets o and lengths n are natural numbers satisfying o+n≤L; operations are total on this admissible domain and undefined outside it, with no modular wraparound or padding. Inputs and outputs have the same bit length. The same key, nonce and offset are required for inversion. Nonce allocation and nonoverlapping stream-position use across encryptions are caller obligations, not enforced by the value model. The profile excludes self-synchronizing ciphers and makes no pseudorandomness, confidentiality, authentication or side-channel assertion.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical interface review; only individually registered witnesses have compiler evidence.",
    "verificationObligation": [
      "Map key/nonce encoding, bit order, initial counters, capacity and offset units to the concrete algorithm. Reject exhaustion rather than wrapping counters.",
      "Keep encryption stream positions disjoint for a fixed key/nonce across messages; nonce uniqueness across writers and restarts is a typical stronger protocol rule. Unique nonces alone do not establish security for arbitrary G.",
      "The concrete demonstration generator is deliberately insecure. Functional inversion is independent of pseudorandomness; this cipher alone supplies no tag, integrity, replay protection or wrong-key rejection."
    ],
    "mathematicalFormulation": "G:K×N×Fin(L)→Bool; E(k,ν,o,m)[i]=m[i]⊕G(k,ν,o+i); D=E. Bounded synchronous XOR profile. K and N are nonempty key and nonce carriers with exact equality; L∈ℕ is the available bit capacity per key/nonce stream. B_n={0,1}^{Fin(n)} has extensional equality, including its unique empty value at n=0. G:K×N×Fin(L)→{0,1} is deterministic and independent of plaintext and ciphertext. Offsets o and lengths n are natural numbers satisfying o+n≤L; operations are total on this admissible domain and undefined outside it, with no modular wraparound or padding. Inputs and outputs have the same bit length. The same key, nonce and offset are required for inversion. Nonce allocation and nonoverlapping stream-position use across encryptions are caller obligations, not enforced by the value model. The profile excludes self-synchronizing ciphers and makes no pseudorandomness, confidentiality, authentication or side-channel assertion.",
    "hasOperation": [
      "urn:csabs:operation/StreamCipher-keystream",
      "urn:csabs:operation/StreamCipher-xor",
      "urn:csabs:operation/StreamCipher-encrypt",
      "urn:csabs:operation/StreamCipher-decrypt"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/StreamCipher-bounded-keystream",
      "urn:csabs:axiom/StreamCipher-xor-transform"
    ],
    "hasLaw": [
      "urn:csabs:law/StreamCipher-roundtrip",
      "urn:csabs:law/StreamCipher-empty-message"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/StreamCipher-model-satisfaction",
      "urn:csabs:theorem/StreamCipher-keystream-reuse-leakage",
      "urn:csabs:theorem/StreamCipher-malleability"
    ],
    "source": [
      "urn:csabs:source/rfc8439"
    ],
    "sourceLocator": "Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted",
    "requiresConcept": [
      "urn:csabs:concept/BitVector"
    ],
    "relatedConcept": [
      "urn:csabs:concept/BlockCipher",
      "urn:csabs:concept/AEAD",
      "urn:csabs:concept/GCM"
    ],
    "leanFormulation": "abbrev StreamCipher (K N : Type) (capacity : Nat) := K → N → Fin capacity → Bool",
    "formulationSource": "urn:csabs:source/local-lean-StreamCipher",
    "formulationLocator": "Catalog.StreamCipher",
    "formulationScope": "model",
    "leanModelMapping": "For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.",
    "leanModelLimitations": "Random-access denotation of a bounded synchronous generator, not an implementation of ChaCha20 or a general self-synchronizing cipher. No nonce history, state allocation, block serialization, key sampling or security game. The example generator is intentionally insecure. Nonempty K,N are an instantiation requirement; the generic Lean type does not carry Nonempty fields."
  },
  {
    "id": "urn:csabs:operation/StreamCipher-keystream",
    "type": "Operation",
    "name": "keystream",
    "signature": "G : K×N×Fin(L)→Bool",
    "description": "Return the deterministic keystream bit at the specified position, independently of message data.",
    "concept": "urn:csabs:concept/StreamCipher",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "Return the deterministic keystream bit at the specified position, independently of message data.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/rfc8439"
    ],
    "sourceLocator": "Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/StreamCipher-xor",
    "type": "Operation",
    "name": "xor",
    "signature": "xor_n : B_n×B_n→B_n",
    "description": "Combine equal-length bit vectors pointwise with Boolean XOR.",
    "concept": "urn:csabs:concept/StreamCipher",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "Combine equal-length bit vectors pointwise with Boolean XOR.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/rfc8439"
    ],
    "sourceLocator": "Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/StreamCipher-encrypt",
    "type": "Operation",
    "name": "encrypt",
    "signature": "E : {(k,ν,o,n,m) | k∈K, ν∈N, o,n∈ℕ, o+n≤L, m∈B_n}→B_n",
    "description": "XOR each plaintext bit with the corresponding bit at stream offset o; return exactly n ciphertext bits.",
    "concept": "urn:csabs:concept/StreamCipher",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "XOR each plaintext bit with the corresponding bit at stream offset o; return exactly n ciphertext bits.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/rfc8439"
    ],
    "sourceLocator": "Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/StreamCipher-decrypt",
    "type": "Operation",
    "name": "decrypt",
    "signature": "D : {(k,ν,o,n,c) | k∈K, ν∈N, o,n∈ℕ, o+n≤L, c∈B_n}→B_n",
    "description": "Apply the same XOR transform to ciphertext with the matching key, nonce and offset; every admissible bit string is accepted without authentication.",
    "concept": "urn:csabs:concept/StreamCipher",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "Apply the same XOR transform to ciphertext with the matching key, nonce and offset; every admissible bit string is accepted without authentication.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/rfc8439"
    ],
    "sourceLocator": "Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/StreamCipher-bounded-keystream",
    "type": "Axiom",
    "name": "bounded-keystream",
    "statement": "A fixed key/nonce selects a deterministic plaintext-independent keystream on exactly the available positions.",
    "description": "A fixed key/nonce selects a deterministic plaintext-independent keystream on exactly the available positions.",
    "formalStatement": "K,N nonempty; L∈ℕ; G:K×N×Fin(L)→{0,1}; B_n={0,1}^{Fin(n)}; admitted (o,n) satisfy o+n≤L.",
    "assumptions": [
      "Bounded synchronous XOR profile. K and N are nonempty key and nonce carriers with exact equality; L∈ℕ is the available bit capacity per key/nonce stream. B_n={0,1}^{Fin(n)} has extensional equality, including its unique empty value at n=0. G:K×N×Fin(L)→{0,1} is deterministic and independent of plaintext and ciphertext. Offsets o and lengths n are natural numbers satisfying o+n≤L; operations are total on this admissible domain and undefined outside it, with no modular wraparound or padding. Inputs and outputs have the same bit length. The same key, nonce and offset are required for inversion. Nonce allocation and nonoverlapping stream-position use across encryptions are caller obligations, not enforced by the value model. The profile excludes self-synchronizing ciphers and makes no pseudorandomness, confidentiality, authentication or side-channel assertion."
    ],
    "appliesTo": [
      "urn:csabs:concept/StreamCipher"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/rfc8439"
    ],
    "sourceLocator": "Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/StreamCipher-xor-transform",
    "type": "Axiom",
    "name": "xor-transform",
    "statement": "Encryption and decryption are the same length-preserving pointwise XOR transform.",
    "description": "Encryption and decryption are the same length-preserving pointwise XOR transform.",
    "formalStatement": "For every admissible (k,ν,o,n), E(k,ν,o,m)[i]=m[i]⊕G(k,ν,o+i) and D(k,ν,o,c)[i]=c[i]⊕G(k,ν,o+i), i∈Fin(n).",
    "assumptions": [
      "Bounded synchronous XOR profile. K and N are nonempty key and nonce carriers with exact equality; L∈ℕ is the available bit capacity per key/nonce stream. B_n={0,1}^{Fin(n)} has extensional equality, including its unique empty value at n=0. G:K×N×Fin(L)→{0,1} is deterministic and independent of plaintext and ciphertext. Offsets o and lengths n are natural numbers satisfying o+n≤L; operations are total on this admissible domain and undefined outside it, with no modular wraparound or padding. Inputs and outputs have the same bit length. The same key, nonce and offset are required for inversion. Nonce allocation and nonoverlapping stream-position use across encryptions are caller obligations, not enforced by the value model. The profile excludes self-synchronizing ciphers and makes no pseudorandomness, confidentiality, authentication or side-channel assertion."
    ],
    "appliesTo": [
      "urn:csabs:concept/StreamCipher"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/rfc8439"
    ],
    "sourceLocator": "Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/StreamCipher-roundtrip",
    "type": "Law",
    "name": "roundtrip",
    "statement": "Applying the same segment twice recovers the original message.",
    "description": "Applying the same segment twice recovers the original message.",
    "formalStatement": "D(k,ν,o,E(k,ν,o,m))=m and E(k,ν,o,D(k,ν,o,c))=c for every admissible segment.",
    "assumptions": [
      "Bounded synchronous XOR profile. K and N are nonempty key and nonce carriers with exact equality; L∈ℕ is the available bit capacity per key/nonce stream. B_n={0,1}^{Fin(n)} has extensional equality, including its unique empty value at n=0. G:K×N×Fin(L)→{0,1} is deterministic and independent of plaintext and ciphertext. Offsets o and lengths n are natural numbers satisfying o+n≤L; operations are total on this admissible domain and undefined outside it, with no modular wraparound or padding. Inputs and outputs have the same bit length. The same key, nonce and offset are required for inversion. Nonce allocation and nonoverlapping stream-position use across encryptions are caller obligations, not enforced by the value model. The profile excludes self-synchronizing ciphers and makes no pseudorandomness, confidentiality, authentication or side-channel assertion."
    ],
    "appliesTo": [
      "urn:csabs:concept/StreamCipher"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/rfc8439"
    ],
    "sourceLocator": "Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).",
    "sourceNote": "Derived from the directly linked defining premises; At every index (m[i]⊕s[i])⊕s[i]=m[i]. Function extensionality yields bit-vector equality. Encryption and decryption share the same transform, giving both inverse equations.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/StreamCipher-bounded-keystream",
      "urn:csabs:axiom/StreamCipher-xor-transform"
    ],
    "proofSketch": "At every index (m[i]⊕s[i])⊕s[i]=m[i]. Function extensionality yields bit-vector equality. Encryption and decryption share the same transform, giving both inverse equations.",
    "leanFormulation": "∀ {K N : Type} {capacity : Nat} (g : Catalog.StreamCipher K N capacity) (k : K) (nonce : N) (offset n : Nat) (fits : offset + n ≤ capacity) (m : Catalog.CryptoBits n), Catalog.streamCrypt g k nonce offset n fits (Catalog.streamCrypt g k nonce offset n fits m) = m",
    "formulationSource": "urn:csabs:source/local-lean-StreamCipher",
    "formulationLocator": "Catalog.stream_roundtrip",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.",
    "leanModelLimitations": "Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/StreamCipher-bounded-keystream\": \"Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.\", \"urn:csabs:axiom/StreamCipher-xor-transform\": \"Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.\"}"
  },
  {
    "id": "urn:csabs:law/StreamCipher-empty-message",
    "type": "Law",
    "name": "empty-message",
    "statement": "The admissible empty message encrypts and decrypts to itself.",
    "description": "The admissible empty message encrypts and decrypts to itself.",
    "formalStatement": "For 0≤o≤L, E(k,ν,o,ε)=D(k,ν,o,ε)=ε.",
    "assumptions": [
      "Bounded synchronous XOR profile. K and N are nonempty key and nonce carriers with exact equality; L∈ℕ is the available bit capacity per key/nonce stream. B_n={0,1}^{Fin(n)} has extensional equality, including its unique empty value at n=0. G:K×N×Fin(L)→{0,1} is deterministic and independent of plaintext and ciphertext. Offsets o and lengths n are natural numbers satisfying o+n≤L; operations are total on this admissible domain and undefined outside it, with no modular wraparound or padding. Inputs and outputs have the same bit length. The same key, nonce and offset are required for inversion. Nonce allocation and nonoverlapping stream-position use across encryptions are caller obligations, not enforced by the value model. The profile excludes self-synchronizing ciphers and makes no pseudorandomness, confidentiality, authentication or side-channel assertion."
    ],
    "appliesTo": [
      "urn:csabs:concept/StreamCipher"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/rfc8439"
    ],
    "sourceLocator": "Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).",
    "sourceNote": "Derived from the directly linked defining premises; There is no index in Fin(0); all functions Fin(0)→Bool are extensionally equal, including at offset L.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/StreamCipher-bounded-keystream",
      "urn:csabs:axiom/StreamCipher-xor-transform"
    ],
    "proofSketch": "There is no index in Fin(0); all functions Fin(0)→Bool are extensionally equal, including at offset L.",
    "leanFormulation": "∀ {K N : Type} {capacity : Nat} (g : Catalog.StreamCipher K N capacity) (k : K) (nonce : N) (offset : Nat) (fits : offset + 0 ≤ capacity) (m : Catalog.CryptoBits 0), Catalog.streamCrypt g k nonce offset 0 fits m = m",
    "formulationSource": "urn:csabs:source/local-lean-StreamCipher",
    "formulationLocator": "Catalog.stream_empty",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.",
    "leanModelLimitations": "Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/StreamCipher-bounded-keystream\": \"Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.\", \"urn:csabs:axiom/StreamCipher-xor-transform\": \"Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.\"}"
  },
  {
    "id": "urn:csabs:theorem/StreamCipher-model-satisfaction",
    "type": "Theorem",
    "name": "model-satisfaction",
    "statement": "The bounded Boolean function model realizes the selected keystream and XOR basis, including distinct one-bit outcomes.",
    "description": "The bounded Boolean function model realizes the selected keystream and XOR basis, including distinct one-bit outcomes.",
    "formalStatement": "The typed G and streamCrypt satisfy the displayed equation at every admissible index. With K=N=Bool, L=2 and m=[false], the explicit example at nonce=false, o=0 yields [true] for key=true and [false] for key=false.",
    "assumptions": [
      "Bounded synchronous XOR profile. K and N are nonempty key and nonce carriers with exact equality; L∈ℕ is the available bit capacity per key/nonce stream. B_n={0,1}^{Fin(n)} has extensional equality, including its unique empty value at n=0. G:K×N×Fin(L)→{0,1} is deterministic and independent of plaintext and ciphertext. Offsets o and lengths n are natural numbers satisfying o+n≤L; operations are total on this admissible domain and undefined outside it, with no modular wraparound or padding. Inputs and outputs have the same bit length. The same key, nonce and offset are required for inversion. Nonce allocation and nonoverlapping stream-position use across encryptions are caller obligations, not enforced by the value model. The profile excludes self-synchronizing ciphers and makes no pseudorandomness, confidentiality, authentication or side-channel assertion."
    ],
    "appliesTo": [
      "urn:csabs:concept/StreamCipher"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/rfc8439"
    ],
    "sourceLocator": "Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).",
    "sourceNote": "Derived from the directly linked defining premises; The function types provide the exact carriers and deterministic generator; the fits proof supplies a valid stream address. Unfold streamCrypt for the XOR equation and reduce the explicit Bool example. No target law is an assumed structure field.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/StreamCipher-bounded-keystream",
      "urn:csabs:axiom/StreamCipher-xor-transform"
    ],
    "proofSketch": "The function types provide the exact carriers and deterministic generator; the fits proof supplies a valid stream address. Unfold streamCrypt for the XOR equation and reduce the explicit Bool example. No target law is an assumed structure field.",
    "leanFormulation": "(∀ {K N : Type} {capacity : Nat} (g : Catalog.StreamCipher K N capacity) (k : K) (nonce : N) (offset n : Nat) (fits : offset + n ≤ capacity) (m : Catalog.CryptoBits n) (i : Fin n), Catalog.streamCrypt g k nonce offset n fits m i = xor (m i) (g k nonce ⟨offset + i.val, Nat.lt_of_lt_of_le (Nat.add_lt_add_left i.isLt offset) fits⟩)) ∧ Catalog.streamCrypt Catalog.exampleStreamCipher true false 0 1 (by decide) (fun _ => false) 0 = true ∧ Catalog.streamCrypt Catalog.exampleStreamCipher false false 0 1 (by decide) (fun _ => false) 0 = false",
    "formulationSource": "urn:csabs:source/local-lean-StreamCipher",
    "formulationLocator": "Catalog.stream_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.",
    "leanModelLimitations": "Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/StreamCipher-bounded-keystream\": \"Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.\", \"urn:csabs:axiom/StreamCipher-xor-transform\": \"Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.\"}"
  },
  {
    "id": "urn:csabs:theorem/StreamCipher-keystream-reuse-leakage",
    "type": "Theorem",
    "name": "keystream-reuse-leakage",
    "statement": "Two messages encrypted with the same key, nonce and offset expose their bitwise XOR.",
    "description": "Two messages encrypted with the same key, nonce and offset expose their bitwise XOR.",
    "formalStatement": "E(k,ν,o,a)⊕E(k,ν,o,b)=a⊕b for equally long admissible a,b.",
    "assumptions": [
      "Bounded synchronous XOR profile. K and N are nonempty key and nonce carriers with exact equality; L∈ℕ is the available bit capacity per key/nonce stream. B_n={0,1}^{Fin(n)} has extensional equality, including its unique empty value at n=0. G:K×N×Fin(L)→{0,1} is deterministic and independent of plaintext and ciphertext. Offsets o and lengths n are natural numbers satisfying o+n≤L; operations are total on this admissible domain and undefined outside it, with no modular wraparound or padding. Inputs and outputs have the same bit length. The same key, nonce and offset are required for inversion. Nonce allocation and nonoverlapping stream-position use across encryptions are caller obligations, not enforced by the value model. The profile excludes self-synchronizing ciphers and makes no pseudorandomness, confidentiality, authentication or side-channel assertion."
    ],
    "appliesTo": [
      "urn:csabs:concept/StreamCipher"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/rfc8439"
    ],
    "sourceLocator": "Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).",
    "sourceNote": "Derived from the directly linked defining premises; At each position the repeated keystream bit cancels: (a⊕s)⊕(b⊕s)=a⊕b. This proves the exact leakage identity for overlapping identical segments, independently of generator security.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/StreamCipher-bounded-keystream",
      "urn:csabs:axiom/StreamCipher-xor-transform"
    ],
    "proofSketch": "At each position the repeated keystream bit cancels: (a⊕s)⊕(b⊕s)=a⊕b. This proves the exact leakage identity for overlapping identical segments, independently of generator security.",
    "leanFormulation": "∀ {K N : Type} {capacity : Nat} (g : Catalog.StreamCipher K N capacity) (k : K) (nonce : N) (offset n : Nat) (fits : offset + n ≤ capacity) (a b : Catalog.CryptoBits n), Catalog.streamXor (Catalog.streamCrypt g k nonce offset n fits a) (Catalog.streamCrypt g k nonce offset n fits b) = Catalog.streamXor a b",
    "formulationSource": "urn:csabs:source/local-lean-StreamCipher",
    "formulationLocator": "Catalog.stream_reused_keystream",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.",
    "leanModelLimitations": "Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/StreamCipher-bounded-keystream\": \"Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.\", \"urn:csabs:axiom/StreamCipher-xor-transform\": \"Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.\"}"
  },
  {
    "id": "urn:csabs:theorem/StreamCipher-malleability",
    "type": "Theorem",
    "name": "malleability",
    "statement": "XOR changes to ciphertext cause the same XOR changes in the decrypted plaintext.",
    "description": "XOR changes to ciphertext cause the same XOR changes in the decrypted plaintext.",
    "formalStatement": "D(k,ν,o,E(k,ν,o,m)⊕Δ)=m⊕Δ for Δ∈B_n and admissible (o,n).",
    "assumptions": [
      "Bounded synchronous XOR profile. K and N are nonempty key and nonce carriers with exact equality; L∈ℕ is the available bit capacity per key/nonce stream. B_n={0,1}^{Fin(n)} has extensional equality, including its unique empty value at n=0. G:K×N×Fin(L)→{0,1} is deterministic and independent of plaintext and ciphertext. Offsets o and lengths n are natural numbers satisfying o+n≤L; operations are total on this admissible domain and undefined outside it, with no modular wraparound or padding. Inputs and outputs have the same bit length. The same key, nonce and offset are required for inversion. Nonce allocation and nonoverlapping stream-position use across encryptions are caller obligations, not enforced by the value model. The profile excludes self-synchronizing ciphers and makes no pseudorandomness, confidentiality, authentication or side-channel assertion."
    ],
    "appliesTo": [
      "urn:csabs:concept/StreamCipher"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/rfc8439"
    ],
    "sourceLocator": "Sections 2.4 and 2.4.1 (encryption, decryption, output lengths); section 4 (keystream reuse).",
    "sourceNote": "Derived from the directly linked defining premises; Cancel the two identical keystream bits at every position: (m⊕s⊕Δ)⊕s=m⊕Δ. Authentication requires an additional construction; no probabilistic security statement is inferred.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/StreamCipher-bounded-keystream",
      "urn:csabs:axiom/StreamCipher-xor-transform"
    ],
    "proofSketch": "Cancel the two identical keystream bits at every position: (m⊕s⊕Δ)⊕s=m⊕Δ. Authentication requires an additional construction; no probabilistic security statement is inferred.",
    "leanFormulation": "∀ {K N : Type} {capacity : Nat} (g : Catalog.StreamCipher K N capacity) (k : K) (nonce : N) (offset n : Nat) (fits : offset + n ≤ capacity) (m delta : Catalog.CryptoBits n), Catalog.streamCrypt g k nonce offset n fits (Catalog.streamXor (Catalog.streamCrypt g k nonce offset n fits m) delta) = Catalog.streamXor m delta",
    "formulationSource": "urn:csabs:source/local-lean-StreamCipher",
    "formulationLocator": "Catalog.stream_malleability",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.",
    "leanModelLimitations": "Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/StreamCipher-bounded-keystream\": \"Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.\", \"urn:csabs:axiom/StreamCipher-xor-transform\": \"Direct defining premise interpreted using For K,N : Type and capacity : Nat, StreamCipher K N capacity is K→N→Fin capacity→Bool. CryptoBits n is Fin n→Bool. streamCrypt uses an explicit fits : offset+n≤capacity proof, and implements both E and D. Use inhabited K,N when instantiating the catalog; Bool keys/nonces with capacity 2 supply a concrete nonvacuous example.\"}"
  }
]
```
<!-- graph-record:end -->
