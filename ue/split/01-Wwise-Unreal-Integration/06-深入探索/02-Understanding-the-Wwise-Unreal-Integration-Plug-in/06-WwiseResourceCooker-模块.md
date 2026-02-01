# WwiseResourceCooker 模块

|  |
| --- |
| Wwise Unreal Integration Documentation |

WwiseResourceCooker 模块

WwiseResourceCooker 模块提供以下功能：

- 针对 [WwiseResourceLoader 模块](module_resourceloader.html) 将 WwiseObjectInfo 结构转换为已烘焙结构。
- 将所请求对象的文件从 GeneratedSoundBanks 复制到打包过程所用的 Staging 目录。

参见
:   - [Content Cooking](https://dev.epicgames.com/documentation/en-us/unreal-engine/cooking-content-in-unreal-engine) (Unreal Engine documentation)

# 为 Wwise 对象准备已烘焙数据

WwiseResourceCooker 由用于识别特定 Wwise 对象的 WwiseObjectInfo 结构开始，从与该 Wwise 对象相关的 Project Database 收集各种信息，并返回已烘焙并包含该信息的数据结构。

对于 SoundBank 或媒体文件，操作起来比较简单。因为这些都是最基本的，其各自代表不同的文件。外部源相对也比较简单。不过，它们通常由用户定义，所以复杂性不得而知。也就是说，默认生成的已烘焙数据仅将 Cookie 作为非调试信息。

有些已烘焙数据仅包含 Short ID。就跟包含 Cookie 的外部源一样，Trigger、Game Parameter (RTPC) 和 Acoustic Texture 的已烘焙数据中只需要 Short ID 信息。同样，Switch 和 State 只需要其所属分组的标识符及其所代表的值。

其他对象（如 Auxiliary Bus 和 Effect ShareSet）可能会稍微复杂一些。最复杂的是 Event。其可能包含多个所需媒体、SoundBank、外部源、Aux Bus 和多个可选 Switch Container 元素。

## 默认实例化和平台实例化

WwiseResourceCooker 模块包含 Editor 和未烘焙工程中使用的默认实例化。此实例化用于 Play in Editor 模式，可在 Editor 中加载 Wwise 素材时根据需要提供已烘焙数据。此数据类似于已烘焙并在打包好的游戏中的 Wwise 素材中序列化的数据。唯一的区别在于 Editor 的已烘焙数据直接使用 GeneratedSoundBanks 文件夹中的资源文件（.bnk 和 .wem）。与之相比，已烘焙并打包的数据使用随游戏一起打包的资源文件。

在打包时，通常会生成外部烘焙过程，其只负责烘焙特定的平台。比如，在 Mac 电脑上会将默认实例化用于 Mac 平台。这时可以将 Android WwiseResourceCooker 实例化来打包 Android 游戏。

由于为平台加载 Project Database 可能会很耗时，所以只会针对各个烘焙过程加载所需的平台。通常，这意味着只会在 Project Database 中加载一个平台。不过，若同一过程在烘焙多个平台，或直接在编辑器过程内烘焙，则可能会加载多个平台。

# 从烘焙 Wwise 资源到暂存

基于已烘焙并在内部缓存的数据，将所有必要文件从 GeneratedSoundBanks 复制到 Staging 目录。媒体和 SoundBank 代表单个文件。外部源由用户定义，因为 Cookie 不代表文件。其他对象代表一个以上的文件。比如，Init Bank 从技术层面来说是 SoundBank。它也可能需要外部媒体文件。因此，在烘焙 Init Bank 时还会复制其媒体文件。

# 烘焙选项

以下烘焙选项可用于打包好的游戏。

## Package as Bulk Data

A **Package as bulk data** is available in the Unreal Project Settings dialog in the Wwise - Integration Settings section. This setting determines how Wwise assets are packaged during cooking.

If the setting is selected, the packaging process changes in the following ways:

- Wwise data files used in a single location in the Wwise project are packaged inside the assets that reference them. For example, if an Unreal asset called FootstepsAudioEvent references a Wwise auto-defined SoundBank Event called Play\_Footsteps, then when it is packaged the SoundBank and the associated Wwise Media are bundled inside the Footsteps AudioEvent UAsset as Unreal Bulk Data.
- Wwise External Sources and shared files are not packaged inside the Unreal assets. For example, if an Unreal object called PlaySnareAudioEvent references a Play\_Snare Event inside a user-defined SoundBank called DrumKit, then the DrumKit is packaged as individually copied files.
- This setting enables the **Libraries used for cooking Wwise UAssets as BulkData** option, through which you can define a prioritized order of Wwise Asset Libraries that are used to package shared Wwise files or specific files.
- When enabled, you can also use the Unreal **Multi-Process Cooking** or **Iterative Cooking** option. Due to engine limitations, these options only function fully when Wwise assets are packaged as bulk data.

If the setting is not selected:

- Wwise data files are individually copied as additional files alongside the other assets. They can be packaged as Pak files, but are not packaged in the IO Store.
- Incremental cooking is unreliable. Every additional file that Unreal doesn't handle directly (such as .uasset and .umap files) are copied and never cleaned up. You can, however, delete all the .wem and .bnk files before the cooking or packaging process begins.
- Multi-process cooking is unreliable. If a shared asset is cooked by two different processes, the latter will fail. There is no workaround.

参见
:   - [Packaging Wwise Assets as Bulk Data](using_features_package_as_bulk_data.html)

## ExportDebugNameRule

在 Editor 中针对默认实例进行烘焙时，每个已烘焙素材都有一个调试名称。该名称中包含完整的 Wwise Object Path。藉此，可在调试时轻松识别素材。

在对打包好的游戏进行烘焙时，ExportDebugNameRule 会确定是填充各个素材的调试名称字段还是将其保留为空。通过将这些字段保留为空，可减小文件的大小并方便实施逆向工程；不过也增加了调试的难度，因为只能使用素材的 Short ID 来识别已烘焙数据中的对应 Wwise 对象。

## LoadOnReference

您可以在 AkAudioEvent 素材上启用 LoadOnReference 选项。若启用该选项，会根据当前加载的 Switch 和 State 仅加载所需的 SoundBank 和媒体。在加载和卸载 Switch 或 State 时，会反过来动态地加载和卸载关联的资源。若禁用该选项，在加载包含 Switch Container 的 Event 时，会加载这些 Switch Container 使用的所有 SoundBank 和媒体。

在启用此选项时，烘焙过程会为 Event 准备已烘焙数据，以便为这种动态加载资源的方式提供支持。在禁用该选项时，已烘焙数据会随 Event 一起加载所有资源。

您可以根据需要为各个素材分别启用此选项。

|  |  |
| --- | --- |
|  | **注記：** 启用此选项会增加很多麻烦。为此，需要对功能有清楚的了解，尤其是在工程以编程方式设置 Switch 和 State 的时候。在大部分情况下，该选项带来的优化并不足以抵消这些缺点。 |

参见
:   - [Optimizing Memory Usage with Reference-Loaded Switch Containers](using_features_reference_load_switch_container.html)