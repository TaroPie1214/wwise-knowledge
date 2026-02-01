# 使用 Wwise Simple External Source Manager

|  |
| --- |
| Wwise Unreal Integration Documentation |

使用 Wwise Simple External Source Manager

External Sources and their media are decoupled by default. You must map External Source Cookies, which are equivalent to ShortIDs, to the media to play. External Source media can be generated alongside SoundBanks and streaming media, but you must also track the media files and their metadata.

借助 Simple External Source Manager，可追踪 External Source 媒体并将其映射到 External Source。It uses Data Tables (`.csv` files) that describe the External Source media to use in the game as well as an API and Blueprint functions to assign media to External Sources.

The Simple External Source Manager supports the External Source Manager Implementation in the following ways:

- Provides cookies
- Provides the default cookie table
- Provides the media list table
- Supports the functions that set IDs

A usage example of this submodule is available in the Wwise Demo Game (see [使用 Wwise Demo Game](using_samplegame.html)).

# 启用 Simple External Source Manager

在默认情况下，会禁用 Simple External Source Manager 模块。若要启用，请将以下代码行添加到 Unreal 工程中的 `DefaultEngine.ini` 文件：

[Audio]

WwiseFileHandlerModuleName=WwiseSimpleExternalSource

此代码会使用模块来覆盖 `WwiseFileHandlerModule`。该模块使用 Wwise Simple External Source Manager 子模块加载 External Source。

# 设置

在 Wwise Simple External Source Manager Settings 中，有两个 Data Table 和一个 Directory要设置。

- **Media Info Table**：包含加载媒体文件所需的元数据。
- **External Source Default Media**（可选）：定义 External Source 和 Media Info Table 中的媒体之间的初始映射关系。您可以通过本文档后续章节所述的 API 或 Blueprint 函数来更新或添加此映射关系。
- **External Source Staging Directory**：指定要将 External Source 媒体文件复制到哪个位置（相对于打包好的游戏中的 Game 文件夹）。

![](../../../../images/wsesm_settings.png)

## Media Info Table

Media Info Table 中的条目具有以下属性：

- **Name**：必须与 **ExternalSourceMediaInfoId** 匹配。用于在表格中实施查询。
- **ExternalSourceMediaInfoId**：用于在管理器中追踪媒体的唯一 ID。
- **MediaName**：用于在磁盘上查找文件的文件名称（带有扩展名）。同时由管理器在按名称设置媒体的情况下查找媒体 ID。
- **CodecID**：用于对媒体数据进行解码的 ID。参见 `AkGameplayTypes.h` 中的 `AkCodecId` 枚举值。
- **bIsStreamed**：决定是对媒体进行流传输还是将其加载到内存中。
- **bUseDeviceMemory**：决定是否使用设备专用内存。仅适用于内存中的媒体。
- **MemoryAlignment**：所要使用的内存对齐方式。仅适用于内存中的媒体。
- **PrefetchSize**：所要预取的数据量（以字节为单位）。仅适用于流媒体。

## External Source Default Media

Default Media Table 中的条目具有以下属性：

- **Name**：必须与 `ExternalSourceCookie` 匹配。用于在表格中实施查询。
- **ExternalSourceCookie**：External Source 的唯一 ID（可在 Wwise 设计工具或 SoundBank 元数据中找到）。
- **ExternalSourceName**：用于日志记录。
- **MediaInfoId**：必须与 **Media Info Table** 中的 `ExternalSourceMediaInfoId` 匹配。
- **MediaName**：用于日志记录。

# Understanding the Simple External Source Manager

