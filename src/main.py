"""Main Typer application to assemble the CLI."""

import logging

import typer
from rich.logging import RichHandler

from commands import charm, report, rock

log = logging.getLogger(__name__)

app = typer.Typer()
app.add_typer(report.app, name="report")
app.add_typer(charm.app, name="charm")
app.add_typer(rock.app, name="rock")


@app.callback()
def enable_logs(verbose: bool = False):
    """Enable INFO logging."""
    if verbose:
        logging.basicConfig(level=logging.INFO, handlers=[RichHandler()])


if __name__ == "__main__":
    app()
