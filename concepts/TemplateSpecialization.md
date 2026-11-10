# Class template partial-specialization selection

Selection from matching class-template partial specializations using deduction, constraints and a supplied strict more-specialized relation, with explicit primary and ambiguity outcomes.

**Notation:** S finite; M_Γ(a)={s∈S | deduces(s,a) ∧ satisfied(s,a)}; s≻t means strictly more specialized; select(a)∈Primary⊎Chosen(S)⊎Ambiguous

**Stable ID:** `urn:csabs:concept/TemplateSpecialization`

**Categories:** Programming-language semantics → Generic programming → Template metaprogramming

**Kind:** semantic-model

**Prerequisites:** [Partial Order](PartialOrder.md), [Finite set collection](FiniteSet.md)

**Related concepts:** [Kinded partial template metafunction](TemplateMetafunction.md), [Normalized template constraints with atomic identity](TemplateConstraint.md), [Ordered substitution with immediate-context failure](TemplateSubstitution.md)

## Backlinks

- [Normalized template constraints with atomic identity](TemplateConstraint.md) — `relatedConcept`
- [Kinded partial template metafunction](TemplateMetafunction.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected defining rules: M_Γ(a)={s∈S | deduces(s,a)∧satisfied(s,a)}; S is finite and ≻ is irreflexive and transitive. M=∅ ⇒ select=Primary; M≠∅ ∧ winner(M,s) ⇒ select=Chosen(s); M≠∅ ∧ no winner ⇒ select=Ambiguous. winner(M,s) ⇔ s∈M ∧ ∀t∈M, t≠s ⇒ s≻t.

**basisKind:** extensional-structural-definition

**basisScope:** C++20 N4861 class-template partial-specialization profile. Matching/ordering are supplied by faithful deduction and associated-constraint adapters; accepting a larger set of arguments does not itself establish the standard ordering. ≻ is a strict partial order on declaration identities. Exact explicit specializations, declaration well-formedness, variable templates, function-template overload resolution and body validity are outside this selector. All candidate declarations are fixed and visible in Γ. Selection does not instantiate or validate a body.

**verificationObligation:** Use the stated C++20 N4861 profile and map types, argument equivalence, visibility, definedness and implementation limits explicitly.; Do not infer an entire compiler semantics, decidability, universal termination or executable proof from these selected interfaces.

**reviewStatus:** Editorial source/interface review; model bindings and compiled theorem witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-TemplateSpecialization-matches"></a>

### matches

`urn:csabs:operation/TemplateSpecialization-matches`

**signature:** matches : Γ×Args→𝒫fin(S)

**description:** Collect partial specializations for which deduction succeeds and associated constraints are satisfied.

**precondition:** Typed inputs satisfying the selected profile.

**postcondition:** Collect partial specializations for which deduction succeeds and associated constraints are satisfied.

**totality:** Total mathematical operation on the stated inputs.

**source:** [C++20 working draft N4861 [temp.class.spec.match] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.class.spec.match); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.class.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.class.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.class.spec.match] ¶1–2; [temp.class.order] ¶1, rewrite to function-template ordering

**sourceNote:** Abstracts the standard selection decision after matching. Uses a supplied strict ordering rather than replacing C++ partial ordering with pattern-set inclusion.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-TemplateSpecialization-winner"></a>

### winner

`urn:csabs:operation/TemplateSpecialization-winner`

**signature:** winner : 𝒫fin(S)×S→Prop

**description:** winner(M,s) iff s∈M and s≻t for every other t∈M; a singleton matches vacuously.

**precondition:** Typed inputs satisfying the selected profile.

**postcondition:** winner(M,s) iff s∈M and s≻t for every other t∈M; a singleton matches vacuously.

**totality:** Total mathematical operation on the stated inputs.

**source:** [C++20 working draft N4861 [temp.class.spec.match] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.class.spec.match); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.class.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.class.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.class.spec.match] ¶1–2; [temp.class.order] ¶1, rewrite to function-template ordering

**sourceNote:** Abstracts the standard selection decision after matching. Uses a supplied strict ordering rather than replacing C++ partial ordering with pattern-set inclusion.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-TemplateSpecialization-select"></a>

