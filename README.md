<div align="center">
 <img alt="Jupyter Accessibility logo" src="https://github.com/jupyter/accessibility/blob/main/docs/_static/logo.png?raw=true" width="250" />
</div>
<br>

# JupyterLab accessible themes

<!-- prettier-ignore-start -->
<!-- ignoring because prettier by default adds loads of spaces -->

| Information                  | Links                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Project                      | [![OSI License clickable badge - BSD-3](https://img.shields.io/badge/License-BSD%203--Clause%20📃-gray.svg?colorA=2D2A56&colorB=5936D9&style=flat.svg)](https://opensource.org/licenses/BSD-3-Clause) [![Project backlog clickable badge](https://img.shields.io/badge/Backlog-GitHub%20Board%20🗃️-gray.svg?colorA=2D2A56&colorB=A7B2F2&style=flat.svg)](https://github.com/orgs/Quansight-Labs/projects/8/views/1) |
| Tools                        | [![Launch on Binder clickable badge](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/github_username/jupyterlab-accessible-themes/main?urlpath=lab)                                                                                                                                                                                                                                                |
| <!-- prettier-ignore-end --> |

Welcome to the JupyterLab accessible themes repository 👋🏽 .
To learn more about the broader accessibility initiatives within Jupyter, check the [jupyter/accessibility repository][jupyter-accesibility].

- [JupyterLab accessible themes](#jupyterlab-accessible-themes)
  - [Themes](#themes)
  - [Font](#font)
  - [📦 Requirements](#-requirements)
  - [🙋🏽‍♀️ Contributing](#️-contributing)
    - [💻 Installing the development version](#-installing-the-development-version)
      - [Pre-requisites](#pre-requisites)
        - [Building and linking the extension](#building-and-linking-the-extension)
    - [🧹 Pre-commit hooks](#-pre-commit-hooks)
    - [🧽 Uninstalling the development version](#-uninstalling-the-development-version)
    - [✅ Testing the extension](#-testing-the-extension)
      - [Frontend tests](#frontend-tests)
      - [Integration tests](#integration-tests)
    - [📦 Packaging the extension](#-packaging-the-extension)
  - [📖 License](#-license)
  - [Acknowledgements](#acknowledgements)


This repository defines a set of accessible themes according to [WCAG color standards](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html). Please note that some themes are optimized for colorblindness and/or high contrast. Inside the readme of each theme you will find detailed information of the colors, its purpose and reference links from the original authors.

## Themes

- [Pitaya Smoothie](./packages/pitayasmoothie/README.md) - Color-blind friendly
- [GitHub light](./packages/githublight/README.md) - Color-blind friendly

## Font

All the themes are using the [Atkinson Hyperlegible font](https://brailleinstitute.org/freefont), which focuses on letterform distinction to increase character recognition, ultimately improving readability.

This font can only be changed for the `Markdown viewer` and the `Terminal`. You will need to make these changes from the `Advanced settings` editor in the JupyterLab UI:

1. Select the `Settings` option in the `menu bar`.
2. Go to `Markdown viewer settings`, and type the font family that you want to use.
3. To change the `Terminal` font, scroll down to `Terminal settings` and type the name of the font family.

## 📦 Requirements

- [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) >= 3.0

<!-- Will comment this section as it is not yet applicable, and was leftover from the cookiecutter -->
<!-- ## 🏗 Installing the extension

To install the extension, execute:

```bash
pip install jupyterlab_accessible_themes
```

## 🧽 Uninstalling the extension

To remove the extension, execute:

```bash
pip uninstall jupyterlab_accessible_themes
``` -->

## 🙋🏽‍♀️ Contributing

### 💻 Installing the development version

#### Pre-requisites

1. You will need to have [NodeJS](https://nodejs.org/en/download/) installed in your local computer to build the extension package.
2. Python >= 3.6 and pip.

##### Building and linking the extension

> **Note**
> The `jlpm` command is JupyterLab's pinned version of [yarn](https://yarnpkg.com/) that is installed with JupyterLab. You may use`yarn` or `npm` in lieu of `jlpm` in the commands below.
> You will need to have NodeJS installed in your local computer to build the extension package.

1. Clone this repository to your local computer:

   ```bash
   git clone https://github.com/Quansight-Labs/jupyterlab-accessible-themes.git
   ```

2. Change to the `jupyterlab-accessible-themes` directory:

   ```bash
    cd jupyterlab-accessible-themes
   ```

3. Optional- Create and activate a development environment with your package manager:

   ```bash
   # Create environment named `jupyterlab-accessible-themes`
   conda create -n jupyterlab-accessible-themes
   conda activate jupyterlab-accessible-themes
   ```

4. Install Jupyterlab and NodeJS **if not installed**:

   ```bash
   # Install node and jupyterlab from conda-forge
   conda install -c conda-forge 'nodejs>16' 'jupyterlab<4'
   ```

5. Install the node dependencies and build the extension:

   ```bash
   # Install node dependencies
   jlpm install

   # Compile packages before linking to Jupyterlab development version
   jlpm build
   ```

6. Install the package in development mode:

   ```bash
   pip install -e .
   ```

7. Now you'll need to link the development version of the extension to JupyterLab and rebuild the Typescript source:

   ```bash
   # Link your development version of the extension with JupyterLab
   jupyter labextension develop . --overwrite
   ```

8. On first installation, or after making some changes, to visualize them in your local JupyterLab re-run the following command:

   ```bash
   # Rebuild extension Typescript source after making changes
   jlpm build
   ```

9. Run JupyterLab and check that the installation worked:

    ```bash
    # Run JupyterLab
    jupyter lab
    ```

Once everything is installed, please remember that you will still need to select the theme inside JupyterLab via the main menu `Settings > Theme`.

##### Further development tips

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

### 🧹 Pre-commit hooks

This repository uses the `prettier` [pre-commit hook](https://pre-commit.com/) to standardize our YAML and markdown structure.

1. Before you can run the hooks, you need to install the pre-commit package manager:

   ```bash
   # using pip
   pip install pre-commit

   # if you prefer using conda
   conda install -c conda-forge pre-commit
   ```

2. From the root of this project, install the git hook scripts:

   ```bash
   # install the pre-commit hooks
   pre-commit install
   ```

3. Optional- run the hooks against the files in this repository

   ```bash
   # run the pre-commit hooks
   pre-commit run --all-files
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

Detailed instructions for creating a `jupyterlab-accesible-themes` can be found in the [RELEASE](RELEASE.md) file.

> **Warning**
> As of 3rd of August this projects is still in its infancy and no releases are made yet.

## 📖 License

[This project is licensed under the BSD-3-Clause license](https://opensource.org/licenses/BSD-3-Clause).

<!-- links -->

[jupyter-accesibility]: https://github.com/jupyter/accessibility

## Acknowledgements

We want to thank the following sources for being the source of inspiration for one or more themes that are available in this repository,

- [Pitaya Smoothie theme](https://github.com/trallard/pitaya_smoothie)
- [GitHub's VS Code themes](https://github.com/primer/github-vscode-theme)
