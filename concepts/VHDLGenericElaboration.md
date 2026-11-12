# VHDL generic elaboration and static structural generation

A staged elaboration relation that binds generic actuals in formal declaration order, performs kind-specific elaboration checks and constructs the selected instance and generate structure.

**Notation:** elab(Γ,unit,assoc)⇀Instance; header=genericClause;genericMap;portClause;portMap where applicable; forGenerate(R,B)=[B(i) | i in discrete R in its declared direction]

**Stable ID:** `urn:csabs:concept/VHDLGenericElaboration`

**Categories:** Programming-language semantics → Generic programming → VHDL generics

**Kind:** semantic-model

**Prerequisites:** [VHDL generic interfaces and whole-formal association](VHDLGenericInterface.md), [Contextual parametric declaration instantiation](ParametricInstantiation.md), [Finite sequence (List datatype)](Sequence.md)

**Related concepts:** [Checked signed-integer constant-evaluation fragment](CompileTimeEvaluation.md), [Transition System](TransitionSystem.md)

## Backlinks

- [Contextual parametric declaration instantiation](ParametricInstantiation.md) — `relatedConcept`
- [VHDL generic interfaces and whole-formal association](VHDLGenericInterface.md) — `relatedConcept`

## Mathematical formulation

For partial step:Env×Event⇀Env, run(e,[])=some(e), run(e,a::as)=step(e,a) >>= (e′↦run(e′,as)); elaborate(e,as)=run(e,as) >>= finish. forGenerate(xs,b)=map(b,xs); ifGenerate(true,b)=[b], ifGenerate(false,b)=[]. Staticness predicates and language event semantics remain supplied.

**Lean formulation** (in its source module context):

```lean
structure VHDLGenericElaboration (Env Event Instance : Type u) where
  step : Env → Event → Option Env
  finish : Env → Option Instance
  locallyStatic : Env → Event → Prop
  globallyStatic : Env → Event → Prop
```

