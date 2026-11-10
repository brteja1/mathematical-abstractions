# Behavioral subtyping with explicit history constraints

A contract-based relation between subtype and supertype specifications, using an abstraction function, inherited-method correspondence, invariant preservation and an explicit history-constraint rule.

**Notation:** S ≼[α,ρ] T; α:S→T; ρ:M_T→M_S; I_S,I_T invariants; P,Q method contracts; C_S,C_T two-state history constraints

**Stable ID:** `urn:csabs:concept/BehavioralSubtyping`

**Categories:** Programming-language semantics → Object-oriented semantics

**Kind:** Relation

**Prerequisites:** [Relational method contract with write effects](MethodContract.md), [Visible-state object invariant protocol](ObjectInvariant.md)

**Related concepts:** [Single-inheritance class table and dynamic dispatch](ClassTable.md), [Simulation](Simulation.md), [Predicate-restricted subtype](Subtype.md)

## Backlinks

- [Single-inheritance class table and dynamic dispatch](ClassTable.md) — `relatedConcept`
- [Java bounded parameterized types and nominal subtyping](JavaParameterizedType.md) — `relatedConcept`
- [Relational method contract with write effects](MethodContract.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected defining rules: S≼[α,ρ]T ⇒ ∀s, I_S(s)⇒I_T(αs). S≼[α,ρ]T ⇒ ∀m∈M_T,s,i, I_S(s)∧P_T(m,αs,i) ⇒ P_S(ρm,s,i) ∧ (∀s′,o, Q_S(ρm,s,i,s′,o) ⇒ I_S(s′)∧Q_T(m,αs,i,αs′,o)). S≼[α,ρ]T ⇒ ∀s,s′, I_S(s)∧I_S(s′)∧C_S(s,s′) ⇒ C_T(αs,αs′); every admissible ordered subtype-history pair satisfies C_S, including pairs spanning extra methods. S≼[α,ρ]T iff the invariant, methods and constraint rules hold and every supertype method has a signature-compatible provided method under ρ; subtype specs preserve their stated invariants and history constraints.

**basisKind:** extensional-structural-definition

**basisScope:** Constraint-rule profile adapted from Liskov–Wing §5.2, not the alternative explanation-rule definition. α is total on legal subtype states (extended arbitrarily outside them); ρ maps each supertype method to a provided subtype method. A shared typed input/outcome encoding already accounts for signature compatibility and permitted exceptions; otherwise explicit adapters and variance obligations are required. Q includes frame/effect observations. C_S constrains all ordered pairs along admissible subtype histories, including extra methods and alias-visible changes; subtype specs must themselves preserve I_S and C_S. This is partial-correctness substitutability, not contextual equivalence for all languages or a termination/progress guarantee. α need not be surjective.

**verificationObligation:** Instantiate carriers, equality, definedness and the stated semantic profile before using these records.; Catalog validation checks structure, not source entailment or target implementation conformance.

**reviewStatus:** Editorial source and interface review; Lean model bindings and individual proof witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-BehavioralSubtyping-invariant-map"></a>

### invariant-map

`urn:csabs:operation/BehavioralSubtyping-invariant-map`

**signature:** invariantMap : α×I_S×I_T→Prop

**description:** ∀s, I_S(s) ⇒ I_T(α(s)).

**precondition:** Typed inputs in the stated semantic profile.

**postcondition:** ∀s, I_S(s) ⇒ I_T(α(s)).

**totality:** Total mathematical operation.

**source:** [Liskov and Wing: A Behavioral Notion of Subtyping, TOPLAS 16(6), 1811–1841, 1994](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach

**sourceNote:** Adapts the constraint definition to explicit state functions and fixed input/outcome carriers. Retains separate history obligations; nominal subclassing and predicate-restricted Subtype are distinct concepts.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BehavioralSubtyping-method-refines"></a>

### method-refines

`urn:csabs:operation/BehavioralSubtyping-method-refines`

**signature:** methodRefines : α×ρ×Spec_S×Spec_T→Prop

**description:** For each m∈M_T and legal s: P_T(m,αs,i)⇒P_S(ρm,s,i); under P_T, every Q_S(ρm,s,i,s′,o) yields Q_T(m,αs,i,αs′,o), with legal subtype poststates.

**precondition:** Typed inputs in the stated semantic profile.

**postcondition:** For each m∈M_T and legal s: P_T(m,αs,i)⇒P_S(ρm,s,i); under P_T, every Q_S(ρm,s,i,s′,o) yields Q_T(m,αs,i,αs′,o), with legal subtype poststates.

**totality:** Total mathematical operation.

**source:** [Liskov and Wing: A Behavioral Notion of Subtyping, TOPLAS 16(6), 1811–1841, 1994](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach

**sourceNote:** Adapts the constraint definition to explicit state functions and fixed input/outcome carriers. Retains separate history obligations; nominal subclassing and predicate-restricted Subtype are distinct concepts.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BehavioralSubtyping-history-refines"></a>

### history-refines

`urn:csabs:operation/BehavioralSubtyping-history-refines`

**signature:** historyRefines : α×C_S×C_T→Prop

**description:** For legal s,s′, C_S(s,s′) ⇒ C_T(αs,αs′). The subtype specification must establish C_S for all admissible ordered history pairs, including extra methods.

**precondition:** Typed inputs in the stated semantic profile.

**postcondition:** For legal s,s′, C_S(s,s′) ⇒ C_T(αs,αs′). The subtype specification must establish C_S for all admissible ordered history pairs, including extra methods.

**totality:** Total mathematical operation.

**source:** [Liskov and Wing: A Behavioral Notion of Subtyping, TOPLAS 16(6), 1811–1841, 1994](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach

**sourceNote:** Adapts the constraint definition to explicit state functions and fixed input/outcome carriers. Retains separate history obligations; nominal subclassing and predicate-restricted Subtype are distinct concepts.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BehavioralSubtyping-is-subtype"></a>

### is-subtype

`urn:csabs:operation/BehavioralSubtyping-is-subtype`

**signature:** isSubtype : Spec_S×Spec_T×α×ρ→Prop

**description:** Conjoin invariantMap, methodRefines, historyRefines and well-formed signature/method-coverage obligations; subtype specifications satisfy their own invariants and constraints.

**precondition:** Typed inputs in the stated semantic profile.

**postcondition:** Conjoin invariantMap, methodRefines, historyRefines and well-formed signature/method-coverage obligations; subtype specifications satisfy their own invariants and constraints.

**totality:** Total mathematical operation.

**source:** [Liskov and Wing: A Behavioral Notion of Subtyping, TOPLAS 16(6), 1811–1841, 1994](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach

**sourceNote:** Adapts the constraint definition to explicit state functions and fixed input/outcome carriers. Retains separate history obligations; nominal subclassing and predicate-restricted Subtype are distinct concepts.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-BehavioralSubtyping-invariant-rule"></a>

### invariant-rule

`urn:csabs:axiom/BehavioralSubtyping-invariant-rule`

**statement:** S≼[α,ρ]T ⇒ ∀s, I_S(s)⇒I_T(αs).

**formalStatement:** S≼[α,ρ]T ⇒ ∀s, I_S(s)⇒I_T(αs).

**assumptions:** Constraint-rule profile adapted from Liskov–Wing §5.2, not the alternative explanation-rule definition. α is total on legal subtype states (extended arbitrarily outside them); ρ maps each supertype method to a provided subtype method. A shared typed input/outcome encoding already accounts for signature compatibility and permitted exceptions; otherwise explicit adapters and variance obligations are required. Q includes frame/effect observations. C_S constrains all ordered pairs along admissible subtype histories, including extra methods and alias-visible changes; subtype specs must themselves preserve I_S and C_S. This is partial-correctness substitutability, not contextual equivalence for all languages or a termination/progress guarantee. α need not be surjective.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Liskov and Wing: A Behavioral Notion of Subtyping, TOPLAS 16(6), 1811–1841, 1994](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach

**sourceNote:** Adapts the constraint definition to explicit state functions and fixed input/outcome carriers. Retains separate history obligations; nominal subclassing and predicate-restricted Subtype are distinct concepts.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-BehavioralSubtyping-methods-rule"></a>

### methods-rule

`urn:csabs:axiom/BehavioralSubtyping-methods-rule`

**statement:** S≼[α,ρ]T ⇒ ∀m∈M_T,s,i, I_S(s)∧P_T(m,αs,i) ⇒ P_S(ρm,s,i) ∧ (∀s′,o, Q_S(ρm,s,i,s′,o) ⇒ I_S(s′)∧Q_T(m,αs,i,αs′,o)).

**formalStatement:** S≼[α,ρ]T ⇒ ∀m∈M_T,s,i, I_S(s)∧P_T(m,αs,i) ⇒ P_S(ρm,s,i) ∧ (∀s′,o, Q_S(ρm,s,i,s′,o) ⇒ I_S(s′)∧Q_T(m,αs,i,αs′,o)).

**assumptions:** Constraint-rule profile adapted from Liskov–Wing §5.2, not the alternative explanation-rule definition. α is total on legal subtype states (extended arbitrarily outside them); ρ maps each supertype method to a provided subtype method. A shared typed input/outcome encoding already accounts for signature compatibility and permitted exceptions; otherwise explicit adapters and variance obligations are required. Q includes frame/effect observations. C_S constrains all ordered pairs along admissible subtype histories, including extra methods and alias-visible changes; subtype specs must themselves preserve I_S and C_S. This is partial-correctness substitutability, not contextual equivalence for all languages or a termination/progress guarantee. α need not be surjective.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Liskov and Wing: A Behavioral Notion of Subtyping, TOPLAS 16(6), 1811–1841, 1994](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach

**sourceNote:** Adapts the constraint definition to explicit state functions and fixed input/outcome carriers. Retains separate history obligations; nominal subclassing and predicate-restricted Subtype are distinct concepts.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-BehavioralSubtyping-constraint-rule"></a>

### constraint-rule

`urn:csabs:axiom/BehavioralSubtyping-constraint-rule`

**statement:** S≼[α,ρ]T ⇒ ∀s,s′, I_S(s)∧I_S(s′)∧C_S(s,s′) ⇒ C_T(αs,αs′); every admissible ordered subtype-history pair satisfies C_S, including pairs spanning extra methods.

**formalStatement:** S≼[α,ρ]T ⇒ ∀s,s′, I_S(s)∧I_S(s′)∧C_S(s,s′) ⇒ C_T(αs,αs′); every admissible ordered subtype-history pair satisfies C_S, including pairs spanning extra methods.

**assumptions:** Constraint-rule profile adapted from Liskov–Wing §5.2, not the alternative explanation-rule definition. α is total on legal subtype states (extended arbitrarily outside them); ρ maps each supertype method to a provided subtype method. A shared typed input/outcome encoding already accounts for signature compatibility and permitted exceptions; otherwise explicit adapters and variance obligations are required. Q includes frame/effect observations. C_S constrains all ordered pairs along admissible subtype histories, including extra methods and alias-visible changes; subtype specs must themselves preserve I_S and C_S. This is partial-correctness substitutability, not contextual equivalence for all languages or a termination/progress guarantee. α need not be surjective.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Liskov and Wing: A Behavioral Notion of Subtyping, TOPLAS 16(6), 1811–1841, 1994](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach

**sourceNote:** Adapts the constraint definition to explicit state functions and fixed input/outcome carriers. Retains separate history obligations; nominal subclassing and predicate-restricted Subtype are distinct concepts.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-BehavioralSubtyping-subtype-definition"></a>

### subtype-definition

`urn:csabs:axiom/BehavioralSubtyping-subtype-definition`

**statement:** S≼[α,ρ]T iff the invariant, methods and constraint rules hold and every supertype method has a signature-compatible provided method under ρ; subtype specs preserve their stated invariants and history constraints.

**formalStatement:** S≼[α,ρ]T iff the invariant, methods and constraint rules hold and every supertype method has a signature-compatible provided method under ρ; subtype specs preserve their stated invariants and history constraints.

**assumptions:** Constraint-rule profile adapted from Liskov–Wing §5.2, not the alternative explanation-rule definition. α is total on legal subtype states (extended arbitrarily outside them); ρ maps each supertype method to a provided subtype method. A shared typed input/outcome encoding already accounts for signature compatibility and permitted exceptions; otherwise explicit adapters and variance obligations are required. Q includes frame/effect observations. C_S constrains all ordered pairs along admissible subtype histories, including extra methods and alias-visible changes; subtype specs must themselves preserve I_S and C_S. This is partial-correctness substitutability, not contextual equivalence for all languages or a termination/progress guarantee. α need not be surjective.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Liskov and Wing: A Behavioral Notion of Subtyping, TOPLAS 16(6), 1811–1841, 1994](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach

**sourceNote:** Adapts the constraint definition to explicit state functions and fixed input/outcome carriers. Retains separate history obligations; nominal subclassing and predicate-restricted Subtype are distinct concepts.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-BehavioralSubtyping-client-postcondition-transfer"></a>

### client-postcondition-transfer

`urn:csabs:law/BehavioralSubtyping-client-postcondition-transfer`

**statement:** S≼[α,ρ]T ∧ I_S(s) ∧ P_T(m,αs,i) ∧ Q_S(ρm,s,i,s′,o) ⇒ Q_T(m,αs,i,αs′,o).

**formalStatement:** S≼[α,ρ]T ∧ I_S(s) ∧ P_T(m,αs,i) ∧ Q_S(ρm,s,i,s′,o) ⇒ Q_T(m,αs,i,αs′,o).

**assumptions:** Constraint-rule profile adapted from Liskov–Wing §5.2, not the alternative explanation-rule definition. α is total on legal subtype states (extended arbitrarily outside them); ρ maps each supertype method to a provided subtype method. A shared typed input/outcome encoding already accounts for signature compatibility and permitted exceptions; otherwise explicit adapters and variance obligations are required. Q includes frame/effect observations. C_S constrains all ordered pairs along admissible subtype histories, including extra methods and alias-visible changes; subtype specs must themselves preserve I_S and C_S. This is partial-correctness substitutability, not contextual equivalence for all languages or a termination/progress guarantee. α need not be surjective.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Liskov and Wing: A Behavioral Notion of Subtyping, TOPLAS 16(6), 1811–1841, 1994](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach

**sourceNote:** Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.

**provenanceKind:** derived

**dependsOn:** [methods-rule](BehavioralSubtyping.md#node-urn-csabs-axiom-BehavioralSubtyping-methods-rule)

**proofSketch:** Instantiate the methods rule at the supertype method, legal initial state and input, then apply its postcondition implication to the actual permitted subtype outcome.

<a id="node-urn-csabs-law-BehavioralSubtyping-declared-history-transfer"></a>

### declared-history-transfer

`urn:csabs:law/BehavioralSubtyping-declared-history-transfer`

**statement:** S≼[α,ρ]T ∧ s,s′ occur in order in an admissible subtype history ⇒ C_T(αs,αs′).

**formalStatement:** S≼[α,ρ]T ∧ s,s′ occur in order in an admissible subtype history ⇒ C_T(αs,αs′).

**assumptions:** Constraint-rule profile adapted from Liskov–Wing §5.2, not the alternative explanation-rule definition. α is total on legal subtype states (extended arbitrarily outside them); ρ maps each supertype method to a provided subtype method. A shared typed input/outcome encoding already accounts for signature compatibility and permitted exceptions; otherwise explicit adapters and variance obligations are required. Q includes frame/effect observations. C_S constrains all ordered pairs along admissible subtype histories, including extra methods and alias-visible changes; subtype specs must themselves preserve I_S and C_S. This is partial-correctness substitutability, not contextual equivalence for all languages or a termination/progress guarantee. α need not be surjective.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Liskov and Wing: A Behavioral Notion of Subtyping, TOPLAS 16(6), 1811–1841, 1994](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach

**sourceNote:** Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.

**provenanceKind:** derived

**dependsOn:** [invariant-rule](BehavioralSubtyping.md#node-urn-csabs-axiom-BehavioralSubtyping-invariant-rule); [constraint-rule](BehavioralSubtyping.md#node-urn-csabs-axiom-BehavioralSubtyping-constraint-rule); [subtype-definition](BehavioralSubtyping.md#node-urn-csabs-axiom-BehavioralSubtyping-subtype-definition)

**proofSketch:** Well-formed subtype histories have legal states satisfying I_S and C_S on every ordered pair. Apply the constraint rule. The invariant rule also ensures the mapped states are legal supertype states; no undeclared history property is inferred.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Liskov and Wing: A Behavioral Notion of Subtyping, TOPLAS 16(6), 1811–1841, 1994](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach

**sourceNote:** Adapts the constraint definition to explicit state functions and fixed input/outcome carriers. Retains separate history obligations; nominal subclassing and predicate-restricted Subtype are distinct concepts.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/BehavioralSubtyping",
    "type": "Concept",
    "shortForm": "BehavioralSubtyping",
    "fullName": "Behavioral subtyping with explicit history constraints",
    "category": [
      "urn:csabs:category/object-oriented-semantics"
    ],
    "kind": "urn:csabs:kind/relation",
    "definition": "A contract-based relation between subtype and supertype specifications, using an abstraction function, inherited-method correspondence, invariant preservation and an explicit history-constraint rule.",
    "notation": "S ≼[α,ρ] T; α:S→T; ρ:M_T→M_S; I_S,I_T invariants; P,Q method contracts; C_S,C_T two-state history constraints",
    "requiresConcept": [
      "urn:csabs:concept/MethodContract",
      "urn:csabs:concept/ObjectInvariant"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ClassTable",
      "urn:csabs:concept/Simulation",
      "urn:csabs:concept/Subtype"
    ],
    "hasOperation": [
      "urn:csabs:operation/BehavioralSubtyping-invariant-map",
      "urn:csabs:operation/BehavioralSubtyping-method-refines",
      "urn:csabs:operation/BehavioralSubtyping-history-refines",
      "urn:csabs:operation/BehavioralSubtyping-is-subtype"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/BehavioralSubtyping-invariant-rule",
      "urn:csabs:axiom/BehavioralSubtyping-methods-rule",
      "urn:csabs:axiom/BehavioralSubtyping-constraint-rule",
      "urn:csabs:axiom/BehavioralSubtyping-subtype-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/BehavioralSubtyping-client-postcondition-transfer",
      "urn:csabs:law/BehavioralSubtyping-declared-history-transfer"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "Constraint-rule profile adapted from Liskov–Wing §5.2, not the alternative explanation-rule definition. α is total on legal subtype states (extended arbitrarily outside them); ρ maps each supertype method to a provided subtype method. A shared typed input/outcome encoding already accounts for signature compatibility and permitted exceptions; otherwise explicit adapters and variance obligations are required. Q includes frame/effect observations. C_S constrains all ordered pairs along admissible subtype histories, including extra methods and alias-visible changes; subtype specs must themselves preserve I_S and C_S. This is partial-correctness substitutability, not contextual equivalence for all languages or a termination/progress guarantee. α need not be surjective.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source and interface review; Lean model bindings and individual proof witnesses are separate.",
    "verificationObligation": [
      "Instantiate carriers, equality, definedness and the stated semantic profile before using these records.",
      "Catalog validation checks structure, not source entailment or target implementation conformance."
    ],
    "source": [
      "urn:csabs:source/oop-liskov-wing"
    ],
    "sourceLocator": "§§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach",
    "sourceNote": "Adapts the constraint definition to explicit state functions and fixed input/outcome carriers. Retains separate history obligations; nominal subclassing and predicate-restricted Subtype are distinct concepts.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: S≼[α,ρ]T ⇒ ∀s, I_S(s)⇒I_T(αs). S≼[α,ρ]T ⇒ ∀m∈M_T,s,i, I_S(s)∧P_T(m,αs,i) ⇒ P_S(ρm,s,i) ∧ (∀s′,o, Q_S(ρm,s,i,s′,o) ⇒ I_S(s′)∧Q_T(m,αs,i,αs′,o)). S≼[α,ρ]T ⇒ ∀s,s′, I_S(s)∧I_S(s′)∧C_S(s,s′) ⇒ C_T(αs,αs′); every admissible ordered subtype-history pair satisfies C_S, including pairs spanning extra methods. S≼[α,ρ]T iff the invariant, methods and constraint rules hold and every supertype method has a signature-compatible provided method under ρ; subtype specs preserve their stated invariants and history constraints."
  },
  {
    "id": "urn:csabs:operation/BehavioralSubtyping-invariant-map",
    "type": "Operation",
    "name": "invariant-map",
    "signature": "invariantMap : α×I_S×I_T→Prop",
    "description": "∀s, I_S(s) ⇒ I_T(α(s)).",
    "concept": "urn:csabs:concept/BehavioralSubtyping",
    "precondition": "Typed inputs in the stated semantic profile.",
    "postcondition": "∀s, I_S(s) ⇒ I_T(α(s)).",
    "totality": "Total mathematical operation.",
    "source": [
      "urn:csabs:source/oop-liskov-wing"
    ],
    "sourceLocator": "§§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach",
    "sourceNote": "Adapts the constraint definition to explicit state functions and fixed input/outcome carriers. Retains separate history obligations; nominal subclassing and predicate-restricted Subtype are distinct concepts.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BehavioralSubtyping-method-refines",
    "type": "Operation",
    "name": "method-refines",
    "signature": "methodRefines : α×ρ×Spec_S×Spec_T→Prop",
    "description": "For each m∈M_T and legal s: P_T(m,αs,i)⇒P_S(ρm,s,i); under P_T, every Q_S(ρm,s,i,s′,o) yields Q_T(m,αs,i,αs′,o), with legal subtype poststates.",
    "concept": "urn:csabs:concept/BehavioralSubtyping",
    "precondition": "Typed inputs in the stated semantic profile.",
    "postcondition": "For each m∈M_T and legal s: P_T(m,αs,i)⇒P_S(ρm,s,i); under P_T, every Q_S(ρm,s,i,s′,o) yields Q_T(m,αs,i,αs′,o), with legal subtype poststates.",
    "totality": "Total mathematical operation.",
    "source": [
      "urn:csabs:source/oop-liskov-wing"
    ],
    "sourceLocator": "§§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach",
    "sourceNote": "Adapts the constraint definition to explicit state functions and fixed input/outcome carriers. Retains separate history obligations; nominal subclassing and predicate-restricted Subtype are distinct concepts.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BehavioralSubtyping-history-refines",
    "type": "Operation",
    "name": "history-refines",
    "signature": "historyRefines : α×C_S×C_T→Prop",
    "description": "For legal s,s′, C_S(s,s′) ⇒ C_T(αs,αs′). The subtype specification must establish C_S for all admissible ordered history pairs, including extra methods.",
    "concept": "urn:csabs:concept/BehavioralSubtyping",
    "precondition": "Typed inputs in the stated semantic profile.",
    "postcondition": "For legal s,s′, C_S(s,s′) ⇒ C_T(αs,αs′). The subtype specification must establish C_S for all admissible ordered history pairs, including extra methods.",
    "totality": "Total mathematical operation.",
    "source": [
      "urn:csabs:source/oop-liskov-wing"
    ],
    "sourceLocator": "§§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach",
    "sourceNote": "Adapts the constraint definition to explicit state functions and fixed input/outcome carriers. Retains separate history obligations; nominal subclassing and predicate-restricted Subtype are distinct concepts.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BehavioralSubtyping-is-subtype",
    "type": "Operation",
    "name": "is-subtype",
    "signature": "isSubtype : Spec_S×Spec_T×α×ρ→Prop",
    "description": "Conjoin invariantMap, methodRefines, historyRefines and well-formed signature/method-coverage obligations; subtype specifications satisfy their own invariants and constraints.",
    "concept": "urn:csabs:concept/BehavioralSubtyping",
    "precondition": "Typed inputs in the stated semantic profile.",
    "postcondition": "Conjoin invariantMap, methodRefines, historyRefines and well-formed signature/method-coverage obligations; subtype specifications satisfy their own invariants and constraints.",
    "totality": "Total mathematical operation.",
    "source": [
      "urn:csabs:source/oop-liskov-wing"
    ],
    "sourceLocator": "§§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach",
    "sourceNote": "Adapts the constraint definition to explicit state functions and fixed input/outcome carriers. Retains separate history obligations; nominal subclassing and predicate-restricted Subtype are distinct concepts.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/BehavioralSubtyping-invariant-rule",
    "type": "Axiom",
    "name": "invariant-rule",
    "statement": "S≼[α,ρ]T ⇒ ∀s, I_S(s)⇒I_T(αs).",
    "formalStatement": "S≼[α,ρ]T ⇒ ∀s, I_S(s)⇒I_T(αs).",
    "assumptions": [
      "Constraint-rule profile adapted from Liskov–Wing §5.2, not the alternative explanation-rule definition. α is total on legal subtype states (extended arbitrarily outside them); ρ maps each supertype method to a provided subtype method. A shared typed input/outcome encoding already accounts for signature compatibility and permitted exceptions; otherwise explicit adapters and variance obligations are required. Q includes frame/effect observations. C_S constrains all ordered pairs along admissible subtype histories, including extra methods and alias-visible changes; subtype specs must themselves preserve I_S and C_S. This is partial-correctness substitutability, not contextual equivalence for all languages or a termination/progress guarantee. α need not be surjective.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BehavioralSubtyping"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-liskov-wing"
    ],
    "sourceLocator": "§§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach",
    "sourceNote": "Adapts the constraint definition to explicit state functions and fixed input/outcome carriers. Retains separate history obligations; nominal subclassing and predicate-restricted Subtype are distinct concepts.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/BehavioralSubtyping-methods-rule",
    "type": "Axiom",
    "name": "methods-rule",
    "statement": "S≼[α,ρ]T ⇒ ∀m∈M_T,s,i, I_S(s)∧P_T(m,αs,i) ⇒ P_S(ρm,s,i) ∧ (∀s′,o, Q_S(ρm,s,i,s′,o) ⇒ I_S(s′)∧Q_T(m,αs,i,αs′,o)).",
    "formalStatement": "S≼[α,ρ]T ⇒ ∀m∈M_T,s,i, I_S(s)∧P_T(m,αs,i) ⇒ P_S(ρm,s,i) ∧ (∀s′,o, Q_S(ρm,s,i,s′,o) ⇒ I_S(s′)∧Q_T(m,αs,i,αs′,o)).",
    "assumptions": [
      "Constraint-rule profile adapted from Liskov–Wing §5.2, not the alternative explanation-rule definition. α is total on legal subtype states (extended arbitrarily outside them); ρ maps each supertype method to a provided subtype method. A shared typed input/outcome encoding already accounts for signature compatibility and permitted exceptions; otherwise explicit adapters and variance obligations are required. Q includes frame/effect observations. C_S constrains all ordered pairs along admissible subtype histories, including extra methods and alias-visible changes; subtype specs must themselves preserve I_S and C_S. This is partial-correctness substitutability, not contextual equivalence for all languages or a termination/progress guarantee. α need not be surjective.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BehavioralSubtyping"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-liskov-wing"
    ],
    "sourceLocator": "§§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach",
    "sourceNote": "Adapts the constraint definition to explicit state functions and fixed input/outcome carriers. Retains separate history obligations; nominal subclassing and predicate-restricted Subtype are distinct concepts.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/BehavioralSubtyping-constraint-rule",
    "type": "Axiom",
    "name": "constraint-rule",
    "statement": "S≼[α,ρ]T ⇒ ∀s,s′, I_S(s)∧I_S(s′)∧C_S(s,s′) ⇒ C_T(αs,αs′); every admissible ordered subtype-history pair satisfies C_S, including pairs spanning extra methods.",
    "formalStatement": "S≼[α,ρ]T ⇒ ∀s,s′, I_S(s)∧I_S(s′)∧C_S(s,s′) ⇒ C_T(αs,αs′); every admissible ordered subtype-history pair satisfies C_S, including pairs spanning extra methods.",
    "assumptions": [
      "Constraint-rule profile adapted from Liskov–Wing §5.2, not the alternative explanation-rule definition. α is total on legal subtype states (extended arbitrarily outside them); ρ maps each supertype method to a provided subtype method. A shared typed input/outcome encoding already accounts for signature compatibility and permitted exceptions; otherwise explicit adapters and variance obligations are required. Q includes frame/effect observations. C_S constrains all ordered pairs along admissible subtype histories, including extra methods and alias-visible changes; subtype specs must themselves preserve I_S and C_S. This is partial-correctness substitutability, not contextual equivalence for all languages or a termination/progress guarantee. α need not be surjective.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BehavioralSubtyping"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-liskov-wing"
    ],
    "sourceLocator": "§§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach",
    "sourceNote": "Adapts the constraint definition to explicit state functions and fixed input/outcome carriers. Retains separate history obligations; nominal subclassing and predicate-restricted Subtype are distinct concepts.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/BehavioralSubtyping-subtype-definition",
    "type": "Axiom",
    "name": "subtype-definition",
    "statement": "S≼[α,ρ]T iff the invariant, methods and constraint rules hold and every supertype method has a signature-compatible provided method under ρ; subtype specs preserve their stated invariants and history constraints.",
    "formalStatement": "S≼[α,ρ]T iff the invariant, methods and constraint rules hold and every supertype method has a signature-compatible provided method under ρ; subtype specs preserve their stated invariants and history constraints.",
    "assumptions": [
      "Constraint-rule profile adapted from Liskov–Wing §5.2, not the alternative explanation-rule definition. α is total on legal subtype states (extended arbitrarily outside them); ρ maps each supertype method to a provided subtype method. A shared typed input/outcome encoding already accounts for signature compatibility and permitted exceptions; otherwise explicit adapters and variance obligations are required. Q includes frame/effect observations. C_S constrains all ordered pairs along admissible subtype histories, including extra methods and alias-visible changes; subtype specs must themselves preserve I_S and C_S. This is partial-correctness substitutability, not contextual equivalence for all languages or a termination/progress guarantee. α need not be surjective.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BehavioralSubtyping"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-liskov-wing"
    ],
    "sourceLocator": "§§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach",
    "sourceNote": "Adapts the constraint definition to explicit state functions and fixed input/outcome carriers. Retains separate history obligations; nominal subclassing and predicate-restricted Subtype are distinct concepts.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/BehavioralSubtyping-client-postcondition-transfer",
    "type": "Law",
    "name": "client-postcondition-transfer",
    "statement": "S≼[α,ρ]T ∧ I_S(s) ∧ P_T(m,αs,i) ∧ Q_S(ρm,s,i,s′,o) ⇒ Q_T(m,αs,i,αs′,o).",
    "formalStatement": "S≼[α,ρ]T ∧ I_S(s) ∧ P_T(m,αs,i) ∧ Q_S(ρm,s,i,s′,o) ⇒ Q_T(m,αs,i,αs′,o).",
    "assumptions": [
      "Constraint-rule profile adapted from Liskov–Wing §5.2, not the alternative explanation-rule definition. α is total on legal subtype states (extended arbitrarily outside them); ρ maps each supertype method to a provided subtype method. A shared typed input/outcome encoding already accounts for signature compatibility and permitted exceptions; otherwise explicit adapters and variance obligations are required. Q includes frame/effect observations. C_S constrains all ordered pairs along admissible subtype histories, including extra methods and alias-visible changes; subtype specs must themselves preserve I_S and C_S. This is partial-correctness substitutability, not contextual equivalence for all languages or a termination/progress guarantee. α need not be surjective.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BehavioralSubtyping"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-liskov-wing"
    ],
    "sourceLocator": "§§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach",
    "sourceNote": "Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/BehavioralSubtyping-methods-rule"
    ],
    "proofSketch": "Instantiate the methods rule at the supertype method, legal initial state and input, then apply its postcondition implication to the actual permitted subtype outcome."
  },
  {
    "id": "urn:csabs:law/BehavioralSubtyping-declared-history-transfer",
    "type": "Law",
    "name": "declared-history-transfer",
    "statement": "S≼[α,ρ]T ∧ s,s′ occur in order in an admissible subtype history ⇒ C_T(αs,αs′).",
    "formalStatement": "S≼[α,ρ]T ∧ s,s′ occur in order in an admissible subtype history ⇒ C_T(αs,αs′).",
    "assumptions": [
      "Constraint-rule profile adapted from Liskov–Wing §5.2, not the alternative explanation-rule definition. α is total on legal subtype states (extended arbitrarily outside them); ρ maps each supertype method to a provided subtype method. A shared typed input/outcome encoding already accounts for signature compatibility and permitted exceptions; otherwise explicit adapters and variance obligations are required. Q includes frame/effect observations. C_S constrains all ordered pairs along admissible subtype histories, including extra methods and alias-visible changes; subtype specs must themselves preserve I_S and C_S. This is partial-correctness substitutability, not contextual equivalence for all languages or a termination/progress guarantee. α need not be surjective.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BehavioralSubtyping"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-liskov-wing"
    ],
    "sourceLocator": "§§4.1–4.3 method specifications/invariants; §5.2 and Figure 4, constraint-rule subtyping; §5.3 distinguishes the explanation approach",
    "sourceNote": "Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/BehavioralSubtyping-invariant-rule",
      "urn:csabs:axiom/BehavioralSubtyping-constraint-rule",
      "urn:csabs:axiom/BehavioralSubtyping-subtype-definition"
    ],
    "proofSketch": "Well-formed subtype histories have legal states satisfying I_S and C_S on every ordered pair. Apply the constraint rule. The invariant rule also ensures the mapped states are legal supertype states; no undeclared history property is inferred."
  }
]
```
<!-- graph-record:end -->
