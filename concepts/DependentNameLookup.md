# Definition/instantiation lookup for dependent calls

A staged candidate-set model for dependent unqualified function calls, keeping ordinary definition-context lookup separate from admissible argument-dependent lookup at definition and instantiation.

**Notation:** ΓD definition context; ΓI instantiation context; OrdD(name)⊆Decl; ADLD(name,args),ADLI(name,args)⊆Decl; candidates=OrdD∪ADLD∪ADLI when ADL is enabled

**Stable ID:** `urn:csabs:concept/DependentNameLookup`

**Categories:** Programming-language semantics → Generic programming → Template metaprogramming

**Kind:** semantic-model

**Prerequisites:** [Finite set collection](FiniteSet.md), [Binary relation](Relation.md)

**Related concepts:** [Single-inheritance class table and dynamic dispatch](ClassTable.md), [Kinded partial template metafunction](TemplateMetafunction.md), [Ordered substitution with immediate-context failure](TemplateSubstitution.md)

## Interface and scope

**axiomBasis:** Selected defining rules: Nondependent bindings and the ordinary part of dependent unqualified-call lookup use ΓD, not an additional ordinary lookup in ΓI. candidates(O,D,I,true)=O∪D∪I; candidates(O,D,I,false)=O; D and I contain only declarations admitted by the standard ADL rules for the selected call.

**basisKind:** extensional-structural-definition

**basisScope:** C++20 N4861 selected unqualified-call profile after dependency classification. Ordinary candidates are frozen from the definition context; ADL eligibility, associated entities, visibility/reachability and permitted contexts are supplied by a faithful frontend. If ordinary lookup suppresses ADL, only OrdD is used. Nondependent names are bound by definition-context lookup. Qualified/member lookup, current instantiation and unknown-specialization rules, modules and cross-translation-unit consistency/undefined behavior are outside this reduced model. Candidate-set formation is not deduction, overload ranking or execution. Declaration identity, not name spelling, defines set equality.

**verificationObligation:** Use the stated C++20 N4861 profile and map types, argument equivalence, visibility, definedness and implementation limits explicitly.; Do not infer an entire compiler semantics, decidability, universal termination or executable proof from these selected interfaces.

**reviewStatus:** Editorial source/interface review; model bindings and compiled theorem witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-DependentNameLookup-bind-nondependent"></a>

### bind-nondependent

`urn:csabs:operation/DependentNameLookup-bind-nondependent`

**signature:** bindNondependent : ΓD×Name→𝒫fin(Decl)

**description:** Return the supplied definition-context binding/candidate set; ΓI does not rebind it.

**precondition:** Typed inputs satisfying the selected profile.

**postcondition:** Return the supplied definition-context binding/candidate set; ΓI does not rebind it.

**totality:** Total mathematical operation on the stated inputs.

**source:** [C++20 working draft N4861 [temp.dep.candidate] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.dep.candidate); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.res] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.res); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.dep.candidate] ¶1, definition-context lookup and instantiation-context ADL; [temp.res], name dependency and resolution

**sourceNote:** Separates supplied lookup candidate sets and an ADL-enable guard. It does not claim that every later declaration is visible or that the union alone chooses a call target.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DependentNameLookup-dependent-candidates"></a>

### dependent-candidates

`urn:csabs:operation/DependentNameLookup-dependent-candidates`

**signature:** dependentCandidates : OrdD×ADLD×ADLI×Bool→𝒫fin(Decl)

**description:** If the ADL-enable guard is true, return OrdD∪ADLD∪ADLI; otherwise return OrdD.

**precondition:** Typed inputs satisfying the selected profile.

**postcondition:** If the ADL-enable guard is true, return OrdD∪ADLD∪ADLI; otherwise return OrdD.

**totality:** Total mathematical operation on the stated inputs.

**source:** [C++20 working draft N4861 [temp.dep.candidate] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.dep.candidate); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.res] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.res); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.dep.candidate] ¶1, definition-context lookup and instantiation-context ADL; [temp.res], name dependency and resolution

**sourceNote:** Separates supplied lookup candidate sets and an ADL-enable guard. It does not claim that every later declaration is visible or that the union alone chooses a call target.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DependentNameLookup-definition-binding"></a>

### definition-binding

`urn:csabs:axiom/DependentNameLookup-definition-binding`

