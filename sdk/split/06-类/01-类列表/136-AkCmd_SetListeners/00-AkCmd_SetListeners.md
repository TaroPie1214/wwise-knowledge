# AkCmd_SetListeners

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_listeners-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetListeners结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___set_listeners_aa7fa22efa253000ec63e28b01b86f962.html#aa7fa22efa253000ec63e28b01b86f962) |
|  | Game Object ID [更多...](struct_ak_cmd___set_listeners_aa7fa22efa253000ec63e28b01b86f962.html#aa7fa22efa253000ec63e28b01b86f962) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [operation](struct_ak_cmd___set_listeners_a8f6012d1615b1637cf27db9f88ba8011.html#a8f6012d1615b1637cf27db9f88ba8011) |
|  | Type of operation, see [AkListenerOp](_ak_enums_8h_a76a5fdc9e33cbd5441aafd1f760fe8b6.html#a76a5fdc9e33cbd5441aafd1f760fe8b6) [更多...](struct_ak_cmd___set_listeners_a8f6012d1615b1637cf27db9f88ba8011.html#a8f6012d1615b1637cf27db9f88ba8011) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [numListenerIDs](struct_ak_cmd___set_listeners_a24f52ff397bfea59fbbbc0fb179d9ee4.html#a24f52ff397bfea59fbbbc0fb179d9ee4) |
|  | Number of listeners [更多...](struct_ak_cmd___set_listeners_a24f52ff397bfea59fbbbc0fb179d9ee4.html#a24f52ff397bfea59fbbbc0fb179d9ee4) |
|  | |

## 详细描述

Modifies a game object's set of active listeners. The `operation` field determines the type of operation to execute on the set (set, add, or remove).

The Sound Engine expects an array of `AkGameObjectID` objects after the command. For example:

```
auto cmd = (AkCmd_SetListeners*)AK_CommandBuffer_Add(buffer, AkCommand_SetListeners);
cmd->gameObjectID = 100;
cmd->numListenerIDs = mylistenerArray.size();
AK_CommandBuffer_AddArray(buffer, sizeof(AkGameObjectID), mylistenerArray.size(), mylistenerArray.data());
```

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` is outside the valid range, or incomplete array after the command
- AK\_IDNotFound: `gameObjectID` is not a registered game object ID.

参见
:   - [AkCommand\_SetListeners](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda28d2e0777e20fd3e1041437522db6431 "See AkCmd_SetListeners")
    - [AK\_CommandBuffer\_AddArray](_ak_command_buffer_8h_a7512f07e3e8f24cf4ed15bebf3a6392e.html#a7512f07e3e8f24cf4ed15bebf3a6392e)
    - [集成 Listener](soundengine_listeners.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [343](_ak_command_types_8h_source.html#l00343) 行定义.