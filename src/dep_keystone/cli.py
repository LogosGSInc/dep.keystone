from pathlib import Path
import json
import click

from dep_keystone.parsers.requirements_txt import parse_requirements_txt


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

    content = input_path.read_text(encoding="utf-8")

    if input_type == "requirements.txt":
        packages = parse_requirements_txt(content)
    else:
        raise click.ClickException(f"Unsupported input type: {input_type}")

    normalized_graph = {
        "input_type": input_type,
        "package_count": len(packages),
        "packages": packages,
    }

    output_file = out_dir / "normalized-graph.json"
    output_file.write_text(json.dumps(normalized_graph, indent=2), encoding="utf-8")

    click.echo(f"Wrote {output_file}")
