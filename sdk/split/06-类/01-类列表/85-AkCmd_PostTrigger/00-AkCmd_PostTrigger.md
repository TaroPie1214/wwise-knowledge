# AkCmd_PostTrigger

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___post_trigger-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_PostTrigger结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkTriggerID](_ak_typedefs_8h_a901799fa6607134b3677918a7014f662.html#a901799fa6607134b3677918a7014f662) | [triggerID](struct_ak_cmd___post_trigger_a92a49f82816ab1a10a4ad8413c2b42e4.html#a92a49f82816ab1a10a4ad8413c2b42e4) |
|  | ID of the trigger [更多...](struct_ak_cmd___post_trigger_a92a49f82816ab1a10a4ad8413c2b42e4.html#a92a49f82816ab1a10a4ad8413c2b42e4) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___post_trigger_aa0f2c0708663410b4bff8004ed99d1df.html#aa0f2c0708663410b4bff8004ed99d1df) |
|  | (optional) Game Object ID; set to AK\_INVALID\_GAME\_OBJECT post trigger in global scope. [更多...](struct_ak_cmd___post_trigger_aa0f2c0708663410b4bff8004ed99d1df.html#aa0f2c0708663410b4bff8004ed99d1df) |
|  | |

## 详细描述

Post the specified trigger. This operation can be performed at global scope or game object scope.

This command can fail for the following reason:

- AK\_InvalidParameter: `triggerID` is not valid
- AK\_IDNotFound: `gameObjectID` is specified but not registered.

参见
:   - [集成详情——触发器](soundengine_triggers.html)
    - [AkCommand\_PostTrigger](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda2435ca4e862f810f7d574e6930912c67 "See AkCmd_PostTrigger")
    - `AK::SoundEngine::PostTrigger()`

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [718](_ak_command_types_8h_source.html#l00718) 行定义.