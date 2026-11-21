# Capped increment pilot

This is an engineering example, accepted as a demonstration design by the
implementing agent. It is not a stakeholder acceptance receipt for a real product.

R1. For every natural number limit and n, bump terminates. If n < limit it
returns exactly n + 1; otherwise it returns n, including when n > limit.
R2. If n ≤ limit initially, the result is ≤ limit.

Naturals are unbounded mathematical Nat, with value equality. No machine integer,
allocation, concurrency, native compilation or IO execution guarantee is made.
The observable behavior of the pure function is its unique result. The
BehaviorRefinement interpretation has singleton sets of terminating results
on the same complete input domain. R2 is a conditional invariant; it does not
remove above-limit inputs from R1. The function has no loops or recursive calls.

The source implementation and proof use the same Counter.bump definition.
The independent finite oracle covers limits 0..12 and inputs 0..15, including
empty capacity and invalid-invariant initial states. Finite coverage is not proof.
The expected propositions must still be reviewed for correspondence to R1/R2.
