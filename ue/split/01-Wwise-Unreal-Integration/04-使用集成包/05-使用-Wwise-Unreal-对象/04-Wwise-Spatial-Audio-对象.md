# Wwise Spatial Audio 对象

|  |
| --- |
| Wwise Unreal Integration Documentation |

Wwise Spatial Audio 对象

# AkSpotReflector

您可以使用 Spot Reflector Actor 来在 3D 空间中放置全指向 Spot Reflector（反射点）。Spot Reflector 适合放在半径较大的远距离对象上（如远处的大山）。

您可以使用多个选项来控制 Spot Reflector 行为。

对于启用了 **Enable Spot Reflectors** 的 [AkComponent](pg_features_objects_components.html#features_akcomponent) ，Spot Reflector 会反射其发出的全部声音。

若要确保 Spot Reflector 仅反射来自同一 Spatial Audio Room 的声音，请启用 **Same Room Only**。In this case, an [AkComponent](pg_features_objects_components.html#features_akcomponent) feeds a Spot Reflector if they are both outside Rooms or if they are both in the same Room. 您可以通过绑定有 [AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent) 的 Volume 创建 Room。

To override the Room that contains the Spot Reflector, enable **Enable Room Override** and assign a Room to **Room Override**. If you do not set a **Room Override**, the Spot Reflector is virtually placed outside Rooms.

`AkSpotReflector` 会在 BeginPlay 时通过 Spatial Audio API 调用 `AK::SpatialAudio::AddImageSource()` 。

属性：

- **Aux Bus**：带有 `AkReflect` 插件（用于早期反射 DSP）的 [UAkAuxBus](pg_features_objects_assets.html#features_objects_classes_UAkAuxBus) 。此辅助总线会启用游戏定义的辅助发送，同时启用 Listener Relative Routing，但会将 3D Spatialization 设为 **None**。
- **Acoustic Texture**: [UAkAcousticTexture](pg_features_objects_assets.html#features_objects_classes_UAkAcousticTexture) that filters sounds reflected by the image source.
- **Distance Scaling Factor**：镜像声源距离缩放系数。此数值用于根据听者所在位置调节 `sourcePosition` 矢量，进而缩放距离并保持朝向。
- **Level**：针对声源设置的游戏控制的线性电平。

# AkSurfaceReflectorSetComponent

此组件跟 [AkGeometryComponent](pg_features_spatialaudio.html#features_objects_akgeometrycomponent) 一样，但必须绑定到 AVolume Actor 上。在 BeginPlay 时，会将 Volume 启用的所有多边形发送到 Spatial Audio 引擎。

在使用 [AkSurfaceReflectorSetComponent](pg_features_spatialaudio.html#features_objects_aksurfacereflectorset) 时，确保将视口设为 **Realtime** 以正确更新相应的模型。

![](../../../../images/SATutorialViewportRealtime.png)

在 Viewport Options 中启用 Realtime

属性：

- **Enable Surface Reflector Set**：启用此组件。
- **Acoustic Surfaces**：使用这些控件来编辑与 Volume 上一个或多个表面关联的属性。在默认情况下，会将针对这些属性所作的更改应用于所选 Actor 上的所有表面。
  - **Enable Edit Surfaces/Disable Edit Surfaces**: When enabled, the Unreal Editor switches to Brush Editing mode and hides all non-selected actors in the level. 在 Edit Surfaces 模式下，可单独选中 Volume 上的一个或多个表面。这时会将针对 Acoustic Surfaces 属性所作的更改应用于选中的所有表面。各项属性之后括号中的文本会指示当前在编辑多少个表面。 In Brush Editing mode, you can change AkSpatialAudioVolume objects from rectangles into other shapes. For more information on Brush Editing, see [Geometry Brush Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine).
  - **AkAcousticTexture**: The [UAkAcousticTexture](pg_features_objects_assets.html#features_objects_classes_UAkAcousticTexture) associated with the selected faces. 系统会根据该 Acoustic Texture 所对应的 Edit Color 为这些表面着色，同时在 Game Viewport 中的表面上显示 Acoustic Texture 的名称。对于完全反射的表面，请将该项设为 None，以确保不会额外应用任何 Acoustic Texture 滤波器。
  - **Transmission Loss**：指示有多少声音穿透了表面。有效范围为 0.0 - 1.0。若值为 0.0，则表示声音全部穿透了表面。若值为 1.0，则表示声音被表面完全阻挡。
  - **Enable Surface**：指示是否将所选表面发送到 Spatial Audio 引擎。对于被禁用的表面，不会显示任何 Acoustic Texture 名称或 Transmission Loss 值。
- **Geometry Settings**：
  - **Enable Diffraction**：针对此 Geometry 启用几何衍射。
  - **Enable Diffraction on Boundary Edges**：针对此 Geometry 在边界边缘启用几何衍射。其中，Boundary Edge 代表仅连有一个三角形的边缘。边界边缘可能有用也可能没用（取决于几何构造的具体形状），因此最好减少所要处理的衍射边缘总数。
  - **Bypass Portal Subtraction**: Prevents Portal bounding boxes from being subtracted from this geometry.
  - **Solid**: Applies transmission loss once for each time a transmission path enters and exits its volume, using the max transmission loss between each hit surface. A non-solid geometry instance is one where each surface is infinitely thin, applying transmission loss at each surface. This option has no effect if the Transmission Operation is set to Max.
  - **Associated Room**: (Deprecated) Associate this AkSurfaceReflectorSetComponent with a Room. This property is deprecated and will be removed in a future version. We recommend not using it by leaving it set to **None**. Associating an AkSurfaceReflectorSetComponent with a particular Room limits the scope in which the geometry is accessible. 这样可以缩小反射和衍射计算中执行的射线投射的搜索范围。在设为 None 时，会将该几何构造的范围设为全局。Note if one or more geometry sets are associated with a Room, that Room can no longer access geometry that is in the global scope.

参见
:   - [AkSurfaceReflectorSetComponent Blueprint 函数](features_blueprint_spatialaudio.html#features_blueprint_spatialaudio_surfacereflectorset)
    - [Spatial Audio Geometry SDK 文档](https://www.audiokinetic.com/library/edge/?source=SDK&id=spatial_audio_apigeometry.html)
    - [Reflect 文档](https://www.audiokinetic.com/library/edge/?source=Help&id=wwise_reflect_plug_in_effect)

# AkRoomComponent

您可以将此组件添加到任何 `UPrimitiveComponent` 以将 Spatial Audio Room 注册到 Wwise 声音引擎。Room 有两个作用：

- 实现带有朝向的混响效果。Room 内游戏对象所应用的所有 Auxiliary Bus 朝向均与 Volume 的前向矢量相同。
- 在与 [AkAcousticPortal](pg_features_spatialaudio.html#features_objects_akacousticportal) 或 [AkPortalComponent](pg_features_spatialaudio.html#features_objects_akportalcomponent) 结合使用时，可通过 Portal 将湿声信号从某一 Room 输出到另一 Room。

无论对于哪种情况，都必须针对 Auxiliary Bus 启用 **Listener Relative Routing**，以便在 Positioning 选项卡中指定 3D Spatialization 并指派 Attenuation。

To specify the Auxiliary Bus and other late reverb properties, add a sibling [AkLateReverbComponent](pg_features_objects_components.html#features_aklatereverbcomponent).

属性：

- **Enable Room**：启用此组件。
- **Is Dynamic**: Enables runtime changes to the Portal connections for this Room based on the Room's movement. When the value for this property is set, bWantsOnUpdateTransform is also set to the same value. For worlds that contain many Portals, enabling this property can be computationally expensive. When this option is disabled, the Room's Portal connections might still change if dynamic Portals are moved (that is, Portals with Is Dynamic enabled).
- **Priority**: Determines the order in which the Rooms are applied. If Rooms overlap, the one with the highest priority is selected. If two or more overlapping Rooms have the same priority, it is not possible to predict which Room will be selected.
- **Transmission Loss**: Sets the transmission loss value on the direct sound emitted in the Room when the listener is in another Room. Think of this value as 'thickness', because it relates to how much sound energy is transmitted through the Room's walls. The valid range is 0.0f-1.0f. If the Room has a parent or sibling [AkGeometryComponent](pg_features_spatialaudio.html#features_objects_akgeometrycomponent) or [AkSurfaceReflectorSetComponent](pg_features_spatialaudio.html#features_objects_aksurfacereflectorset), the transmission loss of these component surfaces is used, unless they are set to 0.
- **Ak Event**
  - **Aux Send Level**: Send level for sounds that are posted to the Room. 有效范围：(0.f-1.f)。若值为 0，则禁用辅助发送。
  - **Auto Post**: Automatically post the audio event posted to the Room on BeginPlay.
  - **Ak Audio Event**: The event to post to the Room game oject.
- **Reverb Zone**
  - **Enable Reverb Zone**: Sets this Room as a Reverb Zone. A Reverb Zone models a region that has a distinct reverb effect or ambience but does not require Portals to connect to neighboring Rooms. Use Reverb Zones instead of standard Rooms whenever there are no obvious walls, or generally when there is more negative space than positive space at the interface between the two regions.
  - **Parent Room Actor**: Establishes a parent-child relationship between two Rooms and allows for sound propagation between them as if they were the same Room, without the need for a connecting Portal. 父级 Room 可具有多个 Reverb Zone，但 Reverb Zone 只能有一个父对象。The Reverb Zone and its parent are both Rooms, and as such, must be specified using Enable Room. The automatically created 'outdoors' Room is commonly used as a parent Room for Reverb Zones, because they often model open spaces. When set to None (the default value), the Reverb Zone is automatically attached to the 'outdoors' Room.
  - **Parent Room Name**: The name of the Parent Room of this Reverb Zone. If the Parent Room Actor is None, or if the Parent Room Actor is not valid, the 'outdoors' Room is chosen and printed here.
  - **Transition Region Width**: Width of the transition region between the Reverb Zone and its parent. The transition region acts the same way as Portal depth, but is centered around the Reverb Zone geometry (see [AkPortalComponent](pg_features_spatialaudio.html#features_objects_akportalcomponent) for more details about the Portal depth). It only applies where surface transmission loss is set to 0. 该值必须为正值。负值将被视作 0。

|  |  |
| --- | --- |
|  | **注記：**  - Ak Room 组件必须与组件层级结构中的 `UPrimitiveComponent` 绑定。若 Ak Room 组件没有 `UPrimitiveComponent` 父对象，则日志中将显示错误，组件也会不起作用。 - 在更新 Wwise 时，Ak Room 组件使用其父对象 (`UPrimitiveComponent`) 的位置和边界。所有直接应用于 Ak Room 组件的变换、旋转或缩放都将不起作用。 - In order to avoid repeating expensive computations, dynamic Rooms wait until they have stopped moving for .1 seconds before processing the change in position. This involves updating the Room index and re-evaluating Portal connectivity in Unreal, and sending updated Room parameters to the Spatial Audio engine. Therefore, a continuously moving AkRoomComponent behaves as if it were stationary. - 在自定义 Blueprint 类中使用 `AkRoomComponent` 时，建议将 Simple Collision 组件用作父对象（如 `BoxCollision` 、`SphereCollision` 或 `CapsuleCollision` ）。有关详细信息，请参阅 [Spatial Audio Blueprint 组件](sa_components.html) 章节。 |

参见
:   - [AkRoomComponent Blueprint 函数](features_blueprint_spatialaudio.html#features_blueprint_spatialaudio_room)
    - [Room 和 Portal SDK 文档](https://www.audiokinetic.com/library/edge/?source=SDK&id=using_rooms_and_portals.html)

# FAkOutdoorsRoomParameters

When a game object is not within a [AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent), it is assigned to the Outdoors Room, which is automatically created. You do not have to add the Outdoors Room to the scene, but you can customize it with global Blueprint functions. See [Outdoors Room Blueprint Functions](features_blueprint_spatialaudio.html#features_blueprint_spatial_audio_outdoorsroom) for more information.

属性：

- **ReverbAuxBus**: Wwise Auxiliary Bus associated with the Outdoors Room. Default is null.
- **ReverbLevel**: Maximum send level to the Wwise Auxiliary Bus associated with the Outdoors Room. Valid range is 0.0f-1.0f. Default value is 1.
- **TransmissionLoss**: The transmission loss value in Wwise, on emitters in the Outdoors Room, when no audio paths to the listener are found via sound propagation in Wwise Spatial Audio. Valid range 0.0f-1.0f. Default value is 0.
- **AuxSendLevel**: Send level for sounds that are posted in the Outdoors Room. Valid range is 0.f-1.f. 若值为 0，则禁用辅助发送。Default value is 0.

# AkPortalComponent

您可以将此组件添加到任何 `UPrimitiveComponent` 以将 Spatial Audio Portal 注册到 Wwise 声音引擎。此组件允许某个绑定有 [AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent) 的 Actor（如 [AkSpatialAudioVolume](pg_features_spatialaudio.html#features_objects_akspatialaudiovolume) ）内所含的声音渗透到其他绑定有 [AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent) 的 Actor。在初始化时，会检测这些与 Portal 重叠的 Actor。Both panned and 3D-spatialized sounds can be routed through Portals. Portals have a front and a back Room. They must have at least one Room connected, the front Room must be different than the back Room, and the front and back Rooms cannot have a parent-child relationship (see [AkReverbZone](pg_features_spatialaudio.html#features_objects_akreverbzone) for more information). The depth of a Portal determines the crossfade distance for both reverb sends and spread transition between the front and back Rooms. A deeper Portal (along its local X-axis) results in a longer crossfade distance when an `AkComponent` transitions through the Portal.

If you are using built-in game parameters to drive RTPCs, any obstruction and occlusion values set on the Portal do not affect the RTPC values. This behavior is intentional and occurs because RTPCs only provide one value per game object, but a single game object can have multiple paths through different Portals, each with different obstruction and occlusion values.

You can view Rooms and Portals in the Viewport to adjust their positions, and to visualize Portal-Room connections. 您可以在 Wwise Integration Settings 中的 **Viewports - Visualize Rooms and Portals** 下启用或禁用该设置。另外，还可直接通过 Unreal Level Editor Viewport 菜单来切换该设置。

![](../../../../images/ViewportRoomsPortals.png)

在 Level Editor Viewport 菜单中直观地显示 Room 和 Portal

属性：

- **Is Dynamic**: Enables runtime changes to the Room connections for this Portal based on the Portal's movement. When the value for this property is set, bWantsOnUpdateTransform is also set to its value. For worlds that contain many Rooms, enabling this property can be computationally expensive. When this option is disabled, the Portal's Room connections might still change if dynamic Rooms are moved (that is, Rooms with Is Dynamic enabled).
- **Initial State**: Initially enables or disables the Portal. When the Portal is enabled, emitters positioned in the AkRoomComponent in front of and behind the Portal emit through it.
- **Initial Occlusion**: The initial occlusion value applied to the Portal. When the occlusion value is set to 0, the Portal is not occluded, and when it is set to 1, the Portal is completely occluded. The occlusion value is directly applied to the Portal with [AK::SpatialAudio::SetPortalObstructionAndOcclusion](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_aaf04c21b13be01b9f66cd77618423110.html). Portal occlusion can be used to modulate sound in response to a door opening or closing.
- **Obstruction Refresh Interval**: Set the time interval between obstruction checks (direct line of sight between game objects or other Portals and this Portal). 若设为 0，则禁用声障检查。Only use this feature if you plan to obstruct this Portal with geometry that is neither [AkSurfaceReflectorSetComponent](pg_features_spatialaudio.html#features_objects_aksurfacereflectorset) nor [AkGeometryComponent](pg_features_spatialaudio.html#features_objects_akgeometrycomponent). If not, we recommend that you disable obstruction checks and exclusively use Spatial Audio Geometric Diffraction and Transmission.
- **Obstruction Collision Channel**: The object collision channel that creates the collision of the obstruction ray-casts between game objects and this Portal with the desired geometry.

|  |  |
| --- | --- |
|  | **注記：**  - AkPortalComponent 必须与组件层级结构中的 `UPrimitiveComponent` 绑定。若 AkPortalComponent 没有 `UPrimitiveComponent` 父对象，则日志中将显示错误，组件也会不起作用。 - When a Portal is selected, the names of its connected Rooms are displayed on each side. - 在更新 Wwise 时，AkPortalComponent 使用其父对象 (`UPrimitiveComponent`) 的位置和边界。所有直接应用于 AkPortalComponent 的变换、旋转或缩放都将不起作用。 - 若向自定义 Blueprint 类添加了多个 AkPortalComponent，则在 Level Editor 中移动该类的实例时 Unreal Editor 可能会陷入无响应状态。为避免出现这一问题，可按照以下所述在 Class Settings 中禁用 **Run Construction Script on Drag**：   1. 在 Blueprint Editor 中打开自定义 Blueprint 类。   2. 单击 **Class Settings**。   3. 在 Details 面板的 Blueprint Options 下，禁用 **Run Construction Script on Drag**。 |

参见
:   - [AkPortalComponent Blueprint 函数](features_blueprint_spatialaudio.html#features_blueprint_spatialaudio_portal)
    - [Room 和 Portal SDK 文档](https://www.audiokinetic.com/library/edge/?source=SDK&id=using_rooms_and_portals.html)

# AkSpatialAudioVolume

我们在集成包中添加了一个 AkSpatialAudio Volume。它由一个简单的 Volume 构成，并绑定了 [AkSurfaceReflectorSetComponent](pg_features_spatialaudio.html#features_objects_aksurfacereflectorset) 、[AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent) 和 [AkLateReverbComponent](pg_features_objects_components.html#features_aklatereverbcomponent) 。

# AkAcousticPortal

该 Actor 可直接在游戏环境中生成，其绑定有 [AkPortalComponent](pg_features_spatialaudio.html#features_objects_akportalcomponent) 。

# AkGeometryComponent

此组件跟 [AkSurfaceReflectorSetComponent](pg_features_spatialaudio.html#features_objects_aksurfacereflectorset) 一样，只不过它不能直接绑定到 Brush 而是必须添加到 StaticMeshComponent。`AkGeometryComponent` 会将其 Mesh 转换为 Spatial Audio Geometry。它可以通过 Static Mesh 和 Simple Collision Mesh 来进行转换。对于 Simple Collision，Sphere Primitive 和 Capsule Primitive 近似于 Bounding Box Mesh。

在调试游戏时，可在 Wwise 设计工具内的 Game Object 3D Viewer 中查看 Spatial Audio Geometry。利用 `AkGeometryComponent` ，可以发送更加复杂的形状。不过，这样可能会阻止 Game Object 3D Viewer 显示几何构造。为了对游戏发送的附加数据进行补偿，请确保在 [Platform Initialization Settings](using_initialsetup.html#initialsetup_inifiles) 中恰当设置 Monitor Queue Pool Size。

无论选择哪种 Mesh Type，都将通过 Mesh 的 Physical Material 得出 Acoustic Texture 和透射损失值。Use the Geometry Surface Properties Table in the [Integration Settings](using_initialsetup.html#initialsetup_gamesettings) to associate Physical Materials with [UAkAcousticTexture](pg_features_objects_assets.html#features_objects_classes_UAkAcousticTexture) and transmission loss values.

- 在选用 Static Mesh 时，将通过 Static Mesh 所用每种 Material 的 Physical Material 得出 Surface Properties。
- 在选用 Simple Collision 时，将通过 Simple Collision Physical Material 得出 Surface Properties。

注意，在 Unreal 中，若未选择任何 Physical Material（设为 None），则使用 DefaultPhysicalMaterial。Associate Geometry Surface Properties to the DefaultPhysicalMaterial for meshes that do not have assigned Physical Materials.

属性：

- Geometry
  - **Mesh Type**：决定是要通过 Static Mesh 还是 Simple Collision Mesh 转换几何构造。
  - **LOD**（细节层次）：若在 **Mesh Type** 列表中选择 **Static Mesh**，则可利用此参数来选择将 LOD 用作 Spatial Audio Geometry。
  - **Welding Threshold**：若在 **Mesh Type** 列表中选择 **Static Mesh**，则可利用此参数来选择按 Unreal 单位计量两个要融为一体的顶点之间的局部距离。只要两个顶点之间的距离小于此阈值，就会将其视为同一顶点并为其指派相同的位置。增大此阈值会减少三角形之间的间隙数量，使得网格更加连续、声音泄漏更少，同时也会删除因太小而无关紧要的三角形。此外，增大此阈值还有利于 Spatial Audio 借助寻边算法找出更多有效的衍射边缘。
  - **Enable Diffraction**：针对此 Geometry 启用几何衍射。
  - **Enable Diffraction on Boundary Edges**：针对此 Geometry 在边界边缘启用几何衍射。
  - **Bypass Portal Subtraction**: Prevents Portal bounding boxes from being subtracted from this geometry.
  - **Solid**: Applies transmission loss once for each time a transmission path enters and exits its volume, using the max transmission loss between each hit surface. A non-solid geometry instance is one where each surface is infinitely thin, applying transmission loss at each surface. This option has no effect if the Transmission Operation is set to Max.
  - Surface Overrides
    - **AkAcousticTexture**: Overrides the [UAkAcousticTexture](pg_features_objects_assets.html#features_objects_classes_UAkAcousticTexture) that is automatically chosen based on the physical material of the mesh. 若在 **Mesh Type** 中选择 **Static Mesh**，则可单独覆盖每种 Material 的 Acoustic Texture。
    - **Override Transmission Loss**: Overrides the transmission loss value.
    - **Transmission Loss**：覆盖要依据 Mesh 的 Physical Material 自动选择的透射值。若在 **Mesh Type** 中选择 **Static Mesh**，则可单独覆盖每种 Material 的透射损失值。有效范围为 0.0 - 1.0。若值为 0.0，则表示声音全部穿透了表面。若值为 1.0，则表示声音被表面完全阻挡。
  - Advanced
    - **Associated Room**: (Deprecated) Associate this AkGeometryComponent with a Room. This property is deprecated and will be removed in a future version. We recommend not using it by leaving it set to **None**. Associating an AkGeometryComponent with a particular Room limits the scope in which the geometry is accessible. 这样可以缩小反射和衍射计算中执行的射线投射的搜索范围。在设为 None 时，会将该几何构造的范围设为全局。Note if one or more geometry sets are associated with a room, that room can no longer access geometry that is in the global scope.

|  |  |
| --- | --- |
|  | **注記：** 在 Unreal 内的 Blueprint Editor 中添加 AkGeometryComponent 时，若将 **Mesh Type** 设为 **Static Mesh**，则不会自动填充 Acoustic Texture 数组。因为 Blueprint Editor 中的 Component Details 面板只会显示模板组件实例的详细信息，而这些实例跟 Blueprint 中的其他组件并无关联。 |

参见
:   - [Unreal Spatial Audio 教程](spatialaudio.html)
    - [AkGeometry Blueprint 函数](features_blueprint_spatialaudio.html#features_blueprint_spatialaudio_geometry)
    - [Spatial Audio Geometry SDK 文档](https://www.audiokinetic.com/library/edge/?source=SDK&id=spatial_audio_apigeometry.html)
    - [Reflect 文档](https://www.audiokinetic.com/library/edge/?source=Help&id=wwise_reflect_plug_in_effect)

# AkReverbZone

A Reverb Zone is useful in situations where two or more acoustic environments are not easily modeled as closed Rooms connected by Portals. Possible uses for Reverb Zones include: a covered area with no walls, a forested area within an outdoor space, or any situation where multiple reverb effects are desired within a common space. Reverb Zones have many advantages compared to standard Game-Defined Auxiliary Sends (that is compared to the [AkLateReverbComponent](pg_features_objects_components.html#features_aklatereverbcomponent) or the [AkReverbVolume](pg_features_objects_actors.html#features_akreverbvolume)). They are part of the wet path, and form reverb chains with other Rooms; they are spatialized according to their 3D extent; they are also subject to other acoustic phenomena simulated in Wwise Spatial Audio, such as diffraction and transmission.

The AkReverbZone Actor is the same as an [AkSpatialAudioVolume](pg_features_spatialaudio.html#features_objects_akspatialaudiovolume) Actor, but with different default values optimized for Reverb Zones.

- The [AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent) has **Enable Reverb Zone** set to True and its **Transmission Loss** value set to 0.
- The [AkSurfaceReflectorSetComponent](pg_features_spatialaudio.html#features_objects_aksurfacereflectorset) component is disabled. This allows sound to pass through all of the volume's surfaces and for the transition region to be applied to all of them.

The Room's transmission loss value can be set to something other than 0. In this case, it is applied to all sounds emitted by the Room itself (for example, Room tones or ambience) and to the wet path (the chain of Room Auxiliary Busses) of sounds crossing the Room boundary.

Another kind of transmission loss is the geometric transmission loss that can be set on the Room's surfaces. The geometric transmission loss value is applied to the direct path of sounds crossing these surfaces, in other words the transmission path. When the [AkSurfaceReflectorSetComponent](pg_features_spatialaudio.html#features_objects_aksurfacereflectorset) component is disabled, the geometry is sent to Spatial Audio to define the shape of the room, but is not used for reflection and diffraction. Defining a room shape with geometry makes it possible to enable only certain surfaces, in which case, their transmission loss values are set to 1. It is possible to enable the [AkSurfaceReflectorSetComponent](pg_features_spatialaudio.html#features_objects_aksurfacereflectorset) to set surfaces with different acoustic textures and transmission loss values. Surfaces with a transmission loss value between 0 and 1, or, in other words, semi-transparent surfaces, do not let diffraction and reflection paths pass through. Only direct transmission paths pass through such surfaces. The final effective geometric transmission loss value is the maximum transmission loss value of all the different surfaces a sound path passes through.

参见
:   - [AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent)
    - [AkPortalComponent](pg_features_spatialaudio.html#features_objects_akportalcomponent)
    - [AkRoomComponent Blueprint 函数](features_blueprint_spatialaudio.html#features_blueprint_spatialaudio_room)