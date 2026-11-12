# Normalized template constraints with atomic identity

Normalized conjunction/disjunction trees whose satisfaction short-circuits and whose C++ subsumption compares atomic origins and parameter mappings rather than arbitrary logical implication.

**Notation:** C ::= Atom(origin,mapping) | And(C,C) | Or(C,C); sat:C×Args→Satisfied⊎Unsatisfied⊎IllFormed; P⊒Q iff every DNF(P) clause shares an identical atom with every CNF(Q) clause

**Stable ID:** `urn:csabs:concept/TemplateConstraint`

**Categories:** Programming-language semantics → Generic programming → Template metaprogramming

**Kind:** semantic-model

**Prerequisites:** [Finite propositional formula syntax](PropositionalFormula.md), [Finite sequence (List datatype)](Sequence.md)

**Related concepts:** [Class template partial-specialization selection](TemplateSpecialization.md), [Ordered substitution with immediate-context failure](TemplateSubstitution.md), [Predicate Logic](PredicateLogic.md)

## Backlinks

- [Java generic inference constraints and resolution obligations](JavaTypeInference.md) — `relatedConcept`
- [Class template partial-specialization selection](TemplateSpecialization.md) — `relatedConcept`
- [Ordered substitution with immediate-context failure](TemplateSubstitution.md) — `relatedConcept`

## Mathematical formulation

Normalized constraints are identity-bearing syntax C ::= atom(a) | C∧C | C∨C. Satisfaction is ordered short-circuit evaluation into {satisfied,unsatisfied,illFormed}. p subsumes q iff every clause L of DNF(p) and R of CNF(q) share an identical atom: ∀L∈DNF(p),R∈CNF(q),∃a∈L,b∈R,a=b.

**Lean formulation** (in its source module context):

```lean
inductive TemplateConstraint (Atom : Type u) where
  | atom : Atom → TemplateConstraint Atom
  | conj : TemplateConstraint Atom → TemplateConstraint Atom → TemplateConstraint Atom
  | disj : TemplateConstraint Atom → TemplateConstraint Atom → TemplateConstraint Atom
```

**Source:** [`Catalog.TMP.TemplateConstraint`](../lean/Catalog/TemplateMetaprogramming.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Atom/conjunction/disjunction trees, three-way short-circuit satisfaction, DNF/CNF clauses and identity-based subsumption. Atom equality must encode resolved source-expression origin and parameter mappings.

**Limits:** Actual C++ normalization, argument substitution, atomic equivalence and constant-expression checking remain adapters. Invalid normalization/IFNDR and later-standard fold-expanded subsumption are outside the profile.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected defining rules: Identical atoms have the same source-expression appearance and equivalent parameter mappings; satisfaction substitutes arguments and requires a bool constant-expression result. Different expressions with equal values need not be identical atoms. sat(And(P,Q),a)=Unsatisfied if sat(P,a)=Unsatisfied, else sat(Q,a) if sat(P,a)=Satisfied; sat(Or(P,Q),a)=Satisfied if sat(P,a)=Satisfied, else sat(Q,a) if sat(P,a)=Unsatisfied; encountered IllFormed propagates. dnf(Atom a)=[[a]]; dnf(P∨Q)=dnf(P)++dnf(Q); dnf(P∧Q)=[p++q | p∈dnf(P),q∈dnf(Q)]; cnf uses the dual equations, swapping ∧ and ∨. P⊒Q ⇔ ∀p∈dnf(P),q∈cnf(Q), ∃a∈p,b∈q, identical(a,b).

**basisKind:** extensional-structural-definition

**basisScope:** C++20 N4861 normalized-constraint fragment, after well-formed normalization. Atoms include source-expression appearance and canonical parameter mapping; equal truth values do not identify atoms. Atom substitution invalidity yields Unsatisfied only where the standard permits it; a required non-bool/nonconstant-expression diagnostic is IllFormed. Normalization-time invalid mappings/IFNDR are outside this tree model, not silently false. Constraint fold expressions remain opaque atoms as appropriate to this version; no C++26 fold-expanded ordering is imported. No arbitrary SAT/SMT entailment or full overload resolution is assumed. Tree equality is syntactic in atom identities; satisfaction equivalence is a different relation.

**verificationObligation:** Use the stated C++20 N4861 profile and map types, argument equivalence, visibility, definedness and implementation limits explicitly.; Do not infer an entire compiler semantics, decidability, universal termination or executable proof from these selected interfaces.

**reviewStatus:** Editorial source/interface review; model bindings and compiled theorem witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-TemplateConstraint-satisfy"></a>

### satisfy

`urn:csabs:operation/TemplateConstraint-satisfy`

**signature:** satisfy : Constraint×Args→ConstraintStatus

**description:** Evaluate atoms with the supplied substitution/constant-expression checker. And skips its right operand on Unsatisfied; Or skips it on Satisfied. An encountered IllFormed is propagated.

**precondition:** Typed inputs satisfying the selected profile.

**postcondition:** Evaluate atoms with the supplied substitution/constant-expression checker. And skips its right operand on Unsatisfied; Or skips it on Satisfied. An encountered IllFormed is propagated.

**totality:** Total mathematical operation on the stated inputs.

**source:** [C++20 working draft N4861 [temp.constr.atomic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.atomic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.normal] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.normal); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.op] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.op); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3

