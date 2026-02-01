# Blueprint 函数

|  |
| --- |
| Wwise Unreal Integration Documentation |

Blueprint 函数

一些 Wwise 的全局函数是对脚本开放的，其中大部分会对参数进行换算并将其传给对应的 Wwise API。Audiokinetic 类别中提供以下函数。

# Add Output

Adds an output to the sound engine. Use this to add controller-attached headphones, controller speakers, motion devices, and so on. For more information, refer to [AddOutput](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a15ab79f954a307902f529d8ccde8ad48.html).

# Cancel Event Callback

取消提供给 `PostEvent` 的回调事件。在执行此节点后，将不再调用 Blueprint Event。

# Get Ak Audio Type User Data

从给定素材返回指定类型的用户数据。

# (Deprecated) Get Ak Component

获取给定组件绑定和控制的 [AkComponent](pg_features_objects_components.html#features_akcomponent) 。如需详细了解 `AkComponent` 上可用的方法，请参阅 [AkComponent Blueprint 函数](features_blueprintcomponent.html) 章节。

# Get or Create Ak Component (replaces Get Ak Component)

获取给定组件绑定和控制的 [AkComponent](pg_features_objects_components.html#features_akcomponent) 。如需详细了解 `AkComponent` 上可用的方法，请参阅 [AkComponent Blueprint 函数](features_blueprintcomponent.html) 章节。

# Get Ak Media Asset User Data

从给定媒体素材返回指定类型的用户数据。

# Get RTPC Value

获取 Game Parameter 的值，可以选择指向给定 Actor 的根组件。

# Get Speaker Angles

获取指定设备的扬声器角度。有关详细信息，请参阅 [GetSpeakerAngles](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a02ad46cabd64c04e8be198bfdc44be6b.html)。

# Is Editor

若正在运行的应用程序为 Editor，则返回 true，否则返回 false。

# Is Game

若可从 WorldContextObject 参数获取 World 且其 WorldType 为 Game、GamePreview 或 Play-In-Editor，则返回 true，否则返回 false。

# Post Event At Location

在指定位置发送 Wwise Event。这是一个针对没有对应 [AkComponent](pg_features_objects_components.html#features_akcomponent) 的临时 Wwise Game Object 创建的一次性声音。

# Post Event At Location Async

在指定位置发送 Wwise Event。异步版本会等到加载媒体之后再发送 Event。这是一个针对没有对应 [AkComponent](pg_features_objects_components.html#features_akcomponent) 的临时 Wwise Game Object 创建的一次性声音。

# Remove Output

Removes one output added through `AK::SoundEngine::AddOutput`. If a listener was associated with the device, we recommend that you unregister the listener before you call RemoveOutput so that Game Object/Listener routing is properly updated according to your game scenario. For more information, refer to [RemoveOutput](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a0932ed2a3669258ecc3bbe6448314020.html).

# 重置 RTPC 值

将 Game Parameter 的值重置为 Wwise 工程中指定的默认值；可设为全局作用域或游戏对象作用域，还可选择指向给定 Actor 的根组件。若未指定 Actor 或将其保留为空，则设置全局 Game Parameter 值。若未提供 `RTPCValue` ，则使用 RTPC 参数。否则，予以忽略。

# Set Bus Config

为指定总线强制设置声道配置。有关详细信息，请参阅 [SetBusConfig](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_aa4da48bc7fe7adc10f42272f62fd33fe.html)。

# Set Multiple Channel Emitter Positions

为单个游戏对象设置多个位置，并允许灵活指派输入声道。

参数：

- `GameObjectAkComponent`：要设置位置的游戏对象的 AkComponent。
- `ChannelMasks`：一组要应用于各个位置的声道掩码。
- `Positions`：要应用的一组 Transform。
- `MultiPositionType`：Position Type。

# Set Multiple Positions

为单个游戏对象设置多个位置。不过，只需占用一个声部的资源就可模拟多个声源。您可以使用此函数来模拟墙壁开口、区域声音或在同一区域发出相同声音的多个对象。调用只有一个位置的 `SetMultiplePositions()` 跟调用 `SetPosition()` 是一样的。

参数：

- `GameObjectAkComponent`：要设置位置的游戏对象的 AkComponent。
- `Positions`：要应用的一组 Transform。
- `MultiPositionType`：Position Type。For more information on the different position types, refer to [MultiPositionType](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a363d76a23339510f845da6bda4b95580.html).

# Set Multiple Speaker Emitter Positions

为单个游戏对象设置多个位置，并允许灵活指派输入扬声器。

参数：

- `GameObjectAkComponent`：要设置位置的游戏对象的 AkComponent。
- `SpeakerMasks`：一组要应用于各个位置的扬声器掩码。
- `Positions`：要应用的一组 Transform。
- `MultiPositionType`：Position Type。

# Set Panning Rule

为指定输出设置声像摆位规则。您可以在初始化声音引擎后随时进行更改。有关详细信息，请参阅 [SetPanningRule](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a3e61f70b39d53dd7b8350f2696d9c59e.html)。

# Set RTPC Value

设置 Game Parameter 的值，可以选择指向给定 Actor 的根组件。若未指定 Actor 或将其保留为空，则设置全局 Game Parameter 值。

# Set Speaker Angles

为指定设备设置扬声器角度。For more information, refer to [SetSpeakerAngles](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_afaf319902f00bbf38fbff9129086d912.html).

# Set State

针对给定 State Group 设置活跃 State。

# Spawn Ak Component at Location

在指定位置创建新的 AkComponent。在默认情况下，会在对应的 Event 播放结束后自动销毁该组件。

参数：

- `Auto Post`：控制是否在创建组件时立即发送 Event。默认值为 `false`。
- `Auto Destroy`：控制是否在针对此组件发送的第一个 Event 结束时销毁组件。默认值为 `true`。

您可以使用此 Blueprint 节点来针对一次性声音设置 Switch。为此，可禁用 `Auto Post`，并针对生成的 Ak Component 设置 Switch，然后发送 Event（如下图所示）。

![](../../../images/SpawnAkComponent_Switch.png)

# Stop All

停止播放当前播放的所有声音。

# Set Current Audio Culture

有关详细信息，请参阅 [Localizing Audio Assets](using_features_localization.html) 章节。

# Set Current Audio Culture Async

有关详细信息，请参阅 [Localizing Audio Assets](using_features_localization.html) 章节。

# 其他 Blueprint 函数

子类别中还提供其他一些函数：

- [Actor Blueprint 函数](features_blueprintactor.html)
- [Spatial Audio 对象 Blueprint 函数](features_blueprint_spatialaudio.html)
- [AkAmbientSound Blueprint 函数](features_blueprintambientsound.html)
- [AkComponent Blueprint 函数](features_blueprintcomponent.html)
- [AkAudioInputComponent Blueprint 函数](features_blueprintinputcomponent.html)
- [SoundBank Blueprint 函数](features_blueprintsoundbanks.html)
- [Debug Blueprint 函数](features_blueprintdebug.html)
- [在 Blueprint 中使用回调](features_blueprintcallback.html)