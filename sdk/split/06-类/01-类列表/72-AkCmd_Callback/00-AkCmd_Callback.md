# AkCmd_Callback

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___callback-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_Callback结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkCommandCallbackFunc](_ak_command_types_8h_adf806f94d5311616d788b6b479caac85.html#adf806f94d5311616d788b6b479caac85) | [callback](struct_ak_cmd___callback_a073b6bd930ff905237a6bc4860df22c9.html#a073b6bd930ff905237a6bc4860df22c9) |
|  | |
| void \* | [callbackCookie](struct_ak_cmd___callback_a3661dfcacb8a5f134b07cea9321d4f42.html#a3661dfcacb8a5f134b07cea9321d4f42) |
|  | |

## 详细描述

When this command is executed, the audio rendering thread will call the specified callback.

This command can fail for the following reasons:

- AK\_InvalidParameter: `callback` is not a valid function pointer.

参见
:   [AkCommand\_Callback](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda9c28c3bfda569b533e34991b305792b6 "See AkCmd_Callback")

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [210](_ak_command_types_8h_source.html#l00210) 行定义.