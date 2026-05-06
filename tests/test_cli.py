import os
from pathlib import Path
from typer.testing import CliRunner

import pytest

import embykeeper
from embykeeper.cli import app

runner = CliRunner()


@pytest.fixture()
def in_temp_dir(tmp_path: Path):
    current = os.getcwd()
    os.chdir(tmp_path)
    yield tmp_path
    os.chdir(current)


def test_version():
    result = runner.invoke(app, ["--version"])
    assert embykeeper.__version__ in result.stdout
    assert result.exit_code == 0


def test_create_config(in_temp_dir: Path):
    result = runner.invoke(app, ["--example-config"])
    assert "这是一个配置文件范例" in result.stdout
    assert result.exit_code == 0


def test_removed_feature_flags_are_not_exposed():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "--monitor" not in result.stdout
    assert "--messager" not in result.stdout
    assert "--registrar" not in result.stdout
    assert "--registrar-bot" not in result.stdout


def test_example_config_excludes_removed_features(in_temp_dir: Path):
    result = runner.invoke(app, ["--example-config"])
    assert result.exit_code == 0
    assert "monitor" not in result.stdout
    assert "messager" not in result.stdout
    assert "registrar" not in result.stdout
    assert "embykeeper_auth_bot" not in result.stdout
    assert "cf_challenge" not in result.stdout
