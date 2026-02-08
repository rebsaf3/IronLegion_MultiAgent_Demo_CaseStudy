# Task Envelope Spec
Every worker call uses the same envelope.

Fields
1. run_id
2. intent
3. domain
4. action
5. selection
6. inputs
7. constraints
8. requested_output_format

Selection and disambiguation
If selection is missing and the action requires it, the orchestrator must pause and request selection.

Worker response fields
1. status
2. data
3. warnings
4. errors
5. audit
