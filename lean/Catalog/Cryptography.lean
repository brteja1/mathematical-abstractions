module

public import Mathlib.Logic.Equiv.Defs
public import Mathlib.Algebra.Group.Defs

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

/-- Partial DH carrier/action interface. Prime order, generation, validation,
random sampling and protocol authentication remain correspondence obligations. -/
structure DiffieHellmanInterface (H : Type) [Group H] where
  generator : H
  subgroupOrder : Nat

def DiffieHellmanInterface.publicValue {H : Type} [Group H]
    (params : DiffieHellmanInterface H) (secret : Nat) : H :=
  params.generator ^ secret

/-- Exact exponent maps only. This interface does not enforce RSA prime,
exponent or representative-range conditions and carries no inverse theorem. -/
structure RSAInterface where
  modulus : Nat
  publicExponent : Nat
  privateExponent : Nat

def RSAInterface.publicMap (params : RSAInterface) (message : Nat) : Nat :=
  message ^ params.publicExponent % params.modulus

def RSAInterface.privateMap (params : RSAInterface) (ciphertext : Nat) : Nat :=
  ciphertext ^ params.privateExponent % params.modulus

/-- Partial abstract point-group interpretation: affine coordinates, field
characteristic, nonsingularity and base-point order are not encoded here. -/
structure ECCInterface (Point : Type) [AddCommGroup Point] where
  basePoint : Point
  subgroupOrder : Nat

def ECCInterface.publicPoint {Point : Type} [AddCommGroup Point]
    (params : ECCInterface Point) (secret : Nat) : Point :=
  secret • params.basePoint

/-- Partial ECDH composition. Secret range, subgroup validation, point
representation and conversion to key material remain obligations. -/
structure ECDHInterface (Point : Type) [AddCommGroup Point] where
  curve : ECCInterface Point

def ECDHInterface.sharedPoint {Point : Type} [AddCommGroup Point]
    (_params : ECDHInterface Point) (secret : Nat) (peer : Point) : Point :=
  secret • peer

end Catalog