**statement:** Nondependent bindings and the ordinary part of dependent unqualified-call lookup use ΓD, not an additional ordinary lookup in ΓI.

**formalStatement:** Nondependent bindings and the ordinary part of dependent unqualified-call lookup use ΓD, not an additional ordinary lookup in ΓI.

**assumptions:** C++20 N4861 selected unqualified-call profile after dependency classification. Ordinary candidates are frozen from the definition context; ADL eligibility, associated entities, visibility/reachability and permitted contexts are supplied by a faithful frontend. If ordinary lookup suppresses ADL, only OrdD is used. Nondependent names are bound by definition-context lookup. Qualified/member lookup, current instantiation and unknown-specialization rules, modules and cross-translation-unit consistency/undefined behavior are outside this reduced model. Candidate-set formation is not deduction, overload ranking or execution. Declaration identity, not name spelling, defines set equality.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.dep.candidate] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.dep.candidate); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.res] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.res); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.dep.candidate] ¶1, definition-context lookup and instantiation-context ADL; [temp.res], name dependency and resolution

**sourceNote:** Separates supplied lookup candidate sets and an ADL-enable guard. It does not claim that every later declaration is visible or that the union alone chooses a call target.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-DependentNameLookup-guarded-adl-union"></a>

### guarded-adl-union

`urn:csabs:axiom/DependentNameLookup-guarded-adl-union`

**statement:** candidates(O,D,I,true)=O∪D∪I; candidates(O,D,I,false)=O; D and I contain only declarations admitted by the standard ADL rules for the selected call.

**formalStatement:** candidates(O,D,I,true)=O∪D∪I; candidates(O,D,I,false)=O; D and I contain only declarations admitted by the standard ADL rules for the selected call.

**assumptions:** C++20 N4861 selected unqualified-call profile after dependency classification. Ordinary candidates are frozen from the definition context; ADL eligibility, associated entities, visibility/reachability and permitted contexts are supplied by a faithful frontend. If ordinary lookup suppresses ADL, only OrdD is used. Nondependent names are bound by definition-context lookup. Qualified/member lookup, current instantiation and unknown-specialization rules, modules and cross-translation-unit consistency/undefined behavior are outside this reduced model. Candidate-set formation is not deduction, overload ranking or execution. Declaration identity, not name spelling, defines set equality.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.dep.candidate] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.dep.candidate); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.res] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.res); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.dep.candidate] ¶1, definition-context lookup and instantiation-context ADL; [temp.res], name dependency and resolution

**sourceNote:** Separates supplied lookup candidate sets and an ADL-enable guard. It does not claim that every later declaration is visible or that the union alone chooses a call target.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-DependentNameLookup-later-ordinary-declaration-irrelevance"></a>

### later-ordinary-declaration-irrelevance

`urn:csabs:law/DependentNameLookup-later-ordinary-declaration-irrelevance`

**statement:** Keeping O,D,I and ADL eligibility fixed, adding declarations only to ordinary ΓI lookup does not change candidates.

**formalStatement:** Keeping O,D,I and ADL eligibility fixed, adding declarations only to ordinary ΓI lookup does not change candidates.

**assumptions:** C++20 N4861 selected unqualified-call profile after dependency classification. Ordinary candidates are frozen from the definition context; ADL eligibility, associated entities, visibility/reachability and permitted contexts are supplied by a faithful frontend. If ordinary lookup suppresses ADL, only OrdD is used. Nondependent names are bound by definition-context lookup. Qualified/member lookup, current instantiation and unknown-specialization rules, modules and cross-translation-unit consistency/undefined behavior are outside this reduced model. Candidate-set formation is not deduction, overload ranking or execution. Declaration identity, not name spelling, defines set equality.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.dep.candidate] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.dep.candidate); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.res] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.res); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.dep.candidate] ¶1, definition-context lookup and instantiation-context ADL; [temp.res], name dependency and resolution

**sourceNote:** Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.

**provenanceKind:** derived

