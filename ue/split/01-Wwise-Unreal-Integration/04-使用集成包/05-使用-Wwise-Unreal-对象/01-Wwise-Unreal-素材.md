# Wwise Unreal 素材

|  |
| --- |
| Wwise Unreal Integration Documentation |

Wwise Unreal 素材

### 目录

- [Wwise Unreal 素材](#features_objects_wwise_assets)
  - [AkGameObject](#features_objects_classes_akgameobject)
- [WwiseObjectInfo 结构](#features_objects_classes_assetinfo)
  - [FWwiseObjectInfo](#features_objects_classes_FWwiseObjectInfo)
  - [FWwiseEventInfo](#features_objects_classes_FWwiseEventInfo)
  - [FWwiseGroupValueInfo](#features_objects_classes_FWwiseGroupValueInfo)
- [为 Wwise 素材烘焙和加载的数据](#features_objects_classes_cookeddata)
- [Wwise Unreal 素材类型](#features_objects_classes_asset_types)
  - [UAkAudioType](#features_objects_classes_UAkAudioType)
  - [UAkAudioEvent](#features_objects_classes_UAkAudioEvent)
  - [UAkInitBank](#features_objects_classes_UAkInitBank)
  - [UAkAuxBus](#features_objects_classes_UAkAuxBus)
  - [UAkEffectShareSet](#features_objects_classes_UAkEffectShareSet)
  - [UAkGroupValue](#features_objects_classes_UAkGroupValue)
  - [UAkStateValue](#features_objects_classes_UAkStateValue)
  - [UAkSwitchValue](#features_objects_classes_UAkSwitchValue)
  - [UAkRtpc](#features_objects_classes_UAkRtpc)
  - [UAkTrigger](#features_objects_classes_UAkTrigger)
  - [UAkAcousticTexture](#features_objects_classes_UAkAcousticTexture)
  - [UAkAudioDeviceShareSet](#features_objects_classes_UAkAudioDeviceShareSet)
  - [弃用的素材和数据类型](#features_objects_classes_deprecated)
- [在 Unreal 中查看素材之间的关系](#using_features_ref_viewer)

# Wwise Unreal 素材

Unreal Integration 需要用户创建代表 Wwise 工程中对应对象的素材。You can create these assets through [Using the Drag-and-Drop Feature](features_editor_wwise_browser.html#features_editor_dnd) drag-and-drop from the Wwise Browser, or from the right-click menu in the Content Browser. 通过拖放创建的素材自动包含将其与其代表的 Wwise 对象关联所需的信息（GUID、ShortID、Name）。在通过 Content Browser 创建素材时，必须手动添加这些信息。无论采用哪种方式，随后都可对素材进行编辑来指向新的或不同的 Wwise 对象。如需详细了解使用这些素材类型的 Blueprint 函数，请参阅 [Blueprint 函数](features_blueprint.html) 章节。

|  |  |
| --- | --- |
|  | **注記：** 在地图或 Blueprint 中直接引用素材时，会将素材所需的全部 Wwise 资源（.bnk 和 .wem 文件）自动打包到游戏中。不过，若选择仅通过代码来加载这些素材，则须确保对其进行正确打包。 |

下表列出了具有对应 Unreal 素材类的 Wwise 对象类型。

Wwise Unreal 对象

| Wwise 对象类型 | Unreal 素材类 | 描述 |
| Acoustic Texture | [UAkAcousticTexture](pg_features_objects_assets.html#features_objects_classes_UAkAcousticTexture) | 用于 ShortId 的封装器，可将 ShortId 标识给 SoundEngine。 |
| RTPC | [UAkRtpc](pg_features_objects_assets.html#features_objects_classes_UAkRtpc) |
| Trigger | [UAkTrigger](pg_features_objects_assets.html#features_objects_classes_UAkTrigger) |
| Audio Device ShareSet | [UAkAudioDeviceShareSet](pg_features_objects_assets.html#features_objects_classes_UAkAudioDeviceShareSet) |
| Auxiliary Bus | [UAkAuxBus](pg_features_objects_assets.html#features_objects_classes_UAkAuxBus) | Contains the ShortId and also ensures that the required media and SoundBank resources are loaded into memory and packaged in the built game. |
| Event | [UAkAudioEvent](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent) |
| Effect ShareSet | [UAkEffectShareSet](pg_features_objects_assets.html#features_objects_classes_UAkEffectShareSet) | 用于 ShortId 的封装器，确保在游戏内动态设置 Effect ShareSet。确保将所需的媒体和 SoundBank 资源加载到内存中并打包到构建好的游戏中。 |
| Init Bank | [UAkInitBank](pg_features_objects_assets.html#features_objects_classes_UAkInitBank) | 确保将 Init Bank 文件打包到游戏中并在其他 SoundBank 之前予以加载。 |
| State Value | [UAkStateValue](pg_features_objects_assets.html#features_objects_classes_UAkStateValue) | 用于自身 ShortId 及父组 ShortId 的封装器。确保 [UAkAudioEvent](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent) 素材中的 [FWwiseEventInfo](pg_features_objects_assets.html#features_objects_classes_FWwiseEventInfo) 结构的高级设置 **SwitchContainerLoading::LoadOnReference** 能够正常运行。若启用，在加载和卸载这些 Switch Group 值素材时，会动态加载 Switch Container 媒体资源。有关详细信息，请参阅 [Optimizing Memory Usage with Reference-Loaded Switch Containers](using_features_reference_load_switch_container.html) 章节。 |
| Switch Value | [UAkSwitchValue](pg_features_objects_assets.html#features_objects_classes_UAkSwitchValue) |

## AkGameObject

The AkGameObject acts as a bridge between Unreal game objects and Wwise objects, and is required for Unreal game objects that send data to Wwise. You can use the AkGameObject to play Events, track the position of sound objects in Unreal, and use it for game syncs such as Switches, RTPCs, and environmental values.

AkGameObject is also the base class for Wwise components such as [AkComponent](pg_features_objects_components.html#features_akcomponent) and [AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent).

# WwiseObjectInfo 结构

Wwise Unreal 素材包含 FWwiseObjectInfo 信息结构，其指向 Wwise 工程中的唯一对象。有些素材类使用带有附加字段的子类。这些字段会影响相应的行为（比如如何准备数据以供加载）。在保存素材时，会在素材中将此结构序列化；在烘焙并用于打包好的构建版本时，会弃用相应的数据。在烘焙过程中，会将该结构传给 WwiseResourceCooker 以便获取已烘焙数据。这些数据在打包好的素材中序列化。有关 CookedData 结构的详细信息，请参阅 [为 Wwise 素材烘焙和加载的数据](pg_features_objects_assets.html#features_objects_classes_cookeddata) 章节。

## FWwiseObjectInfo

基础信息结构。在加载并烘焙编辑器中的素材时会使用此结构来查询 WwiseDatabase，以便获取 CookedData 结构并藉此将素材所需的全部资源（.bnk 和 .wem 文件）加载到内存中。

属性：

- **WwiseGuid**：该 GUID 用于识别 Wwise 工程中的此素材。
- **WwiseShortId**：该 32 位整数用于代表 Wwise SoundEngine 中的素材。
- **WwiseName**：该字符串代表 Wwise 工程中的素材的名称。它不需要跟对应 Unreal 素材的名称匹配。不过，偶尔会出现在素材被序列化时 WwiseObjectInfo 中的所有标识字段全部为空的情况。这时，会更新 **WwiseName** 字段并使之与 Unreal 素材的名称匹配。
- **HardCodedSoundBankShortId**：该 32 位整数用于识别必须将素材加载为依赖项的 SoundBank。比如，若有个 Event 被包含在了多个 SoundBank 中，则可指定要将哪个 SoundBank 打包并随素材一起加载。若未设置该字段，则一起加载包含 Wwise 对象的所有 SoundBank。

|  |  |
| --- | --- |
|  | **注記：** **HardCodedSoundBankShortId** 属性只会影响 [UAkAudioEvent](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent) 、[UAkAuxBus](pg_features_objects_assets.html#features_objects_classes_UAkAuxBus) 和 [UAkEffectShareSet](pg_features_objects_assets.html#features_objects_classes_UAkEffectShareSet) 素材，因为只有这些素材需要 SoundBank 资源。 |

在 Wwise Database 中执行搜索时会按照以下顺序设定字段的优先级：WwiseGuid -> WwiseShortId -> WwiseName（由高到低）。比如，若 WwiseGuid 无效，则使用 WwiseShortId 来搜索对象。

若在 Unreal 素材检视器中修改了 WwiseObjectInfo 中用于识别 Wwise 对象的 WwiseShortId、WwiseGuid 或 WwiseName 属性，则会搜索 Wwise Project Database 并查找与新属性的值匹配的对象并相应地更新其他两个字段。

FWwiseObjectInfo 的子类包含用于正确加载数据的附加信息。若在检视器中对 WwiseObjectInfo 的属性或子类的字段实施更改，还会重新加载素材的 Wwise 资源。

## FWwiseEventInfo

UAkAudioEvent 素材所用的 [FWwiseObjectInfo](pg_features_objects_assets.html#features_objects_classes_FWwiseObjectInfo) 的子类。FWwiseEventInfo 包含方便用户自定义 Event 素材加载和销毁行为的附加选项。

附加属性：

- **SwitchContainerLoading**：若设为 AlwaysLoad，则随 Event 一起加载其所用的全部 Switch Container 媒体；若设为 LoadOnReference，则仅在将 Switch 或 Switch Group 值加载到内存中时加载这些媒体。有关详细信息，请参阅 [Optimizing Memory Usage with Reference-Loaded Switch Containers](using_features_reference_load_switch_container.html) 章节。
- **DestroyOptions**：若设为 StopEventOnDestroy，则在销毁 Event 时停止播放 Event；若设为 WaitForEventEnd，则等待 Event 停止播放。

## FWwiseGroupValueInfo

Switch Value 和 State Value 素材所用的 [FWwiseObjectInfo](pg_features_objects_assets.html#features_objects_classes_FWwiseObjectInfo) 的子类。除此之外，FWwiseGroupValueInfo 还包含 State Group 或 Switch Group 的 ShortId。

附加属性：

- **GroupShortId**：该 32 位整数用于识别包含素材的 Group。

# 为 Wwise 素材烘焙和加载的数据

Wwise 素材包含相应的 CookedData 结构。该结构用于加载其所需的资源（.bnk 和 .wem 文件），并监控其对其他 Wwise 对象的依赖关系（比如，对于播放 Switch Container 的 Event，使用哪些 Switch）。WwiseResourceCooker 模块提供函数来接收 [FWwiseObjectInfo](pg_features_objects_assets.html#features_objects_classes_FWwiseObjectInfo) 结构并为该 Wwise 对象返回 CookedData 结构。另外，还提供函数来获取 [FWwiseObjectInfo](pg_features_objects_assets.html#features_objects_classes_FWwiseObjectInfo) 结构并暂存所需资源以供打包。

在编辑器中执行操作时，只会临时使用 CookedData 结构，而不会将其序列化为素材。这样可以避免更改数据或更改 Wwise 对象之间的关系，以免不必要地将对应的 Unreal 素材设为未同步状态。在打包过程中，会在打包好的素材中将 CookedData 序列化并弃用 Wwise Info 结构。

WwiseResourceLoader 模块负责将素材所需的资源加载到内存中。它提供函数来接收 CookedData 结构并通过调用 WwiseFileHandler 模块中的方法来管理实际资源的加载。然后，返回对 Loaded 结构的引用。

|  |  |
| --- | --- |
|  | **注記：** [UAkRtpc](pg_features_objects_assets.html#features_objects_classes_UAkRtpc), [UAkTrigger](pg_features_objects_assets.html#features_objects_classes_UAkTrigger), [UAkAcousticTexture](pg_features_objects_assets.html#features_objects_classes_UAkAcousticTexture), and [UAkAudioDeviceShareSet](pg_features_objects_assets.html#features_objects_classes_UAkAudioDeviceShareSet) assets do not need to load additional resources. 它们不与 WwiseResourceLoader 交互，其 CookedData 结构仅包含对应的 ShortId。 |

# Wwise Unreal 素材类型

## UAkAudioType

针对所有 Unreal Wwise 素材的基类。

属性：

- **AutoLoad**：决定是否随 Unreal 素材一起自动加载 Wwise 数据（Bank 和媒体）。
- **UserData**：此项为用户数据数组。可存储 Wwise Integration 相关自定义功能的信息。比如，可使用 UserData 来存储旁白事件的字幕数据。

Blueprint 函数：

- **LoadData**：加载素材所需的资源（.bnk 和 .wem 文件）。在禁用 **AutoLoad** 时使用此函数来手动加载 Wwise 资源。多次调用该函数并不会造成安全问题，但可能会导致不必要地重新加载资源。
- **UnloadData**：卸载素材所需的资源（.bnk 和 .wem 文件）。若其他加载的素材也需要相应资源，则会等到卸载这些素材再卸载资源。

## UAkAudioEvent

Event 所用的 [UAkAudioType](pg_features_objects_assets.html#features_objects_classes_UAkAudioType) 的子类。

属性：

- **MaxAttenuationRadius**：最大衰减半径。
- **IsInfinite**：指示是否无限循环 Event 所播放的声音。
- **MinimumDuration**：Event 所播放声音的最小时长的估值。
- **MaximumDuration**：Event 所播放声音的最大时长的估值。
- **EventInfo**：此 [FWwiseEventInfo](pg_features_objects_assets.html#features_objects_classes_FWwiseEventInfo) 会填充编辑器中的 EventCookedData 属性。
- **EventCookedData**：临时使用的 FWwiseLocalizedEventCookedData。其包含由语言到语言特定 FWwiseEventCookedData 的映射关系。

|  |  |
| --- | --- |
|  | **注記：** 在编辑器中加载 AkAudioEvent 素材时填充 **EventCookedData**、**MaxAttenuationRadius**、**IsInfinite**、**MinimumDuration** 和 **MaximumDuration** 属性，并在烘焙时将其序列化为素材。Integration 使用 **MaxAttenuationRadius** 在组件观察器中显示附加信息，并使用其他三项属性在 Timeline Track 中显示 Event。 |

Unreal Content Browser 上下文菜单选项：

- **Play Event**：发送 Event。
- **Stop Event**：停止当前播放的所有 Event。

## UAkInitBank

Init Bank 所用的 [UAkAudioType](pg_features_objects_assets.html#features_objects_classes_UAkAudioType) 的子类。

- **InitBankCookedData**：临时使用的 FWwiseInitBankCookedData。

|  |  |
| --- | --- |
|  | **注記：** [UAkAudioType](pg_features_objects_assets.html#features_objects_classes_UAkAudioType) 的 **Autoload** 属性不会影响此素材类型。 |

## UAkAuxBus

[UAkAudioType](pg_features_objects_assets.html#features_objects_classes_UAkAudioType) Auxiliary Bus 的子类。

- **AuxBusInfo**：此 [FWwiseObjectInfo](pg_features_objects_assets.html#features_objects_classes_FWwiseObjectInfo) 会填充编辑器中的 AuxBusCookedData 属性。
- **AuxBusCookedData**：临时使用的 FWwiseLocalizedAuxBusCookedData。其包含由语言到语言特定 FWwiseAuxBusCookedData 的映射关系。

## UAkEffectShareSet

Effect ShareSet 所用的 [UAkAudioType](pg_features_objects_assets.html#features_objects_classes_UAkAudioType) 的子类。

- **ShareSetInfo**：此 [FWwiseObjectInfo](pg_features_objects_assets.html#features_objects_classes_FWwiseObjectInfo) 会填充编辑器中的 AuxBusCookedData 属性。
- **ShareSetCookedData**：临时使用的 FWwiseLocalizedShareSetCookedData。其包含由语言到语言特定 FWwiseShareSetCookedData 的映射关系。

## UAkGroupValue

[UAkAudioType](pg_features_objects_assets.html#features_objects_classes_UAkAudioType) 的子类和 [UAkStateValue](pg_features_objects_assets.html#features_objects_classes_UAkStateValue) 和 [UAkSwitchValue](pg_features_objects_assets.html#features_objects_classes_UAkSwitchValue) 的基类。

- **GroupValueInfo**：此 [FWwiseGroupValueInfo](pg_features_objects_assets.html#features_objects_classes_FWwiseGroupValueInfo) 会填充编辑器中的 GroupValueCookedData 属性。
- **GroupValueCookedData**：临时使用的 FWwiseGroupValueCookedData。

## UAkStateValue

State 值所用的 [UAkGroupValue](pg_features_objects_assets.html#features_objects_classes_UAkGroupValue) 的子类。

## UAkSwitchValue

Switch 值所用的 [UAkGroupValue](pg_features_objects_assets.html#features_objects_classes_UAkGroupValue) 的子类。

## UAkRtpc

RTPC / Game Parameter 所用的 [UAkAudioType](pg_features_objects_assets.html#features_objects_classes_UAkAudioType) 的子类。

- **RtpcInfo**：此 [FWwiseObjectInfo](pg_features_objects_assets.html#features_objects_classes_FWwiseObjectInfo) 会填充编辑器中的 GameParameterCookedData 属性。
- **GameParameterCookedData**：临时使用的 FWwiseGameParameterCookedData。

|  |  |
| --- | --- |
|  | **注記：** [UAkAudioType](pg_features_objects_assets.html#features_objects_classes_UAkAudioType) 的 **Autoload** 属性及 **LoadData** 和 **UnloadData** Blueprint 不会影响此素材类型。 |

## UAkTrigger

Music Trigger 所用的 [UAkAudioType](pg_features_objects_assets.html#features_objects_classes_UAkAudioType) 的子类。

- **TriggerInfo**：此 [FWwiseObjectInfo](pg_features_objects_assets.html#features_objects_classes_FWwiseObjectInfo) 会填充编辑器中的 TriggerCookedData 属性。
- **TriggerCookedData**：临时使用的 FWwiseTriggerCookedData。

|  |  |
| --- | --- |
|  | **注記：** [UAkAudioType](pg_features_objects_assets.html#features_objects_classes_UAkAudioType) 的 **Autoload** 属性及 **LoadData** 和 **UnloadData** Blueprint 不会影响此素材类型。 |

## UAkAcousticTexture

Subclass of [UAkAudioType](pg_features_objects_assets.html#features_objects_classes_UAkAudioType) to represent a Wwise Acoustic Texture. Acoustic Textures can be applied to a [AkSurfaceReflectorSetComponent](pg_features_spatialaudio.html#features_objects_aksurfacereflectorset)'s polygons or to a [AkSpotReflector](pg_features_spatialaudio.html#features_akspotreflector). They can also be associated with Unreal Physical Materials through the Geometry Surface Properties Table in the [Integration Settings](using_initialsetup.html#initialsetup_gamesettings).

- **AcousticTextureCookedData**：临时使用的 FWwiseAcousticTextureCookedData。
- **Edit Color**：此 Editor 专有属性用于定义所要使用的颜色，以便为指派有 `AkAcousticTexture` 的 [AkSurfaceReflectorSetComponent](pg_features_spatialaudio.html#features_objects_aksurfacereflectorset) 多边形着色。Edit Color 将从 Wwise 工程中的 Acoustic Texture 自动提取。若有活跃的 WAAPI 连接，则会将 Wwise 中针对 Acoustic Texture 颜色所作的更改立即应用于 `AkAcousticTexture` Edit Color。
- **AcousticTextureInfo**: [FWwiseObjectInfo](pg_features_objects_assets.html#features_objects_classes_FWwiseObjectInfo) that fills in the AcousticTextureCookedData property when in the editor.

|  |  |
| --- | --- |
|  | **注記：** [UAkAudioType](pg_features_objects_assets.html#features_objects_classes_UAkAudioType) 的 **Autoload** 属性及 **LoadData** 和 **UnloadData** Blueprint 不会影响此素材类型。 |

## UAkAudioDeviceShareSet

Subclass of [UAkAudioType](pg_features_objects_assets.html#features_objects_classes_UAkAudioType) for Audio Device.

- **AudioDeviceShareSetInfo**: [FWwiseObjectInfo](pg_features_objects_assets.html#features_objects_classes_FWwiseObjectInfo) that fills in the AudioDeviceShareSetCookedData property when in the editor.
- **AudioDeviceShareSetCookedData**: Transient FWwiseAudioDeviceShareSetCookedData.

|  |  |
| --- | --- |
|  | **注記：** [UAkAudioType](pg_features_objects_assets.html#features_objects_classes_UAkAudioType) 的 **Autoload** 属性及 **LoadData** 和 **UnloadData** Blueprint 不会影响此素材类型。 |

## 弃用的素材和数据类型

以下类和结构现在已经被弃用，其仅用于从早先工程实施迁移：

- UAkAssetData
- UAkAssetPlatformData
- UAkAudioBank
- UAkExternalMediaAsset
- UAkFolder
- UAkLocalizedMediaAsset
- UAkMediaAsset
- UAkMediaAssetData

# 在 Unreal 中查看素材之间的关系

现在通过 Unreal 引用维护 Event 和媒体之间的关系。因此，您可以使用 Unreal Reference Viewer 来查看素材之间的关系（如下图所示）。

![](../../../../images/ReferenceViewer.png)

For more information about the Unreal Reference Viewer, refer to [Reference Viewer](https://dev.epicgames.com/documentation/en-us/unreal-engine/reference-viewer-in-unreal-engine).