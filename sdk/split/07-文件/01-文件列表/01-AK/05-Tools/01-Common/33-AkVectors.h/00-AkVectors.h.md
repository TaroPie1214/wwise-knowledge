# AkVectors.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)

[类](#nested-classes) |
[宏定义](#define-members) |
[类型定义](#typedef-members) |
[函数](#func-members)

AkVectors.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`  
`#include <AK/SoundEngine/Common/AkSimd.h>`  
`#include <AK/SoundEngine/Common/AkSpeakerVolumes.h>`  
`#include <AK/SoundEngine/Common/IAkPluginMemAlloc.h>`  
`#include <AK/Tools/Common/AkArray.h>`  
`#include <math.h>`  
`#include <stdio.h>`  
`#include <float.h>`

[浏览源代码.](_ak_vectors_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| class | [Ak4DVector](class_ak4_d_vector.html) |
|  | |
| struct | [Ak3DIntVector](struct_ak3_d_int_vector.html) |
|  | |
| class | [RealPrecision< AkReal32 >](class_real_precision_3_01_ak_real32_01_4.html) |
|  | |
| class | [RealPrecision< AkReal64 >](class_real_precision_3_01_ak_real64_01_4.html) |
|  | |
| class | [AkImplicitConversion](class_ak_implicit_conversion.html) |
|  | |
| class | [AkSafeConversion](class_ak_safe_conversion.html) |
|  | |
| class | [T3DVector< TDataType >](class_t3_d_vector.html) |
|  | |
| class | [Ak2DVector](class_ak2_d_vector.html) |
|  | |
| class | [AkMatrix4x4](class_ak_matrix4x4.html) |
|  | |
| class | [AkMatrix3x3](class_ak_matrix3x3.html) |
|  | |
| class | [AkQuaternion](class_ak_quaternion.html) |
|  | |
| struct | [AkIntersectionPoints](struct_ak_intersection_points.html) |
|  | |
| class | [AkLine](class_ak_line.html) |
|  | |
| class | [AkPlane](class_ak_plane.html) |
|  | |
| struct | [TBoundingBox< TReal >](struct_t_bounding_box.html) |
|  | |
| class | [AkBox](class_ak_box.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AKVECTORS\_PI](_ak_vectors_8h_a4b4acf3770f3e821c74951b1ecab99a6.html#a4b4acf3770f3e821c74951b1ecab99a6)   (3.1415926535897932384626433832795f) |
|  | |
| #define | [AKVECTORS\_TWOPI](_ak_vectors_8h_a0397919a5a9109f1acfc5ba12584fc59.html#a0397919a5a9109f1acfc5ba12584fc59)   (6.283185307179586476925286766559f) |
|  | |
| #define | [AKVECTORS\_PIOVERTWO](_ak_vectors_8h_a1185bdd4662b2fdc1726ffdc9beeaad0.html#a1185bdd4662b2fdc1726ffdc9beeaad0)   (1.5707963267948966192313216916398f) |
|  | |
| #define | [AKVECTORS\_EPSILON](_ak_vectors_8h_afb2d16c7b2da66b80a52325edf5d04a1.html#afb2d16c7b2da66b80a52325edf5d04a1)   (1.0e-38f) |
|  | |
| #define | [ADD](_ak_vectors_8h_abb7617f09d826a11cb78c16eac07d723.html#abb7617f09d826a11cb78c16eac07d723)(i, j)   out\_res(i,j) = in\_m0(i,j) + in\_m1(i,j) |
|  | |
| #define | [EPSILON](_ak_vectors_8h_a002b2f4894492820fe708b1b7e7c5e70.html#a002b2f4894492820fe708b1b7e7c5e70)   0.01f |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef [T3DVector](class_t3_d_vector.html)< [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) > | [Ak3DVector](_ak_vectors_8h_a209efc0dd63679f07d59b9cf3955b6ec.html#a209efc0dd63679f07d59b9cf3955b6ec) |
|  | |
| typedef [T3DVector](class_t3_d_vector.html)< [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) > | [Ak3DVector32](_ak_vectors_8h_a10dfe93082d602867c1902a489811cf5.html#a10dfe93082d602867c1902a489811cf5) |
|  | |
| typedef [T3DVector](class_t3_d_vector.html)< [AkReal64](_ak_numeral_types_8h_a3d90a976d004c34e2707f7bf48f3a39e.html#a3d90a976d004c34e2707f7bf48f3a39e) > | [Ak3DVector64](_ak_vectors_8h_ab87a23041bd1f04c89c8151219f51468.html#ab87a23041bd1f04c89c8151219f51468) |
|  | |
| typedef [TBoundingBox](struct_t_bounding_box.html)< [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) > | [AkBoundingBox](_ak_vectors_8h_a2a62153af07be7820923ceaef12f18fe.html#a2a62153af07be7820923ceaef12f18fe) |
|  | |
| typedef [TBoundingBox](struct_t_bounding_box.html)< [AkReal64](_ak_numeral_types_8h_a3d90a976d004c34e2707f7bf48f3a39e.html#a3d90a976d004c34e2707f7bf48f3a39e) > | [AkBoundingBox64](_ak_vectors_8h_a5e088938e2a027297b21511f176faf64.html#a5e088938e2a027297b21511f176faf64) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| template<typename TDataType > | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [T3DVector](class_t3_d_vector.html)< TDataType > | [operator\*](_ak_vectors_8h_aaf11aeb98fc01b40bbe0de8b673792ae.html#aaf11aeb98fc01b40bbe0de8b673792ae) (const TDataType f, const [T3DVector](class_t3_d_vector.html)< TDataType > &v) |
|  | |
| template<typename TDataType > | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [T3DVector](class_t3_d_vector.html)< TDataType > | [operator/](_ak_vectors_8h_a6db76a92804f8056d853ef264470b800.html#a6db76a92804f8056d853ef264470b800) (const TDataType f, const [T3DVector](class_t3_d_vector.html)< TDataType > &v) |
|  | |