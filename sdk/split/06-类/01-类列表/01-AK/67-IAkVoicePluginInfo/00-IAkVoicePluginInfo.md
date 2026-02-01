# IAkVoicePluginInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkVoicePluginInfo](class_a_k_1_1_i_ak_voice_plugin_info.html)

[所有成员列表](class_a_k_1_1_i_ak_voice_plugin_info-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkVoicePluginInfo类 参考abstract

Voice-specific information available to plug-ins.
[更多...](class_a_k_1_1_i_ak_voice_plugin_info.html#details)

`#include <IAkPlugin.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) | [GetPlayingID](class_a_k_1_1_i_ak_voice_plugin_info_ad1883a23e185d45e79654e112574fd7f.html#ad1883a23e185d45e79654e112574fd7f) () const =0 |
|  | Retrieve the Playing ID of the event corresponding to this voice (if applicable). [更多...](class_a_k_1_1_i_ak_voice_plugin_info_ad1883a23e185d45e79654e112574fd7f.html#ad1883a23e185d45e79654e112574fd7f) |
|  | |
| virtual [AkPriority](_ak_typedefs_8h_a6fd4ce3da8a0654b665da32c63623433.html#a6fd4ce3da8a0654b665da32c63623433) | [GetPriority](class_a_k_1_1_i_ak_voice_plugin_info_aaee67c3b0856c6edb01c5e77c40c486f.html#aaee67c3b0856c6edb01c5e77c40c486f) () const =0 |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkVoicePluginInfo](class_a_k_1_1_i_ak_voice_plugin_info_a571a77d553b9a0ad9a1c0172b72a4054.html#a571a77d553b9a0ad9a1c0172b72a4054) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_voice_plugin_info_a571a77d553b9a0ad9a1c0172b72a4054.html#a571a77d553b9a0ad9a1c0172b72a4054) |
|  | |

## 详细描述

Voice-specific information available to plug-ins.

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [219](_i_ak_plugin_8h_source.html#l00219) 行定义.