**sourceNote:** Models only already normalized atom/and/or trees and their identity-based subsumption. Atom identity and evaluation are adapters to the source rules; Boolean equivalence does not erase source identity.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-TemplateConstraint-normal-forms"></a>

### normal-forms

`urn:csabs:operation/TemplateConstraint-normal-forms`

**signature:** dnf,cnf : Constraint→Seq(Seq(Atom))

**description:** For already normalized identity-bearing trees, form DNF/CNF clause lists by distributivity; preserve every atomic origin/mapping. These are not the language normalization step for concept-ids.

**precondition:** Typed inputs satisfying the selected profile.

**postcondition:** For already normalized identity-bearing trees, form DNF/CNF clause lists by distributivity; preserve every atomic origin/mapping. These are not the language normalization step for concept-ids.

**totality:** Total mathematical operation on the stated inputs.

**source:** [C++20 working draft N4861 [temp.constr.atomic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.atomic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.normal] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.normal); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.op] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.op); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3

**sourceNote:** Models only already normalized atom/and/or trees and their identity-based subsumption. Atom identity and evaluation are adapters to the source rules; Boolean equivalence does not erase source identity.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-TemplateConstraint-subsumes"></a>

### subsumes

`urn:csabs:operation/TemplateConstraint-subsumes`

**signature:** subsumes : Constraint×Constraint→Prop

**description:** For every p∈dnf(P) and q∈cnf(Q), some a∈p and b∈q are identical atoms.

**precondition:** Typed inputs satisfying the selected profile.

**postcondition:** For every p∈dnf(P) and q∈cnf(Q), some a∈p and b∈q are identical atoms.

**totality:** Total mathematical operation on the stated inputs.

**source:** [C++20 working draft N4861 [temp.constr.atomic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.atomic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.normal] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.normal); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.op] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.op); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3

**sourceNote:** Models only already normalized atom/and/or trees and their identity-based subsumption. Atom identity and evaluation are adapters to the source rules; Boolean equivalence does not erase source identity.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-TemplateConstraint-atom-identity"></a>

### atom-identity

`urn:csabs:axiom/TemplateConstraint-atom-identity`

**statement:** Identical atoms have the same source-expression appearance and equivalent parameter mappings; satisfaction substitutes arguments and requires a bool constant-expression result. Different expressions with equal values need not be identical atoms.

**formalStatement:** Identical atoms have the same source-expression appearance and equivalent parameter mappings; satisfaction substitutes arguments and requires a bool constant-expression result. Different expressions with equal values need not be identical atoms.

**assumptions:** C++20 N4861 normalized-constraint fragment, after well-formed normalization. Atoms include source-expression appearance and canonical parameter mapping; equal truth values do not identify atoms. Atom substitution invalidity yields Unsatisfied only where the standard permits it; a required non-bool/nonconstant-expression diagnostic is IllFormed. Normalization-time invalid mappings/IFNDR are outside this tree model, not silently false. Constraint fold expressions remain opaque atoms as appropriate to this version; no C++26 fold-expanded ordering is imported. No arbitrary SAT/SMT entailment or full overload resolution is assumed. Tree equality is syntactic in atom identities; satisfaction equivalence is a different relation.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.constr.atomic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.atomic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.normal] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.normal); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.op] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.op); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3

**sourceNote:** Models only already normalized atom/and/or trees and their identity-based subsumption. Atom identity and evaluation are adapters to the source rules; Boolean equivalence does not erase source identity.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-TemplateConstraint-short-circuit"></a>

### short-circuit

`urn:csabs:axiom/TemplateConstraint-short-circuit`

**statement:** sat(And(P,Q),a)=Unsatisfied if sat(P,a)=Unsatisfied, else sat(Q,a) if sat(P,a)=Satisfied; sat(Or(P,Q),a)=Satisfied if sat(P,a)=Satisfied, else sat(Q,a) if sat(P,a)=Unsatisfied; encountered IllFormed propagates.