### select

`urn:csabs:operation/TemplateSpecialization-select`

**signature:** select : Γ×Args→Selection(S)

**description:** Return Primary for M=∅, Chosen(s) for a winner s, otherwise Ambiguous. This total diagnostic classifier is not partial body instantiation.

**precondition:** Typed inputs satisfying the selected profile.

**postcondition:** Return Primary for M=∅, Chosen(s) for a winner s, otherwise Ambiguous. This total diagnostic classifier is not partial body instantiation.

**totality:** Total mathematical operation on the stated inputs.

**source:** [C++20 working draft N4861 [temp.class.spec.match] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.class.spec.match); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.class.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.class.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.class.spec.match] ¶1–2; [temp.class.order] ¶1, rewrite to function-template ordering

**sourceNote:** Abstracts the standard selection decision after matching. Uses a supplied strict ordering rather than replacing C++ partial ordering with pattern-set inclusion.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-TemplateSpecialization-matching"></a>

### matching

`urn:csabs:axiom/TemplateSpecialization-matching`

**statement:** M_Γ(a)={s∈S | deduces(s,a)∧satisfied(s,a)}; S is finite and ≻ is irreflexive and transitive.

**formalStatement:** M_Γ(a)={s∈S | deduces(s,a)∧satisfied(s,a)}; S is finite and ≻ is irreflexive and transitive.

**assumptions:** C++20 N4861 class-template partial-specialization profile. Matching/ordering are supplied by faithful deduction and associated-constraint adapters; accepting a larger set of arguments does not itself establish the standard ordering. ≻ is a strict partial order on declaration identities. Exact explicit specializations, declaration well-formedness, variable templates, function-template overload resolution and body validity are outside this selector. All candidate declarations are fixed and visible in Γ. Selection does not instantiate or validate a body.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.class.spec.match] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.class.spec.match); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.class.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.class.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.class.spec.match] ¶1–2; [temp.class.order] ¶1, rewrite to function-template ordering

**sourceNote:** Abstracts the standard selection decision after matching. Uses a supplied strict ordering rather than replacing C++ partial ordering with pattern-set inclusion.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-TemplateSpecialization-selection"></a>

### selection

`urn:csabs:axiom/TemplateSpecialization-selection`

**statement:** M=∅ ⇒ select=Primary; M≠∅ ∧ winner(M,s) ⇒ select=Chosen(s); M≠∅ ∧ no winner ⇒ select=Ambiguous.

**formalStatement:** M=∅ ⇒ select=Primary; M≠∅ ∧ winner(M,s) ⇒ select=Chosen(s); M≠∅ ∧ no winner ⇒ select=Ambiguous.

**assumptions:** C++20 N4861 class-template partial-specialization profile. Matching/ordering are supplied by faithful deduction and associated-constraint adapters; accepting a larger set of arguments does not itself establish the standard ordering. ≻ is a strict partial order on declaration identities. Exact explicit specializations, declaration well-formedness, variable templates, function-template overload resolution and body validity are outside this selector. All candidate declarations are fixed and visible in Γ. Selection does not instantiate or validate a body.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.class.spec.match] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.class.spec.match); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.class.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.class.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.class.spec.match] ¶1–2; [temp.class.order] ¶1, rewrite to function-template ordering

**sourceNote:** Abstracts the standard selection decision after matching. Uses a supplied strict ordering rather than replacing C++ partial ordering with pattern-set inclusion.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-TemplateSpecialization-winner-definition"></a>

### winner-definition

`urn:csabs:axiom/TemplateSpecialization-winner-definition`

**statement:** winner(M,s) ⇔ s∈M ∧ ∀t∈M, t≠s ⇒ s≻t.

**formalStatement:** winner(M,s) ⇔ s∈M ∧ ∀t∈M, t≠s ⇒ s≻t.

