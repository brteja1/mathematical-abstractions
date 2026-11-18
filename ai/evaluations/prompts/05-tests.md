# Test a persistent FIFO queue

Write a standard-library `unittest` suite in `test_queue_api.py` for an implementation imported as `import queue_api as q`. API contract:

- `empty()` returns an empty persistent queue.
- `enqueue(state, value)` returns a queue with the integer value at the tail; the old queue remains unchanged.
- `dequeue(state)` returns `(oldest_value, new_state)`; empty dequeue raises `IndexError`.
- `contents(state)` returns the logical items as an immutable tuple in FIFO order.
- All Python integers and all finite lengths are supported. Repeated equal values remain distinct queue entries.

A candidate implementation is below. Save it verbatim as `queue_api.py` so your tests can run. Identify any failures without changing it. The tests should also accept other correct representations; only the listed functions are public.

```python
def empty(): return ()
def enqueue(state, value): return state + (value,)
def dequeue(state):
    if not state: raise IndexError("empty")
    return state[-1], state[:-1]
def contents(state): return tuple(state)
```

Map the properties to the API, run your tests, and report failures and evidence limits in `answer.md`. Do not inspect or change catalog records beyond reading relevant mathematical context.
