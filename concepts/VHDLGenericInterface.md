# VHDL generic interfaces and whole-formal association

Finite VHDL generic interfaces with constant/type/subprogram/package formals and a checked normalization of positional or named whole-formal associations.

**Notation:** Kind={Constant,Type,Subprogram,Package}; Assoc=Positional(actual)⊎Named(formal,actual); normalizeΣ:Seq(Assoc)⇀ActualSlots

**Stable ID:** `urn:csabs:concept/VHDLGenericInterface`

**Categories:** Programming-language semantics → Generic programming → VHDL generics

**Kind:** semantic-model

**Prerequisites:** [Finite kinded generic parameter signature](GenericSignature.md), [Resolved generic argument binding with ordered defaults](GenericArgumentBinding.md)

**Related concepts:** [VHDL generic elaboration and static structural generation](VHDLGenericElaboration.md), [Kinded partial template metafunction](TemplateMetafunction.md)

## Backlinks

- [Resolved generic argument binding with ordered defaults](GenericArgumentBinding.md) — `relatedConcept`
- [Finite kinded generic parameter signature](GenericSignature.md) — `relatedConcept`
- [VHDL generic elaboration and static structural generation](VHDLGenericElaboration.md) — `requiresConcept`

## Mathematical formulation

A VHDL generic interface is a distinct-name signature with kinds {constant,type,subprogram,package}, compatibility predicates and default permissions. Association normalization maps actuals to formal indices, rejects duplicates/unknown names/out-of-range positions, and forbids positional associations after a named association. Language conformance remains a supplied predicate.

**Lean formulation** (in its source module context):

```lean
structure VHDLGenericInterface (Name Actual : Type u) where
  signature : GenericSignature Name VHDLGenericKind Actual
  compatible : Nat → Actual → Prop
  allowedDefault : Nat → Prop
```