**assumptions:** C++20 N4861 class-template partial-specialization profile. Matching/ordering are supplied by faithful deduction and associated-constraint adapters; accepting a larger set of arguments does not itself establish the standard ordering. ≻ is a strict partial order on declaration identities. Exact explicit specializations, declaration well-formedness, variable templates, function-template overload resolution and body validity are outside this selector. All candidate declarations are fixed and visible in Γ. Selection does not instantiate or validate a body.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.class.spec.match] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.class.spec.match); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.class.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.class.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.class.spec.match] ¶1–2; [temp.class.order] ¶1, rewrite to function-template ordering

**sourceNote:** Abstracts the standard selection decision after matching. Uses a supplied strict ordering rather than replacing C++ partial ordering with pattern-set inclusion.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-TemplateSpecialization-unique-winner"></a>

### unique-winner

`urn:csabs:law/TemplateSpecialization-unique-winner`

**statement:** winner(M,s) ∧ winner(M,t) ⇒ s=t.

**formalStatement:** winner(M,s) ∧ winner(M,t) ⇒ s=t.

**assumptions:** C++20 N4861 class-template partial-specialization profile. Matching/ordering are supplied by faithful deduction and associated-constraint adapters; accepting a larger set of arguments does not itself establish the standard ordering. ≻ is a strict partial order on declaration identities. Exact explicit specializations, declaration well-formedness, variable templates, function-template overload resolution and body validity are outside this selector. All candidate declarations are fixed and visible in Γ. Selection does not instantiate or validate a body.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.class.spec.match] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.class.spec.match); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.class.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.class.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.class.spec.match] ¶1–2; [temp.class.order] ¶1, rewrite to function-template ordering

**sourceNote:** Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.

**provenanceKind:** derived

**dependsOn:** [matching](TemplateSpecialization.md#node-urn-csabs-axiom-TemplateSpecialization-matching); [winner-definition](TemplateSpecialization.md#node-urn-csabs-axiom-TemplateSpecialization-winner-definition)

**proofSketch:** If distinct winners existed, each would strictly dominate the other. Transitivity would give s≻s, contradicting irreflexivity.

<a id="node-urn-csabs-law-TemplateSpecialization-incomparable-ambiguity"></a>

### incomparable-ambiguity

`urn:csabs:law/TemplateSpecialization-incomparable-ambiguity`

**statement:** M={s,t} ∧ s≠t ∧ ¬(s≻t) ∧ ¬(t≻s) ⇒ select=Ambiguous.

**formalStatement:** M={s,t} ∧ s≠t ∧ ¬(s≻t) ∧ ¬(t≻s) ⇒ select=Ambiguous.

**assumptions:** C++20 N4861 class-template partial-specialization profile. Matching/ordering are supplied by faithful deduction and associated-constraint adapters; accepting a larger set of arguments does not itself establish the standard ordering. ≻ is a strict partial order on declaration identities. Exact explicit specializations, declaration well-formedness, variable templates, function-template overload resolution and body validity are outside this selector. All candidate declarations are fixed and visible in Γ. Selection does not instantiate or validate a body.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.class.spec.match] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.class.spec.match); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.class.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.class.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.class.spec.match] ¶1–2; [temp.class.order] ¶1, rewrite to function-template ordering

**sourceNote:** Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.

**provenanceKind:** derived

**dependsOn:** [selection](TemplateSpecialization.md#node-urn-csabs-axiom-TemplateSpecialization-selection); [winner-definition](TemplateSpecialization.md#node-urn-csabs-axiom-TemplateSpecialization-winner-definition)

**proofSketch:** Neither member can dominate the other, so the nonempty matching set has no winner. Apply the ambiguity branch.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [C++20 working draft N4861 [temp.class.spec.match] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.class.spec.match); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause
- [C++20 working draft N4861 [temp.class.order] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.class.order); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.class.spec.match] ¶1–2; [temp.class.order] ¶1, rewrite to function-template ordering