在将 Simple External Source Manager 实例化时，其会读取 [Media Info Table](using_features_simpleexternalsourcemanager.html#using_features_simpleexternalsourcemanager_mediainfotable) 并填充相应的媒体元数据列表。同时，还会填充由媒体名称到媒体 ID 的映射以用于 [External Source Manager Blueprint 函数](using_features_simpleexternalsourcemanager.html#using_features_simpleexternalsourcemanager_blueprints) 。

Next, the [External Source Default Media](using_features_simpleexternalsourcemanager.html#using_features_simpleexternalsourcemanager_externalsourcedefaultmedia) is read, and External Source Cookie/media ID pairs are added to a map. This optional Data Table sets default media for External Sources to use in the game. 藉此，可减少 Blueprint 和函数对 `SetExternalSourceMedia` 方法的调用次数：若已经定义默认媒体，则只需将这些方法用于 External Source 来动态更改其媒体。

在 External Source Manager 加载 External Source（通常由加载的 `AkAudioEvent` 触发）时，将创建 State 结构以追踪引用 External Source 的素材数量并检查该映射。If a media pairing exists in the map, a state structure for the media is created or updated. Depending on the information read from the [Media Info Table](using_features_simpleexternalsourcemanager.html#using_features_simpleexternalsourcemanager_mediainfotable), the media is either loaded into memory from disk or, if it is streamed, the created state is registered to handle incoming streaming requests from the sound engine.

If an External Source Cookie/media ID pair is set during gameplay (for example, by the [External Source Manager Blueprint 函数](using_features_simpleexternalsourcemanager.html#using_features_simpleexternalsourcemanager_blueprints)), and if the External Source is already loaded, the media is loaded immediately. If the External Source is already mapped to a different media, the reference count of that media is decremented. 若引用计数为 0，则在停止播放后将其卸载。

All `PostEvent` calls that pass through the AkAudioDevice, including `PostEvent` calls from the Integration's Blueprint functions, call the External Source Manager's `PrepareExternalSourceInfos` method. 该方法会选择要在传递的 External Source Cookie 上发送的媒体。在操作成功或失败后，会调用 `BindPlayingIdToExternalSources` 方法，以将所有选定媒体与所发送 Event 的 Playing ID 绑定。同样，在 Event 完成播放时，会调用 `OnEndOfEvent` 方法。藉此，告知 External Source Manager 该 Playing ID 已不再使用相应媒体。

最后，`Cook` 方法支持对 External Source 媒体进行打包。在对使用 External Source 的 Event 进行打包时，会针对每个 External Source 调用 `Cook` 方法。在调用此方法时，Simple External Source Manager 会将所有媒体文件暂存到其 [Media Info Table](using_features_simpleexternalsourcemanager.html#using_features_simpleexternalsourcemanager_mediainfotable) 中以供打包。此操作只需执行一次，在此之后会设置标记。后续再调用 `Cook` 将不再执行任何操作。

|  |  |
| --- | --- |
|  | **注記：** 若直接通过 WwiseSoundEngine API 来随 External Source 一起发送 Event，请确保在适当时机实现 External Source Manager 的 `PrepareExternalSourceInfos`、`BindPlayingIdToExternalSources` 和 `OnEndOfEvent`。Otherwise, if you switch the media an External Source uses while it is playing, the previous media might be unloaded prematurely, which could cause the sound engine to crash. 在较低层级，您也可以覆盖 I/O Hook 并自行管理文件。 |

section using\_features\_simpleexternalsourcemanager\_updating 更新 Data Table

在修改磁盘上的 Data Table 并打开 Unreal Editor 时，会对其内容进行重新解析。在此之后，将卸载并重新加载所加载的全部 Wwise Event 素材。这种粗暴的方法可确保正确更新 External Source Manager 的状态。而且，实现起来也最为简单。

# External Source Manager Blueprint 函数

To update the mapping between External Sources and media, use one of the Blueprint functions to set External Source media.

![](../../../../images/external_source_manager_blueprints.png)

您可以根据个人偏好使用以下三个 Blueprint 函数来按名称或 ID 指定媒体：

- **SetExternalSourceMediaById**：使用 External Source 名称指定 External Source，并使用 `MediaID` 指定媒体。
- **SetExternalSourceMediaByName**：使用 External Source 名称指定 External Source，并使用 [Media Info Table](using_features_simpleexternalsourcemanager.html#using_features_simpleexternalsourcemanager_mediainfotable) 中的 `MediaName` 指定媒体。
- **SetExternalSourceMediaWithIds**：使用 External Source `Cookie` 指定 External Source，并使用 `MediaID` 指定媒体。

When you set an External Source media with strings, the `Cookie` is determined by a hash of the name string. 通过查询解析 **Media Info Table** 时填充的映射中的媒体名称检索 `MediaID`。

|  |  |
| --- | --- |
|  | **注記：** Blueprint 仅可使用有符号短整数。为了规避这一限制，我们使用了 `FAkUniqueID` 变量来设置 External Source Cookie 值。 |

# Using the External Source Manager API

开发者可采用两种方式来通过代码设置 External Source：调用前面章节中所述的 Blueprint 函数，或者检索 External Source Manager 实例并直接调用其方法。Wwise Simple External Source Manager 中的大多数方法都是虚拟的，因此开发者可在新的模块中对此管理器进行扩展以使用自己的数据结构和逻辑来追踪媒体并与 External Source 配对。

# Limitations

Simple External Source Manager 设计的主要限制是 [Media Info Table](using_features_simpleexternalsourcemanager.html#using_features_simpleexternalsourcemanager_mediainfotable) 对跨平台游戏来说不够灵活。不同的平台使用不同的编解码器对媒体进行解码，但 Media Info Table 的结构无法提供相应支持。其中一种潜在解决方案是在对管理器进行扩展时创建特定于平台的 Media Info Table 并根据构建目标对正确的 Media Info Table 进行打包。

When streaming, External Sources have more limitations than internally packaged media. Zero latency is not possible with External Sources, and the prefetched data is only provided to the sound engine when it is requested for playback. There is a playback delay between the initial PostEvent and the actual sample processing, which would occur with any media that do not have zero latency.