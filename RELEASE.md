# Making a new release of `jupyterlab_accessible_themes`

The extension can be published to `PyPI` and `npm` manually or using the [Jupyter Releaser](https://github.com/jupyter-server/jupyter_releaser).

- [Making a new release of `jupyterlab_accessible_themes`](#making-a-new-release-of-jupyterlab_accessible_themes)
  - [🚧 Manual release](#-manual-release)
    - [📦 Python package](#-python-package)
    - [📦 NPM package](#-npm-package)
  - [👷🏽‍♀️ Automated releases with the Jupyter Releaser](#️-automated-releases-with-the-jupyter-releaser)
  - [📰 Publishing to `conda-forge`](#-publishing-to-conda-forge)

## 🚧 Manual release

### 📦 Python package

This extension can be distributed as a Python package.
The [`pyproject.toml`](./pyproject.toml) file contains all the instructions needed to wrap the extension in a
Python package.

0. Before generating a package, we first need to install `build`.

   ```bash
   pip install build twine
   ```

1. To create a Python source package (`.tar.gz`) and the binary package (`.whl`) in the `dist/` directory, do:

   ```bash
   python -m build
   ```

> **Warning** > `python setup.py sdist bdist_wheel` is deprecated and will not work for this package.

2. Then to upload the package to PyPI, do:

   ```bash
   twine upload dist/*
   ```

### 📦 NPM package

1. To publish the frontend part of the extension as a NPM package, do:

   ```bash
   npm login
   npm publish --access public
   ```

## 👷🏽‍♀️ Automated releases with the Jupyter Releaser

The extension repository should already be compatible with the Jupyter Releaser.

Check out the [`jupyter_releaser` workflow documentation](https://github.com/jupyter-server/jupyter_releaser#typical-workflow) for more information.

Here is a summary of the steps to cut a new release:

1. Fork the [`jupyter-releaser` repo](https://github.com/jupyter-server/jupyter_releaser)
2. Add the following secrets as repository secrets in GitHub `ADMIN_GITHUB_TOKEN`, `PYPI_TOKEN` and `NPM_TOKEN`
3. Go to the Actions panel
4. Run the "Draft Changelog" workflow
5. Merge the Changelog PR
6. Run the "Draft Release" workflow
7. Run the "Publish Release" workflow

## 📰 Publishing to `conda-forge`

If the package is not on `conda-forge` yet, check the [`conda-forge`documentation on how to contribute new packages](https://conda-forge.org/docs/maintainer/adding_pkgs.html).

Otherwise, a bot should pick up the new version publish to PyPI, and open a new PR on the feedstock repository automatically.
