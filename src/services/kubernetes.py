"""Wraps and extend `charmcraft` commands."""

import sh
from rich.console import Console
from tenacity import TryAgain, retry, wait_fixed

# pyright: reportAttributeAccessIssue=false

console = Console()


class InputError(Exception):
    """Exception due to wrong user or file input."""


class KubernetesError(Exception):
    """Triggered by a failure in a Kubernetes interaction."""


def _is_pod_running(pod: str, namespace: str) -> bool:
    """Check if a pod is in the Running status."""
    pod_status = sh.kubectl.get.pod(
        pod, namespace=namespace, output="jsonpath={.status.phase}", _long_sep=" "
    )
    return pod_status == "Running"


@retry(wait=wait_fixed(1))  # TODO: add  max retries
def _wait_for_pod(pod: str, namespace: str):
    """Wait for a pod to be in Running status."""
    if not _is_pod_running(pod=pod, namespace=namespace):
        raise TryAgain


def _pod_exists(pod: str, namespace: str) -> bool:
    """Check if a pod exists."""
    try:
        sh.kubectl.get.pod(pod, namespace=namespace, _out=None)
        return True
    except sh.ErrorReturnCode_1:
        return False


def run(pod: str, namespace: str, image_uri: str):
    """Run a pod from the specified image."""
    console.print(f"Running {pod}... ", end="")
    if _pod_exists(pod=pod, namespace=namespace):
        console.print("already up.")
        return
    sh.kubectl.run(pod, image=image_uri, namespace=namespace)
    console.print("done.")


def stop(pod: str, namespace: str):
    """Delete a pod."""
    sh.kubectl.delete.pod(pod, namespace=namespace)
    console.print(f"{pod} deleted")


def open_shell(pod: str, namespace: str):
    """Open a shell into a Running pod."""
    console.print(f"Opening a shell into {pod}")
    _wait_for_pod(pod=pod, namespace=namespace)
    sh.kubectl.exec(pod, f"--namespace={namespace}", "-it", "--", "/bin/bash", _fg=True)


def install_goss(pod: str, namespace: str, arch: str = "amd64"):
    """Install the latest Goss in a pod."""
    _wait_for_pod(pod=pod, namespace=namespace)
    console.print(f"Installing Goss in {pod}... ", end="")
    kubectl_exec = sh.kubectl.exec.bake(pod, namespace=namespace).bake("-it", "--", _tty_in=True)
    try:
        kubectl_exec.which("goss")
        console.print("already installed.")
    except sh.ErrorReturnCode_1:
        kubectl_exec.apt.update()
        kubectl_exec.apt.install("curl", y=True)
        kubectl_exec.curl(
            "-L",
            f"https://github.com/goss-org/goss/releases/latest/download/goss-linux-{arch}",
            "-o",
            "/usr/bin/goss",
        )
        kubectl_exec.chmod("+rx", "/usr/bin/goss")
        console.print("done.")


def install_goss_checks(pod: str, namespace: str, path: str):
    """Copy the 'goss.yaml' file in the pod."""
    _wait_for_pod(pod=pod, namespace=namespace)
    console.print(f"Copying goss.yaml to {pod}...", end="")
    kubectl_cp = sh.kubectl.cp.bake(namespace=namespace)
    kubectl_cp(path, f"{pod}:/goss.yaml")
    console.print("done.")


def run_goss(pod: str, namespace: str, is_ci: bool):
    """Run `goss validate` in a pod.

    It assumes Goss is already installed and that goss checks are available at
    the '/goss.yaml' path.
    """
    kubectl_flags = "-i" if is_ci else "-it"
    kubectl_exec = sh.kubectl.exec.bake(pod, namespace=namespace).bake(kubectl_flags, "--")
    try:
        kubectl_exec.goss.validate(_fg=True)
    except sh.ErrorReturnCode_1:
        exit(1)  # Exit silently to not shadow the Goss output