**formalStatement:** sat(And(P,Q),a)=Unsatisfied if sat(P,a)=Unsatisfied, else sat(Q,a) if sat(P,a)=Satisfied; sat(Or(P,Q),a)=Satisfied if sat(P,a)=Satisfied, else sat(Q,a) if sat(P,a)=Unsatisfied; encountered IllFormed propagates.

**assumptions:** C++20 N4861 normalized-constraint fragment, after well-formed normalization. Atoms include source-expression appearance and canonical parameter mapping; equal truth values do not identify atoms. Atom substitution invalidity yields Unsatisfied only where the standard permits it; a required non-bool/nonconstant-expression diagnostic is IllFormed. Normalization-time invalid mappings/IFNDR are outside this tree model, not silently false. Constraint fold expressions remain opaque atoms as appropriate to this version; no C++26 fold-expanded ordering is imported. No arbitrary SAT/SMT entailment or full overload resolution is assumed. Tree equality is syntactic in atom identities; satisfaction equivalence is a different relation.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.constr.atomic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.atomic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.normal] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.normal); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.op] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.op); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3

**sourceNote:** Models only already normalized atom/and/or trees and their identity-based subsumption. Atom identity and evaluation are adapters to the source rules; Boolean equivalence does not erase source identity.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-TemplateConstraint-clause-forms"></a>

### clause-forms

`urn:csabs:axiom/TemplateConstraint-clause-forms`

**statement:** dnf(Atom a)=[[a]]; dnf(P∨Q)=dnf(P)++dnf(Q); dnf(P∧Q)=[p++q | p∈dnf(P),q∈dnf(Q)]; cnf uses the dual equations, swapping ∧ and ∨.

**formalStatement:** dnf(Atom a)=[[a]]; dnf(P∨Q)=dnf(P)++dnf(Q); dnf(P∧Q)=[p++q | p∈dnf(P),q∈dnf(Q)]; cnf uses the dual equations, swapping ∧ and ∨.

**assumptions:** C++20 N4861 normalized-constraint fragment, after well-formed normalization. Atoms include source-expression appearance and canonical parameter mapping; equal truth values do not identify atoms. Atom substitution invalidity yields Unsatisfied only where the standard permits it; a required non-bool/nonconstant-expression diagnostic is IllFormed. Normalization-time invalid mappings/IFNDR are outside this tree model, not silently false. Constraint fold expressions remain opaque atoms as appropriate to this version; no C++26 fold-expanded ordering is imported. No arbitrary SAT/SMT entailment or full overload resolution is assumed. Tree equality is syntactic in atom identities; satisfaction equivalence is a different relation.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.constr.atomic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.atomic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.normal] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.normal); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.op] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.op); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3

**sourceNote:** Models only already normalized atom/and/or trees and their identity-based subsumption. Atom identity and evaluation are adapters to the source rules; Boolean equivalence does not erase source identity.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-TemplateConstraint-identity-subsumption"></a>

### identity-subsumption

`urn:csabs:axiom/TemplateConstraint-identity-subsumption`

**statement:** P⊒Q ⇔ ∀p∈dnf(P),q∈cnf(Q), ∃a∈p,b∈q, identical(a,b).

**formalStatement:** P⊒Q ⇔ ∀p∈dnf(P),q∈cnf(Q), ∃a∈p,b∈q, identical(a,b).

**assumptions:** C++20 N4861 normalized-constraint fragment, after well-formed normalization. Atoms include source-expression appearance and canonical parameter mapping; equal truth values do not identify atoms. Atom substitution invalidity yields Unsatisfied only where the standard permits it; a required non-bool/nonconstant-expression diagnostic is IllFormed. Normalization-time invalid mappings/IFNDR are outside this tree model, not silently false. Constraint fold expressions remain opaque atoms as appropriate to this version; no C++26 fold-expanded ordering is imported. No arbitrary SAT/SMT entailment or full overload resolution is assumed. Tree equality is syntactic in atom identities; satisfaction equivalence is a different relation.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.constr.atomic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.atomic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.normal] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.normal); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.op] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.op); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3

**sourceNote:** Models only already normalized atom/and/or trees and their identity-based subsumption. Atom identity and evaluation are adapters to the source rules; Boolean equivalence does not erase source identity.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-TemplateConstraint-conjunction-subsumes-atom"></a>

### conjunction-subsumes-atom

`urn:csabs:law/TemplateConstraint-conjunction-subsumes-atom`

**statement:** (Atom(a)∧Atom(b))⊒Atom(a); if a and b are not identical, ¬(Atom(a)⊒(Atom(a)∧Atom(b))).

