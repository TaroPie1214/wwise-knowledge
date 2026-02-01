# result

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkCommandHeader](struct_ak_command_header.html)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [code](struct_ak_command_header_a1a3b088b97d89b4131018ddae654d5d0.html#a1a3b088b97d89b4131018ddae654d5d0) | | [flags](struct_ak_command_header_a2d4296667867ea5e7ad06f080c61aaf7.html#a2d4296667867ea5e7ad06f080c61aaf7) | | [result](struct_ak_command_header_a349ed38e4a74cff355cced1a35987d61.html#a349ed38e4a74cff355cced1a35987d61) | | [size](struct_ak_command_header_a625955ca4952fca68527f201793e4635.html#a625955ca4952fca68527f201793e4635) | | [◆](#a349ed38e4a74cff355cced1a35987d61)result |  | | --- | | [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) AkCommandHeader::result |  Result of processing the command, as listed in [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) enum. This is set by the Sound Engine after the command is processed. When set to a value other than AK\_Success, the command was not processed, and the error code indicates the reason why. Clients can inspect this value after the command buffer's done\_callback is called. Its value has no meaning before this callback is called.  在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1976](_ak_command_types_8h_source.html#l01976) 行定义. |