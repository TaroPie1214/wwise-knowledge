# completionCallback

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkCommandBufferHeader](struct_ak_command_buffer_header.html)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [bufferSize](struct_ak_command_buffer_header_a7f963ec2439a84dda4b4601373b7ebc4.html#a7f963ec2439a84dda4b4601373b7ebc4) | | [completionCallback](struct_ak_command_buffer_header_ab7f0b276825a8aa0cb2be9a4d4ce7bcf.html#ab7f0b276825a8aa0cb2be9a4d4ce7bcf) | | [completionCallbackCookie](struct_ak_command_buffer_header_a11c54c5d7e0f2ce379990e65b3fb0682.html#a11c54c5d7e0f2ce379990e65b3fb0682) | | [lastCommandOffset](struct_ak_command_buffer_header_a0a61b93f3286167655261217dd2b328f.html#a0a61b93f3286167655261217dd2b328f) | | [◆](#ab7f0b276825a8aa0cb2be9a4d4ce7bcf)completionCallback |  | | --- | | [AkCommandCallbackFunc](_ak_command_types_8h_adf806f94d5311616d788b6b479caac85.html#adf806f94d5311616d788b6b479caac85) AkCommandBufferHeader::completionCallback |  At that point in time, the client can free the command buffer memory, or re-use it for something else.  If not null, this callback is called when all commands in the buffer have been processed.  在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1965](_ak_command_types_8h_source.html#l01965) 行定义. |