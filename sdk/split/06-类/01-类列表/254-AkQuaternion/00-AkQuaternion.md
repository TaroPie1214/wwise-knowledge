# AkQuaternion

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_quaternion-members.html) |
[Public 成员函数](#pub-methods) |
[静态 Public 成员函数](#pub-static-methods) |
[Public 属性](#pub-attribs)

AkQuaternion类 参考

`#include <AkVectors.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkQuaternion](class_ak_quaternion_a95e000e9e0d668651d90ab851cfddc26.html#a95e000e9e0d668651d90ab851cfddc26) () |
|  | |
|  | [AkQuaternion](class_ak_quaternion_a75465b723ffd76b8f05f0ea24f82cc6c.html#a75465b723ffd76b8f05f0ea24f82cc6c) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_W, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_X, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_Y, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_Z) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [Length](class_ak_quaternion_abee0b5b856ced608403f8952b2628303.html#abee0b5b856ced608403f8952b2628303) () const |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkQuaternion](class_ak_quaternion.html) & | [Normalize](class_ak_quaternion_a5f2807922f749c3efe4e4e77cef084a4.html#a5f2807922f749c3efe4e4e77cef084a4) () |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkQuaternion](class_ak_quaternion.html) | [Inverse](class_ak_quaternion_a7b5d1ae21c5f5b31bb66e9a27a75e83d.html#a7b5d1ae21c5f5b31bb66e9a27a75e83d) () const |
|  | |
|  | [AkQuaternion](class_ak_quaternion_a14333e18683ff045b0272475aa00aebb.html#a14333e18683ff045b0272475aa00aebb) (const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_v0, const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_v1) |
|  | |
|  | [AkQuaternion](class_ak_quaternion_a989733066797e68eda2122a571228b7f.html#a989733066797e68eda2122a571228b7f) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_angle, const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_axis) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkQuaternion](class_ak_quaternion.html) | [operator\*](class_ak_quaternion_aa5571803e3153db4619510f817dfbbcb.html#aa5571803e3153db4619510f817dfbbcb) (const [AkQuaternion](class_ak_quaternion.html) &Q) const |
|  | Quaternion multiplication. [更多...](class_ak_quaternion_aa5571803e3153db4619510f817dfbbcb.html#aa5571803e3153db4619510f817dfbbcb) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [Ak3DVector32](_ak_vectors_8h_a10dfe93082d602867c1902a489811cf5.html#a10dfe93082d602867c1902a489811cf5) | [operator\*](class_ak_quaternion_af399ad839384d82ea5532feedf716246.html#af399ad839384d82ea5532feedf716246) (const [Ak3DVector32](_ak_vectors_8h_a10dfe93082d602867c1902a489811cf5.html#a10dfe93082d602867c1902a489811cf5) &in\_v) const |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) | [RotateVector](class_ak_quaternion_a5e5bdd78d081b5b5c140c375190d7dc9.html#a5e5bdd78d081b5b5c140c375190d7dc9) (const [Ak3DVector32](_ak_vectors_8h_a10dfe93082d602867c1902a489811cf5.html#a10dfe93082d602867c1902a489811cf5) &in\_v) const |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) | [UnrotateVector](class_ak_quaternion_acee59710533d7b81be2e6c52978e5f23.html#acee59710533d7b81be2e6c52978e5f23) (const [Ak3DVector32](_ak_vectors_8h_a10dfe93082d602867c1902a489811cf5.html#a10dfe93082d602867c1902a489811cf5) &in\_v) const |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static [AkQuaternion](class_ak_quaternion.html) | [FromRotationMatrix](class_ak_quaternion_a26f665813a1b9b6996a387a465c4968d.html#a26f665813a1b9b6996a387a465c4968d) (const [AkMatrix3x3](class_ak_matrix3x3.html) &in\_mat) |
|  | |
| static [AkQuaternion](class_ak_quaternion.html) | [FromEulers](class_ak_quaternion_a769925cb2b779e63a1fedee57c00442e.html#a769925cb2b779e63a1fedee57c00442e) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_x, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_y, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_z) |
|  | |
| static [AkQuaternion](class_ak_quaternion.html) | [FromAngleAndAxis](class_ak_quaternion_abcbb4dd1bfdb00b8f5988d01a6e5c850.html#abcbb4dd1bfdb00b8f5988d01a6e5c850) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_angle, const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_axis) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [W](class_ak_quaternion_a405f37707a178ef766b5d7cd57cfc2ed.html#a405f37707a178ef766b5d7cd57cfc2ed) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [X](class_ak_quaternion_ac73cad91a1db6a37bfcf413e49d93b3c.html#ac73cad91a1db6a37bfcf413e49d93b3c) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [Y](class_ak_quaternion_a1937e9a4d84a344090e7b923a64642cb.html#a1937e9a4d84a344090e7b923a64642cb) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [Z](class_ak_quaternion_a9f10bf33b452874743636a34fead61b7.html#a9f10bf33b452874743636a34fead61b7) |
|  | |

## 详细描述

在文件 [AkVectors.h](_ak_vectors_8h_source.html) 第 [1051](_ak_vectors_8h_source.html#l01051) 行定义.