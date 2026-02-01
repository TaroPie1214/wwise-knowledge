# AkCmd_SA_RegisterListener

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___register_listener-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_RegisterListener结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___s_a___register_listener_a9d8d2d4be96f430aa8b7da356e97ff25.html#a9d8d2d4be96f430aa8b7da356e97ff25) |
|  | |
| bool | [primaryListener](struct_ak_cmd___s_a___register_listener_a99b9ae71952eb6b55061a8867046d2c6.html#a99b9ae71952eb6b55061a8867046d2c6) |
|  | |

## 详细描述

Assign a game object as the Spatial Audio listener. There can be only one Spatial Audio listener registered at any given time; `gameObjectID` will replace any previously set Spatial Audio listener. The game object passed in must be registered by the client, at some point, for sound to be heard. It is not necessary to be registered at the time of calling this function. If no listener is explicitly registered to spatial audio, then a default listener (set via `AK::SoundEngine::SetDefaultListeners()`) is selected. If there are no default listeners, or there are more than one default listeners, then it is necessary to call [RegisterListener()](namespace_a_k_1_1_spatial_audio_ae7fb9da6f767410842d1a47097fc8913.html#ae7fb9da6f767410842d1a47097fc8913) to specify which listener to use with Spatial Audio.

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` is not valid.

参见
:   - [AkCommand\_SA\_RegisterListener](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda5f600d5e7728ae29e9287fed9102fb3f "See AkCmd_SA_RegisterListener")
    - [AK::SpatialAudio::RegisterListener](namespace_a_k_1_1_spatial_audio_ae7fb9da6f767410842d1a47097fc8913.html#ae7fb9da6f767410842d1a47097fc8913)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1342](_ak_command_types_8h_source.html#l01342) 行定义.