# AkGeometryParams

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_geometry_params-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkGeometryParams结构体 参考

Parameters passed to `SetGeometry`
[更多...](struct_ak_geometry_params.html#details)

`#include <AkSpatialAudioTypes.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkGeometryParams](struct_ak_geometry_params_a9ebb5da2ace1fb9ccd42256d99b0beb9.html#a9ebb5da2ace1fb9ccd42256d99b0beb9) () |
|  | Constructor [更多...](struct_ak_geometry_params_a9ebb5da2ace1fb9ccd42256d99b0beb9.html#a9ebb5da2ace1fb9ccd42256d99b0beb9) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| struct [AkTriangle](struct_ak_triangle.html) \* | [Triangles](struct_ak_geometry_params_ab808e7f98df0ca947216913c388f1713.html#ab808e7f98df0ca947216913c388f1713) |
|  | |
| [AkTriIdx](_ak_typedefs_8h_ac81a13a3296704cf7a21c3d34241bf88.html#ac81a13a3296704cf7a21c3d34241bf88) | [NumTriangles](struct_ak_geometry_params_aa4185b0fb36392987a62aff89f1c7925.html#aa4185b0fb36392987a62aff89f1c7925) |
|  | Number of triangles in Triangles. [更多...](struct_ak_geometry_params_aa4185b0fb36392987a62aff89f1c7925.html#aa4185b0fb36392987a62aff89f1c7925) |
|  | |
| [AkVertex](struct_ak_vertex.html) \* | [Vertices](struct_ak_geometry_params_acc48f1b3060eaf1824086feed5f15c62.html#acc48f1b3060eaf1824086feed5f15c62) |
|  | |
| [AkVertIdx](_ak_typedefs_8h_a1a95c4ca5bc0ed5ed18a1c3a0411c4f6.html#a1a95c4ca5bc0ed5ed18a1c3a0411c4f6) | [NumVertices](struct_ak_geometry_params_a1a6ffe46c9c19a547b752a44c71051ca.html#a1a6ffe46c9c19a547b752a44c71051ca) |
|  | Number of vertices in Vertices. [更多...](struct_ak_geometry_params_a1a6ffe46c9c19a547b752a44c71051ca.html#a1a6ffe46c9c19a547b752a44c71051ca) |
|  | |
| struct [AkAcousticSurface](struct_ak_acoustic_surface.html) \* | [Surfaces](struct_ak_geometry_params_af7b6645b9c4b14eb2a81bd4179c946ca.html#af7b6645b9c4b14eb2a81bd4179c946ca) |
|  | |
| [AkSurfIdx](_ak_typedefs_8h_a1d462cf28f5a36878db54c59ab410fc0.html#a1d462cf28f5a36878db54c59ab410fc0) | [NumSurfaces](struct_ak_geometry_params_a7da0be30513e79a77de79c6650944fab.html#a7da0be30513e79a77de79c6650944fab) |
|  | Number of of AkTriangleInfo structures in in\_pTriangleInfo and number of AkTriIdx's in in\_infoMap. [更多...](struct_ak_geometry_params_a7da0be30513e79a77de79c6650944fab.html#a7da0be30513e79a77de79c6650944fab) |
|  | |
| bool | [EnableDiffraction](struct_ak_geometry_params_a9ae54ac73dcb4426a1905fbd3c511ca0.html#a9ae54ac73dcb4426a1905fbd3c511ca0) |
|  | Switch to enable or disable geometric diffraction for this Geometry. [更多...](struct_ak_geometry_params_a9ae54ac73dcb4426a1905fbd3c511ca0.html#a9ae54ac73dcb4426a1905fbd3c511ca0) |
|  | |
| bool | [EnableDiffractionOnBoundaryEdges](struct_ak_geometry_params_a40eab36c1d56b50441d5bce10dcbb6a9.html#a40eab36c1d56b50441d5bce10dcbb6a9) |
|  | Switch to enable or disable geometric diffraction on boundary edges for this Geometry. Boundary edges are edges that are connected to only one triangle. [更多...](struct_ak_geometry_params_a40eab36c1d56b50441d5bce10dcbb6a9.html#a40eab36c1d56b50441d5bce10dcbb6a9) |
|  | |

## 详细描述

Parameters passed to `SetGeometry`

在文件 [AkSpatialAudioTypes.h](_ak_spatial_audio_types_8h_source.html) 第 [777](_ak_spatial_audio_types_8h_source.html#l00777) 行定义.