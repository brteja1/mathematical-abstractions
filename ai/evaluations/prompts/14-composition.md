# Review a composed quota service

Two components each hold a local counter, initially zero. Each has a proved local contract: reserve(k) accepts any positive k if local + k ≤ 10, then adds k; otherwise it rejects. A gateway sends each request to either component and promises that the total accepted outstanding allocation across both never exceeds 10. Requests to different components may overlap; there is no shared lock or coordinator. Releases are outside this task.

Determine whether the component contracts establish the gateway guarantee. Write mapping.md with component assumptions, system invariant, interface/ownership mapping and outstanding composition obligations. Produce and run checks.py with an explicit counterexample if needed, then propose a coherent repair and analyze its assumptions. Do not assert timing or starvation guarantees absent evidence. Keep repairs as proposals and do not edit the catalog. Record findings and evidence scope in answer.md.
