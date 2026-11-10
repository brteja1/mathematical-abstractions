# Template metaprogramming models

These seven concepts organize selected C++-style compile-time mechanisms under Programming-language semantics → Generic programming → Template metaprogramming. The reference profile is **C++20 working draft N4861**, consulted through its clause-addressable HTML rendering. This is an identified draft snapshot, not a claim to implement every rule of the published ISO standard or later revisions. See [shared, Java and VHDL profiles](GENERIC_PROGRAMMING.md) for cross-language scope; the existing C++ meanings and IDs are retained.

| Concept | Mathematical interface | Important distinction |
| --- | --- | --- |
| [TemplateMetafunction](../concepts/TemplateMetafunction.md) | Fixed-environment partial function from kind-correct canonical arguments to a type/value observation | Type, converted value and template arguments have different kinds; arbitrary templates are not total dependent functions. |
| [TemplateSpecialization](../concepts/TemplateSpecialization.md) | Finite matching set, strict more-specialized relation and primary/chosen/ambiguous outcome | Matching a pattern differs from selecting the winning partial specialization and from successfully instantiating its body. |
| [TemplateSubstitution](../concepts/TemplateSubstitution.md) | Lexically ordered checks with success, deduction failure and hard-error outcomes | Immediate-context failure can reject a candidate; errors in required instantiation side effects can still reject the program. |
| [TemplateConstraint](../concepts/TemplateConstraint.md) | Identity-bearing normalized atoms, short-circuit satisfaction and DNF/CNF subsumption | Equal Boolean behavior does not identify atomic constraints or establish C++ subsumption. |
| [TemplateParameterPack](../concepts/TemplateParameterPack.md) | Ordered finite sequences, expansion, equal-length zip and fold-expression trees | Simultaneous packs zip rather than form a Cartesian product; fold grouping does not imply operand evaluation order. |
| [DependentNameLookup](../concepts/DependentNameLookup.md) | Definition-context ordinary candidates plus eligible definition/instantiation ADL candidates | A later ordinary declaration is not automatically considered at instantiation. Candidate formation does not choose an overload. |
| [CompileTimeEvaluation](../concepts/CompileTimeEvaluation.md) | Partial evaluator for a closed signed-integer arithmetic/conditional fragment | An evaluated signed overflow is invalid; an unchosen well-formed branch is not evaluated. A compiler limit is an additional implementation constraint. |

## Existing foundations and hierarchy

`TemplateMetafunction` specializes `PartialFunction` with canonical finite template arguments as its input carrier and tagged type/value observations as its output carrier. The environment fixes declarations, visibility, instantiation point and the member being observed. Equal observations do not identify distinct template entities. Composition requires explicit adapters between a result and the next argument list.

`TemplateParameterPack` specializes `Sequence` by fixing one argument-kind carrier. It retains order, duplicates, length and the empty case, and adds expansion operations. Partial simultaneous expansion is undefined on unequal lengths; it never truncates.

`DependentFunction` remains a related concept with its existing total Pi-type semantics. `TermAlgebra` supplies reusable syntax-tree foundations rather than being duplicated. `PartialOrder`, `PropositionalFormula`, `FixedWidthSignedInteger` and other prerequisites retain their existing meanings. A C++ partial specialization is not class inheritance, and it is not automatically a graph `specializationOf` edge. No prerequisite or subject link transfers axioms.

## Profile and interpretation obligations

