# Ak3DObjects.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[类型定义](#typedef-members) |
[函数](#func-members) |
[变量](#var-members)

Ak3DObjects.h 文件参考

`#include <AK/SoundEngine/Common/AkTypedefs.h>`  
`#include <AK/SoundEngine/Common/AkEnums.h>`

[浏览源代码.](_ak3_d_objects_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkVector64](struct_ak_vector64.html) |
|  | 3D 64-bit vector. Intended as storage for world positions of sounds and objects, benefiting from 64-bit precision range [更多...](struct_ak_vector64.html#details) |
|  | |
| struct | [AkVector](struct_ak_vector.html) |
|  | 3D vector for some operations in 3D space. Typically intended only for localized calculations due to 32-bit precision [更多...](struct_ak_vector.html#details) |
|  | |
| struct | [AkListenerPosition](struct_ak_world_transform.html) |
|  | Position and orientation of game objects in the world (i.e. supports 64-bit-precision position) [更多...](struct_ak_world_transform.html#details) |
|  | |
| struct | [AkTransform](struct_ak_transform.html) |
|  | Position and orientation of objects in a "local" space [更多...](struct_ak_transform.html#details) |
|  | |
| struct | [AkChannelEmitter](struct_ak_channel_emitter.html) |
|  | Positioning information for a sound, with specified subset of its channels. [更多...](struct_ak_channel_emitter.html#details) |
|  | |
| struct | [AkPolarCoord](struct_ak_polar_coord.html) |
|  | Polar coordinates. [更多...](struct_ak_polar_coord.html#details) |
|  | |
| struct | [AkSphericalCoord](struct_ak_spherical_coord.html) |
|  | Spherical coordinates. [更多...](struct_ak_spherical_coord.html#details) |
|  | |
| class | [AkEmitterListenerPair](class_ak_emitter_listener_pair.html) |
|  | Emitter-listener pair: Positioning data pertaining to a single pair of emitter and listener. [更多...](class_ak_emitter_listener_pair.html#details) |
|  | |
| struct | [AkListener](struct_ak_listener.html) |
|  | Listener information. [更多...](struct_ak_listener.html#details) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::MultiPositionType](namespace_a_k_ab7a338fa17fa33066eb196f68c41a0d1.html#ab7a338fa17fa33066eb196f68c41a0d1) = [AkMultiPositionType](_ak_enums_8h_a751ba836dfd5edf52ceaab00cf74b6c1.html#a751ba836dfd5edf52ceaab00cf74b6c1) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| [AkVector](struct_ak_vector.html) | [AK::ConvertAkVector64ToAkVector](namespace_a_k_a6595381923e87c21d2ce7ed68f359144.html#a6595381923e87c21d2ce7ed68f359144) ([AkVector64](struct_ak_vector64.html) in) |
|  | |
| [AkTransform](struct_ak_transform.html) | [AK::ConvertAkWorldTransformToAkTransform](namespace_a_k_a12910f4fb79dd677e70f5b81df9f5724.html#a12910f4fb79dd677e70f5b81df9f5724) ([AkWorldTransform](struct_ak_world_transform.html) in) |
|  | |
| [AkVector64](struct_ak_vector64.html) | [AK::ConvertAkVectorToAkVector64](namespace_a_k_a870136dee7702f30a63cbd0b4c3d8b7f.html#a870136dee7702f30a63cbd0b4c3d8b7f) ([AkVector](struct_ak_vector.html) in) |
|  | |
| [AkWorldTransform](struct_ak_world_transform.html) | [AK::ConvertAkTransformToAkWorldTransform](namespace_a_k_a6bf504a261fee91ff4d87b49b01f1860.html#a6bf504a261fee91ff4d87b49b01f1860) ([AkTransform](struct_ak_transform.html) in) |
|  | |

|  |  |
| --- | --- |
| 变量 | |
| const [AkMultiPositionType](_ak_enums_8h_a751ba836dfd5edf52ceaab00cf74b6c1.html#a751ba836dfd5edf52ceaab00cf74b6c1) | [AK::MultiPositionType\_SingleSource](namespace_a_k_adaa0006bcac5d5330d863f1866748e8c.html#adaa0006bcac5d5330d863f1866748e8c) = [AkMultiPositionType\_SingleSource](_ak_enums_8h_a751ba836dfd5edf52ceaab00cf74b6c1.html#a751ba836dfd5edf52ceaab00cf74b6c1a83d2386681ceca38acecdbf16db6e954) |
|  | |
| const [AkMultiPositionType](_ak_enums_8h_a751ba836dfd5edf52ceaab00cf74b6c1.html#a751ba836dfd5edf52ceaab00cf74b6c1) | [AK::MultiPositionType\_MultiSources](namespace_a_k_af34c486ceb06ec577746d9a7c8120258.html#af34c486ceb06ec577746d9a7c8120258) = [AkMultiPositionType\_MultiSources](_ak_enums_8h_a751ba836dfd5edf52ceaab00cf74b6c1.html#a751ba836dfd5edf52ceaab00cf74b6c1ae3bd14aad82745c91fcc0265e5f2ad30) |
|  | |
| const [AkMultiPositionType](_ak_enums_8h_a751ba836dfd5edf52ceaab00cf74b6c1.html#a751ba836dfd5edf52ceaab00cf74b6c1) | [AK::MultiPositionType\_MultiDirections](namespace_a_k_ac6788fc121b2e7307b5d06ef53e12bc1.html#ac6788fc121b2e7307b5d06ef53e12bc1) = [AkMultiPositionType\_MultiDirections](_ak_enums_8h_a751ba836dfd5edf52ceaab00cf74b6c1.html#a751ba836dfd5edf52ceaab00cf74b6c1a072046d039ae51e407db9b962381d357) |
|  | |
| const [AkMultiPositionType](_ak_enums_8h_a751ba836dfd5edf52ceaab00cf74b6c1.html#a751ba836dfd5edf52ceaab00cf74b6c1) | [AK::MultiPositionType\_Last](namespace_a_k_a2888f5a7786ba7f89c4ed963a55ee0cc.html#a2888f5a7786ba7f89c4ed963a55ee0cc) = [AkMultiPositionType\_Last](_ak_enums_8h_a751ba836dfd5edf52ceaab00cf74b6c1.html#a751ba836dfd5edf52ceaab00cf74b6c1a3907165872c7073f6d3a8ffa89702713) |
|  | |