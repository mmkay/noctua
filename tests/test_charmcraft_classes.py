from unittest.mock import MagicMock, mock_open, patch

import pytest

import services.charmcraft as charmcraft
import tests.constants as constants


@pytest.mark.parametrize(
    "charm_library, expected",
    [
        (
            charmcraft.CharmLibrary(
                charm_name="prometheus-k8s", library_name="prometheus_scrape", api=0, patch=50
            ),
            "charms.prometheus_k8s.v0.prometheus_scrape",
        ),
        (
            charmcraft.CharmLibrary(
                charm_name="traefik-k8s", library_name="ingress", api=2, patch=0
            ),
            "charms.traefik_k8s.v2.ingress",
        ),
    ],
)
def test_charm_library_full_name(charm_library, expected):
    assert charm_library.full_name == expected


@pytest.mark.parametrize(
    "filename, expected",
    [
        ("lib/charms/traefik_k8s/v2/ingress.py", "2.14"),
        ("lib/charms/prometheus_k8s/v0/prometheus_scrape.py", "0.47"),
        ("lib/charms/wrong/v0/library.py", None),  # has content in constants.py
    ],
)
def test_charm_library_from_file(filename, expected):
    with patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=constants.CHARM_LIBRARIES[filename],
    ):
        if expected is None:
            with pytest.raises(charmcraft.InputError):
                charmcraft.CharmLibrary.from_file(filename)
            return
        library = charmcraft.CharmLibrary.from_file(filename)
        version = f"{library.api}.{library.patch}"
        assert version == expected


@pytest.mark.parametrize(
    "filename",
    [
        "some/wrong/path/to/file.py",
        "lib/charms/some/wrong/path.py",
    ],
)
def test_charm_library_from_file_failures(
    filename,
):
    with pytest.raises(charmcraft.InputError):
        charmcraft.CharmLibrary.from_file(filename)
    return


@pytest.mark.parametrize("charm_name", ["catalogue-k8s", "grafana-k8s", "prometheus-k8s"])
def test_charm_library_from_charmhub(charm_name):
    with patch("sh.charmcraft", MagicMock(return_value=constants.CHARMCRAFT_LIST_LIB[charm_name])):
        libraries = charmcraft.CharmLibrary.from_charmhub(charm_name)
        for full_name, library in libraries.items():
            for expected in constants.CHARMCRAFT_LIST_LIB_EXPECTED[charm_name]:
                if full_name != expected.full_name:
                    continue
                assert library.full_name == full_name
                assert library.charm_name == expected.charm_name
                assert library.api == expected.api
                assert library.patch == expected.patch
                assert library.library_id is not None
                assert library.content_hash is not None


@pytest.mark.parametrize(
    "charm_name, library_name",
    [
        ("catalogue-k8s", "catalogue"),
        ("grafana-k8s", "grafana_source"),
        ("prometheus-k8s", "prometheus_scrape"),
    ],
)
def test_charm_library_from_charmhub_with_name(charm_name, library_name):
    with patch("sh.charmcraft", MagicMock(return_value=constants.CHARMCRAFT_LIST_LIB[charm_name])):
        library = charmcraft.CharmLibrary.from_charmhub_with_name(charm_name, library_name)
        for expected in constants.CHARMCRAFT_LIST_LIB_EXPECTED[charm_name]:
            if library.full_name != expected.full_name:
                continue
            assert library.charm_name == expected.charm_name
            assert library.api == expected.api
            assert library.patch == expected.patch
            assert library.library_id is not None
            assert library.content_hash is not None


@pytest.mark.parametrize(
    "charm_name, library_name",
    [
        ("catalogue-k8s", "fake-library"),
        ("grafana-k8s", "this-isnt-real"),
        ("prometheus-k8s", "wrong-wrong-wrong"),
    ],
)
def test_charm_library_from_charmhub_with_name_failures(charm_name, library_name):
    with patch("sh.charmcraft", MagicMock(return_value=constants.CHARMCRAFT_LIST_LIB[charm_name])):
        with pytest.raises(charmcraft.CharmhubError):
            charmcraft.CharmLibrary.from_charmhub_with_name(charm_name, library_name)


@pytest.mark.parametrize(
    "channel, expected_track, expected_risk, expected_next_risk",
    [
        ("latest/edge", "latest", "edge", "beta"),
        ("1.0/beta", "1.0", "beta", "candidate"),
        ("2024/candidate", "2024", "candidate", "stable"),
        ("3.x/stable", "3.x", "stable", "stable"),
        ("latest/wrong", None, None, None),
        ("/notrack", None, None, None),
        ("nochannel/", None, None, None),
        ("onlystring", None, None, None),
        ("too/many/slashes", None, None, None),
        ("too/many/slashes/here", None, None, None),
    ],
)
def test_charm_channel(channel, expected_track, expected_risk, expected_next_risk):
    charm_channel = charmcraft.CharmChannel(name=channel)
    if expected_track is not None and expected_risk is not None:
        assert charm_channel.track == expected_track
        assert charm_channel.risk == expected_risk
        if expected_next_risk is not None:
            assert charm_channel.next_risk_channel.track == expected_track
            assert charm_channel.next_risk_channel.risk == expected_next_risk
        else:
            with pytest.raises(charmcraft.InputError):
                charm_channel.next_risk_channel
    else:
        with pytest.raises(charmcraft.InputError):
            charm_channel.track
        with pytest.raises(charmcraft.InputError):
            charm_channel.risk


@pytest.mark.parametrize(
    "version, arch, expected",
    [("20.04", "amd64", "20.04/amd64"), ("22.04", "arm64", "22.04/arm64")],
)
def test_base_status_name(version, arch, expected):
    base_status = charmcraft.BaseStatus(version=version, arch=arch, channels={})
    assert base_status.name == expected
