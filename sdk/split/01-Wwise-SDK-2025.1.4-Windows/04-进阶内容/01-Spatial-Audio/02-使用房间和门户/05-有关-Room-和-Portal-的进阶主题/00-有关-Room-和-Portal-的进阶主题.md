# 有关 Room 和 Portal 的进阶主题

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

有关 Room 和 Portal 的进阶主题

# 结合 Obstruction 和 Occlusion 使用 Room 和 Portal

在 Wwise Spatial Audio 环境下，完全利用抽象概念 Room 和 Portal 来管理其他房间的声音传播。Rooms with at least one propagation path to the listener through open Portals simulate diffraction. Additionally, rooms model sound transmission through walls. Diffraction 和 Transmission Loss 值会应用于“发声体”游戏对象。在 Wwise 设计工具中，可选择是希望这些值使用衰减曲线还是内置游戏参数来对声音实施衰减。If a sound doesn't have an attenuation instance (either custom or ShareSet), the project diffraction and transmission curves are used to attenuate the sound.

If you are using built-in game parameters to drive RTPCs, any obstruction and occlusion values set on a Portal do not affect the RTPC values. This behavior is intentional and occurs because RTPCs only provide one value per game object, but a single game object can have multiple paths through different Portals, each with different obstruction and occlusion values.

If you want to implement your own solution for obstruction (for example, one driven by game-side raycasting) in conjunction with diffraction set from Spatial Audio, the game can use the `AK::SoundEngine::SetObjectObstructionAndOcclusion` sound engine API. 若想模拟 Portal 开口的声笼效果，则游戏可使用 Spatial Audio API `AK::SpatialAudio::SetPortalObstructionAndOcclusion`。此外，还可借助 `AK::SpatialAudio::SetGameObjectToPortalObstruction` 和 `AK::SpatialAudio::SetPortalToPortalObstruction` ，将声障应用到发声体与附近 Portal、听者与附近 Portal 或一组连续 Portal 之间的声音路径上。不过无论在任何情况下，游戏都不能将 Room ID 作为游戏对象参数来调用 `AK::SoundEngine::SetObjectObstructionAndOcclusion` ，否则可能会导致未定义的行为。有关如何将房间内部声障用于 Spatial Audio 的更多详细信息，请参见“[对 Room 内的障碍物进行建模](spatial_audio_roomsportals_advancedtopics.html#spatial_audio_roomsportals_modelingsoundpropagationfromsameroom) ”部分。

如需回顾相关声学概念，请参见“[Spatial Audio 概念](spatial_audio_concepts.html) ”部分。

# 对 Room 内的障碍物进行建模

听者所在房间内的声障可使用 Geometric Diffraction 进行处理（参阅 [使用 Geometry API 模拟衍射和透射](spatial_audio_apigeometry_diffract.html) 和 [结合 Room 和 Portal 使用几何构造 API](spatial_audio_apigeometry_diffract.html#spatial_audio_api_geometry_aware_rooms) ），但它并不完全依赖 Spatial Audio Room 和 Portal。若不想通过将几何构造发送到 Spatial Audio 来执行声障计算，则须在游戏端处理同一房间内的声障。房间内声障计算中几何构造的表示、方法和规定的细节层次高度依赖于游戏引擎。游戏一般会采用不同复杂程度的射线投射法来实现这一操作。本节提供了一些有关如何结合 Room 和 Portal 在游戏端处理声障的技巧。

不过，借助 Spatial Audio Room 和 Portal，便不用针对每个发声体实施这一操作，而只需考虑听者所在房间内的发声体。这样做有它的好处，因为射线投射法一般会比 Spatial Audio 计算传播路径的算法占用更多资源。顾名思义，发声体和听者之间的房间内部声障作用发生在同一房间。在这种情况下，我们假定障碍物不会完全覆盖听者或发声体，而声音会通过房间内的反射传播到听者所在位置。我们可以通过单纯控制干声/直达信号路径进行准确建模，而不需要涉及辅助发送。也就是说，Obstruction 机制对此来说最为合适。为此，游戏应调用 `AK::SoundEngine::SetObjectObstructionAndOcclusion` 。

另外，相邻房间的 Portal 应被视为听者所在 Room 内的发声体。因此，游戏还需在听者和所在 Room 的 Portal 之间运行声障算法。然后，还要针对每个 Portal 调用 `AK::SpatialAudio::SetPortalObstructionAndOcclusion，以便向听者明确声明房间内部声障。`

# 实现复杂房间混响

游戏可结合 Spatial Audio Room 使用 `AK::SoundEngine::SetGameObjectAuxSendValues` 。这样的话，除了 Room 游戏对象的辅助总线发送（由 `AkRoomParams::ReverbAuxBus` 定义），还会添加游戏的发送。

另外，还可结合 Spatial Audio Emitter 使用 `AK::SoundEngine::SetObjectObstructionAndOcclusion` 或 `AK::SoundEngine::SetMultipleObstructionAndOcclusion` ，即便 Spatial Audio 已经使用衍射和透射。有关声障、声笼以及如何将其用于 Spatial Audio Room 和 Portal 的更多详细信息，请参见“[为其他房间的声音传播建模](spatial_audio_roomsportals_apioverview.html#spatial_audio_roomsportals_modelingsoundpropagationfromotherrooms) ”和“[对 Room 内的障碍物进行建模](spatial_audio_roomsportals_advancedtopics.html#spatial_audio_roomsportals_modelingsoundpropagationfromsameroom) ”部分。

您可以使用声音引擎 API `AK::SoundEngine::SetGameObjectAuxSendValues` 来将其他 Auxiliary Sends 添加到 Spatial Audio 所设的 Auxiliary Sends。这在设计相同房间内的复杂混响时可能会非常有用。比如，物体或地形需要应用不同的环境效果。另外，还可将 Room 对应的 `AkRoomParams::ReverbAuxBus` 保留为空 (`AK_INVALID_AUX_ID`) ，仅由游戏通过 `AK::SoundEngine::SetGameObjectAuxSendValues` 来管理发送总线。

参见
:   - [Room 和 Portal 信号模型中的传播路径](spatial_audio_roomsportals_paths.html)
    - [Geometric Room Distance on Direct Paths](spatial_audio_roomsportals_distance.html)
    - [第三人称视角和 Spatial Audio](spatial_audio_third_person.html)