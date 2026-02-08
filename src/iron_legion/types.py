from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass
class TaskEnvelope:
    run_id: str
    intent: str
    domain: str
    action: str
    selection: Dict[str, Any] = field(default_factory=dict)
    inputs: Dict[str, Any] = field(default_factory=dict)
    constraints: Dict[str, Any] = field(default_factory=dict)
    requested_output_format: str = "text"

@dataclass
class WorkerResult:
    status: str
    data: Dict[str, Any] = field(default_factory=dict)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    audit: Dict[str, Any] = field(default_factory=dict)
