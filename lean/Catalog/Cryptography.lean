module

public import Mathlib.Logic.Equiv.Defs

@[expose] public section

namespace Catalog

/-- Exact bit strings, with position order supplied by each interpretation. -/
abbrev CryptoBits (n : Nat) := Fin n → Bool

/-- Functional permutation model only; contains no pseudorandomness claim. -/
abbrev BlockCipher (K : Type) (n : Nat) := K → (CryptoBits n ≃ CryptoBits n)

/-- Partial AES interface: selects key/block carriers but does not encode the
FIPS round transformations, key expansion or a particular permutation. -/
structure AESInterface where
  keyBits : Nat
  supported : keyBits = 128 ∨ keyBits = 192 ∨ keyBits = 256
  cipher : BlockCipher (CryptoBits keyBits) 128

/-- Deterministic nonce interface with correctness as a structure hypothesis.
Admissible lengths, byte encoding and computational security are not modeled. -/
structure AEADInterface (K N A P W : Type) where
  encrypt : K → N → A → P → W
  decrypt : K → N → A → W → Option P
  correct : ∀ k n a p, decrypt k n a (encrypt k n a p) = some p

/-- Partial GHASH interface; multiplication is a parameter, not a verified
instance of the NIST binary field. Empty input lists are excluded. -/
structure GHASHInterface where
  subkey : CryptoBits 128
  multiply : CryptoBits 128 → CryptoBits 128 → CryptoBits 128

def GHASHInterface.accumulate (h : GHASHInterface)
    (head : CryptoBits 128) (tail : List (CryptoBits 128)) : CryptoBits 128 :=
  (head :: tail).foldl
    (fun acc x => h.multiply (fun i => xor (acc i) (x i)) h.subkey)
    (fun _ => false)

/-- Partial GCM component carrier only. There are no counter, tag, length,
nonce-allocation or authenticated-decryption equations in this Lean model. -/
structure GCMInterface (K : Type) where
  cipher : BlockCipher K 128

/-- Partial composition carrier; the AES and GCM operations are not compiled
from the normative algorithms and there is no registered security witness. -/
structure AESGCMInterface where
  aes : AESInterface

end Catalog