**Source:** [`Catalog.Generics.VHDLGenericElaboration`](../lean/Catalog/GenericProgramming.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Ordered event execution with partial environment steps and final instance construction; separate staticness predicates and finite list-valued for/if generation.

**Limits:** Events must encode declaration order and applicable header phases; concrete VHDL evaluation, conformance, staticness, configurations, package identity and simulation are not implemented. GHDL examples require separate tool evidence.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected defining rules: After association matching, generic declarations/associations are elaborated in formal declaration order. Block headers elaborate generic clause, generic map, port clause and port map in that order; package headers use their applicable generic phases. A constant actual must fit the elaborated formal subtype; a formal type denotes its elaborated actual subtype; formal subprogram/package associations must meet their conformance/matching obligations. Missing required or incompatible actuals prevent successful elaboration. For a valid finite discrete range R, forGenerate(R,B)=[B(i) | i∈R in declared direction]; valid single-condition ifGenerate(true,B)=[B] and ifGenerate(false,B)=[]. Locally/global-static status is supplied by the cited language rules.

**basisKind:** extensional-structural-definition

**basisScope:** IEEE 1076-2019 selected finite elaboration profile. Association matching precedes processing in formal declaration order. Constant actuals/defaults are evaluated and checked against the elaborated formal subtype; generic types denote elaborated actual subtypes, subprograms denote conforming actual declarations, and packages denote compatible instances. Staticness is classified by the language locally/global-static rules, not by a universal compile-time Boolean flag; generic constants are not automatically locally static. Generate controls obey their context-required staticness. No synthesis guarantee, hardware cost, signal/process/delta-cycle semantics, full configuration binding or universal termination is assumed. A failed elaboration does not promise rollback of partial compiler state.

**verificationObligation:** Map language edition, carriers, identity, binding, substitution and phase-specific definedness explicitly.; Shared profiles do not transfer language rules; structural validation and model compilation do not prove language conformance.

**reviewStatus:** Editorial source/interface review; selected Lean interpretations are separate from theorem witnesses.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-VHDLGenericElaboration-elaborate"></a>

### elaborate

`urn:csabs:operation/VHDLGenericElaboration-elaborate`

**signature:** elaborate : Γ×Unit×AssociationList×Instance→Prop

**description:** Relate an instance only after valid association, applicable defaults and declaration-order kind-specific elaboration; package instantiation elaborates its generic-mapped declarations and body when present.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** Relate an instance only after valid association, applicable defaults and declaration-order kind-specific elaboration; package instantiation elaborates its generic-mapped declarations and body when present.

**totality:** Total mathematical operation on the stated carrier.

**source:** [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements

**sourceNote:** Models phase order, explicit checks and finite generate expansion, retaining the distinction between VHDL elaboration and C++ constant-expression evaluation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-VHDLGenericElaboration-staticness"></a>

### staticness

`urn:csabs:operation/VHDLGenericElaboration-staticness`

**signature:** staticness : Γ×Expression→StaticnessInfo

**description:** Report language-derived locally/globally-static properties and context validity. Computability by a tool alone does not establish either property.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** Report language-derived locally/globally-static properties and context validity. Computability by a tool alone does not establish either property.

**totality:** Total mathematical operation on the stated carrier.

**source:** [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements

**sourceNote:** Models phase order, explicit checks and finite generate expansion, retaining the distinction between VHDL elaboration and C++ constant-expression evaluation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-VHDLGenericElaboration-for-generate"></a>

### for-generate

`urn:csabs:operation/VHDLGenericElaboration-for-generate`

**signature:** forGenerate : DiscreteRange×BlockSchema→Seq(BlockInstance)

**description:** Create one block instance per range value in the declared direction; a null range creates no block.

**precondition:** The range and schema meet the context staticness and language well-formedness rules.

**postcondition:** Create one block instance per range value in the declared direction; a null range creates no block.

**totality:** Finite expansion on valid inputs; invalid staticness is a language error, not a zero-length fallback.

**source:** [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements

**sourceNote:** Models phase order, explicit checks and finite generate expansion, retaining the distinction between VHDL elaboration and C++ constant-expression evaluation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-VHDLGenericElaboration-if-generate"></a>

### if-generate

`urn:csabs:operation/VHDLGenericElaboration-if-generate`

**signature:** ifGenerate : StaticBool×BlockSchema→Seq(BlockInstance)

**description:** For the selected single if-generate profile, elaborate one block when its valid condition is true and none when false. Unselected syntax must still pass applicable analysis rules.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** For the selected single if-generate profile, elaborate one block when its valid condition is true and none when false. Unselected syntax must still pass applicable analysis rules.

**totality:** Total mathematical operation on the stated carrier.

**source:** [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements

**sourceNote:** Models phase order, explicit checks and finite generate expansion, retaining the distinction between VHDL elaboration and C++ constant-expression evaluation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-VHDLGenericElaboration-elaboration-order"></a>

### elaboration-order

`urn:csabs:axiom/VHDLGenericElaboration-elaboration-order`

**statement:** After association matching, generic declarations/associations are elaborated in formal declaration order. Block headers elaborate generic clause, generic map, port clause and port map in that order; package headers use their applicable generic phases.

**formalStatement:** After association matching, generic declarations/associations are elaborated in formal declaration order. Block headers elaborate generic clause, generic map, port clause and port map in that order; package headers use their applicable generic phases.

**assumptions:** IEEE 1076-2019 selected finite elaboration profile. Association matching precedes processing in formal declaration order. Constant actuals/defaults are evaluated and checked against the elaborated formal subtype; generic types denote elaborated actual subtypes, subprograms denote conforming actual declarations, and packages denote compatible instances. Staticness is classified by the language locally/global-static rules, not by a universal compile-time Boolean flag; generic constants are not automatically locally static. Generate controls obey their context-required staticness. No synthesis guarantee, hardware cost, signal/process/delta-cycle semantics, full configuration binding or universal termination is assumed. A failed elaboration does not promise rollback of partial compiler state.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements

**sourceNote:** Models phase order, explicit checks and finite generate expansion, retaining the distinction between VHDL elaboration and C++ constant-expression evaluation.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-VHDLGenericElaboration-kind-specific-elaboration"></a>

### kind-specific-elaboration

`urn:csabs:axiom/VHDLGenericElaboration-kind-specific-elaboration`

**statement:** A constant actual must fit the elaborated formal subtype; a formal type denotes its elaborated actual subtype; formal subprogram/package associations must meet their conformance/matching obligations. Missing required or incompatible actuals prevent successful elaboration.

**formalStatement:** A constant actual must fit the elaborated formal subtype; a formal type denotes its elaborated actual subtype; formal subprogram/package associations must meet their conformance/matching obligations. Missing required or incompatible actuals prevent successful elaboration.

**assumptions:** IEEE 1076-2019 selected finite elaboration profile. Association matching precedes processing in formal declaration order. Constant actuals/defaults are evaluated and checked against the elaborated formal subtype; generic types denote elaborated actual subtypes, subprograms denote conforming actual declarations, and packages denote compatible instances. Staticness is classified by the language locally/global-static rules, not by a universal compile-time Boolean flag; generic constants are not automatically locally static. Generate controls obey their context-required staticness. No synthesis guarantee, hardware cost, signal/process/delta-cycle semantics, full configuration binding or universal termination is assumed. A failed elaboration does not promise rollback of partial compiler state.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements

**sourceNote:** Models phase order, explicit checks and finite generate expansion, retaining the distinction between VHDL elaboration and C++ constant-expression evaluation.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-VHDLGenericElaboration-static-generation"></a>

### static-generation

`urn:csabs:axiom/VHDLGenericElaboration-static-generation`

**statement:** For a valid finite discrete range R, forGenerate(R,B)=[B(i) | i∈R in declared direction]; valid single-condition ifGenerate(true,B)=[B] and ifGenerate(false,B)=[]. Locally/global-static status is supplied by the cited language rules.

**formalStatement:** For a valid finite discrete range R, forGenerate(R,B)=[B(i) | i∈R in declared direction]; valid single-condition ifGenerate(true,B)=[B] and ifGenerate(false,B)=[]. Locally/global-static status is supplied by the cited language rules.

**assumptions:** IEEE 1076-2019 selected finite elaboration profile. Association matching precedes processing in formal declaration order. Constant actuals/defaults are evaluated and checked against the elaborated formal subtype; generic types denote elaborated actual subtypes, subprograms denote conforming actual declarations, and packages denote compatible instances. Staticness is classified by the language locally/global-static rules, not by a universal compile-time Boolean flag; generic constants are not automatically locally static. Generate controls obey their context-required staticness. No synthesis guarantee, hardware cost, signal/process/delta-cycle semantics, full configuration binding or universal termination is assumed. A failed elaboration does not promise rollback of partial compiler state.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements

**sourceNote:** Models phase order, explicit checks and finite generate expansion, retaining the distinction between VHDL elaboration and C++ constant-expression evaluation.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-VHDLGenericElaboration-null-generate-empty"></a>

### null-generate-empty

`urn:csabs:law/VHDLGenericElaboration-null-generate-empty`

**statement:** R is a valid null discrete range ⇒ forGenerate(R,B)=[].

**formalStatement:** R is a valid null discrete range ⇒ forGenerate(R,B)=[].

**assumptions:** IEEE 1076-2019 selected finite elaboration profile. Association matching precedes processing in formal declaration order. Constant actuals/defaults are evaluated and checked against the elaborated formal subtype; generic types denote elaborated actual subtypes, subprograms denote conforming actual declarations, and packages denote compatible instances. Staticness is classified by the language locally/global-static rules, not by a universal compile-time Boolean flag; generic constants are not automatically locally static. Generate controls obey their context-required staticness. No synthesis guarantee, hardware cost, signal/process/delta-cycle semantics, full configuration binding or universal termination is assumed. A failed elaboration does not promise rollback of partial compiler state.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements

**sourceNote:** Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.

**provenanceKind:** derived

**dependsOn:** [static-generation](VHDLGenericElaboration.md#node-urn-csabs-axiom-VHDLGenericElaboration-static-generation)

**proofSketch:** A null discrete range has no values, so the indexed block list is empty; validity of the range is still required.

<a id="node-urn-csabs-law-VHDLGenericElaboration-incompatible-actual-no-instance"></a>

### incompatible-actual-no-instance

`urn:csabs:law/VHDLGenericElaboration-incompatible-actual-no-instance`

**statement:** A required actual violates the kind-specific elaboration check ⇒ no successful elaboration instance is related.

**formalStatement:** A required actual violates the kind-specific elaboration check ⇒ no successful elaboration instance is related.

**assumptions:** IEEE 1076-2019 selected finite elaboration profile. Association matching precedes processing in formal declaration order. Constant actuals/defaults are evaluated and checked against the elaborated formal subtype; generic types denote elaborated actual subtypes, subprograms denote conforming actual declarations, and packages denote compatible instances. Staticness is classified by the language locally/global-static rules, not by a universal compile-time Boolean flag; generic constants are not automatically locally static. Generate controls obey their context-required staticness. No synthesis guarantee, hardware cost, signal/process/delta-cycle semantics, full configuration binding or universal termination is assumed. A failed elaboration does not promise rollback of partial compiler state.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements

**sourceNote:** Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.

**provenanceKind:** derived

**dependsOn:** [elaboration-order](VHDLGenericElaboration.md#node-urn-csabs-axiom-VHDLGenericElaboration-elaboration-order); [kind-specific-elaboration](VHDLGenericElaboration.md#node-urn-csabs-axiom-VHDLGenericElaboration-kind-specific-elaboration)

**proofSketch:** Elaboration requires each declared generic association to pass its applicable check. Association normalization alone cannot supply a valid instance.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements

**sourceNote:** Models phase order, explicit checks and finite generate expansion, retaining the distinction between VHDL elaboration and C++ constant-expression evaluation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/VHDLGenericElaboration",
    "type": "Concept",
    "shortForm": "VHDLGenericElaboration",
    "fullName": "VHDL generic elaboration and static structural generation",
    "definition": "A staged elaboration relation that binds generic actuals in formal declaration order, performs kind-specific elaboration checks and constructs the selected instance and generate structure.",
    "notation": "elab(Γ,unit,assoc)⇀Instance; header=genericClause;genericMap;portClause;portMap where applicable; forGenerate(R,B)=[B(i) | i in discrete R in its declared direction]",
    "category": [
      "urn:csabs:category/vhdl-generics"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/VHDLGenericInterface",
      "urn:csabs:concept/ParametricInstantiation",
      "urn:csabs:concept/Sequence"
    ],
    "relatedConcept": [
      "urn:csabs:concept/CompileTimeEvaluation",
      "urn:csabs:concept/TransitionSystem"
    ],
    "hasOperation": [
      "urn:csabs:operation/VHDLGenericElaboration-elaborate",
      "urn:csabs:operation/VHDLGenericElaboration-staticness",
      "urn:csabs:operation/VHDLGenericElaboration-for-generate",
      "urn:csabs:operation/VHDLGenericElaboration-if-generate"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/VHDLGenericElaboration-elaboration-order",
      "urn:csabs:axiom/VHDLGenericElaboration-kind-specific-elaboration",
      "urn:csabs:axiom/VHDLGenericElaboration-static-generation"
    ],
    "hasLaw": [
      "urn:csabs:law/VHDLGenericElaboration-null-generate-empty",
      "urn:csabs:law/VHDLGenericElaboration-incompatible-actual-no-instance"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "IEEE 1076-2019 selected finite elaboration profile. Association matching precedes processing in formal declaration order. Constant actuals/defaults are evaluated and checked against the elaborated formal subtype; generic types denote elaborated actual subtypes, subprograms denote conforming actual declarations, and packages denote compatible instances. Staticness is classified by the language locally/global-static rules, not by a universal compile-time Boolean flag; generic constants are not automatically locally static. Generate controls obey their context-required staticness. No synthesis guarantee, hardware cost, signal/process/delta-cycle semantics, full configuration binding or universal termination is assumed. A failed elaboration does not promise rollback of partial compiler state.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; selected Lean interpretations are separate from theorem witnesses.",
    "verificationObligation": [
      "Map language edition, carriers, identity, binding, substitution and phase-specific definedness explicitly.",
      "Shared profiles do not transfer language rules; structural validation and model compilation do not prove language conformance."
    ],
    "source": [
      "urn:csabs:source/generics-vhdl2019"
    ],
    "sourceLocator": "IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements",
    "sourceNote": "Models phase order, explicit checks and finite generate expansion, retaining the distinction between VHDL elaboration and C++ constant-expression evaluation.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: After association matching, generic declarations/associations are elaborated in formal declaration order. Block headers elaborate generic clause, generic map, port clause and port map in that order; package headers use their applicable generic phases. A constant actual must fit the elaborated formal subtype; a formal type denotes its elaborated actual subtype; formal subprogram/package associations must meet their conformance/matching obligations. Missing required or incompatible actuals prevent successful elaboration. For a valid finite discrete range R, forGenerate(R,B)=[B(i) | i∈R in declared direction]; valid single-condition ifGenerate(true,B)=[B] and ifGenerate(false,B)=[]. Locally/global-static status is supplied by the cited language rules.",
    "leanFormulation": "structure VHDLGenericElaboration (Env Event Instance : Type u) where\n  step : Env → Event → Option Env\n  finish : Env → Option Instance\n  locallyStatic : Env → Event → Prop\n  globallyStatic : Env → Event → Prop",
    "formulationSource": "urn:csabs:source/local-lean-GenericProgramming",
    "formulationLocator": "Catalog.Generics.VHDLGenericElaboration",
    "formulationScope": "partial",
    "leanModelMapping": "Ordered event execution with partial environment steps and final instance construction; separate staticness predicates and finite list-valued for/if generation.",
    "leanModelLimitations": "Events must encode declaration order and applicable header phases; concrete VHDL evaluation, conformance, staticness, configurations, package identity and simulation are not implemented. GHDL examples require separate tool evidence.",
    "mathematicalFormulation": "For partial step:Env×Event⇀Env, run(e,[])=some(e), run(e,a::as)=step(e,a) >>= (e′↦run(e′,as)); elaborate(e,as)=run(e,as) >>= finish. forGenerate(xs,b)=map(b,xs); ifGenerate(true,b)=[b], ifGenerate(false,b)=[]. Staticness predicates and language event semantics remain supplied."
  },
  {
    "id": "urn:csabs:operation/VHDLGenericElaboration-elaborate",
    "type": "Operation",
    "name": "elaborate",
    "signature": "elaborate : Γ×Unit×AssociationList×Instance→Prop",
    "description": "Relate an instance only after valid association, applicable defaults and declaration-order kind-specific elaboration; package instantiation elaborates its generic-mapped declarations and body when present.",
    "concept": "urn:csabs:concept/VHDLGenericElaboration",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "Relate an instance only after valid association, applicable defaults and declaration-order kind-specific elaboration; package instantiation elaborates its generic-mapped declarations and body when present.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-vhdl2019"
    ],
    "sourceLocator": "IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements",
    "sourceNote": "Models phase order, explicit checks and finite generate expansion, retaining the distinction between VHDL elaboration and C++ constant-expression evaluation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/VHDLGenericElaboration-staticness",
    "type": "Operation",
    "name": "staticness",
    "signature": "staticness : Γ×Expression→StaticnessInfo",
    "description": "Report language-derived locally/globally-static properties and context validity. Computability by a tool alone does not establish either property.",
    "concept": "urn:csabs:concept/VHDLGenericElaboration",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "Report language-derived locally/globally-static properties and context validity. Computability by a tool alone does not establish either property.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-vhdl2019"
    ],
    "sourceLocator": "IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements",
    "sourceNote": "Models phase order, explicit checks and finite generate expansion, retaining the distinction between VHDL elaboration and C++ constant-expression evaluation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/VHDLGenericElaboration-for-generate",
    "type": "Operation",
    "name": "for-generate",
    "signature": "forGenerate : DiscreteRange×BlockSchema→Seq(BlockInstance)",
    "description": "Create one block instance per range value in the declared direction; a null range creates no block.",
    "concept": "urn:csabs:concept/VHDLGenericElaboration",
    "precondition": "The range and schema meet the context staticness and language well-formedness rules.",
    "postcondition": "Create one block instance per range value in the declared direction; a null range creates no block.",
    "totality": "Finite expansion on valid inputs; invalid staticness is a language error, not a zero-length fallback.",
    "source": [
      "urn:csabs:source/generics-vhdl2019"
    ],
    "sourceLocator": "IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements",
    "sourceNote": "Models phase order, explicit checks and finite generate expansion, retaining the distinction between VHDL elaboration and C++ constant-expression evaluation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/VHDLGenericElaboration-if-generate",
    "type": "Operation",
    "name": "if-generate",
    "signature": "ifGenerate : StaticBool×BlockSchema→Seq(BlockInstance)",
    "description": "For the selected single if-generate profile, elaborate one block when its valid condition is true and none when false. Unselected syntax must still pass applicable analysis rules.",
    "concept": "urn:csabs:concept/VHDLGenericElaboration",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "For the selected single if-generate profile, elaborate one block when its valid condition is true and none when false. Unselected syntax must still pass applicable analysis rules.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-vhdl2019"
    ],
    "sourceLocator": "IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements",
    "sourceNote": "Models phase order, explicit checks and finite generate expansion, retaining the distinction between VHDL elaboration and C++ constant-expression evaluation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/VHDLGenericElaboration-elaboration-order",
    "type": "Axiom",
    "name": "elaboration-order",
    "statement": "After association matching, generic declarations/associations are elaborated in formal declaration order. Block headers elaborate generic clause, generic map, port clause and port map in that order; package headers use their applicable generic phases.",
    "formalStatement": "After association matching, generic declarations/associations are elaborated in formal declaration order. Block headers elaborate generic clause, generic map, port clause and port map in that order; package headers use their applicable generic phases.",
    "assumptions": [
      "IEEE 1076-2019 selected finite elaboration profile. Association matching precedes processing in formal declaration order. Constant actuals/defaults are evaluated and checked against the elaborated formal subtype; generic types denote elaborated actual subtypes, subprograms denote conforming actual declarations, and packages denote compatible instances. Staticness is classified by the language locally/global-static rules, not by a universal compile-time Boolean flag; generic constants are not automatically locally static. Generate controls obey their context-required staticness. No synthesis guarantee, hardware cost, signal/process/delta-cycle semantics, full configuration binding or universal termination is assumed. A failed elaboration does not promise rollback of partial compiler state.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/VHDLGenericElaboration"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-vhdl2019"
    ],
    "sourceLocator": "IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements",
    "sourceNote": "Models phase order, explicit checks and finite generate expansion, retaining the distinction between VHDL elaboration and C++ constant-expression evaluation.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/VHDLGenericElaboration-kind-specific-elaboration",
    "type": "Axiom",
    "name": "kind-specific-elaboration",
    "statement": "A constant actual must fit the elaborated formal subtype; a formal type denotes its elaborated actual subtype; formal subprogram/package associations must meet their conformance/matching obligations. Missing required or incompatible actuals prevent successful elaboration.",
    "formalStatement": "A constant actual must fit the elaborated formal subtype; a formal type denotes its elaborated actual subtype; formal subprogram/package associations must meet their conformance/matching obligations. Missing required or incompatible actuals prevent successful elaboration.",
    "assumptions": [
      "IEEE 1076-2019 selected finite elaboration profile. Association matching precedes processing in formal declaration order. Constant actuals/defaults are evaluated and checked against the elaborated formal subtype; generic types denote elaborated actual subtypes, subprograms denote conforming actual declarations, and packages denote compatible instances. Staticness is classified by the language locally/global-static rules, not by a universal compile-time Boolean flag; generic constants are not automatically locally static. Generate controls obey their context-required staticness. No synthesis guarantee, hardware cost, signal/process/delta-cycle semantics, full configuration binding or universal termination is assumed. A failed elaboration does not promise rollback of partial compiler state.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/VHDLGenericElaboration"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-vhdl2019"
    ],
    "sourceLocator": "IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements",
    "sourceNote": "Models phase order, explicit checks and finite generate expansion, retaining the distinction between VHDL elaboration and C++ constant-expression evaluation.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/VHDLGenericElaboration-static-generation",
    "type": "Axiom",
    "name": "static-generation",
    "statement": "For a valid finite discrete range R, forGenerate(R,B)=[B(i) | i∈R in declared direction]; valid single-condition ifGenerate(true,B)=[B] and ifGenerate(false,B)=[]. Locally/global-static status is supplied by the cited language rules.",
    "formalStatement": "For a valid finite discrete range R, forGenerate(R,B)=[B(i) | i∈R in declared direction]; valid single-condition ifGenerate(true,B)=[B] and ifGenerate(false,B)=[]. Locally/global-static status is supplied by the cited language rules.",
    "assumptions": [
      "IEEE 1076-2019 selected finite elaboration profile. Association matching precedes processing in formal declaration order. Constant actuals/defaults are evaluated and checked against the elaborated formal subtype; generic types denote elaborated actual subtypes, subprograms denote conforming actual declarations, and packages denote compatible instances. Staticness is classified by the language locally/global-static rules, not by a universal compile-time Boolean flag; generic constants are not automatically locally static. Generate controls obey their context-required staticness. No synthesis guarantee, hardware cost, signal/process/delta-cycle semantics, full configuration binding or universal termination is assumed. A failed elaboration does not promise rollback of partial compiler state.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/VHDLGenericElaboration"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-vhdl2019"
    ],
    "sourceLocator": "IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements",
    "sourceNote": "Models phase order, explicit checks and finite generate expansion, retaining the distinction between VHDL elaboration and C++ constant-expression evaluation.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/VHDLGenericElaboration-null-generate-empty",
    "type": "Law",
    "name": "null-generate-empty",
    "statement": "R is a valid null discrete range ⇒ forGenerate(R,B)=[].",
    "formalStatement": "R is a valid null discrete range ⇒ forGenerate(R,B)=[].",
    "assumptions": [
      "IEEE 1076-2019 selected finite elaboration profile. Association matching precedes processing in formal declaration order. Constant actuals/defaults are evaluated and checked against the elaborated formal subtype; generic types denote elaborated actual subtypes, subprograms denote conforming actual declarations, and packages denote compatible instances. Staticness is classified by the language locally/global-static rules, not by a universal compile-time Boolean flag; generic constants are not automatically locally static. Generate controls obey their context-required staticness. No synthesis guarantee, hardware cost, signal/process/delta-cycle semantics, full configuration binding or universal termination is assumed. A failed elaboration does not promise rollback of partial compiler state.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/VHDLGenericElaboration"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-vhdl2019"
    ],
    "sourceLocator": "IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements",
    "sourceNote": "Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/VHDLGenericElaboration-static-generation"
    ],
    "proofSketch": "A null discrete range has no values, so the indexed block list is empty; validity of the range is still required."
  },
  {
    "id": "urn:csabs:law/VHDLGenericElaboration-incompatible-actual-no-instance",
    "type": "Law",
    "name": "incompatible-actual-no-instance",
    "statement": "A required actual violates the kind-specific elaboration check ⇒ no successful elaboration instance is related.",
    "formalStatement": "A required actual violates the kind-specific elaboration check ⇒ no successful elaboration instance is related.",
    "assumptions": [
      "IEEE 1076-2019 selected finite elaboration profile. Association matching precedes processing in formal declaration order. Constant actuals/defaults are evaluated and checked against the elaborated formal subtype; generic types denote elaborated actual subtypes, subprograms denote conforming actual declarations, and packages denote compatible instances. Staticness is classified by the language locally/global-static rules, not by a universal compile-time Boolean flag; generic constants are not automatically locally static. Generate controls obey their context-required staticness. No synthesis guarantee, hardware cost, signal/process/delta-cycle semantics, full configuration binding or universal termination is assumed. A failed elaboration does not promise rollback of partial compiler state.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/VHDLGenericElaboration"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-vhdl2019"
    ],
    "sourceLocator": "IEEE 1076-2019 §§9.4.1–9.4.3;14.3.1–14.3.3.5;14.4.2.10 packages;14.5.3 generate statements",
    "sourceNote": "Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/VHDLGenericElaboration-elaboration-order",
      "urn:csabs:axiom/VHDLGenericElaboration-kind-specific-elaboration"
    ],
    "proofSketch": "Elaboration requires each declared generic association to pass its applicable check. Association normalization alone cannot supply a valid instance."
  }
]
```
<!-- graph-record:end -->
