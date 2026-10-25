from src.utils.masking import mask_cc, mask_email, mask_password


def test_mask_email_basic():
    assert mask_email("john@example.com") == "jo***@e***.com"


def test_mask_email_short_local():
    assert mask_email("ab@x.com") == "***@x***.com"


def test_mask_email_no_at():
    assert mask_email("notanemail") == "***"


def test_mask_password_basic():
    assert mask_password("hunter2") == "hu***"


def test_mask_password_empty():
    assert mask_password("") == "***"


def test_mask_cc_basic():
    assert mask_cc("4111111111111111") == "41**********11"
