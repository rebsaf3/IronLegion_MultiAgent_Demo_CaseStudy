# Iron Legion Multi Agent Demo Case Study
This repository is a public case study plus a runnable demo harness that shows multi agent work in a simple, auditable way.

It is public safe. It contains no tenant identifiers, no internal urls, no secrets, and no proprietary data. It focuses on agent behavior, worker boundaries, and deterministic selection and disambiguation.

## What this repo demonstrates
1. Orchestrator that routes intent to specialized workers
2. Agent registry that controls which workers exist and what they can do
3. Task envelope schema used for every worker call and every response
4. Deterministic selection and disambiguation before targeted actions
5. Structured run logs for audit and testing
6. End to end scenarios you can run locally

## Quick start
1. Install Python 3.11 or later
2. From the repo root run
   python demos_run.py scenario_01_sharepoint_read.json
3. Review the output log in demos runs

## Repo map
docs: narrative case study
src: demo orchestrator and worker stubs
demos: scenarios and recorded run logs
tests: test pack and scoring rubric
assets: architecture visuals
governance: change control
redaction: public repo checklist

## License
MIT
