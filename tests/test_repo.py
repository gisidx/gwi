import json
import subprocess

import pytest


@pytest.fixture
def packages() -> dict:
    with open("./simple/index.json", "r") as f:
        packages = json.load(f)
    return packages


def test_repo(packages, pth="./simple"):
    subprocess.run(
        ["uv", "pip", "install", "--default-index", "./simple", "--no-deps", "gdal"]
    )

    packages = list(packages.keys())

    print("\nInstalling packages:")
    print(packages)
    print("Index:", pth)

    subprocess.run(
        [
            "uv",
            "pip",
            "install",
            "--default-index",
            "./simple",
            "--no-deps",
        ]
        + packages
    )

    subprocess.run(["uv", "pip", "uninstall"] + packages)
