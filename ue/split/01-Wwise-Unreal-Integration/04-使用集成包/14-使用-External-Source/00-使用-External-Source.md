# 使用 External Source

|  |
| --- |
| Wwise Unreal Integration Documentation |

使用 External Source

External Sources are a type of source that developers can associate with Wwise sound objects to provide sound data at runtime. You can use External Sources to load media dynamically, especially if there are many different media files associated with an Event, such as multiple lines of dialogue.

You can use the External Source Manager to implement your own system that determines which media to load, as well as when and how to load it. The External Source Manager provides a highly extensible base class that contains a basic implementation to track states of External Sources and their media, but you must extend it to define the actual loading behavior.

In the Wwise Unreal Integration, the External Source system consists of three parts:

- The External Source Manager, which contains interfaces necessary for calling operations.
- The External Source Manager Implementation, which provides low-level media management operations that respond to PostEvent calls. These operations identify which media to load, and indicate when to unload and load media.
- The Simple External Source Manager, a sample extension that supports basic External Source management and acts as a reference for developers. It provides the data that the implementation layer uses. For more information, see [使用 Wwise Simple External Source Manager](using_features_simpleexternalsourcemanager.html).

# Setting up External Sources in Wwise Authoring

To use External Sources, you must first set the generation path in Wwise Authoring, in the External Sources tab in the Project Settings dialog. See [Specifying the Input/Output Locations for External Sources](https://www.audiokinetic.com/library/edge/?source=Help&id=specifying_input_output_locations_for_external_sources) for more information.

# 了解 External Source

External Source 是个空的容器。The game has to fill it in and inform the sound engine about its contents.

An External Source uses a Cookie as an identifier, similar to a ShortId. 若要获取 Cookie，请对在源的 Contents Editor 中为 External Source 插件指定的名称进行哈希处理。See [Contents Editor: Wwise External Source](https://www.audiokinetic.com/library/edge/?source=Help&id=contents_editor_wwise_external_source_plug_in) for more information.

When an Event that uses External Sources is posted to the sound engine, an array of [AkExternalSourceInfo](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_external_source_info.html) structures that identify the media to use for each Cookie must be passed with it. This media can be in memory or streamed, and the game must ensure that these resources are ready when the Event is posted.

For more information about External Sources, see the following topics:

- [Wwise External Source 概述](https://www.audiokinetic.com/library/edge/?source=Help&id=wwise_external_source_plug_in_overview)
- [Contents Editor：Wwise External Source](https://www.audiokinetic.com/library/edge/?source=Help&id=contents_editor_wwise_external_source_plug_in)
- [AkExternalSourceInfo 结构参考](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_external_source_info.html)
- [Integrating External Sources](https://www.audiokinetic.com/library/edge/?source=SDK&id=integrating_external_sources.html)

# 了解 Wwise External Source Manager

External Source 具有以下几个显著特性：

- 多个 Event 可使用同一 External Source。
- Multiple External Sources can use the same media.
- External Source 所用的媒体不在 SoundBank 中定义，并且可随时由游戏逻辑进行更改。

To manage the relationship between Events, External Sources, and media, the External Source Manager:

- tracks the state of External Sources used by loaded Events.
- provides `AkExternalSourceInfo` structures for calls to `PostEvent`.
- tracks the state of loaded media used by External Sources.
- tracks the mapping between loaded External Sources and media.
- triggers the loading and unloading of media used by External Sources.
- packages the media files used by External Sources in the game.

# 实现 Wwise External Source Manager

The default implementation of the Wwise External Source Manager attempts to answer `PostEvent` calls (`PrepareExternalSourceInfos`, `BindPlayingIdToExternalSources`, and `OnEndOfEvent`) as quickly as possible. It requests `PrepareExternalSourceInfos` in order to "use" the specified media until `OnEndOfEvent` indicates that the playing media is no longer needed. The Simple External Source Manager provides the cookies that identify the media to load. You can override the default implementation if desired.

To implement a custom Wwise External Source Manager, you must first create an Unreal module. 该模块至少要包含两个类：

- 一个继承 `FWwiseExternalSourceManager`，负责履行上节中所列的职责。
  - `FWwiseExternalSourceManager` 包含定义 External Source 所需的纯虚拟接口。在特殊情况下，工程可将此定义为其继承点，并完全控制 External Source 管线。
  - `FWwiseExternalSourceManagerImpl` 具有在运行时加载和卸载 External Source 所用媒体所需的各种函数。它包含由 External Source Cookie 到媒体 ID 的映射，可处理 I/O 操作并追踪媒体的生命周期。通过继承该类，可简化自定义追踪操作和打包的实现。`FWwiseExternalSourceManagerImpl` 类可自行处理复杂的 I/O 详细信息。
  - 您也可以将 `FWwiseSimpleExtSrcModule` 用作父类，因为它是可扩展的。
- 一个实现 `FWwiseFileHandlerModule`，负责覆盖 `InstantiateExternalSourceManager` 以返回第一个类的实例。

在此之后，若要启用模块，可将 `WwiseFileHandlerModuleName` 设为 `DefaultEngine.ini` 文件的 `[Audio]` 部分中的新模块的名称。有关详细信息，请参阅 [启用 Simple External Source Manager](using_features_simpleexternalsourcemanager.html#using_features_simpleexternalsourcemanager_enabling) 章节。

Wwise External Source Manager 是 `WwiseFileHandler` 模块中的接口。When Wwise Event assets that use External Sources are loaded, the `WwiseResourceLoader` module passes the External Source information in the Event's `CookedData` (see [Wwise Unreal 素材](pg_features_objects_assets.html)) to the `WwiseFileHandler`, which then delegates resource loading to the Wwise External Source Manager Implementation. Subsequent behavior depends on the implementation.

## Tracking External Source states

在默认实现中，External Source Manager 会创建 [FWwiseExternalSourceState](using_features_ext_src.html#using_features_ext_src_states_FWwiseExternalSourceState) 结构以供追踪 External Source。基于具体的实现和可用信息，会加载媒体或准备进行流传输。同样，在加载 Event 素材时，会告知 External Source Manager 并相应地更新 External Source 的状态。此行为履行 External Source Manager 的第一项职责（追踪 External Source 的状态），其在以下函数中实现：

- **PrepareExternalSourceInfos**：该公共方法会根据请求的 External Source 选择并检索所要播放的媒体列表，并准备所需的 `AkExternalSourceInfo` 以便播放 External Source。
- **LoadExternalSource**：该公共方法会在管理器的执行队列中准备对 `LoadExternalSourceImpl` 的调用。
- **UnloadExternalSource**：该公共方法会在管理器的执行队列中准备对 `UnloadExternalSourceImpl` 的调用。
- **LoadExternalSourceImpl**：该虚方法负责创建或更新被追踪 External Source 的状态。随后，调用 `LoadExternalSourceMedia`。
- **UnloadExternalSourceImpl**：该虚方法负责移除或更新被追踪 External Source 的状态。If the External Source State must be removed, `UnloadExternalSourceMedia` is called.

The default implementation answers `PostEvent` calls (`Prepare`, `Bind`) as quickly as possible.

## Providing information to PostEvent calls

第二项职责（填充 AkExternalSourceInfo 结构）由 `PrepareExternalSourceInfos` 履行。对此，将返回 `PostEvent` External Source 参数。它会检索 `CookieToMedia` 中的数据，使用该信息来定义不同的文件状态，并提供所需的 `AkExternalSourceInfo` 以便发送 Event。若要使用更为复杂的选择算法，可将其覆盖。

在 Wwise Simple External Source Manager 扩展中，有个固定的 `MediaInfo` DataTable，其用于识别工程中的所有 External Source 媒体及相关元数据。您可以采用更为高级的系统来动态更新已知媒体列表。因为有很多不同的方式来实现此类系统，所以所有操作都可以虚拟化。您可以创建相应的代码来让 Random Container 更改每一 PostEvent，或者根据外部状态（如语言变化）来更改结构。

## Loading and unloading media

The `FWwiseExternalSourceManagerImpl` class tracks known External Source media and the information necessary to load them. 这种状态追踪通过 `ExternalSourceStatesById` 映射在内部完成。

在实现前面所说的系统和结构后，建议实现以下虚函数：

- **LoadExternalSourceMedia**：查找 External Source 所用的媒体并予以加载或准备进行流传输。建议使用从 `FWwiseFileHandlerBase` 继承的方法来追踪媒体加载状态，并使用 [FWwiseExternalSourceFileState](using_features_ext_src.html#using_features_ext_src_states_FWwiseExternalSourceFileState) 结构来管理媒体资源。
- **UnloadExternalSourceMedia**：查找 External Source 所用的媒体并卸载与之对应的资源。
- **SetExternalSourceMediaById**：设置通过名称识别的 External Source 的媒体 ID。
- **SetExternalSourceMediaByName**：设置通过名称识别的 External Source 的媒体名称。
- **SetExternalSourceMediaWithIds**：设置通过 Cookie 识别的 External Source 的媒体 ID。

`SetExternalSourceMedia` 函数假定各个 External Source 媒体具有唯一的 ID。对于 `SetExternalSourceMediaByName`，则可通过名称来检索媒体 ID。建议将 Wwise Simple External Source Manager 作为这些函数的参考，因为实现很可能仅在如何存储、更新和检索由 External Source 到媒体的映射上有所不同。记住，External Source 和媒体文件之间映射关系的动态变化可能会导致资源被加载和卸载。

The current implementation treats these as blocking functions, which potentially run through the game thread. 不过，这并不是必需的。

|  |  |
| --- | --- |
|  | **警告：** Forcibly unloading External Source media while it is playing causes the sound engine to crash. The [FWwiseExternalSourceFileState](using_features_ext_src.html#using_features_ext_src_states_FWwiseExternalSourceFileState) can handle this automatically through the `BindPlayingIdToExternalSources` and `OnEndOfEvent` methods to increment and decrement their play counts. |

After you implement the desired functions, the most complex part of External Source manager development is complete. 倘若一切正常，可通过加载 Event 素材或采用系统对 External Source 的准备方式，来将 External Source 所用的媒体加载到内存中或准备进行流传输。

## Packaging External Source media

最后，必须对 External Source 媒体进行打包。简单来说，可在 Unreal 工程中生成 External Source 媒体，并将其保存到被设为始终烘焙的目录。To implement more complex packaging logic, override the External Source Manager's **Cook** method, which the Wwise Resource Cooker calls for each External Source contained in cooked Wwise Assets.

The following functions, which you can override, are also available:

- **BindPlayingIdToExternalSources**：覆盖该函数来在发送使用 External Source 的 Event 时更新管理器的内部状态。
- **OnEndOfEvent**：覆盖该函数来在停止播放使用 External Source 的 Event 时更新管理器的内部状态。
- **SetGranularity**：设置流媒体的预取数据块的粒度（要读取的最小字节数）。

# Wwise External Source Manager Blueprint

在默认情况下，会在 WwiseExternalSourceStatics 中暴露三个 Blueprint 函数。

- **SetExternalSourceMediaById**
- **SetExternalSourceMediaByName**
- **SetExternalSourceMediaWithIds**

These functions call the corresponding functions defined in the Simple External Source Manager extension. 有关详细信息，请参阅 [External Source Manager Blueprint 函数](using_features_simpleexternalsourcemanager.html#using_features_simpleexternalsourcemanager_blueprints) 章节。

# External Source Manager 所用的 State 结构

## FWwiseExternalSourceState

默认在 `WwiseExternalSourceManagerImpl` 中使用该结构来获取所加载 External Source 的引用计数。

## FWwiseExternalSourceFileState

Wwise Simple External Source Manager 使用该结构来处理媒体资源。状态可追踪引用计数以及其当前是否正在播放。Unloading External Source media while it is playing causes the sound engine to crash. 您可以通过两个子类来处理加载到内存中或进行流传输的媒体。

- **FWwiseInMemoryExternalSourceFileState**
  - 将 Media Data 加载到内存中以用于创建 [AkExternalSourceInfo](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_external_source_info.html) 结构并传给 SoundEngine。
- **FWwiseStreamedExternalSourceFileState**
  - FileState 通过 External Source Manager 的 `FWwiseFileHandlerBase` 基类对自身进行注册。在将要对媒体进行流传输的请求传给 External Source Manager 时，会检索注册的 FileState 并由其处理后续 I/O 请求。