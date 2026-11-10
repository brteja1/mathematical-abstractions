# VHDL generic interface example

Source: [generic_interfaces.vhd](generic_interfaces.vhd). Profiles and source locators: [generic-programming guide](../docs/GENERIC_PROGRAMMING.md).

**Status: illustrative and unexecuted locally.** Neither GHDL nor NVC is installed. The source uses a VHDL-2008-compatible subset of the cited IEEE 1076-2019 model; compiler support must be checked separately.

The generic package accepts a type and a positive width. One instantiation supplies named actuals in a different order from the declaration; another omits width and uses its constant default. The testbench checks the resulting array lengths and contains a null-range generate whose body would fail if incorrectly instantiated. Inline comments map each observation to its catalog law/axiom. Kind-specific subtype checking and declaration-order elaboration remain distinct from named matching.

With a supporting GHDL installation, from an isolated scratch directory run:

```sh
ghdl -a --std=08 /path/to/mathematical-abstractions/examples/generic_interfaces.vhd
ghdl --elab-run --std=08 generic_interfaces_tb --assert-level=error --stop-time=1ns
```

Expected observation: analysis/elaboration succeeds, lengths are 8 and 4, and no assertion fails. This is an expectation, not recorded execution evidence. The finite time limit is for this small example only and does not establish arbitrary design progress.

Useful negative variations are a named association followed by a positional one, a repeated whole-formal association, an omitted mandatory type actual, or `width => 0` violating `positive`. Check the language-required analysis/elaboration rejection and retain diagnostics; do not treat a compiler crash or unsupported generic feature as a demonstrated semantic rejection.

This example does not exercise all generic subprogram/package-formal rules, staticness cases, VHDL-2019 features, synthesis or simulation semantics. Passing it would provide scoped compiler evidence, not a proof of the catalog's universal claims.