**formalStatement:** (Atom(a)∧Atom(b))⊒Atom(a); if a and b are not identical, ¬(Atom(a)⊒(Atom(a)∧Atom(b))).

**assumptions:** C++20 N4861 normalized-constraint fragment, after well-formed normalization. Atoms include source-expression appearance and canonical parameter mapping; equal truth values do not identify atoms. Atom substitution invalidity yields Unsatisfied only where the standard permits it; a required non-bool/nonconstant-expression diagnostic is IllFormed. Normalization-time invalid mappings/IFNDR are outside this tree model, not silently false. Constraint fold expressions remain opaque atoms as appropriate to this version; no C++26 fold-expanded ordering is imported. No arbitrary SAT/SMT entailment or full overload resolution is assumed. Tree equality is syntactic in atom identities; satisfaction equivalence is a different relation.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.constr.atomic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.atomic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.normal] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.normal); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.op] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.op); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3

**sourceNote:** Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.

**provenanceKind:** derived

**dependsOn:** [clause-forms](TemplateConstraint.md#node-urn-csabs-axiom-TemplateConstraint-clause-forms); [identity-subsumption](TemplateConstraint.md#node-urn-csabs-axiom-TemplateConstraint-identity-subsumption)

**proofSketch:** The conjunction has one DNF clause [a,b], sharing a with the target [a]. In the reverse direction CNF has clauses [a] and [b], and [a] cannot share an identical atom with [b].

<a id="node-urn-csabs-law-TemplateConstraint-false-left-skips-invalid-right"></a>

### false-left-skips-invalid-right

`urn:csabs:law/TemplateConstraint-false-left-skips-invalid-right`

**statement:** sat(P,a)=Unsatisfied ⇒ sat(And(P,Q),a)=Unsatisfied without checking Q, even if evaluating Q separately would be IllFormed.

**formalStatement:** sat(P,a)=Unsatisfied ⇒ sat(And(P,Q),a)=Unsatisfied without checking Q, even if evaluating Q separately would be IllFormed.

**assumptions:** C++20 N4861 normalized-constraint fragment, after well-formed normalization. Atoms include source-expression appearance and canonical parameter mapping; equal truth values do not identify atoms. Atom substitution invalidity yields Unsatisfied only where the standard permits it; a required non-bool/nonconstant-expression diagnostic is IllFormed. Normalization-time invalid mappings/IFNDR are outside this tree model, not silently false. Constraint fold expressions remain opaque atoms as appropriate to this version; no C++26 fold-expanded ordering is imported. No arbitrary SAT/SMT entailment or full overload resolution is assumed. Tree equality is syntactic in atom identities; satisfaction equivalence is a different relation.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.constr.atomic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.atomic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.normal] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.normal); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.constr.op] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.op); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3

**sourceNote:** Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.

**provenanceKind:** derived

