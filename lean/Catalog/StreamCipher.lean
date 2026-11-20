module

public import Catalog.Cryptography
public import Mathlib.Data.Bool.Basic

@[expose] public section

namespace Catalog

/-- Bounded synchronous bit keystream, with no assumed security properties. -/
abbrev StreamCipher (K N : Type) (capacity : Nat) := K → N → Fin capacity → Bool

def streamXor {n : Nat} (a b : CryptoBits n) : CryptoBits n :=
  fun i => xor (a i) (b i)

/-- Offset and length must stay within capacity; no counter wraparound. -/
def streamCrypt {K N : Type} {capacity : Nat} (g : StreamCipher K N capacity)
    (k : K) (nonce : N) (offset n : Nat) (fits : offset + n ≤ capacity)
    (message : CryptoBits n) : CryptoBits n :=
  fun i => xor (message i)
    (g k nonce ⟨offset + i.val, Nat.lt_of_lt_of_le (Nat.add_lt_add_left i.isLt offset) fits⟩)

/-- A deliberately insecure concrete inhabitant demonstrating nonempty inputs. -/
def exampleStreamCipher : StreamCipher Bool Bool 2 :=
  fun k nonce i => xor k (xor nonce (i.val == 1))

theorem stream_roundtrip {K N : Type} {capacity : Nat}
    (g : StreamCipher K N capacity) (k : K) (nonce : N)
    (offset n : Nat) (fits : offset + n ≤ capacity) (m : CryptoBits n) :
    streamCrypt g k nonce offset n fits (streamCrypt g k nonce offset n fits m) = m := by
  funext i
  simp [streamCrypt]

theorem stream_model_satisfaction :
    (∀ {K N : Type} {capacity : Nat} (g : StreamCipher K N capacity)
      (k : K) (nonce : N) (offset n : Nat) (fits : offset + n ≤ capacity)
      (m : CryptoBits n) (i : Fin n),
      streamCrypt g k nonce offset n fits m i =
        xor (m i) (g k nonce ⟨offset + i.val,
          Nat.lt_of_lt_of_le (Nat.add_lt_add_left i.isLt offset) fits⟩)) ∧
    streamCrypt exampleStreamCipher true false 0 1 (by decide) (fun _ => false) 0 = true ∧
    streamCrypt exampleStreamCipher false false 0 1 (by decide) (fun _ => false) 0 = false := by
  exact ⟨by intros; rfl, rfl, rfl⟩

theorem stream_empty {K N : Type} {capacity : Nat}
    (g : StreamCipher K N capacity) (k : K) (nonce : N)
    (offset : Nat) (fits : offset + 0 ≤ capacity) (m : CryptoBits 0) :
    streamCrypt g k nonce offset 0 fits m = m := by
  funext i
  exact Fin.elim0 i

theorem stream_reused_keystream {K N : Type} {capacity : Nat}
    (g : StreamCipher K N capacity) (k : K) (nonce : N)
    (offset n : Nat) (fits : offset + n ≤ capacity) (a b : CryptoBits n) :
    streamXor (streamCrypt g k nonce offset n fits a)
      (streamCrypt g k nonce offset n fits b) = streamXor a b := by
  funext i
  simp only [streamXor, streamCrypt]
  cases a i <;> cases b i <;>
    cases g k nonce ⟨offset + i.val,
      Nat.lt_of_lt_of_le (Nat.add_lt_add_left i.isLt offset) fits⟩ <;> rfl

theorem stream_malleability {K N : Type} {capacity : Nat}
    (g : StreamCipher K N capacity) (k : K) (nonce : N)
    (offset n : Nat) (fits : offset + n ≤ capacity) (m delta : CryptoBits n) :
    streamCrypt g k nonce offset n fits
      (streamXor (streamCrypt g k nonce offset n fits m) delta) = streamXor m delta := by
  funext i
  simp only [streamXor, streamCrypt]
  cases m i <;> cases delta i <;>
    cases g k nonce ⟨offset + i.val,
      Nat.lt_of_lt_of_le (Nat.add_lt_add_left i.isLt offset) fits⟩ <;> rfl

end Catalog
