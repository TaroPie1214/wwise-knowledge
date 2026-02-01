# Room 和 Portal API 配置

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Room 和 Portal API 配置

# 创建 Room 和 Portal

您需要根据地图或关卡的几何构造使用 `AK::SpatialAudio::SetRoom` 和 `AK::SpatialAudio::SetPortal` 创建 Room 和 Portal。在运行时，可使用相同 ID 再次调用这些函数，从而更改 Room 和 Portal 相关设置。然后，游戏会针对每个发声体和听者调用 `AK::SpatialAudio::SetGameObjectInRoom` ，进而将两者所在房间告知 Spatial Audio。从 Spatial Audio 的角度来说，Room 并没有固定的位置、形状或尺寸。因此，它们可以是任何形状。不过，为了确定对象所在 Room，游戏引擎需要执行几何包含关系检测。

|  |  |
| --- | --- |
|  | **警告:** 注意，请谨慎设置 Room ID（房间 ID）。它们的取值范围与游戏对象相同。因此，假如某个 ID 已经用于游戏对象，切勿将其重复用作 Room ID。 |

|  |  |
| --- | --- |
|  | **警告:** Spatial Audio 会在后台针对每个 Room 将游戏对象注册到 Wwise。用户可以针对此游戏对象发送 Event 来触发环境声/房间底噪，但不要尝试在调用 `AK::SoundEngine` 时修改该对象的位置或 Game-defined 发送。 |

