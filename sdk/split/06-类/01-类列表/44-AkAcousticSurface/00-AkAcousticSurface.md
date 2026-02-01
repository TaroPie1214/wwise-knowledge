# AkAcousticSurface

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_acoustic_surface-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkAcousticSurface结构体 参考

`#include <AkSpatialAudioTypes.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkAcousticSurface](struct_ak_acoustic_surface_a0eb9ec2455e04c3541f7caf58fd3bd7e.html#a0eb9ec2455e04c3541f7caf58fd3bd7e) () |
|  | Constructor [更多...](struct_ak_acoustic_surface_a0eb9ec2455e04c3541f7caf58fd3bd7e.html#a0eb9ec2455e04c3541f7caf58fd3bd7e) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [textureID](struct_ak_acoustic_surface_a875e008bcff3807257f5bfeec8207e66.html#a875e008bcff3807257f5bfeec8207e66) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [transmissionLoss](struct_ak_acoustic_surface_ab0ec8a6eee25b28b4f8b9e91dbff17da.html#ab0ec8a6eee25b28b4f8b9e91dbff17da) |
|  | |
| const char \* | [strName](struct_ak_acoustic_surface_a05d4856b1c911d231702254f41d94fab.html#a05d4856b1c911d231702254f41d94fab) |
|  | Name to describe this surface [更多...](struct_ak_acoustic_surface_a05d4856b1c911d231702254f41d94fab.html#a05d4856b1c911d231702254f41d94fab) |
|  | |

## 详细描述

Describes the acoustic surface properties of one or more triangles. An single acoustic surface may describe any number of triangles, depending on the granularity desired. For example, if desired for debugging, one could create a unique `AkAcousticSurface` struct for each triangle, and define a unique name for each. Alternatively, a single `AkAcousticSurface` could be used to describe all triangles. In fact it is not necessary to define any acoustic surfaces at all. If the `AkTriangle::surface` field is left as `AK_INVALID_SURFACE`, then a default-constructed `AkAcousticSurface` is used.

在文件 [AkSpatialAudioTypes.h](_ak_spatial_audio_types_8h_source.html) 第 [453](_ak_spatial_audio_types_8h_source.html#l00453) 行定义.