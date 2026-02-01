# 使用 Premake 配置工程

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

使用 Premake 配置工程

`premake` 命令会生成供 `build` 命令用来构建插件的解决方案。`new` 命令生成的默认 Premake 配置文件只需稍作修改便可用于所要创建的插件。注意**不可直接修改生成的解决方案**，因为再次调用 `premake` 命令会覆盖针对这些文件所作的全部修改。正确的做法是修改 Premake 配置文件。此配置文件存放在插件的根目录下，名为 **PremakePlugin.lua**。

Looking at the top of the **PremakePlugin.lua** file, notice a global table named **Plugin** is created. It contains the definition of the Wwise plug-in that Premake will import and use to generate the required projects and solutions. Entries of that table include the following:

- The **name** entry is a string that corresponds to the name of the plug-in, used as a prefix for all generated projects and solutions.
- The **factoryheader** entry is a string corresponding to the relative path to the factory header that will be installed with the plug-in into the public include directory of the Wwise SDK.
- The **appleteamid** entry is a string corresponding to the development team ID to set in the Signing & Capabilities section of an Xcode project, which is required for signing binaries on Apple platforms.
- The **signtoolargs** entry is an array, implemented as an integer-indexed table, which provides arguments to forward to `SignTool.exe` in a post-build step to sign dynamic libraries on Windows. When the array is empty, the post-build step is not added to the project.

Notice how the rest of the file is divided into three similar sections. 每个部分包含一个表格，里面设有多个字符串列表，用于配置如何生成解决方案：

- **Plugin.sdk.static** 表格用于配置静态 SDK 插件。
- **Plugin.sdk.shared** 表格用于配置共享 SDK 插件，并**链接静态 SDK 插件**（由 premake 脚本在后台完成）。
- **Plugin.authoring** 表格用于配置设计工具插件，并**链接静态 SDK 插件**。

有关如何填充每个列表的详细信息，请参阅 Premake 文档：

- **includedirs** -> <https://github.com/premake/premake-core/wiki/includedirs>
- **files** -> <https://github.com/premake/premake-core/wiki/files>
- **links** -> <https://github.com/premake/premake-core/wiki/links>
- **libdirs** -> <https://github.com/premake/premake-core/wiki/libdirs>
- **defines** -> <https://github.com/premake/premake-core/wiki/defines>

在创建插件工程后，须从工程文件夹内调用 `premake` 等其他命令。下面展示了如何在当前操作系统上为设计工具平台生成解决方案：

cd MyNewFX

python "%WWISEROOT%/Scripts/Build/Plugins/wp.py" premake Authoring

可用平台包括：

```
Android, Authoring, Authoring_Windows, Authoring_Linux, Authoring_Mac, iOS, Linux, LinuxAuto, Mac, NX, OpenHarmony, PS4, PS5, QNX, tvOS, visionOS, Windows_vc160, Windows_vc170, XboxOneGC, XboxSeriesX
```

在生成解决方案时，请参阅 [针对不同的 Wwise 平台构建工程](effectplugin_tools_building.html) 章节来构建插件并将其安装到 Wwise 安装目录下。

|  |  |
| --- | --- |
|  | **备注:** To disable the code signing post-build step of shared libraries during development, pass the `--disable-codesign` flag to the premake action. |

# 静态 Authoring 配置

即便没有包含在生成的 `PremakePlugin.lua` 文件中，也会提供一个可选的 `Plugin.sdk.authoringstatic` 表格。该表格专门用于特定的用例，可为链接设计工具插件的静态 SDK 插件提供不同的配置。这里的示例展示了如何重复使用相同的 SDK 插件代码，并通过 `FOR_AUTHORING` 编译器进行如下定义：

Plugin.sdk.staticauthoring = {}

-- SDK STATIC AUTHORING PLUGIN SECTION

Plugin.sdk.staticauthoring.includedirs = Plugin.sdk.static.includedirs

Plugin.sdk.staticauthoring.files = Plugin.sdk.static.files

Plugin.sdk.staticauthoring.excludes = Plugin.sdk.static.excludes

Plugin.sdk.staticauthoring.links = Plugin.sdk.static.links

Plugin.sdk.staticauthoring.libdirs = Plugin.sdk.static.libdirs

Plugin.sdk.staticauthoring.defines = table.join(Plugin.sdk.static.defines, { "FOR\_AUTHORING" })

# 高级 Premake 配置

从以下示例可以看出工程的配置非常简单，因为大部分 Premake 代码都隐藏在了配置表中。若要实施更为高级的配置，请将 `custom` 字段添加到以下相应配置部分：

Plugin.sdk.static.custom = function()

-- put your Premake code here

end

Plugin.sdk.shared.custom = function()

-- put your Premake code here

end

Plugin.authoring.custom = function()

-- 在此插入 Premake 代码

end

下一章节：[针对不同的 Wwise 平台构建工程](effectplugin_tools_building.html)