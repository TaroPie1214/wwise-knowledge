# TBoundingBox

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_t_bounding_box-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

TBoundingBox< TReal > 模板结构体 参考

`#include <AkVectors.h>`

|  |  |
| --- | --- |
| Public 类型 | |
| using | [TVectorType](struct_t_bounding_box_a753f9ec458083e80c5fed60d7647f8e4.html#a753f9ec458083e80c5fed60d7647f8e4) = [T3DVector](class_t3_d_vector.html)< TReal > |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [TBoundingBox](struct_t_bounding_box_ac69dba04b76dba6fb6a84b6f60b36948.html#ac69dba04b76dba6fb6a84b6f60b36948) (const [TVectorType](struct_t_bounding_box_a753f9ec458083e80c5fed60d7647f8e4.html#a753f9ec458083e80c5fed60d7647f8e4) &in\_min, const [TVectorType](struct_t_bounding_box_a753f9ec458083e80c5fed60d7647f8e4.html#a753f9ec458083e80c5fed60d7647f8e4) &in\_max) |
|  | |
|  | [TBoundingBox](struct_t_bounding_box_aafedf223931eee873856f3fa5d3f5ddc.html#aafedf223931eee873856f3fa5d3f5ddc) () |
|  | |
| void | [Update](struct_t_bounding_box_a472f91fafa47b2df55dffdad21cc7151.html#a472f91fafa47b2df55dffdad21cc7151) (const [TVectorType](struct_t_bounding_box_a753f9ec458083e80c5fed60d7647f8e4.html#a753f9ec458083e80c5fed60d7647f8e4) &in\_point) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [IsWithin](struct_t_bounding_box_a8e6f8f24302948d931a2869235b6d9f6.html#a8e6f8f24302948d931a2869235b6d9f6) (const [TVectorType](struct_t_bounding_box_a753f9ec458083e80c5fed60d7647f8e4.html#a753f9ec458083e80c5fed60d7647f8e4) &in\_Point) const |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [IsWithin](struct_t_bounding_box_af9a149c8ce760dcdff399183bcceff0b.html#af9a149c8ce760dcdff399183bcceff0b) (const [TBoundingBox](struct_t_bounding_box.html) &in\_BB) const |
|  | |
| [TBoundingBox](struct_t_bounding_box.html) | [Intersect](struct_t_bounding_box_a7b103b0de48fdabc362997f717835d14.html#a7b103b0de48fdabc362997f717835d14) (const [TBoundingBox](struct_t_bounding_box.html) &in\_BB) const |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [IsEmpty](struct_t_bounding_box_a163195fc1db98419c67597edb1592b47.html#a163195fc1db98419c67597edb1592b47) () const |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [IsValid](struct_t_bounding_box_a15ea4c9a27913bdf6670db6e92a5d94f.html#a15ea4c9a27913bdf6670db6e92a5d94f) () const |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [TVectorType](struct_t_bounding_box_a753f9ec458083e80c5fed60d7647f8e4.html#a753f9ec458083e80c5fed60d7647f8e4) | [m\_Min](struct_t_bounding_box_ad06627c5e9e117950124707bbb2fd79b.html#ad06627c5e9e117950124707bbb2fd79b) |
|  | |
| [TVectorType](struct_t_bounding_box_a753f9ec458083e80c5fed60d7647f8e4.html#a753f9ec458083e80c5fed60d7647f8e4) | [m\_Max](struct_t_bounding_box_a44db510d9a94832875643016aa233dd8.html#a44db510d9a94832875643016aa233dd8) |
|  | |

## 详细描述

### template<typename TReal> struct TBoundingBox< TReal >

在文件 [AkVectors.h](_ak_vectors_8h_source.html) 第 [1760](_ak_vectors_8h_source.html#l01760) 行定义.