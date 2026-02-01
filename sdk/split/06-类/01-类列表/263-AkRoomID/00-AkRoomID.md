# AkRoomID

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_room_i_d-members.html) |
[Public 成员函数](#pub-methods) |
[静态 Public 成员函数](#pub-static-methods)

AkRoomID结构体 参考

`#include <AkSpatialAudioTypes.h>`

类 AkRoomID 继承关系图:

![](../../../images/struct_ak_room_i_d.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| constexpr | [AkRoomID](struct_ak_room_i_d_a605eb48885ae49b531f55f0bcc602416.html#a605eb48885ae49b531f55f0bcc602416) () |
|  | Default constructor. Creates an invalid ID. [更多...](struct_ak_room_i_d_a605eb48885ae49b531f55f0bcc602416.html#a605eb48885ae49b531f55f0bcc602416) |
|  | |
|  | [AkRoomID](struct_ak_room_i_d_a593e8d8315e6b774d7b6ee996e6ed743.html#a593e8d8315e6b774d7b6ee996e6ed743) ([AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) \_id) |
|  | Construct from a 64-bit int. [更多...](struct_ak_room_i_d_a593e8d8315e6b774d7b6ee996e6ed743.html#a593e8d8315e6b774d7b6ee996e6ed743) |
|  | |
|  | [AkRoomID](struct_ak_room_i_d_a0708f8d23a227a7095b830030f788568.html#a0708f8d23a227a7095b830030f788568) (const void \*ptr) |
|  | Conversion from a pointer to a [AkRoomID](struct_ak_room_i_d.html) [更多...](struct_ak_room_i_d_a0708f8d23a227a7095b830030f788568.html#a0708f8d23a227a7095b830030f788568) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [AsGameObjectID](struct_ak_room_i_d_abe791f0510a62ba13d02ca5e35d3b4eb.html#abe791f0510a62ba13d02ca5e35d3b4eb) () const |
|  | Conversion function used to convert [AkRoomID](struct_ak_room_i_d.html)'s to AkGameObjectIDs. [更多...](struct_ak_room_i_d_abe791f0510a62ba13d02ca5e35d3b4eb.html#abe791f0510a62ba13d02ca5e35d3b4eb) |
|  | |
| - Public 成员函数 继承自 [AkSpatialAudioID](struct_ak_spatial_audio_i_d.html) | |
| constexpr | [AkSpatialAudioID](struct_ak_spatial_audio_i_d_a0d66e28d1b620f2425a3efe030aa6302.html#a0d66e28d1b620f2425a3efe030aa6302) () |
|  | Default constructor. Creates an invalid ID. [更多...](struct_ak_spatial_audio_i_d_a0d66e28d1b620f2425a3efe030aa6302.html#a0d66e28d1b620f2425a3efe030aa6302) |
|  | |
|  | [AkSpatialAudioID](struct_ak_spatial_audio_i_d_ac3e644faab2fc9b9de416a5af0ca1120.html#ac3e644faab2fc9b9de416a5af0ca1120) ([AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) \_id) |
|  | Construct from a 64-bit int. [更多...](struct_ak_spatial_audio_i_d_ac3e644faab2fc9b9de416a5af0ca1120.html#ac3e644faab2fc9b9de416a5af0ca1120) |
|  | |
|  | [AkSpatialAudioID](struct_ak_spatial_audio_i_d_a330dcbe1e1f19c37a5f2162b4dbb14e3.html#a330dcbe1e1f19c37a5f2162b4dbb14e3) (const void \*ptr) |
|  | Conversion from a pointer to a [AkSpatialAudioID](struct_ak_spatial_audio_i_d.html "Base type for ID's used by Wwise spatial audio.") [更多...](struct_ak_spatial_audio_i_d_a330dcbe1e1f19c37a5f2162b4dbb14e3.html#a330dcbe1e1f19c37a5f2162b4dbb14e3) |
|  | |
| bool | [operator==](struct_ak_spatial_audio_i_d_a4d48f54a1c8a9cf3271bfb6b8ff7cdbc.html#a4d48f54a1c8a9cf3271bfb6b8ff7cdbc) (const [AkSpatialAudioID](struct_ak_spatial_audio_i_d.html) &rhs) const |
|  | |
| bool | [operator!=](struct_ak_spatial_audio_i_d_ae8867e424bca8ae71af515af85894aac.html#ae8867e424bca8ae71af515af85894aac) (const [AkSpatialAudioID](struct_ak_spatial_audio_i_d.html) &rhs) const |
|  | |
| bool | [operator<](struct_ak_spatial_audio_i_d_ac39db91e2028d99e328cb5122e8b97b5.html#ac39db91e2028d99e328cb5122e8b97b5) (const [AkSpatialAudioID](struct_ak_spatial_audio_i_d.html) &rhs) const |
|  | |
| bool | [operator>](struct_ak_spatial_audio_i_d_a95f39f9c79908f5e4711469f90490a42.html#a95f39f9c79908f5e4711469f90490a42) (const [AkSpatialAudioID](struct_ak_spatial_audio_i_d.html) &rhs) const |
|  | |
| bool | [operator<=](struct_ak_spatial_audio_i_d_a0423a1254f2f6e79157fdff96f0d26bf.html#a0423a1254f2f6e79157fdff96f0d26bf) (const [AkSpatialAudioID](struct_ak_spatial_audio_i_d.html) &rhs) const |
|  | |
| bool | [operator>=](struct_ak_spatial_audio_i_d_a16e65cbd293d48edf3b448662e42c62a.html#a16e65cbd293d48edf3b448662e42c62a) (const [AkSpatialAudioID](struct_ak_spatial_audio_i_d.html) &rhs) const |
|  | |
| bool | [IsValid](struct_ak_spatial_audio_i_d_af5d6b1d61bfa39d77bb2adbf859076fd.html#af5d6b1d61bfa39d77bb2adbf859076fd) () const |
|  | Determine if this ID is valid. [更多...](struct_ak_spatial_audio_i_d_af5d6b1d61bfa39d77bb2adbf859076fd.html#af5d6b1d61bfa39d77bb2adbf859076fd) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [AsGameObjectID](struct_ak_spatial_audio_i_d_a3a23e224bda27bb9c07635feeeabee91.html#a3a23e224bda27bb9c07635feeeabee91) () const |
|  | Conversion function used internally to convert from a [AkSpatialAudioID](struct_ak_spatial_audio_i_d.html "Base type for ID's used by Wwise spatial audio.") to a AkGameObjectID. [更多...](struct_ak_spatial_audio_i_d_a3a23e224bda27bb9c07635feeeabee91.html#a3a23e224bda27bb9c07635feeeabee91) |
|  | |
|  | [operator AkUInt64](struct_ak_spatial_audio_i_d_a2f6fb1fa560a98d3fd7505fba0498e0e.html#a2f6fb1fa560a98d3fd7505fba0498e0e) () const |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static [AkRoomID](struct_ak_room_i_d.html) | [FromGameObjectID](struct_ak_room_i_d_a432886ab12d142f576e467681db1a190.html#a432886ab12d142f576e467681db1a190) ([AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_fromGameObject) |
|  | Conversion function used to convert to AkGameObjectIDs to [AkRoomID](struct_ak_room_i_d.html). [更多...](struct_ak_room_i_d_a432886ab12d142f576e467681db1a190.html#a432886ab12d142f576e467681db1a190) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - Public 属性 继承自 [AkSpatialAudioID](struct_ak_spatial_audio_i_d.html) | |
| [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [id](struct_ak_spatial_audio_i_d_a808b21c5653f6781e558284489d78df1.html#a808b21c5653f6781e558284489d78df1) |
|  | |

## 详细描述

Spatial Audio Room ID type. This ID type exists in the same ID-space as game object ID's. The client is responsible for not choosing room ID's that conflict with registered game objects' ID's. Internally, the spatial audio rooms and portals API manages registration and un-registration of game objects that represent rooms using [AkRoomID](struct_ak_room_i_d.html)'s provided by the client; [AkRoomID](struct_ak_room_i_d.html)'s are converted to AkGameObjectID's by calling [AsGameObjectID()](struct_ak_room_i_d_abe791f0510a62ba13d02ca5e35d3b4eb.html#abe791f0510a62ba13d02ca5e35d3b4eb "Conversion function used to convert AkRoomID's to AkGameObjectIDs.").

参见
:   - [AK::SpatialAudio::SetRoom](namespace_a_k_1_1_spatial_audio_ab991cec1e8c9f4d2721fea2d37b285c8.html#ab991cec1e8c9f4d2721fea2d37b285c8)
    - [AK::SpatialAudio::RemoveRoom](namespace_a_k_1_1_spatial_audio_a130a8d8fba48b2207aab063ce9ac729c.html#a130a8d8fba48b2207aab063ce9ac729c)

在文件 [AkSpatialAudioTypes.h](_ak_spatial_audio_types_8h_source.html) 第 [124](_ak_spatial_audio_types_8h_source.html#l00124) 行定义.