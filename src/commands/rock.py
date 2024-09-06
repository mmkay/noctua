"""Typer application to run rock-related commands."""

import logging
import os
from typing import Annotated, List

import typer
import yaml
from rich.console import Console

import services.rockcraft as rockcraft

log = logging.getLogger(__name__)
console = Console()

app = typer.Typer()


class InputError(Exception):
    """Exception due to wrong user or file input."""


@app.command()
def status(
    rock_name: Annotated[str, typer.Argument(help="Name of a rock built in OCI Factory.")],
):
    """Print the diff between local tags and the ones currently in OCI Factory."""
    locals = rockcraft.local_tags(os.listdir())
    remote = rockcraft.oci_factory_tags(rock_name=rock_name)

    only_locals = [v for v in locals.keys() if v not in remote]
    if not only_locals:
        console.print(f"[b]{rock_name}[/b] is [green]in sync[/green] with OCI Factory.")
    else:
        console.print(
            f"[b]{rock_name}[/b] is [red]out of sync[/red]: "
            f"the following versions exist locally, but not on OCI Factory: {only_locals}"
        )


@app.command()
def manifest(
    rock_repo: Annotated[
        str,
        typer.Argument(
            help="Full name of the rock repository (e.g., 'canonical/prometheus-rock')."
        ),
    ],
    commit_sha: Annotated[
        str,
        typer.Option(
            "--commit", help="SHA of the commit on the rock repo to point at", show_default=False
        ),
    ],
    version_list: Annotated[
        List[str],
        typer.Option(
            "--version",
            help="Rock version to build the manifest for (you can pass multiple)",
            show_default=False,
        ),
    ],
    base: Annotated[str, typer.Option(help="Base to append to the tags")] = "22.04",
):
    """Generate the 'image.yaml' manifest for OCI Factory."""
    # Get the tags to apply to each version
    versions_with_tags = rockcraft.local_tags(os.listdir())
    selected_versions = {k: v for k, v in versions_with_tags.items() if k in version_list}
    # Append the -base suffix to the tag
    for version, tags in selected_versions.items():
        selected_versions[version] = [f"{t}-{base}" for t in tags]
    # Validate the rock_repo
    if len(rock_repo.split("/")) != 2:
        raise InputError(
            f"The provided repository '{rock_repo}' is invalid; "
            "please use a full repository name (e.g., 'canonical/prometheus-rock')"
        )
    # Validate the input versions
    for version in version_list:
        if version not in selected_versions:
            raise InputError(
                f"The specified rock version '{version}' doesn't exist locally. "
                f"Existing versions: {list(versions_with_tags.keys())}"
            )

    # Generate the 'image.yaml' manifest
    manifest = rockcraft.oci_factory_manifest(
        repository=rock_repo, commit=commit_sha, versions_with_tags=selected_versions
    )
    console.print(yaml.dump(manifest, sort_keys=False))


if __name__ == "__main__":
    app()
