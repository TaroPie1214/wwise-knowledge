# WwiseResourceLoader 模块

|  |
| --- |
| Wwise Unreal Integration Documentation |

WwiseResourceLoader 模块

WwiseResourceLoader 模块在 [WwiseFileHandler 模块](module_filehandler.html) 的上一层级，负责处理 Wwise 工程素材及其依赖项。跟 WwiseFileHandler 一样，WwiseResourceLoader 执行的两项主要操作也是加载和卸载各种资源。不过，WwiseResourceLoader 会针对所有素材类型执行这些操作。

比如，Aux Bus 可以与一个 SoundBank 关联。不过，也有可能依赖于与别的 SoundBank 关联的另一 Aux Bus。而且，其也可与各个效果器插件所需的媒体文件关联。在加载所有这些 SoundBank 和媒体文件之后，才能使用 Aux Bus。在 WwiseResourceLoader 收到加载 Aux Bus 的请求时，WwiseFileHandler 会加载所有这些资源。

# Event 和 Switch Container 资源

Event 是要加载的最复杂的 Wwise 对象，也是执行各种 Wwise 操作的基础。Wwise Event 可包含各种其他类型的 Wwise 对象。它可能需要准备外部源并加载多个必要的 SoundBank 和媒体文件。另外，还可能将所有这些依赖项嵌套在 Switch Container 层级结构内。此外，AkAudioEvent 素材还设有 [LoadOnReference](module_resourcecooker.html#switchloadinginevents) 选项。其仅在地图中当前加载了关联的 Switch 和 State 时加载 Switch Container 资源。在默认情况下，会禁用此优化选项。不过，在使用较大的 Switch Container 层级结构时启用可以节省内存。

比如，对于使用依赖于地面材质 Switch 的 Switch Container 的 *Play Footsteps* Event，只会为当前所加载地图中的 Switch 加载声音。此外，可能存在多个 Switch Container 分层。比如，仅通过 DLC 提供的高品质版本，或动态选择的条件（如鞋子种类、角色的重量或速度）。基于这些条件，可设置非常复杂的 Switch Container 层级结构。藉此，可在给定时间选择是否加载所有这些内容。

在 Integration 中，可借助 Switch Container Leaf 来管理这些条件。其中每个 Leaf 代表一组潜在条件（Switch 和 State）和满足条件时所须加载的关联 SoundBank、媒体及外部源。

虽然 Group Value（如 Switch 和 State）可以作为素材包含在工程中并打包到部署的游戏中，但仍可通过直接调用声音引擎中暴露的方法来以编程方式加以设置。在这种情况下，在使用 LoadOnReference 选项时，必须在设置 Group Value 前将相应信息发送到 WwiseResourceLoader 以便其准备加载潜在文件。比如，在代码将整个应用程序设为 High Quality 时，需要告知 WwiseResourceLoader 视为已经设置 Group Value。即便在烘焙之后，也可以编程方式为 Switch、State 和 Game Parameter 结构提供这些数据。

参见
:   - [Optimizing Memory Usage with Reference-Loaded Switch Containers](using_features_reference_load_switch_container.html)

# 更改语言

若应用程序的语言发生变化，WwiseResourceLoader 会重新加载本地化素材。在这个耗时的过程中，会卸载所有本地化的 SoundBank 和媒体，然后加载与新语言对应的资源。在此操作当中，会暂时无法使用受影响的素材，发送的话会导致发生错误。