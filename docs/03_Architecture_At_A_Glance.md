# Architecture at a Glance
Components
1. Orchestrator
Routes intent, enforces selection and disambiguation, and decides which worker to call

2. Agent registry
Defines which workers exist and what actions are allowed

3. Workers
Domain execution units with strict boundaries
MS365 Worker
OneDrive SharePoint Worker
Jira Worker
Teams Worker

4. Task envelope
A single schema that wraps every worker call and every response

5. Run log
Structured records for audit, testing, and debugging
