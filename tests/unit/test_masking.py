from src.utils.masking import mask, mask_cc, mask_email, mask_password, mask_ssn


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
    assert mask_cc("4111111111111111") == "41************11"


def test_mask_cc_with_spaces():
    assert mask_cc("4111 1111 1111 1111") == "41************11"


def test_mask_ssn_basic():
    assert mask_ssn("123-45-6789") == "***-**-6789"


def test_mask_ssn_no_dashes():
    assert mask_ssn("123456789") == "***-**-6789"


def test_mask_dispatcher_unknown_type():
    assert mask("unknown", "anything") == "***"


def test_mask_dispatcher_routes_email():
    assert mask("email", "john@example.com") == "jo***@e***.com"
