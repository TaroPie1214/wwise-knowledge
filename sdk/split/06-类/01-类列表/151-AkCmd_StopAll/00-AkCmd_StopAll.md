# AkCmd_StopAll

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___stop_all-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_StopAll结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___stop_all_a380fdcf2501c29b47227174b1b4a5d23.html#a380fdcf2501c29b47227174b1b4a5d23) |
|  | Game Object ID; set to AK\_INVALID\_GAME\_OBJECT to stop all sounds. [更多...](struct_ak_cmd___stop_all_a380fdcf2501c29b47227174b1b4a5d23.html#a380fdcf2501c29b47227174b1b4a5d23) |
|  | |

## 详细描述

Stops the current content playing associated to the specified game object ID. If no game object is specified, all sounds will be stopped.

This command can fail for the following reasons:

- AK\_InsufficientMemory: Failed to allocate memory necessary to begin processing the command
- AK\_IDNotFound: `gameObjectID` was specified but is not a registered game object.

参见
:   [AkCommand\_StopAll](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdac83100924ce85da8060bfb1f37495f33 "See AkCmd_StopAll")

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [572](_ak_command_types_8h_source.html#l00572) 行定义.