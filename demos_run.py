import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))

from iron_legion.orchestrator import Orchestrator, load_task

def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python demos_run.py <scenario_file>")
        return 2

    scenario_file = sys.argv[1]
    scenario_path = Path(__file__).parent / "demos" / "scenarios" / scenario_file
    task = load_task(str(scenario_path))

    orch = Orchestrator()
    result = orch.run_task(task)

    out_dir = Path(__file__).parent / "demos" / "runs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{task.run_id}.json"

    payload = {
        "task": task.__dict__,
        "result": result,
    }
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(str(out_path))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
