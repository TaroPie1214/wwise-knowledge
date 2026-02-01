# ConvertedFileInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [ConvertedFileInfo](struct_a_k_1_1_wwise_1_1_plugin_1_1_converted_file_info.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_converted_file_info-members.html) |
[Public 属性](#pub-attribs)

AK.Wwise::Plugin::ConvertedFileInfo结构体 参考

`#include <PluginDef.h>`

类 AK.Wwise::Plugin::ConvertedFileInfo 继承关系图:

![](../../../../../../images/struct_a_k_1_1_wwise_1_1_plugin_1_1_converted_file_info.png)

|  |  |
| --- | --- |
| Public 属性 | |
| uint32\_t | [dataSize](struct_a_k_1_1_wwise_1_1_plugin_1_1_converted_file_info_af1a4b2316d85e77d5823ae71c0130105.html#af1a4b2316d85e77d5823ae71c0130105) = 0 |
|  | Actual size of data, taking duration into account (for prefetch) [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_converted_file_info_af1a4b2316d85e77d5823ae71c0130105.html#af1a4b2316d85e77d5823ae71c0130105) |
|  | |
| uint32\_t | [duration](struct_a_k_1_1_wwise_1_1_plugin_1_1_converted_file_info_a5946489c7804ea407d9848e08f40ce2b.html#a5946489c7804ea407d9848e08f40ce2b) = -1 |
|  | Actual duration of data, or -1 for entire file [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_converted_file_info_a5946489c7804ea407d9848e08f40ce2b.html#a5946489c7804ea407d9848e08f40ce2b) |
|  | |
| uint32\_t | [sampleRate](struct_a_k_1_1_wwise_1_1_plugin_1_1_converted_file_info_ab55ef9a9fb4f9632c409d7bc90a7746e.html#ab55ef9a9fb4f9632c409d7bc90a7746e) = 0 |
|  | Number of samples per second [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_converted_file_info_ab55ef9a9fb4f9632c409d7bc90a7746e.html#ab55ef9a9fb4f9632c409d7bc90a7746e) |
|  | |
| [AkChannelConfig](struct_ak_channel_config.html) | [channelConfig](struct_a_k_1_1_wwise_1_1_plugin_1_1_converted_file_info_ac5d62251f3c9384cc2fcfc6021a9782b.html#ac5d62251f3c9384cc2fcfc6021a9782b) |
|  | Channel configuration [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_converted_file_info_ac5d62251f3c9384cc2fcfc6021a9782b.html#ac5d62251f3c9384cc2fcfc6021a9782b) |
|  | |
| uint32\_t | [decodedFileSize](struct_a_k_1_1_wwise_1_1_plugin_1_1_converted_file_info_a255c225928b9c4102d44f1169be97416.html#a255c225928b9c4102d44f1169be97416) = -1 |
|  | File size of file when decoded to PCM format, *If* offline decoding is supported by the codec. Otherwise has value NO\_OFFLINE\_DECODING (-1) [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_converted_file_info_a255c225928b9c4102d44f1169be97416.html#a255c225928b9c4102d44f1169be97416) |
|  | |
| uint8\_t | [abyHash](struct_a_k_1_1_wwise_1_1_plugin_1_1_converted_file_info_abde0be2429fbf609bd7ebc1560c41e58.html#abde0be2429fbf609bd7ebc1560c41e58) [16] = { 0 } |
|  | Converted file hash (as present in the HASH chunk). [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_converted_file_info_abde0be2429fbf609bd7ebc1560c41e58.html#abde0be2429fbf609bd7ebc1560c41e58) |
|  | |

## 详细描述

在文件 [PluginDef.h](_plugin_def_8h_source.html) 第 [470](_plugin_def_8h_source.html#l00470) 行定义.