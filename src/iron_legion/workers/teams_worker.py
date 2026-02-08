from __future__ import annotations
from iron_legion.types import TaskEnvelope, WorkerResult
from iron_legion.workers.base import BaseWorker

class TeamsWorker(BaseWorker):
    name = "Teams Worker"

    def run(self, task: TaskEnvelope) -> WorkerResult:
        required = ["team", "channel"]
        missing = self.validate_required_selection(task, required)
        if missing:
            return WorkerResult(
                status="needs_selection",
                errors=[f"missing_selection:{','.join(missing)}"],
                audit={"worker": self.name, "action": task.action},
            )

        team = task.selection["team"]
        channel = task.selection["channel"]
        message = task.inputs.get("message", "")
        message_id = "MSG_001"

        return WorkerResult(
            status="ok",
            data={"team": team, "channel": channel, "message": message, "message_id": message_id},
            audit={"worker": self.name, "action": task.action},
        )
