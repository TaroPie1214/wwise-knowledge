# Packaging DLC files

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [完善工程](../00-完善工程.md) > [管理 File Package](00-管理-File-Package.md) > Packaging DLC files

## Packaging DLC files

Downloadable content, or DLC, is additional game content that is delivered separately from
the base game. This topic explains how to use the Wwise File Packager to prepare audio
DLC packages, which you can combine with other game assets. However, if you are using
the Wwise Unreal Integration or the Wwise Unity Integration, we recommend that you use
the bulk asset packaging option in Unreal (see [Packaging Wwise Assets as Bulk Data](https://www.audiokinetic.com/library/edge/?source=UE4&id=using_features_package_as_bulk_data.html)) or the Addressables system in Unity
(see [The Wwise Addressables Package for Unity](https://www.audiokinetic.com/library/edge/?source=Unity&id=pg_addressables.html)), respectively.

If you are using the File Packager for your DLC, it is important to remember the following
best practices and requirements when planning:

- When packaging content for the base game, set all of the default file
  assignments to **None** and manually assign
  files to packages (see [“Manually assigning files to a package”一节](02-Managing-file-packages-in-File-Packager-projects/01-Assigning-files-to-packages.md#manually_adding_files_to_package "Manually assigning files to a package")) so that you can
  identify any DLC you add later.
- After you generate the packages for the base game, save the project. You
  can use it as a point of reference for the initial game release.
- Ensure that you place any DLC-specific SoundBanks, streaming files, and
  loose media in separate DLC packages.
- When creating DLC assets, use the same version of Wwise and the same Wwise
  project that you used for the base game to ensure compatibility of the
  SoundBank and package formats.
- If any DLC-specific changes affect SoundBanks that already exist in the
  base game, add the SoundBanks to the DLC package as well. Package loading
  order determines which SoundBanks take precedence in case of
  conflict.
- To determine loading order, use the File Package Low-Level I/O,
  specifically the `CAkFilePackageLowLevelIO::LoadFilePackage()`
  method. For more information, see [Sample File Package Low-Level I/O
  Implementation Walkthrough](00-管理-File-Package.md "管理 File Package").

### Workflow example

The following example demonstrates how to work with DLC packages.

1. SoundBankA, which contains all of the base game assets, is assigned to
   Package\_Main.
2. The content of SoundBankA is modified after the initial release with
   additional DLC sound structures. It is assigned to the new, DLC-specific
   Package\_DLC.
3. The File Package Low-Level I/O is updated to load Package\_Main before
   Package\_DLC.
4. The game, which has the DLC, loads Package\_Main and then
   Package\_DLC.
5. When the game loads SoundBankA, Wwise loads it from Package\_DLC, which has a higher
   priority than Package\_Main.

使用相同的方法，可以继续为您的游戏部署新增内容。只需记住要手动将所有文件指派至一个文件包，并保存 File Packager 工程来为各版本创建新的起始参考点。

---