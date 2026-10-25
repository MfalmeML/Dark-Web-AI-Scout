from src.utils.masking import mask_email


def test_mask_email_basic():
    assert mask_email("john@example.com") == "jo***@e***.com"
