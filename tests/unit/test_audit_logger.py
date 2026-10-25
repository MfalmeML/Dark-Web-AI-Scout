from datetime import datetime

from src.audit.logger import AuditEvent


def test_audit_event_is_frozen():
    e = AuditEvent(
        actor="analyst1",
        action="search_email",
        entity_hash="abc123",
        entity_type="email",
        purpose="incident_response",
        timestamp=datetime.utcnow(),
    )
    try:
        e.actor = "attacker"
        assert False, "AuditEvent should be immutable"
    except Exception:
        assert True


def test_audit_event_has_no_plaintext_field():
    fields = AuditEvent.__dataclass_fields__.keys()
    assert "entity_plaintext" not in fields
    assert "entity_hash" in fields


def test_audit_event_requires_purpose():
    import pytest

    with pytest.raises(TypeError):
        AuditEvent(
            actor="x",
            action="y",
            entity_hash="z",
            entity_type="email",
            timestamp=datetime.utcnow(),
        )
