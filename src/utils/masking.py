"""Return first 2 chars of local part + domain TLD only. Example: jo***@g***.com"""
def mask_email(value: str) -> str:
    if "@" not in value:
        return "***"
    local, domain = value.split("@", 1)
    masked_local = local[:2] + "***" if len(local) > 2 else "***"
    tld = domain.split(".")[-1]
    return f"{masked_local}@{domain[0]}***.{tld}"


def mask_password(value: str) -> str:
    if not value:
        return "***"
    if len(value) <= 2:
        return "***"
    return value[:2] + "***"


def mask_cc(value: str) -> str:
    digits = "".join(c for c in value if c.isdigit())
    if len(digits) < 4:
        return "***"
    return digits[:2] + "*" * (len(digits) - 4) + digits[-2:]


def mask_ssn(value: str) -> str:
    ...