**sourceNote:** Abstracts the standard selection decision after matching. Uses a supplied strict ordering rather than replacing C++ partial ordering with pattern-set inclusion.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/TemplateSpecialization",
    "type": "Concept",
    "shortForm": "TemplateSpecialization",
    "fullName": "Class template partial-specialization selection",
    "definition": "Selection from matching class-template partial specializations using deduction, constraints and a supplied strict more-specialized relation, with explicit primary and ambiguity outcomes.",
    "notation": "S finite; M_Γ(a)={s∈S | deduces(s,a) ∧ satisfied(s,a)}; s≻t means strictly more specialized; select(a)∈Primary⊎Chosen(S)⊎Ambiguous",
    "category": [
      "urn:csabs:category/template-metaprogramming"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/PartialOrder",
      "urn:csabs:concept/FiniteSet"
    ],
    "relatedConcept": [
      "urn:csabs:concept/TemplateMetafunction",
      "urn:csabs:concept/TemplateConstraint",
      "urn:csabs:concept/TemplateSubstitution"
    ],
    "hasOperation": [
      "urn:csabs:operation/TemplateSpecialization-matches",
      "urn:csabs:operation/TemplateSpecialization-winner",
      "urn:csabs:operation/TemplateSpecialization-select"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/TemplateSpecialization-matching",
      "urn:csabs:axiom/TemplateSpecialization-selection",
      "urn:csabs:axiom/TemplateSpecialization-winner-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/TemplateSpecialization-unique-winner",
      "urn:csabs:law/TemplateSpecialization-incomparable-ambiguity"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "C++20 N4861 class-template partial-specialization profile. Matching/ordering are supplied by faithful deduction and associated-constraint adapters; accepting a larger set of arguments does not itself establish the standard ordering. ≻ is a strict partial order on declaration identities. Exact explicit specializations, declaration well-formedness, variable templates, function-template overload resolution and body validity are outside this selector. All candidate declarations are fixed and visible in Γ. Selection does not instantiate or validate a body.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; model bindings and compiled theorem witnesses are separate.",
    "verificationObligation": [
      "Use the stated C++20 N4861 profile and map types, argument equivalence, visibility, definedness and implementation limits explicitly.",
      "Do not infer an entire compiler semantics, decidability, universal termination or executable proof from these selected interfaces."
    ],
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.class.spec.match",
      "urn:csabs:source/cpp20-n4861-temp.class.order"
    ],
    "sourceLocator": "[temp.class.spec.match] ¶1–2; [temp.class.order] ¶1, rewrite to function-template ordering",
    "sourceNote": "Abstracts the standard selection decision after matching. Uses a supplied strict ordering rather than replacing C++ partial ordering with pattern-set inclusion.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: M_Γ(a)={s∈S | deduces(s,a)∧satisfied(s,a)}; S is finite and ≻ is irreflexive and transitive. M=∅ ⇒ select=Primary; M≠∅ ∧ winner(M,s) ⇒ select=Chosen(s); M≠∅ ∧ no winner ⇒ select=Ambiguous. winner(M,s) ⇔ s∈M ∧ ∀t∈M, t≠s ⇒ s≻t."
  },
  {
    "id": "urn:csabs:operation/TemplateSpecialization-matches",
    "type": "Operation",
    "name": "matches",
    "signature": "matches : Γ×Args→𝒫fin(S)",
    "description": "Collect partial specializations for which deduction succeeds and associated constraints are satisfied.",
    "concept": "urn:csabs:concept/TemplateSpecialization",
    "precondition": "Typed inputs satisfying the selected profile.",
    "postcondition": "Collect partial specializations for which deduction succeeds and associated constraints are satisfied.",
    "totality": "Total mathematical operation on the stated inputs.",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.class.spec.match",
      "urn:csabs:source/cpp20-n4861-temp.class.order"
    ],
    "sourceLocator": "[temp.class.spec.match] ¶1–2; [temp.class.order] ¶1, rewrite to function-template ordering",
    "sourceNote": "Abstracts the standard selection decision after matching. Uses a supplied strict ordering rather than replacing C++ partial ordering with pattern-set inclusion.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/TemplateSpecialization-winner",
    "type": "Operation",
    "name": "winner",
    "signature": "winner : 𝒫fin(S)×S→Prop",
    "description": "winner(M,s) iff s∈M and s≻t for every other t∈M; a singleton matches vacuously.",
    "concept": "urn:csabs:concept/TemplateSpecialization",
    "precondition": "Typed inputs satisfying the selected profile.",
    "postcondition": "winner(M,s) iff s∈M and s≻t for every other t∈M; a singleton matches vacuously.",
    "totality": "Total mathematical operation on the stated inputs.",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.class.spec.match",
      "urn:csabs:source/cpp20-n4861-temp.class.order"
    ],
    "sourceLocator": "[temp.class.spec.match] ¶1–2; [temp.class.order] ¶1, rewrite to function-template ordering",
    "sourceNote": "Abstracts the standard selection decision after matching. Uses a supplied strict ordering rather than replacing C++ partial ordering with pattern-set inclusion.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/TemplateSpecialization-select",
    "type": "Operation",
    "name": "select",
    "signature": "select : Γ×Args→Selection(S)",
    "description": "Return Primary for M=∅, Chosen(s) for a winner s, otherwise Ambiguous. This total diagnostic classifier is not partial body instantiation.",
    "concept": "urn:csabs:concept/TemplateSpecialization",
    "precondition": "Typed inputs satisfying the selected profile.",
    "postcondition": "Return Primary for M=∅, Chosen(s) for a winner s, otherwise Ambiguous. This total diagnostic classifier is not partial body instantiation.",
    "totality": "Total mathematical operation on the stated inputs.",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.class.spec.match",
      "urn:csabs:source/cpp20-n4861-temp.class.order"
    ],
    "sourceLocator": "[temp.class.spec.match] ¶1–2; [temp.class.order] ¶1, rewrite to function-template ordering",
    "sourceNote": "Abstracts the standard selection decision after matching. Uses a supplied strict ordering rather than replacing C++ partial ordering with pattern-set inclusion.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/TemplateSpecialization-matching",
    "type": "Axiom",
    "name": "matching",
    "statement": "M_Γ(a)={s∈S | deduces(s,a)∧satisfied(s,a)}; S is finite and ≻ is irreflexive and transitive.",
    "formalStatement": "M_Γ(a)={s∈S | deduces(s,a)∧satisfied(s,a)}; S is finite and ≻ is irreflexive and transitive.",
    "assumptions": [
      "C++20 N4861 class-template partial-specialization profile. Matching/ordering are supplied by faithful deduction and associated-constraint adapters; accepting a larger set of arguments does not itself establish the standard ordering. ≻ is a strict partial order on declaration identities. Exact explicit specializations, declaration well-formedness, variable templates, function-template overload resolution and body validity are outside this selector. All candidate declarations are fixed and visible in Γ. Selection does not instantiate or validate a body.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateSpecialization"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.class.spec.match",
      "urn:csabs:source/cpp20-n4861-temp.class.order"
    ],
    "sourceLocator": "[temp.class.spec.match] ¶1–2; [temp.class.order] ¶1, rewrite to function-template ordering",
    "sourceNote": "Abstracts the standard selection decision after matching. Uses a supplied strict ordering rather than replacing C++ partial ordering with pattern-set inclusion.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/TemplateSpecialization-selection",
    "type": "Axiom",
    "name": "selection",
    "statement": "M=∅ ⇒ select=Primary; M≠∅ ∧ winner(M,s) ⇒ select=Chosen(s); M≠∅ ∧ no winner ⇒ select=Ambiguous.",
    "formalStatement": "M=∅ ⇒ select=Primary; M≠∅ ∧ winner(M,s) ⇒ select=Chosen(s); M≠∅ ∧ no winner ⇒ select=Ambiguous.",
    "assumptions": [
      "C++20 N4861 class-template partial-specialization profile. Matching/ordering are supplied by faithful deduction and associated-constraint adapters; accepting a larger set of arguments does not itself establish the standard ordering. ≻ is a strict partial order on declaration identities. Exact explicit specializations, declaration well-formedness, variable templates, function-template overload resolution and body validity are outside this selector. All candidate declarations are fixed and visible in Γ. Selection does not instantiate or validate a body.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateSpecialization"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.class.spec.match",
      "urn:csabs:source/cpp20-n4861-temp.class.order"
    ],
    "sourceLocator": "[temp.class.spec.match] ¶1–2; [temp.class.order] ¶1, rewrite to function-template ordering",
    "sourceNote": "Abstracts the standard selection decision after matching. Uses a supplied strict ordering rather than replacing C++ partial ordering with pattern-set inclusion.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/TemplateSpecialization-winner-definition",
    "type": "Axiom",
    "name": "winner-definition",
    "statement": "winner(M,s) ⇔ s∈M ∧ ∀t∈M, t≠s ⇒ s≻t.",
    "formalStatement": "winner(M,s) ⇔ s∈M ∧ ∀t∈M, t≠s ⇒ s≻t.",
    "assumptions": [
      "C++20 N4861 class-template partial-specialization profile. Matching/ordering are supplied by faithful deduction and associated-constraint adapters; accepting a larger set of arguments does not itself establish the standard ordering. ≻ is a strict partial order on declaration identities. Exact explicit specializations, declaration well-formedness, variable templates, function-template overload resolution and body validity are outside this selector. All candidate declarations are fixed and visible in Γ. Selection does not instantiate or validate a body.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateSpecialization"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.class.spec.match",
      "urn:csabs:source/cpp20-n4861-temp.class.order"
    ],
    "sourceLocator": "[temp.class.spec.match] ¶1–2; [temp.class.order] ¶1, rewrite to function-template ordering",
    "sourceNote": "Abstracts the standard selection decision after matching. Uses a supplied strict ordering rather than replacing C++ partial ordering with pattern-set inclusion.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/TemplateSpecialization-unique-winner",
    "type": "Law",
    "name": "unique-winner",
    "statement": "winner(M,s) ∧ winner(M,t) ⇒ s=t.",
    "formalStatement": "winner(M,s) ∧ winner(M,t) ⇒ s=t.",
    "assumptions": [
      "C++20 N4861 class-template partial-specialization profile. Matching/ordering are supplied by faithful deduction and associated-constraint adapters; accepting a larger set of arguments does not itself establish the standard ordering. ≻ is a strict partial order on declaration identities. Exact explicit specializations, declaration well-formedness, variable templates, function-template overload resolution and body validity are outside this selector. All candidate declarations are fixed and visible in Γ. Selection does not instantiate or validate a body.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateSpecialization"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.class.spec.match",
      "urn:csabs:source/cpp20-n4861-temp.class.order"
    ],
    "sourceLocator": "[temp.class.spec.match] ¶1–2; [temp.class.order] ¶1, rewrite to function-template ordering",
    "sourceNote": "Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/TemplateSpecialization-matching",
      "urn:csabs:axiom/TemplateSpecialization-winner-definition"
    ],
    "proofSketch": "If distinct winners existed, each would strictly dominate the other. Transitivity would give s≻s, contradicting irreflexivity."
  },
  {
    "id": "urn:csabs:law/TemplateSpecialization-incomparable-ambiguity",
    "type": "Law",
    "name": "incomparable-ambiguity",
    "statement": "M={s,t} ∧ s≠t ∧ ¬(s≻t) ∧ ¬(t≻s) ⇒ select=Ambiguous.",
    "formalStatement": "M={s,t} ∧ s≠t ∧ ¬(s≻t) ∧ ¬(t≻s) ⇒ select=Ambiguous.",
    "assumptions": [
      "C++20 N4861 class-template partial-specialization profile. Matching/ordering are supplied by faithful deduction and associated-constraint adapters; accepting a larger set of arguments does not itself establish the standard ordering. ≻ is a strict partial order on declaration identities. Exact explicit specializations, declaration well-formedness, variable templates, function-template overload resolution and body validity are outside this selector. All candidate declarations are fixed and visible in Γ. Selection does not instantiate or validate a body.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateSpecialization"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.class.spec.match",
      "urn:csabs:source/cpp20-n4861-temp.class.order"
    ],
    "sourceLocator": "[temp.class.spec.match] ¶1–2; [temp.class.order] ¶1, rewrite to function-template ordering",
    "sourceNote": "Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/TemplateSpecialization-selection",
      "urn:csabs:axiom/TemplateSpecialization-winner-definition"
    ],
    "proofSketch": "Neither member can dominate the other, so the nonempty matching set has no winner. Apply the ambiguity branch."
  }
]
```
<!-- graph-record:end -->
