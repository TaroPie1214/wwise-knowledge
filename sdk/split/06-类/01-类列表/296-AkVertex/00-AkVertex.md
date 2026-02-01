# AkVertex

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_vertex-members.html) |
[Public 成员函数](#pub-methods)

AkVertex结构体 参考

`#include <AkSpatialAudioTypes.h>`

类 AkVertex 继承关系图:

![](../../../images/struct_ak_vertex.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkVertex](struct_ak_vertex_a14a89b7f2b04b59b77dde97dec90df6b.html#a14a89b7f2b04b59b77dde97dec90df6b) () |
|  | |
|  | [AkVertex](struct_ak_vertex_afb36eeafdace25406a331c737bf4de2a.html#afb36eeafdace25406a331c737bf4de2a) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_x, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_y, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_z) |
|  | |
| - Public 成员函数 继承自 [AkVector](struct_ak_vector.html) | |
| [AkVector](struct_ak_vector.html) | [operator+](struct_ak_vector_a2f75dd8300184ffc4f6f88fdfcb9bf11.html#a2f75dd8300184ffc4f6f88fdfcb9bf11) (const [AkVector](struct_ak_vector.html) &b) const |
|  | |
| [AkVector](struct_ak_vector.html) | [operator-](struct_ak_vector_a26ba511565776c9c25fc045efa13db6f.html#a26ba511565776c9c25fc045efa13db6f) (const [AkVector](struct_ak_vector.html) &b) const |
|  | |
| [AkVector](struct_ak_vector.html) | [operator\*](struct_ak_vector_a21ca1d52f48022441bcb3f381aed9109.html#a21ca1d52f48022441bcb3f381aed9109) (const [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) f) const |
|  | |
| [AkVector](struct_ak_vector.html) | [operator/](struct_ak_vector_ad114c0de5097af0ebe08ed536cd16216.html#ad114c0de5097af0ebe08ed536cd16216) (const [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) f) const |
|  | |
| void | [Zero](struct_ak_vector_af613699526452cde6be672a3ff035f00.html#af613699526452cde6be672a3ff035f00) () |
|  | |
|  | [operator AkVector64](struct_ak_vector_a73ab07b0ca09d7e2243ff9d38c2b1c81.html#a73ab07b0ca09d7e2243ff9d38c2b1c81) () const |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - Public 属性 继承自 [AkVector](struct_ak_vector.html) | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [X](struct_ak_vector_ad976d2990ff1acc75d10051a7035baea.html#ad976d2990ff1acc75d10051a7035baea) |
|  | X Position [更多...](struct_ak_vector_ad976d2990ff1acc75d10051a7035baea.html#ad976d2990ff1acc75d10051a7035baea) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [Y](struct_ak_vector_a7d00da14f7e9d326592ba82a28d7bc0f.html#a7d00da14f7e9d326592ba82a28d7bc0f) |
|  | Y Position [更多...](struct_ak_vector_a7d00da14f7e9d326592ba82a28d7bc0f.html#a7d00da14f7e9d326592ba82a28d7bc0f) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [Z](struct_ak_vector_ae29b396901bdb7592f010b36bee9c868.html#ae29b396901bdb7592f010b36bee9c868) |
|  | Z Position [更多...](struct_ak_vector_ae29b396901bdb7592f010b36bee9c868.html#ae29b396901bdb7592f010b36bee9c868) |
|  | |

## 详细描述

Unique ID for portals. This ID type exists in the same ID-space as game object ID's. The client is responsible for not choosing portal ID's that conflict with registered game objects' ID's. Internally, the spatial audio rooms and portals API manages registration and un-registration of game objects that represent portals using AkPortalID's provided by the client; AkPortalID's are convertied to AkGameObjectID's by calling AsGameObjectID().

参见
:   - [AK::SpatialAudio::SetPortal](namespace_a_k_1_1_spatial_audio_aeffa58bec3569a1bac5feac3e0c370d9.html#aeffa58bec3569a1bac5feac3e0c370d9)
    - [AK::SpatialAudio::RemovePortal](namespace_a_k_1_1_spatial_audio_a6185cae414e959f5d7e270c4afe0f68f.html#a6185cae414e959f5d7e270c4afe0f68f)

在文件 [AkSpatialAudioTypes.h](_ak_spatial_audio_types_8h_source.html) 第 [162](_ak_spatial_audio_types_8h_source.html#l00162) 行定义.