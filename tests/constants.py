import services.charmcraft as charmcraft

CHARMCRAFT_STATUS = {
    "blackbox-exporter-k8s": """
[
    {
        "track": "latest",
        "mappings": [
            {
                "base": {
                    "name": "ubuntu",
                    "channel": "20.04",
                    "architecture": "amd64"
                },
                "releases": [
                    {
                        "status": "closed",
                        "channel": "latest/stable",
                        "version": null,
                        "revision": null,
                        "resources": null,
                        "expires_at": null
                    },
                    {
                        "status": "open",
                        "channel": "latest/candidate",
                        "version": "1",
                        "revision": 1,
                        "resources": [
                            {
                                "name": "blackbox-exporter-image",
                                "revision": 1
                            }
                        ],
                        "expires_at": null
                    },
                    {
                        "status": "open",
                        "channel": "latest/beta",
                        "version": "1",
                        "revision": 1,
                        "resources": [
                            {
                                "name": "blackbox-exporter-image",
                                "revision": 1
                            }
                        ],
                        "expires_at": null
                    },
                    {
                        "status": "open",
                        "channel": "latest/edge",
                        "version": "1",
                        "revision": 1,
                        "resources": [
                            {
                                "name": "blackbox-exporter-image",
                                "revision": 1
                            }
                        ],
                        "expires_at": null
                    }
                ]
            },
            {
                "base": {
                    "name": "ubuntu",
                    "channel": "22.04",
                    "architecture": "amd64"
                },
                "releases": [
                    {
                        "status": "open",
                        "channel": "latest/stable",
                        "version": "15",
                        "revision": 15,
                        "resources": [
                            {
                                "name": "blackbox-exporter-image",
                                "revision": 3
                            }
                        ],
                        "expires_at": null
                    },
                    {
                        "status": "open",
                        "channel": "latest/candidate",
                        "version": "17",
                        "revision": 17,
                        "resources": [
                            {
                                "name": "blackbox-exporter-image",
                                "revision": 4
                            }
                        ],
                        "expires_at": null
                    },
                    {
                        "status": "open",
                        "channel": "latest/beta",
                        "version": "17",
                        "revision": 17,
                        "resources": [
                            {
                                "name": "blackbox-exporter-image",
                                "revision": 4
                            }
                        ],
                        "expires_at": null
                    },
                    {
                        "status": "open",
                        "channel": "latest/edge",
                        "version": "17",
                        "revision": 17,
                        "resources": [
                            {
                                "name": "blackbox-exporter-image",
                                "revision": 4
                            }
                        ],
                        "expires_at": null
                    }
                ]
            }
        ]
    }
]
"""
}

RELEASE_STATUS = {
    "blackbox-exporter-k8s": {
        "latest": charmcraft.TrackStatus(
            name="latest",
            bases={
                "20.04/amd64": charmcraft.BaseStatus(
                    version="20.04",
                    arch="amd64",
                    channels={
                        "latest/stable": charmcraft.ChannelStatus(
                            name="latest/stable",
                            status="closed",
                            base_version="20.04",
                            base_arch="amd64",
                            revision=-1,
                            resources=[],
                        ),
                        "latest/candidate": charmcraft.ChannelStatus(
                            name="latest/candidate",
                            status="open",
                            base_version="20.04",
                            base_arch="amd64",
                            revision=1,
                            resources=[
                                charmcraft.CharmResource(
                                    name="blackbox-exporter-image", revision=1
                                )
                            ],
                        ),
                        "latest/beta": charmcraft.ChannelStatus(
                            name="latest/beta",
                            status="open",
                            base_version="20.04",
                            base_arch="amd64",
                            revision=1,
                            resources=[
                                charmcraft.CharmResource(
                                    name="blackbox-exporter-image", revision=1
                                )
                            ],
                        ),
                        "latest/edge": charmcraft.ChannelStatus(
                            name="latest/edge",
                            status="open",
                            base_version="20.04",
                            base_arch="amd64",
                            revision=1,
                            resources=[
                                charmcraft.CharmResource(
                                    name="blackbox-exporter-image", revision=1
                                )
                            ],
                        ),
                    },
                ),
                "22.04/amd64": charmcraft.BaseStatus(
                    version="22.04",
                    arch="amd64",
                    channels={
                        "latest/stable": charmcraft.ChannelStatus(
                            name="latest/stable",
                            status="open",
                            base_version="22.04",
                            base_arch="amd64",
                            revision=15,
                            resources=[
                                charmcraft.CharmResource(
                                    name="blackbox-exporter-image", revision=3
                                )
                            ],
                        ),
                        "latest/candidate": charmcraft.ChannelStatus(
                            name="latest/candidate",
                            status="open",
                            base_version="22.04",
                            base_arch="amd64",
                            revision=17,
                            resources=[
                                charmcraft.CharmResource(
                                    name="blackbox-exporter-image", revision=4
                                )
                            ],
                        ),
                        "latest/beta": charmcraft.ChannelStatus(
                            name="latest/beta",
                            status="open",
                            base_version="22.04",
                            base_arch="amd64",
                            revision=17,
                            resources=[
                                charmcraft.CharmResource(
                                    name="blackbox-exporter-image", revision=4
                                )
                            ],
                        ),
                        "latest/edge": charmcraft.ChannelStatus(
                            name="latest/edge",
                            status="open",
                            base_version="22.04",
                            base_arch="amd64",
                            revision=17,
                            resources=[
                                charmcraft.CharmResource(
                                    name="blackbox-exporter-image", revision=4
                                )
                            ],
                        ),
                    },
                ),
            },
        )
    }
}

