"""Typer application to run commands related to charm libraries."""

import dataclasses
import json
from typing import Annotated

import typer
from rich.console import Console

import services.charmcraft as charmcraft

app = typer.Typer()

console = Console()


class InputError(Exception):
    """Exception due to wrong user or file input."""


@app.command()
def check(
    minor: Annotated[bool, typer.Option(help="Check for minor library updates")] = False,
    major: Annotated[bool, typer.Option(help="Check for major library updates.")] = False,
    format_json: Annotated[
        bool, typer.Option("--json", help="If True print the CI status as a json.")
    ] = False,
):
    """Check if charm libraries are updated to the latest version."""
    if not minor and not major:
        raise InputError("You must pass at least one of the '--minor' or '--major' flags.")
    libraries = charmcraft.outdated_charm_libraries(minor=minor, major=major)
    if format_json:
        libraries_dict = {k: dataclasses.asdict(v) for k, v in libraries.items()}
        console.print(json.dumps(libraries_dict))
    else:
        for library in libraries.values():
            console.print(
                f"([i]{library.charm_name}[/i]) [b]{library.library_name}[/b] "
                f"should be updated to {library.api}.{library.patch}"
            )


@app.command()
def print(
    format_json: Annotated[
        bool, typer.Option("--json", help="If True print the CI status as a json.")
    ] = False,
):
    """Print the charm libraries used by the charm, along with their version."""
    libraries = charmcraft.local_charm_libraries()
    if format_json:
        libraries_dict = {k: dataclasses.asdict(v) for k, v in libraries.items()}
        console.print(json.dumps(libraries_dict))
    else:
        console.print("Charm libraries used by the charm:")
        console.print(libraries)


@app.command()
def publish(
    dry_run: Annotated[
        bool,
        typer.Option(help="Only print the library that would be released"),
    ] = True,
):
    """Publish all the charm libraries that belong to the charm."""
    charmcraft.publish_charm_libraries(dry_run)
