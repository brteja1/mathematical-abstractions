# Java generic inference constraints and resolution obligations

A staged constraint/bound interface for unknown generic argument types, separating applicability, target-type constraints, reduction, incorporation and sound resolution.

**Notation:** θ:InferenceVar→ProperType; Sol(B)={θ | every bound/compatibility obligation in B holds under θ}; infer(Γ,call,target)⇀θ

**Stable ID:** `urn:csabs:concept/JavaTypeInference`

**Categories:** Programming-language semantics → Generic programming → Java generics

**Kind:** semantic-model

**Prerequisites:** [Java bounded parameterized types and nominal subtyping](JavaParameterizedType.md), [Java wildcard capture with fresh bounded variables](JavaWildcardCapture.md), [Binary relation](Relation.md)

**Related concepts:** [Contextual parametric declaration instantiation](ParametricInstantiation.md), [Normalized template constraints with atomic identity](TemplateConstraint.md)

## Backlinks

- [Java bounded parameterized types and nominal subtyping](JavaParameterizedType.md) — `relatedConcept`
- [Java wildcard capture with fresh bounded variables](JavaWildcardCapture.md) — `relatedConcept`

## Mathematical formulation

For constraints C and assignment θ:Var→Ty, Solution(C,θ) ⇔ (∀v,proper(θ(v))∧inScope(θ(v)))∧∀c∈C,satisfies(θ,c). A supplied resolver must satisfy resolve(C)=some(θ)⇒Solution(C,θ). Completeness or a JLS Chapter 18 algorithm is not encoded.

**Lean formulation** (in its source module context):

```lean
structure JavaTypeInference (Var Ty Constraint : Type u) where
  proper : Ty → Prop
  inScope : Ty → Prop
  satisfies : (Var → Ty) → Constraint → Prop
  resolve : List Constraint → Option (Var → Ty)
  resolution_sound : ∀ constraints assignment, resolve constraints = some assignment →
    (∀ v, proper (assignment v) ∧ inScope (assignment v)) ∧
      ∀ c ∈ constraints, satisfies assignment c
```