CHARM_METADATA_BLACKBOX = {
    "name": "blackbox-exporter-k8s",
    "assumes": ["k8s-api", "juju >= 3.4"],
    "summary": "Kubernetes charm for Blackbox Exporter.\n",
    "description": "Blackbox exporter is a Prometheus exporter that allows to perform blackbox probes using a\nmultitude of protocols, including HTTP(s), DNS, TCP and ICMP.\n",
    "website": "https://charmhub.io/blackbox-exporter-k8s",
    "source": "https://github.com/canonical/blackbox-exporter-k8s-operator",
    "issues": "https://github.com/canonical/blackbox-exporter-k8s-operator/issues",
    "docs": "https://discourse.charmhub.io/t/blackbox-exporter-k8s-docs-index/11728",
    "containers": {"blackbox": {"resource": "blackbox-exporter-image"}},
    "resources": {
        "blackbox-exporter-image": {
            "type": "oci-image",
            "description": "OCI image for Blackbox Exporter",
            "upstream-source": "quay.io/prometheus/blackbox-exporter:v0.24.0",
        }
    },
    "provides": {
        "self-metrics-endpoint": {"interface": "prometheus_scrape"},
        "grafana-dashboard": {"interface": "grafana_dashboard"},
    },
    "requires": {
        "logging": {
            "interface": "loki_push_api",
            "description": "Receives Loki's push api endpoint address to push logs to, and forwards charm's built-in alert rules to Loki.\n",
        },
        "ingress": {"interface": "ingress", "limit": 1},
        "catalogue": {"interface": "catalogue"},
    },
}

CHARM_METADATA_LOKI = {
    "name": "loki-k8s",
    "assumes": ["k8s-api", "juju >= 3.0.3"],
    "summary": "Loki is a set of components that can be composed into a fully featured logging stack.\n",
    "description": "Loki for Kubernetes cluster\n",
    "maintainers": ["Jose Massón <jose.masson@canonical.com>"],
    "website": "https://charmhub.io/loki-k8s",
    "source": "https://github.com/canonical/loki-k8s-operator",
    "issues": "https://github.com/canonical/loki-k8s-operator/issues",
    "docs": "https://discourse.charmhub.io/t/loki-k8s-docs-index/5228",
    "containers": {
        "loki": {
            "resource": "loki-image",
            "mounts": [
                {
                    "storage": "active-index-directory",
                    "location": "/loki/boltdb-shipper-active",
                },
                {"storage": "loki-chunks", "location": "/loki/chunks"},
            ],
        },
        "node-exporter": {
            "resource": "node-exporter-image",
            "mounts": [
                {
                    "storage": "active-index-directory",
                    "location": "/loki/boltdb-shipper-active",
                },
                {"storage": "loki-chunks", "location": "/loki/chunks"},
            ],
        },
    },
    "storage": {
        "active-index-directory": {
            "type": "filesystem",
            "description": "Mount point in which Loki will store index",
        },
        "loki-chunks": {
            "type": "filesystem",
            "description": "Mount point in which Loki will store chunks (objects)",
        },
    },
    "provides": {
        "logging": {"interface": "loki_push_api"},
        "grafana-source": {"interface": "grafana_datasource", "optional": True},
        "metrics-endpoint": {"interface": "prometheus_scrape"},
        "grafana-dashboard": {"interface": "grafana_dashboard"},
    },
    "requires": {
        "alertmanager": {"interface": "alertmanager_dispatch"},
        "ingress": {"interface": "ingress_per_unit", "limit": 1},
        "certificates": {
            "interface": "tls-certificates",
            "limit": 1,
            "description": "Certificate and key files for the loki server.\n",
        },
        "catalogue": {"interface": "catalogue"},
        "tracing": {"interface": "tracing", "limit": 1},
    },
    "peers": {"replicas": {"interface": "loki_replica"}},
    "resources": {
        "loki-image": {
            "type": "oci-image",
            "description": "Loki OCI image",
            "upstream-source": "docker.io/ubuntu/loki:2-22.04",
        },
        "node-exporter-image": {
            "type": "oci-image",
            "description": "Node-exporter OCI image",
            "upstream-source": "docker.io/prom/node-exporter:v1.7.0",
        },
    },
}

