# Distributed under the terms of the Modified BSD License.

"""JupyterLab extension for accessible themes.""" ""

import json
from pathlib import Path

HERE = Path(__file__).parent.resolve()
EXT = HERE / "labextensions"


def _jupyter_labextension_paths():
    return [
        {"src": str(EXT / package["name"].rpartition("-")[-1]), "dest": package["name"]}
        for package in map(json.loads, map(Path.read_text, HERE.rglob("package.json")))
    ]
