from dataclasses import dataclass
from datetime import datetime
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


def log_event(event: AuditEvent) -> None:
    ...
