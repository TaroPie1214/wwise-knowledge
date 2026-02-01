# Spatial Audio 对象 Blueprint 函数

|  |
| --- |
| Wwise Unreal Integration Documentation |

Spatial Audio 对象 Blueprint 函数

# AkGeometry Blueprint 函数

- **ConvertMesh**：将父级 Mesh 转换为 Spatial Audio Geometry 可用的 `FAkGeometryData` 结构。在将 Mesh Type 设为 Static Mesh 时，使用父级 Mesh 的索引和顶点。在将 Mesh Type 设为 Simple Collision 时，把父对象的 BodySetup 转换为 `FAkGeometryData` 。若 Simple Collision 由 Box Primitive、Sphere Primitive 或 Capsule Primitive 构成，则使用各个 Primitive 的 Bounding Box。若 Simple Collision 包含 Convex Hull Primitive，则使用 Simple Collision 的索引和顶点。
- **RemoveGeometry**：通过调用 [AK:SpatialAudio::RemoveGeometry()](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_ae450803c582e5e6e2f8906cfdd384a25.html) 来移除 Spatial Audio 中的几何构造。
- **UpdateGeometry**：将 `FAkGeometryData` 组件发送到 Spatial Audio。

# AkLateReverbComponent Blueprint 函数

- **AssociateAkTextureSetComponent**：设置组件以用于估算 HFDamping。比如，在 Blueprint 所含 Static Mesh 组件带有 AkGeometry 子组件的情况下，可通过在 BeginPlay 时调用该函数来将所述 AkGeometry 组件与此 Late Reverb 组件关联。若该 Late Reverb 组件包含同级 Geometry 组件或 Surface Reflector Set 组件，则会自动与之进行关联，而无需调用此函数。

# AkRoomComponent Blueprint 函数

-**SetAttenuationScalingFactor**: Sets the attenuation scaling factor, which modifies the attenuation computations on the game object to simulate sounds with a larger or smaller area of effect.

