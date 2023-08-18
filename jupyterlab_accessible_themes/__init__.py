# Distributed under the terms of the Modified BSD License.

"""JupyterLab extension for accessible themes."""

import json
from pathlib import Path

HERE = Path(__file__).parent.resolve()
extension_paths = HERE / "labextensions"

try:
    from ._version import __version__
except ImportError:
    # Fallback when using the package in dev mode without installing
    # in editable mode with pip. It is highly recommended to install
    # the package from a stable release or in editable mode:
    # https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs
    import warnings

    warnings.warn(
        "Importing 'jupyterlab_accessible_themes' outside a proper installation."
    )
    __version__ = "dev"


def _jupyter_labextension_paths():
    """Generate extension paths from packages in the extension directory.

    Returns:
        _type_: _description_
    """
    # We use glob to check the extension directories for package.json files - each package.json will indicate
    # a subdirectory of the extension directory that should be included as a labextension (i.e. a JupyterLab theme).
    extensions = []
    for theme in map(
        json.loads, map(Path.read_text, extension_paths.rglob("package.json"))
    ):
        extensions.append(
            {
                "src": str(extension_paths / theme["name"].rpartition("-")[-1]),
                "dest": theme["name"],
            }
        )

    return extensions
