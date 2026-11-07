# Total function

A mapping assigning each element of a domain exactly one element of a codomain.

**Notation:** f : A → B; ∀a∈A ∃!b∈B: f(a)=b.

**Stable ID:** `urn:csabs:concept/Function`

**Categories:** Set theory and foundations

**Kind:** Function

**Specializes:** [Partial function](PartialFunction.md)

**Related concepts:** [Partial function](PartialFunction.md), [Cartesian product](CartesianProduct.md)

## Backlinks

- [Deterministic finite automaton with total transition](DFA.md) — `requiresConcept`
- [Empty type](EmptyType.md) — `requiresConcept`
- [Fixed Point](FixedPoint.md) — `requiresConcept`
- [Function type](FunctionType.md) — `requiresConcept`
- [Functional dependency on a relational schema](FunctionalDependency.md) — `relatedConcept`
- [Linear map](LinearMap.md) — `requiresConcept`
- [Linear map](LinearMap.md) — `specializationOf`
- [Finite rectangular matrix over a field](Matrix.md) — `requiresConcept`
- [Finite rectangular matrix over a field](Matrix.md) — `specializationOf`
- [Measurable function](MeasurableFunction.md) — `requiresConcept`
- [Measurable function](MeasurableFunction.md) — `specializationOf`
- [Monotone Function](MonotoneFunction.md) — `requiresConcept`
- [Monotone Function](MonotoneFunction.md) — `specializationOf`
- [Partial function](PartialFunction.md) — `requiresConcept`
- [Pigeonhole Principle](PigeonholePrinciple.md) — `requiresConcept`
- [Named relational schema with attribute domains](RelationalSchema.md) — `requiresConcept`
- [Unit type](UnitType.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Selected presentation: A mapping assigning each element of a domain exactly one element of a codomain. Governing rules: Every element of the domain has an output in the codomain. Each input has at most one output. A total function is a single-valued total relation with specified domain and codomain. Typed functions are equal if they agree on every input. Composition evaluates the right function first.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:** Take the defined domain D=A; evaluation and extensional equality then agree with the total-function interface.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-function-identity"></a>

### identity

`urn:csabs:operation/function-identity`

**signature:** id_A : A → A; id_A(x)=x

**description:** Maps each value to itself.

<a id="node-urn-csabs-operation-function-composition"></a>

### composition

`urn:csabs:operation/function-composition`

**signature:** ∘ : (B→C) × (A→B) → (A→C)

**description:** Applies the right-hand function first, then the left-hand function.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-function-totality"></a>

### function-totality

`urn:csabs:axiom/function-totality`

**statement:** Every element of the domain has an output in the codomain.

**formalStatement:** ∀a∈A ∃b∈B: f(a)=b

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-function-functionality"></a>

### function-functionality

`urn:csabs:axiom/function-functionality`

**statement:** Each input has at most one output.

**formalStatement:** ∀a∈A,b₁,b₂∈B: f(a)=b₁ ∧ f(a)=b₂ ⇒ b₁=b₂

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Function-graph"></a>

### graph

`urn:csabs:axiom/Function-graph`

**statement:** A total function is a single-valued total relation with specified domain and codomain.

**formalStatement:** graph(f)⊆A×B; ∀a∈A ∃!b∈B: (a,b)∈graph(f)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Function-extensionality"></a>

### extensionality

`urn:csabs:axiom/Function-extensionality`

**statement:** Typed functions are equal if they agree on every input.

**formalStatement:** f,g:A→B; f=g iff ∀a∈A: f(a)=g(a)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Function-compose-definition"></a>

### compose-definition

`urn:csabs:axiom/Function-compose-definition`

**statement:** Composition evaluates the right function first.

**formalStatement:** (g∘f)(a)=g(f(a))

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-function-composition-associative"></a>

### law/function-composition-associative

`urn:csabs:law/function-composition-associative`

**statement:** Typed function composition is associative.

**formalStatement:** h∘(g∘f)=(h∘g)∘f

**assumptions:** codomains and domains are compatible

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [function-totality](Function.md#node-urn-csabs-axiom-function-totality); [function-functionality](Function.md#node-urn-csabs-axiom-function-functionality); [graph](Function.md#node-urn-csabs-axiom-Function-graph); [extensionality](Function.md#node-urn-csabs-axiom-Function-extensionality); [compose-definition](Function.md#node-urn-csabs-axiom-Function-compose-definition)

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-law-function-identity"></a>

### law/function-identity

`urn:csabs:law/function-identity`

**statement:** Identity functions are left and right identities for composition.

**formalStatement:** id_B∘f=f=f∘id_A

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [function-totality](Function.md#node-urn-csabs-axiom-function-totality); [function-functionality](Function.md#node-urn-csabs-axiom-function-functionality); [graph](Function.md#node-urn-csabs-axiom-Function-graph); [extensionality](Function.md#node-urn-csabs-axiom-Function-extensionality); [compose-definition](Function.md#node-urn-csabs-axiom-Function-compose-definition)

**assumptions:** Use the explicit mathematical bases and typed carriers of the linked concepts.

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-bijection-inverse"></a>

### theorem/bijection-inverse

`urn:csabs:theorem/bijection-inverse`

**statement:** A total function is bijective iff it has a two-sided inverse function.

**formalStatement:** f:A→B bijective ⇔ ∃g:B→A: g∘f=id_A ∧ f∘g=id_B

**reviewStatus:** editorial-summary; not machine-proved

**proofSketch:** Unique preimages of a bijection define the inverse; the two inverse identities imply injectivity and surjectivity in the other direction.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [function-totality](Function.md#node-urn-csabs-axiom-function-totality); [function-functionality](Function.md#node-urn-csabs-axiom-function-functionality); [graph](Function.md#node-urn-csabs-axiom-Function-graph); [extensionality](Function.md#node-urn-csabs-axiom-Function-extensionality); [compose-definition](Function.md#node-urn-csabs-axiom-Function-compose-definition)

**assumptions:** Use the explicit mathematical bases and typed carriers of the linked concepts.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-theorem-Function-composition-injective"></a>

### composition-injective

`urn:csabs:theorem/Function-composition-injective`

**statement:** The composite of two injective total functions is injective.

**formalStatement:** f,g injective ⇒ g∘f injective

**proofSketch:** From g(f(x))=g(f(y)), cancel g and then f.

**assumptions:** The explicit basis, carriers, and side conditions stated for Function apply.

**dependsOn:** [function-totality](Function.md#node-urn-csabs-axiom-function-totality); [function-functionality](Function.md#node-urn-csabs-axiom-function-functionality); [graph](Function.md#node-urn-csabs-axiom-Function-graph); [extensionality](Function.md#node-urn-csabs-axiom-Function-extensionality); [compose-definition](Function.md#node-urn-csabs-axiom-Function-compose-definition)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

Historical source gap retained; see `provenanceStatus` and the frozen baseline.

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Function",
    "type": "Concept",
    "shortForm": "Function",
    "fullName": "Total function",
    "category": [
      "urn:csabs:category/foundations"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "A mapping assigning each element of a domain exactly one element of a codomain.",
    "notation": "f : A → B; ∀a∈A ∃!b∈B: f(a)=b.",
    "hasOperation": [
      "urn:csabs:operation/function-identity",
      "urn:csabs:operation/function-composition"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/function-totality",
      "urn:csabs:axiom/function-functionality",
      "urn:csabs:axiom/Function-graph",
      "urn:csabs:axiom/Function-extensionality",
      "urn:csabs:axiom/Function-compose-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/function-composition-associative",
      "urn:csabs:law/function-identity"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/bijection-inverse",
      "urn:csabs:theorem/Function-composition-injective"
    ],
    "relatedConcept": [
      "urn:csabs:concept/PartialFunction",
      "urn:csabs:concept/CartesianProduct"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A mapping assigning each element of a domain exactly one element of a codomain. Governing rules: Every element of the domain has an output in the codomain. Each input has at most one output. A total function is a single-valued total relation with specified domain and codomain. Typed functions are equal if they agree on every input. Composition evaluates the right function first.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "specializationOf": [
      "urn:csabs:concept/PartialFunction"
    ],
    "specializationNote": "Take the defined domain D=A; evaluation and extensional equality then agree with the total-function interface."
  },
  {
    "id": "urn:csabs:operation/function-identity",
    "type": "Operation",
    "name": "identity",
    "signature": "id_A : A → A; id_A(x)=x",
    "description": "Maps each value to itself.",
    "concept": "urn:csabs:concept/Function"
  },
  {
    "id": "urn:csabs:operation/function-composition",
    "type": "Operation",
    "name": "composition",
    "signature": "∘ : (B→C) × (A→B) → (A→C)",
    "description": "Applies the right-hand function first, then the left-hand function.",
    "concept": "urn:csabs:concept/Function"
  },
  {
    "id": "urn:csabs:axiom/function-totality",
    "type": "Axiom",
    "statement": "Every element of the domain has an output in the codomain.",
    "formalStatement": "∀a∈A ∃b∈B: f(a)=b",
    "appliesTo": [
      "urn:csabs:concept/Function"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "function-totality",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/function-functionality",
    "type": "Axiom",
    "statement": "Each input has at most one output.",
    "formalStatement": "∀a∈A,b₁,b₂∈B: f(a)=b₁ ∧ f(a)=b₂ ⇒ b₁=b₂",
    "appliesTo": [
      "urn:csabs:concept/Function"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "function-functionality",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Function-graph",
    "type": "Axiom",
    "name": "graph",
    "statement": "A total function is a single-valued total relation with specified domain and codomain.",
    "formalStatement": "graph(f)⊆A×B; ∀a∈A ∃!b∈B: (a,b)∈graph(f)",
    "appliesTo": [
      "urn:csabs:concept/Function"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Function-extensionality",
    "type": "Axiom",
    "name": "extensionality",
    "statement": "Typed functions are equal if they agree on every input.",
    "formalStatement": "f,g:A→B; f=g iff ∀a∈A: f(a)=g(a)",
    "appliesTo": [
      "urn:csabs:concept/Function"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Function-compose-definition",
    "type": "Axiom",
    "name": "compose-definition",
    "statement": "Composition evaluates the right function first.",
    "formalStatement": "(g∘f)(a)=g(f(a))",
    "appliesTo": [
      "urn:csabs:concept/Function"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/function-composition-associative",
    "type": "Law",
    "statement": "Typed function composition is associative.",
    "formalStatement": "h∘(g∘f)=(h∘g)∘f",
    "assumptions": [
      "codomains and domains are compatible"
    ],
    "appliesTo": [
      "urn:csabs:concept/Function"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/function-totality",
      "urn:csabs:axiom/function-functionality",
      "urn:csabs:axiom/Function-graph",
      "urn:csabs:axiom/Function-extensionality",
      "urn:csabs:axiom/Function-compose-definition"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/function-identity",
    "type": "Law",
    "statement": "Identity functions are left and right identities for composition.",
    "formalStatement": "id_B∘f=f=f∘id_A",
    "appliesTo": [
      "urn:csabs:concept/Function"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/function-totality",
      "urn:csabs:axiom/function-functionality",
      "urn:csabs:axiom/Function-graph",
      "urn:csabs:axiom/Function-extensionality",
      "urn:csabs:axiom/Function-compose-definition"
    ],
    "assumptions": [
      "Use the explicit mathematical bases and typed carriers of the linked concepts."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/bijection-inverse",
    "type": "Theorem",
    "statement": "A total function is bijective iff it has a two-sided inverse function.",
    "formalStatement": "f:A→B bijective ⇔ ∃g:B→A: g∘f=id_A ∧ f∘g=id_B",
    "appliesTo": [
      "urn:csabs:concept/Function"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "proofSketch": "Unique preimages of a bijection define the inverse; the two inverse identities imply injectivity and surjectivity in the other direction.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/function-totality",
      "urn:csabs:axiom/function-functionality",
      "urn:csabs:axiom/Function-graph",
      "urn:csabs:axiom/Function-extensionality",
      "urn:csabs:axiom/Function-compose-definition"
    ],
    "assumptions": [
      "Use the explicit mathematical bases and typed carriers of the linked concepts."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Function-composition-injective",
    "type": "Theorem",
    "name": "composition-injective",
    "statement": "The composite of two injective total functions is injective.",
    "formalStatement": "f,g injective ⇒ g∘f injective",
    "proofSketch": "From g(f(x))=g(f(y)), cancel g and then f.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Function apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Function"
    ],
    "dependsOn": [
      "urn:csabs:axiom/function-totality",
      "urn:csabs:axiom/function-functionality",
      "urn:csabs:axiom/Function-graph",
      "urn:csabs:axiom/Function-extensionality",
      "urn:csabs:axiom/Function-compose-definition"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
