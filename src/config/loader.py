from pathlib import Path
from typing import Literal

import yaml


ComplianceMode = Literal["strict", "research", "off"]

_DEFAULTS = {"safety": {"compliance_mode": "strict"}}


def load_config(path: Path = Path("configs/default.yaml")) -> dict:
    if not path.exists():
        return dict(_DEFAULTS)
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or dict(_DEFAULTS)


def get_compliance_mode(cfg: dict) -> ComplianceMode:
    mode = cfg.get("safety", {}).get("compliance_mode", "strict")
    if mode not in ("strict", "research", "off"):
        return "strict"
    return mode
