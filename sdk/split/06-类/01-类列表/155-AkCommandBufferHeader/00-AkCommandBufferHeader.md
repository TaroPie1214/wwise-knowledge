# AkCommandBufferHeader

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_command_buffer_header-members.html) |
[Public 属性](#pub-attribs)

AkCommandBufferHeader结构体 参考

Describes the data written at the beginning of any initialized command buffer.
[更多...](struct_ak_command_buffer_header.html#details)

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [bufferSize](struct_ak_command_buffer_header_a7f963ec2439a84dda4b4601373b7ebc4.html#a7f963ec2439a84dda4b4601373b7ebc4) |
|  | Total size of command buffer in bytes [更多...](struct_ak_command_buffer_header_a7f963ec2439a84dda4b4601373b7ebc4.html#a7f963ec2439a84dda4b4601373b7ebc4) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [lastCommandOffset](struct_ak_command_buffer_header_a0a61b93f3286167655261217dd2b328f.html#a0a61b93f3286167655261217dd2b328f) |
|  | Internal use. Should be zero-initialized. [更多...](struct_ak_command_buffer_header_a0a61b93f3286167655261217dd2b328f.html#a0a61b93f3286167655261217dd2b328f) |
|  | |
| [AkCommandCallbackFunc](_ak_command_types_8h_adf806f94d5311616d788b6b479caac85.html#adf806f94d5311616d788b6b479caac85) | [completionCallback](struct_ak_command_buffer_header_ab7f0b276825a8aa0cb2be9a4d4ce7bcf.html#ab7f0b276825a8aa0cb2be9a4d4ce7bcf) |
|  | At that point in time, the client can free the command buffer memory, or re-use it for something else. [更多...](struct_ak_command_buffer_header_ab7f0b276825a8aa0cb2be9a4d4ce7bcf.html#ab7f0b276825a8aa0cb2be9a4d4ce7bcf) |
|  | |
| void \* | [completionCallbackCookie](struct_ak_command_buffer_header_a11c54c5d7e0f2ce379990e65b3fb0682.html#a11c54c5d7e0f2ce379990e65b3fb0682) |
|  | User cookie for done\_callback [更多...](struct_ak_command_buffer_header_a11c54c5d7e0f2ce379990e65b3fb0682.html#a11c54c5d7e0f2ce379990e65b3fb0682) |
|  | |

## 详细描述

Describes the data written at the beginning of any initialized command buffer.

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1961](_ak_command_types_8h_source.html#l01961) 行定义.