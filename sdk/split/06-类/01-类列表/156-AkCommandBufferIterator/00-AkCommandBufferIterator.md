# AkCommandBufferIterator

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_command_buffer_iterator-members.html) |
[Public 属性](#pub-attribs)

AkCommandBufferIterator结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| struct [AkCommandHeader](struct_ak_command_header.html) \* | [header](struct_ak_command_buffer_iterator_a33db0cc07340b6a43e5159be2dd516d5.html#a33db0cc07340b6a43e5159be2dd516d5) |
|  | Pointer to header of command. Use this to check the code of the command and the result code after processing. [更多...](struct_ak_command_buffer_iterator_a33db0cc07340b6a43e5159be2dd516d5.html#a33db0cc07340b6a43e5159be2dd516d5) |
|  | |
| void \* | [payload](struct_ak_command_buffer_iterator_a0be2553f03068aa22f6ef92547fa6f0e.html#a0be2553f03068aa22f6ef92547fa6f0e) |
|  | Pointer to payload of current command [更多...](struct_ak_command_buffer_iterator_a0be2553f03068aa22f6ef92547fa6f0e.html#a0be2553f03068aa22f6ef92547fa6f0e) |
|  | |
| void \* | [buffer](struct_ak_command_buffer_iterator_af86245a5933a8249e0b4b526da48333d.html#af86245a5933a8249e0b4b526da48333d) |
|  | Pointer to beginning of command buffer [更多...](struct_ak_command_buffer_iterator_af86245a5933a8249e0b4b526da48333d.html#af86245a5933a8249e0b4b526da48333d) |
|  | |

## 详细描述

Structure used to iterate through a command buffer.

参见
:   - [AK\_CommandBuffer\_Begin](_ak_command_buffer_8h_ab02aeefa1db98786d3133a41cc3027ae.html#ab02aeefa1db98786d3133a41cc3027ae)
    - [AK\_CommandBuffer\_Next](_ak_command_buffer_8h_a66fa021ab3bd03957b61bd74ce88ef08.html#a66fa021ab3bd03957b61bd74ce88ef08)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1987](_ak_command_types_8h_source.html#l01987) 行定义.