# AkCommandHeader

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_command_header-members.html) |
[Public 属性](#pub-attribs)

AkCommandHeader结构体 参考

Describes the data written at the beginning of each command in the command buffer
[更多...](struct_ak_command_header.html#details)

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [code](struct_ak_command_header_a1a3b088b97d89b4131018ddae654d5d0.html#a1a3b088b97d89b4131018ddae654d5d0) |
|  | Unique ID of the command, as listed in [AkCommand](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfd) enum [更多...](struct_ak_command_header_a1a3b088b97d89b4131018ddae654d5d0.html#a1a3b088b97d89b4131018ddae654d5d0) |
|  | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [size](struct_ak_command_header_a625955ca4952fca68527f201793e4635.html#a625955ca4952fca68527f201793e4635) |
|  | Size of the payload (without this header), in bytes [更多...](struct_ak_command_header_a625955ca4952fca68527f201793e4635.html#a625955ca4952fca68527f201793e4635) |
|  | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [flags](struct_ak_command_header_a2d4296667867ea5e7ad06f080c61aaf7.html#a2d4296667867ea5e7ad06f080c61aaf7) |
|  | Internal flags for the command [更多...](struct_ak_command_header_a2d4296667867ea5e7ad06f080c61aaf7.html#a2d4296667867ea5e7ad06f080c61aaf7) |
|  | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [result](struct_ak_command_header_a349ed38e4a74cff355cced1a35987d61.html#a349ed38e4a74cff355cced1a35987d61) |
|  | |

## 详细描述

Describes the data written at the beginning of each command in the command buffer

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1971](_ak_command_types_8h_source.html#l01971) 行定义.