# Developing DLC with the Wwise Unreal Integration

|  |
| --- |
| Wwise Unreal Integration Documentation |

Developing DLC with the Wwise Unreal Integration

This section lists several important requirements and recommendations to remember if you plan to release downloadable content (DLC) for your game.

# Working with DLC in Wwise Authoring

When working on DLC in Wwise Authoring, you can add new DLC-specific sound structures and Wwise assets, or add child elements to existing structures such as Switch Containers, Music Playlist Containers, and so on. Depending on the type of object you modify, you must then either repackage the affected SoundBanks or add new SoundBanks. For details and examples of SoundBank management for DLC in Wwise Authoring, see [DLC considerations and limitations](https://www.audiokinetic.com/library/edge/?source=Help&id=dlc_considerations_and_limitations).

Additionally, when working with media files in your project, ensure that there are no conflicts between DLC and base game asset ShortIDs. For more information, see [Short IDs in action](https://www.audiokinetic.com/library/edge/?source=Help&id=managing_media_asset_ids#shortids_in_action).

# Loading Events and Switch Containers

If you are using a customized `WwiseResourceLoader` module, you can manage Event and Switch Container loading to ensure that DLC-specific sounds are only loaded for DLC-specific maps, even if those sounds are part of a Switch Container that the base game also uses. See the Events and Switch Container section on the [WwiseResourceLoader 模块](module_resourceloader.html) page for more information.

# Packaging DLC

You must ensure that DLC-specific assets are packaged with the rest of the Unreal DLC game assets so they can be delivered appropriately as add-ons. We recommend that you use the **Package as Bulk Data** Unreal project setting, which packages Wwise assets with their corresponding Unreal UAssets. This option is required for Unreal's Cook On the Fly option to work. You can also use Wwise Asset Libraries to further distinguish DLC-specific assets, although this is not required.

For more information about bulk data and asset libraries, see [Packaging Wwise Assets as Bulk Data](using_features_package_as_bulk_data.html).