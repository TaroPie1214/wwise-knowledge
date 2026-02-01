# Managing Wwise and Unreal Assets

|  |
| --- |
| Wwise Unreal Integration Documentation |

Managing Wwise and Unreal Assets

When Wwise and Unreal projects are integrated, all Wwise-specific Unreal assets have IDs, which reference corresponding objects in the Wwise project. You can create assets in the Content Browser, or use the [Wwise Browser](features_editor_wwise_browser.html).

To enable a connection to the Wwise project through WAAPI, refer to [Wwise Authoring API (WAAPI)](using_features_waapi.html).

![](../../../../images/WAAPIUserSettings.png)

# Synchronizing from Wwise to Unreal

When you generate SoundBanks in Wwise while the Unreal Editor is open, Unreal parses the content of the generated SoundBanks and updates the contents of the [Wwise Browser](features_editor_wwise_browser.html). In addition, any assets that are currently loaded in Unreal are then reloaded, and include the changes made in the Wwise project.

As shown in the following image, the associated Unreal and Wwise Assets can have different names. The association between the two is determined by the GUID, ShortID, and Asset Name properties. Therefore, you can rename Unreal assets without affecting the Wwise objects they reference.

![](../../../../images/AssetNameMatch.png)