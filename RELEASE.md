# Making a new release of `jupyterlab_accessible_themes`

- [Making a new release of `jupyterlab_accessible_themes`](#making-a-new-release-of-jupyterlab_accessible_themes)
  - [Manual release 🛠](#manual-release-)
    - [Python package 📦](#python-package-)
      - [Pre-requisites](#pre-requisites)
      - [Making a new release](#making-a-new-release)
    - [NPM package 📦](#npm-package-)
  - [Automated releases with the Jupyter Releaser 🏗](#automated-releases-with-the-jupyter-releaser-)
  - [Publishing to `conda-forge`](#publishing-to-conda-forge)

## Manual release 🛠

### Python package 📦

This extension can be distributed as Python packages.
The Python packaging instructions are specified in the [`pyproject.toml`](./pyproject.toml) file in the root of repository.

#### Pre-requisites

We use [hatch](https://hatch.pypa.io/latest/) with the [hatch-jupyter-builder](https://github.com/jupyterlab/hatch-jupyter-builder) to handle the packaging and distribution of this extension.

You can install the dependencies with:

```bash
pip install build twine hatch gitchangelog
```

#### Making a new release

1. Make sure you have the latest version of the `main` branch:

   ```bash
   git checkout main
   git pull
   ```

1. Bump the version using `hatch`. By default, this will create a tag.
   See the docs on [hatch-nodejs-version](https://github.com/agoose77/hatch-nodejs-version#semver) for details.

   ```bash
   hatch version <new-version>
   # example
   hatch version 1.0.0
   ```

1. Ensure that the individual themes are aligned with the package version. The version of the themes is specified in the `package.json` file in the root of the repository. Update these as needed.

1. Cleanup any development files before building the package:

```bash
  jlpm clean:all
```

1. Clean your local repository:

   ```bash
   git clean -xdfi
   ```

1. Push the changes and tag to GitHub:

   ```bash
   git push
   git push --tags
   ```

1. To create a Python source package (`.tar.gz`) and the binary package (`.whl`) in the `dist/` directory, do:

```bash
python -m build
```

> `python setup.py sdist bdist_wheel` is deprecated and will not work for this package.

1. Ensure artifacts were built correctly:

   ```bash
   twine check dist/\*
   ```

1. To upload the package to PyPi:

```bash
twine upload dist/*
```

### NPM package 📦

1. To publish the frontend part of the extension as a NPM package, do:

   ```bash
   npm login
   npm publish --access public
   ```

## Automated releases with the Jupyter Releaser 🏗

The extension repository should already be compatible with the Jupyter Releaser.

Check out the [workflow documentation](https://jupyter-releaser.readthedocs.io/en/latest/get_started/making_release_from_repo.html) for more information.

> **Note**
> These steps should only be done once to set up the action workflow.

1. Add tokens to the [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) in the repository:

   - `ADMIN_GITHUB_TOKEN` (with "public_repo" and "repo:status" permissions); see the [documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
   - `NPM_TOKEN` (with "automation" permission); see the [documentation](https://docs.npmjs.com/creating-and-viewing-access-tokens)

2. Set up PyPI tokens as a trusted publisher:

   - Set up your PyPI project by [adding a trusted publisher](https://docs.pypi.org/trusted-publishers/adding-a-publisher/)
     - The _workflow name_ is `publish-release.yml` and the _environment_ should be left blank.
   - Ensure the publishing release job as `permissions`: `id-token : write` (see the [documentation](https://docs.pypi.org/trusted-publishers/using-a-publisher/))

3. To create the release:
   1. Go to the "Actions" panel in the GitHub repository
   2. Run the "Step 1: Prep Release" workflow
   3. Check the draft change log
   4. Run the "Step 2: Publish Release" workflow

## Publishing to `conda-forge`

Once a new release is made on PyPI the conda-forge bot should pick up the new version publish to PyPI, and open a new PR on the feedstock repository automatically.
