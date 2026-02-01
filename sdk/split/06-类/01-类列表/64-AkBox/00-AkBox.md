# AkBox

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_box-members.html) |
[Public 成员函数](#pub-methods)

AkBox类 参考

`#include <AkVectors.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkBox](class_ak_box_ac84c02ac157f1786e842825a86b7f7fa.html#ac84c02ac157f1786e842825a86b7f7fa) ()=default |
|  | |
| void | [Init](class_ak_box_aec3fde39a868f0597230f18807e59165.html#aec3fde39a868f0597230f18807e59165) (const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_center, const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_extent, const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_Front, const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_Up) |
|  | |
| bool | [IsPointInBox](class_ak_box_a650e6a44e10c1373abd5b0ef040bd8d4.html#a650e6a44e10c1373abd5b0ef040bd8d4) (const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_Point) const |
|  | |
| [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) | [GetSize](class_ak_box_a8322b68c069d13e1535cb1b28d5ccc2d.html#a8322b68c069d13e1535cb1b28d5ccc2d) () const |
|  | |
| [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) | [GetCenter](class_ak_box_a48844f531231743d9418a219f034e3fe.html#a48844f531231743d9418a219f034e3fe) () const |
|  | |
| [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) | [GetUx](class_ak_box_aed669d5305548ee4f575bbfc72040545.html#aed669d5305548ee4f575bbfc72040545) () const |
|  | |
| [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) | [GetUy](class_ak_box_aae33e5f500207ee1257e34bc870736e9.html#aae33e5f500207ee1257e34bc870736e9) () const |
|  | |
| [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) | [GetUz](class_ak_box_a50e2a6a3ced2784abb88ead5b3291ab4.html#a50e2a6a3ced2784abb88ead5b3291ab4) () const |
|  | |
| [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) | [GetFront](class_ak_box_abc7b60499a04081b91c9cbf8388099ff.html#abc7b60499a04081b91c9cbf8388099ff) () const |
|  | |
| [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) | [GetUp](class_ak_box_a5082ac092ca7042fdb6ae5aa57139d5c.html#a5082ac092ca7042fdb6ae5aa57139d5c) () const |
|  | |
| [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) | [GetSide](class_ak_box_aa4c739624d62db8312d84931d60d22f2.html#aa4c739624d62db8312d84931d60d22f2) () const |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [GetVolume](class_ak_box_a6a69daee73fa9787f0b62af1b42131ed.html#a6a69daee73fa9787f0b62af1b42131ed) () const |
|  | |
| bool | [SeparatingAxisExists](class_ak_box_a47585bbeca42be21f238eea7ba0ee351.html#a47585bbeca42be21f238eea7ba0ee351) (const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &L, const [AkBox](class_ak_box.html) &B) const |
|  | |
| void | [UpdateBoundingBox](class_ak_box_ace62abc8a6195121b8281e0879ef2cd7.html#ace62abc8a6195121b8281e0879ef2cd7) ([AkBoundingBox](_ak_vectors_8h_a2a62153af07be7820923ceaef12f18fe.html#a2a62153af07be7820923ceaef12f18fe) &out\_aabb) const |
|  | |

## 详细描述

在文件 [AkVectors.h](_ak_vectors_8h_source.html) 第 [1839](_ak_vectors_8h_source.html#l01839) 行定义.