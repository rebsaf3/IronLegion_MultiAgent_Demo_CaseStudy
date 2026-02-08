````markdown
# Iron Legion Case Study: Multi Agent Governance
A practical case study showing how to build and operate a multi agent system that is safe, predictable, and scalable.

Iron Legion is the name of the framework pattern.
The goal is simple: deliver many business agents across teams without turning your org into an ungoverned bot petting zoo.

This repo is public safe.
No tenant identifiers. No internal urls. No secrets. No proprietary data.
Everything here is focused on repeatable patterns, clear contracts, and real world governance that you can apply in any platform.

## Who this case study is for
This repo is written for end users and stakeholders who want to understand what a multi agent system does and why governance matters.

It is also useful for builders because it includes scenarios, run logs, and a test pack that make the behavior reviewable.

If you have ever asked any of these questions, this case study is for you:
Why does our agent keep guessing where to write things
How do we let teams build agents without breaking compliance
How do we know the agent used approved content
How do we prevent silent regressions when prompts change
How do we prove to leadership that the agent is safe

## What Iron Legion is, in plain English
Iron Legion is a way to run agents like real products.

Instead of one agent trying to do everything, you use multiple specialized agents with strict roles.
A central orchestrator routes work to the right agent.
A registry defines what each agent is allowed to do.
Workers execute only within their domain.
A selection and disambiguation standard prevents wrong target actions.
Every hop is logged so outcomes are auditable.
Tests make changes safe.

That combination is what makes multi agent work trustworthy.

## What this case study demonstrates
This case study demonstrates a governed multi agent system end to end.

You will see
1. How a user request becomes an orchestrated task
2. How the system decides which agent should handle it
3. How governance rules prevent unsafe actions
4. How selection and disambiguation block execution when the target is unclear
5. How the system produces run logs that can be reviewed like evidence
6. How tests enforce quality and prevent regression

This is not about hype.
It is about building systems that do not confidently do the wrong thing.

## The multi agent roster
Iron Legion is built around a clear roster of agents. Each agent has a specific job and a defined contract.

### Orchestrator
What it does
Receives the task, determines intent, selects the correct worker, enforces governance rules, and blocks execution when required identifiers are missing.

Why it matters
This is the control point that keeps behavior consistent across the whole system.

### Agent Registry
What it does
Defines which agents exist, what actions they are allowed to perform, and what selection fields are required for each action.

Why it matters
This prevents tool sprawl and capability creep. It is the difference between a program and a free for all.

### OneDrive SharePoint Worker
What it does
Retrieves approved content by site and page path in a controlled way.

Hard rule
If the site or page path is missing or ambiguous, it refuses and requests selection.

Why it matters
Approved knowledge is a common requirement for HR, finance, legal, and other risk sensitive domains. This worker demonstrates that pattern.

### Jira Worker
What it does
Creates work items only after the correct project is selected.

Hard rule
If project_key is missing, it refuses and requests selection.
No project selection means no ticket.

Why it matters
This demonstrates write action governance. No guessing. No silent writes.

### Teams Worker
What it does
Posts a message only after the correct team and channel are selected.

Hard rule
If team or channel is missing, it refuses and requests selection.
No selection means no post.

Why it matters
Teams is a real world blast radius surface. This demonstrates how to prevent wrong channel mistakes.

### MS365 Worker
What it does
Handles safe, read oriented lookups and utility style tasks.

Hard rule
Read only behavior by default.

Why it matters
Many business workflows start with read operations. This worker shows how to keep read tasks bounded and safe.

## The defining behavior: selection and disambiguation
This is the core of governance in practice.

If a task requires a specific target and the target is not provided, execution stops.

The system returns
status needs_selection
and the exact missing fields

Nothing is created. Nothing is updated. Nothing is posted.
The system forces clarity before action.

This prevents the most common failure mode in real agent deployments:
The agent guessed the target and did the wrong thing confidently.

## What makes this a case study, not just code
This repo includes proof artifacts that make behavior reviewable for non technical stakeholders.

### Scenarios
Prebuilt scenario files show inputs for common multi agent flows.
They are written in a simple JSON format that mirrors how real orchestrators pass tasks to workers.

### Run logs
Each scenario produces a structured run log.
A run log is evidence of what happened, not a vibe.

A run log includes
1. The task envelope that was submitted
2. The domain and action selected
3. Whether selection was required and whether it was provided
4. The worker that was called
5. The worker response payload
6. Errors and warnings
7. Audit metadata

### Test pack
Tests define passing behavior and automatic fail rules.
This is how you prevent changes from quietly breaking safety.

## How to explore this case study
If you are here to understand the concept quickly, follow this path.

1. Read docs/01_Executive_Summary.md
2. Read docs/04_Task_Envelope_Spec.md
3. Read docs/05_Worker_Contracts.md
4. Open tests/Test_Pack.md
5. Run the scenarios and inspect the run logs

You do not need to be an engineer to follow the story.
The artifacts are designed to be readable.

## Run the demo locally
Requirements
Python 3.11 or later

Run Scenario 01
This scenario includes required selection and should succeed.
```bash
python demos_run.py scenario_01_sharepoint_read.json
````

Expected
status ok
and a run log written to demos/runs

Run Scenario 02
This scenario omits project selection and should be blocked.

```bash
python demos_run.py scenario_02_jira_create_needs_selection.json
```

Expected
status needs_selection
missing_selection includes project_key
no ticket created

Run Scenario 03
This scenario omits Teams targeting and should be blocked.

```bash
python demos_run.py scenario_03_teams_post_needs_selection.json
```

Expected
status needs_selection
missing_selection includes team and channel
no message posted

## Repository structure

docs
Narrative case study content written for end users

src
Orchestrator, registry rules, worker stubs, and contracts

demos/scenarios
Scenario inputs you can run

demos/runs
Generated run logs

tests
Test pack and scoring rubric

governance
Change control and change log

redaction
Public repo checklist

## What to ask next

If this case study matches problems you are facing, here are strong follow up questions that lead to real progress.

1. What are the highest risk actions you want agents to perform
2. Which domains need approved knowledge only constraints
3. What are your required identifiers for write actions in each system
4. What would an audit log need to capture for your leadership and compliance teams
5. What are your top twenty user intents by volume
6. What does a passing test pack look like for your environment

Those questions are where multi agent systems stop being theory and become operational.

## Governance and change control

See governance/Change_Control.md.

The rule is simple.
If you change routing, registry rules, worker contracts, or prompts, you re run scenarios and update tests.
If anything invents facts or executes without selection, it fails and rolls back.

## Public safe note

See redaction/Public_Redaction_Checklist.md before publishing any updates.
If a detail is not required to explain the design, remove it.

## License

MIT

```
```
