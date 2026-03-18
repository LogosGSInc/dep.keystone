from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Package:
    name: str
    version: Optional[str]
    ecosystem: str


@dataclass(frozen=True)
class VerificationReport:
    tool: str
    version: str
    input_type: str
    package_count: int
    input_sha256: str
    status: str
    deterministic: bool
