# AkMotionSinkScePadHelpers.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Plugin](dir_815d3776a7d381c10e5f611b84aea7f6.html)

[命名空间](#namespaces) |
[宏定义](#define-members) |
[类型定义](#typedef-members) |
[函数](#func-members)

AkMotionSinkScePadHelpers.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`  
`#include <windef.h>`  
`#include <pad.h>`

[浏览源代码.](_ak_motion_sink_sce_pad_helpers_8h_source.html)

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AKMOTION\_SCEPAD\_HAPTICS\_MODE](_ak_motion_sink_sce_pad_helpers_8h_a91e2a21c12f393d50629fbffe8d12b38.html#a91e2a21c12f393d50629fbffe8d12b38)   0x80000000 |
|  | |
| #define | [AKMOTIONSINK\_STATIC\_LINK\_SCEPAD\_FUNCTIONS](_ak_motion_sink_sce_pad_helpers_8h_a719c39606c82fd8636d8d1b0f991a6c6.html#a719c39606c82fd8636d8d1b0f991a6c6) |
|  | |
| #define | [AKMOTIONSINK\_DYNAMIC\_LINK\_SCEPAD\_FUNCTIONS](_ak_motion_sink_sce_pad_helpers_8h_a2366feb62e611151e7c850ae476e63fb.html#a2366feb62e611151e7c850ae476e63fb) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef int(\* | [AK::\_akmotionPadGetHandle](namespace_a_k_a53e5cc6d1819969a882e31a66508cb1c.html#a53e5cc6d1819969a882e31a66508cb1c)) (int userId, int type, int index) |
|  | |
| typedef int(\* | [AK::\_akmotionPadGetContainerIdInformation](namespace_a_k_ada85e6ec496159efd79cfd7bb936f867.html#ada85e6ec496159efd79cfd7bb936f867)) (int handle, void \*pInfo) |
|  | |
| typedef int(\* | [AK::\_akmotionPadGetControllerType](namespace_a_k_a94ac7044e239dc2d9db6f383de7e027d.html#a94ac7044e239dc2d9db6f383de7e027d)) (int handle, void \*pControllerType) |
|  | |
| typedef int(\* | [AK::\_akmotionPadSetVibrationMode](namespace_a_k_a6452f9f30a12ab53971e8e74828f06a1.html#a6452f9f30a12ab53971e8e74828f06a1)) (int handle, ScePadVibrationMode mode) |
|  | |
| typedef int(\* | [AK::\_akmotionPadSetVibration](namespace_a_k_a8bff83e14f6785426bc63cac42452dbd.html#a8bff83e14f6785426bc63cac42452dbd)) (int handle, const void \*pParam) |
|  | |
| typedef int(\* | [AK::\_akmotionPadGetControllerBusType](namespace_a_k_a76c215c171faf9ae4647d79f8bc5ea8e.html#a76c215c171faf9ae4647d79f8bc5ea8e)) (int handle, void \*pBusType) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| [AK\_DLLEXPORT](_platforms_2_windows_2_ak_types_8h_ab291f969500ebc378f2344e1477d2dd7.html#ab291f969500ebc378f2344e1477d2dd7) void | [AkMotionInitializeScePadFunctions](_ak_motion_sink_sce_pad_helpers_8h_a86e939e029e9214f697980de37446855.html#a86e939e029e9214f697980de37446855) ([AK::\_akmotionPadGetHandle](namespace_a_k_a53e5cc6d1819969a882e31a66508cb1c.html#a53e5cc6d1819969a882e31a66508cb1c) in\_pPadGetHandle, [AK::\_akmotionPadGetContainerIdInformation](namespace_a_k_ada85e6ec496159efd79cfd7bb936f867.html#ada85e6ec496159efd79cfd7bb936f867) in\_pPadGetContainerIdInformation, [AK::\_akmotionPadGetControllerType](namespace_a_k_a94ac7044e239dc2d9db6f383de7e027d.html#a94ac7044e239dc2d9db6f383de7e027d) in\_pPadGetControllerType, [AK::\_akmotionPadSetVibrationMode](namespace_a_k_a6452f9f30a12ab53971e8e74828f06a1.html#a6452f9f30a12ab53971e8e74828f06a1) in\_pPadSetVibrationMode, [AK::\_akmotionPadSetVibration](namespace_a_k_a8bff83e14f6785426bc63cac42452dbd.html#a8bff83e14f6785426bc63cac42452dbd) in\_pPadSetVibration, [AK::\_akmotionPadGetControllerBusType](namespace_a_k_a76c215c171faf9ae4647d79f8bc5ea8e.html#a76c215c171faf9ae4647d79f8bc5ea8e) in\_pPadGetControllerBusType) |
|  | |