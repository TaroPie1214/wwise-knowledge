# IAkPluginServiceWavFileWriter

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPluginServiceWavFileWriter](class_a_k_1_1_i_ak_plugin_service_wav_file_writer.html)

[所有成员列表](class_a_k_1_1_i_ak_plugin_service_wav_file_writer-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkPluginServiceWavFileWriter类 参考abstract

Interface for the wav file writer service.
[更多...](class_a_k_1_1_i_ak_plugin_service_wav_file_writer.html#details)

`#include <IAkPluginWavFileWriter.h>`

类 AK::IAkPluginServiceWavFileWriter 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_plugin_service_wav_file_writer.png)

|  |  |
| --- | --- |
| Public 类型 | |
| enum | [FormatType](class_a_k_1_1_i_ak_plugin_service_wav_file_writer_a0cd9d8238da57957ece0290b8b4f69ba.html#a0cd9d8238da57957ece0290b8b4f69ba) { [WAV](class_a_k_1_1_i_ak_plugin_service_wav_file_writer_a0cd9d8238da57957ece0290b8b4f69ba.html#a0cd9d8238da57957ece0290b8b4f69baabcf7d63fc2d456b11e8ef07f17368621) = 0, [WEM](class_a_k_1_1_i_ak_plugin_service_wav_file_writer_a0cd9d8238da57957ece0290b8b4f69ba.html#a0cd9d8238da57957ece0290b8b4f69baa30e667fccb2380bc7d857e3511fa4992) = 1, [ADM](class_a_k_1_1_i_ak_plugin_service_wav_file_writer_a0cd9d8238da57957ece0290b8b4f69ba.html#a0cd9d8238da57957ece0290b8b4f69baa0cf14d9b3f37a867d9d0202c404e1ff7) = 2 } |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Start](class_a_k_1_1_i_ak_plugin_service_wav_file_writer_a2dcf1369aecde4186f87de0fbe7f7a80.html#a2dcf1369aecde4186f87de0fbe7f7a80) ([AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszPath, [AkChannelConfig](struct_ak_channel_config.html) in\_channelConfig, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uSampleRate, [FormatType](class_a_k_1_1_i_ak_plugin_service_wav_file_writer_a0cd9d8238da57957ece0290b8b4f69ba.html#a0cd9d8238da57957ece0290b8b4f69ba) in\_eFormat, uint64\_t in\_sourceHash[2], [IAkPluginWavFileWriter](class_a_k_1_1_i_ak_plugin_wav_file_writer.html) \*\*out\_ppWriter)=0 |
|  | Start writing into a new wav file. Upon success, a writer is returned via out\_ppWriter. [更多...](class_a_k_1_1_i_ak_plugin_service_wav_file_writer_a2dcf1369aecde4186f87de0fbe7f7a80.html#a2dcf1369aecde4186f87de0fbe7f7a80) |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkPluginServiceWavFileWriter](class_a_k_1_1_i_ak_plugin_service_wav_file_writer_a9da0792fcd618001828604825893492f.html#a9da0792fcd618001828604825893492f) () |
|  | |
| - Protected 成员函数 继承自 [AK::IAkPluginService](class_a_k_1_1_i_ak_plugin_service.html) | |
| virtual | [~IAkPluginService](class_a_k_1_1_i_ak_plugin_service_af880be6eab8f4f3cd124ec8db8b562de.html#af880be6eab8f4f3cd124ec8db8b562de) () |
|  | |

## 详细描述

Interface for the wav file writer service.

在文件 [IAkPluginWavFileWriter.h](_i_ak_plugin_wav_file_writer_8h_source.html) 第 [58](_i_ak_plugin_wav_file_writer_8h_source.html#l00058) 行定义.