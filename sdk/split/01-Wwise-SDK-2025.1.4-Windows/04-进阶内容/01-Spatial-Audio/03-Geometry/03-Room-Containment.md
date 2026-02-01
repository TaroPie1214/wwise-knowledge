# Room Containment

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Room Containment

Wwise automatically assigns Rooms to Game Objects using the geometry associated with each Room when available. Rooms can also be manually assigned using [AK::SpatialAudio::SetGameObjectInRoom()](namespace_a_k_1_1_spatial_audio_a3f080206f12c04b3464838cb18c43f4e.html#a3f080206f12c04b3464838cb18c43f4e) (see also [AK::SpatialAudio::UnsetGameObjectInRoom()](namespace_a_k_1_1_spatial_audio_a63a469a6dfb61ecc4883607720f1e448.html#a63a469a6dfb61ecc4883607720f1e448)).

# Room Geometry

When a geometry is used to define the shape of a Room, the following restrictions apply:

- Geometry is watertight: there must not be any holes in the geometry.
- Geometry is a manifold: the geometry must not overlap itself.

|  |  |
| --- | --- |
|  | **备注:** Wwise supports both convex and concave geometries. |

# Relation between Rooms

Rooms can overlap or be fully contained in other Rooms. However, in these situations, a Game Object can be located in several Rooms at the same time. Wwise uses a priority system to disambiguate these cases: Rooms whith the highest priority are always assigned first (refer to [AkRoomParams](struct_ak_room_params.html)). If two or more Rooms share the same priority, Wwise tries to assign the innermost room if possible.