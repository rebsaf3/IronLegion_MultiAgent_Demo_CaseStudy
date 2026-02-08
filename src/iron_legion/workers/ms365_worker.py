from __future__ import annotations
from iron_legion.types import TaskEnvelope, WorkerResult
from iron_legion.workers.base import BaseWorker

class MS365Worker(BaseWorker):
    name = "MS365 Worker"

    def run(self, task: TaskEnvelope) -> WorkerResult:
        query = task.inputs.get("query", "")
        if not query.strip():
            return WorkerResult(status="error", errors=["missing_query"], audit={"worker": self.name, "action": task.action})
        return WorkerResult(status="ok", data={"query": query, "result": "User lookup placeholder"}, audit={"worker": self.name, "action": task.action})
