# AkTriangle

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_triangle-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkTriangle结构体 参考

Triangle for a spatial audio mesh.
[更多...](struct_ak_triangle.html#details)

`#include <AkSpatialAudioTypes.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkTriangle](struct_ak_triangle_a45d10a459a16bc9484dedc37916fdc3e.html#a45d10a459a16bc9484dedc37916fdc3e) () |
|  | Constructor [更多...](struct_ak_triangle_a45d10a459a16bc9484dedc37916fdc3e.html#a45d10a459a16bc9484dedc37916fdc3e) |
|  | |
|  | [AkTriangle](struct_ak_triangle_a2c6d27652a1ca9225adbe5d058f739fc.html#a2c6d27652a1ca9225adbe5d058f739fc) ([AkVertIdx](_ak_typedefs_8h_a1a95c4ca5bc0ed5ed18a1c3a0411c4f6.html#a1a95c4ca5bc0ed5ed18a1c3a0411c4f6) in\_pt0, [AkVertIdx](_ak_typedefs_8h_a1a95c4ca5bc0ed5ed18a1c3a0411c4f6.html#a1a95c4ca5bc0ed5ed18a1c3a0411c4f6) in\_pt1, [AkVertIdx](_ak_typedefs_8h_a1a95c4ca5bc0ed5ed18a1c3a0411c4f6.html#a1a95c4ca5bc0ed5ed18a1c3a0411c4f6) in\_pt2, [AkSurfIdx](_ak_typedefs_8h_a1d462cf28f5a36878db54c59ab410fc0.html#a1d462cf28f5a36878db54c59ab410fc0) in\_surfaceInfo) |
|  | Constructor [更多...](struct_ak_triangle_a2c6d27652a1ca9225adbe5d058f739fc.html#a2c6d27652a1ca9225adbe5d058f739fc) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkVertIdx](_ak_typedefs_8h_a1a95c4ca5bc0ed5ed18a1c3a0411c4f6.html#a1a95c4ca5bc0ed5ed18a1c3a0411c4f6) | [point0](struct_ak_triangle_af614ef877ed84a7549afe7f6cf34df8e.html#af614ef877ed84a7549afe7f6cf34df8e) |
|  | Index into the vertex table passed into `AkGeometryParams` that describes the first vertex of the triangle. Triangles are double-sided, so vertex order in not important. [更多...](struct_ak_triangle_af614ef877ed84a7549afe7f6cf34df8e.html#af614ef877ed84a7549afe7f6cf34df8e) |
|  | |
| [AkVertIdx](_ak_typedefs_8h_a1a95c4ca5bc0ed5ed18a1c3a0411c4f6.html#a1a95c4ca5bc0ed5ed18a1c3a0411c4f6) | [point1](struct_ak_triangle_a35cbb7b236ff8eb4af3a423b4401e2c5.html#a35cbb7b236ff8eb4af3a423b4401e2c5) |
|  | Index into the vertex table passed into `AkGeometryParams` that describes the second vertex of the triangle. Triangles are double-sided, so vertex order in not important. [更多...](struct_ak_triangle_a35cbb7b236ff8eb4af3a423b4401e2c5.html#a35cbb7b236ff8eb4af3a423b4401e2c5) |
|  | |
| [AkVertIdx](_ak_typedefs_8h_a1a95c4ca5bc0ed5ed18a1c3a0411c4f6.html#a1a95c4ca5bc0ed5ed18a1c3a0411c4f6) | [point2](struct_ak_triangle_ad824a53f0e5dfa36ec7cd2fc88303f30.html#ad824a53f0e5dfa36ec7cd2fc88303f30) |
|  | Index into the vertex table passed into `AkGeometryParams` that describes the third vertex of the triangle. Triangles are double-sided, so vertex order in not important. [更多...](struct_ak_triangle_ad824a53f0e5dfa36ec7cd2fc88303f30.html#ad824a53f0e5dfa36ec7cd2fc88303f30) |
|  | |
| [AkSurfIdx](_ak_typedefs_8h_a1d462cf28f5a36878db54c59ab410fc0.html#a1d462cf28f5a36878db54c59ab410fc0) | [surface](struct_ak_triangle_aefb228938046af58e01307605f391171.html#aefb228938046af58e01307605f391171) |
|  | |

## 详细描述

Triangle for a spatial audio mesh.

在文件 [AkSpatialAudioTypes.h](_ak_spatial_audio_types_8h_source.html) 第 [416](_ak_spatial_audio_types_8h_source.html#l00416) 行定义.