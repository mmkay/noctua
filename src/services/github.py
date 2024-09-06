"""Wrapper around the GitHub CLI."""

import json
import re
from dataclasses import dataclass
from typing import Dict, List, Literal, Optional

import sh
from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeRemainingColumn,
)

# pyright: reportAttributeAccessIssue=false

console = Console()


@dataclass
class WorkflowStatus:
    """A GitHub workflow."""

    name: str
    status: Literal[
        # From GitHub API
        "action_required",
        "cancelled",
        "failure",
        "neutral",
        "success",
        "skipped",
        "stale",
        "timed_out",
        # Custom statuses
        "missing",
        "no runs",
        "queued",
    ]
    url: Optional[str] = None


@dataclass
class GithubRepo:
    """A GitHub repository wrapper."""

    full_name: str

    @property
    def name(self) -> str:
        """Return the repository name, without the organization."""
        return self.full_name.split("/")[1]

    @property
    def readme(self) -> str:
        """Return the repository README."""
        return sh.gh.repo.view(self.full_name, _tty_out=False)

    @property
    def workflows_in_readme(self) -> List[str]:
        """Extract the workflows that have badges on a repository's README."""
        badges_regex = re.compile(
            rf"\!\[.*\]\(https://github.com/{self.full_name}/actions/workflows/(.+)/badge.svg\)"
        )
        return re.findall(badges_regex, self.readme)

    def workflow_status(self, workflow: str) -> WorkflowStatus:
        """Return the status of the specified workflow.

        Args:
            workflow: The name of the YAML file of a workflow.
        """
        try:
            run_statuses = json.loads(
                sh.gh.run.list(
                    repo=self.full_name,
                    workflow=workflow,
                    json="conclusion,status,url",
                    limit=1,
                    _tty_out=False,
                )
            )
            if not run_statuses:  # The workflow exists, but has no runs yet
                return WorkflowStatus(name=workflow, status="no runs")
            run_status = run_statuses[0]  # We selected one run with limit=1
            if not run_status["conclusion"] and run_status["status"] == "queued":
                return WorkflowStatus(name=workflow, status="queued")
            return WorkflowStatus(
                name=workflow, status=run_status["conclusion"], url=run_status["url"]
            )
        except sh.ErrorReturnCode_1:  # The workflow has been removed from the repo
            return WorkflowStatus(name=workflow, status="missing")


def team_ci_status(team_name: str):
    """Return the CI status of all unarchived repos under the specified Canonical team."""
    team_repos = json.loads(
        sh.gh.api(f"orgs/canonical/teams/{team_name}/repos", paginate=True, _tty_out=False)
    )
    repos = [GithubRepo(full_name=r["full_name"]) for r in team_repos if not r["archived"]]
    repos.sort(key=lambda x: x.full_name)
    ci_status: Dict[str, List[WorkflowStatus]] = {}
    progress = Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=20),
        TaskProgressColumn(),
        TimeRemainingColumn(),
        SpinnerColumn(spinner_name="line"),
        TextColumn("{task.fields[repo]}"),
        transient=True,
    )
    progress_task = progress.add_task("Fetching CI", total=len(repos), repo="")
    with progress:
        for repo in repos:
            progress.update(progress_task, advance=1, repo=repo.name)
            ci_status[repo.name] = []
            # Process repositories with no badges in the README
            workflows = repo.workflows_in_readme
            if not workflows:
                continue

            # For each workflow, report its status
            for workflow_yaml in workflows:
                workflow_status: WorkflowStatus = repo.workflow_status((workflow_yaml))
                ci_status[repo.name].append(workflow_status)

    return ci_status
