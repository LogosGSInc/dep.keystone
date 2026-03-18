from dep_keystone.models import VerificationReport


def build_verification_report(input_type: str, package_count: int, input_sha256: str) -> dict:
    report = VerificationReport(
        tool="DEP.KEYSTONE",
        version="0.1.0",
        input_type=input_type,
        package_count=package_count,
        input_sha256=input_sha256,
        status="generated",
        deterministic=True,
    )
    return {
        "tool": report.tool,
        "version": report.version,
        "input_type": report.input_type,
        "package_count": report.package_count,
        "input_sha256": report.input_sha256,
        "status": report.status,
        "deterministic": report.deterministic,
    }
