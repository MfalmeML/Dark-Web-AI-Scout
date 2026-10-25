from dataclasses import dataclass
from datetime import datetime
import json
from pathlib import Path
from typing import Optional


@dataclass(frozen=True)
class AuditEvent:
    actor: str
    action: str
    entity_hash: str
    entity_type: str
    purpose: str
    timestamp: datetime
    source_ip: Optional[str] = None
    success: bool = True


AUDIT_PATH = Path("audit_log.jsonl")


def log_event(event: AuditEvent, path: Path = AUDIT_PATH) -> None:
    record = {
        "actor": event.actor,
        "action": event.action,
        "entity_hash": event.entity_hash,
        "entity_type": event.entity_type,
        "purpose": event.purpose,
        "timestamp": event.timestamp.isoformat(),
        "source_ip": event.source_ip,
        "success": event.success,
    }
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
