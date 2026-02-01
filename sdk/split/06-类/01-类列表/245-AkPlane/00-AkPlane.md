# AkPlane

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_plane-members.html) |
[Public 成员函数](#pub-methods)

AkPlane类 参考

`#include <AkVectors.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkPlane](class_ak_plane_a32737c6177dbf84d391ed46da4de130f.html#a32737c6177dbf84d391ed46da4de130f) ()=default |
|  | |
|  | [AkPlane](class_ak_plane_a1edcd77173ae8cd9c0a54dbc91665f8d.html#a1edcd77173ae8cd9c0a54dbc91665f8d) ([Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) in\_p1, [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) in\_p2, [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) in\_p4) |
|  | |
| void | [SetPlane](class_ak_plane_ae006cfbb52fe50f7bbb2dbed862b18e6.html#ae006cfbb52fe50f7bbb2dbed862b18e6) ([Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) in\_p1, [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) in\_p2, [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) in\_p4) |
|  | |
| bool | [DoesRayIntersect](class_ak_plane_a44558e55d8fe5cdcffda5a7e2747d231.html#a44558e55d8fe5cdcffda5a7e2747d231) (const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_Origin, const [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &in\_Destination, [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &out\_Intersection) const |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [DistPoint\_to\_Plane](class_ak_plane_a92c27a5eb3d5cd50cf01833af9b4a53b.html#a92c27a5eb3d5cd50cf01833af9b4a53b) ([Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) in\_P, [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) &out\_B) const |
|  | |
| void | [SetReflection](class_ak_plane_a405e0e1057517ea2e12410beabba65cc.html#a405e0e1057517ea2e12410beabba65cc) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \*out\_mat) const |
|  | |
| [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) | [GetN](class_ak_plane_a0c22ed6c0fa69bc59dfd8f4854295851.html#a0c22ed6c0fa69bc59dfd8f4854295851) () const |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [GetD](class_ak_plane_adb98bf90f7c3d77b103b2299dbb9631f.html#adb98bf90f7c3d77b103b2299dbb9631f) () const |
|  | |
| bool | [FindIntersectionPoints](class_ak_plane_afa3174073a07801c88f1f019cd4e0946.html#afa3174073a07801c88f1f019cd4e0946) (const [AkPlane](class_ak_plane.html) &in\_PlaneB, [AkIntersectionPoints](struct_ak_intersection_points.html) &out\_Intrs) const |
|  | |
| [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) | [GetP1](class_ak_plane_a6c87946e208be455cfab0c3d7adca6ac.html#a6c87946e208be455cfab0c3d7adca6ac) () const |
|  | |
| [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) | [GetP2](class_ak_plane_ac64af2c21f5520acb525b4d987d15563.html#ac64af2c21f5520acb525b4d987d15563) () const |
|  | |
| [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) | [GetP4](class_ak_plane_a4244918da5107889fdd165fa5985c9bf.html#a4244918da5107889fdd165fa5985c9bf) () const |
|  | |

## 详细描述

在文件 [AkVectors.h](_ak_vectors_8h_source.html) 第 [1378](_ak_vectors_8h_source.html#l01378) 行定义.