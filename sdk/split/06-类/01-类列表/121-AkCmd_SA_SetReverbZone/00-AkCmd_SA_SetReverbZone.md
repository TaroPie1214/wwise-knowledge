# AkCmd_SA_SetReverbZone

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_reverb_zone-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetReverbZone结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkRoomID](struct_ak_room_i_d.html) | [reverbZoneRoomID](struct_ak_cmd___s_a___set_reverb_zone_aed4d6014020b63a758518a3e322efd47.html#aed4d6014020b63a758518a3e322efd47) |
|  | ID of the Room which will be specified as a Reverb Zone. [更多...](struct_ak_cmd___s_a___set_reverb_zone_aed4d6014020b63a758518a3e322efd47.html#aed4d6014020b63a758518a3e322efd47) |
|  | |
| [AkRoomID](struct_ak_room_i_d.html) | [parentRoomID](struct_ak_cmd___s_a___set_reverb_zone_afc6cbc4b69bcea7de0d1f93b184f6daf.html#afc6cbc4b69bcea7de0d1f93b184f6daf) |
|  | ID of the parent Room. [更多...](struct_ak_cmd___s_a___set_reverb_zone_afc6cbc4b69bcea7de0d1f93b184f6daf.html#afc6cbc4b69bcea7de0d1f93b184f6daf) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [transitionRegionWidth](struct_ak_cmd___s_a___set_reverb_zone_ab1b105d659ef630c39ea086ce9ce50f4.html#ab1b105d659ef630c39ea086ce9ce50f4) |
|  | Width of the transition region between the Reverb Zone and its parent. The transition region is centered around the Reverb Zone geometry. It only applies where triangle transmission loss is set to 0. [更多...](struct_ak_cmd___s_a___set_reverb_zone_ab1b105d659ef630c39ea086ce9ce50f4.html#ab1b105d659ef630c39ea086ce9ce50f4) |
|  | |

## 详细描述

Use a Room as a Reverb Zone. `AkCmd_SA_SetReverbZone` establishes a parent-child relationship between two Rooms and allows for sound propagation between them as if they were the same Room, without the need for a connecting Portal. Setting a Room as a Reverb Zone is useful in situations where two or more acoustic environments are not easily modeled as closed rooms connected by portals. Possible uses for Reverb Zones include: a covered area with no walls, a forested area within an outdoor space, or any situation where multiple reverb effects are desired within a common space. Reverb Zones have many advantages compared to standard Game-Defined Auxiliary Sends. They are part of the wet path, and form reverb chains with other Rooms; they are spatialized according to their 3D extent;   
they are also subject to other acoustic phenomena simulated in Wwise Spatial Audio, such as diffraction and transmission. A parent Room may have multiple Reverb Zones, but a Reverb Zone can only have a single Parent. If a Room is already assigned to a parent Room, it will first be removed from the old parent (exactly as if [AkCmd\_SA\_RemoveReverbZone](struct_ak_cmd___s_a___remove_reverb_zone.html) was used) before then being assigned to the new parent Room. A Room can not be its own parent. The Reverb Zone and its parent are both Rooms, and as such, must be specified using [AkCmd\_SA\_SetRoom](struct_ak_cmd___s_a___set_room.html). If [AkCmd\_SA\_SetReverbZone](struct_ak_cmd___s_a___set_reverb_zone.html) is sent before [AkCmd\_SA\_SetRoom](struct_ak_cmd___s_a___set_room.html), and either of the two rooms do not yet exist, placeholder Rooms with default parameters are created. They should be subsequently parametrized with [AkCmd\_SA\_SetRoom](struct_ak_cmd___s_a___set_room.html).

To set which Reverb Zone a Game Object is in, use the [AkCmd\_SA\_SetGameObjectInRoom](struct_ak_cmd___s_a___set_game_object_in_room.html) API, and pass the Reverb Zone's Room ID. In Wwise Spatial Audio, a Game Object can only ever be inside a single room, and Reverb Zones are no different in this regard.

|  |  |
| --- | --- |
|  | **备注:** The automatically created 'outdoors' Room is commonly used as a parent Room for Reverb Zones, since they often model open spaces. To attach a Reverb zone to outdoors, set `AK_OUTDOORS_ROOM_ID` as the `parentRoomID` argument. Like all Rooms, the 'outdoors' Room can be parameterized (for example, to assign a reverb bus) by specifying `AK_OUTDOORS_ROOM_ID` in a [AkCmd\_SA\_SetRoom](struct_ak_cmd___s_a___set_room.html) command./// This command can fail for the following reasons:  This command can fail for the following reasons:   - AK\_InvalidParameter: `reverbZoneRoomID` or `parentRoomID` are not valid room IDs, or they are the same value. - AK\_InsufficientMemory: Not enough memory to complete the operation.   参见  - [AkCommand\_SA\_SetReverbZone](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda86d714befda425a13f49fda43a4135ac) - [AkRoomID](struct_ak_room_i_d.html) - [AkCmd\_SA\_SetRoom](struct_ak_cmd___s_a___set_room.html) - [AkCmd\_SA\_RemoveRoom](struct_ak_cmd___s_a___remove_room.html) - [AkCmd\_SA\_RemoveReverbZone](struct_ak_cmd___s_a___remove_reverb_zone.html) - [AK\_OUTDOORS\_ROOM\_ID](_ak_spatial_audio_types_8h_a62ad8b5b6e2398f717a9c4a4beb8b144.html#a62ad8b5b6e2398f717a9c4a4beb8b144) |

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1698](_ak_command_types_8h_source.html#l01698) 行定义.