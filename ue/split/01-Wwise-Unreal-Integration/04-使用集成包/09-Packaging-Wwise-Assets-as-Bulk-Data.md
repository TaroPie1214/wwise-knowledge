# Packaging Wwise Assets as Bulk Data

|  |
| --- |
| Wwise Unreal Integration Documentation |

Packaging Wwise Assets as Bulk Data

The Wwise Unreal Integration includes configuration options that control file packaging behavior during Unreal's cooking process. By default, Wwise assets are packaged as "bulk data" during cooking, which means that the assets are packaged within Unreal UAssets when possible. If desired, you can clear the relevant configuration option to package files individually.

There are several reasons to package assets as bulk data:

- It reduces the number of files to package. For example, instead of packaging three different files for Fire\_Weapon (Fire\_Weapon.uasset, FireWeapon.bnk, and 903830747.wem), they are all packaged into the UAsset directly because they are referenced in the Fire\_Weapon Unreal asset exclusively.
- Performance is improved. Instead of opening and reading multiple files, only one file is read and processed sequentially. The effect on performance can be dramatic. For example, if a single Event prefetches thousands of streamed and resident assets that are not packaged as bulk data, each file must be opened, read, and closed individually.
- You can use the **Multi-Process Cooking (experimental)** and **Iterative Cooking** options as long as all the assets are properly packaged as bulk data, either directly in the requested UAsset or through Wwise Asset Libraries.
- Modular Gameplay, Asset Chunking, DLCs, and optional contents are fully supported. Although you can package a game with individual files with these Unreal options or goals, bulk data streamlines the packaging operation. The Wwise files are included in the main package, so the developer does not have to move them.
- The IO Store and Zen Store (experimental) are natively supported.

There are also several reasons to package files as individual additional files instead of as bulk data:

- When packaged as bulk data, some object duplication can occur. If two Unreal UObjects define the same Event, the data is duplicated.
- Unreal bulk data requires additional memory and storage resources. Although minimal, you must account for the additional resources (up to 500 bytes per asset).
- The files are embedded inside the UAsset. File replacement and updates are less granular, because a single change in one Wwise asset results in an update of the UAsset, including all the Wwise assets. User-modifiable assets are also less accessible.
- Unused assets might be packaged. Instead of automatic Unreal asset tree-shaking, you would have to manually manage Wwise Asset Libraries to minimize duplication.

# File Packaging Behavior

When you package files as bulk data, Wwise assets used in a single location in the Wwise project are packaged inside the Unreal UAssets that reference them. Typically, these are streamed audio files and files generated through the Wwise Auto-Defined SoundBanks.

The final destination of multi-reference assets depends on the file packaging configuration. In this context, a *multi-reference asset* is a Wwise asset that is referenced by multiple Events *in Wwise*, even if only some of those Events are used in Unreal. If two Wwise Events, such as Play\_Banter and Play\_Banter\_Test, use the same Wwise assets but there is only an Unreal UAsset for Play\_Banter, the packaging system still considers all the Wwise assets to be multi-reference.

All multi-reference assets are packaged as Additional files and after the files are cooked, they appear in the Wwise Staging Directory defined in the Wwise Integration settings. For example, a User-Defined SoundBank called DrumKit.bnk that contains multiple assets used in different Wwise Events would be packaged as an Additional file.

**To change packaging behavior:**

1. In Unreal, select **Edit** > **Project Settings**.
2. Scroll to the Wwise section and click **Wwise Packaging**. By default, **Package as Bulk Data** is selected. These default options support Multi-Process Cooking, Iterative Cooking, Modular Gameplay, and Asset Chunking.
3. To disable bulk data packaging, clear **Package as Bulk Data**.

|  |  |
| --- | --- |
|  | **注記：** If you want to temporarily disable bulk data packaging without changing configuration settings, you can pass the `-DisableWwiseBulkData` argument to the Cook commandlet. With this argument, the game is packaged using loose files, so you can generate SoundBanks directly in a packaged game. |

# Using Wwise Asset Libraries

