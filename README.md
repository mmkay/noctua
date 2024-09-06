# Noctua

Noctua is a helper tool to simplify CI for Canonical repositories! ✨

## Installation

You can install Noctua with pip:

```bash
pip install git+https://github.com/lucabello/noctua
```

## Usage

Noctua has a top-level `--verbose` flag to show the bash commands it's running under the hood.

```bash
Usage: noctua [OPTIONS] COMMAND [ARGS]...

 Enable INFO logging.

╭─ Options ───────────────────────────────────────────────────────────────────╮
│ --verbose               --no-verbose      [default: no-verbose]             │
│ --install-completion                      Install completion for the        │
│                                           current shell.                    │
│ --show-completion                         Show completion for the current   │
│                                           shell, to copy it or customize    │
│                                           the installation.                 │
│ --help                                    Show this message and exit.       │
╰─────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────╮
│ charm                                                                       │
│ report                                                                      │
│ rock                                                                        │
╰─────────────────────────────────────────────────────────────────────────────╯
```

### Commands

Charm commands (`noctua charm`):
```
╭─ Commands ──────────────────────────────────────────────────────────────────╮
│ libraries       (+) Commands related to charm libraries.                    │
│ pack            Pack a charm from any 'charmcraft.yaml' file.               │
│ promote         Promote a charm revision from a channel to the next risk    │
│                 channel.                                                    │
│ promote-train   Promote all the revisions in a track to their next risk     │
│                 channel.                                                    │
│ release         Upload and release a local '.charm' file to Charmhub.       │
╰─────────────────────────────────────────────────────────────────────────────╯
```

Charm libraries commands (`noctua charm libraries`):
```
╭─ Commands ──────────────────────────────────────────────────────────────────╮
│ check     Check if charm libraries are updated to the latest version.       │
│ print     Print the charm libraries used by the charm, along with their     │
│           version.                                                          │
│ publish   Publish all the charm libraries that belong to the charm.         │
╰─────────────────────────────────────────────────────────────────────────────╯
```

Rock commands (`noctua rock`):
```
╭─ Commands ──────────────────────────────────────────────────────────────────╮
│ manifest   Generate the 'image.yaml' manifest for OCI Factory.              │
│ status     Print the diff between local tags and the ones currently in OCI  │
│            Factory.                                                         │
╰─────────────────────────────────────────────────────────────────────────────╯
```

Report commands (`noctua report`):
```
╭─ Commands ──────────────────────────────────────────────────────────────────╮
│ ci   Print a table with CI status for the specified team under the          │
│      Canonical org.                                                         │
╰─────────────────────────────────────────────────────────────────────────────╯
```
