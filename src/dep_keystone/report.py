def build_verification_report(input_type: str, package_count: int, input_sha256: str) -> dict:
    return {
        "tool": "DEP.KEYSTONE",
        "version": "0.1.0",
        "input_type": input_type,
        "package_count": package_count,
        "input_sha256": input_sha256,
        "status": "verified",
        "deterministic": True,
    }
