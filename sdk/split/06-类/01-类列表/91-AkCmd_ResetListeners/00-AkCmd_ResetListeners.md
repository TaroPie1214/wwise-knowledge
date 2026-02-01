# AkCmd_ResetListeners

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___reset_listeners-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_ResetListeners结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___reset_listeners_a4e5343b4fa03f97bceb1cf79385ef656.html#a4e5343b4fa03f97bceb1cf79385ef656) |
|  | Game Object ID [更多...](struct_ak_cmd___reset_listeners_a4e5343b4fa03f97bceb1cf79385ef656.html#a4e5343b4fa03f97bceb1cf79385ef656) |
|  | |

## 详细描述

Resets the listener associations to the default listener(s). This will also reset per-listener gains that may have been set.

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` is outside the valid range
- AK\_IDNotFound: `gameObjectID` is not a registered game object ID.

参见
:   - [AkCommand\_ResetListeners](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda03865610c80e1789db0c82c82387871d "See AkCmd_ResetListeners")
    - [集成 Listener](soundengine_listeners.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [382](_ak_command_types_8h_source.html#l00382) 行定义.