READMES = {
    "canonical/blackbox-exporter-k8s-operator": "# Blackbox Exporter Operator (k8s)\n[![Charmhub Badge](https://charmhub.io/blackbox-exporter-k8s/badge.svg)](https://charmhub.io/blackbox-exporter-k8s)\n[![Release](https://github.com/canonical/blackbox-exporter-k8s-operator/actions/workflows/release.yaml/badge.svg)](https://github.com/canonical/blackbox-exporter-k8s-operator/actions/workflows/release.yaml)\n[![Discourse Status](https://img.shields.io/discourse/status?server=https%3A%2F%2Fdiscourse.charmhub.io&style=flat&label=CharmHub%20Discourse)](https://discourse.charmhub.io)\n\n[Charmed Blackbox Exporter (blackbox-exporter-k8s)][Blackbox Exporter operator] is a charm for\n[Blackbox Exporter].\n\nThe charm imposes configurable resource limits on the workload, can be readily\nintegrated with [prometheus][Prometheus operator], [grafana][Grafana operator]\nand [loki][Loki operator], and it comes with built-in alert rules and dashboards for\nself-monitoring.\n\n[Blackbox Exporter]: https://github.com/prometheus/blackbox_exporter\n[Grafana operator]: https://charmhub.io/grafana-k8s\n[Loki operator]: https://charmhub.io/loki-k8s\n[Prometheus operator]: https://charmhub.io/prometheus-k8s\n[Blackbox Exporter operator]: https://charmhub.io/blackbox-exporter-k8s\n\n\n## Getting started\n\n### Basic deployment\n\nOnce you have a controller and model ready, you can deploy the blackbox exporter\nusing the Juju CLI:\n\n```shell\njuju deploy --channel=beta blackbox-exporter-k8s\n```\n\nThe available [channels](https://snapcraft.io/docs/channels) are listed at the top\nof [the page](https://charmhub.io/blackbox-exporter-k8s) and can also be retrieved with\nCharmcraft CLI:\n\n```shell\n$ charmcraft status blackbox-exporter-k8s\n\nTrack    Base                  Channel    Version    Revision    Resources\nlatest   ubuntu 22.04 (amd64)  stable     -          -           -\n                               candidate  -          -           -\n                               beta       1          1           blackbox-exporter-image (r1)\n                               edge       1          1           blackbox-exporter-image (r1)\n```\n\nOnce the Charmed Operator is deployed, the status can be checked by running:\n\n```shell\njuju status --relations --storage --color\n```\n\n\n### Configuration\n\nIn order to configure the Blackbox Exporter, a [configuration file](https://github.com/prometheus/blackbox_exporter/blob/master/CONFIGURATION.md)\nshould be provided using the\n[`config_file`](https://charmhub.io/blackbox-exporter-k8s/configure#config_file) option:\n\n```shell\njuju config blackbox-exporter-k8s \\\n  config_file='@path/to/blackbox.yml'\n```\n\nTo verify Blackbox Exporter is using the expected configuration you can use the\n[`show-config`](https://charmhub.io/blackbox-exporter-k8s/actions#show-config) action:\n\n```shell\njuju run-action blackbox-exporter-k8s/0 show-config --wait\n```\n\nTo configure the actual probes, there first needs to be a Prometheus relation:\n\n```shell\njuju relate blackbox-exporter-k8s prometheus\n```\n\nThen, the probes configuration should be written to a file (following the \n[Blackbox Exporter docs](https://github.com/prometheus/blackbox_exporter#prometheus-configuration)\n) and passed via `juju config`:\n\n```shell\njuju config blackbox-exporter-k8s \\\n  probes_file='@path/to/probes.yml'\n```\n\nNote that the `relabel_configs` of each scrape job doesn't need to be specified, and will be \noverridden by the charm with the needed labels and the correct Blackbox Exporter url.\n\n## OCI Images\nThis charm is published on Charmhub with blackbox exporter images from\nthe official [quay.io/prometheus/blackbox-exporter].\n\n[quay.io/prometheus/blackbox-exporter]: https://quay.io/repository/prometheus/blackbox-exporter?tab=tags\n\n## Additional Information\n- [Blackbox Exporter README](https://github.com/prometheus/blackbox-exporter)\n",
    "canonical/alertmanager-rock": "# alertmanager-rock\n\n[![Open a PR to OCI Factory](https://github.com/canonical/alertmanager-rock/actions/workflows/rock-release-oci-factory.yaml/badge.svg)](https://github.com/canonical/alertmanager-rock/actions/workflows/rock-release-oci-factory.yaml)\n[![Publish to GHCR:dev](https://github.com/canonical/alertmanager-rock/actions/workflows/rock-release-dev.yaml/badge.svg)](https://github.com/canonical/alertmanager-rock/actions/workflows/rock-release-dev.yaml)\n[![Update rock](https://github.com/canonical/alertmanager-rock/actions/workflows/rock-update.yaml/badge.svg)](https://github.com/canonical/alertmanager-rock/actions/workflows/rock-update.yaml)\n\n[Rocks](https://canonical-rockcraft.readthedocs-hosted.com/en/latest/) for [Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/).  \nThis repository holds all the necessary files to build rocks for the upstream versions we support. The Alertmanager rock is used by the [alertmanager-k8s-operator](https://github.com/canonical/alertmanager-k8s-operator) charm.\n\nThe rocks on this repository are built with [OCI Factory](https://github.com/canonical/oci-factory/), which also takes care of periodically rebuilding the images.\n\nAutomation takes care of:\n* validating PRs, by simply trying to build the rock;\n* pulling upstream releases, creating a PR with the necessary files to be manually reviewed;\n* releasing to GHCR at [ghcr.io/canonical/alertmanager:dev](https://ghcr.io/canonical/alertmanager:dev), when merging to main, for development purposes.\n\n",
}

