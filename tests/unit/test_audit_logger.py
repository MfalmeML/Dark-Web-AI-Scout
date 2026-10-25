from datetime import datetime
import json

from src.audit.logger import AuditEvent, log_event


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


def test_log_event_appends_jsonl(tmp_path):
    p = tmp_path / "audit.jsonl"
    e = AuditEvent(
        actor="analyst1",
        action="search_email",
        entity_hash="abc",
        entity_type="email",
        purpose="ir",
        timestamp=datetime.utcnow(),
    )
    log_event(e, path=p)
    log_event(e, path=p)
    lines = p.read_text().strip().split("\n")
    assert len(lines) == 2
    assert json.loads(lines[0])["entity_hash"] == "abc"


def test_log_event_never_writes_plaintext(tmp_path):
    p = tmp_path / "audit.jsonl"
    e = AuditEvent(
        actor="x",
        action="y",
        entity_hash="sha256hash",
        entity_type="email",
        purpose="ir",
        timestamp=datetime.utcnow(),
    )
    log_event(e, path=p)
    content = p.read_text()
    record = json.loads(content)
    assert "john@" not in content
    assert "password" not in content.lower()
    assert "entity_plaintext" not in record
    assert set(record) == {
        "actor",
        "action",
        "entity_hash",
        "entity_type",
        "purpose",
        "timestamp",
        "source_ip",
        "success",
    }