**dependsOn:** [short-circuit](TemplateConstraint.md#node-urn-csabs-axiom-TemplateConstraint-short-circuit)

**proofSketch:** Apply the first conjunction branch. This is satisfaction short-circuiting after valid normalization, not permission to ignore normalization errors.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [C++20 working draft N4861 [temp.constr.atomic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.atomic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause
- [C++20 working draft N4861 [temp.constr.normal] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.normal); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause
- [C++20 working draft N4861 [temp.constr.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause
- [C++20 working draft N4861 [temp.constr.op] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.constr.op); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3

**sourceNote:** Models only already normalized atom/and/or trees and their identity-based subsumption. Atom identity and evaluation are adapters to the source rules; Boolean equivalence does not erase source identity.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/TemplateConstraint",
    "type": "Concept",
    "shortForm": "TemplateConstraint",
    "fullName": "Normalized template constraints with atomic identity",
    "definition": "Normalized conjunction/disjunction trees whose satisfaction short-circuits and whose C++ subsumption compares atomic origins and parameter mappings rather than arbitrary logical implication.",
    "notation": "C ::= Atom(origin,mapping) | And(C,C) | Or(C,C); sat:C×Args→Satisfied⊎Unsatisfied⊎IllFormed; P⊒Q iff every DNF(P) clause shares an identical atom with every CNF(Q) clause",
    "category": [
      "urn:csabs:category/template-metaprogramming"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/PropositionalFormula",
      "urn:csabs:concept/Sequence"
    ],
    "relatedConcept": [
      "urn:csabs:concept/TemplateSpecialization",
      "urn:csabs:concept/TemplateSubstitution",
      "urn:csabs:concept/PredicateLogic"
    ],
    "hasOperation": [
      "urn:csabs:operation/TemplateConstraint-satisfy",
      "urn:csabs:operation/TemplateConstraint-normal-forms",
      "urn:csabs:operation/TemplateConstraint-subsumes"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/TemplateConstraint-atom-identity",
      "urn:csabs:axiom/TemplateConstraint-short-circuit",
      "urn:csabs:axiom/TemplateConstraint-clause-forms",
      "urn:csabs:axiom/TemplateConstraint-identity-subsumption"
    ],
    "hasLaw": [
      "urn:csabs:law/TemplateConstraint-conjunction-subsumes-atom",
      "urn:csabs:law/TemplateConstraint-false-left-skips-invalid-right"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "C++20 N4861 normalized-constraint fragment, after well-formed normalization. Atoms include source-expression appearance and canonical parameter mapping; equal truth values do not identify atoms. Atom substitution invalidity yields Unsatisfied only where the standard permits it; a required non-bool/nonconstant-expression diagnostic is IllFormed. Normalization-time invalid mappings/IFNDR are outside this tree model, not silently false. Constraint fold expressions remain opaque atoms as appropriate to this version; no C++26 fold-expanded ordering is imported. No arbitrary SAT/SMT entailment or full overload resolution is assumed. Tree equality is syntactic in atom identities; satisfaction equivalence is a different relation.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; model bindings and compiled theorem witnesses are separate.",
    "verificationObligation": [
      "Use the stated C++20 N4861 profile and map types, argument equivalence, visibility, definedness and implementation limits explicitly.",
      "Do not infer an entire compiler semantics, decidability, universal termination or executable proof from these selected interfaces."
    ],
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.constr.atomic",
      "urn:csabs:source/cpp20-n4861-temp.constr.normal",
      "urn:csabs:source/cpp20-n4861-temp.constr.order",
      "urn:csabs:source/cpp20-n4861-temp.constr.op"
    ],
    "sourceLocator": "[temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3",
    "sourceNote": "Models only already normalized atom/and/or trees and their identity-based subsumption. Atom identity and evaluation are adapters to the source rules; Boolean equivalence does not erase source identity.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: Identical atoms have the same source-expression appearance and equivalent parameter mappings; satisfaction substitutes arguments and requires a bool constant-expression result. Different expressions with equal values need not be identical atoms. sat(And(P,Q),a)=Unsatisfied if sat(P,a)=Unsatisfied, else sat(Q,a) if sat(P,a)=Satisfied; sat(Or(P,Q),a)=Satisfied if sat(P,a)=Satisfied, else sat(Q,a) if sat(P,a)=Unsatisfied; encountered IllFormed propagates. dnf(Atom a)=[[a]]; dnf(P∨Q)=dnf(P)++dnf(Q); dnf(P∧Q)=[p++q | p∈dnf(P),q∈dnf(Q)]; cnf uses the dual equations, swapping ∧ and ∨. P⊒Q ⇔ ∀p∈dnf(P),q∈cnf(Q), ∃a∈p,b∈q, identical(a,b).",
    "leanFormulation": "inductive TemplateConstraint (Atom : Type u) where\n  | atom : Atom → TemplateConstraint Atom\n  | conj : TemplateConstraint Atom → TemplateConstraint Atom → TemplateConstraint Atom\n  | disj : TemplateConstraint Atom → TemplateConstraint Atom → TemplateConstraint Atom",
    "formulationSource": "urn:csabs:source/local-lean-TemplateMetaprogramming",
    "formulationLocator": "Catalog.TMP.TemplateConstraint",
    "formulationScope": "partial",
    "leanModelMapping": "Atom/conjunction/disjunction trees, three-way short-circuit satisfaction, DNF/CNF clauses and identity-based subsumption. Atom equality must encode resolved source-expression origin and parameter mappings.",
    "leanModelLimitations": "Actual C++ normalization, argument substitution, atomic equivalence and constant-expression checking remain adapters. Invalid normalization/IFNDR and later-standard fold-expanded subsumption are outside the profile.",
    "mathematicalFormulation": "Normalized constraints are identity-bearing syntax C ::= atom(a) | C∧C | C∨C. Satisfaction is ordered short-circuit evaluation into {satisfied,unsatisfied,illFormed}. p subsumes q iff every clause L of DNF(p) and R of CNF(q) share an identical atom: ∀L∈DNF(p),R∈CNF(q),∃a∈L,b∈R,a=b."
  },
  {
    "id": "urn:csabs:operation/TemplateConstraint-satisfy",
    "type": "Operation",
    "name": "satisfy",
    "signature": "satisfy : Constraint×Args→ConstraintStatus",
    "description": "Evaluate atoms with the supplied substitution/constant-expression checker. And skips its right operand on Unsatisfied; Or skips it on Satisfied. An encountered IllFormed is propagated.",
    "concept": "urn:csabs:concept/TemplateConstraint",
    "precondition": "Typed inputs satisfying the selected profile.",
    "postcondition": "Evaluate atoms with the supplied substitution/constant-expression checker. And skips its right operand on Unsatisfied; Or skips it on Satisfied. An encountered IllFormed is propagated.",
    "totality": "Total mathematical operation on the stated inputs.",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.constr.atomic",
      "urn:csabs:source/cpp20-n4861-temp.constr.normal",
      "urn:csabs:source/cpp20-n4861-temp.constr.order",
      "urn:csabs:source/cpp20-n4861-temp.constr.op"
    ],
    "sourceLocator": "[temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3",
    "sourceNote": "Models only already normalized atom/and/or trees and their identity-based subsumption. Atom identity and evaluation are adapters to the source rules; Boolean equivalence does not erase source identity.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/TemplateConstraint-normal-forms",
    "type": "Operation",
    "name": "normal-forms",
    "signature": "dnf,cnf : Constraint→Seq(Seq(Atom))",
    "description": "For already normalized identity-bearing trees, form DNF/CNF clause lists by distributivity; preserve every atomic origin/mapping. These are not the language normalization step for concept-ids.",
    "concept": "urn:csabs:concept/TemplateConstraint",
    "precondition": "Typed inputs satisfying the selected profile.",
    "postcondition": "For already normalized identity-bearing trees, form DNF/CNF clause lists by distributivity; preserve every atomic origin/mapping. These are not the language normalization step for concept-ids.",
    "totality": "Total mathematical operation on the stated inputs.",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.constr.atomic",
      "urn:csabs:source/cpp20-n4861-temp.constr.normal",
      "urn:csabs:source/cpp20-n4861-temp.constr.order",
      "urn:csabs:source/cpp20-n4861-temp.constr.op"
    ],
    "sourceLocator": "[temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3",
    "sourceNote": "Models only already normalized atom/and/or trees and their identity-based subsumption. Atom identity and evaluation are adapters to the source rules; Boolean equivalence does not erase source identity.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/TemplateConstraint-subsumes",
    "type": "Operation",
    "name": "subsumes",
    "signature": "subsumes : Constraint×Constraint→Prop",
    "description": "For every p∈dnf(P) and q∈cnf(Q), some a∈p and b∈q are identical atoms.",
    "concept": "urn:csabs:concept/TemplateConstraint",
    "precondition": "Typed inputs satisfying the selected profile.",
    "postcondition": "For every p∈dnf(P) and q∈cnf(Q), some a∈p and b∈q are identical atoms.",
    "totality": "Total mathematical operation on the stated inputs.",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.constr.atomic",
      "urn:csabs:source/cpp20-n4861-temp.constr.normal",
      "urn:csabs:source/cpp20-n4861-temp.constr.order",
      "urn:csabs:source/cpp20-n4861-temp.constr.op"
    ],
    "sourceLocator": "[temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3",
    "sourceNote": "Models only already normalized atom/and/or trees and their identity-based subsumption. Atom identity and evaluation are adapters to the source rules; Boolean equivalence does not erase source identity.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/TemplateConstraint-atom-identity",
    "type": "Axiom",
    "name": "atom-identity",
    "statement": "Identical atoms have the same source-expression appearance and equivalent parameter mappings; satisfaction substitutes arguments and requires a bool constant-expression result. Different expressions with equal values need not be identical atoms.",
    "formalStatement": "Identical atoms have the same source-expression appearance and equivalent parameter mappings; satisfaction substitutes arguments and requires a bool constant-expression result. Different expressions with equal values need not be identical atoms.",
    "assumptions": [
      "C++20 N4861 normalized-constraint fragment, after well-formed normalization. Atoms include source-expression appearance and canonical parameter mapping; equal truth values do not identify atoms. Atom substitution invalidity yields Unsatisfied only where the standard permits it; a required non-bool/nonconstant-expression diagnostic is IllFormed. Normalization-time invalid mappings/IFNDR are outside this tree model, not silently false. Constraint fold expressions remain opaque atoms as appropriate to this version; no C++26 fold-expanded ordering is imported. No arbitrary SAT/SMT entailment or full overload resolution is assumed. Tree equality is syntactic in atom identities; satisfaction equivalence is a different relation.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateConstraint"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.constr.atomic",
      "urn:csabs:source/cpp20-n4861-temp.constr.normal",
      "urn:csabs:source/cpp20-n4861-temp.constr.order",
      "urn:csabs:source/cpp20-n4861-temp.constr.op"
    ],
    "sourceLocator": "[temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3",
    "sourceNote": "Models only already normalized atom/and/or trees and their identity-based subsumption. Atom identity and evaluation are adapters to the source rules; Boolean equivalence does not erase source identity.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/TemplateConstraint-short-circuit",
    "type": "Axiom",
    "name": "short-circuit",
    "statement": "sat(And(P,Q),a)=Unsatisfied if sat(P,a)=Unsatisfied, else sat(Q,a) if sat(P,a)=Satisfied; sat(Or(P,Q),a)=Satisfied if sat(P,a)=Satisfied, else sat(Q,a) if sat(P,a)=Unsatisfied; encountered IllFormed propagates.",
    "formalStatement": "sat(And(P,Q),a)=Unsatisfied if sat(P,a)=Unsatisfied, else sat(Q,a) if sat(P,a)=Satisfied; sat(Or(P,Q),a)=Satisfied if sat(P,a)=Satisfied, else sat(Q,a) if sat(P,a)=Unsatisfied; encountered IllFormed propagates.",
    "assumptions": [
      "C++20 N4861 normalized-constraint fragment, after well-formed normalization. Atoms include source-expression appearance and canonical parameter mapping; equal truth values do not identify atoms. Atom substitution invalidity yields Unsatisfied only where the standard permits it; a required non-bool/nonconstant-expression diagnostic is IllFormed. Normalization-time invalid mappings/IFNDR are outside this tree model, not silently false. Constraint fold expressions remain opaque atoms as appropriate to this version; no C++26 fold-expanded ordering is imported. No arbitrary SAT/SMT entailment or full overload resolution is assumed. Tree equality is syntactic in atom identities; satisfaction equivalence is a different relation.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateConstraint"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.constr.atomic",
      "urn:csabs:source/cpp20-n4861-temp.constr.normal",
      "urn:csabs:source/cpp20-n4861-temp.constr.order",
      "urn:csabs:source/cpp20-n4861-temp.constr.op"
    ],
    "sourceLocator": "[temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3",
    "sourceNote": "Models only already normalized atom/and/or trees and their identity-based subsumption. Atom identity and evaluation are adapters to the source rules; Boolean equivalence does not erase source identity.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/TemplateConstraint-clause-forms",
    "type": "Axiom",
    "name": "clause-forms",
    "statement": "dnf(Atom a)=[[a]]; dnf(P∨Q)=dnf(P)++dnf(Q); dnf(P∧Q)=[p++q | p∈dnf(P),q∈dnf(Q)]; cnf uses the dual equations, swapping ∧ and ∨.",
    "formalStatement": "dnf(Atom a)=[[a]]; dnf(P∨Q)=dnf(P)++dnf(Q); dnf(P∧Q)=[p++q | p∈dnf(P),q∈dnf(Q)]; cnf uses the dual equations, swapping ∧ and ∨.",
    "assumptions": [
      "C++20 N4861 normalized-constraint fragment, after well-formed normalization. Atoms include source-expression appearance and canonical parameter mapping; equal truth values do not identify atoms. Atom substitution invalidity yields Unsatisfied only where the standard permits it; a required non-bool/nonconstant-expression diagnostic is IllFormed. Normalization-time invalid mappings/IFNDR are outside this tree model, not silently false. Constraint fold expressions remain opaque atoms as appropriate to this version; no C++26 fold-expanded ordering is imported. No arbitrary SAT/SMT entailment or full overload resolution is assumed. Tree equality is syntactic in atom identities; satisfaction equivalence is a different relation.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateConstraint"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.constr.atomic",
      "urn:csabs:source/cpp20-n4861-temp.constr.normal",
      "urn:csabs:source/cpp20-n4861-temp.constr.order",
      "urn:csabs:source/cpp20-n4861-temp.constr.op"
    ],
    "sourceLocator": "[temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3",
    "sourceNote": "Models only already normalized atom/and/or trees and their identity-based subsumption. Atom identity and evaluation are adapters to the source rules; Boolean equivalence does not erase source identity.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/TemplateConstraint-identity-subsumption",
    "type": "Axiom",
    "name": "identity-subsumption",
    "statement": "P⊒Q ⇔ ∀p∈dnf(P),q∈cnf(Q), ∃a∈p,b∈q, identical(a,b).",
    "formalStatement": "P⊒Q ⇔ ∀p∈dnf(P),q∈cnf(Q), ∃a∈p,b∈q, identical(a,b).",
    "assumptions": [
      "C++20 N4861 normalized-constraint fragment, after well-formed normalization. Atoms include source-expression appearance and canonical parameter mapping; equal truth values do not identify atoms. Atom substitution invalidity yields Unsatisfied only where the standard permits it; a required non-bool/nonconstant-expression diagnostic is IllFormed. Normalization-time invalid mappings/IFNDR are outside this tree model, not silently false. Constraint fold expressions remain opaque atoms as appropriate to this version; no C++26 fold-expanded ordering is imported. No arbitrary SAT/SMT entailment or full overload resolution is assumed. Tree equality is syntactic in atom identities; satisfaction equivalence is a different relation.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateConstraint"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.constr.atomic",
      "urn:csabs:source/cpp20-n4861-temp.constr.normal",
      "urn:csabs:source/cpp20-n4861-temp.constr.order",
      "urn:csabs:source/cpp20-n4861-temp.constr.op"
    ],
    "sourceLocator": "[temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3",
    "sourceNote": "Models only already normalized atom/and/or trees and their identity-based subsumption. Atom identity and evaluation are adapters to the source rules; Boolean equivalence does not erase source identity.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/TemplateConstraint-conjunction-subsumes-atom",
    "type": "Law",
    "name": "conjunction-subsumes-atom",
    "statement": "(Atom(a)∧Atom(b))⊒Atom(a); if a and b are not identical, ¬(Atom(a)⊒(Atom(a)∧Atom(b))).",
    "formalStatement": "(Atom(a)∧Atom(b))⊒Atom(a); if a and b are not identical, ¬(Atom(a)⊒(Atom(a)∧Atom(b))).",
    "assumptions": [
      "C++20 N4861 normalized-constraint fragment, after well-formed normalization. Atoms include source-expression appearance and canonical parameter mapping; equal truth values do not identify atoms. Atom substitution invalidity yields Unsatisfied only where the standard permits it; a required non-bool/nonconstant-expression diagnostic is IllFormed. Normalization-time invalid mappings/IFNDR are outside this tree model, not silently false. Constraint fold expressions remain opaque atoms as appropriate to this version; no C++26 fold-expanded ordering is imported. No arbitrary SAT/SMT entailment or full overload resolution is assumed. Tree equality is syntactic in atom identities; satisfaction equivalence is a different relation.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateConstraint"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.constr.atomic",
      "urn:csabs:source/cpp20-n4861-temp.constr.normal",
      "urn:csabs:source/cpp20-n4861-temp.constr.order",
      "urn:csabs:source/cpp20-n4861-temp.constr.op"
    ],
    "sourceLocator": "[temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3",
    "sourceNote": "Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/TemplateConstraint-clause-forms",
      "urn:csabs:axiom/TemplateConstraint-identity-subsumption"
    ],
    "proofSketch": "The conjunction has one DNF clause [a,b], sharing a with the target [a]. In the reverse direction CNF has clauses [a] and [b], and [a] cannot share an identical atom with [b]."
  },
  {
    "id": "urn:csabs:law/TemplateConstraint-false-left-skips-invalid-right",
    "type": "Law",
    "name": "false-left-skips-invalid-right",
    "statement": "sat(P,a)=Unsatisfied ⇒ sat(And(P,Q),a)=Unsatisfied without checking Q, even if evaluating Q separately would be IllFormed.",
    "formalStatement": "sat(P,a)=Unsatisfied ⇒ sat(And(P,Q),a)=Unsatisfied without checking Q, even if evaluating Q separately would be IllFormed.",
    "assumptions": [
      "C++20 N4861 normalized-constraint fragment, after well-formed normalization. Atoms include source-expression appearance and canonical parameter mapping; equal truth values do not identify atoms. Atom substitution invalidity yields Unsatisfied only where the standard permits it; a required non-bool/nonconstant-expression diagnostic is IllFormed. Normalization-time invalid mappings/IFNDR are outside this tree model, not silently false. Constraint fold expressions remain opaque atoms as appropriate to this version; no C++26 fold-expanded ordering is imported. No arbitrary SAT/SMT entailment or full overload resolution is assumed. Tree equality is syntactic in atom identities; satisfaction equivalence is a different relation.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateConstraint"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.constr.atomic",
      "urn:csabs:source/cpp20-n4861-temp.constr.normal",
      "urn:csabs:source/cpp20-n4861-temp.constr.order",
      "urn:csabs:source/cpp20-n4861-temp.constr.op"
    ],
    "sourceLocator": "[temp.constr.atomic] ¶1–3; [temp.constr.normal] ¶1; [temp.constr.order] ¶1; [temp.constr.op] ¶2–3",
    "sourceNote": "Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/TemplateConstraint-short-circuit"
    ],
    "proofSketch": "Apply the first conjunction branch. This is satisfaction short-circuiting after valid normalization, not permission to ignore normalization errors."
  }
]
```
<!-- graph-record:end -->
