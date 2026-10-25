from src.utils.masking import mask_email


def test_mask_email_basic():
    assert mask_email("john@example.com") == "jo***@e***.com"


def test_mask_email_short_local():
    assert mask_email("ab@x.com") == "***@x***.com"


def test_mask_email_no_at():
    assert mask_email("notanemail") == "***"
