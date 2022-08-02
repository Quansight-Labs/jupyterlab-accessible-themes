# Distributed under the terms of the Modified BSD License.

import json
from pathlib import Path

from ._version import __version__

HERE = Path(__file__).parent.resolve()
EXT = HERE / "labextensions"


def _jupyter_labextension_paths():
    return [
        dict(src=str(EXT / package["name"].rpartition("-")[-1]), dest=package["name"])
        for package in map(json.loads, map(Path.read_text, HERE.rglob("package.json")))
    ]
