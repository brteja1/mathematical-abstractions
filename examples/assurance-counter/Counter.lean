import Mathlib.Tactic

namespace Counter

-- The implementation proved below is also executed by main.
def bump (limit n : Nat) : Nat := if n < limit then n + 1 else n

def allowed (limit n result : Nat) : Prop :=
  (n < limit → result = n + 1) ∧ (¬ n < limit → result = n)

theorem refines : ∀ limit n, allowed limit n (bump limit n) := by
  intro limit n
  unfold allowed bump
  split <;> simp_all

theorem bounded : ∀ limit n, n ≤ limit → bump limit n ≤ limit := by
  intro limit n h
  unfold bump
  split <;> omega

end Counter

-- Exercise the actual implementation, including inputs above the limit.
def main : IO Unit := do
  for limit in List.range 13 do
    for n in List.range 16 do
      IO.println s!"{limit},{n},{Counter.bump limit n}"
