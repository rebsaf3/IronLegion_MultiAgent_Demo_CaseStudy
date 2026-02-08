# Why Multi Agent
Single agent designs break down as scope grows.
A multi agent design splits work into focused roles.

Benefits
1. Clear tool boundaries per worker domain
2. Easier testing because each worker has a small contract
3. Lower risk because the orchestrator can block unsafe actions
4. Better auditing because every hop is logged

Tradeoffs
1. More structure to maintain
2. Requires a registry and contracts
3. Requires evaluation and change control or it still drifts
