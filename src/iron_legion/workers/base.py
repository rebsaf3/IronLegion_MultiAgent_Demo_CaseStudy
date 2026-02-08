from __future__ import annotations
from typing import List
from iron_legion.types import TaskEnvelope, WorkerResult

class BaseWorker:
    name: str = "BaseWorker"

    def validate_required_selection(self, task: TaskEnvelope, required: List[str]) -> List[str]:
        missing = []
        for k in required:
            v = task.selection.get(k)
            if v is None or str(v).strip() == "":
                missing.append(k)
        return missing

    def run(self, task: TaskEnvelope) -> WorkerResult:
        raise NotImplementedError
