# JupyterLab accessible themes

| Information | Links                                                                                                                                                                |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| Project     | [![License](https://img.shields.io/badge/License-BSD%203--Clause-gray.svg?colorA=2D2A56&colorB=5936D9&style=flat.svg)](https://opensource.org/licenses/BSD-3-Clause) |
| Tools | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/github_username/jupyterlab-accessible-themes/main?urlpath=lab) |

Welcome to the JupyterLab accessible themes repository 👋🏽 .
To learn more about the broader accessibility initiatives within Jupyter, check the [jupyter/accessibility repository][jupyter-accesibility].

- [JupyterLab accessible themes](#jupyterlab-accessible-themes)
  - [📦 Requirements](#-requirements)
  - [🏗 Installing the extension](#-installing-the-extension)
  - [🧽 Uninstalling the extension](#-uninstalling-the-extension)
  - [🙋🏽‍♀️ Contributing](#️-contributing)
    - [💻 Installing the development version](#-installing-the-development-version)
      - [Pre-requisites](#pre-requisites)
    - [🧽 Uninstalling the development version](#-uninstalling-the-development-version)
    - [✅ Testing the extension](#-testing-the-extension)
      - [Frontend tests](#frontend-tests)
      - [Integration tests](#integration-tests)
    - [📦 Packaging the extension](#-packaging-the-extension)
  - [📖 License](#-license)

<!-- TODO: we need to add a warning/disclose on what we mean by JLab accessible themes as pointed out by @gabalafou -->

## 📦 Requirements

- [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) >= 3.0

## 🏗 Installing the extension

To install the extension, execute:

```bash
pip install jupyterlab_accessible_themes
```

## 🧽 Uninstalling the extension

To remove the extension, execute:

```bash
pip uninstall jupyterlab_accessible_themes
```

## 🙋🏽‍♀️ Contributing

### 💻 Installing the development version

#### Pre-requisites

You will need to have [NodeJS](https://nodejs.org/en/download/) installed in your local computer to build the extension package.

The `jlpm` command is JupyterLab's pinned version of [yarn](https://yarnpkg.com/) that is installed with JupyterLab. You may use`yarn` or `npm` in lieu of `jlpm` in the commands below.

1. Clone this repository to your local computer

   ```bash
   git clone https://github.com/Quansight-Labs/jupyterlab-accessible-themes.git
   ```

2. Change to the `jupyterlab_accessible_themes` directory

   ```bash
    cd jupyterlab_accessible_themes
    ```

3. Install the package in development mode

    ```bash
    pip install -e .
    ```

4. Now you'll need to link the development version of the extension to Jupyterlab and rebuild the Typescript source:

   ```bash
   # Link your development version of the extension with JupyterLab
   jupyter labextension develop . --overwrite
   # Rebuild extension Typescript source after making changes - can use yarn or npm depending on your preference
   jlpm build
   ```

🔍 You can watch the source directory and run JupyterLab at the same time in different terminals to watch for changes in the extension's source and automatically rebuild the extension.

```bash
# Watch the source directory in one terminal, automatically rebuilding when needed
# Can use yarn or npm depending on your preference
jlpm watch
# Run JupyterLab in another terminal
jupyter lab
```

With the watch command running, every saved change will immediately be built locally and available in your running JupyterLab. Refresh JupyterLab to load the change in your browser (you may need to wait several seconds for the extension to be rebuilt).

By default, the `jlpm build` command generates the source maps for this extension to make it easier to debug using the browser dev tools. To also generate source maps for the JupyterLab core extensions, you can run the following command:

```bash
jupyter lab build --minimize=False
```

### 🧽 Uninstalling the development version

1. Remove the extension:

   ```bash
   pip uninstall jupyterlab_accessible_themes
   ```

2. In development mode, you will also need to remove the symlink created by `jupyter labextension develop`
command. To find its location, you can run `jupyter labextension list` to figure out where the `labextensions`
folder is located. Then you can remove the symlink named `jupyterlab-accessible-themes` within that folder.

### ✅ Testing the extension

#### Frontend tests

This extension is using [Jest](https://jestjs.io/) for JavaScript code testing.

To execute the tests run the following command:

```bash
jlpm
jlpm test
```

#### Integration tests

This extension uses [Playwright](https://playwright.dev/docs/intro/) for the integration tests (aka user level tests).
More precisely, the JupyterLab helper [Galata](https://github.com/jupyterlab/jupyterlab/tree/master/galata) is used to handle testing the extension in JupyterLab.

More information are provided within the [ui-tests](./ui-tests/README.md) README.

### 📦 Packaging the extension

See [RELEASE](RELEASE.md)

## 📖 License

[This project is licensed under the BSD-3-Clause license](https://opensource.org/licenses/BSD-3-Clause).

<!-- links -->
[jupyter-accesibility]: https://github.com/jupyter/accessibility
