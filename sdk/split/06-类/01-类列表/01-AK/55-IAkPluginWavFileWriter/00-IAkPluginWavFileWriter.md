# IAkPluginWavFileWriter

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPluginWavFileWriter](class_a_k_1_1_i_ak_plugin_wav_file_writer.html)

[所有成员列表](class_a_k_1_1_i_ak_plugin_wav_file_writer-members.html) |
[Public 成员函数](#pub-methods)

AK::IAkPluginWavFileWriter类 参考abstract

Interface for the wav file writer.
[更多...](class_a_k_1_1_i_ak_plugin_wav_file_writer.html#details)

`#include <IAkPluginWavFileWriter.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [PassAudioData](class_a_k_1_1_i_ak_plugin_wav_file_writer_a47e314a49b194f5a7068f3c2bb6f763c.html#a47e314a49b194f5a7068f3c2bb6f763c) (void \*in\_pData, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_size)=0 |
|  | Pass audio data to be written as-is into the data chunk of the wav file. [更多...](class_a_k_1_1_i_ak_plugin_wav_file_writer_a47e314a49b194f5a7068f3c2bb6f763c.html#a47e314a49b194f5a7068f3c2bb6f763c) |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [PassExtraData](class_a_k_1_1_i_ak_plugin_wav_file_writer_ac9b3924f3079c9253685a3c6c5b4d28d.html#ac9b3924f3079c9253685a3c6c5b4d28d) (void \*in\_pData, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_size)=0 |
|  | |
| virtual void | [Destroy](class_a_k_1_1_i_ak_plugin_wav_file_writer_af2bbf829a294612781e6016ad225517a.html#af2bbf829a294612781e6016ad225517a) ()=0 |
|  | Destroy the writer, closing the file and freeing all resources. [更多...](class_a_k_1_1_i_ak_plugin_wav_file_writer_af2bbf829a294612781e6016ad225517a.html#af2bbf829a294612781e6016ad225517a) |
|  | |

## 详细描述

Interface for the wav file writer.

在文件 [IAkPluginWavFileWriter.h](_i_ak_plugin_wav_file_writer_8h_source.html) 第 [37](_i_ak_plugin_wav_file_writer_8h_source.html#l00037) 行定义.