import click

@click.group()
def main():
    """DEP.KEYSTONE CLI."""
    pass

@main.command()
def verify():
    """Run verification."""
    click.echo("DEP.KEYSTONE verify invoked")
