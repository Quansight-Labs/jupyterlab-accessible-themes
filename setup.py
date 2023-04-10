# Copyright (c) Jupyter Accessibility Team.
# Distributed under the terms of the Modified BSD License.

import json
import re
from pathlib import Path

import setuptools

HERE = Path(__file__).parent
MOD = "jupyterlab_accessible_themes"
VARIANTS = ["pitayasmoothie"]
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

SETUP_ARGS = dict(
    name=PACKAGES[0]["jupyterlab"]["discovery"]["server"]["base"]["name"],
    description=PACKAGES[0]["description"],
    version=PACKAGES[0]["version"],
    url=PACKAGES[0]["homepage"],
    license=PACKAGES[0]["license"],
    packages=["jupyterlab_accessible_themes"],
    data_files=DATA_FILES,
    project_urls={
        "Bug Tracker": PACKAGES[0]["bugs"]["url"],
        "Source Code": PACKAGES[0]["repository"]["url"],
    },
    author="quansight-labs",
    author_email="contact@quansight.com",
)


if __name__ == "__main__":
    setuptools.setup(**SETUP_ARGS)