**dependsOn:** [definition-binding](DependentNameLookup.md#node-urn-csabs-axiom-DependentNameLookup-definition-binding); [guarded-adl-union](DependentNameLookup.md#node-urn-csabs-axiom-DependentNameLookup-guarded-adl-union)

**proofSketch:** The ordinary ΓI set is not an input to either candidate equation. This does not cover declarations that also become admissible ADL candidates.

<a id="node-urn-csabs-law-DependentNameLookup-adl-disabled"></a>

### adl-disabled

`urn:csabs:law/DependentNameLookup-adl-disabled`

**statement:** candidates(O,D,I,false)=O for any D,I; no instantiation-context ADL candidate is added.

**formalStatement:** candidates(O,D,I,false)=O for any D,I; no instantiation-context ADL candidate is added.

**assumptions:** C++20 N4861 selected unqualified-call profile after dependency classification. Ordinary candidates are frozen from the definition context; ADL eligibility, associated entities, visibility/reachability and permitted contexts are supplied by a faithful frontend. If ordinary lookup suppresses ADL, only OrdD is used. Nondependent names are bound by definition-context lookup. Qualified/member lookup, current instantiation and unknown-specialization rules, modules and cross-translation-unit consistency/undefined behavior are outside this reduced model. Candidate-set formation is not deduction, overload ranking or execution. Declaration identity, not name spelling, defines set equality.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.dep.candidate] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.dep.candidate); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.res] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.res); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.dep.candidate] ¶1, definition-context lookup and instantiation-context ADL; [temp.res], name dependency and resolution

**sourceNote:** Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.

**provenanceKind:** derived

**dependsOn:** [guarded-adl-union](DependentNameLookup.md#node-urn-csabs-axiom-DependentNameLookup-guarded-adl-union)

**proofSketch:** Instantiate the false-guard branch. No assertion about later deduction or overload selection follows.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [C++20 working draft N4861 [temp.dep.candidate] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.dep.candidate); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause
- [C++20 working draft N4861 [temp.res] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.res); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.dep.candidate] ¶1, definition-context lookup and instantiation-context ADL; [temp.res], name dependency and resolution

