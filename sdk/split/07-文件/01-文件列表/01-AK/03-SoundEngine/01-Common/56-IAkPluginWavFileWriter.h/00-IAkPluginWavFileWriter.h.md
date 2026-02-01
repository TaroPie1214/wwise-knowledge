# IAkPluginWavFileWriter.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members)

IAkPluginWavFileWriter.h 文件参考

`#include <AK/SoundEngine/Common/IAkPlugin.h>`

[浏览源代码.](_i_ak_plugin_wav_file_writer_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| class | [AK::IAkPluginWavFileWriter](class_a_k_1_1_i_ak_plugin_wav_file_writer.html) |
|  | Interface for the wav file writer. [更多...](class_a_k_1_1_i_ak_plugin_wav_file_writer.html#details) |
|  | |
| class | [AK::IAkPluginServiceWavFileWriter](class_a_k_1_1_i_ak_plugin_service_wav_file_writer.html) |
|  | Interface for the wav file writer service. [更多...](class_a_k_1_1_i_ak_plugin_service_wav_file_writer.html#details) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_GET\_PLUGIN\_SERVICE\_WAV\_FILE\_WRITER](_i_ak_plugin_wav_file_writer_8h_a5f8c7a38b9bfc827f420801a57943368.html#a5f8c7a38b9bfc827f420801a57943368)(plugin\_ctx)   static\_cast<[AK::IAkPluginServiceWavFileWriter](class_a_k_1_1_i_ak_plugin_service_wav_file_writer.html)\*>(plugin\_ctx->GetPluginService([AK::PluginServiceType\_WavFileWriter](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99a901ac2dc1e4a8a7d11827a063fd7b784))) |
|  | |

## 详细描述

Plug-in interface for wav file writing

在文件 [IAkPluginWavFileWriter.h](_i_ak_plugin_wav_file_writer_8h_source.html) 中定义.