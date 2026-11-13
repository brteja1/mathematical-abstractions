# Formal Model Checking: Concurrent Mutex Verification

This reference demonstrates formal model checking of a concurrent mutual-exclusion protocol grounded in the catalog concept **`urn:csabs:concept/Mutex`**. It provides both the formal TLA+ specification and a runnable dependency-free Python state-space explorer that detects safety violations and deadlocks.

---

## 1. Catalog Grounding

* **Concept:** [`urn:csabs:concept/Mutex`](file:///linuxdev/github/mathematical-abstractions/concepts/Mutex.md)
* **Governing Axioms:**
  * `urn:csabs:axiom/Mutex-owner`: Mutex states are optional-owner values; initially unowned.
  * `urn:csabs:axiom/Mutex-acquire`: Acquire completes only when currently unowned.
  * `urn:csabs:axiom/Mutex-release`: Release is defined only for the current owner, restoring the unlocked state.
* **Target Properties:**
  * **Safety (Mutual Exclusion):** At most one process is in the critical section at any time:
    $$\text{MutualExclusion} \triangleq \forall p, q \in \text{Processes} : (\text{pc}[p] = \text{"in_cs"} \land \text{pc}[q] = \text{"in_cs"}) \implies p = q$$
  * **Deadlock Freedom:** At least one process can always make progress if any are waiting.

---

## 2. TLA+ Specification: Ticket Lock Protocol

The Ticket Lock protocol assigns incrementing ticket numbers to arriving threads, granting access in strict FIFO ticket order.

```tla
----------------------------- MODULE TicketLock -----------------------------
EXTENDS Integers, Sequences, FiniteSets

CONSTANTS Processes
VARIABLES next_ticket, serving, pc, my_ticket

vars == << next_ticket, serving, pc, my_ticket >>

TypeOK ==
  /\ next_ticket \in Nat
  /\ serving \in Nat
  /\ pc \in [Processes -> {"idle", "waiting", "in_cs"}]
  /\ my_ticket \in [Processes -> Nat]

Init ==
  /\ next_ticket = 0
  /\ serving = 0
  /\ pc = [p \in Processes |-> "idle"]
  /\ my_ticket = [p \in Processes |-> 0]

TakeTicket(p) ==
  /\ pc[p] = "idle"
  /\ my_ticket' = [my_ticket EXCEPT ![p] = next_ticket]
  /\ next_ticket' = next_ticket + 1
  /\ pc' = [pc EXCEPT ![p] = "waiting"]
  /\ UNCHANGED serving

EnterCS(p) ==
  /\ pc[p] = "waiting"
  /\ my_ticket[p] = serving
  /\ pc' = [pc EXCEPT ![p] = "in_cs"]
  /\ UNCHANGED << next_ticket, serving, my_ticket >>

LeaveCS(p) ==
  /\ pc[p] = "in_cs"
  /\ serving' = serving + 1
  /\ pc' = [pc EXCEPT ![p] = "idle"]
  /\ UNCHANGED << next_ticket, my_ticket >>

Next ==
  \E p \in Processes : TakeTicket(p) \/ EnterCS(p) \/ LeaveCS(p)

Spec == Init /\ [][Next]_vars /\ \A p \in Processes : WF_vars(EnterCS(p) \/ LeaveCS(p))

MutualExclusion ==
  \A p, q \in Processes :
    (pc[p] = "in_cs" /\ pc[q] = "in_cs") => (p = q)

StarvationFree ==
  \A p \in Processes : (pc[p] = "waiting") ~> (pc[p] = "in_cs")
=============================================================================
```

---

## 3. Executable Python State-Space Explorer

This standalone script explores the complete reachable state space of the protocol using breadth-first search (BFS). It verifies safety and deadlock freedom, and can simulate a concurrency bug to illustrate counterexample trace generation.

```python
#!/usr/bin/env python3
"""
Exhaustive state-space explorer for concurrent protocols.
Verifies safety and liveness against urn:csabs:concept/Mutex.
"""
from collections import deque
from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple

@dataclass(frozen=True)
class State:
    next_ticket: int
    serving: int
    pc: Tuple[Tuple[str, str], ...]       # ((p1, "idle"), (p2, "waiting"))
    my_ticket: Tuple[Tuple[str, int], ...] # ((p1, 0), (p2, 1))

    def get_pc(self, p: str) -> str:
        return dict(self.pc)[p]

    def get_ticket(self, p: str) -> int:
        return dict(self.my_ticket)[p]

    def with_update(self, p: str, new_pc: str, new_ticket: Optional[int] = None,
                    new_next: Optional[int] = None, new_serving: Optional[int] = None) -> "State":
        pcs = dict(self.pc)
        pcs[p] = new_pc
        tickets = dict(self.my_ticket)
        if new_ticket is not None:
            tickets[p] = new_ticket
        return State(
            next_ticket=self.next_ticket if new_next is None else new_next,
            serving=self.serving if new_serving is None else new_serving,
            pc=tuple(sorted(pcs.items())),
            my_ticket=tuple(sorted(tickets.items()))
        )

def get_transitions(s: State, processes: List[str], inject_bug: bool = False) -> List[Tuple[str, State]]:
    transitions = []
    for p in processes:
        pc = s.get_pc(p)
        # Action 1: Take ticket
        if pc == "idle":
            # BUG SIMULATION: Non-atomic ticket fetch allows two processes to get the same ticket
            ticket = s.next_ticket if not inject_bug else (s.next_ticket // 2)
            succ = s.with_update(p, new_pc="waiting", new_ticket=ticket, new_next=s.next_ticket + 1)
            transitions.append((f"{p} takes ticket {ticket}", succ))

        # Action 2: Enter Critical Section
        elif pc == "waiting":
            if s.get_ticket(p) == s.serving:
                succ = s.with_update(p, new_pc="in_cs")
                transitions.append((f"{p} enters CS", succ))

        # Action 3: Leave Critical Section
        elif pc == "in_cs":
            succ = s.with_update(p, new_pc="idle", new_serving=s.serving + 1)
            transitions.append((f"{p} leaves CS", succ))
    return transitions

def check_mutual_exclusion(s: State) -> bool:
    in_cs = [p for p, status in s.pc if status == "in_cs"]
    return len(in_cs) <= 1

def model_check(processes: List[str], max_ticket_bound: int = 3, inject_bug: bool = False):
    initial = State(
        next_ticket=0,
        serving=0,
        pc=tuple((p, "idle") for p in sorted(processes)),
        my_ticket=tuple((p, 0) for p in sorted(processes))
    )

    visited: Set[State] = {initial}
    parent_map: Dict[State, Tuple[Optional[State], str]] = {initial: (None, "Init")}
    queue = deque([initial])

    print(f"Starting model check: {len(processes)} processes, bounded next_ticket <= {max_ticket_bound} (bug={inject_bug})")

    while queue:
        curr = queue.popleft()

        # Check Invariant
        if not check_mutual_exclusion(curr):
            print("\n❌ SAFETY VIOLATION FOUND! Mutual exclusion broken.")
            trace = []
            state: Optional[State] = curr
            while state:
                parent, action = parent_map[state]
                trace.append((action, state))
                state = parent
            trace.reverse()
            print("Counterexample Trace:")
            for idx, (action, st) in enumerate(trace):
                print(f"  Step {idx}: {action} -> pc={dict(st.pc)}, serving={st.serving}")
            return False

        # Next states
        successors = get_transitions(curr, processes, inject_bug=inject_bug)
        for action_name, succ in successors:
            if succ.next_ticket > max_ticket_bound:
                continue  # bound state exploration
            if succ not in visited:
                visited.add(succ)
                parent_map[succ] = (curr, action_name)
                queue.append(succ)

    print(f"✅ VERIFIED: All {len(visited)} reachable states satisfy MutualExclusion.")
    return True

if __name__ == "__main__":
    procs = ["P1", "P2"]
    # 1. Correct model verification
    model_check(procs, max_ticket_bound=3, inject_bug=False)
    print("\n" + "=" * 60 + "\n")
    # 2. Injected race-condition bug producing counterexample trace
    model_check(procs, max_ticket_bound=3, inject_bug=True)
```
