import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { IThemeManager } from '@jupyterlab/apputils';

import { ISettingRegistry } from '@jupyterlab/settingregistry';

/**
 * Initialization data for the jupyterlab-accessible-themes extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab-accessible-themes:dark',
  autoStart: true,
  requires: [IThemeManager],
  optional: [ISettingRegistry],
  activate: (app: JupyterFrontEnd, manager: IThemeManager, settingRegistry: ISettingRegistry | null) => {
    console.log('JupyterLab extension jupyterlab-accessible-themes is activated!');
    const style = '@jupyterlab-accessible-themes/jupyterlab-theme-dark/index.css';

    manager.register({
      name: 'jupyterlab-accessible-dark',
      isLight: true,
      load: () => manager.loadCSS(style),
      unload: () => Promise.resolve(undefined)
    });

    if (settingRegistry) {
      settingRegistry
        .load(plugin.id)
        .then(settings => {
          console.log('jupyterlab-accessible-themes settings loaded:', settings.composite);
        })
        .catch(reason => {
          console.error('Failed to load settings for jupyterlab-accessible-themes.', reason);
        });
    }
  }
};

export default plugin;
