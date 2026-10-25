from src.config.loader import get_compliance_mode


def test_unknown_mode_fails_closed():
    assert get_compliance_mode({"safety": {"compliance_mode": "yolo"}}) == "strict"


def test_missing_section_fails_closed():
    assert get_compliance_mode({}) == "strict"


def test_valid_mode_passes_through():
    assert (
        get_compliance_mode({"safety": {"compliance_mode": "research"}})
        == "research"
    )
