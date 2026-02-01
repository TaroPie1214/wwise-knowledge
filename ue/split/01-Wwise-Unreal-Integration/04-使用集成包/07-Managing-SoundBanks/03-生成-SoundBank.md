# 生成 SoundBank

|  |
| --- |
| Wwise Unreal Integration Documentation |

生成 SoundBank

There are several ways to generate the Wwise SoundBanks: from [Wwise Authoring](https://www.audiokinetic.com/library/edge/?source=Help&id=generating_soundbanks_for_project), from the Unreal Editor, or through a [commandlet](using_features_generatecommandlet.html). This section explains how to generate SoundBanks in Unreal.

After you generate SoundBanks, you can access Events and other Wwise Objects through the Wwise Browser (see [Managing Assets with the Wwise Browser](features_editor_wwise_browser.html)), Blueprints, and so on.

**To generate SoundBanks in Unreal:**

1. Do one of the following:

   - From the menu bar, click **Build** > **Generate SoundBanks**.
   - In the upper-right corner of the Wwise Browser, click **Generate SoundBanks**

     ![](../../../../images/GenerateSoundBankBrowserButton.png)

   The Generate SoundBanks dialog opens.

   ![](../../../../images/GenerateSoundDataWindow.png)

   The dialog lists the platforms and languages that the Wwise project supports.
2. Select the desired platforms and languages. If you do not select any platforms or languages, all items in the respective list will be generated.
3. (Optional) To reduce soundbank generation time, select **Skip generation of localized assets**.
4. Click **Generate**. The SoundBanks are generated.

# SoundBank Generation 详情

## 通过 WwiseConsole 生成 SoundBank

在禁用 WAAPI 或没有打开 Wwise 设计工具时，可通过 WwiseConsole 来在 GeneratedSoundBanks 文件夹中生成 SoundBank。

## 通过 WAAPI 生成 SoundBank

在连接 WAAPI 时，会通过 WAAPI 直接把要生成 SoundBank 的命令发送到 Wwise 设计工具，但仍会在磁盘上的 GeneratedSoundBanks 文件夹中生成 SoundBank。

## SoundBank Generation Watcher

When the Unreal Editor is open, a directory watcher monitors changes in the GeneratedSoundBanks folder. Changes to files in this folder trigger a countdown timer that appears in a temporary window in the lower-right corner of the screen. Any subsequent changes reset the timer.

When the timer expires, the JSON metadata in the GeneratedSoundBanks folder is parsed, which updates the integration's internal database of the Wwise project.

After the project is parsed, all currently loaded Wwise assets are reloaded to properly apply changes in project data.

# Triggering Generated SoundBanks Parsing

If you do not manually generate SoundBanks, any operation that synchronizes the GeneratedSoundBanks folder contents causes the directory watcher to trigger the parsing process.

The following operations parse the project metadata from the GeneratedSoundBanks folder:

- Opening the Unreal Editor.
- Clicking **Refresh** in the Wwise Browser.
- Clicking **Refresh Project Database** in the Build menu.
- Changing the **Generated SoundBanks Folder** setting in the Unreal project's Wwise Integration Settings.
- Changing the **Generated SoundBanks Folder User Override** in the Unreal project's Wwise User Settings.
- Changing any of the files in the GeneratedSoundBanks folder.

# 素材重新加载选项

To avoid reloading in-memory assets every time you change the contents of the GeneratedSoundBanks folder, you can select an option in the Unreal Project Wwise User Settings to enable a prompt before assets are reloaded. When this setting is enabled, Wwise assets can only be reloaded with explicit user input except during the initialization of the Wwise Project Database when the Unreal editor is opened.

![](../../../../images/wwise_user_settings_asset_reload.png)

This is the prompt that appears in the bottom right corner of the screen:

![](../../../../images/wwise_database_update_reload_prompt.png)

After 10 seconds, if you do not click either option, the "Not Now" option is automatically selected.