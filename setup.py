# Copyright (c) Jupyter Accessibility Team.
# Distributed under the terms of the Modified BSD License.

import json
import os
import setuptools
from pathlib import Path


def get_long_description():
    with open(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'README.md'
    ), encoding='utf8') as fp:
        return fp.read()

HERE = Path(__file__).parent
MOD = "jupyterlab_accessible_themes"
VARIANTS = ["pitayasmoothie", "githublight"]
EXTS = [HERE / MOD / f"labextensions/{v}" for v in VARIANTS]
MANIFESTS = [ext / "package.json" for ext in EXTS]
PACKAGES = [json.loads(pkg_json.read_text(encoding="utf-8")) for pkg_json in MANIFESTS]

SHARE = "share/jupyter/labextensions"
EXT_FILES = {f"""{SHARE}/{pkg["name"]}""": ["install.json"] for pkg in PACKAGES}

for ext, pkg in zip(EXTS, PACKAGES):
    for ext_path in [ext] + [d for d in ext.rglob("*") if d.is_dir()]:
        target = f"""{SHARE}/{pkg["name"]}"""
        if ext_path != ext:
            target = f"""{target}/{ext_path.relative_to(ext)}"""
        EXT_FILES[target] = [
            str(p.relative_to(HERE).as_posix())
            for p in ext_path.glob("*")
            if not p.is_dir()
        ]

DATA_FILES = sorted([(k, v) for k, v in EXT_FILES.items()])

pkg_name = HERE / "package.json"
PKG_INFO = json.loads(pkg_name.read_text(encoding="utf-8"))

SETUP_ARGS = dict(
    name=PKG_INFO["name"],
    description=PKG_INFO["description"],
    version=PKG_INFO["version"],
    url=PKG_INFO["homepage"],
    license=PKG_INFO["license"],
    packages=["jupyterlab_accessible_themes"],
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    data_files=DATA_FILES,
    project_urls={
        "Bug Tracker": PKG_INFO["bugs"]["url"],
        "Source Code": PKG_INFO["repository"]["url"],
    },
    author="quansight-labs",
    author_email="contact@quansight.com",
)


if __name__ == "__main__":
    setuptools.setup(**SETUP_ARGS)