**Source:** [`Catalog.Generics.JavaTypeInference`](../lean/Catalog/GenericProgramming.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Assignments to proper in-scope types, supplied interpreted constraints and an explicitly sound partial resolver; solutions is the all-obligations predicate.

**Limits:** Actual JLS reduction, incorporation, applicability/target stages, capture/boxing/lambda rules and resolution algorithms are not implemented. Soundness is an explicit structure hypothesis, not proof about javac or arbitrary resolver code.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected defining rules: Sol(B)={θ | θ maps inference variables to in-scope proper types and ∀b∈B, satisfiesBound(θ,b)}. addTarget(B,T)=B∪T; resolution success requires θ∈Sol(B∪T) when a target is required; applicability alone uses its argument-stage obligations. resolve(Γ,B)=Some(θ) ⇒ θ∈Sol(B); no converse, uniqueness or completeness is assumed for the supplied JLS-stage adapter.

**basisKind:** extensional-structural-definition

**basisScope:** Java SE 25 JLS Chapter 18-inspired relational interface. Inference variables differ from declaration variables and capture variables. Proper types contain no inference variables. Compatibility, subtyping, boxing, capture, expression scope and throws constraints require language adapters. Reduction and resolution follow staged source rules; a chosen successful result must satisfy the applicable obligations, but this abstraction does not assert completeness, a unique/principal solution, or that every mathematical solution is selectable by Java inference. Applicability and target compatibility are separate checks. Lambdas/method references, overload selection and all Chapter 18 algorithms are not implemented here.

**verificationObligation:** Map language edition, carriers, identity, binding, substitution and phase-specific definedness explicitly.; Shared profiles do not transfer language rules; structural validation and model compilation do not prove language conformance.

**reviewStatus:** Editorial source/interface review; selected Lean interpretations are separate from theorem witnesses.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-JavaTypeInference-solutions"></a>

### solutions

`urn:csabs:operation/JavaTypeInference-solutions`

**signature:** solutions : BoundSet→𝒫(Assignment)

**description:** Return assignments to in-scope proper types satisfying every interpreted bound and compatibility constraint.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** Return assignments to in-scope proper types satisfying every interpreted bound and compatibility constraint.

**totality:** Total mathematical operation on the stated carrier.

**source:** [Java Language Specification, Java SE 25, Chapter 18: Type Inference](https://docs.oracle.com/javase/specs/jls/se25/html/jls-18.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§18.1–18.4 and18.5.1–18.5.2, applicability versus target compatibility; §18.2 completeness limitations

**sourceNote:** Records semantic solution obligations and stage boundaries rather than a complete Java inference engine or arbitrary logical constraint solver.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-JavaTypeInference-add-target"></a>

### add-target

`urn:csabs:operation/JavaTypeInference-add-target`

**signature:** addTarget : BoundSet×TargetConstraints→BoundSet

**description:** Conjoin target-type obligations to the already applicable invocation bound set; argument-derived obligations are retained.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** Conjoin target-type obligations to the already applicable invocation bound set; argument-derived obligations are retained.

**totality:** Total mathematical operation on the stated carrier.

**source:** [Java Language Specification, Java SE 25, Chapter 18: Type Inference](https://docs.oracle.com/javase/specs/jls/se25/html/jls-18.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§18.1–18.4 and18.5.1–18.5.2, applicability versus target compatibility; §18.2 completeness limitations

**sourceNote:** Records semantic solution obligations and stage boundaries rather than a complete Java inference engine or arbitrary logical constraint solver.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-JavaTypeInference-resolve"></a>

### resolve

`urn:csabs:operation/JavaTypeInference-resolve`

**signature:** resolve : Γ×BoundSet⇀Assignment

**description:** A supplied resolution procedure may return only an assignment satisfying the selected bounds and scope rules; failure is not automatically proof that the semantic solution set is empty.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** A supplied resolution procedure may return only an assignment satisfying the selected bounds and scope rules; failure is not automatically proof that the semantic solution set is empty.

**totality:** Total mathematical operation on the stated carrier.

**source:** [Java Language Specification, Java SE 25, Chapter 18: Type Inference](https://docs.oracle.com/javase/specs/jls/se25/html/jls-18.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§18.1–18.4 and18.5.1–18.5.2, applicability versus target compatibility; §18.2 completeness limitations

**sourceNote:** Records semantic solution obligations and stage boundaries rather than a complete Java inference engine or arbitrary logical constraint solver.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-JavaTypeInference-solution-set"></a>

### solution-set

`urn:csabs:axiom/JavaTypeInference-solution-set`

**statement:** Sol(B)={θ | θ maps inference variables to in-scope proper types and ∀b∈B, satisfiesBound(θ,b)}.

**formalStatement:** Sol(B)={θ | θ maps inference variables to in-scope proper types and ∀b∈B, satisfiesBound(θ,b)}.

**assumptions:** Java SE 25 JLS Chapter 18-inspired relational interface. Inference variables differ from declaration variables and capture variables. Proper types contain no inference variables. Compatibility, subtyping, boxing, capture, expression scope and throws constraints require language adapters. Reduction and resolution follow staged source rules; a chosen successful result must satisfy the applicable obligations, but this abstraction does not assert completeness, a unique/principal solution, or that every mathematical solution is selectable by Java inference. Applicability and target compatibility are separate checks. Lambdas/method references, overload selection and all Chapter 18 algorithms are not implemented here.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, Chapter 18: Type Inference](https://docs.oracle.com/javase/specs/jls/se25/html/jls-18.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§18.1–18.4 and18.5.1–18.5.2, applicability versus target compatibility; §18.2 completeness limitations

**sourceNote:** Records semantic solution obligations and stage boundaries rather than a complete Java inference engine or arbitrary logical constraint solver.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-JavaTypeInference-target-conjunction"></a>

### target-conjunction

`urn:csabs:axiom/JavaTypeInference-target-conjunction`

**statement:** addTarget(B,T)=B∪T; resolution success requires θ∈Sol(B∪T) when a target is required; applicability alone uses its argument-stage obligations.

**formalStatement:** addTarget(B,T)=B∪T; resolution success requires θ∈Sol(B∪T) when a target is required; applicability alone uses its argument-stage obligations.

**assumptions:** Java SE 25 JLS Chapter 18-inspired relational interface. Inference variables differ from declaration variables and capture variables. Proper types contain no inference variables. Compatibility, subtyping, boxing, capture, expression scope and throws constraints require language adapters. Reduction and resolution follow staged source rules; a chosen successful result must satisfy the applicable obligations, but this abstraction does not assert completeness, a unique/principal solution, or that every mathematical solution is selectable by Java inference. Applicability and target compatibility are separate checks. Lambdas/method references, overload selection and all Chapter 18 algorithms are not implemented here.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, Chapter 18: Type Inference](https://docs.oracle.com/javase/specs/jls/se25/html/jls-18.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§18.1–18.4 and18.5.1–18.5.2, applicability versus target compatibility; §18.2 completeness limitations

**sourceNote:** Records semantic solution obligations and stage boundaries rather than a complete Java inference engine or arbitrary logical constraint solver.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-JavaTypeInference-sound-resolution"></a>

### sound-resolution

`urn:csabs:axiom/JavaTypeInference-sound-resolution`

**statement:** resolve(Γ,B)=Some(θ) ⇒ θ∈Sol(B); no converse, uniqueness or completeness is assumed for the supplied JLS-stage adapter.

**formalStatement:** resolve(Γ,B)=Some(θ) ⇒ θ∈Sol(B); no converse, uniqueness or completeness is assumed for the supplied JLS-stage adapter.

**assumptions:** Java SE 25 JLS Chapter 18-inspired relational interface. Inference variables differ from declaration variables and capture variables. Proper types contain no inference variables. Compatibility, subtyping, boxing, capture, expression scope and throws constraints require language adapters. Reduction and resolution follow staged source rules; a chosen successful result must satisfy the applicable obligations, but this abstraction does not assert completeness, a unique/principal solution, or that every mathematical solution is selectable by Java inference. Applicability and target compatibility are separate checks. Lambdas/method references, overload selection and all Chapter 18 algorithms are not implemented here.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, Chapter 18: Type Inference](https://docs.oracle.com/javase/specs/jls/se25/html/jls-18.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§18.1–18.4 and18.5.1–18.5.2, applicability versus target compatibility; §18.2 completeness limitations

**sourceNote:** Records semantic solution obligations and stage boundaries rather than a complete Java inference engine or arbitrary logical constraint solver.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-JavaTypeInference-target-narrows-solutions"></a>

### target-narrows-solutions

`urn:csabs:law/JavaTypeInference-target-narrows-solutions`

**statement:** Sol(B∪T)=Sol(B)∩Sol(T), hence Sol(B∪T)⊆Sol(B).

**formalStatement:** Sol(B∪T)=Sol(B)∩Sol(T), hence Sol(B∪T)⊆Sol(B).

**assumptions:** Java SE 25 JLS Chapter 18-inspired relational interface. Inference variables differ from declaration variables and capture variables. Proper types contain no inference variables. Compatibility, subtyping, boxing, capture, expression scope and throws constraints require language adapters. Reduction and resolution follow staged source rules; a chosen successful result must satisfy the applicable obligations, but this abstraction does not assert completeness, a unique/principal solution, or that every mathematical solution is selectable by Java inference. Applicability and target compatibility are separate checks. Lambdas/method references, overload selection and all Chapter 18 algorithms are not implemented here.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, Chapter 18: Type Inference](https://docs.oracle.com/javase/specs/jls/se25/html/jls-18.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§18.1–18.4 and18.5.1–18.5.2, applicability versus target compatibility; §18.2 completeness limitations

**sourceNote:** Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.

**provenanceKind:** derived

**dependsOn:** [solution-set](JavaTypeInference.md#node-urn-csabs-axiom-JavaTypeInference-solution-set); [target-conjunction](JavaTypeInference.md#node-urn-csabs-axiom-JavaTypeInference-target-conjunction)

**proofSketch:** An assignment satisfies every obligation in a union exactly when it satisfies each set; the same scope/proper-type universe is used on both sides.

<a id="node-urn-csabs-law-JavaTypeInference-failed-target-no-resolution"></a>

### failed-target-no-resolution

`urn:csabs:law/JavaTypeInference-failed-target-no-resolution`

**statement:** Sol(B)≠∅ ∧ Sol(B∪T)=∅ ⇒ no successful resolution of B∪T, even though argument-stage solutions exist.

**formalStatement:** Sol(B)≠∅ ∧ Sol(B∪T)=∅ ⇒ no successful resolution of B∪T, even though argument-stage solutions exist.

**assumptions:** Java SE 25 JLS Chapter 18-inspired relational interface. Inference variables differ from declaration variables and capture variables. Proper types contain no inference variables. Compatibility, subtyping, boxing, capture, expression scope and throws constraints require language adapters. Reduction and resolution follow staged source rules; a chosen successful result must satisfy the applicable obligations, but this abstraction does not assert completeness, a unique/principal solution, or that every mathematical solution is selectable by Java inference. Applicability and target compatibility are separate checks. Lambdas/method references, overload selection and all Chapter 18 algorithms are not implemented here.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, Chapter 18: Type Inference](https://docs.oracle.com/javase/specs/jls/se25/html/jls-18.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§18.1–18.4 and18.5.1–18.5.2, applicability versus target compatibility; §18.2 completeness limitations

**sourceNote:** Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.

**provenanceKind:** derived

**dependsOn:** [target-conjunction](JavaTypeInference.md#node-urn-csabs-axiom-JavaTypeInference-target-conjunction); [sound-resolution](JavaTypeInference.md#node-urn-csabs-axiom-JavaTypeInference-sound-resolution)

**proofSketch:** Sound resolution would produce a member of the empty target-stage solution set. Applicability without a target does not supply that member.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Java Language Specification, Java SE 25, Chapter 18: Type Inference](https://docs.oracle.com/javase/specs/jls/se25/html/jls-18.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§18.1–18.4 and18.5.1–18.5.2, applicability versus target compatibility; §18.2 completeness limitations

**sourceNote:** Records semantic solution obligations and stage boundaries rather than a complete Java inference engine or arbitrary logical constraint solver.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/JavaTypeInference",
    "type": "Concept",
    "shortForm": "JavaTypeInference",
    "fullName": "Java generic inference constraints and resolution obligations",
    "definition": "A staged constraint/bound interface for unknown generic argument types, separating applicability, target-type constraints, reduction, incorporation and sound resolution.",
    "notation": "θ:InferenceVar→ProperType; Sol(B)={θ | every bound/compatibility obligation in B holds under θ}; infer(Γ,call,target)⇀θ",
    "category": [
      "urn:csabs:category/java-generics"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/JavaParameterizedType",
      "urn:csabs:concept/JavaWildcardCapture",
      "urn:csabs:concept/Relation"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ParametricInstantiation",
      "urn:csabs:concept/TemplateConstraint"
    ],
    "hasOperation": [
      "urn:csabs:operation/JavaTypeInference-solutions",
      "urn:csabs:operation/JavaTypeInference-add-target",
      "urn:csabs:operation/JavaTypeInference-resolve"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/JavaTypeInference-solution-set",
      "urn:csabs:axiom/JavaTypeInference-target-conjunction",
      "urn:csabs:axiom/JavaTypeInference-sound-resolution"
    ],
    "hasLaw": [
      "urn:csabs:law/JavaTypeInference-target-narrows-solutions",
      "urn:csabs:law/JavaTypeInference-failed-target-no-resolution"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "Java SE 25 JLS Chapter 18-inspired relational interface. Inference variables differ from declaration variables and capture variables. Proper types contain no inference variables. Compatibility, subtyping, boxing, capture, expression scope and throws constraints require language adapters. Reduction and resolution follow staged source rules; a chosen successful result must satisfy the applicable obligations, but this abstraction does not assert completeness, a unique/principal solution, or that every mathematical solution is selectable by Java inference. Applicability and target compatibility are separate checks. Lambdas/method references, overload selection and all Chapter 18 algorithms are not implemented here.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; selected Lean interpretations are separate from theorem witnesses.",
    "verificationObligation": [
      "Map language edition, carriers, identity, binding, substitution and phase-specific definedness explicitly.",
      "Shared profiles do not transfer language rules; structural validation and model compilation do not prove language conformance."
    ],
    "source": [
      "urn:csabs:source/generics-jls25-inference"
    ],
    "sourceLocator": "JLS §§18.1–18.4 and18.5.1–18.5.2, applicability versus target compatibility; §18.2 completeness limitations",
    "sourceNote": "Records semantic solution obligations and stage boundaries rather than a complete Java inference engine or arbitrary logical constraint solver.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: Sol(B)={θ | θ maps inference variables to in-scope proper types and ∀b∈B, satisfiesBound(θ,b)}. addTarget(B,T)=B∪T; resolution success requires θ∈Sol(B∪T) when a target is required; applicability alone uses its argument-stage obligations. resolve(Γ,B)=Some(θ) ⇒ θ∈Sol(B); no converse, uniqueness or completeness is assumed for the supplied JLS-stage adapter.",
    "leanFormulation": "structure JavaTypeInference (Var Ty Constraint : Type u) where\n  proper : Ty → Prop\n  inScope : Ty → Prop\n  satisfies : (Var → Ty) → Constraint → Prop\n  resolve : List Constraint → Option (Var → Ty)\n  resolution_sound : ∀ constraints assignment, resolve constraints = some assignment →\n    (∀ v, proper (assignment v) ∧ inScope (assignment v)) ∧\n      ∀ c ∈ constraints, satisfies assignment c",
    "formulationSource": "urn:csabs:source/local-lean-GenericProgramming",
    "formulationLocator": "Catalog.Generics.JavaTypeInference",
    "formulationScope": "partial",
    "leanModelMapping": "Assignments to proper in-scope types, supplied interpreted constraints and an explicitly sound partial resolver; solutions is the all-obligations predicate.",
    "leanModelLimitations": "Actual JLS reduction, incorporation, applicability/target stages, capture/boxing/lambda rules and resolution algorithms are not implemented. Soundness is an explicit structure hypothesis, not proof about javac or arbitrary resolver code.",
    "mathematicalFormulation": "For constraints C and assignment θ:Var→Ty, Solution(C,θ) ⇔ (∀v,proper(θ(v))∧inScope(θ(v)))∧∀c∈C,satisfies(θ,c). A supplied resolver must satisfy resolve(C)=some(θ)⇒Solution(C,θ). Completeness or a JLS Chapter 18 algorithm is not encoded."
  },
  {
    "id": "urn:csabs:operation/JavaTypeInference-solutions",
    "type": "Operation",
    "name": "solutions",
    "signature": "solutions : BoundSet→𝒫(Assignment)",
    "description": "Return assignments to in-scope proper types satisfying every interpreted bound and compatibility constraint.",
    "concept": "urn:csabs:concept/JavaTypeInference",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "Return assignments to in-scope proper types satisfying every interpreted bound and compatibility constraint.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-jls25-inference"
    ],
    "sourceLocator": "JLS §§18.1–18.4 and18.5.1–18.5.2, applicability versus target compatibility; §18.2 completeness limitations",
    "sourceNote": "Records semantic solution obligations and stage boundaries rather than a complete Java inference engine or arbitrary logical constraint solver.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/JavaTypeInference-add-target",
    "type": "Operation",
    "name": "add-target",
    "signature": "addTarget : BoundSet×TargetConstraints→BoundSet",
    "description": "Conjoin target-type obligations to the already applicable invocation bound set; argument-derived obligations are retained.",
    "concept": "urn:csabs:concept/JavaTypeInference",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "Conjoin target-type obligations to the already applicable invocation bound set; argument-derived obligations are retained.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-jls25-inference"
    ],
    "sourceLocator": "JLS §§18.1–18.4 and18.5.1–18.5.2, applicability versus target compatibility; §18.2 completeness limitations",
    "sourceNote": "Records semantic solution obligations and stage boundaries rather than a complete Java inference engine or arbitrary logical constraint solver.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/JavaTypeInference-resolve",
    "type": "Operation",
    "name": "resolve",
    "signature": "resolve : Γ×BoundSet⇀Assignment",
    "description": "A supplied resolution procedure may return only an assignment satisfying the selected bounds and scope rules; failure is not automatically proof that the semantic solution set is empty.",
    "concept": "urn:csabs:concept/JavaTypeInference",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "A supplied resolution procedure may return only an assignment satisfying the selected bounds and scope rules; failure is not automatically proof that the semantic solution set is empty.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-jls25-inference"
    ],
    "sourceLocator": "JLS §§18.1–18.4 and18.5.1–18.5.2, applicability versus target compatibility; §18.2 completeness limitations",
    "sourceNote": "Records semantic solution obligations and stage boundaries rather than a complete Java inference engine or arbitrary logical constraint solver.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/JavaTypeInference-solution-set",
    "type": "Axiom",
    "name": "solution-set",
    "statement": "Sol(B)={θ | θ maps inference variables to in-scope proper types and ∀b∈B, satisfiesBound(θ,b)}.",
    "formalStatement": "Sol(B)={θ | θ maps inference variables to in-scope proper types and ∀b∈B, satisfiesBound(θ,b)}.",
    "assumptions": [
      "Java SE 25 JLS Chapter 18-inspired relational interface. Inference variables differ from declaration variables and capture variables. Proper types contain no inference variables. Compatibility, subtyping, boxing, capture, expression scope and throws constraints require language adapters. Reduction and resolution follow staged source rules; a chosen successful result must satisfy the applicable obligations, but this abstraction does not assert completeness, a unique/principal solution, or that every mathematical solution is selectable by Java inference. Applicability and target compatibility are separate checks. Lambdas/method references, overload selection and all Chapter 18 algorithms are not implemented here.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/JavaTypeInference"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-inference"
    ],
    "sourceLocator": "JLS §§18.1–18.4 and18.5.1–18.5.2, applicability versus target compatibility; §18.2 completeness limitations",
    "sourceNote": "Records semantic solution obligations and stage boundaries rather than a complete Java inference engine or arbitrary logical constraint solver.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/JavaTypeInference-target-conjunction",
    "type": "Axiom",
    "name": "target-conjunction",
    "statement": "addTarget(B,T)=B∪T; resolution success requires θ∈Sol(B∪T) when a target is required; applicability alone uses its argument-stage obligations.",
    "formalStatement": "addTarget(B,T)=B∪T; resolution success requires θ∈Sol(B∪T) when a target is required; applicability alone uses its argument-stage obligations.",
    "assumptions": [
      "Java SE 25 JLS Chapter 18-inspired relational interface. Inference variables differ from declaration variables and capture variables. Proper types contain no inference variables. Compatibility, subtyping, boxing, capture, expression scope and throws constraints require language adapters. Reduction and resolution follow staged source rules; a chosen successful result must satisfy the applicable obligations, but this abstraction does not assert completeness, a unique/principal solution, or that every mathematical solution is selectable by Java inference. Applicability and target compatibility are separate checks. Lambdas/method references, overload selection and all Chapter 18 algorithms are not implemented here.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/JavaTypeInference"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-inference"
    ],
    "sourceLocator": "JLS §§18.1–18.4 and18.5.1–18.5.2, applicability versus target compatibility; §18.2 completeness limitations",
    "sourceNote": "Records semantic solution obligations and stage boundaries rather than a complete Java inference engine or arbitrary logical constraint solver.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/JavaTypeInference-sound-resolution",
    "type": "Axiom",
    "name": "sound-resolution",
    "statement": "resolve(Γ,B)=Some(θ) ⇒ θ∈Sol(B); no converse, uniqueness or completeness is assumed for the supplied JLS-stage adapter.",
    "formalStatement": "resolve(Γ,B)=Some(θ) ⇒ θ∈Sol(B); no converse, uniqueness or completeness is assumed for the supplied JLS-stage adapter.",
    "assumptions": [
      "Java SE 25 JLS Chapter 18-inspired relational interface. Inference variables differ from declaration variables and capture variables. Proper types contain no inference variables. Compatibility, subtyping, boxing, capture, expression scope and throws constraints require language adapters. Reduction and resolution follow staged source rules; a chosen successful result must satisfy the applicable obligations, but this abstraction does not assert completeness, a unique/principal solution, or that every mathematical solution is selectable by Java inference. Applicability and target compatibility are separate checks. Lambdas/method references, overload selection and all Chapter 18 algorithms are not implemented here.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/JavaTypeInference"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-inference"
    ],
    "sourceLocator": "JLS §§18.1–18.4 and18.5.1–18.5.2, applicability versus target compatibility; §18.2 completeness limitations",
    "sourceNote": "Records semantic solution obligations and stage boundaries rather than a complete Java inference engine or arbitrary logical constraint solver.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/JavaTypeInference-target-narrows-solutions",
    "type": "Law",
    "name": "target-narrows-solutions",
    "statement": "Sol(B∪T)=Sol(B)∩Sol(T), hence Sol(B∪T)⊆Sol(B).",
    "formalStatement": "Sol(B∪T)=Sol(B)∩Sol(T), hence Sol(B∪T)⊆Sol(B).",
    "assumptions": [
      "Java SE 25 JLS Chapter 18-inspired relational interface. Inference variables differ from declaration variables and capture variables. Proper types contain no inference variables. Compatibility, subtyping, boxing, capture, expression scope and throws constraints require language adapters. Reduction and resolution follow staged source rules; a chosen successful result must satisfy the applicable obligations, but this abstraction does not assert completeness, a unique/principal solution, or that every mathematical solution is selectable by Java inference. Applicability and target compatibility are separate checks. Lambdas/method references, overload selection and all Chapter 18 algorithms are not implemented here.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/JavaTypeInference"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-inference"
    ],
    "sourceLocator": "JLS §§18.1–18.4 and18.5.1–18.5.2, applicability versus target compatibility; §18.2 completeness limitations",
    "sourceNote": "Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/JavaTypeInference-solution-set",
      "urn:csabs:axiom/JavaTypeInference-target-conjunction"
    ],
    "proofSketch": "An assignment satisfies every obligation in a union exactly when it satisfies each set; the same scope/proper-type universe is used on both sides."
  },
  {
    "id": "urn:csabs:law/JavaTypeInference-failed-target-no-resolution",
    "type": "Law",
    "name": "failed-target-no-resolution",
    "statement": "Sol(B)≠∅ ∧ Sol(B∪T)=∅ ⇒ no successful resolution of B∪T, even though argument-stage solutions exist.",
    "formalStatement": "Sol(B)≠∅ ∧ Sol(B∪T)=∅ ⇒ no successful resolution of B∪T, even though argument-stage solutions exist.",
    "assumptions": [
      "Java SE 25 JLS Chapter 18-inspired relational interface. Inference variables differ from declaration variables and capture variables. Proper types contain no inference variables. Compatibility, subtyping, boxing, capture, expression scope and throws constraints require language adapters. Reduction and resolution follow staged source rules; a chosen successful result must satisfy the applicable obligations, but this abstraction does not assert completeness, a unique/principal solution, or that every mathematical solution is selectable by Java inference. Applicability and target compatibility are separate checks. Lambdas/method references, overload selection and all Chapter 18 algorithms are not implemented here.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/JavaTypeInference"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-inference"
    ],
    "sourceLocator": "JLS §§18.1–18.4 and18.5.1–18.5.2, applicability versus target compatibility; §18.2 completeness limitations",
    "sourceNote": "Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/JavaTypeInference-target-conjunction",
      "urn:csabs:axiom/JavaTypeInference-sound-resolution"
    ],
    "proofSketch": "Sound resolution would produce a member of the empty target-stage solution set. Applicability without a target does not supply that member."
  }
]
```
<!-- graph-record:end -->