- **GetPrimitiveParent**：返回与此 Ak Room 组件绑定的 `UPrimitiveComponent` 。
- **SetReverbZone**: Establishes a parent-child relationship between this [AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent) and a parent [AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent) and allows for sound propagation between them as if they were the same Room, without the need for a connecting [AkPortalComponent](pg_features_spatialaudio.html#features_objects_akportalcomponent). Setting a Room as a Reverb Zone is useful in situations where two or more acoustic environments are not easily modeled as closed Rooms connected by Portals. Possible uses for Reverb Zones include: a covered area with no walls, a forested area within an outdoor space, or any situation where multiple reverb effects are desired within a common space. Reverb Zones have many advantages compared to standard Game-Defined Auxiliary Sends (that is compared to the [AkLateReverbComponent](pg_features_objects_components.html#features_aklatereverbcomponent) or the [AkReverbVolume](pg_features_objects_actors.html#features_akreverbvolume)). They are part of the wet path, and form reverb chains with other Rooms; they are spatialized according to their 3D extent; they are also subject to other acoustic phenomena simulated in Wwise Spatial Audio, such as diffraction and transmission. 父级 Room 可具有多个 Reverb Zone，但 Reverb Zone 只能有一个父对象。If a Room is already assigned to a parent Room, it is first removed from the old parent (exactly as if RemoveReverbZone were called), and is then assigned to the new parent Room. A Reverb Zone can be the parent of another Reverb Zone. A Room cannot be its own parent. The automatically created 'Outdoors' Room is commonly used as a parent Room for Reverb Zones, because they often model open spaces. A Reverb Zone needs to be a Room component with an associated geometry. This function also sets a transition region between the Reverb Zone and its parent. The transition region acts the same way as Portal depth, but is centered around the Reverb Zone geometry (see [AkPortalComponent](pg_features_spatialaudio.html#features_objects_akportalcomponent) for more details about the Portal depth). Transition regions are only added on surfaces where transmission loss is set to 0.
- **RemoveReverbZone**: Removes this Reverb Zone from its parent. Sound can no longer propagate between the two Rooms, unless they are explicitly connected with a Portal.
- **SetGeometryComponent**: Sets the geometry component to use to send the geometry of the room to Wwise. For example, in a Blueprint that has a static mesh component with an AkGeometry child component, this function can be called in BeginPlay to associate that AkGeometry component with this room component. If this room component has a sibling geometry component (or surface reflector set component), they are automatically associated and there is no need to call this function.

# AkPortalComponent Blueprint 函数

您可以针对 [AkPortalComponent](pg_features_spatialaudio.html#features_objects_akportalcomponent) 对象执行多个 Wwise 函数。在 Ak Portal Component 类别中可以找到这些函数。

- **EnablePortal**: Enables the portal. Emitters positioned in the [AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent) in front of and behind the portal emit through it.
- **DisablePortal**: Disables the portal. Emitters positioned in the AkRoomComponent in front of and behind the portal do not emit through it.
- **GetCurrentState**: Returns an `AkAcousticPortalState`, which represents the current state of the portal (Enabled or Disabled).
- **GetPortalOcclusion**: Returns a floating point number between 0 and 1 that represents the occlusion value applied to the portal. A value of 0 indicates that the portal is not occluded and a value of 1 indicates that it is completely occluded.
- **SetPortalOcclusion**: Sets a new portal occlusion value. A value of 0 indicates that the portal is not occluded and a value of 1 indicates that it is completely occluded. The occlusion value is applied to the portal with [AK::SpatialAudio::SetPortalObstructionAndOcclusion](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_aaf04c21b13be01b9f66cd77618423110.html). Portal occlusion can be used to modulate sound in response to a door opening or closing.
- **GetPrimitiveParent**：返回与此 Ak Portal 组件绑定的 `UPrimitiveComponent` 。
- **PortalPlacementValid**：若 Portal 位置和朝向有效，则返回 true。Portals have a front and a back Room. They must have at least one connected Room, the front Room must be different than the back Room, and the Rooms cannot be a Reverb Zone and its parent. 有关详细信息，请参阅 [AkPortalComponent](pg_features_spatialaudio.html#features_objects_akportalcomponent) 和 [AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent) 章节。

# AkSurfaceReflectorSetComponent Blueprint 函数

- **SendSurfaceReflectorSet**：通过调用 [AK:SpatialAudio::SetGeometry()](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_a0cada36fab682ebb3005a79dd05a5640.html) 来将 Brush 的索引和顶点转换为 Spatial Audio Geometry 数据并发送到 Spatial Audio。
- **RemoveSurfaceReflectorSet**：通过调用 [AK:SpatialAudio::RemoveGeometry()](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_ae450803c582e5e6e2f8906cfdd384a25.html) 来移除 Spatial Audio 中的几何构造。
- **UpdateSurfaceReflectorSet**：通过调用 `SendSurfaceReflectorSet` 来将新的 Brush 转换结果发送到 Spatial Audio。

# Outdoors Room Blueprint Functions

When using the Spatial Audio Rooms and Portal feature, a default Room is automatically created to place game objects that are currently not in a Room. This Room is typically used for outdoors and is therefore nicknamed the Outdoors Room.

Because the Outdoors Room is automatically created, you do not have to add it to a scene, but you can customize it with the following global Blueprint functions:

- **GetCurrentOutdoorsRoomParameters**: Returns a [FAkOutdoorsRoomParameters](pg_features_spatialaudio.html#features_objects_akoutdoorsroomparameters) structure containing the current Outdoors Room parameters.
- **SetOutdoorsRoomParameters**: Sets the parameters of the Outdoors Room by sending a [FAkOutdoorsRoomParameters](pg_features_spatialaudio.html#features_objects_akoutdoorsroomparameters) structure as a parameter.
- **ResetOutdoorsRoomParams**: Resets the Outdoors Room parameters to their default values. See the [FAkOutdoorsRoomParameters](pg_features_spatialaudio.html#features_objects_akoutdoorsroomparameters) properties for more information.
- **PostEventOutdoors**: Posts an Event on the Outdoors Room.
- **StopOutdoors**: Stops all sounds for the Outdoors Room.

参见
:   - [Wwise Spatial Audio 对象](pg_features_spatialaudio.html)
    - [Unreal Spatial Audio 教程](spatialaudio.html)