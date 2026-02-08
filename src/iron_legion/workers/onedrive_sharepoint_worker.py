from __future__ import annotations
from iron_legion.types import TaskEnvelope, WorkerResult
from iron_legion.workers.base import BaseWorker

class OneDriveSharePointWorker(BaseWorker):
    name = "OneDrive SharePoint Worker"

    def run(self, task: TaskEnvelope) -> WorkerResult:
        required = ["site", "page_path"]
        missing = self.validate_required_selection(task, required)
        if missing:
            return WorkerResult(
                status="needs_selection",
                errors=[f"missing_selection:{','.join(missing)}"],
                audit={"worker": self.name, "action": task.action},
            )

        site = task.selection["site"]
        page_path = task.selection["page_path"]

        content = f"Approved content placeholder for site {site} and page {page_path}."
        return WorkerResult(
            status="ok",
            data={"content": content, "site": site, "page_path": page_path},
            audit={"worker": self.name, "action": task.action},
        )
