# AkMatrix3x3

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_matrix3x3-members.html) |
[Public 成员函数](#pub-methods) |
[静态 Public 成员函数](#pub-static-methods) |
[Public 属性](#pub-attribs)

AkMatrix3x3类 参考

`#include <AkVectors.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkMatrix3x3](class_ak_matrix3x3_a53500ac83f75a61b0cb3b2b3ed12a967.html#a53500ac83f75a61b0cb3b2b3ed12a967) ()=default |
|  | |
| [AkMatrix3x3](class_ak_matrix3x3.html) & | [operator/=](class_ak_matrix3x3_a8fd0f14bd7bcc13869705e1b7171cf66.html#a8fd0f14bd7bcc13869705e1b7171cf66) (const [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) f) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) & | [operator()](class_ak_matrix3x3_afa54e9847e69116dbc94dbba8c80366e.html#afa54e9847e69116dbc94dbba8c80366e) (const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) row, const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) column) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) const [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) & | [operator()](class_ak_matrix3x3_af34d812fc4b7cd2581e6616b9beb8796.html#af34d812fc4b7cd2581e6616b9beb8796) (const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) row, const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) column) const |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) | [operator\*](class_ak_matrix3x3_a1a0cbd7dec274dbc463effd7f46b0eb0.html#a1a0cbd7dec274dbc463effd7f46b0eb0) (const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_rhs) const |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkMatrix3x3](class_ak_matrix3x3.html) & | [operator+=](class_ak_matrix3x3_ab299bbf46c1a0818daf46f216889a8b2.html#ab299bbf46c1a0818daf46f216889a8b2) (const [AkMatrix3x3](class_ak_matrix3x3.html) &in\_rhs) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkMatrix3x3](class_ak_matrix3x3.html) & | [operator\*=](class_ak_matrix3x3_ad49ed34dbfd74c9d0d128c013c0ac480.html#ad49ed34dbfd74c9d0d128c013c0ac480) (const [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) &in\_f) |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static [AkMatrix3x3](class_ak_matrix3x3.html) | [FromColumnVectors](class_ak_matrix3x3_a66077ee91ddfe35b9d7d8fd3f3348ffe.html#a66077ee91ddfe35b9d7d8fd3f3348ffe) (const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_col0, const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_col1, const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_col2) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Add](class_ak_matrix3x3_a5f20b31ea3cc6698d77ead6b87f2161d.html#a5f20b31ea3cc6698d77ead6b87f2161d) ([AkMatrix3x3](class_ak_matrix3x3.html) &out\_res, const [AkMatrix3x3](class_ak_matrix3x3.html) &in\_m0, const [AkMatrix3x3](class_ak_matrix3x3.html) &in\_m1) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Diagonal](class_ak_matrix3x3_a0a98518a78009623cb8d85fa06187eec.html#a0a98518a78009623cb8d85fa06187eec) ([AkMatrix3x3](class_ak_matrix3x3.html) &out\_mat, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_f) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [CrossProductMatrix](class_ak_matrix3x3_a3a17661f6d3b2f8916353a1407402a46.html#a3a17661f6d3b2f8916353a1407402a46) ([AkMatrix3x3](class_ak_matrix3x3.html) &out\_mat, const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_u) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [OuterProduct](class_ak_matrix3x3_a55bfcf11267da22ae57bf2cd8b03cf98.html#a55bfcf11267da22ae57bf2cd8b03cf98) ([AkMatrix3x3](class_ak_matrix3x3.html) &out\_mat, const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_v0, const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_v1) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Rotation](class_ak_matrix3x3_a64c50009707ba16e2d35f793a8de1b25.html#a64c50009707ba16e2d35f793a8de1b25) ([AkMatrix3x3](class_ak_matrix3x3.html) &out\_mat, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_angle, const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_axis) |
|  | |
| static void | [Rotation](class_ak_matrix3x3_ac9cbe1c5a789927d5f23043a5b944595.html#ac9cbe1c5a789927d5f23043a5b944595) ([AkMatrix3x3](class_ak_matrix3x3.html) &out\_mat, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_sin, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_cos, const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_axis) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [m\_Data](class_ak_matrix3x3_a3cf4cdfa6903f792781045efe0dfce4d.html#a3cf4cdfa6903f792781045efe0dfce4d) [3][3] |
|  | |

## 详细描述

在文件 [AkVectors.h](_ak_vectors_8h_source.html) 第 [923](_ak_vectors_8h_source.html#l00923) 行定义.