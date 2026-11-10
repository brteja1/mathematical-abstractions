# Cryptographic abstractions

The initial cryptography subject covers symmetric encryption through AES-GCM:

| Record | Mathematical role |
| --- | --- |
| [BlockCipher](../concepts/BlockCipher.md) | Keyed permutations and their inverses |
| [AES](../concepts/AES.md) | FIPS 197 permutations, specializing BlockCipher |
| [AEAD](../concepts/AEAD.md) | Deterministic nonce-based authenticated-encryption interface |
| [GHASH](../concepts/GHASH.md) | Binary-field polynomial accumulator used by GCM |
| [GCM](../concepts/GCM.md) | AEAD construction from a 128-bit block cipher and GHASH |
| [AESGCM](../concepts/AESGCM.md) | GCM specialized to AES; detached and combined tag encodings |

AES is a prerequisite component of AES-GCM, not its specialization parent.
GHASH uses the existing FiniteField abstraction with an explicit polynomial and
bit encoding; a hash function is not itself a specialization of a field. No
concept-link inference transfers axioms.

## Selected profile

GCM and AES-GCM here use byte strings, exactly 12-byte nonces and 16-byte tags.
AES key lengths are 16, 24 or 32 bytes; every AES block is 16 bytes. The selected
NIST plaintext ceiling is **2^36 − 32 bytes**, and the AAD ceiling is
**2^61 − 1 bytes**. Empty plaintext and empty AAD are valid. Combined output is
`ciphertext || tag`, so an empty message still has a 16-byte combined output.
Other GCM IV/tag lengths need explicit variants rather than implicit widening
of these domains.

[NIST SP 800-38D](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf)
§5.2.1.1 limits plaintext to 2^39 − 256 bits.
[RFC 5116](https://www.rfc-editor.org/rfc/rfc5116.html) §5.1 instead lists
P_MAX as 2^36 − 31 octets. These records deliberately use the stricter NIST
ceiling. RFC 5116 names the AES-128 and AES-256 GCM instances; the AES-192
instance here comes from the NIST construction and has no asserted RFC 5116
algorithm identifier. The source editions are recorded explicitly; this is
not a claim of certification or coverage of later revisions.

## Correctness and security

The records give defining equations, round-trip derivations and a nonce-reuse
XOR consequence. Sources and precise locators are attached directly to each
new concept and claim, using FIPS 197-upd1, SP 800-38D and RFC 5116.

Permutation invertibility and AEAD round trips do not imply confidentiality
or unforgeability. Secure-use analysis also needs an adversary model, key
generation, nonce uniqueness across all writers and restarts, total-data and
invocation budgets, and limits on failed verifications. A tag collision can
allow changed input to pass: there is no universal theorem that every
modification is rejected. A successful decryption does not prevent replay.
Tentative plaintext must not be returned on authentication failure.

GHASH multiplication uses the leftmost bit as the constant polynomial
coefficient; integer length encodings and counter words use big-endian order.
The records preserve this distinction. GHASH has a nonempty whole-block input
domain; GCM performs its own padding and appends a length block even when
plaintext and AAD are both empty. GHASH alone is not a standalone MAC.

## Lean scope

[`Catalog/Cryptography.lean`](../lean/Catalog/Cryptography.lean) and
[`bindings.json`](../lean/bindings.json) provide one binding for each entry.
BlockCipher has a permutation model; the other five bindings are explicitly
partial. AES rounds, NIST field multiplication, GCM counter/tag equations,
wire encodings and security bounds are not compiled formalizations. AEAD
correctness is a structure hypothesis. There are no new registered proof
witnesses, admitted target results or global cryptographic axioms.
