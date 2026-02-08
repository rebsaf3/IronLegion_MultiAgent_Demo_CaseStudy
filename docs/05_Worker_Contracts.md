# Worker Contracts
Each worker has a small contract.

Contract rules
1. Validate required fields
2. Refuse ambiguous targets
3. Default to read only unless write intent is explicit and allowed
4. Return structured outputs that can be logged
5. Never fabricate links, ids, or results

This demo implements worker stubs that simulate behavior.
In a real implementation, the stubs are replaced by platform tools.
