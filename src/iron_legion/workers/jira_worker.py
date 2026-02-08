from __future__ import annotations
from iron_legion.types import TaskEnvelope, WorkerResult
from iron_legion.workers.base import BaseWorker

class JiraWorker(BaseWorker):
    name = "Jira Worker"

    def run(self, task: TaskEnvelope) -> WorkerResult:
        required = ["project_key"]
        missing = self.validate_required_selection(task, required)
        if missing:
            return WorkerResult(
                status="needs_selection",
                errors=[f"missing_selection:{','.join(missing)}"],
                audit={"worker": self.name, "action": task.action},
            )

        summary = task.inputs.get("summary", "Untitled issue")
        description = task.inputs.get("description", "")
        project_key = task.selection["project_key"]

        issue_key = f"{project_key}_123"
        return WorkerResult(
            status="ok",
            data={"issue_key": issue_key, "summary": summary, "description": description},
            audit={"worker": self.name, "action": task.action, "project_key": project_key},
        )
