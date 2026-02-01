# AkExtent

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_extent-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkExtent结构体 参考

`#include <AkSpatialAudioTypes.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkExtent](struct_ak_extent_a509bb4eadc08850ff9c1af0350bc641a.html#a509bb4eadc08850ff9c1af0350bc641a) () |
|  | |
|  | [AkExtent](struct_ak_extent_a34b870246ace936d6f9471f116fa9047.html#a34b870246ace936d6f9471f116fa9047) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_halfWidth, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_halfHeight, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_halfDepth) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [halfWidth](struct_ak_extent_ad658bb9909cf0058efc29fd2a2ded501.html#ad658bb9909cf0058efc29fd2a2ded501) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [halfHeight](struct_ak_extent_a439543c984fc71cdf23d9a2453148c50.html#a439543c984fc71cdf23d9a2453148c50) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [halfDepth](struct_ak_extent_a2607ea6d037b049de1b780a0515c3e14.html#a2607ea6d037b049de1b780a0515c3e14) |
|  | |

## 详细描述

[AkExtent](struct_ak_extent.html) describes an extent with width, height and depth. halfWidth, halfHeight and halfDepth should form a vector from the centre of the volume to the positive corner. Used in `AkPortalParams`, negative values in the extent will cause an error. For rooms, negative values can be used to opt out of room transmission.

在文件 [AkSpatialAudioTypes.h](_ak_spatial_audio_types_8h_source.html) 第 [398](_ak_spatial_audio_types_8h_source.html#l00398) 行定义.