**sourceNote:** Separates supplied lookup candidate sets and an ADL-enable guard. It does not claim that every later declaration is visible or that the union alone chooses a call target.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/DependentNameLookup",
    "type": "Concept",
    "shortForm": "DependentNameLookup",
    "fullName": "Definition/instantiation lookup for dependent calls",
    "definition": "A staged candidate-set model for dependent unqualified function calls, keeping ordinary definition-context lookup separate from admissible argument-dependent lookup at definition and instantiation.",
    "notation": "ΓD definition context; ΓI instantiation context; OrdD(name)⊆Decl; ADLD(name,args),ADLI(name,args)⊆Decl; candidates=OrdD∪ADLD∪ADLI when ADL is enabled",
    "category": [
      "urn:csabs:category/template-metaprogramming"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/FiniteSet",
      "urn:csabs:concept/Relation"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ClassTable",
      "urn:csabs:concept/TemplateMetafunction",
      "urn:csabs:concept/TemplateSubstitution"
    ],
    "hasOperation": [
      "urn:csabs:operation/DependentNameLookup-bind-nondependent",
      "urn:csabs:operation/DependentNameLookup-dependent-candidates"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DependentNameLookup-definition-binding",
      "urn:csabs:axiom/DependentNameLookup-guarded-adl-union"
    ],
    "hasLaw": [
      "urn:csabs:law/DependentNameLookup-later-ordinary-declaration-irrelevance",
      "urn:csabs:law/DependentNameLookup-adl-disabled"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "C++20 N4861 selected unqualified-call profile after dependency classification. Ordinary candidates are frozen from the definition context; ADL eligibility, associated entities, visibility/reachability and permitted contexts are supplied by a faithful frontend. If ordinary lookup suppresses ADL, only OrdD is used. Nondependent names are bound by definition-context lookup. Qualified/member lookup, current instantiation and unknown-specialization rules, modules and cross-translation-unit consistency/undefined behavior are outside this reduced model. Candidate-set formation is not deduction, overload ranking or execution. Declaration identity, not name spelling, defines set equality.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; model bindings and compiled theorem witnesses are separate.",
    "verificationObligation": [
      "Use the stated C++20 N4861 profile and map types, argument equivalence, visibility, definedness and implementation limits explicitly.",
      "Do not infer an entire compiler semantics, decidability, universal termination or executable proof from these selected interfaces."
    ],
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.dep.candidate",
      "urn:csabs:source/cpp20-n4861-temp.res"
    ],
    "sourceLocator": "[temp.dep.candidate] ¶1, definition-context lookup and instantiation-context ADL; [temp.res], name dependency and resolution",
    "sourceNote": "Separates supplied lookup candidate sets and an ADL-enable guard. It does not claim that every later declaration is visible or that the union alone chooses a call target.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: Nondependent bindings and the ordinary part of dependent unqualified-call lookup use ΓD, not an additional ordinary lookup in ΓI. candidates(O,D,I,true)=O∪D∪I; candidates(O,D,I,false)=O; D and I contain only declarations admitted by the standard ADL rules for the selected call."
  },
  {
    "id": "urn:csabs:operation/DependentNameLookup-bind-nondependent",
    "type": "Operation",
    "name": "bind-nondependent",
    "signature": "bindNondependent : ΓD×Name→𝒫fin(Decl)",
    "description": "Return the supplied definition-context binding/candidate set; ΓI does not rebind it.",
    "concept": "urn:csabs:concept/DependentNameLookup",
    "precondition": "Typed inputs satisfying the selected profile.",
    "postcondition": "Return the supplied definition-context binding/candidate set; ΓI does not rebind it.",
    "totality": "Total mathematical operation on the stated inputs.",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.dep.candidate",
      "urn:csabs:source/cpp20-n4861-temp.res"
    ],
    "sourceLocator": "[temp.dep.candidate] ¶1, definition-context lookup and instantiation-context ADL; [temp.res], name dependency and resolution",
    "sourceNote": "Separates supplied lookup candidate sets and an ADL-enable guard. It does not claim that every later declaration is visible or that the union alone chooses a call target.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DependentNameLookup-dependent-candidates",
    "type": "Operation",
    "name": "dependent-candidates",
    "signature": "dependentCandidates : OrdD×ADLD×ADLI×Bool→𝒫fin(Decl)",
    "description": "If the ADL-enable guard is true, return OrdD∪ADLD∪ADLI; otherwise return OrdD.",
    "concept": "urn:csabs:concept/DependentNameLookup",
    "precondition": "Typed inputs satisfying the selected profile.",
    "postcondition": "If the ADL-enable guard is true, return OrdD∪ADLD∪ADLI; otherwise return OrdD.",
    "totality": "Total mathematical operation on the stated inputs.",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.dep.candidate",
      "urn:csabs:source/cpp20-n4861-temp.res"
    ],
    "sourceLocator": "[temp.dep.candidate] ¶1, definition-context lookup and instantiation-context ADL; [temp.res], name dependency and resolution",
    "sourceNote": "Separates supplied lookup candidate sets and an ADL-enable guard. It does not claim that every later declaration is visible or that the union alone chooses a call target.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DependentNameLookup-definition-binding",
    "type": "Axiom",
    "name": "definition-binding",
    "statement": "Nondependent bindings and the ordinary part of dependent unqualified-call lookup use ΓD, not an additional ordinary lookup in ΓI.",
    "formalStatement": "Nondependent bindings and the ordinary part of dependent unqualified-call lookup use ΓD, not an additional ordinary lookup in ΓI.",
    "assumptions": [
      "C++20 N4861 selected unqualified-call profile after dependency classification. Ordinary candidates are frozen from the definition context; ADL eligibility, associated entities, visibility/reachability and permitted contexts are supplied by a faithful frontend. If ordinary lookup suppresses ADL, only OrdD is used. Nondependent names are bound by definition-context lookup. Qualified/member lookup, current instantiation and unknown-specialization rules, modules and cross-translation-unit consistency/undefined behavior are outside this reduced model. Candidate-set formation is not deduction, overload ranking or execution. Declaration identity, not name spelling, defines set equality.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/DependentNameLookup"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.dep.candidate",
      "urn:csabs:source/cpp20-n4861-temp.res"
    ],
    "sourceLocator": "[temp.dep.candidate] ¶1, definition-context lookup and instantiation-context ADL; [temp.res], name dependency and resolution",
    "sourceNote": "Separates supplied lookup candidate sets and an ADL-enable guard. It does not claim that every later declaration is visible or that the union alone chooses a call target.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/DependentNameLookup-guarded-adl-union",
    "type": "Axiom",
    "name": "guarded-adl-union",
    "statement": "candidates(O,D,I,true)=O∪D∪I; candidates(O,D,I,false)=O; D and I contain only declarations admitted by the standard ADL rules for the selected call.",
    "formalStatement": "candidates(O,D,I,true)=O∪D∪I; candidates(O,D,I,false)=O; D and I contain only declarations admitted by the standard ADL rules for the selected call.",
    "assumptions": [
      "C++20 N4861 selected unqualified-call profile after dependency classification. Ordinary candidates are frozen from the definition context; ADL eligibility, associated entities, visibility/reachability and permitted contexts are supplied by a faithful frontend. If ordinary lookup suppresses ADL, only OrdD is used. Nondependent names are bound by definition-context lookup. Qualified/member lookup, current instantiation and unknown-specialization rules, modules and cross-translation-unit consistency/undefined behavior are outside this reduced model. Candidate-set formation is not deduction, overload ranking or execution. Declaration identity, not name spelling, defines set equality.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/DependentNameLookup"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.dep.candidate",
      "urn:csabs:source/cpp20-n4861-temp.res"
    ],
    "sourceLocator": "[temp.dep.candidate] ¶1, definition-context lookup and instantiation-context ADL; [temp.res], name dependency and resolution",
    "sourceNote": "Separates supplied lookup candidate sets and an ADL-enable guard. It does not claim that every later declaration is visible or that the union alone chooses a call target.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/DependentNameLookup-later-ordinary-declaration-irrelevance",
    "type": "Law",
    "name": "later-ordinary-declaration-irrelevance",
    "statement": "Keeping O,D,I and ADL eligibility fixed, adding declarations only to ordinary ΓI lookup does not change candidates.",
    "formalStatement": "Keeping O,D,I and ADL eligibility fixed, adding declarations only to ordinary ΓI lookup does not change candidates.",
    "assumptions": [
      "C++20 N4861 selected unqualified-call profile after dependency classification. Ordinary candidates are frozen from the definition context; ADL eligibility, associated entities, visibility/reachability and permitted contexts are supplied by a faithful frontend. If ordinary lookup suppresses ADL, only OrdD is used. Nondependent names are bound by definition-context lookup. Qualified/member lookup, current instantiation and unknown-specialization rules, modules and cross-translation-unit consistency/undefined behavior are outside this reduced model. Candidate-set formation is not deduction, overload ranking or execution. Declaration identity, not name spelling, defines set equality.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/DependentNameLookup"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.dep.candidate",
      "urn:csabs:source/cpp20-n4861-temp.res"
    ],
    "sourceLocator": "[temp.dep.candidate] ¶1, definition-context lookup and instantiation-context ADL; [temp.res], name dependency and resolution",
    "sourceNote": "Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/DependentNameLookup-definition-binding",
      "urn:csabs:axiom/DependentNameLookup-guarded-adl-union"
    ],
    "proofSketch": "The ordinary ΓI set is not an input to either candidate equation. This does not cover declarations that also become admissible ADL candidates."
  },
  {
    "id": "urn:csabs:law/DependentNameLookup-adl-disabled",
    "type": "Law",
    "name": "adl-disabled",
    "statement": "candidates(O,D,I,false)=O for any D,I; no instantiation-context ADL candidate is added.",
    "formalStatement": "candidates(O,D,I,false)=O for any D,I; no instantiation-context ADL candidate is added.",
    "assumptions": [
      "C++20 N4861 selected unqualified-call profile after dependency classification. Ordinary candidates are frozen from the definition context; ADL eligibility, associated entities, visibility/reachability and permitted contexts are supplied by a faithful frontend. If ordinary lookup suppresses ADL, only OrdD is used. Nondependent names are bound by definition-context lookup. Qualified/member lookup, current instantiation and unknown-specialization rules, modules and cross-translation-unit consistency/undefined behavior are outside this reduced model. Candidate-set formation is not deduction, overload ranking or execution. Declaration identity, not name spelling, defines set equality.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/DependentNameLookup"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.dep.candidate",
      "urn:csabs:source/cpp20-n4861-temp.res"
    ],
    "sourceLocator": "[temp.dep.candidate] ¶1, definition-context lookup and instantiation-context ADL; [temp.res], name dependency and resolution",
    "sourceNote": "Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/DependentNameLookup-guarded-adl-union"
    ],
    "proofSketch": "Instantiate the false-guard branch. No assertion about later deduction or overload selection follows."
  }
]
```
<!-- graph-record:end -->
