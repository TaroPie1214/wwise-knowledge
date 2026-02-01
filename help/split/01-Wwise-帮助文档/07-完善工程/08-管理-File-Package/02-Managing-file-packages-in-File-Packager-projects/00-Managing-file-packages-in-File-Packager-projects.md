# Managing file packages in File Packager projects

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理 File Package](../00-管理-File-Package.md) > Managing file packages in File Packager projects

## Managing file packages in File Packager projects

After you create the File Packager project and import the SoundBank and streamed file
information, you can create and populate the packages you need. You can then generate
the packages so they can be included in the game.

File package management consists of the following tasks:

- [“在工程中添加文件包”一节](00-Managing-file-packages-in-File-Packager-projects.md#adding_file_packages_to_project "在工程中添加文件包")
- [“从工程中移除文件包”一节](00-Managing-file-packages-in-File-Packager-projects.md#removing_file_packages_from_project "从工程中移除文件包")
- [“Assigning files to packages”一节](01-Assigning-files-to-packages.md "Assigning files to packages")
- [“对文件包内的文件排序”一节](02-对文件包内的文件排序.md "对文件包内的文件排序")

### 在工程中添加文件包

根据需要，您可以在工程中添加任意数量的文件包（File Package）。When you add packages, you can specify the *block size*, the number of bytes upon which to align the data in your packages, which can vary depending on each platform's I/O device.

|  |  |
| --- | --- |
| [备注] | 备注 |
| For more information about block size and I/O device constraints, see [Low-Level I/O](https://www.audiokinetic.com/library/?source=SDK&id=streamingmanager__lowlevel.html) in the SDK documentation. For more information about block size, see [“配置 Block Size”一节](../03-配置-Block-Size.md "配置 Block Size"). |

**在工程中添加文件包的方法如下：**

1. 在 Packages 列表中，点击 **Add**（添加）。

   A new package is added to the Packages list.
2. 为新文件包命名，替换默认名称。
3. 按 **Enter** 键。
4. Repeat steps 1-3 until all your packages have been created.
5. (Optional) To specify the number of bytes upon which to align the data in your packages,
   type a value in the **Block Size** field. The
   typical value for each platform is 1, which indicates that there is no
   alignment.

### 从工程中移除文件包

If you no longer need a package, you can remove it from your project at any time.

**从工程中删除文件包的方法如下：**

1. 从 Packages 列表中，选择要删除的文件包。
2. 点击 **Remove**（删除）。

   文件包将从工程中删除。

---