# AkCmd_SA_UnregisterListener

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___unregister_listener-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_UnregisterListener结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___s_a___unregister_listener_a96af9bb31dab2fbc451bbf5804857646.html#a96af9bb31dab2fbc451bbf5804857646) |
|  | |

## 详细描述

Unregister a game object as a listener in the SpatialAudio API; clean up Spatial Audio listener data associated with `gameObjectID`.   
If `gameObjectID` is the current registered listener, calling this function will clear the Spatial Audio listener and Spatial Audio features will be disabled until another listener is registered. This function is optional - listener are automatically unregistered when their game object is deleted in the sound engine.

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` is not valid.

参见
:   - [AkCommand\_SA\_UnregisterListener](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda7c244e6a4352f39fa3290b5e89d1fbb8 "See AkCmd_SA_UnregisterListener")
    - [AK::SpatialAudio::UnregisterListener](namespace_a_k_1_1_spatial_audio_a7bda2871c9fd5b963fa6c33372d07b7d.html#a7bda2871c9fd5b963fa6c33372d07b7d)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1359](_ak_command_types_8h_source.html#l01359) 行定义.