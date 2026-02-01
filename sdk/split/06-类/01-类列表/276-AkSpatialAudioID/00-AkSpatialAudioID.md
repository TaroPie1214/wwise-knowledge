# AkSpatialAudioID

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_spatial_audio_i_d-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkSpatialAudioID结构体 参考

Base type for ID's used by Wwise spatial audio.   
[更多...](struct_ak_spatial_audio_i_d.html#details)

`#include <AkSpatialAudioTypes.h>`

类 AkSpatialAudioID 继承关系图:

![](../../../images/struct_ak_spatial_audio_i_d.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
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
| Public 属性 | |
| [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [id](struct_ak_spatial_audio_i_d_a808b21c5653f6781e558284489d78df1.html#a808b21c5653f6781e558284489d78df1) |
|  | |

## 详细描述

Base type for ID's used by Wwise spatial audio.

在文件 [AkSpatialAudioTypes.h](_ak_spatial_audio_types_8h_source.html) 第 [89](_ak_spatial_audio_types_8h_source.html#l00089) 行定义.