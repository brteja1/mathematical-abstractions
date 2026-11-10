# Java generic examples

Source: [GenericExamples.java](GenericExamples.java). Profiles and source locators: [generic-programming guide](../docs/GENERIC_PROGRAMMING.md).

Carriers are Java nominal types, boxed numbers, lists and fresh wildcard capture variables. Observations are static type acceptance, rejection diagnostics and explicit runtime checks. The examples avoid raw/unchecked conversions. Each source assertion group and rejection snippet in the runner identifies the catalog claim/operation and the concrete observation it exercises.

```sh
python3 scripts/check_java_generic_examples.py --output /tmp/java-generic-evidence.json
```

The runner uses installed `javac`/`java` and a temporary output directory, compiles with `--release 21 -Xlint:all -Werror`, and runs the positive example before the six independently compiled rejection cases. The target can be changed with `--release`; that does not change the recorded reference profile automatically. The catalog reference is SE25 JLS, while these selected examples exercise established Java generics rules using the installed Java 21 toolchain.

| Case | Claim-to-observation mapping |
| --- | --- |
| Positive member substitution | `JavaParameterizedType-member-argument-replacement`: `Box<Integer>.get()` has type `Integer`. |
| Positive wildcard capture | `JavaWildcardCapture-super-capture-lower-bound` and `fresh-nonrecursive`: a lower-bounded list accepts `Integer`, while a helper captures one unknown type for a read/write round trip. |
| Positive target inference | `JavaTypeInference-target-narrows-solutions`: `List<Number>` target and an integer input admit an appropriate inferred parameter. |
| Positive erasure | `JavaTypeErasure-same-head-erasure`: two source parameterizations have the same runtime class. |
| `bound` | A `String` actual violates `T extends Number`. |
| `invariance` | An integer list cannot be assigned to `List<Number>` merely from element subtyping. |
| `extends-write` | A captured upper bound does not authorize inserting an arbitrary value of that bound. |
| `capture-mismatch` | Separate wildcard captures do not automatically identify their unknown element types. |
| `erasure-clash` | Two methods cannot be distinguished by `List<String>` versus `List<Integer>` parameter signatures after erasure. |
| `target-conflict` | A `List<String>` target conflicts with the numeric inference bound. |

JSON evidence retains compiler/version, release, command/result, source variant hashes, selected catalog/premise/source fingerprint and diagnostics. Inspect rejection diagnostics for their intended cause; a nonzero process exit alone is not a language-semantic explanation. Timeouts/tool failures are not successful rejection evidence. Temporary class files are removed; commands using their paths must be rerun through the runner.

These are finite observations for the reported toolchain. They do not prove full Java conformance, universal implementation refinement, capture metatheorems or Lean witnesses.