- **Arguments and instantiation:** canonical type identity, converted non-type argument equivalence, template-template compatibility, deduction, defaults and visibility require faithful frontend adapters. Nontermination and failed instantiation are outside a metafunction's successful domain; the Option-valued Lean interpretation does not decide arbitrary compilation.
- **Partial specializations:** the selected model covers class-template partial specializations, with the standard deduction/constraint ordering supplied explicitly. It does not derive C++ ordering from the sets of arguments accepted by patterns. Exact explicit specializations, function overload resolution and selected-body validity are separate mechanisms.
- **Substitution:** the immediate context is determined by language rules, not simply by textual nesting under `decltype` or another unevaluated operand. A reached helper/class instantiation can cause a hard error. Lexical early failure can prevent that instantiation from being required. Unsupported ill-formed-no-diagnostic-required cases are not misclassified as ordinary SFINAE failures.
- **Constraints:** language normalization of concept-ids and parameter mappings precedes this normalized-tree model. Invalid normalization can have its own diagnostics/IFNDR rules. Atom identity preserves source appearance and mapping, and is different from truth-value equivalence. C++20 fold constraints must not be silently given C++26 fold-expanded subsumption rules.
- **Packs:** pure total pattern functions are the selected abstraction; actual ill-formed pattern instantiations need a substitution/constraint analysis. Empty unary folds exist for `&&`, `||` and comma under the cited rules; unary `+` has no invented empty identity. Binary folds use their explicit initializer.
- **Lookup:** dependent unqualified-call candidate sets are supplied after eligibility/reachability filtering. An explicit guard accounts for ordinary lookup suppressing ADL. Qualified/member lookup, modules, current-instantiation details and cross-translation-unit consistency are not fully modeled.
- **Constant evaluation:** the small evaluator covers closed literal/add/multiply/Boolean-conditional trees in one fixed signed type of rank at least `int`, with implementation width recorded and literal leaves in range. It excludes mixed conversions, pointers, calls, state and recursion. Both branches must be structurally well-formed even though only one is evaluated. This does not make template arguments lazy, and does not model the full rules of `if constexpr` or `std::conditional_t`. `constexpr` alone does not force every invocation to be evaluated at compile time.

Compiler recursion/evaluation budgets and diagnostics are evidence about an implementation/configuration. Do not infer universal template termination, invalidity in every implementation, or mathematical proof from a finite compiler experiment.

## Compiler examples

[`examples/template_metaprogramming.cpp`](../examples/template_metaprogramming.cpp) maps assertions and rejection cases to stable catalog IDs. Its [companion document](../examples/template_metaprogramming.md) records the carriers, observations and expected outcomes. Run:

```sh
python3 scripts/check_template_examples.py --output /tmp/template-example-evidence.json
```

The standard-library-only runner checks the positive translation unit first, then eight independently enabled rejection cases. It uses `-std=c++20 -pedantic-errors -fsyntax-only`, records compiler/version, source hash, commands and diagnostics, and treats timeouts or compiler crashes as failed evidence. It does not install a compiler. Rejection diagnostics still need inspection to confirm the intended cause; a nonzero return code alone is not a semantic explanation.

## Retrieval and software generation

```sh
python3 scripts/catalog.py list --category template-metaprogramming
python3 scripts/catalog.py get TemplateMetafunction --sections operations axioms laws sources
python3 scripts/agent_query.py node urn:csabs:axiom/TemplateConstraint-identity-subsumption
python3 scripts/agent_query.py node urn:csabs:law/TemplateSubstitution-hard-error-is-not-sfinae
python3 scripts/lean.py get TemplateConstraint
```

Use [implementation-mapping](../ai/skills/implementation-mapping/SKILL.md) to connect intended compile-time behavior to template parameters, selected result members, candidate sets, atomic origins, numeric ranges and failure policy. Use [implementation-conformance](../ai/skills/implementation-conformance/SKILL.md) and [mathematical-tests](../ai/skills/mathematical-tests/SKILL.md) for code review and executable examples. Keep source gaps and required frontend assumptions visible; no graph-wide dump or runtime catalog dependency is needed.

## Lean scope

[`Catalog/TemplateMetaprogramming.lean`](../lean/Catalog/TemplateMetaprogramming.lean) models all seven concepts. The substitution and constraint bindings are explicitly partial: their actual syntax/context classification, normalization, atomic-identity resolution and compiler-expression adapters remain obligations. Other bindings interpret the selected mathematical carriers/interfaces; supplied matching, ordering and lookup sets still need justification against C++.

No new template law is registered as a compiled theorem witness. Model compilation establishes well-typed Lean declarations, not their correspondence to all C++ rules or the correctness of generated software. Pins and the existing witness set remain separate from these additions.
