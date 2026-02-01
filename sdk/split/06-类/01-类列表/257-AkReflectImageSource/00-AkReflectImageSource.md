# AkReflectImageSource

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_reflect_image_source-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkReflectImageSource结构体 参考

`#include <AkReflectGameData.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkReflectImageSource](struct_ak_reflect_image_source_a1f020ff2cb432bda97d1275aa6cf7706.html#a1f020ff2cb432bda97d1275aa6cf7706) () |
|  | |
|  | [AkReflectImageSource](struct_ak_reflect_image_source_ad6656e8fc691a10ceb843925554da975.html#ad6656e8fc691a10ceb843925554da975) ([AkImageSourceID](_ak_typedefs_8h_aa8cb517b34d4fc2a5ad99c122136db30.html#aa8cb517b34d4fc2a5ad99c122136db30) in\_uID, [AkVector64](struct_ak_vector64.html) in\_sourcePosition, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fDistanceScalingFactor, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fLevel) |
|  | |
| void | [SetName](struct_ak_reflect_image_source_af3479c3fd2e8d17ecc1c70edc31b99cb.html#af3479c3fd2e8d17ecc1c70edc31b99cb) (const char \*in\_pName) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkImageSourceID](_ak_typedefs_8h_aa8cb517b34d4fc2a5ad99c122136db30.html#aa8cb517b34d4fc2a5ad99c122136db30) | [uID](struct_ak_reflect_image_source_ae6f7de77ef37b68d0261265148c0fa42.html#ae6f7de77ef37b68d0261265148c0fa42) |
|  | Image source ID (for matching delay lines across frames) [更多...](struct_ak_reflect_image_source_ae6f7de77ef37b68d0261265148c0fa42.html#ae6f7de77ef37b68d0261265148c0fa42) |
|  | |
| [AkImageSourceParams](struct_ak_image_source_params.html) | [params](struct_ak_reflect_image_source_ae4e5167ecaf7ab87c13f75181b46ada8.html#ae4e5167ecaf7ab87c13f75181b46ada8) |
|  | Image source properties [更多...](struct_ak_reflect_image_source_ae4e5167ecaf7ab87c13f75181b46ada8.html#ae4e5167ecaf7ab87c13f75181b46ada8) |
|  | |
| [AkImageSourceTexture](struct_ak_image_source_texture.html) | [texture](struct_ak_reflect_image_source_ae28ae09070914f3e0918dceb8a006098.html#ae28ae09070914f3e0918dceb8a006098) |
|  | Image source's acoustic textures. Note that changing any of these textures across frames for a given image source, identified by uID, may result in a discontinuity in the audio signal. [更多...](struct_ak_reflect_image_source_ae28ae09070914f3e0918dceb8a006098.html#ae28ae09070914f3e0918dceb8a006098) |
|  | |
| [AkImageSourceName](struct_ak_image_source_name.html) | [name](struct_ak_reflect_image_source_af23faed8cdff04f0fa282c57daf38c21.html#af23faed8cdff04f0fa282c57daf38c21) |
|  | Image source name, for profiling. [更多...](struct_ak_reflect_image_source_af23faed8cdff04f0fa282c57daf38c21.html#af23faed8cdff04f0fa282c57daf38c21) |
|  | |

## 详细描述

在文件 [AkReflectGameData.h](_ak_reflect_game_data_8h_source.html) 第 [33](_ak_reflect_game_data_8h_source.html#l00033) 行定义.