**Source:** [`Catalog.Generics.VHDLGenericInterface`](../lean/Catalog/GenericProgramming.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Constant/type/subprogram/package kinds; finite distinct signature, compatibility/default obligations and whole-formal positional-prefix/named association normalizer. Unknown/repeated targets and late positional associations are rejected.

**Limits:** Selected whole-formal interface only. Subtype/type-category/profile/package matching, default expressions and anonymous generic type associations require language adapters; syntax normalization does not execute elaboration.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected defining rules: A generic interface is a finite list of constant, type, subprogram or package formals, with their language-specific declarations and compatibility requirements. A positional actual associates with the same-index formal; named actuals associate by formal identity in any order. Once a named association occurs, later positional associations are rejected; unknown/duplicate whole formals are rejected. Omission/open is resolved only by the applicable formal-kind default rules and environment. No missing mandatory actual is silently supplied; normalization precedes declaration-order elaboration.

**basisKind:** extensional-structural-definition

**basisScope:** IEEE 1076-2019 selected generic-interface profile. All four formal kinds are retained, with subtype, profile and package-map compatibility supplied by language adapters. Associations cover whole formals only; individual composite subelements, conversions and implicit associations for anonymous generic types are outside this reduced normalizer. Positional associations must precede named ones; named order may differ from declaration order; duplicate/unknown whole formals fail. open/omission can invoke only defaults allowed for that formal kind, notably constants and subprograms; no blanket type/package default is invented. Actual syntax is not prematurely evaluated in named-association order.

**verificationObligation:** Map language edition, carriers, identity, binding, substitution and phase-specific definedness explicitly.; Shared profiles do not transfer language rules; structural validation and model compilation do not prove language conformance.

**reviewStatus:** Editorial source/interface review; selected Lean interpretations are separate from theorem witnesses.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-VHDLGenericInterface-normalize"></a>

### normalize

`urn:csabs:operation/VHDLGenericInterface-normalize`

**signature:** normalize : Interface×Seq(Association)⇀ActualSlots

**description:** Map a positional prefix by index and named associations by declared formal identity; reject late positional, repeated or unknown whole-formal assignments.

**precondition:** Interface names are distinct and associations use the selected whole-formal profile.

**postcondition:** Map a positional prefix by index and named associations by declared formal identity; reject late positional, repeated or unknown whole-formal assignments.

**totality:** Partial on malformed associations; normalization does not establish value/subtype validity.

**source:** [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** IEEE 1076-2019 §§6.5.2–6.5.7, especially6.5.6.1–2,6.5.7.1–2;14.3.3.1

**sourceNote:** Extracts whole-formal matching and kind-specific compatibility/default obligations, not the complete association grammar or all VHDL-2019 type-category rules.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-VHDLGenericInterface-compatible"></a>

### compatible

`urn:csabs:operation/VHDLGenericInterface-compatible`

**signature:** compatible : Γ×Formal×Actual→Prop

**description:** Check the formal-kind-specific subtype/type-category, subprogram-profile or instantiated-package/generic-map requirements.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** Check the formal-kind-specific subtype/type-category, subprogram-profile or instantiated-package/generic-map requirements.

**totality:** Total mathematical operation on the stated carrier.

**source:** [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** IEEE 1076-2019 §§6.5.2–6.5.7, especially6.5.6.1–2,6.5.7.1–2;14.3.3.1

**sourceNote:** Extracts whole-formal matching and kind-specific compatibility/default obligations, not the complete association grammar or all VHDL-2019 type-category rules.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-VHDLGenericInterface-interface-kinds"></a>

### interface-kinds

`urn:csabs:axiom/VHDLGenericInterface-interface-kinds`

**statement:** A generic interface is a finite list of constant, type, subprogram or package formals, with their language-specific declarations and compatibility requirements.

**formalStatement:** A generic interface is a finite list of constant, type, subprogram or package formals, with their language-specific declarations and compatibility requirements.

**assumptions:** IEEE 1076-2019 selected generic-interface profile. All four formal kinds are retained, with subtype, profile and package-map compatibility supplied by language adapters. Associations cover whole formals only; individual composite subelements, conversions and implicit associations for anonymous generic types are outside this reduced normalizer. Positional associations must precede named ones; named order may differ from declaration order; duplicate/unknown whole formals fail. open/omission can invoke only defaults allowed for that formal kind, notably constants and subprograms; no blanket type/package default is invented. Actual syntax is not prematurely evaluated in named-association order.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** IEEE 1076-2019 §§6.5.2–6.5.7, especially6.5.6.1–2,6.5.7.1–2;14.3.3.1

**sourceNote:** Extracts whole-formal matching and kind-specific compatibility/default obligations, not the complete association grammar or all VHDL-2019 type-category rules.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-VHDLGenericInterface-association-order"></a>

### association-order

`urn:csabs:axiom/VHDLGenericInterface-association-order`

**statement:** A positional actual associates with the same-index formal; named actuals associate by formal identity in any order. Once a named association occurs, later positional associations are rejected; unknown/duplicate whole formals are rejected.

**formalStatement:** A positional actual associates with the same-index formal; named actuals associate by formal identity in any order. Once a named association occurs, later positional associations are rejected; unknown/duplicate whole formals are rejected.

**assumptions:** IEEE 1076-2019 selected generic-interface profile. All four formal kinds are retained, with subtype, profile and package-map compatibility supplied by language adapters. Associations cover whole formals only; individual composite subelements, conversions and implicit associations for anonymous generic types are outside this reduced normalizer. Positional associations must precede named ones; named order may differ from declaration order; duplicate/unknown whole formals fail. open/omission can invoke only defaults allowed for that formal kind, notably constants and subprograms; no blanket type/package default is invented. Actual syntax is not prematurely evaluated in named-association order.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** IEEE 1076-2019 §§6.5.2–6.5.7, especially6.5.6.1–2,6.5.7.1–2;14.3.3.1

**sourceNote:** Extracts whole-formal matching and kind-specific compatibility/default obligations, not the complete association grammar or all VHDL-2019 type-category rules.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-VHDLGenericInterface-kind-specific-defaults"></a>

### kind-specific-defaults

`urn:csabs:axiom/VHDLGenericInterface-kind-specific-defaults`

**statement:** Omission/open is resolved only by the applicable formal-kind default rules and environment. No missing mandatory actual is silently supplied; normalization precedes declaration-order elaboration.

**formalStatement:** Omission/open is resolved only by the applicable formal-kind default rules and environment. No missing mandatory actual is silently supplied; normalization precedes declaration-order elaboration.

**assumptions:** IEEE 1076-2019 selected generic-interface profile. All four formal kinds are retained, with subtype, profile and package-map compatibility supplied by language adapters. Associations cover whole formals only; individual composite subelements, conversions and implicit associations for anonymous generic types are outside this reduced normalizer. Positional associations must precede named ones; named order may differ from declaration order; duplicate/unknown whole formals fail. open/omission can invoke only defaults allowed for that formal kind, notably constants and subprograms; no blanket type/package default is invented. Actual syntax is not prematurely evaluated in named-association order.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** IEEE 1076-2019 §§6.5.2–6.5.7, especially6.5.6.1–2,6.5.7.1–2;14.3.3.1

**sourceNote:** Extracts whole-formal matching and kind-specific compatibility/default obligations, not the complete association grammar or all VHDL-2019 type-category rules.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-VHDLGenericInterface-named-permutation"></a>

### named-permutation

`urn:csabs:law/VHDLGenericInterface-named-permutation`

**statement:** Permuting a valid all-named association list with distinct whole formals preserves its normalized formal-to-actual map.

**formalStatement:** Permuting a valid all-named association list with distinct whole formals preserves its normalized formal-to-actual map.

**assumptions:** IEEE 1076-2019 selected generic-interface profile. All four formal kinds are retained, with subtype, profile and package-map compatibility supplied by language adapters. Associations cover whole formals only; individual composite subelements, conversions and implicit associations for anonymous generic types are outside this reduced normalizer. Positional associations must precede named ones; named order may differ from declaration order; duplicate/unknown whole formals fail. open/omission can invoke only defaults allowed for that formal kind, notably constants and subprograms; no blanket type/package default is invented. Actual syntax is not prematurely evaluated in named-association order.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** IEEE 1076-2019 §§6.5.2–6.5.7, especially6.5.6.1–2,6.5.7.1–2;14.3.3.1

**sourceNote:** Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.

**provenanceKind:** derived

**dependsOn:** [interface-kinds](VHDLGenericInterface.md#node-urn-csabs-axiom-VHDLGenericInterface-interface-kinds); [association-order](VHDLGenericInterface.md#node-urn-csabs-axiom-VHDLGenericInterface-association-order)

**proofSketch:** Each named association targets its unique declared identity independently of list position; distinctness excludes overwrite effects. This is about normalization, not reordering expression evaluation.

<a id="node-urn-csabs-law-VHDLGenericInterface-late-positional-rejected"></a>

### late-positional-rejected

`urn:csabs:law/VHDLGenericInterface-late-positional-rejected`

**statement:** An association list with a named item followed by a positional item is outside dom(normalizeΣ).

**formalStatement:** An association list with a named item followed by a positional item is outside dom(normalizeΣ).

**assumptions:** IEEE 1076-2019 selected generic-interface profile. All four formal kinds are retained, with subtype, profile and package-map compatibility supplied by language adapters. Associations cover whole formals only; individual composite subelements, conversions and implicit associations for anonymous generic types are outside this reduced normalizer. Positional associations must precede named ones; named order may differ from declaration order; duplicate/unknown whole formals fail. open/omission can invoke only defaults allowed for that formal kind, notably constants and subprograms; no blanket type/package default is invented. Actual syntax is not prematurely evaluated in named-association order.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** IEEE 1076-2019 §§6.5.2–6.5.7, especially6.5.6.1–2,6.5.7.1–2;14.3.3.1

**sourceNote:** Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.

**provenanceKind:** derived

**dependsOn:** [association-order](VHDLGenericInterface.md#node-urn-csabs-axiom-VHDLGenericInterface-association-order)

**proofSketch:** It violates the positional-prefix rule regardless of whether its actual values might otherwise fit.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** IEEE 1076-2019 §§6.5.2–6.5.7, especially6.5.6.1–2,6.5.7.1–2;14.3.3.1

**sourceNote:** Extracts whole-formal matching and kind-specific compatibility/default obligations, not the complete association grammar or all VHDL-2019 type-category rules.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/VHDLGenericInterface",
    "type": "Concept",
    "shortForm": "VHDLGenericInterface",
    "fullName": "VHDL generic interfaces and whole-formal association",
    "definition": "Finite VHDL generic interfaces with constant/type/subprogram/package formals and a checked normalization of positional or named whole-formal associations.",
    "notation": "Kind={Constant,Type,Subprogram,Package}; Assoc=Positional(actual)⊎Named(formal,actual); normalizeΣ:Seq(Assoc)⇀ActualSlots",
    "category": [
      "urn:csabs:category/vhdl-generics"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/GenericSignature",
      "urn:csabs:concept/GenericArgumentBinding"
    ],
    "relatedConcept": [
      "urn:csabs:concept/VHDLGenericElaboration",
      "urn:csabs:concept/TemplateMetafunction"
    ],
    "hasOperation": [
      "urn:csabs:operation/VHDLGenericInterface-normalize",
      "urn:csabs:operation/VHDLGenericInterface-compatible"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/VHDLGenericInterface-interface-kinds",
      "urn:csabs:axiom/VHDLGenericInterface-association-order",
      "urn:csabs:axiom/VHDLGenericInterface-kind-specific-defaults"
    ],
    "hasLaw": [
      "urn:csabs:law/VHDLGenericInterface-named-permutation",
      "urn:csabs:law/VHDLGenericInterface-late-positional-rejected"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "IEEE 1076-2019 selected generic-interface profile. All four formal kinds are retained, with subtype, profile and package-map compatibility supplied by language adapters. Associations cover whole formals only; individual composite subelements, conversions and implicit associations for anonymous generic types are outside this reduced normalizer. Positional associations must precede named ones; named order may differ from declaration order; duplicate/unknown whole formals fail. open/omission can invoke only defaults allowed for that formal kind, notably constants and subprograms; no blanket type/package default is invented. Actual syntax is not prematurely evaluated in named-association order.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; selected Lean interpretations are separate from theorem witnesses.",
    "verificationObligation": [
      "Map language edition, carriers, identity, binding, substitution and phase-specific definedness explicitly.",
      "Shared profiles do not transfer language rules; structural validation and model compilation do not prove language conformance."
    ],
    "source": [
      "urn:csabs:source/generics-vhdl2019"
    ],
    "sourceLocator": "IEEE 1076-2019 §§6.5.2–6.5.7, especially6.5.6.1–2,6.5.7.1–2;14.3.3.1",
    "sourceNote": "Extracts whole-formal matching and kind-specific compatibility/default obligations, not the complete association grammar or all VHDL-2019 type-category rules.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: A generic interface is a finite list of constant, type, subprogram or package formals, with their language-specific declarations and compatibility requirements. A positional actual associates with the same-index formal; named actuals associate by formal identity in any order. Once a named association occurs, later positional associations are rejected; unknown/duplicate whole formals are rejected. Omission/open is resolved only by the applicable formal-kind default rules and environment. No missing mandatory actual is silently supplied; normalization precedes declaration-order elaboration.",
    "leanFormulation": "structure VHDLGenericInterface (Name Actual : Type u) where\n  signature : GenericSignature Name VHDLGenericKind Actual\n  compatible : Nat → Actual → Prop\n  allowedDefault : Nat → Prop",
    "formulationSource": "urn:csabs:source/local-lean-GenericProgramming",
    "formulationLocator": "Catalog.Generics.VHDLGenericInterface",
    "formulationScope": "model",
    "leanModelMapping": "Constant/type/subprogram/package kinds; finite distinct signature, compatibility/default obligations and whole-formal positional-prefix/named association normalizer. Unknown/repeated targets and late positional associations are rejected.",
    "leanModelLimitations": "Selected whole-formal interface only. Subtype/type-category/profile/package matching, default expressions and anonymous generic type associations require language adapters; syntax normalization does not execute elaboration.",
    "mathematicalFormulation": "A VHDL generic interface is a distinct-name signature with kinds {constant,type,subprogram,package}, compatibility predicates and default permissions. Association normalization maps actuals to formal indices, rejects duplicates/unknown names/out-of-range positions, and forbids positional associations after a named association. Language conformance remains a supplied predicate."
  },
  {
    "id": "urn:csabs:operation/VHDLGenericInterface-normalize",
    "type": "Operation",
    "name": "normalize",
    "signature": "normalize : Interface×Seq(Association)⇀ActualSlots",
    "description": "Map a positional prefix by index and named associations by declared formal identity; reject late positional, repeated or unknown whole-formal assignments.",
    "concept": "urn:csabs:concept/VHDLGenericInterface",
    "precondition": "Interface names are distinct and associations use the selected whole-formal profile.",
    "postcondition": "Map a positional prefix by index and named associations by declared formal identity; reject late positional, repeated or unknown whole-formal assignments.",
    "totality": "Partial on malformed associations; normalization does not establish value/subtype validity.",
    "source": [
      "urn:csabs:source/generics-vhdl2019"
    ],
    "sourceLocator": "IEEE 1076-2019 §§6.5.2–6.5.7, especially6.5.6.1–2,6.5.7.1–2;14.3.3.1",
    "sourceNote": "Extracts whole-formal matching and kind-specific compatibility/default obligations, not the complete association grammar or all VHDL-2019 type-category rules.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/VHDLGenericInterface-compatible",
    "type": "Operation",
    "name": "compatible",
    "signature": "compatible : Γ×Formal×Actual→Prop",
    "description": "Check the formal-kind-specific subtype/type-category, subprogram-profile or instantiated-package/generic-map requirements.",
    "concept": "urn:csabs:concept/VHDLGenericInterface",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "Check the formal-kind-specific subtype/type-category, subprogram-profile or instantiated-package/generic-map requirements.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-vhdl2019"
    ],
    "sourceLocator": "IEEE 1076-2019 §§6.5.2–6.5.7, especially6.5.6.1–2,6.5.7.1–2;14.3.3.1",
    "sourceNote": "Extracts whole-formal matching and kind-specific compatibility/default obligations, not the complete association grammar or all VHDL-2019 type-category rules.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/VHDLGenericInterface-interface-kinds",
    "type": "Axiom",
    "name": "interface-kinds",
    "statement": "A generic interface is a finite list of constant, type, subprogram or package formals, with their language-specific declarations and compatibility requirements.",
    "formalStatement": "A generic interface is a finite list of constant, type, subprogram or package formals, with their language-specific declarations and compatibility requirements.",
    "assumptions": [
      "IEEE 1076-2019 selected generic-interface profile. All four formal kinds are retained, with subtype, profile and package-map compatibility supplied by language adapters. Associations cover whole formals only; individual composite subelements, conversions and implicit associations for anonymous generic types are outside this reduced normalizer. Positional associations must precede named ones; named order may differ from declaration order; duplicate/unknown whole formals fail. open/omission can invoke only defaults allowed for that formal kind, notably constants and subprograms; no blanket type/package default is invented. Actual syntax is not prematurely evaluated in named-association order.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/VHDLGenericInterface"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-vhdl2019"
    ],
    "sourceLocator": "IEEE 1076-2019 §§6.5.2–6.5.7, especially6.5.6.1–2,6.5.7.1–2;14.3.3.1",
    "sourceNote": "Extracts whole-formal matching and kind-specific compatibility/default obligations, not the complete association grammar or all VHDL-2019 type-category rules.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/VHDLGenericInterface-association-order",
    "type": "Axiom",
    "name": "association-order",
    "statement": "A positional actual associates with the same-index formal; named actuals associate by formal identity in any order. Once a named association occurs, later positional associations are rejected; unknown/duplicate whole formals are rejected.",
    "formalStatement": "A positional actual associates with the same-index formal; named actuals associate by formal identity in any order. Once a named association occurs, later positional associations are rejected; unknown/duplicate whole formals are rejected.",
    "assumptions": [
      "IEEE 1076-2019 selected generic-interface profile. All four formal kinds are retained, with subtype, profile and package-map compatibility supplied by language adapters. Associations cover whole formals only; individual composite subelements, conversions and implicit associations for anonymous generic types are outside this reduced normalizer. Positional associations must precede named ones; named order may differ from declaration order; duplicate/unknown whole formals fail. open/omission can invoke only defaults allowed for that formal kind, notably constants and subprograms; no blanket type/package default is invented. Actual syntax is not prematurely evaluated in named-association order.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/VHDLGenericInterface"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-vhdl2019"
    ],
    "sourceLocator": "IEEE 1076-2019 §§6.5.2–6.5.7, especially6.5.6.1–2,6.5.7.1–2;14.3.3.1",
    "sourceNote": "Extracts whole-formal matching and kind-specific compatibility/default obligations, not the complete association grammar or all VHDL-2019 type-category rules.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/VHDLGenericInterface-kind-specific-defaults",
    "type": "Axiom",
    "name": "kind-specific-defaults",
    "statement": "Omission/open is resolved only by the applicable formal-kind default rules and environment. No missing mandatory actual is silently supplied; normalization precedes declaration-order elaboration.",
    "formalStatement": "Omission/open is resolved only by the applicable formal-kind default rules and environment. No missing mandatory actual is silently supplied; normalization precedes declaration-order elaboration.",
    "assumptions": [
      "IEEE 1076-2019 selected generic-interface profile. All four formal kinds are retained, with subtype, profile and package-map compatibility supplied by language adapters. Associations cover whole formals only; individual composite subelements, conversions and implicit associations for anonymous generic types are outside this reduced normalizer. Positional associations must precede named ones; named order may differ from declaration order; duplicate/unknown whole formals fail. open/omission can invoke only defaults allowed for that formal kind, notably constants and subprograms; no blanket type/package default is invented. Actual syntax is not prematurely evaluated in named-association order.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/VHDLGenericInterface"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-vhdl2019"
    ],
    "sourceLocator": "IEEE 1076-2019 §§6.5.2–6.5.7, especially6.5.6.1–2,6.5.7.1–2;14.3.3.1",
    "sourceNote": "Extracts whole-formal matching and kind-specific compatibility/default obligations, not the complete association grammar or all VHDL-2019 type-category rules.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/VHDLGenericInterface-named-permutation",
    "type": "Law",
    "name": "named-permutation",
    "statement": "Permuting a valid all-named association list with distinct whole formals preserves its normalized formal-to-actual map.",
    "formalStatement": "Permuting a valid all-named association list with distinct whole formals preserves its normalized formal-to-actual map.",
    "assumptions": [
      "IEEE 1076-2019 selected generic-interface profile. All four formal kinds are retained, with subtype, profile and package-map compatibility supplied by language adapters. Associations cover whole formals only; individual composite subelements, conversions and implicit associations for anonymous generic types are outside this reduced normalizer. Positional associations must precede named ones; named order may differ from declaration order; duplicate/unknown whole formals fail. open/omission can invoke only defaults allowed for that formal kind, notably constants and subprograms; no blanket type/package default is invented. Actual syntax is not prematurely evaluated in named-association order.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/VHDLGenericInterface"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-vhdl2019"
    ],
    "sourceLocator": "IEEE 1076-2019 §§6.5.2–6.5.7, especially6.5.6.1–2,6.5.7.1–2;14.3.3.1",
    "sourceNote": "Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/VHDLGenericInterface-interface-kinds",
      "urn:csabs:axiom/VHDLGenericInterface-association-order"
    ],
    "proofSketch": "Each named association targets its unique declared identity independently of list position; distinctness excludes overwrite effects. This is about normalization, not reordering expression evaluation."
  },
  {
    "id": "urn:csabs:law/VHDLGenericInterface-late-positional-rejected",
    "type": "Law",
    "name": "late-positional-rejected",
    "statement": "An association list with a named item followed by a positional item is outside dom(normalizeΣ).",
    "formalStatement": "An association list with a named item followed by a positional item is outside dom(normalizeΣ).",
    "assumptions": [
      "IEEE 1076-2019 selected generic-interface profile. All four formal kinds are retained, with subtype, profile and package-map compatibility supplied by language adapters. Associations cover whole formals only; individual composite subelements, conversions and implicit associations for anonymous generic types are outside this reduced normalizer. Positional associations must precede named ones; named order may differ from declaration order; duplicate/unknown whole formals fail. open/omission can invoke only defaults allowed for that formal kind, notably constants and subprograms; no blanket type/package default is invented. Actual syntax is not prematurely evaluated in named-association order.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/VHDLGenericInterface"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-vhdl2019"
    ],
    "sourceLocator": "IEEE 1076-2019 §§6.5.2–6.5.7, especially6.5.6.1–2,6.5.7.1–2;14.3.3.1",
    "sourceNote": "Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/VHDLGenericInterface-association-order"
    ],
    "proofSketch": "It violates the positional-prefix rule regardless of whether its actual values might otherwise fit."
  }
]
```
<!-- graph-record:end -->
