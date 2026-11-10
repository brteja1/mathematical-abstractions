# Finite kinded generic parameter signature

An ordered finite interface of distinctly named parameters, each carrying an argument kind, together with kind-correct argument lists.

**Notation:** Σ=[(p₀,k₀),…,(pₙ₋₁,kₙ₋₁)]; kind:Arg→Kind; names(Σ) distinct; kindCorrect(Σ,a) iff |a|=n ∧ ∀i<n,kind(aᵢ)=kᵢ

**Stable ID:** `urn:csabs:concept/GenericSignature`

**Categories:** Programming-language semantics → Generic programming

**Kind:** Abstract data type

**Prerequisites:** [Finite sequence (List datatype)](Sequence.md), [Finite set collection](FiniteSet.md)

**Related concepts:** [Kinded partial template metafunction](TemplateMetafunction.md), [Resolved generic argument binding with ordered defaults](GenericArgumentBinding.md), [Java bounded parameterized types and nominal subtyping](JavaParameterizedType.md), [VHDL generic interfaces and whole-formal association](VHDLGenericInterface.md)

## Backlinks

- [Resolved generic argument binding with ordered defaults](GenericArgumentBinding.md) — `requiresConcept`
- [Java bounded parameterized types and nominal subtyping](JavaParameterizedType.md) — `requiresConcept`
- [Contextual parametric declaration instantiation](ParametricInstantiation.md) — `requiresConcept`
- [VHDL generic interfaces and whole-formal association](VHDLGenericInterface.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Selected defining rules: Σ is a finite ordered list of (name,kind) pairs with pairwise distinct declaration-local names; argument equality is canonical carrier equality. kindCorrect(Σ,a) ⇔ |a|=|Σ| ∧ ∀i<|Σ|, kind(aᵢ)=kindOf(Σᵢ).

**basisKind:** extensional-structural-definition

**basisScope:** Language-independent interface abstraction adapted from parameterized declarations, not a complete type system. Kind and Arg are fixed carriers supplied by a language adapter; type/value/template/subprogram/package are possible tags, not kinds supported by every language. Names identify declaration-local parameters, and argument equality is the chosen canonical identity. Packs must be explicitly flattened/encoded before this fixed-arity profile. Bounds, defaults, dependent admissibility, implicit arguments and body validity are separate obligations; recursive/F-bounds are not incorrectly restricted to earlier parameters.

**verificationObligation:** Map language edition, carriers, identity, binding, substitution and phase-specific definedness explicitly.; Shared profiles do not transfer language rules; structural validation and model compilation do not prove language conformance.

**reviewStatus:** Editorial source/interface review; selected Lean interpretations are separate from theorem witnesses.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-GenericSignature-arity"></a>

### arity

`urn:csabs:operation/GenericSignature-arity`

**signature:** arity : Signature→ℕ

**description:** Return the number of ordered parameter slots.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** Return the number of ordered parameter slots.

**totality:** Total mathematical operation on the stated carrier.

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §4.5 parameterized declarations and argument arity; IEEE 1076-2019 §6.5.6; N4861 [temp.arg] ¶1

**sourceNote:** Extracts only finite named/kinded interfaces common to these mechanisms; language-specific well-formedness is intentionally retained by separate profiles.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-GenericSignature-kind-correct"></a>

### kind-correct

`urn:csabs:operation/GenericSignature-kind-correct`

**signature:** kindCorrect : Signature×Seq(Arg)→Prop

**description:** Check exact arity and the declared kind at each slot, without evaluating language-specific bounds.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** Check exact arity and the declared kind at each slot, without evaluating language-specific bounds.

**totality:** Total mathematical operation on the stated carrier.

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §4.5 parameterized declarations and argument arity; IEEE 1076-2019 §6.5.6; N4861 [temp.arg] ¶1

**sourceNote:** Extracts only finite named/kinded interfaces common to these mechanisms; language-specific well-formedness is intentionally retained by separate profiles.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-GenericSignature-signature-shape"></a>

### signature-shape

`urn:csabs:axiom/GenericSignature-signature-shape`

**statement:** Σ is a finite ordered list of (name,kind) pairs with pairwise distinct declaration-local names; argument equality is canonical carrier equality.

**formalStatement:** Σ is a finite ordered list of (name,kind) pairs with pairwise distinct declaration-local names; argument equality is canonical carrier equality.

**assumptions:** Language-independent interface abstraction adapted from parameterized declarations, not a complete type system. Kind and Arg are fixed carriers supplied by a language adapter; type/value/template/subprogram/package are possible tags, not kinds supported by every language. Names identify declaration-local parameters, and argument equality is the chosen canonical identity. Packs must be explicitly flattened/encoded before this fixed-arity profile. Bounds, defaults, dependent admissibility, implicit arguments and body validity are separate obligations; recursive/F-bounds are not incorrectly restricted to earlier parameters.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §4.5 parameterized declarations and argument arity; IEEE 1076-2019 §6.5.6; N4861 [temp.arg] ¶1

**sourceNote:** Extracts only finite named/kinded interfaces common to these mechanisms; language-specific well-formedness is intentionally retained by separate profiles.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-GenericSignature-kind-correctness"></a>

### kind-correctness

`urn:csabs:axiom/GenericSignature-kind-correctness`

**statement:** kindCorrect(Σ,a) ⇔ |a|=|Σ| ∧ ∀i<|Σ|, kind(aᵢ)=kindOf(Σᵢ).

**formalStatement:** kindCorrect(Σ,a) ⇔ |a|=|Σ| ∧ ∀i<|Σ|, kind(aᵢ)=kindOf(Σᵢ).

**assumptions:** Language-independent interface abstraction adapted from parameterized declarations, not a complete type system. Kind and Arg are fixed carriers supplied by a language adapter; type/value/template/subprogram/package are possible tags, not kinds supported by every language. Names identify declaration-local parameters, and argument equality is the chosen canonical identity. Packs must be explicitly flattened/encoded before this fixed-arity profile. Bounds, defaults, dependent admissibility, implicit arguments and body validity are separate obligations; recursive/F-bounds are not incorrectly restricted to earlier parameters.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §4.5 parameterized declarations and argument arity; IEEE 1076-2019 §6.5.6; N4861 [temp.arg] ¶1

**sourceNote:** Extracts only finite named/kinded interfaces common to these mechanisms; language-specific well-formedness is intentionally retained by separate profiles.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-GenericSignature-arity-mismatch"></a>

### arity-mismatch

`urn:csabs:law/GenericSignature-arity-mismatch`

**statement:** |a|≠|Σ| ⇒ ¬kindCorrect(Σ,a).

**formalStatement:** |a|≠|Σ| ⇒ ¬kindCorrect(Σ,a).

**assumptions:** Language-independent interface abstraction adapted from parameterized declarations, not a complete type system. Kind and Arg are fixed carriers supplied by a language adapter; type/value/template/subprogram/package are possible tags, not kinds supported by every language. Names identify declaration-local parameters, and argument equality is the chosen canonical identity. Packs must be explicitly flattened/encoded before this fixed-arity profile. Bounds, defaults, dependent admissibility, implicit arguments and body validity are separate obligations; recursive/F-bounds are not incorrectly restricted to earlier parameters.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §4.5 parameterized declarations and argument arity; IEEE 1076-2019 §6.5.6; N4861 [temp.arg] ¶1

**sourceNote:** Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.

**provenanceKind:** derived

**dependsOn:** [kind-correctness](GenericSignature.md#node-urn-csabs-axiom-GenericSignature-kind-correctness)

**proofSketch:** The length conjunct in kindCorrect cannot hold.

<a id="node-urn-csabs-law-GenericSignature-empty-interface"></a>

### empty-interface

`urn:csabs:law/GenericSignature-empty-interface`

**statement:** kindCorrect([],[]) and no nonempty argument list is kindCorrect for [].

**formalStatement:** kindCorrect([],[]) and no nonempty argument list is kindCorrect for [].

**assumptions:** Language-independent interface abstraction adapted from parameterized declarations, not a complete type system. Kind and Arg are fixed carriers supplied by a language adapter; type/value/template/subprogram/package are possible tags, not kinds supported by every language. Names identify declaration-local parameters, and argument equality is the chosen canonical identity. Packs must be explicitly flattened/encoded before this fixed-arity profile. Bounds, defaults, dependent admissibility, implicit arguments and body validity are separate obligations; recursive/F-bounds are not incorrectly restricted to earlier parameters.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §4.5 parameterized declarations and argument arity; IEEE 1076-2019 §6.5.6; N4861 [temp.arg] ¶1

**sourceNote:** Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.

**provenanceKind:** derived

**dependsOn:** [signature-shape](GenericSignature.md#node-urn-csabs-axiom-GenericSignature-signature-shape); [kind-correctness](GenericSignature.md#node-urn-csabs-axiom-GenericSignature-kind-correctness)

**proofSketch:** The empty length equality holds and the per-slot condition is vacuous; every nonempty list fails the length equality.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification
- [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification
- [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §4.5 parameterized declarations and argument arity; IEEE 1076-2019 §6.5.6; N4861 [temp.arg] ¶1

**sourceNote:** Extracts only finite named/kinded interfaces common to these mechanisms; language-specific well-formedness is intentionally retained by separate profiles.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/GenericSignature",
    "type": "Concept",
    "shortForm": "GenericSignature",
    "fullName": "Finite kinded generic parameter signature",
    "definition": "An ordered finite interface of distinctly named parameters, each carrying an argument kind, together with kind-correct argument lists.",
    "notation": "Σ=[(p₀,k₀),…,(pₙ₋₁,kₙ₋₁)]; kind:Arg→Kind; names(Σ) distinct; kindCorrect(Σ,a) iff |a|=n ∧ ∀i<n,kind(aᵢ)=kᵢ",
    "category": [
      "urn:csabs:category/generic-programming"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "requiresConcept": [
      "urn:csabs:concept/Sequence",
      "urn:csabs:concept/FiniteSet"
    ],
    "relatedConcept": [
      "urn:csabs:concept/TemplateMetafunction",
      "urn:csabs:concept/GenericArgumentBinding",
      "urn:csabs:concept/JavaParameterizedType",
      "urn:csabs:concept/VHDLGenericInterface"
    ],
    "hasOperation": [
      "urn:csabs:operation/GenericSignature-arity",
      "urn:csabs:operation/GenericSignature-kind-correct"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/GenericSignature-signature-shape",
      "urn:csabs:axiom/GenericSignature-kind-correctness"
    ],
    "hasLaw": [
      "urn:csabs:law/GenericSignature-arity-mismatch",
      "urn:csabs:law/GenericSignature-empty-interface"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "Language-independent interface abstraction adapted from parameterized declarations, not a complete type system. Kind and Arg are fixed carriers supplied by a language adapter; type/value/template/subprogram/package are possible tags, not kinds supported by every language. Names identify declaration-local parameters, and argument equality is the chosen canonical identity. Packs must be explicitly flattened/encoded before this fixed-arity profile. Bounds, defaults, dependent admissibility, implicit arguments and body validity are separate obligations; recursive/F-bounds are not incorrectly restricted to earlier parameters.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; selected Lean interpretations are separate from theorem witnesses.",
    "verificationObligation": [
      "Map language edition, carriers, identity, binding, substitution and phase-specific definedness explicitly.",
      "Shared profiles do not transfer language rules; structural validation and model compilation do not prove language conformance."
    ],
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §4.5 parameterized declarations and argument arity; IEEE 1076-2019 §6.5.6; N4861 [temp.arg] ¶1",
    "sourceNote": "Extracts only finite named/kinded interfaces common to these mechanisms; language-specific well-formedness is intentionally retained by separate profiles.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: Σ is a finite ordered list of (name,kind) pairs with pairwise distinct declaration-local names; argument equality is canonical carrier equality. kindCorrect(Σ,a) ⇔ |a|=|Σ| ∧ ∀i<|Σ|, kind(aᵢ)=kindOf(Σᵢ)."
  },
  {
    "id": "urn:csabs:operation/GenericSignature-arity",
    "type": "Operation",
    "name": "arity",
    "signature": "arity : Signature→ℕ",
    "description": "Return the number of ordered parameter slots.",
    "concept": "urn:csabs:concept/GenericSignature",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "Return the number of ordered parameter slots.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §4.5 parameterized declarations and argument arity; IEEE 1076-2019 §6.5.6; N4861 [temp.arg] ¶1",
    "sourceNote": "Extracts only finite named/kinded interfaces common to these mechanisms; language-specific well-formedness is intentionally retained by separate profiles.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/GenericSignature-kind-correct",
    "type": "Operation",
    "name": "kind-correct",
    "signature": "kindCorrect : Signature×Seq(Arg)→Prop",
    "description": "Check exact arity and the declared kind at each slot, without evaluating language-specific bounds.",
    "concept": "urn:csabs:concept/GenericSignature",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "Check exact arity and the declared kind at each slot, without evaluating language-specific bounds.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §4.5 parameterized declarations and argument arity; IEEE 1076-2019 §6.5.6; N4861 [temp.arg] ¶1",
    "sourceNote": "Extracts only finite named/kinded interfaces common to these mechanisms; language-specific well-formedness is intentionally retained by separate profiles.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/GenericSignature-signature-shape",
    "type": "Axiom",
    "name": "signature-shape",
    "statement": "Σ is a finite ordered list of (name,kind) pairs with pairwise distinct declaration-local names; argument equality is canonical carrier equality.",
    "formalStatement": "Σ is a finite ordered list of (name,kind) pairs with pairwise distinct declaration-local names; argument equality is canonical carrier equality.",
    "assumptions": [
      "Language-independent interface abstraction adapted from parameterized declarations, not a complete type system. Kind and Arg are fixed carriers supplied by a language adapter; type/value/template/subprogram/package are possible tags, not kinds supported by every language. Names identify declaration-local parameters, and argument equality is the chosen canonical identity. Packs must be explicitly flattened/encoded before this fixed-arity profile. Bounds, defaults, dependent admissibility, implicit arguments and body validity are separate obligations; recursive/F-bounds are not incorrectly restricted to earlier parameters.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/GenericSignature"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §4.5 parameterized declarations and argument arity; IEEE 1076-2019 §6.5.6; N4861 [temp.arg] ¶1",
    "sourceNote": "Extracts only finite named/kinded interfaces common to these mechanisms; language-specific well-formedness is intentionally retained by separate profiles.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/GenericSignature-kind-correctness",
    "type": "Axiom",
    "name": "kind-correctness",
    "statement": "kindCorrect(Σ,a) ⇔ |a|=|Σ| ∧ ∀i<|Σ|, kind(aᵢ)=kindOf(Σᵢ).",
    "formalStatement": "kindCorrect(Σ,a) ⇔ |a|=|Σ| ∧ ∀i<|Σ|, kind(aᵢ)=kindOf(Σᵢ).",
    "assumptions": [
      "Language-independent interface abstraction adapted from parameterized declarations, not a complete type system. Kind and Arg are fixed carriers supplied by a language adapter; type/value/template/subprogram/package are possible tags, not kinds supported by every language. Names identify declaration-local parameters, and argument equality is the chosen canonical identity. Packs must be explicitly flattened/encoded before this fixed-arity profile. Bounds, defaults, dependent admissibility, implicit arguments and body validity are separate obligations; recursive/F-bounds are not incorrectly restricted to earlier parameters.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/GenericSignature"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §4.5 parameterized declarations and argument arity; IEEE 1076-2019 §6.5.6; N4861 [temp.arg] ¶1",
    "sourceNote": "Extracts only finite named/kinded interfaces common to these mechanisms; language-specific well-formedness is intentionally retained by separate profiles.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/GenericSignature-arity-mismatch",
    "type": "Law",
    "name": "arity-mismatch",
    "statement": "|a|≠|Σ| ⇒ ¬kindCorrect(Σ,a).",
    "formalStatement": "|a|≠|Σ| ⇒ ¬kindCorrect(Σ,a).",
    "assumptions": [
      "Language-independent interface abstraction adapted from parameterized declarations, not a complete type system. Kind and Arg are fixed carriers supplied by a language adapter; type/value/template/subprogram/package are possible tags, not kinds supported by every language. Names identify declaration-local parameters, and argument equality is the chosen canonical identity. Packs must be explicitly flattened/encoded before this fixed-arity profile. Bounds, defaults, dependent admissibility, implicit arguments and body validity are separate obligations; recursive/F-bounds are not incorrectly restricted to earlier parameters.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/GenericSignature"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §4.5 parameterized declarations and argument arity; IEEE 1076-2019 §6.5.6; N4861 [temp.arg] ¶1",
    "sourceNote": "Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/GenericSignature-kind-correctness"
    ],
    "proofSketch": "The length conjunct in kindCorrect cannot hold."
  },
  {
    "id": "urn:csabs:law/GenericSignature-empty-interface",
    "type": "Law",
    "name": "empty-interface",
    "statement": "kindCorrect([],[]) and no nonempty argument list is kindCorrect for [].",
    "formalStatement": "kindCorrect([],[]) and no nonempty argument list is kindCorrect for [].",
    "assumptions": [
      "Language-independent interface abstraction adapted from parameterized declarations, not a complete type system. Kind and Arg are fixed carriers supplied by a language adapter; type/value/template/subprogram/package are possible tags, not kinds supported by every language. Names identify declaration-local parameters, and argument equality is the chosen canonical identity. Packs must be explicitly flattened/encoded before this fixed-arity profile. Bounds, defaults, dependent admissibility, implicit arguments and body validity are separate obligations; recursive/F-bounds are not incorrectly restricted to earlier parameters.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/GenericSignature"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §4.5 parameterized declarations and argument arity; IEEE 1076-2019 §6.5.6; N4861 [temp.arg] ¶1",
    "sourceNote": "Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/GenericSignature-signature-shape",
      "urn:csabs:axiom/GenericSignature-kind-correctness"
    ],
    "proofSketch": "The empty length equality holds and the per-slot condition is vacuous; every nonempty list fails the length equality."
  }
]
```
<!-- graph-record:end -->
