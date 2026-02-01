# Ak3dData

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak3d_data-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

Ak3dData结构体 参考

`#include <AkCommonDefs.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [Ak3dData](struct_ak3d_data_adc7bb6f76a3283edc2660604150c9e89.html#adc7bb6f76a3283edc2660604150c9e89) () |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkTransform](struct_ak_transform.html) | [xform](struct_ak3d_data_a175ec6a58f0c97ab2070e23eb2b016db.html#a175ec6a58f0c97ab2070e23eb2b016db) |
|  | Object position / orientation. [更多...](struct_ak3d_data_a175ec6a58f0c97ab2070e23eb2b016db.html#a175ec6a58f0c97ab2070e23eb2b016db) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [spread](struct_ak3d_data_abfb9e8ec0c2ce93cac44104256947220.html#abfb9e8ec0c2ce93cac44104256947220) |
|  | Spread [0,1] [更多...](struct_ak3d_data_abfb9e8ec0c2ce93cac44104256947220.html#abfb9e8ec0c2ce93cac44104256947220) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [focus](struct_ak3d_data_ab1cbcf35d13b65c2332eaaaf6a9de161.html#ab1cbcf35d13b65c2332eaaaf6a9de161) |
|  | Focus [0,1] [更多...](struct_ak3d_data_ab1cbcf35d13b65c2332eaaaf6a9de161.html#ab1cbcf35d13b65c2332eaaaf6a9de161) |
|  | |
| [AkChannelMask](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) | [uEmitterChannelMask](struct_ak3d_data_aecd52f23daa16c434f33ec487c92daa8.html#aecd52f23daa16c434f33ec487c92daa8) |
|  | Emitter channel mask. With 3D spatialization, zeroed channels should be dropped. [更多...](struct_ak3d_data_aecd52f23daa16c434f33ec487c92daa8.html#aecd52f23daa16c434f33ec487c92daa8) |
|  | |

## 详细描述

3D data needed for 3D spatialization. Undergoes transformations based on emitter-listener placement.

在文件 [AkCommonDefs.h](_ak_common_defs_8h_source.html) 第 [236](_ak_common_defs_8h_source.html#l00236) 行定义.