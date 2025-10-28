import json
import os
import shutil

import pandas as pd
import semver
from github import Github

SRC_REPO = "cgohlke/geospatial-wheels"


def get_packages() -> dict[str, list]:
    g = Github()
    repo = g.get_repo(SRC_REPO)
    releases = repo.get_releases()

    wheels = list()

    for release in releases:
        tag = release.tag_name
        assets = release.assets
        for asset in assets:
            whl_url = asset.browser_download_url

            binary_name = asset.name[:-4]  # remove ".whl"
            binary_name_elms = binary_name.split("-")
            distribution, version, python_tag, abi_tag, platform = binary_name_elms
            try:
                version = semver.Version.parse(version)
            except ValueError:
                v = version.split(".")
                version = semver.Version(
                    major=int(v[0]),
                    minor=int(v[1]),
                    patch=int(v[2]),
                    prerelease=None,
                    build=v[3],
                )

            wheels.append(
                {
                    "distribution": distribution,
                    "version_major": version.major,
                    "version_minor": version.minor,
                    "version_patch": version.patch,
                    "version_build": version.build,
                    "python_tag": python_tag,
                    "abi_tag": abi_tag,
                    "platform": platform,
                    "whl_url": whl_url,
                }
            )

    assets = pd.DataFrame().from_records(wheels).convert_dtypes()
    # assets.to_csv("assets.csv")
    assets = (
        assets.sort_values(
            by=[
                "version_major",
                "version_minor",
                "version_patch",
                "version_build",
                "python_tag",
                "abi_tag",
                "platform",
            ],
            ascending=False,
        )
        .drop_duplicates(
            subset=[
                "version_major",
                "version_minor",
                "version_patch",
                "version_build",
                "python_tag",
                "abi_tag",
                "platform",
                "distribution",
            ],
            keep="first",
        )
        .reset_index(drop=True)
    )
    assets = assets.to_dict("records")

    package_names = {pkg["distribution"].lower() for pkg in assets}
    package_names = sorted(list(package_names))

    packages = dict()
    for package in package_names:
        if package not in packages:
            packages[package] = list()
        for asset in assets:
            if asset["distribution"].lower() == package.lower():
                packages[package].append(asset["whl_url"])

    return packages


def build_repo(packages: dict[str, list], pth="./simple"):
    print("Deleting", pth)
    if os.path.exists(pth):
        shutil.rmtree(pth)
    os.mkdir(pth)

    with open(os.path.join(pth, "index.json"), "w") as f:
        print(os.path.join(pth, "index.json"))
        json.dump(packages, f, indent=4)

    index_links = list()
    for name in packages.keys():
        index_links.append(f'<a href="{name}/index.html">{name}</a>')

        os.mkdir(os.path.join(pth, name))
        print(os.path.join(pth, name))

        with open(os.path.join(pth, name, "index.html"), "w") as f:
            print(os.path.join(pth, name, "index.html"))
            f.write(
                f"""
                <!DOCTYPE html>
                    <html>
                      <body>
                        <h1>{name}</h1>
                        <hr>
                """
            )
            for asset in packages[name]:
                f.write(f'<a href="{asset}">{asset.split("/")[-1].lower()}</a><br/>')

            f.write(
                f"""
                  <hr>
                  <a href="../index.html")">&larr; Back</a>
                  </body>
                </html>
                """
            )

    with open(os.path.join(pth, "index.html"), "w") as f:
        print(os.path.join(pth, "index.html"))
        f.write(
            f"""
            <!DOCTYPE html>
                <html>
                  <body>
            """
        )
        f.write(
            """
            <h1>Simple Index for <a href="https://github.com/cgohlke/geospatial-wheels">cgohlke/geospatial-wheels</a></h1>
            <hr>
            """
        )
        f.write("<br/>".join(index_links))
        f.write(
            """
              <hr>
              Source: <a href="https://github.com/corbel-spatial/geospatial-wheels-index">geospatial-wheels-index</a>
              </body>
            </html>
            """
        )


if __name__ == "__main__":
    packages = get_packages()
    build_repo(packages)
    print("Done!")
