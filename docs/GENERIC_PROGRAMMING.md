# Shared generic programming, Java and VHDL

The catalog separates a shared mathematical interface from language-specific semantics. Generic programming is a subject under Programming-language semantics, with C++ template metaprogramming, Java generics and VHDL generics as distinct subsubjects. Subject membership never transfers axioms or compiler rules.

## Shared foundation

| Concept | Interface | Deliberate limit |
| --- | --- | --- |
| [GenericSignature](../concepts/GenericSignature.md) | Finite ordered, distinctly named parameter slots and argument kinds | Kind correctness is weaker than language well-formedness. Packs require an explicit encoding. |
| [GenericArgumentBinding](../concepts/GenericArgumentBinding.md) | Resolved actual slots, explicit-actual precedence and permitted ordered defaults | Named/positional matching and inference occur before this selected completion profile; full bounds follow it. |
| [ParametricInstantiation](../concepts/ParametricInstantiation.md) | Kind checks, simultaneous substitution, admissibility and language realization | Instantiation is a relation, allowing fresh/generative identities; it is not universally a type/value function. |

These are catalog abstractions adapted from consulted JLS, IEEE VHDL and C++ draft clauses. A language adapter supplies its supported kinds, canonical identities, compatibility, scope, default policy and realization. The shared layer does not require all languages to support named arguments, default type arguments, template arguments or package arguments.

Bounds are not restricted to preceding parameters: Java recursive/F-bounds require simultaneous substitution. The ordered-default binding profile is narrower and applies only when a language permits those defaults. Java's inferred arguments are supplied by inference; Java type parameters have no default-argument mechanism in this profile.

The original C++ concept IDs, definitions and claims retain their meanings. Their subject now appears beneath Generic programming. New common concepts use related/prerequisite links to C++ rather than silently generalizing C++ SFINAE, partial-specialization selection, atomic constraint identity or lookup into universal generic-programming rules. See [the C++ guide](TEMPLATE_METAPROGRAMMING.md).

## Java profile

The reference is **Java SE 25 JLS**, with explicit section locators in each record. The runnable examples use established generic rules available in the installed **Java 21** compiler; that execution is not full SE25 conformance evidence.

| Concept | Selected behavior |
| --- | --- |
| [JavaParameterizedType](../concepts/JavaParameterizedType.md) | Class/interface parameterization, arity, reference/wildcard arguments, capture-adjusted bounds, member substitution and nominal generic subtyping |
| [JavaWildcardCapture](../concepts/JavaWildcardCapture.md) | Fresh bounded variables for outer-level wildcards; simultaneous upper/lower bounds; no recursive capture of nested arguments |
| [JavaTypeErasure](../concepts/JavaTypeErasure.md) | Erasure of parameterizations, arrays, leftmost variable bounds and signatures, with reifiability as a separate predicate |
| [JavaTypeInference](../concepts/JavaTypeInference.md) | Proper-type assignments, interpreted bounds, applicability/target separation and obligations for sound resolution |

For example, `Integer <: Number` does not establish `List<Integer> <: List<Number>`. Wildcard containment permits different relationships, such as assigning an integer list to a suitable `List<? extends Number>` view. Capturing that view introduces an unknown type with bounds; it does not authorize inserting any `Number` into it.

`Box<Integer>` and `Box<Double>` can have different member types yet share an erased nominal class. Erasure does not establish source-type equality, eliminate every metadata representation, or prove heap-pollution safety. Runtime-reifiable parameterizations such as suitable `G<?>` are governed by separate JLS rules.

Inference considers both argument obligations and, when applicable, target obligations. Adding a target intersects semantic solution sets; it does not guarantee a unique/principal solution or that Java's staged inference can select every semantic solution. The Lean interface does not implement Chapter 18.

The [Java example](../examples/GenericExamples.md) maps compiler/runtime observations and six rejection cases to catalog IDs. Run:

```sh
python3 scripts/check_java_generic_examples.py --output /tmp/java-generic-evidence.json
```

## VHDL profile

The reference is **IEEE Std 1076-2019**, especially §§6.5, 9.4 and 14.3–14.5. The illustrative source uses a VHDL-2008-compatible subset; edition-specific features and tool support must be mapped separately.

| Concept | Selected behavior |
| --- | --- |
| [VHDLGenericInterface](../concepts/VHDLGenericInterface.md) | Constant, type, subprogram and package formal kinds; whole-formal positional/named association; kind-specific compatibility/default obligations |
| [VHDLGenericElaboration](../concepts/VHDLGenericElaboration.md) | Formal-order generic elaboration, subtype/profile/package checks, staticness obligations and finite generate expansion |

An all-named generic map may list associations in different orders while normalizing to the same formal-to-actual map. Actual elaboration still proceeds in formal declaration order. A positional item after a named item is invalid. The reduced normalizer deliberately excludes individually associated composite subelements, conversions and implicit anonymous-type associations.

Omission or `open` does not mean every kind has a default. Applicable constant/subprogram defaults must be justified; mandatory type/package actuals are not invented. Formal generic types denote their actual subtypes. Package realization and newly declared types have language-specific instance/declaration identity obligations.

Locally and globally static expressions are language classifications. A tool's ability to evaluate an expression does not establish either classification, and generic constants are not automatically locally static in every context. Generate expansion describes elaborated blocks, not a guarantee of synthesizable hardware, a cost model or complete simulation semantics.

The [VHDL example](../examples/generic_interfaces.md) demonstrates type/value generics, a constant default, named order and a null generate range. **It has not been compiled or simulated locally: neither GHDL nor NVC is installed.** Commands for a later compiler run are provided without claiming success.

## Retrieval and use

```sh
python3 scripts/catalog.py list --category generic-programming
python3 scripts/catalog.py list --category java-generics
python3 scripts/catalog.py list --category vhdl-generics
python3 scripts/catalog.py get GenericArgumentBinding --sections operations axioms laws sources
python3 scripts/agent_query.py node urn:csabs:law/JavaTypeInference-target-narrows-solutions
python3 scripts/agent_query.py node urn:csabs:law/VHDLGenericInterface-named-permutation
```

Use [implementation-mapping](../ai/skills/implementation-mapping/SKILL.md) to select a profile and connect clauses to language types, parameter identity, substitution, bounds, defaults, elaboration phases and observable outcomes. Use [implementation-conformance](../ai/skills/implementation-conformance/SKILL.md) and [mathematical-tests](../ai/skills/mathematical-tests/SKILL.md) for reviews and executable evidence. A cross-language analogy alone is not an applicable axiom.

## Lean coverage

[`Catalog/GenericProgramming.lean`](../lean/Catalog/GenericProgramming.lean) has bindings for all nine concepts. `GenericSignature`, `GenericArgumentBinding` and the selected `VHDLGenericInterface` normalizer have carrier/interface models. The six other bindings are explicitly partial. They expose obligations and selected rules, with language frontends, hygienic substitution, complete Java checks and concrete VHDL elaboration still supplied by clients.

The erasure core uses bounded fuel and omits nested-owner types, signature translation and reifiability. Fuel exhaustion is inconclusive, not a proof of invalidity. Inference soundness is an explicit interface hypothesis rather than a proof about `javac`. No new generic law/theorem is registered as a compiled witness. Existing witnesses, source provenance and target implementation correctness remain separate forms of evidence.
