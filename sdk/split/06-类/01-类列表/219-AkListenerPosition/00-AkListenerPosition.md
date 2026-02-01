# AkListenerPosition

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_world_transform-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkListenerPosition结构体 参考

Position and orientation of game objects in the world (i.e. supports 64-bit-precision position)
[更多...](struct_ak_world_transform.html#details)

`#include <Ak3DObjects.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| const [AkVector64](struct_ak_vector64.html) & | [Position](struct_ak_world_transform_a1005b9f33ceeb9650102360701be6873.html#a1005b9f33ceeb9650102360701be6873) () const |
|  | Get position vector. [更多...](struct_ak_world_transform_a1005b9f33ceeb9650102360701be6873.html#a1005b9f33ceeb9650102360701be6873) |
|  | |
| const [AkVector](struct_ak_vector.html) & | [OrientationFront](struct_ak_world_transform_af5f3f9d651a1224a7f8d2d1c748efd51.html#af5f3f9d651a1224a7f8d2d1c748efd51) () const |
|  | Get orientation front vector. [更多...](struct_ak_world_transform_af5f3f9d651a1224a7f8d2d1c748efd51.html#af5f3f9d651a1224a7f8d2d1c748efd51) |
|  | |
| const [AkVector](struct_ak_vector.html) & | [OrientationTop](struct_ak_world_transform_af6a0bc6de28d5deefe7c9a97d94a23b1.html#af6a0bc6de28d5deefe7c9a97d94a23b1) () const |
|  | Get orientation top vector. [更多...](struct_ak_world_transform_af6a0bc6de28d5deefe7c9a97d94a23b1.html#af6a0bc6de28d5deefe7c9a97d94a23b1) |
|  | |
| void | [Set](struct_ak_world_transform_abeeaf19f83184bd502370c1b980b269a.html#abeeaf19f83184bd502370c1b980b269a) (const [AkVector64](struct_ak_vector64.html) &in\_position, const [AkVector](struct_ak_vector.html) &in\_orientationFront, const [AkVector](struct_ak_vector.html) &in\_orientationTop) |
|  | Set position and orientation. Orientation front and top should be orthogonal and normalized. [更多...](struct_ak_world_transform_abeeaf19f83184bd502370c1b980b269a.html#abeeaf19f83184bd502370c1b980b269a) |
|  | |
| void | [Set](struct_ak_world_transform_a716e4b56c54609ce90732e67f10939cb.html#a716e4b56c54609ce90732e67f10939cb) ([AkReal64](_ak_numeral_types_8h_a3d90a976d004c34e2707f7bf48f3a39e.html#a3d90a976d004c34e2707f7bf48f3a39e) in\_positionX, [AkReal64](_ak_numeral_types_8h_a3d90a976d004c34e2707f7bf48f3a39e.html#a3d90a976d004c34e2707f7bf48f3a39e) in\_positionY, [AkReal64](_ak_numeral_types_8h_a3d90a976d004c34e2707f7bf48f3a39e.html#a3d90a976d004c34e2707f7bf48f3a39e) in\_positionZ, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientFrontX, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientFrontY, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientFrontZ, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientTopX, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientTopY, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientTopZ) |
|  | Set position and orientation. Orientation front and top should be orthogonal and normalized. [更多...](struct_ak_world_transform_a716e4b56c54609ce90732e67f10939cb.html#a716e4b56c54609ce90732e67f10939cb) |
|  | |
| void | [SetPosition](struct_ak_world_transform_a3b29511546d8d6dcf6cf1ccaabd7e214.html#a3b29511546d8d6dcf6cf1ccaabd7e214) (const [AkVector64](struct_ak_vector64.html) &in\_position) |
|  | Set position. [更多...](struct_ak_world_transform_a3b29511546d8d6dcf6cf1ccaabd7e214.html#a3b29511546d8d6dcf6cf1ccaabd7e214) |
|  | |
| void | [SetPosition](struct_ak_world_transform_aed1a0d4de647c4cd918758eafb287a77.html#aed1a0d4de647c4cd918758eafb287a77) ([AkReal64](_ak_numeral_types_8h_a3d90a976d004c34e2707f7bf48f3a39e.html#a3d90a976d004c34e2707f7bf48f3a39e) in\_x, [AkReal64](_ak_numeral_types_8h_a3d90a976d004c34e2707f7bf48f3a39e.html#a3d90a976d004c34e2707f7bf48f3a39e) in\_y, [AkReal64](_ak_numeral_types_8h_a3d90a976d004c34e2707f7bf48f3a39e.html#a3d90a976d004c34e2707f7bf48f3a39e) in\_z) |
|  | Set position. [更多...](struct_ak_world_transform_aed1a0d4de647c4cd918758eafb287a77.html#aed1a0d4de647c4cd918758eafb287a77) |
|  | |
| void | [SetOrientation](struct_ak_world_transform_a00d8566d46d54639f8d742b90d415fd6.html#a00d8566d46d54639f8d742b90d415fd6) (const [AkVector](struct_ak_vector.html) &in\_orientationFront, const [AkVector](struct_ak_vector.html) &in\_orientationTop) |
|  | Set orientation. Orientation front and top should be orthogonal and normalized. [更多...](struct_ak_world_transform_a00d8566d46d54639f8d742b90d415fd6.html#a00d8566d46d54639f8d742b90d415fd6) |
|  | |
| void | [SetOrientation](struct_ak_world_transform_aa8f7f14d6a8e15223e369f63aec1e42b.html#aa8f7f14d6a8e15223e369f63aec1e42b) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientFrontX, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientFrontY, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientFrontZ, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientTopX, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientTopY, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientTopZ) |
|  | Set orientation. Orientation front and top should be orthogonal and normalized. [更多...](struct_ak_world_transform_aa8f7f14d6a8e15223e369f63aec1e42b.html#aa8f7f14d6a8e15223e369f63aec1e42b) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| struct [AkVector](struct_ak_vector.html) | [orientationFront](struct_ak_world_transform_ae78435eab7143d3edb359259e6c8b81b.html#ae78435eab7143d3edb359259e6c8b81b) |
|  | Orientation of the listener [更多...](struct_ak_world_transform_ae78435eab7143d3edb359259e6c8b81b.html#ae78435eab7143d3edb359259e6c8b81b) |
|  | |
| struct [AkVector](struct_ak_vector.html) | [orientationTop](struct_ak_world_transform_afa58415d52641467688aff5377d6e3c5.html#afa58415d52641467688aff5377d6e3c5) |
|  | Top orientation of the listener [更多...](struct_ak_world_transform_afa58415d52641467688aff5377d6e3c5.html#afa58415d52641467688aff5377d6e3c5) |
|  | |
| struct [AkVector64](struct_ak_vector64.html) | [position](struct_ak_world_transform_a47c0be01ed9b42a641834d17cc196f2c.html#a47c0be01ed9b42a641834d17cc196f2c) |
|  | Position of the listener [更多...](struct_ak_world_transform_a47c0be01ed9b42a641834d17cc196f2c.html#a47c0be01ed9b42a641834d17cc196f2c) |
|  | |

## 详细描述

Position and orientation of game objects in the world (i.e. supports 64-bit-precision position)

Positioning information for a listener.

Positioning information for a sound.

在文件 [Ak3DObjects.h](_ak3_d_objects_8h_source.html) 第 [133](_ak3_d_objects_8h_source.html#l00133) 行定义.