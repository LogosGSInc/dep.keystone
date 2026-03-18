import json
from pathlib import Path

from click.testing import CliRunner

from dep_keystone.cli import main


def test_verify_creates_artifacts(tmp_path: Path):
    runner = CliRunner()
    input_file = tmp_path / "requirements.txt"
    out_dir = tmp_path / "out"

    input_file.write_text("flask==3.0.0\nrequests==2.31.0\n", encoding="utf-8")

    result = runner.invoke(
        main,
        [
            "verify",
            "--input", str(input_file),
            "--type", "requirements.txt",
            "--out", str(out_dir),
        ],
    )

    assert result.exit_code == 0, result.output
    assert (out_dir / "normalized-graph.json").exists()
    assert (out_dir / "verification-report.json").exists()
    assert (out_dir / "evidence.sha256").exists()

    report = json.loads((out_dir / "verification-report.json").read_text(encoding="utf-8"))
    assert report["status"] == "generated"
    assert report["package_count"] == 2
