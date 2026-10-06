"""Command line interface for nowolf."""

import typer

from nowolf import __version__

app = typer.Typer()

def _show_version(value: bool) -> None:
    if value:
        typer.echo(__version__)
        raise typer.Exit()

@app.callback()
def main(version: bool = typer.Option(False, "--version", callback=_show_version)) -> None:
    """A local LLM code reviewer"""