CHARM_LIBRARIES = {
    "lib/charms/traefik_k8s/v2/ingress.py": """import ipaddress\nimport json\nimport logging\nimport socket\nimport typing\nfrom dataclasses import dataclass\nfrom functools import partial\nfrom typing import Any, Callable, Dict, List, MutableMapping, Optional, Sequence, Tuple, Union\n\nimport pydantic\nfrom ops.charm import CharmBase, RelationBrokenEvent, RelationEvent\nfrom ops.framework import EventSource, Object, ObjectEvents, StoredState\nfrom ops.model import ModelError, Relation, Unit\nfrom pydantic import AnyHttpUrl, BaseModel, Field\n\n# The unique Charmhub library identifier, never change it\nLIBID = "e6de2a5cd5b34422a204668f3b8f90d2"\n\n# Increment this major API version when introducing breaking changes\nLIBAPI = 2\n\n# Increment this PATCH version before using `charmcraft publish-lib` or reset\n# to 0 if you are raising the major API version\nLIBPATCH = 14\n\nPYDEPS = ["pydantic"]\n\n""",
    "lib/charms/prometheus_k8s/v0/prometheus_scrape.py": """import copy\nimport hashlib\nimport ipaddress\nimport json\nimport logging\nimport os\nimport platform\nimport re\nimport socket\nimport subprocess\nimport tempfile\nfrom collections import defaultdict\nfrom pathlib import Path\nfrom typing import Any, Callable, Dict, List, Optional, Tuple, Union\nfrom urllib.parse import urlparse\n\nimport yaml\nfrom cosl import JujuTopology\nfrom cosl.rules import AlertRules\nfrom ops.charm import CharmBase, RelationRole\nfrom ops.framework import (\n    BoundEvent,\n    EventBase,\n    EventSource,\n    Object,\n    ObjectEvents,\n    StoredDict,\n    StoredList,\n    StoredState,\n)\nfrom ops.model import Relation\n\n# The unique Charmhub library identifier, never change it\nLIBID = "bc84295fef5f4049878f07b131968ee2"\n\n# Increment this major API version when introducing breaking changes\nLIBAPI = 0\n\n# Increment this PATCH version before using `charmcraft publish-lib` or reset\n# to 0 if you are raising the major API version\nLIBPATCH = 47\n\nPYDEPS = ["cosl"]""",
    "lib/charms/wrong/v0/library.py": """This is a fake library without versioning.""",
}

