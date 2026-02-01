# Assigning files to packages

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理 File Package](../00-管理-File-Package.md) > [Managing file packages in File Packager projects](00-Managing-file-packages-in-File-Packager-projects.md) > Assigning files to packages

### Assigning files to packages

After you create your packages, you can fill them with SoundBanks and streamed media files.

You can assign files to packages in two ways:

- [“Manually assigning files to a package”一节](01-Assigning-files-to-packages.md#manually_adding_files_to_package "Manually assigning files to a package")
- [“Automatically assigning files to a package”一节](01-Assigning-files-to-packages.md#assigning_files_to_package_automatically "Automatically assigning files to a package")

#### Manually assigning files to a package

You can manually assign files to packages when necessary, for example when
creating new game content that will be available after the initial release. When
you manually add files to a package, all automatic file assignments are
overridden.

When you add a SoundBank to a package manually, you can choose to include only the
SoundBank, the streamed files associated with the SoundBank, or both. At any
time, you can switch to the Resulting contents tab of the Package contents pane
to review the actual contents of a package.

**To manually assign files to a package:**

1. Select a package in the Packages pane.

   The contents of the package are displayed in the Package contents pane.
2. 执行以下操作之一：

   - In the Packages pane, select the desired package, then select one or more files from
     Files to package pane and click **Add to
     current package**.
   - In the Packages pane, select the desired package, then drag one or more files from
     the Files to package pane to the Manually added files tab in
     the Package contents pane.
   - Drag one or more files from the Files to package pane to the desired package in the
     Packages pane.

   The number of files assigned to the package appears in parenthese on the Manually added
   files tab in the Package contents pane. The Resulting contents tab
   displays the total number of files included in the package, which might
   be different (for example, if a single SoundBank is added to a package
   that includes references to several streamed media files).

#### Automatically assigning files to a package

You can create a set of rules in the File Packager to automatically assign files to
specific packages. You can select package assignments based on language or file
type. Automatic assignment rules only apply to files that have not already been
manually assigned to packages.

**To automatically assign files to a package:**

- In the Default file assignments pane, use the expandable lists to select the destination
  packages for SoundBanks, Streams, and LooseMedia for each language and
  for SFX files as desired.

  Any files that are not manually assigned to a package are automatically assigned to
  their appropriate packages.

---