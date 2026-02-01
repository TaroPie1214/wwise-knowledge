# Wwise Unreal 组件

|  |
| --- |
| Wwise Unreal Integration Documentation |

Wwise Unreal 组件

### 目录

- [AkLateReverbComponent](#features_aklatereverbcomponent)
- [AkComponent](#features_akcomponent)
- [AkAudioInputComponent](#features_akaudioinputcomponent)

# AkLateReverbComponent

You can add this component to any `UPrimitiveComponent` to create a reverb area from that Primitive Component. 若要获得混响效果，可将 Wwise Auxiliary Bus 指派给组件，并把所有进入此 Volume 的 `AkComponent` 发送到关联的 Wwise Auxiliary Bus。若 Volume 之间存在重叠，则使用 `Priority` 属性来决定将目标 `AkComponent` 发送到哪条 Auxiliary Bus。在进入/离开 `AkReverbVolume` 时，会向 Auxiliary Bus 的电平应用即时淡入/淡出效果。若 Actor 上绑定有活跃的 Ak Late Reverb 组件，而且还带有 [AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent) ，则将禁用 Late Reverb 组件，并由 [AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent) 处理混响，同时使用 Spatial Audio 引擎来渲染效果。

有关混响参数的信息会显示在绑定有 Ak Late Reverb 组件的对象上。您可以在 Wwise Integration Settings 中的 Viewports - Show Reverb Info 下或通过 Unreal Level Editor Viewport 菜单来启用或禁用该文本信息。

![](../../../../images/ViewportReverbInfo.png)

在 Level Editor Viewport 菜单中显示混响信息

属性：

- **Enable Late Reverb**：启用或禁用此组件。
- **Send Level**：与 Wwise Auxiliary Bus 关联的最大发送电平。
- **Fade Rate**：进入/离开当前 Late Reverb 组件时的 Send Level 淡入/淡出速率（单位为百分比每秒）。比如，若值为 0.2，则淡变时间为 5 秒。
- **Priority**：Late Reverb 组件的应用顺序。若 Volume 之间存在重叠，则仅选择优先级最高的 Late Reverb 组件（可在 Unreal Editor Project Settings 的 **Wwise > Integration Settings** 下配置同时可有多少个 Late Reverb 组件）。若两个或多个重叠的 Late Reverb 组件拥有相同的优先级，则无法预测会先应用哪个 Late Reverb 组件。
- **Auto Assign Aux Bus**：依据体积和表面积来估算父级 Primitive 组件产生的混响衰减时间，以此来自动为此 Late Reverb 组件指派 Aux Bus。此衰减值用于通过 Integration Settings 中的 [Automatically Assigning a Reverb Aux Bus](features_editor_reverb_estimation.html#features_editor_reverb_estimation_aux_bus_map) 来选择 Aux Bus。该项默认设为启用状态。
- **Aux Bus**：指派给此 Volume 的 [UAkAuxBus](pg_features_objects_assets.html#features_objects_classes_UAkAuxBus) 。在 Wwise 工程中，此 Aux Bus 会启用游戏定义的辅助发送。若要结合 [AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent) 和 [AkPortalComponent](pg_features_spatialaudio.html#features_objects_akportalcomponent) 使用 Late Reverb，则还须针对 Positioning 启用 **Listener Relative Routing** 并指派 3D Spatialization。
- **Environment Decay Estimate**：混响环境的 T60 估值（声压级降低 60 dB 所需的时间），基于与 Late Reverb 绑定的 Primitive 组件。此 T60 值可用于通过 Integration Settings 中的 [Automatically Assigning a Reverb Aux Bus](features_editor_reverb_estimation.html#features_editor_reverb_estimation_aux_bus_map) 来自动指派 Aux Bus，并驱动 "Decay Estimate" RTPC（Integration Settings 中的 [Driving Reverb RTPCs](features_editor_reverb_estimation.html#features_editor_reverb_estimation_rtpcs) ）。
- **HFDamping**：环境产生的高频阻尼估值，基于关联的 [AkGeometryComponent](pg_features_spatialaudio.html#features_objects_akgeometrycomponent) 或 [AkSurfaceReflectorSetComponent](pg_features_spatialaudio.html#features_objects_aksurfacereflectorset) （如所属 Actor 为 Volume）。要想估算 HFDamping，必须通过 AssociateAkTextureSetComponent 函数将 Geometry 组件与此 Reverb 组件关联。若该 Late Reverb 组件包含同级 Geometry 组件或 Surface Reflector Set 组件，则会自动与之进行关联，而无需调用 AssociateAkTextureSetComponent 函数。若使用 AssociateAkTextureSetComponent，则 HFDamping 值只有在播放时才是准确的。若值等于 0.0，则表示所有频率的阻尼相同。若值大于 0.0，则表示高频的阻尼大于低频。若值小于 0.0，则表示低频的阻尼大于高频。此值可用于驱动 "HFDamping" RTPC（Integration Settings 中的 [Driving Reverb RTPCs](features_editor_reverb_estimation.html#features_editor_reverb_estimation_rtpcs) ）。Average absorption values are calculated using each of the textures in the collection, weighted by their corresponding surface area.
- **Time to First Reflection**：一阶反射声到达听者位置预计所需的时间，基于与 Late Reverb 绑定的 Primitive 组件。其估算基于放在父级 Primitive 组件中央的发声体和听者。此值可用于驱动 "Time To First Reflection" RTPC（Integration Settings 中的 [Driving Reverb RTPCs](features_editor_reverb_estimation.html#features_editor_reverb_estimation_rtpcs) ）。

Blueprint 函数：

- **Associate Ak Texture Set Component**：设置组件（[AkGeometryComponent](pg_features_spatialaudio.html#features_objects_akgeometrycomponent) 或 [AkSurfaceReflectorSetComponent](pg_features_spatialaudio.html#features_objects_aksurfacereflectorset) ）以用于估算 HFDamping。比如，在 Blueprint 所含 Static Mesh 组件带有 [AkGeometryComponent](pg_features_spatialaudio.html#features_objects_akgeometrycomponent) 子组件的情况下，可通过在 BeginPlay 时调用该函数来将所述 [AkGeometryComponent](pg_features_spatialaudio.html#features_objects_akgeometrycomponent) 与此 Late Reverb 组件关联。若该 Late Reverb 组件包含同级 [AkGeometryComponent](pg_features_spatialaudio.html#features_objects_akgeometrycomponent) 或 [AkSurfaceReflectorSetComponent](pg_features_spatialaudio.html#features_objects_aksurfacereflectorset) ，则会自动与之进行关联，而无需调用此函数。

|  |  |
| --- | --- |
|  | **注記：**  - Ak Late Reverb 组件必须与组件层级结构中的 `UPrimitiveComponent` 绑定。若 Ak Late Reverb 组件没有 `UPrimitiveComponent` 父对象，则日志中将显示错误，组件也会不起作用。 - 在自定义 Blueprint 类中使用 `AkLateReverbComponent` 时，建议将 Simple Collision 组件用作父对象（如 `BoxCollision` 、`SphereCollision` 或 `CapsuleCollision` 组件）。有关详细信息，请参阅 [Spatial Audio Blueprint 组件](sa_components.html) 章节。 - 只有 Late Reverb 组件包含同级 [AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent) （即 [AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent) 共用同一 Primitive 父组件），才能结合 Integration Settings 中的 [Driving Reverb RTPCs](features_editor_reverb_estimation.html#features_editor_reverb_estimation_rtpcs) 使用 Environment Decay Estimate、HFDamping 和 Time to First Reflection 值。这些 RTPC 值设在 Room ID 上。 - 在 Level Editor 中设置 Ak Late Reverb 组件时，强烈建议在 Viewport Options 中启用 **Realtime**。若禁用 Realtime，则在调节 Actor 时或在 Wwise 工程中更改 Acoustic Texture 参数时将不会更新 Reverb Parameter Estimation 值。 |

# AkComponent

The `AkComponent` acts as a proxy for a `GameObject`, and registers and unregisters its associated `AkGameObjectID` at the appropriate time.

If you look at the Unreal Integration C++ files, you can see that `UAkComponent` offers many of the same functions that receive an `AkGameObjectID` as `AK::SoundEngine`, and that `UAkGameObject` has a `GetAkGameObjectID()` function that returns a casted `this` pointer.

If you are adding functionality to an `AkAudioDevice`, for example, you can use `GetAkGameObjectID()` to obtain the `AkGameObjectID` that you need for any of the SoundEngine functions.

属性：

- **Attenuation Scaling Factor**：若 Ambient Sound 使用 Wwise 中的衰减，则可使用此属性来修改该环境声的衰减计算结果，以便模拟具有更大或更小传播区域的声音。
- **Use Reverb Volumes**：决定组件是否会受 `AAkReverbVolumes` 影响。
- Obstruction Occlusion
  - **Collision Channel**: The object collision channel to use when doing line of sight traces for obstruction/occlusion calculations. When set to 'Use Integration Settings Default', the value is taken from the DefaultOcclusionCollisionChannel in the Wwise [Integration Settings](using_initialsetup.html#initialsetup_gamesettings).
  - **Refresh Interval**: Set the time interval between obstruction/occlusion checks (direct line of sight between the listener and this game object). Obstruction is used if Spatial Audio Rooms are present in the map. Otherwise, occlusion is used. Set to 0 to disable obstruction/occlusion on this component. The obstruction/occlusion value is directly applied with [AK::SoundEngine::SetObjectObstructionAndOcclusion](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a1b3e18a25b405e55ba82de9b70cd11ba.html). When using Spatial Audio, obstruction checks are also done between portals in the same room and this game object. Only use this feature if you plan to obstruct this game object with geometry that is neither [AkSurfaceReflectorSetComponent](pg_features_spatialaudio.html#features_objects_aksurfacereflectorset) nor [AkGeometryComponent](pg_features_spatialaudio.html#features_objects_akgeometrycomponent). If not, we recommend that you disable obstruction/occlusion checks and exclusively use Spatial Audio Geometric Diffraction and Transmission.
- Spatial Audio
  - **Enable Spot Reflectors**：针对此 `AkComponent` 在 [AkSpotReflector](pg_features_spatialaudio.html#features_akspotreflector) 上启用反射。
  - Radial Emitter
    - **Outer Radius**：将字段设为所需外径大小。将把指定的数值直接发送到 Spatial Audio [AK:SpatialAudio::SetGameObjectRadius()](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_a8c2e8f50769b6ae29dcbcb636e9c33f2.html) 调用而不进行任何转换。在选中 Actor 时，将围绕该游戏对象所在位置绘制黄色球体框线以直观地反映数值大小。
    - **Inner Radius**：将字段设为所需内径大小。该值须小于或等于外径大小。将把指定的数值直接发送到 Spatial Audio [AK:SpatialAudio::SetGameObjectRadius()](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_a8c2e8f50769b6ae29dcbcb636e9c33f2.html) 调用而不进行任何转换。在选中 Actor 时，将围绕该游戏对象所在位置绘制黄色球体框线以直观地反映数值大小。
  - Reflect
    - **Early Reflection Aux Bus**：为当前游戏对象设置早期反射辅助总线。该组件会依据所选辅助总线调用 [AK::SpatialAudio::SetEarlyReflectionsAuxSend()](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_af9357c33f3ea4f9551b0e169ded73c15.html)。辅助总线参数将被应用到未在设计工具中指定早期反射辅助总线的游戏对象声音。针对各个声音指定的早期反射辅助总线参数在优先级上高于此处传递的值。
    - **Early Reflection Bus Send Gain**：为当前游戏对象设置早期反射发送音量。该组件会依据所指定的音量值调用 [AK:SpatialAudio::SetEarlyReflectionsVolume()](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_a691784b217ba9ccd30e6513dedb924e6.html)。该值将连同设计工具中指定的早期反射音量一并应用到游戏对象播放的所有声音。有效值为 [0, 1]。若设为 0，则针对此游戏对象禁用所有反射处理。
  - **Debug Draw** 选项：使用这些选项来直观地呈现 Spatial Audio 引擎所执行的射线投射以及投射射线所碰到的三角形。在需要调试 Spatial Audio 引擎时，这种直观呈现会很有用。每次仅可针对一个组件执行此操作。
- AkEvent
  - **Ak Audio Event**：在指示开始播放 [AkAmbientSound](pg_features_objects_actors.html#features_akambientsound) 对象时发送的 [UAkAudioEvent](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent) 。若要使用 Spatial Audio 功能，则 Event 的音效需启用游戏定义的辅助发送。

参见
:   - [AkComponent Blueprint 函数](features_blueprintcomponent.html)
    - [利用 C++ 创建 AkComponent](using_cpp.html#akcomponent_cpp).
    - [Obstruction and Occlusion SDK Documentation](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine_obsocc.html)
    - [Radial Emitters SDK Documentation](https://www.audiokinetic.com/library/edge/?source=SDK&id=spatial_audio_radial_emitters.html)
    - [Reflect Wwise Help](https://www.audiokinetic.com/library/edge/?source=Help&id=wwise_reflect_plug_in_effect)

# AkAudioInputComponent

`AkAudioInputComponent` 由 `AkComponent` 派生，代表音频输入实例。

Blueprint 函数：

- **Post Associated Audio Input Event**：开始播放指定的 Event，并注册对应的回调。