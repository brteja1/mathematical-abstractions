# Stack abstract data type

A collection supporting last-in, first-out insertion and removal, with empty behavior specified by the contract.

**Notation:** push : Stack×V→Stack; pop : Stack⇀Stack×V; top : Stack⇀V.

**Stable ID:** `urn:csabs:concept/Stack`

**Categories:** Data structures → Sequential collections

**Kind:** Abstract data type

## Interface and scope

**axiomBasis:** Selected presentation: A collection supporting last-in, first-out insertion and removal, with empty behavior specified by the contract. Governing rules: Stack values are finite sequences with the head as the top. Top and pop are defined exactly on nonempty stacks.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-stack-push"></a>

### push

`urn:csabs:operation/stack-push`

**signature:** push : Stack×V→Stack

**description:** Places a value at the top of the stack.

<a id="node-urn-csabs-operation-stack-pop"></a>

### pop

`urn:csabs:operation/stack-pop`

**signature:** pop : Stack⇀Stack×V

**description:** Removes and returns the top value and resulting stack.

**precondition:** stack is nonempty

<a id="node-urn-csabs-operation-stack-top"></a>

### top

`urn:csabs:operation/stack-top`

**signature:** top : Stack⇀V

**description:** Returns the most recently pushed value not yet removed.

**precondition:** stack is nonempty

<a id="node-urn-csabs-operation-Stack-basis-empty"></a>

### empty

`urn:csabs:operation/Stack-basis-empty`

**signature:** empty : Stack(V)

**description:** Returns the empty sequence model.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Stack-sequence-model"></a>

### sequence-model

`urn:csabs:axiom/Stack-sequence-model`

**statement:** Stack values are finite sequences with the head as the top.

**formalStatement:** Stack(V)=Seq(V); empty=nil; push(s,x)=cons(x,s)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Stack-observers"></a>

### observers

`urn:csabs:axiom/Stack-observers`

**statement:** Top and pop are defined exactly on nonempty stacks.

**formalStatement:** top(cons(x,s))=x; pop(cons(x,s))=(s,x); dom(top)=dom(pop)=Stack(V)−{empty}

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-stack-push-top"></a>

### law/stack-push-top

`urn:csabs:law/stack-push-top`

**statement:** Pushing x onto a stack makes x its top element.

