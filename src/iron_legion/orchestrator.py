from __future__ import annotations
import json
from typing import Dict, Any, List
from iron_legion.types import TaskEnvelope, WorkerResult
from iron_legion.registry import REGISTRY
from iron_legion.workers.onedrive_sharepoint_worker import OneDriveSharePointWorker
from iron_legion.workers.jira_worker import JiraWorker
from iron_legion.workers.teams_worker import TeamsWorker
from iron_legion.workers.ms365_worker import MS365Worker

WORKERS = {
    "OneDriveSharePointWorker": OneDriveSharePointWorker(),
    "JiraWorker": JiraWorker(),
    "TeamsWorker": TeamsWorker(),
    "MS365Worker": MS365Worker(),
}

class Orchestrator:
    def __init__(self) -> None:
        self.active_targets: Dict[str, Dict[str, Any]] = {}

    def required_selection(self, domain: str, action: str) -> List[str]:
        info = REGISTRY.get(domain, {})
        req = info.get("required_selection", {})
        return list(req.get(action, []))

    def run_task(self, task: TaskEnvelope) -> Dict[str, Any]:
        registry_entry = REGISTRY.get(task.domain)
        if not registry_entry:
            return {"status": "error", "errors": ["unknown_domain"], "audit": {"domain": task.domain}}

        if task.action not in registry_entry.get("allowed_actions", []):
            return {"status": "error", "errors": ["action_not_allowed"], "audit": {"domain": task.domain, "action": task.action}}

        required = self.required_selection(task.domain, task.action)

        if not task.selection and task.domain in self.active_targets:
            task.selection = dict(self.active_targets[task.domain])

        missing = [k for k in required if not str(task.selection.get(k, "")).strip()]
        if missing:
            return {
                "status": "needs_selection",
                "missing_selection": missing,
                "message": "selection_required",
                "audit": {"domain": task.domain, "action": task.action},
            }

        self.active_targets[task.domain] = dict(task.selection)

        worker_name = registry_entry["worker"]
        worker = WORKERS[worker_name]
        result: WorkerResult = worker.run(task)

        return {
            "status": result.status,
            "data": result.data,
            "warnings": result.warnings,
            "errors": result.errors,
            "audit": result.audit,
        }

def load_task(path: str) -> TaskEnvelope:
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    return TaskEnvelope(**raw)
