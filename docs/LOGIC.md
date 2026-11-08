# Propositional and first-order logic

The catalog separates raw syntax, truth in interpretations, and finite formal
derivations. These records add reusable mathematical interfaces; they do not
claim a complete survey of logic or a verified theorem-prover implementation.

| Layer | Authoritative record | Scope |
| --- | --- | --- |
| Propositional syntax | [PropositionalFormula](../concepts/PropositionalFormula.md) | Constructors, structural induction, atom support, simultaneous substitution |
| Propositional semantics | [PropositionalLogic](../concepts/PropositionalLogic.md) | Evaluation, entailment, validity, satisfiability, equivalence, substitution semantics, finite truth tables, CNF/DNF existence |
| Propositional proofs | [PropositionalNaturalDeduction](../concepts/PropositionalNaturalDeduction.md) | Assumption discharge, classical reductio, finite premise support, soundness, completeness, compactness |
| Signature | [FirstOrderSignature](../concepts/FirstOrderSignature.md) | Countable single-sorted finite-arity vocabulary, including nullary symbols |
| Terms | [TermAlgebra](../concepts/TermAlgebra.md) | Existing free ranked terms, instantiated rather than duplicated |
| Binding syntax | [FirstOrderFormula](../concepts/FirstOrderFormula.md) | Named binders, free variables, partial capture-free substitution, substitution support |
| First-order semantics | [PredicateLogic](../concepts/PredicateLogic.md) | Nonempty structures, total functions, identity equality, atomic satisfaction, assignment update, semantic queries, substitution lemma, assignment coincidence |
| First-order proofs | [FirstOrderNaturalDeduction](../concepts/FirstOrderNaturalDeduction.md) | Quantifier/equality rules, freshness, finite support, soundness, sentence completeness and compactness |

## Conventions

Primitive propositional syntax uses falsity, negation and conjunction; the
remaining classical connectives are macros. First-order syntax adds relation
applications, equality and named universal binders; existential quantification
is the classical dual macro. Natural deduction records explicitly instantiate
their rules. Prerequisites never supply inference rules or axioms implicitly.

Raw equality retains constructor shape and binder names. Semantic equivalence
compares truth in all interpretations. Alpha equivalence is a different
relation; no quotient or automatic renaming is assumed. First-order substitution
is **partial**: a term must be free for the substituted name. Renaming to a fresh
representative can prepare a legal substitution, but the current interface does
not implement that renaming.

For example, substituting `y` for free `x` in `∀y R(x,y)` is outside the
operation's domain. Substitution under `∀x` stops at that binder. The same
restrictions apply to universal elimination and equality substitution.
Universal introduction requires its name to be absent from every undischarged
hypothesis's free variables. Existential elimination also restricts its fresh
name in the conclusion and other hypotheses.

Propositional syntax permits any atom set, including the empty set. Its recorded
strong completeness and compactness proofs use at most countably many atoms.
First-order metatheorems use a countable signature, infinitely many names and
all nonempty models, including infinite ones. Compactness does not carry over
to finite models alone. Open formulas occur in proofs; the first-order
completeness/compactness statements use sentences.

CNF/DNF existence preserves semantic equivalence and uses the original atoms.
Empty conjunction means truth; empty disjunction means falsity. The construction
may grow exponentially. No efficient SAT encoding or first-order decision
procedure is asserted.

## Consulted sources

The expansion consulted the Open Logic Project's
[Propositional Logic](https://builds.openlogicproject.org/content/propositional-logic/propositional-logic.pdf)
and [First-order Logic](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf)
parts, both identifying revision `9620cc7` dated 2026-07-12, on 2026-11-08.
The named-variable rules were also checked against
[Logic and Proof, section 8.1](https://leanprover-community.github.io/logic_and_proof/natural_deduction_for_first_order_logic.html#rules-of-inference).
Each graph record has exact locators, adaptations, direct sources and explicit
derivation premises. Normal forms and several elementary substitution results
are catalog derivations from consulted definitions, rather than claims that
the references state those exact theorems.

Eleven historical source gaps in the two original semantic records were closed
after consultation, preserving their stable IDs and removing their missing-source
baseline entries. Other inherited gaps, including Boolean algebra citations,
remain disclosed.

The consulted PDF SHA-256 values identify the actual bytes (build URLs may change):

```text
Propositional Logic  1953b5ef2f6e8316ee8f054cb013967948cd36edb2dd2b48b0cdb205968014bf
First-order Logic    9532602efa8a9b70f393b76c95604bf31265abe39bfdcfabc1c9d71f734c2d93
```

PDFs were downloaded to temporary storage, not added to the repository.

## Lean and retrieval

[LogicSyntax.lean](../lean/Catalog/LogicSyntax.lean) adds named first-order syntax,
support and guarded substitution, a countable signature, and inductive
propositional/first-order derivability. Symbol families instantiate the subtypes
in `FirstOrderSignature`. Support functions return sets; their finiteness has
no registered compiled witness.

The original first-order satisfaction model uses de Bruijn binders. Its
correspondence with the new named syntax has no registered translation theorem.
No new soundness, completeness, compactness, substitution or normal-form result
is registered as a Lean proof witness. Compiling syntax and inference rules
does not prove those metatheorems. Consult each binding's limitations and fresh
verification evidence separately.

```sh
python3 scripts/catalog.py get FirstOrderFormula --sections operations axioms laws theorems
python3 scripts/agent_query.py node urn:csabs:theorem/PredicateLogic-substitution-semantics
python3 scripts/agent_query.py dossier FirstOrderNaturalDeduction --purpose proof --limit 80
```

Check truncation and retrieve omitted premises. Further extensions include
alpha-renaming/alpha quotients, prenex and Skolem forms, resolution/unification,
sequent calculi, and separately scoped intuitionistic or higher-order logics.
