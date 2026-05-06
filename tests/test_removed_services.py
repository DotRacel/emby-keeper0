import pytest

from embykeeper.schema import Config
from embykeeper.telegram.dynamic import get_names


@pytest.mark.parametrize("feature", ["monitor", "messager", "registrar"])
def test_removed_top_level_configs_are_rejected(feature):
    with pytest.raises(ValueError):
        Config(**{feature: {}})


def test_removed_telegram_account_flags_are_rejected():
    with pytest.raises(ValueError):
        Config(telegram={"account": [{"phone": "+8613800000000", "monitor": True}]})


@pytest.mark.parametrize("service", ["monitor", "messager", "registrar"])
def test_removed_dynamic_service_types_are_rejected(service):
    with pytest.raises(ValueError):
        get_names(service)


def test_removed_checkiners_are_not_discoverable():
    removed = {
        "charon",
        "epub_group_chat",
        "future",
        "pornfans_game_group",
        "pornfans_group",
        "ruji",
        "rujing",
        "temby",
        "temby_beta",
        "xigua",
    }

    assert not removed.intersection(get_names("checkiner"))