**formalStatement:** top(push(S,x))=x

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [sequence-model](Stack.md#node-urn-csabs-axiom-Stack-sequence-model); [observers](Stack.md#node-urn-csabs-axiom-Stack-observers)

**assumptions:** Use the explicit mathematical bases and typed carriers of the linked concepts.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-law-stack-push-pop"></a>

### law/stack-push-pop

`urn:csabs:law/stack-push-pop`

**statement:** Popping immediately after a push returns the pushed value and prior stack.

**formalStatement:** pop(push(S,x))=(S,x)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [sequence-model](Stack.md#node-urn-csabs-axiom-Stack-sequence-model); [observers](Stack.md#node-urn-csabs-axiom-Stack-observers)

**assumptions:** Use the explicit mathematical bases and typed carriers of the linked concepts.

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-Stack-push-injective"></a>

### push-injective

`urn:csabs:theorem/Stack-push-injective`

**statement:** Pushing is injective in both the prior stack and the new value.

**formalStatement:** push(s,x)=push(t,y) ⇒ s=t ∧ x=y

**proofSketch:** Apply pop to the equality and use the push-pop equation.

**assumptions:** The explicit basis, carriers, and side conditions stated for Stack apply.

**dependsOn:** [sequence-model](Stack.md#node-urn-csabs-axiom-Stack-sequence-model); [observers](Stack.md#node-urn-csabs-axiom-Stack-observers)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

- [List of data structures (Wikipedia)](https://en.wikipedia.org/wiki/List_of_data_structures); sourceRole: discovery

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Stack",
    "type": "Concept",
    "shortForm": "Stack",
    "fullName": "Stack abstract data type",
    "category": [
      "urn:csabs:category/sequential-collections"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A collection supporting last-in, first-out insertion and removal, with empty behavior specified by the contract.",
    "notation": "push : Stack×V→Stack; pop : Stack⇀Stack×V; top : Stack⇀V.",
    "hasOperation": [
      "urn:csabs:operation/stack-push",
      "urn:csabs:operation/stack-pop",
      "urn:csabs:operation/stack-top",
      "urn:csabs:operation/Stack-basis-empty"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Stack-sequence-model",
      "urn:csabs:axiom/Stack-observers"
    ],
    "hasLaw": [
      "urn:csabs:law/stack-push-top",
      "urn:csabs:law/stack-push-pop"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Stack-push-injective"
    ],
    "source": [
      "urn:csabs:source/wikipedia-data-structures"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A collection supporting last-in, first-out insertion and removal, with empty behavior specified by the contract. Governing rules: Stack values are finite sequences with the head as the top. Top and pop are defined exactly on nonempty stacks.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof"
  },
  {
    "id": "urn:csabs:operation/stack-push",
    "type": "Operation",
    "name": "push",
    "signature": "push : Stack×V→Stack",
    "description": "Places a value at the top of the stack.",
    "concept": "urn:csabs:concept/Stack"
  },
  {
    "id": "urn:csabs:operation/stack-pop",
    "type": "Operation",
    "name": "pop",
    "signature": "pop : Stack⇀Stack×V",
    "description": "Removes and returns the top value and resulting stack.",
    "precondition": "stack is nonempty",
    "concept": "urn:csabs:concept/Stack"
  },
  {
    "id": "urn:csabs:operation/stack-top",
    "type": "Operation",
    "name": "top",
    "signature": "top : Stack⇀V",
    "description": "Returns the most recently pushed value not yet removed.",
    "precondition": "stack is nonempty",
    "concept": "urn:csabs:concept/Stack"
  },
  {
    "id": "urn:csabs:operation/Stack-basis-empty",
    "type": "Operation",
    "name": "empty",
    "signature": "empty : Stack(V)",
    "description": "Returns the empty sequence model.",
    "concept": "urn:csabs:concept/Stack"
  },
  {
    "id": "urn:csabs:axiom/Stack-sequence-model",
    "type": "Axiom",
    "name": "sequence-model",
    "statement": "Stack values are finite sequences with the head as the top.",
    "formalStatement": "Stack(V)=Seq(V); empty=nil; push(s,x)=cons(x,s)",
    "appliesTo": [
      "urn:csabs:concept/Stack"
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
    "id": "urn:csabs:axiom/Stack-observers",
    "type": "Axiom",
    "name": "observers",
    "statement": "Top and pop are defined exactly on nonempty stacks.",
    "formalStatement": "top(cons(x,s))=x; pop(cons(x,s))=(s,x); dom(top)=dom(pop)=Stack(V)−{empty}",
    "appliesTo": [
      "urn:csabs:concept/Stack"
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
    "id": "urn:csabs:law/stack-push-top",
    "type": "Law",
    "statement": "Pushing x onto a stack makes x its top element.",
    "formalStatement": "top(push(S,x))=x",
    "appliesTo": [
      "urn:csabs:concept/Stack"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/Stack-sequence-model",
      "urn:csabs:axiom/Stack-observers"
    ],
    "assumptions": [
      "Use the explicit mathematical bases and typed carriers of the linked concepts."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/stack-push-pop",
    "type": "Law",
    "statement": "Popping immediately after a push returns the pushed value and prior stack.",
    "formalStatement": "pop(push(S,x))=(S,x)",
    "appliesTo": [
      "urn:csabs:concept/Stack"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/Stack-sequence-model",
      "urn:csabs:axiom/Stack-observers"
    ],
    "assumptions": [
      "Use the explicit mathematical bases and typed carriers of the linked concepts."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Stack-push-injective",
    "type": "Theorem",
    "name": "push-injective",
    "statement": "Pushing is injective in both the prior stack and the new value.",
    "formalStatement": "push(s,x)=push(t,y) ⇒ s=t ∧ x=y",
    "proofSketch": "Apply pop to the equality and use the push-pop equation.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Stack apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Stack"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Stack-sequence-model",
      "urn:csabs:axiom/Stack-observers"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
