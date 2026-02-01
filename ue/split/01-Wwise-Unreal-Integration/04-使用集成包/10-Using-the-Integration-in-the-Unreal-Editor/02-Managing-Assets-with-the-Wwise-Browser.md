# Managing Assets with the Wwise Browser

|  |
| --- |
| Wwise Unreal Integration Documentation |

Managing Assets with the Wwise Browser

You can use the Wwise Browser to access objects from your Wwise project in Unreal. To access the Wwise Browser, click **Window** > **Wwise Browser**.

![](../../../../images/WwiseBrowser.png)

The Wwise Browser includes a variety of features, some of which require a connection to the Wwise Authoring API (WAAPI), and others that do not. For more information about WAAPI features, refer to [Using Waapi Features](features_editor_wwise_browser.html#features_editor_waapi_picker).

The Wwise Browser's contents are refreshed automatically after you regenerate SoundBanks. To manually refresh the list, click the **Refresh** button.

You can use the Wwise Browser to:

- Locate files on disk.
- [Importing Wwise Assets](features_editor_wwise_browser.html#browser_importing_assets) Import Wwise Assets
- [Using the Drag-and-Drop Feature](features_editor_wwise_browser.html#features_editor_dnd) Drag Assets into Unreal Blueprint nodes or object components and properties.

# Using Waapi Features

Certain Wwise Browser features require the Wwise Authoring API (WAAPI). To enable these features, you must:

- Enable the Wwise Authoring API. Refer to [Wwise Authoring API (WAAPI)](using_features_waapi.html) for instructions.
- Open the Wwise project in Wwise Authoring.

The Wwise Browser is populated in real time with data from the Wwise Authoring tool. Any changes you make to object names or IDs in Wwise are reflected in the Wwise Browser.

After WAAPI is enabled, you can use the Wwise Browser to:

- Preview sounds.
- Toggle item selection sync between Wwise and Unreal.

## Previewing Sounds

You can use the Wwise Browser to preview sounds from your Wwise project in the Unreal Editor before you generate SoundBanks.

To preview a sound in the Wwise Browser, do one of the following:

- Select an Event or a Property Container and press the **Space bar**.
- Right-click the Event or Property Container and then click **Play/Stop**.

To stop a sound, do one of the following:

- Press **Space bar**.
- Right-click any element and click **Stop All**.

## Finding Work Units on Disk

You can use the Wwise Browser to open the folder in your file system that contains the Work Unit associated with an object.

To show the Work Unit location on disk:

- Right-click the element in the Wwise Browser, then click **Show in Folder**.

# Using the Drag-and-Drop Feature

You can drag Events, Auxiliary Busses, Acoustic Textures, States, Switches, Game Parameters (RTPCs), and Triggers from the Wwise Browser into the Unreal Content Browser to create corresponding [UAkAudioEvent](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent), [UAkAuxBus](pg_features_objects_assets.html#features_objects_classes_UAkAuxBus), [UAkAcousticTexture](pg_features_objects_assets.html#features_objects_classes_UAkAcousticTexture), [UAkStateValue](pg_features_objects_assets.html#features_objects_classes_UAkStateValue), [UAkSwitchValue](pg_features_objects_assets.html#features_objects_classes_UAkSwitchValue), [UAkRtpc](pg_features_objects_assets.html#features_objects_classes_UAkRtpc), [UAkTrigger](pg_features_objects_assets.html#features_objects_classes_UAkTrigger) assets.

To drag Wwise Assets into Unreal:

1. Open the Content Browser folder in which you want to create the asset.
2. In the Wwise Browser, select the Wwise object you want to use.
3. Drag the Wwise object into the Content Browser. A corresponding Unreal object is created.

In addition to individual items, you can drag any container (Work Unit, Folder, Switch/State Group) into the Content Browser to recreate the hierarchy as it exists in Wwise Authoring.

In addition, you can drag objects into:

- Parameters to Blueprint nodes.

  ![](../../../../images/DragBlueprint.png)
- Object components or properties.

  ![](../../../../images/DragProperty.png)

|  |  |
| --- | --- |
|  | **注記：** If you drop an object anywhere other than the Content Browser, the asset is created in the folder specified by the [Default Asset Creation Path](features_editor_wwise_browser.html#default_asset_creation_path_setting). |

## Setting the Default Asset Creation Path

You can specify a default asset creation path. Assets that are automatically created from Wwise objects (for example, by dropping an object from the Wwise Browser onto a Blueprint) are created in this folder.

|  |  |
| --- | --- |
|  | **注記：** We recommend that you retain the default `/Game/` part of the asset creation path. If you remove it, assets are created under the Plugins folder, which might cause confusion. |

To set the default asset creation path:

1. In the Unreal menu bar, click **Edit** > **Project Settings**. The Project Settings dialog opens.
2. On the Wwise - Integration Settings page, scroll to the Asset Creation section and type or paste the desired **Default Asset Creation Path**:

![](../../../../images/DefaultAssetCreationPath.png)

# Importing Wwise Assets

You can import Wwise Assets into your Unreal project from the Wwise Browser.

To import a Wwise Asset:

1. In the Wwise Browser, right-click the Asset you want to import and in the contextual menu, click **Import Selected Assets**. A file browser opens.
2. Browse to the desired location and click **Select Folder**. The Asset is imported to the folder.

# Wwise Browser Columns

The Wwise Browser is separated into four columns, which are described in the following sections.

## Name Column

The Name column recreates the hierarchy of the project as it exists in the SoundBanks and displays the name of the Wwise Items. It prioritises the name found in the Generated SoundBanks over the name in Wwise if the names are different.

## Wwise Project vs SoundBank Column

The Wwise Project vs SoundBank Column compares the Wwise Project to the Generated SoundBanks and provides information about the differences between the two. For this column to work properly, the Wwise Browser musbe [connected to Waapi](features_editor_wwise_browser.html#features_editor_waapi_picker).

- **New in Wwise**: The Wwise Project has the information but the SoundBanks do not. Generating the SoundBanks creates the item in the SoundBanks and changes this column to **SoundBank Up to Date**.
- **Deleted in Wwise**: The SoundBanks have the item information but Wwise does not. Generating the SoundBanks removes the item from the Wwise Browser or, if a UAsset of the item exists, changes the column to **Not in Wwise or SoundBank**.
- **Renamed in Wwise**: The Wwise Project and the SoundBanks have the same item but with different names. Generating the SoundBanks renames the item inside the SoundBanks to match the name in Wwise.
- **Not in Wwise or SoundBank**: A UAsset uses an item that does not exist in Wwise or the SoundBanks. Avoid using this UAsset in your game.
- **Moved in Wwise**: The item exists in both Wwise and the SoundBank, but in a different location in each. Generating the SoundBanks moves the item to the same location it is in Wwise and changes this column to **SoundBank Up to Date**. Items with this label are shown where they are according to the SoundBanks in the Wwise Browser.
- **SoundBank Up to Date**: The name and ID of the item are the same in the Wwise Project and in the SoundBanks.

## Unreal Assets Column

The Unreal Assets Column provides information about the Wwise assets inside the Unreal project. If the Wwise item does not have a matching UAsset, this column is empty. If only one UAsset exists for the item, the Column shows the name of the UAsset. If there are multiple UAssets for the item, then “Multiple UAssets” followed by the number of UAssets is displayed. To see all the items, right-click on the item and click **Show in Content Browser**.

## SoundBank vs UAsset Column

The SoundBank vs UAsset Column compares the Generated SoundBanks to the assets in the Unreal project.

- **UAsset Missing**: The item exists in the SoundBanks but there are no UAssets associated with it. This means that the item is not used in your game.
- **Not in SoundBank or Unreal**: The item exists only in Wwise. Generating the SoundBanks changes this item to **UAsset Missing**.
- **UAsset Orphaned**: This UAsset has no item associated with it. Using it in your game will throw warnings.
- **Renamed in SoundBank**: The item exists and there is a single UAsset associated with it but the name of the item and the UAsset are different.
- **Multiple UAssets**: The item exists and there are multiple UAssets associated with it.
- **UAsset Needs Update**: There is one UAsset associated with the item but its information is not up to date with the SoundBanks.
- **UAsset Up to Date**: There is one UAsset associated with the item and its information is up to date with the SoundBanks.

## Orphaned UAssets Folder

If the Unreal project references Wwise assets that you then delete from your Wwise project, they are listed in the Orphaned UAssets folder, which appears at the end of the folder list:

![](../../../../images/WwiseBrowserOrphanedUAssets.png)

It is not possible to remove these UAssets with the Wwise Browser's reconciliation function. Instead, you must delete them manually. For more information on reconciliation, refer to [Reconciling Wwise UAssets](features_editor_reconcile.html).

# Filtering

You can filter Wwise objects to reduce the number of objects displayed in the Browser. There are three categories of filtering: SoundBank Status, UAsset Status, and Types. The SoundBank Status filters on the “Wwise Project vs SoundBanks” column, The UAsset Status filters on the **SoundBanks vs UAssets** column and Types filters on the Wwise item type. When you select a filter, all Wwise objects that do not satisfy the condition are filtered out of the Wwise Browser.

For an item to remain in the Wwise Browser, it must satisfy the conditions of all three categories. 例如：

![](../../../../images/WwiseBrowserFilter.png)

In this case, the Wwise objects must be Events or Switches that are UAsset Orphaned or Not in SoundBank or UAsset and Renamed in Wwise or New in Wwise.

There is also a filter bar in which you can type Wwise object names to search for those objects.

# Reconciling

It is possible to [Reconcile UAssets](features_editor_reconcile.html#reconcile_browser) with the Wwise Browser.