# Worked example: a sequential stack

This is an illustrative product contract, not a new catalog claim. Its clauses are:

- S1: Values are Python integers; equality compares ordered contents by value.
- S2: Starting from any finite stack, `push(x)` appends `x` as the top. There is no product capacity bound.
- S3: `pop()` on a nonempty stack returns its former top and removes exactly that element.
- S4: `pop()` on an empty stack raises `IndexError` without changing the stack.
- S5: `snapshot()` returns an immutable bottom-to-top observation of current contents.

The example is sequential. Allocation failure and interpreter resource exhaustion are excluded environment failures, not modeled success outcomes. This scope is an explicit example assumption; a real product must decide its own resource guarantees.

## Mapping

Retrieve `Stack` operations, its sequence-model/observer premises and selected laws from the catalog. The recorded Stack sequence uses the head as top, whereas the implementation below stores the top at the end. Define:

```text
concrete state: a private Python list L of integers
abstract state: A(L) = reverse(L), a sequence with the head as top
representation invariant: L is finite and all elements are integers
abstract equality: sequence value equality
snapshot observation: tuple(reverse(A(L))) = tuple(L)
```

`snapshot()` is a product observer used to compare abstract states; it is not claimed to be a primitive catalog Stack operation. S4 supplies behavior outside the catalog's nonempty domain for `pop`. Python's concrete `pop()` returns only the value; its mutated receiver supplies the resulting state in the catalog pair `(S, x)`.

| Obligation | Clause | Catalog record | Concrete obligation |
| --- | --- | --- | --- |
| O1 | S1 | Stack carrier/sequence model | Construction establishes the representation invariant. |
| O2 | S2 | `urn:csabs:operation/stack-push` | Every integer push is supported in the modeled environment and preserves the invariant. |
| O3 | S2, S3, S5 | `urn:csabs:law/stack-push-pop` | After push then pop, return x and restore the previous snapshot. |
| O4 | S4 | `urn:csabs:operation/stack-pop` (partial domain only) | Empty pop raises the product exception and preserves state. |

The selected catalog push/pop law is currently marked `legacy-source-missing`. Preserve that gap; the explicit product clauses justify the example's expected behavior independently. Resolve catalog versions/hashes and current metadata when applying this example.

## A mismatch that happy-path tests miss

Suppose generated `push` contains this code:

```python
if len(self._items) == 4:
    raise OverflowError("full")
self._items.append(x)
```

The representation invariant can still hold, and O3 can pass for small stacks. Nevertheless, starting with four integers, `push(9)` violates O2/S2: the product requires an outcome that the implementation rejects. The finding is an implementation mismatch under the stated environment, not an inconsistent specification or a failure of the push/pop law.

A growable list satisfies the chosen capacity policy within the example environment. A bounded-stack contract would be a behavior change requiring specification authority; silently filtering tests to stacks shorter than four would hide the defect.

## Runnable scoped evidence

Run this block with Python 3 in a scratch directory. It implements the relevant API and checks O3/O4 on selected inputs, including a push beyond the faulty capacity above. It does not prove refinement for every finite stack. S1's integer-only carrier is a precondition; invalid-type behavior is intentionally outside this example contract.

```python
class Stack:
    def __init__(self, values=()):
        self._items = list(values)

    def push(self, x):
        self._items.append(x)

    def pop(self):
        return self._items.pop()

    def snapshot(self):
        return tuple(self._items)


for initial in ((), (1,), (1, 2, 3, 4)):
    for x in (-1, 0, 9):
        stack = Stack(initial)
        before = stack.snapshot()
        stack.push(x)  # O2/S2: includes a push from length four.
        # O3/S2,S3,S5; urn:csabs:law/stack-push-pop:
        # returned value equals x; observed state equals the pre-push state.
        assert stack.pop() == x
        assert stack.snapshot() == before

empty = Stack()
before = empty.snapshot()
try:
    empty.pop()  # O4/S4: product-defined extension of the partial operation.
except IndexError:
    assert empty.snapshot() == before
else:
    raise AssertionError("empty pop must raise IndexError")
print("9 push/pop cases and the empty-error case passed")
```
