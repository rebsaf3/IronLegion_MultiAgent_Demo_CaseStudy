from __future__ import annotations
from typing import Dict, Any

REGISTRY: Dict[str, Dict[str, Any]] = {
    "onedrive_sharepoint": {
        "worker": "OneDriveSharePointWorker",
        "allowed_actions": ["read_page_by_path"],
        "required_selection": {"read_page_by_path": ["site", "page_path"]},
        "default_mode": "read_only",
    },
    "jira": {
        "worker": "JiraWorker",
        "allowed_actions": ["create_issue"],
        "required_selection": {"create_issue": ["project_key"]},
        "default_mode": "write_allowed_with_confirmation",
    },
    "teams": {
        "worker": "TeamsWorker",
        "allowed_actions": ["post_message"],
        "required_selection": {"post_message": ["team", "channel"]},
        "default_mode": "write_allowed_with_confirmation",
    },
    "ms365": {
        "worker": "MS365Worker",
        "allowed_actions": ["lookup_user"],
        "required_selection": {"lookup_user": []},
        "default_mode": "read_only",
    },
}