CHARMCRAFT_LIST_LIB = {
    "catalogue-k8s": """[{"charm_name": "catalogue-k8s", "library_name": "catalogue", "library_id": "fa28b361293b46668bcd1f209ada6983", "api": 1, "patch": 0, "content_hash": "873f348ecc88ad7cfaf1a0d0791f36ceffc7725e1d92320ffc552fdb58261fb7"}]""",
    "grafana-k8s": """[{"charm_name": "grafana-k8s", "library_name": "grafana_auth", "library_id": "e9e05109343345d4bcea3bce6eacf8ed", "api": 0, "patch": 4, "content_hash": "0a66059a004daee472042a18cf92cf6c244b407066045325c420b8d371127530"}, {"charm_name": "grafana-k8s", "library_name": "grafana_dashboard", "library_id": "c49eb9c7dfef40c7b6235ebd67010a3f", "api": 0, "patch": 36, "content_hash": "24793360183818ed4d13debc5433b3330989d2f394cb39ac3c713ec5476a57b5"}, {"charm_name": "grafana-k8s", "library_name": "grafana_source", "library_id": "974705adb86f40228298156e34b460dc", "api": 0, "patch": 21, "content_hash": "7870a0a7158107b55a6e05395efc246443c9f7a6d95f43f9bf8d22c2ca19d249"}]""",
    "prometheus-k8s": """[{"charm_name": "prometheus-k8s", "library_name": "prometheus_remote_write", "library_id": "f783823fa75f4b7880eb70f2077ec259", "api": 1, "patch": 4, "content_hash": "1837b04372b41e35a0a77c0ea814af76a8db1a29c4dc557efbfa8b8a3037f71d"}, {"charm_name": "prometheus-k8s", "library_name": "prometheus_scrape", "library_id": "bc84295fef5f4049878f07b131968ee2", "api": 0, "patch": 47, "content_hash": "d174e6ebab3cc78a4160ef826c107314a0f503de2dd844491aadc2d964d8beb9"}]""",
}

CHARMCRAFT_LIST_LIB_EXPECTED = {
    "catalogue-k8s": [
        charmcraft.CharmLibrary(
            charm_name="catalogue-k8s", library_name="catalogue", api=0, patch=10
        )
    ],
    "grafana-k8s": [
        charmcraft.CharmLibrary(
            charm_name="grafana-k8s", library_name="grafana_auth", api=0, patch=4
        ),
        charmcraft.CharmLibrary(
            charm_name="grafana-k8s",
            library_name="grafana_source",
            api=0,
            patch=21,
        ),
        charmcraft.CharmLibrary(
            charm_name="grafana-k8s",
            library_name="grafana_dashboard",
            api=0,
            patch=36,
        ),
    ],
    "prometheus-k8s": [
        charmcraft.CharmLibrary(
            charm_name="prometheus-k8s",
            library_name="prometheus_scrape",
            api=0,
            patch=47,
        ),
        charmcraft.CharmLibrary(
            charm_name="prometheus-k8s", library_name="prometheus_remote_write", api=1, patch=4
        ),
    ],
}

ROCKCRAFT_OCI_RELEASES = {
    "prometheus": """{"2.45.0-22.04": {"end-of-life": "2024-10-04T00:00:00Z", "stable": {"target": "106"}, "candidate": {"target": "2.45.0-22.04_stable"}, "beta": {"target": "2.45.0-22.04_candidate"}, "edge": {"target": "2.45.0-22.04_beta"}}, "2.45-22.04": {"end-of-life": "2024-10-04T00:00:00Z", "stable": {"target": "106"}, "candidate": {"target": "2.45-22.04_stable"}, "beta": {"target": "2.45-22.04_candidate"}, "edge": {"target": "2.45-22.04_beta"}}}"""
}
