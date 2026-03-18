from pathlib import Path
import json
import click

from dep_keystone.parsers.requirements_txt import parse_requirements_txt
from dep_keystone.hashing import sha256_file_bytes
from dep_keystone.report import build_verification_report
from dep_keystone.sbom import build_sbom


@click.group()
def main():
    """DEP.KEYSTONE CLI."""
    pass


@main.command()
@click.option("--input", "input_path", required=True, type=click.Path(exists=True, path_type=Path))
@click.option("--type", "input_type", required=True, type=click.Choice(["requirements.txt"]))
@click.option("--out", "out_dir", required=True, type=click.Path(path_type=Path))
def verify(input_path: Path, input_type: str, out_dir: Path):
    """Run verification."""
    out_dir.mkdir(parents=True, exist_ok=True)

    raw_bytes = input_path.read_bytes()
    content = raw_bytes.decode("utf-8")

    if input_type == "requirements.txt":
        packages = parse_requirements_txt(content)
    else:
        raise click.ClickException(f"Unsupported input type: {input_type}")

    normalized_graph = {
        "input_type": input_type,
        "package_count": len(packages),
        "packages": packages,
    }

    report = build_verification_report(
        input_type=input_type,
        package_count=len(packages),
        input_sha256=sha256_file_bytes(raw_bytes),
    )

    sbom = build_sbom(normalized_graph)

    (out_dir / "normalized-graph.json").write_text(json.dumps(normalized_graph, indent=2))
    (out_dir / "verification-report.json").write_text(json.dumps(report, indent=2))
    (out_dir / "sbom.cdx.json").write_text(json.dumps(sbom, indent=2))
    (out_dir / "evidence.sha256").write_text(report["input_sha256"] + "\n")

    click.echo(f"Wrote artifacts to {out_dir}")
