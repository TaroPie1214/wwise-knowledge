# AkCmd_SetDefaultListeners

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_default_listeners-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetDefaultListeners结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [operation](struct_ak_cmd___set_default_listeners_a7e0754b688ea45e298cb6a5cbd491c5b.html#a7e0754b688ea45e298cb6a5cbd491c5b) |
|  | Type of operation, see [AkListenerOp](_ak_enums_8h_a76a5fdc9e33cbd5441aafd1f760fe8b6.html#a76a5fdc9e33cbd5441aafd1f760fe8b6) [更多...](struct_ak_cmd___set_default_listeners_a7e0754b688ea45e298cb6a5cbd491c5b.html#a7e0754b688ea45e298cb6a5cbd491c5b) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [numListenerIDs](struct_ak_cmd___set_default_listeners_a37bcb23767b2256a421fa6a39e172cf6.html#a37bcb23767b2256a421fa6a39e172cf6) |
|  | Number of listeners [更多...](struct_ak_cmd___set_default_listeners_a37bcb23767b2256a421fa6a39e172cf6.html#a37bcb23767b2256a421fa6a39e172cf6) |
|  | |

## 详细描述

Modifies the default set of associated listeners for game objects that have not explicitly overridden their listener sets. Upon registration, all game objects reference the default listener set. The listeners.operation field determines the type of operation to execute on the set (set, add, or remove).

The Sound Engine expects an array of `AkGameObjectID` objects after the command. For example:

```
auto cmd = (AkCmd_SetDefaultListeners*)AK_CommandBuffer_Add(buffer, AkCommand_SetDefaultListeners);
cmd->numListenerIDs = mylistenerArray.size();
AK_CommandBuffer_AddArray(buffer, sizeof(AkGameObjectID), mylistenerArray.size(), mylistenerArray.data());
```

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` is outside the valid range, or incomplete array after the command

参见
:   - [AkCommand\_SetDefaultListeners](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdac1477710c8ff85a24e53f09213edf55d "See AkCmd_SetDefaultListeners")
    - [AK\_CommandBuffer\_AddArray](_ak_command_buffer_8h_a7512f07e3e8f24cf4ed15bebf3a6392e.html#a7512f07e3e8f24cf4ed15bebf3a6392e)
    - [集成 Listener](soundengine_listeners.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [367](_ak_command_types_8h_source.html#l00367) 行定义.