// Copyright (c) Jupyter Accessibility Team.
// Distributed under the terms of the Modified BSD License.

import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin,
} from "@jupyterlab/application";

import { IThemeManager } from "@jupyterlab/apputils";

import { ISettingRegistry } from "@jupyterlab/settingregistry";

/**
 * Initialization data for the jupyterlab-accessible-themes extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  // NOTE: The package id cannot contain a dash or underscore, so we need
  // to remove it here.
  id: "jupyterlab-accessible-themes:pitayasmoothie",
  autoStart: true,
  requires: [IThemeManager],
  optional: [ISettingRegistry],
  activate: (
    app: JupyterFrontEnd,
    manager: IThemeManager,
    settingRegistry: ISettingRegistry | null
  ) => {
    console.log(
      "JupyterLab extension jupyterlab-accessible-themes is activated!"
    );
    // NOTE: The package name cannot contain a dash or underscore, so we need
    // to remove it for the installation folder name.
    const style =
      "@jupyterlab-accessible-themes/jupyterlab-theme-pitayasmoothie/index.css";

    manager.register({
      name: "pitaya smoothie",
      isLight: true,
      load: () => manager.loadCSS(style),
      unload: () => Promise.resolve(undefined),
    });

    if (settingRegistry) {
      settingRegistry
        .load(plugin.id)
        .then((settings) => {
          console.log(
            "jupyterlab-accessible-themes settings loaded:",
            settings.composite
          );
        })
        .catch((reason) => {
          console.error(
            "Failed to load settings for jupyterlab-accessible-themes.",
            reason
          );
        });
    }
  },
};

export default plugin;
