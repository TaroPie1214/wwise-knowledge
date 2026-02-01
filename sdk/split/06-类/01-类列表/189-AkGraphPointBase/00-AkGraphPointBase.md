# AkGraphPointBase

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_graph_point_base-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkGraphPointBase< VALUE\_TYPE > 模板结构体 参考

Type for a point in an RTPC or Attenuation curve.
[更多...](struct_ak_graph_point_base.html#details)

`#include <AkSoundEngineTypes.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkGraphPointBase](struct_ak_graph_point_base_ab8d082b691dbaf27ecf1ded5a66ab62f.html#ab8d082b691dbaf27ecf1ded5a66ab62f) ()=default |
|  | |
|  | [AkGraphPointBase](struct_ak_graph_point_base_a86b18a03042ed613d571dd41dd7a4b68.html#a86b18a03042ed613d571dd41dd7a4b68) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_from, VALUE\_TYPE in\_to, [AkCurveInterpolation](_ak_enums_8h_a77872044bca52a4d20324739154f2399.html#a77872044bca52a4d20324739154f2399) in\_interp) |
|  | |
| bool | [operator==](struct_ak_graph_point_base_af3429648815f9c701d47f9523d8a684c.html#af3429648815f9c701d47f9523d8a684c) (const [AkGraphPointBase](struct_ak_graph_point_base.html) &other) const |
|  | |
| bool | [operator!=](struct_ak_graph_point_base_ac991db9df08dfa25fb512d98d6b9e2ff.html#ac991db9df08dfa25fb512d98d6b9e2ff) (const [AkGraphPointBase](struct_ak_graph_point_base.html) &other) const |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [From](struct_ak_graph_point_base_a3acad2773cb2efcf74f6b9f4adc2f048.html#a3acad2773cb2efcf74f6b9f4adc2f048) |
|  | Represents the value on the X axis. [更多...](struct_ak_graph_point_base_a3acad2773cb2efcf74f6b9f4adc2f048.html#a3acad2773cb2efcf74f6b9f4adc2f048) |
|  | |
| VALUE\_TYPE | [To](struct_ak_graph_point_base_a0a22137e028dbe743983796c75c97a20.html#a0a22137e028dbe743983796c75c97a20) |
|  | Represents the value on the Y axis. [更多...](struct_ak_graph_point_base_a0a22137e028dbe743983796c75c97a20.html#a0a22137e028dbe743983796c75c97a20) |
|  | |
| [AkCurveInterpolation](_ak_enums_8h_a77872044bca52a4d20324739154f2399.html#a77872044bca52a4d20324739154f2399) | [Interp](struct_ak_graph_point_base_a03ab976f1d5a0c561881d401a525a3de.html#a03ab976f1d5a0c561881d401a525a3de) |
|  | The shape of the interpolation curve between this point and the next. [更多...](struct_ak_graph_point_base_a03ab976f1d5a0c561881d401a525a3de.html#a03ab976f1d5a0c561881d401a525a3de) |
|  | |

## 详细描述

### template<class VALUE\_TYPE> struct AkGraphPointBase< VALUE\_TYPE >

Type for a point in an RTPC or Attenuation curve.

在文件 [AkSoundEngineTypes.h](_ak_sound_engine_types_8h_source.html) 第 [327](_ak_sound_engine_types_8h_source.html#l00327) 行定义.