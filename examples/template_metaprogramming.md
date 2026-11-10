# C++20 template metaprogramming example

Source: [template_metaprogramming.cpp](template_metaprogramming.cpp). Model profiles and consulted clause references: [template metaprogramming guide](../docs/TEMPLATE_METAPROGRAMMING.md).

The example has no runtime oracle dependency. Its carriers are actual C++ types, `int` constants, template declarations and finite type packs; observations are `std::is_same_v`, integral `static_assert` results and compiler acceptance/rejection. The signed-integer range comes from `std::numeric_limits<int>`, not a guessed machine width. Patterns are pure, all successful examples have finite small instantiations, and lookup examples use one translation unit without modules. Comments connect each assertion group or rejection case to a stable catalog claim and the concrete observation being checked.

Run the repeatable checks from any directory:

```sh
python3 /path/to/mathematical-abstractions/scripts/check_template_examples.py --output /tmp/template-example-evidence.json
```

Use `--compiler clang++` to try another installed compiler. The runner first requires the baseline to compile, preventing a generally broken translation unit from making all rejection cases appear successful. Each negative macro is compiled independently:

| Macro suffix after `TMP_FAIL_` | Required observation |
| --- | --- |
| `WRONG_KIND` | A value cannot fill the type-argument position. |
| `AMBIGUITY` | Two matching incomparable partial specializations do not yield a winner. |
| `HARD_ERROR` | A required helper instantiation error is not absorbed as SFINAE. |
| `CONSTRAINT_BODY` | A reached helper body error is not an ordinary false constraint. |
| `ATOMIC_IDENTITY` | Separate requirement-expression origins do not acquire subsumption merely from equal behavior. |
| `PACK_LENGTH` | A simultaneous expansion rejects unequal pack lengths. |
| `EMPTY_FOLD` | An empty unary `+` fold is ill-formed. |
| `OVERFLOW` | A required constant expression rejects evaluated signed overflow. |

For one manual check:

```sh
g++ -std=c++20 -pedantic-errors -fsyntax-only examples/template_metaprogramming.cpp
g++ -std=c++20 -pedantic-errors -fsyntax-only -DTMP_FAIL_PACK_LENGTH examples/template_metaprogramming.cpp
```

The first command should succeed and the second should fail. Inspect retained diagnostics for the intended cause. A timeout, compiler crash or unavailable compiler is inconclusive/failed evidence. These examples establish behavior for the reported compiler and selected cases, not universal language correctness, implementation refinement or Lean proofs. Their direct catalog sources contain the authoritative provenance; successful compilation does not repair or replace citations.