The Wwise Asset Libraries are groups that are equivalent to Wwise SoundBanks. However, they are defined inside the Unreal project itself. You can use them to package all the Wwise files (if the Asset Library filter is empty), only the Multi-Reference assets (using the WwiseAssetLibraryFilterMultiReference), particular languages, or other criteria. You can create and configure as many Wwise Asset Libraries as required.

**To create a Wwise Asset Library:**

1. Do one of the following:
   - In the Unreal Content Browser:
     - Right-click and select **Wwise** > **WwiseAssetLibrary**.
   - On the Wwise Packaging settings page:
     1. Next to **Libraries use for cooking Wwise UAssets as Bulk Data**, click **+**. An empty element is added to the list.
     2. Open the empty element's dropdown and select **Wwise Asset Library**, then name and save the library.
2. Double-click the new Asset Library.
3. Configure your content filters as desired. The following example shows a "Footsteps" Wwise Asset Library that filters all Wwise assets that contain the text "Footstep\*" (the asterisk is a wildcard operator), or in other words the various footstep sounds used throughout the Unreal project.

   ![](../../../images/WwiseAssetLibraryFilters.png)

## Ordering and Priority

The **Libraries used for cooking Wwise UAssets as BulkData** list is ordered. The first library in the list overrides all items below it, the second library overrides the items below it, and so on. You can therefore create and arrange your libraries in such a way as to package more granular content first by placing the associated libraries at the top of the list, then gradually expanding the scope of the libraries.

The following example Demonstrates a series of Wwise Asset Libraries.

![](../../../images/packaging_libraries.png)

|  |  |
| --- | --- |
| **1** | WwiseAssetLibrary\_ComplexDLC, which contains certain DLC-specific content. |
| **2** | WwiseAssetLibrary\_fr, which contains exclusive French language assets. |
| **3** | WwiseAssetLibrary\_en, which contains exclusive English language assets. |
| **4** | WwiseMultiReferenceAssetLibrary, which contains all multi-reference assets that were not included in any of the previous libraries. |

In this case, some Wwise assets might be multi-reference and also tagged as French. If those assets match the filters configured in WwiseAssetLibrary\_fr, they are included in it instead of in the WwiseMultiReferenceAssetLibrary, because WwiseAssetLibrary\_fr is higher in the list and therefore takes precedence.

|  |  |
| --- | --- |
|  | **注記：** Every packaged Asset Library contains individual Bulk Data for every asset it loads. They are loaded on project startup, which means that there is a slight delay to startup timing, as well as a slight increase in memory usage. However, the effect is minimal. For example, in debug, 10 000 assets might cost 10000\*500 bytes of memory, or 5 megabytes of RAM.  Asset Libraries are not less efficient than individual file access. However, they are much less efficient and out of order than inline asset packaging. It is always faster to access cooked Wwise files inline to the Wwise Event (or other AkAudioType UAsset) to which it relates. Test thoroughly to see if there are any performance issues at load time. |

|  |  |
| --- | --- |
|  | **警告：** Leaks might occur if your packaged game includes unused assets such as media and SoundBanks that are only used for testing during development. Ensure that you create filters to exclude such assets from Asset Libraries. |

# Previewing Wwise Asset Library contents

After you create the Wwise Asset Libraries you need, you can preview the contents before you cook the files.

**To preview Wwise Asset Library contents:**

- On the Wwise Packaging settings page, double-click a Wwise Asset Library. The Preview section displays the predicted contents of the library according to the specified filters. However, note that the **Apply Wwise Packaging Settings** option must be selected in order to view the actual contents, because some files that might satisfy the current filter might already be included in another library that takes precedence. For example, the following preview shows the contents of the WwiseAssetLibrary\_play1 library, which has a filter to select all files that begin with the text "Play":

  ![](../../../images/packaging_preview.png)

  If the **Apply Wwise Packaging Settings** is cleared, the list expands to include additional files that match the filter:

  ![](../../../images/packaging_preview2.png)

  However, it is important to remember that **the contents of the library do not change**. Clearing the option only shows you all of the possible files, even the ones that would be packaged in other libraries that take precedence. It can nonetheless help you evaluate your library configuration.