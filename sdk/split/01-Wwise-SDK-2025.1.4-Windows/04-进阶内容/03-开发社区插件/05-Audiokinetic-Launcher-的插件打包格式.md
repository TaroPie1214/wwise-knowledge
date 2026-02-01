# Audiokinetic Launcher 的插件打包格式

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Audiokinetic Launcher 的插件打包格式

此页面主要针对插件作者。为此，我们将阐述在 Wwise 插件商店发布与 Audiokinetic Launcher 兼容的 Wwise 插件时需要遵守哪些要求。如需详细了解如何创建插件，请参阅“ [开发社区插件](goingfurther_newplugins.html) ”。

以下章节将详细说明在发布完全兼容的 Wwise 插件时需要遵循哪些必要步骤：

- [插件打包](plugin_packaging.html#plugin_packaging_body)
  - [定义](plugin_packaging.html#plugin_packaging_defs)
  - [捆绑包目录结构](plugin_packaging.html#plugin_packaging_bundle_dir_struct)
  - [捆绑包元数据](plugin_packaging.html#plugin_packaging_bundle_metadata)
- [版本管理](plugin_packaging.html#plugin_packaging_version_man)

# 插件打包

为了确保与 Audiokinetic Launcher 兼容并有效运用插件管理流程，插件作者需要按照特定方式打包插件。Audiokinetic Launcher 在运行时需要加载捆绑包，就像独立文件夹和存档一样，它必须包含插件安装所需的全部文件和元数据。

## 定义

在探讨如何打包插件前，我们需要先定义一下其中用到的一些参数。下表列出了这些参数可能使用的值。假如您看到有参数前后加了尖括号（<参数>），则表示其可扩展为相应的值。

|  |  |
| --- | --- |
| **DeploymentPlatforms** | SDKPlatforms |
| Android   OpenHarmony   iOS   tvOS   visionOS   Mac   Linux   Windows\_vc160   Windows\_vc170   XboxOne   XboxSeriesX   PS4   PS5   NX | android-9\_armeabi-v7a   android-9\_x86   android-21\_arm64-v8a   android-21\_x86\_64   OpenHarmony\_arm64-v8a   iOS   Linux\_x64   Mac   NX64   PS4   PS5   tvOS   visionOS   Win32\_vc160   Win32\_vc170   x64\_vc160   x64\_vc170   XboxOneGC\_vc160   XboxOneGC\_vc170   XboxSeriesX\_vc160   XboxSeriesX\_vc170 |

## 捆绑包目录结构

插件捆绑包是一个可能包含以下各种文件的扁平目录或存档（其中只有 bundle.json 为必须包含的文件）。

|  |  |
| --- | --- |
| **bundle.json** | 插件捆绑包描述文件。  **此文件为必含文件。** |
| **Authoring.tar.xz** | 此数据包包含所有设计文件，包括二进制文件、数据文件和法律声明文件。在必要时，可将该数据包拆分成多个文件。比如，您可以将其拆分为 Data、Binary 和 Documentation。不过，系统会安装所有数据包。 |
| **SDK.tar.xz** | 该数据包包含所有非平台专用 SDK 文件，包括插件头文件。 |
| **SDK\_<DeploymentPlatforms>.tar.xz** | 开发平台专用 Wwise SDK 插件文件。  **注：**所列命名方案只是为了方便演示。所有名称均可自行设定。我们只是为了与特定平台保持一致才使用了这样的组/值关联方式。 |

|  |  |
| --- | --- |
|  | **备注:** **存档格式**   捆绑包中的存档文件必须采用 TAR.XZ 或 ZIP 格式。Audiokinetic Launcher 会使用 bundle.json 文件内指定的元数据来解压该文件。注意，捆绑包本身也可以 .tar.xz 存档而非文件夹形式提供给 Audiokinetic Launcher。 |

这些存档内的文件夹结构必须遵循以下格式。请注意，现在 Wwise 设计工具中仅支持 64 位插件。我们在 Wwise 2017.2 中便取消了对 32 位插件的支持。

PluginName/

├── bundle.json

│

├── Authoring.tar.xz

│ └── Authoring

│ ├── Help

│ ├── Data

│ | └── Factory Assets

│ | └── PluginName

│ └── x64

│ └── Release

│ └── bin

│ └── plugins

│

├── SDK.tar.xz

│ └── SDK

│ └── include

│ └── [AK](namespace_a_k.html)

| └── Plugin

│

└── SDK\_<DeploymentPlatforms>.tar.xz

└── SDK

└── <SDKPlatforms>

├── Release

| ├── bin

| └── lib

├── Debug

| ├── bin

| └── lib

└── Profile

├── bin

└── lib

|  |  |
| --- | --- |
|  | **备注:** **法律声明**   插件程序员请从此处复制与插件代码相关的“法律声明”：\Authoring\x64\Release\bin\plugins\PluginName.txt |

### 示例

下面举例说明了支持 Wwise 设计工具以及 Linux\_x32 和 Linux\_x64 Wwise SDK 平台的插件捆绑包。

PluginName/

├── bundle.json

│

├── Authoring.tar.xz

│ └── Authoring

│ ├── Help

│ | └── PluginName\_UserGuide.pdf

│ ├── Data

│ | └── Factory Assets

│ | └── PluginName

│ | ├── Manifest.xml

│ | └── ...

│ └── x64

│ └── Release

│ └── bin

│ └── plugins

│ ├── PluginName.dll

│ ├── PluginName.xml

│ └── PluginName.txt

├── SDK.tar.xz

│ └── SDK

│ └── include

│ └── [AK](namespace_a_k.html)

| └── Plugin

| └── PluginName.h

│

└── SDK\_Linux.tar.xz

└── SDK

├── Linux\_x32

| ├── Release

| | ├── bin

| | | └── libPluginName.so

| | └── lib

| | └── libPluginNameFX.a

| ├── Debug

| | ├── bin

| | | └── libPluginName.so

| | └── lib

| | | └── libPluginNameFX.a

| └── Profile

| ├── bin

| | └── libPluginName.so

| └── lib

| └── libPluginNameFX.a

└── Linux\_x64

├── Release

| ├── bin

| | └── libPluginName.so

| └── lib

| └── libPluginNameFX.a

├── Debug

| ├── bin

| | └── libPluginName.so

| └── lib

| └── libPluginNameFX.a

└── Profile

├── bin

| └── libPluginName.so

└── lib

└── libPluginNameFX.a

## 捆绑包元数据

捆绑包中包含的 bundle.json 文件应采用以下结构（除非特别声明，否则全部字段均为必填字段）。

{

"id": string, // 此捆绑包的唯一标识符。id 不可与任何现有插件和版本重复。为了避免冲突，请在 id 中结合使用公司名称、插件名称、版本和内部版本号。For example: audiokinetic\_convolutionreverb\_2017.2.3\_4877

"name": string, // Name displayed in the Audiokinetic Launcher for this bundle

"tag": string, // Tag uniquely identifying the plug-in (format [0-9A-z\_]+, 50 characters maximum)

"description": string, // Description displayed in the Audiokinetic Launcher for this bundle

"image": string, // Base64 representation of an image to be displayed in the Audiokinetic Launcher for this bundle (PNG, JPEG or GIF)

"vendor": string, // Vendor name displayed in the Audiokinetic Launcher for this bundle

"type": "plugin", // Type of this bundle, must be "plugin"

// Data that is specific to this bundle type

"productDependentData": {

// Version of Wwise this bundle was built against.

// 如需了解所构建插件的兼容性，请参阅 AK\_OLDEST\_SUPPORTED\_WWISESDK\_VERSION。

"targetWwiseVersion": {

"year": number,

"major": number

}

},

// Version of this bundle

"version": {

"year": number,

"major": number,

"minor": number,

"build": number

},

// List of files to be installed for this bundle

"files": [

{

"id": string, // Unique identifier

"sha1": string, // SHA1 of the file

"size": number, // Size of the file (in bytes)

"sourceName": string, // Name of the file

"uncompressedSize": number, // Uncompressed size of the file (in bytes)

// List of groups for which this file should be installed (refer to the table below for the complete list of groups plug-ins have access to)

"groups": [

{

"groupId": string, // Unique identifier of the group

"groupValueId": string // Unique identifier of the group's value field

},

...

]

},

...

],

// List of EULAs associated with this bundle

"eulas": [

{

"displayName": string, // Name displayed in the Audiokinetic Launcher for this EULA

"displayContent": string, // Text displayed in the Audiokinetic Launcher for this EULA

"id": string // Unique identifier of this EULA

},

...

],

// Labels displayed next to this bundle

"labels": [

{

"class": string, // Style class applied to this label (default, primary, success, info, warning, danger)

"displayName": string // Name displayed in the Audiokinetic Launcher for this label

},

...

],

// Online documentation links for this bundle

"links": [

{

"displayName": string, // Name displayed in the Audiokinetic Launcher for this link

"id": string, // Unique identifier of this link

"url": string // Target URL of this link

},

...

],

// Local documentation files for this bundle

"documentation": [

{

"displayName": string, // Name displayed in the Audiokinetic Launcher for this documentation file

"filePath": string, // Path to the documentation file

"language": "en" | "ja" | "zh" // Language of the documentation file

},

...

]

}

|  |  |
| --- | --- |
|  | **备注:** **插件唯一标识符**  为了避免与其他插件重名，必须在插件唯一标识符中包含以下信息：  - 供应商名称 - 插件名称 - 完整版本 - 内部版本号 |

### 捆绑包组

bundle.json 中指定的每个文件都必须关联至一个或多个组。Audiokinetic Launcher 将使用此信息来确定是否要根据情况安装给定的文件。

|  |  |
| --- | --- |
| **groupId** | groupValueId |
| Packages | Authoring   SDK |
| DeploymentPlatforms | (*Please refer to the DeploymentPlatforms column in [定义](plugin_packaging.html#plugin_packaging_defs)*.) |

### 示例

接着前面的例子，下面举例说明了支持 Wwise 设计工具以及 Linux\_x32 和 Linux\_x64 Wwise SDK 平台的插件捆绑包对应的 bundle.json；它配套提供英文文档：

{

"id": "PluginAuthor\_PluginName\_2017.1.0\_0",

"name": "PluginName",

"description": "PluginName is an awesome Wwise plug-in that does XYZ.",

"image": "data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==",

"vendor": "PluginAuthor",

"type": "plugin",

"version": {

"year": 2017,

"major": 1,

"minor": 0,

"build": 0

},

"productDependentData": {

"targetWwiseVersion": {

"year": 2017,

"major": 1

}

},

"files": [

{

"id": "Authoring.tar.xz",

"sha1": "2ab1fb750b2d4c6f9ad8f4c0b8966fe866a676c4",

"size": 7450993,

"uncompressedSize": 74509930,

"sourceName": "Authoring.tar.xz",

"groups": [

{

"groupId": "Packages",

"groupValueId": "Authoring"

}

]

},

{

"id": "SDK.tar.xz",

"sha1": "4e86453b2541ce4f3400778f932c850fd09cc0ff",

"size": 503316,

"uncompressedSize": 5033160,

"sourceName": "SDK.tar.xz",

"groups": [

{

"groupId": "Packages",

"groupValueId": "SDK"

}

]

},

{

"id": "SDK\_Linux.tar.xz",

"sha1": "9cb1b7db241e476c4024d43aed46c2b17beee366",

"size": 263682,

"uncompressedSize": 2636820,

"sourceName": "SDK\_Linux\_x32\_Debug.tar.xz",

"groups": [

{

"groupId": "Packages",

"groupValueId": "SDK"

},

{

"groupId": "DeploymentPlatforms",

"groupValueId": "Linux"

}

]

}

],

"eulas": [

{

"displayName": "PluginName",

"displayContent": "PluginName is provided for free on an \"as is\" basis. As such, ...",

"id": "EULA"

}

],

"labels": [

{

"class": "info",

"displayName": "Alpha"

}

],

"links": [

{

"displayName": "Release Notes",

"id": "ReleaseNotes",

"url": "https://example.com"

}

],

"documentation": [

{

"displayName": "User Guide",

"filePath": "Authoring/Help/PluginName\_UserGuide.pdf",

"language": "en"

}

]

}

# 版本管理

每个插件捆绑包都对应一个特定版本的 Wwise。不过，每个版本的 Wwise 都支持先前版本的 Wwise 对应的插件。

我们会一直支持 Wwise 小版本之间的兼容性。比如，2017.1.1 和 2017.1.2 就是兼容的。此外，大版本之间也有可能兼容；不过，您要准备好使用 Wwise 大版本更新自己构建的插件。如需了解当前版本的 Wwise 兼容哪些插件版本，请参阅“ [版本说明](releasenotes.html)”。

每次我们中断兼容性，插件供应商都需要发布新版本的捆绑包。请不要尝试通过 Wwise Launcher 安装不兼容版本的插件。在安装 Wwise 的过程中，将自动列出 audiokinetic.com 上托管的兼容版本的插件捆绑包。

[AK](namespace_a_k.html)

Definition of data structures for AkAudioObject

**Definition:** [AkWwiseSDKVersion.cs:31](_ak_wwise_s_d_k_version_8cs_source.html#l00030)