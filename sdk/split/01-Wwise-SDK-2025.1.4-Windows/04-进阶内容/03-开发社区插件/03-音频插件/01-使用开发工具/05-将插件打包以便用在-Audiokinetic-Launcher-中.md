# 将插件打包以便用在 Audiokinetic Launcher 中

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

将插件打包以便用在 Audiokinetic Launcher 中

在针对所有目标平台和配置构建插件后，需要将其打包以便[通过 Audiokinetic Launcher 安装](https://www.audiokinetic.com/library/wwise_launcher/?source=InstallGuide&id=plugins)。为此，请执行以下两个步骤：

1. 打包各个目标平台以及专用的 **Common** 平台。打包脚本会从 Wwise 安装目录自动检索全部所需文件。
2. 生成 **bundle.json** 文件。捆绑包生成脚本会从插件目录自动检索之前打包的存档。

比如，通过在命令行中运行以下代码，来打包 Common、Documentation、Windows\_vc160 和 Authoring 平台：

python "%WWISEROOT%/Scripts/Build/Plugins/wp.py" package Common --version=XXXX.X.X.X

python "%WWISEROOT%/Scripts/Build/Plugins/wp.py" package Documentation --version=XXXX.X.X.X

python "%WWISEROOT%/Scripts/Build/Plugins/wp.py" package Windows\_vc160 --version=XXXX.X.X.X

python "%WWISEROOT%/Scripts/Build/Plugins/wp.py" package Authoring --version=XXXX.X.X.X

python "%WWISEROOT%/Scripts/Build/Plugins/wp.py" generate-bundle --version=XXXX.X.X.X

`version` 参数采用 Wwise 版本号格式，即 `year.major.minor.build` 。

|  |  |
| --- | --- |
|  | **备注:** 在生成捆绑包之前，可能还要编辑 bundle\_template.json 文件。如需进一步了解插件打包格式及其与 Audiokinetic Launcher 的关系，请参阅 [Audiokinetic Launcher 的插件打包格式](plugin_packaging.html) 。 |

|  |  |
| --- | --- |
|  | **备注:** 插件的 Documentation 部分为可选部分。 |

# 使用插件打包附加文件

您可以使用 **–additional-artifacts** 或 **–additional-artifacts-file** 标记来针对任何平台打包附加文件。

在使用 **–additional-artifacts-file** 标记时，必须提供相应的 JSON 文件以列出所要打包的附加文件。目标路径必须是相对于 Wwise 安装根目录的，而源路径则须是相对于插件根目录的。

这里我们以前面章节中的命令行为例稍作更新，以便针对 Windows\_vc160 和 Authoring 平台打包附加 DLL 文件：

python "%WWISEROOT%/Scripts/Build/Plugins/wp.py" package Common --version=XXXX.X.X.X

python "%WWISEROOT%/Scripts/Build/Plugins/wp.py" package Documentation --version=XXXX.X.X.X

python "%WWISEROOT%/Scripts/Build/Plugins/wp.py" package Windows\_vc160 --version=XXXX.X.X.X --additional-artifacts-file=additional\_artifacts.json

python "%WWISEROOT%/Scripts/Build/Plugins/wp.py" package Authoring --version=XXXX.X.X.X --additional-artifacts-file=additional\_artifacts.json

python "%WWISEROOT%/Scripts/Build/Plugins/wp.py" generate-bundle --version=XXXX.X.X.X

前面例子中所用的 **additional\_artifacts.json** 文件将被存放在插件根目录并包含以下内容（假定 `lib/Debug/library.dll` 和 `lib/Release/library.dll` 存在于插件目录下）：

{

"Authoring": [

{

"Authoring/x64/Release/bin/Plugins": ["lib/Release/library.dll"]

}

],

"Windows\_vc160": [

{

"SDK/Win32\_vc160/Debug/bin": ["/lib/Debug/library.dll"],

"SDK/Win32\_vc160/Release/bin": ["/lib/Release/library.dll"],

"SDK/x64\_vc160/Debug/bin": ["lib/Debug/library.dll"],

"SDK/x64\_vc160/Release/bin": ["lib/Release/library.dll"]

}

],

}

**–additional-artifacts** 标记的作用与此类似，只不过其每次只接收一个路径（若要打包多个附加文件，则须多次指定该标记）。

最后，可使用同一 **additional\_artifacts.json** 文件来打包存放在工程目录下的其他文件。为此，请指定 destination -> sources 条目而非路径。如前所述，目标路径必须是相对于 Wwise 安装根目录的，而源路径则须是相对于插件根目录的。这里我们对前面的 Authoring 平台示例稍作更新，以便同时打包 **Factory** **Assets** 和 **Help** 文件：

{

"Authoring": [

{

"Authoring/x64/Release/bin/Plugins": ["lib/Release/library.dll"]

"Authoring/Help/<PluginName>": ["Help/\*.pdf"],

"Authoring/Data/Factory Assets/<PluginName>": [

"FactoryAssets/\*.wproj",

"FactoryAssets/\*.xml"

]

}

],

"Windows\_vc160": [

{

"SDK/Win32\_vc160/Debug/bin": ["/lib/Debug/library.dll"],

"SDK/Win32\_vc160/Release/bin": ["/lib/Release/library.dll"],

"SDK/x64\_vc160/Debug/bin": ["lib/Debug/library.dll"],

"SDK/x64\_vc160/Release/bin": ["lib/Release/library.dll"]

}

],

}

前面所述的 additional\_artifacts 文件可进一步用来将文件从工程根目录复制到 Wwise 安装根目录。destination -> sources 条目可使用 **–copy-artifacts** 标记来复制。此选项会跳过打包流程，而直接复制相应的文件。

下一章节：[为插件创建 Factory Asset](effectplugin_tools_factoryassets.html)