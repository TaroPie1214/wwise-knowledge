# AkTransform

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_transform-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkTransform结构体 参考

Position and orientation of objects in a "local" space
[更多...](struct_ak_transform.html#details)

`#include <Ak3DObjects.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| const [AkVector](struct_ak_vector.html) & | [Position](struct_ak_transform_a1b2697d425ca3e8e0a5fb0faee87fcd5.html#a1b2697d425ca3e8e0a5fb0faee87fcd5) () const |
|  | Get position vector. [更多...](struct_ak_transform_a1b2697d425ca3e8e0a5fb0faee87fcd5.html#a1b2697d425ca3e8e0a5fb0faee87fcd5) |
|  | |
| const [AkVector](struct_ak_vector.html) & | [OrientationFront](struct_ak_transform_a3bd22931409f0dc23578631a2a6d50c1.html#a3bd22931409f0dc23578631a2a6d50c1) () const |
|  | Get orientation front vector. [更多...](struct_ak_transform_a3bd22931409f0dc23578631a2a6d50c1.html#a3bd22931409f0dc23578631a2a6d50c1) |
|  | |
| const [AkVector](struct_ak_vector.html) & | [OrientationTop](struct_ak_transform_a3fb8ed7b29d03c5e365b5c06320ca24e.html#a3fb8ed7b29d03c5e365b5c06320ca24e) () const |
|  | Get orientation top vector. [更多...](struct_ak_transform_a3fb8ed7b29d03c5e365b5c06320ca24e.html#a3fb8ed7b29d03c5e365b5c06320ca24e) |
|  | |
| void | [Set](struct_ak_transform_a9a46a98d7efc6486dd06956950b6f34e.html#a9a46a98d7efc6486dd06956950b6f34e) (const [AkVector](struct_ak_vector.html) &in\_position, const [AkVector](struct_ak_vector.html) &in\_orientationFront, const [AkVector](struct_ak_vector.html) &in\_orientationTop) |
|  | Set position and orientation. Orientation front and top should be orthogonal and normalized. [更多...](struct_ak_transform_a9a46a98d7efc6486dd06956950b6f34e.html#a9a46a98d7efc6486dd06956950b6f34e) |
|  | |
| void | [Set](struct_ak_transform_a3bc42dc5b00b880229c08a8ebd0db72a.html#a3bc42dc5b00b880229c08a8ebd0db72a) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_positionX, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_positionY, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_positionZ, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientFrontX, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientFrontY, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientFrontZ, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientTopX, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientTopY, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientTopZ) |
|  | Set position and orientation. Orientation front and top should be orthogonal and normalized. [更多...](struct_ak_transform_a3bc42dc5b00b880229c08a8ebd0db72a.html#a3bc42dc5b00b880229c08a8ebd0db72a) |
|  | |
| void | [SetPosition](struct_ak_transform_a5213b68637f2d661c1cd811af22bee7d.html#a5213b68637f2d661c1cd811af22bee7d) (const [AkVector](struct_ak_vector.html) &in\_position) |
|  | Set position. [更多...](struct_ak_transform_a5213b68637f2d661c1cd811af22bee7d.html#a5213b68637f2d661c1cd811af22bee7d) |
|  | |
| void | [SetPosition](struct_ak_transform_a547da374d8d6ac9a089536b69f018de8.html#a547da374d8d6ac9a089536b69f018de8) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_x, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_y, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_z) |
|  | Set position. [更多...](struct_ak_transform_a547da374d8d6ac9a089536b69f018de8.html#a547da374d8d6ac9a089536b69f018de8) |
|  | |
| void | [SetOrientation](struct_ak_transform_a9bb03962057cebf8d48a3f6f62cedcb6.html#a9bb03962057cebf8d48a3f6f62cedcb6) (const [AkVector](struct_ak_vector.html) &in\_orientationFront, const [AkVector](struct_ak_vector.html) &in\_orientationTop) |
|  | Set orientation. Orientation front and top should be orthogonal and normalized. [更多...](struct_ak_transform_a9bb03962057cebf8d48a3f6f62cedcb6.html#a9bb03962057cebf8d48a3f6f62cedcb6) |
|  | |
| void | [SetOrientation](struct_ak_transform_ae80cd8ed1198d043981e55cb5245d117.html#ae80cd8ed1198d043981e55cb5245d117) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientFrontX, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientFrontY, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientFrontZ, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientTopX, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientTopY, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_orientTopZ) |
|  | Set orientation. Orientation front and top should be orthogonal and normalized. [更多...](struct_ak_transform_ae80cd8ed1198d043981e55cb5245d117.html#ae80cd8ed1198d043981e55cb5245d117) |
|  | |
|  | [operator AkWorldTransform](struct_ak_transform_a8104721290127488455d6afb8a7291b9.html#a8104721290127488455d6afb8a7291b9) () const |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| struct [AkVector](struct_ak_vector.html) | [orientationFront](struct_ak_transform_a95751f614eb22e5dd85037631ae3f3a8.html#a95751f614eb22e5dd85037631ae3f3a8) |
|  | Orientation of the listener [更多...](struct_ak_transform_a95751f614eb22e5dd85037631ae3f3a8.html#a95751f614eb22e5dd85037631ae3f3a8) |
|  | |
| struct [AkVector](struct_ak_vector.html) | [orientationTop](struct_ak_transform_af07a88d4f0f781f176fa0a58aa14479d.html#af07a88d4f0f781f176fa0a58aa14479d) |
|  | Top orientation of the listener [更多...](struct_ak_transform_af07a88d4f0f781f176fa0a58aa14479d.html#af07a88d4f0f781f176fa0a58aa14479d) |
|  | |
| struct [AkVector](struct_ak_vector.html) | [position](struct_ak_transform_ae04e2558f563395152c12ba35d097ecb.html#ae04e2558f563395152c12ba35d097ecb) |
|  | Position of the listener [更多...](struct_ak_transform_ae04e2558f563395152c12ba35d097ecb.html#ae04e2558f563395152c12ba35d097ecb) |
|  | |

## 详细描述

Position and orientation of objects in a "local" space

在文件 [Ak3DObjects.h](_ak3_d_objects_8h_source.html) 第 [254](_ak3_d_objects_8h_source.html#l00254) 行定义.