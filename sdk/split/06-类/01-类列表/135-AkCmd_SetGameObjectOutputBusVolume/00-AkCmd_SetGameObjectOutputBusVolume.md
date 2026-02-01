# AkCmd_SetGameObjectOutputBusVolume

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_game_object_output_bus_volume-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetGameObjectOutputBusVolume结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [emitterID](struct_ak_cmd___set_game_object_output_bus_volume_a6c3ffe33541a949c867e751753c0a8ee.html#a6c3ffe33541a949c867e751753c0a8ee) |
|  | Emitter Game Object ID. [更多...](struct_ak_cmd___set_game_object_output_bus_volume_a6c3ffe33541a949c867e751753c0a8ee.html#a6c3ffe33541a949c867e751753c0a8ee) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [listenerID](struct_ak_cmd___set_game_object_output_bus_volume_af602658af8f580c0761ec5d6e9f283de.html#af602658af8f580c0761ec5d6e9f283de) |
|  | Listener Game Object ID. [更多...](struct_ak_cmd___set_game_object_output_bus_volume_af602658af8f580c0761ec5d6e9f283de.html#af602658af8f580c0761ec5d6e9f283de) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [controlValue](struct_ak_cmd___set_game_object_output_bus_volume_a1ee7cef692759ed23b593c4bea4d09e9.html#a1ee7cef692759ed23b593c4bea4d09e9) |
|  | A multiplier in the range [0.0f:16.0f] ( -∞ dB to +24 dB). [更多...](struct_ak_cmd___set_game_object_output_bus_volume_a1ee7cef692759ed23b593c4bea4d09e9.html#a1ee7cef692759ed23b593c4bea4d09e9) |
|  | |

## 详细描述

Sets the Output Bus Volume (direct) to be used for the specified game object. The control value is a number ranging from 0.0f to 1.0f. Output Bus Volumes are stored per listener association, so executing this command will override the default set of listeners. The game object `emitterID` will now reference its own set of listeners which will be the same as the old set of listeners, but with the new associated gain. Future changes to the default listener set will not be picked up by this game object unless `AkCommand_ResetListeners` is executed.

This command can fail for the following reasons:

- AK\_InvalidParameter: `emitterID` is not a valid game object ID or `controlValue` is outside the valid range.
- AK\_IDNotFound: `emitterID` is not a registered game object ID.

参见
:   - [AkCommand\_SetGameObjectOutputBusVolume](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda24263a6c13160d3d91c9c4e2b64c9fb9 "See AkCmd_SetGameObjectOutputBusVolume")
    - [AkCommand\_ResetListeners](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda03865610c80e1789db0c82c82387871d "See AkCmd_ResetListeners")
    - [集成详情——环境和游戏定义的辅助发送](soundengine_environments.html)
    - [设置主输出电平（或者干声级别）](soundengine_environments.html#soundengine_environments_setting_dry_environment)
    - [使用 ID 或字符串（Unicode 或 ANSI）](soundengine_environments.html#soundengine_environments_id_vs_string)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [467](_ak_command_types_8h_source.html#l00467) 行定义.