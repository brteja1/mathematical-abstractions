# Fuzzy sets and truth-value algebras

The catalog uses exact real degrees in I=[0,1]. Membership grades have no probability normalization. Each concept links directly to consulted mathematical sources, while local Lean sources document a separate interpretation.

| Concept | Interface | Relationship |
| --- | --- | --- |
| [FuzzySet](../concepts/FuzzySet.md) | Membership, min/max, standard complement, weak alpha cuts | A lattice on X→I with pointwise order; X may be empty |
| [TNorm](../concepts/TNorm.md) | Associative, commutative, monotone conjunction with identity 1 | A monoid on I; continuity is an extra condition |
| [TConorm](../concepts/TConorm.md) | Associative, commutative, monotone disjunction with identity 0 | A monoid on I; standard-negation duality constructs examples |
| [ResiduatedFuzzyLogic](../concepts/ResiduatedFuzzyLogic.md) | Left-continuous t-norm and residual adjunction | Specializes TNorm; a truth-value algebra rather than a proof calculus |

## Conventions and boundaries

For fuzzy sets, intersection is pointwise min, union is pointwise max, and standard complement is 1−μ. These operations form a bounded distributive lattice, but the selected complement does not make it a Boolean algebra when X is nonempty: on a singleton, μ=1/2 gives both min(μ,1−μ)=1/2 and max(μ,1−μ)=1/2. For X empty the function carrier has one member and the bounds coincide. Weak cuts use μ≥α, so the zero cut is all of X. Support {x:μ(x)>0} uses a strict inequality and is different from the zero cut.

The common t-norm instances are minimum, product, and Łukasiewicz max(0,a+b−1). The corresponding standard-negation dual conorms are maximum, a+b−ab, and min(1,a+b). A general t-norm need not be idempotent: product at a=b=1/2 returns 1/4. Thus replacing min by product changes the semantics of repeated conjunction, and its dual conorm is generally different from lattice join.

Residual implication is selected by T(a,c)≤b iff c≤(a⇒b). Left-continuity ensures the defining supremum is attained. For instance the product residual is 1 when a≤b, otherwise b/a; the latter branch has a>0. Its induced negation a⇒0 is 0 for a>0, whereas standard complement is 1−a. An arbitrary t-conorm paired with an arbitrary t-norm need not satisfy De Morgan duality.

These counterexamples are exact rational arithmetic and can be reproduced without catalog dependencies:

```sh
python3 - <<'PY'
from fractions import Fraction as Q
x = Q(1, 2)
assert min(x, 1-x) == max(x, 1-x) == x
assert x*x == Q(1, 4) != x
assert Q(0)/x == 0 != 1-x
PY
```

## Sources and Lean scope

The concept records attach claim-specific provenance to [Zadeh (1965)](https://people.eecs.berkeley.edu/~pister/publications/FamousPapers/Zadeh65FuzzySets.pdf), sections II–III and the level sets in section V; [Klement, Mesiar and Pap (2004)](https://www.flll.jku.at/sites/default/files/44_2004_KMesPap_TNormsPosPaperI_FSSPrintedVersion.pdf), definitions 2.1 and 3.1 and standard duality; and [Vetterlein, Regular left-continuous t-norms](https://www.flll.jku.at/sites/default/files/u24/LstetigeTnormen.pdf), sections 1–2. Consulted 2026-11-15. The weak-cut definition is extended from Zadeh's Euclidean context to any universe and includes α=0 explicitly.

[Catalog/FuzzyLogic.lean](../lean/Catalog/FuzzyLogic.lean) models bounded real degrees, membership functions, basic fuzzy-set operations, t-norm/conorm structures and residual adjunction. The conorm dual constructor and residual-derived operations are recorded as partial interfaces. Adjunction constrains the residual algebra; a Lean proof of its equivalence to sequential left-continuity is outside this change. No new law/theorem proof witnesses are registered. Compilation of a model does not prove every catalog claim.

Formula syntax, deductive systems, completeness theorems, fuzzy inference controllers, defuzzification, general residuated lattices, fuzzy numbers and fuzzy relations remain outside these four entries. Rounded implementations require their own explicit numeric semantics and law checks.
