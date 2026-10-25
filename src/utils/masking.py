"""Return first 2 chars of local part + domain TLD only. Example: jo***@g***.com"""
from src.config.loader import get_compliance_mode, load_config


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
    digits = "".join(c for c in value if c.isdigit())
    if len(digits) != 9:
        return "***"
    return f"***-**-{digits[-4:]}"


MASKERS = {
    "email": mask_email,
    "password": mask_password,
    "credit_card": mask_cc,
    "ssn": mask_ssn,
}


def mask(entity_type: str, value: str) -> str:
    fn = MASKERS.get(entity_type)
    return fn(value) if fn else "***"


def may_store_plaintext() -> bool:
    return get_compliance_mode(load_config()) != "strict"