`AkRoomParams::ReverbAuxBus` 是最重要的 Room 设置，可在发声体位于该 Room 内时告知 Spatial Audio 应发送至哪条辅助总线。其他设置将在下文部分探讨（参见“ [在 Wwise 中设置 Room Auxiliary Bus](spatial_audio_roomsportals_wwisesetup.html#spatial_audio_roomsportals_using3dreverbs) ”和“ [透射](spatial_audio_roomsportals_apioverview.html#spatial_audio_roomsportals_modelingsoundpropagationfromotherrooms_transmission) ”部分）。

Portal 代表两个 Room 之间的开口。与 Room 相反，Portal 对应有位置和尺寸。因此，Spatial Audio 可自行执行几何包含关系检测。Portal 尺寸由 Portal 设置 `AkPortalParams::Extent` 给定。Spatial Audio 会使用宽度和高度（X 和 Y）计算衍射和散布，同时使用深度 (Z) 定义 Spatial Audio 在哪个区域内精确操控辅助发送电平、Room 对象方位及 Spread（用于 3D Spatialization），进而在两个相连 Room 之间应用平滑过渡。有关更多详细信息，请参见“ [在 Wwise 中设置 Room Auxiliary Bus](spatial_audio_roomsportals_wwisesetup.html#spatial_audio_roomsportals_using3dreverbs) ”和“ [声音传播特性概要](spatial_audio_roomsportals_apioverview.html#spatial_audio_roomsportals_summary) ”部分。另外，还可使用 `AkPortalParams::bEnabled` 设置将 Portal 设为启用（打开）或禁用（关闭）状态。

# 针对 Room 游戏对象发送 Event

您可以针对 Room 游戏对象发送 Event 来充分利用其空间化行为。为此，可直接调用 [AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e) ，来将 Room ID 作为 AkGameObjectID 加以传递。通过调用 [AkRoomID::AsGameObjectID](struct_ak_room_i_d_abe791f0510a62ba13d02ca5e35d3b4eb.html#abe791f0510a62ba13d02ca5e35d3b4eb) ，可将 Room ID 安全地转换为 AkGameObjectID。若要将 Room 用于发送 Event，则须告知 Spatial Audio 不要在没有使用 Room 游戏对象时将其注销。为此，请确保将 [AkRoomParams::RoomGameObj\_KeepRegistered](struct_ak_room_params_abd3091429f5aaa78b09cd2984861be6b.html#abd3091429f5aaa78b09cd2984861be6b) 设为 true。

另外，在使用房间底噪时，最好将该游戏对象发送到其自己的 Room Auxiliary Bus。为此，可将大于零的值传给 [AkRoomParams::RoomGameObj\_AuxSendLevelToSelf](struct_ak_room_params_a07f3e05103b351f449673dfff361aa71.html#a07f3e05103b351f449673dfff361aa71) 。

# 设置 Room 几何构造

通过将 Geometry Instance 与 Room 关联可达到以下目的：

- 计算 Room 的边界框，进而据此计算 Room 的透射路径的位置和散布。
- 由 Spatial Audio 确定各个 Game Object 所在的 Room。在必要时，客户还可使用 `AK::SpatialAudio::SetGameObjectInRoom` 来实现这一目的。
- 根据各个表面的透射损失系数准确指定透射损失值。
- 在 Game Object 3D Viewer 内显示 Room。
- 若将 `AkGeometryInstanceParams::UseForReflectionAndDiffraction` 设为 true，还可选择使用 Room 的墙壁来做反射和衍射模拟。

用户可选择是否设置 Room 几何构造（最好设置）。在没有 Room 几何构造的情况下，Game Object 3D Viewer 中不会显示 Room。此时，Spatial Audio 通过计算将所有关联 Portal 囊括在内的边界框，来估算 Room 的边界以应用 Room 透射。有关 Room 透射的详细信息，请参阅 [Transmission of Room Tones and a Room's Diffuse Field](spatial_audio_roomsportals_apioverview.html#spatial_audio_roomsportals_modelingsoundpropagationfromotherrooms_roomtransmission) 章节。

Spatial Audio 会使用 Room 几何构造来执行几何包含关系检测以确定各个 Game Object 所在的 Room。若需要特定类型的几何包含关系检测，则可由客户使用 `AK::SpatialAudio::SetGameObjectInRoom` 来执行这一任务。不过，对于指定为 Reverb Zone 的 Room，必须设置几何构造。这样 Spatial Audio 才能确定 Game Object 是否处在 Reverb Zone 的过渡区之内（参见 [Reverb Zone 过渡区](spatial_audio_roomsportals_reverbzones.html#spatial_audio_roomsportals_reverbzones_transition_regions) 章节）。

若要将几何构造与 Room 关联，请先使用 [AK::SpatialAudio::SetGeometry](namespace_a_k_1_1_spatial_audio_a0cada36fab682ebb3005a79dd05a5640.html#a0cada36fab682ebb3005a79dd05a5640) 将几何构造传给 Wwise。在此之后，需要创建 Geometry Instance 来指派位置并对几何构造进行缩放和旋转。参见 [AK::SpatialAudio::SetGeometryInstance](namespace_a_k_1_1_spatial_audio_ac2d5e660de0cc2a323d50f44a2731fa9.html#ac2d5e660de0cc2a323d50f44a2731fa9) 章节。最后，使用代表 Room 的 Geometry Instance 的 ID 调用 [AK::SpatialAudio::SetRoom](namespace_a_k_1_1_spatial_audio_ab991cec1e8c9f4d2721fea2d37b285c8.html#ab991cec1e8c9f4d2721fea2d37b285c8) ，来填写 [AkRoomParams::GeometryInstanceID](struct_ak_room_params_ac63a7f55f7bf863dde9af7e3e3a69758.html#ac63a7f55f7bf863dde9af7e3e3a69758) 字段。Spatial Audio 假定之前或之后有对 [AK::SpatialAudio::SetGeometryInstance](namespace_a_k_1_1_spatial_audio_ac2d5e660de0cc2a323d50f44a2731fa9.html#ac2d5e660de0cc2a323d50f44a2731fa9) 的对应调用。不过，[AK::SpatialAudio::SetRoom](namespace_a_k_1_1_spatial_audio_ab991cec1e8c9f4d2721fea2d37b285c8.html#ab991cec1e8c9f4d2721fea2d37b285c8) 和 [AK::SpatialAudio::SetGeometryInstance](namespace_a_k_1_1_spatial_audio_ac2d5e660de0cc2a323d50f44a2731fa9.html#ac2d5e660de0cc2a323d50f44a2731fa9) 的调用顺序无关紧要。

|  |  |
| --- | --- |
|  | **备注:** 若 Room 仅使用 Geometry Instance 实现上述目的，而不利用其计算反射和衍射，请将 `AkGeometryInstanceParams::UseForReflectionAndDiffraction` 设为 false。 |

有关如何在 Spatial Audio 中定义几何构造的信息，请参阅 [Geometry](spatial_audio_apigeometry.html) 章节。

|  |  |
| --- | --- |
|  | **备注:** 若仅使用 Geometry Set 描述 Room，而不利用其计算反射和衍射，请务必将 `AkGeometryParams::EnableTriangles` 设为 false。 |

# 具有多个位置的发声体

在使用 `AK::SoundEngine::SetMultiplePositions` 时，Spatial Audio 会针对传给 API 的各个声音位置执行包括反射、衍射和透射在内的各种计算。

在针对采用 Room 发送的游戏对象使用 `AK::SoundEngine::SetMultiplePositions` 时要注意，在某一特定时刻只能将给定的游戏对象指派给一个 Room（使用 `AK::SpatialAudio::SetGameObjectInRoom` ）。之所以存在该限制，是因为声音引擎内的所有声音位置必须使用相同的辅助发送配置。

所有从发声体位置开始计算的声音路径都是相对于某个特定 Room 而言的。如果声音位置位于游戏定义的 Room 边界之外（由 `AK::SpatialAudio::SetGameObjectInRoom` 决定），那么生成的声音路径就很可能是错误的。

在游戏对象穿过 Portal 的情况下，Spatial Audio 会对传给 `AK::SoundEngine::SetMultiplePositions` 的所有声音位置取平均数，并据此来计算两个 Room 之间的交叉淡变。

为此，建议游戏也使用声音位置的平均数来对 Room 实施几何包含关系检测，并将生成的 Room ID 传给 `AK::SpatialAudio::SetGameObjectInRoom` 。

# Room 和 Portal Integration 示例

Integration Demo 示例（*SDK/samples/IntegrationDemo* 中）设有演示页面，并包含有关如何使用 API 的说明。请转至 Demo Positioning > Spatial Audio: Portals（演示定位 > Spatial Audio: 门户）。