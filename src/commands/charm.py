"""Typer application to run charm-related commands."""

import logging
from typing import Annotated, Optional

import typer
from rich.console import Console

import services.charmcraft as charmcraft
from commands.charm_libraries import app as libraries_app

log = logging.getLogger(__name__)
console = Console()

app = typer.Typer()
app.add_typer(libraries_app, name="libraries", help="(+) Commands related to charm libraries.")


class InputError(Exception):
    """Exception due to wrong user or file input."""


@app.command()
def promote(
    charm: Annotated[
        str,
        typer.Argument(help="Charm name as registered in Charmhub.", show_default=False),
    ],
    source: Annotated[
        str,
        typer.Option(
            "--from",
            help="Channel in the format 'TRACK/RISK' (e.g., 'latest/edge').",
            show_default=False,
        ),
    ],
    dry_run: Annotated[
        bool,
        typer.Option(help="Only print releases instead of promoting the charm."),
    ] = False,
):
    """Promote a charm revision from a channel to the next risk channel.

    Example: 'latest/edge' will be promoted to 'latest/beta'.
    """
    source_channel = charmcraft.CharmChannel(source)
    target_channel = source_channel.next_risk_channel
    if source_channel.risk == "stable":
        raise InputError(
            f"Can't promote a charm from {source}: there's no lower risk than 'stable'."
        )

    charmcraft.promote(charm=charm, source=source, target=target_channel.name, dry_run=dry_run)


@app.command()
def promote_train(
    charm: Annotated[
        str,
        typer.Argument(help="Charm name as registered in Charmhub.", show_default=False),
    ],
    track: Annotated[
        str,
        typer.Option(help="Track to run the promotion train on.", show_default=False),
    ],
    dry_run: Annotated[
        bool,
        typer.Option(help="Only print the releases instead of promoting the charm"),
    ] = False,
):
    """Promote all the revisions in a track to their next risk channel.

    The revision in 'candidate' will be released to 'stable', 'beta' to 'candidate',
    and 'edge' to 'beta'.
    """
    # Validate the input
    if "/" in track:
        raise InputError(f"{track} is a channel. Please specify a track (e.g., 'latest').")
    # Execute the promotion train
    console.print(f"Promotion train for [b]{charm}[/b]")
    promote(charm, source=f"{track}/candidate", dry_run=dry_run)
    promote(charm, source=f"{track}/beta", dry_run=dry_run)
    promote(charm, source=f"{track}/edge", dry_run=dry_run)


@app.command()
def release(
    charm_path: Annotated[
        str,
        typer.Option(
            "--path",
            help="Path to the local '.charm' file to upload and release.",
            show_default=False,
        ),
    ],
    channel: Annotated[
        str,
        typer.Option(
            help="Channel to release the charm to (e.g., 'latest/edge').",
            show_default=False,
        ),
    ],
    charm_name: Annotated[
        Optional[str],
        typer.Argument(
            help="Charm name as registered in Charmhub. Parsed from metadata if not specified.",
            show_default=False,
            ),
        ] = None,
    dry_run: Annotated[
        bool,
        typer.Option(help="Only print the releases instead of promoting the charm."),
    ] = True,
    format_json: Annotated[
        bool, typer.Option("--json", help="If True print the CI status as a json.")
    ] = False,
):
    """Upload and release a local '.charm' file to Charmhub."""
    charm_name = charm_name or charmcraft.metadata()["name"]
    uploaded_charm = charmcraft.upload(charm_name=charm_name, path=charm_path, dry_run=dry_run)
    charmcraft.release(
        charm=charm_name,
        channel=channel,
        revision=uploaded_charm.revision,
        resources=[f"{r.name}:{r.revision}" for r in uploaded_charm.resources],
        dry_run=dry_run,
    )
    if format_json:
        console.print({"revision": uploaded_charm.revision})


@app.command()
def pack(
    filename: Annotated[
        str, typer.Argument(help="Path to a 'charmcraft.yaml' file to use to pack the charm.")
    ] = "charmcraft.yaml",
):
    """Pack a charm from any 'charmcraft.yaml' file."""
    charmcraft.pack(filename=filename)


# @app.command()
# def tag(charm_repo: str, )

if __name__ == "__main__":
    app()
