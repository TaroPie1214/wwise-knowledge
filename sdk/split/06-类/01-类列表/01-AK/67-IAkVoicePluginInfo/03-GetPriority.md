# GetPriority

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkVoicePluginInfo](class_a_k_1_1_i_ak_voice_plugin_info.html)

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [GetPlayingID](class_a_k_1_1_i_ak_voice_plugin_info_ad1883a23e185d45e79654e112574fd7f.html#ad1883a23e185d45e79654e112574fd7f) | | [GetPriority](class_a_k_1_1_i_ak_voice_plugin_info_aaee67c3b0856c6edb01c5e77c40c486f.html#aaee67c3b0856c6edb01c5e77c40c486f) | | [~IAkVoicePluginInfo](class_a_k_1_1_i_ak_voice_plugin_info_a571a77d553b9a0ad9a1c0172b72a4054.html#a571a77d553b9a0ad9a1c0172b72a4054) | | [◆](#aaee67c3b0856c6edb01c5e77c40c486f)GetPriority() |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  | | --- | --- | --- | --- | --- | | virtual [AkPriority](_ak_typedefs_8h_a6fd4ce3da8a0654b665da32c63623433.html#a6fd4ce3da8a0654b665da32c63623433) AK::IAkVoicePluginInfo::GetPriority | ( |  | ) | const | | pure virtual |  Get priority value associated to this voice. When priority voice is modified by distance, the minimum distance among emitter-listener pairs is used.  返回  The priority between AK\_MIN\_PRIORITY and AK\_MAX\_PRIORITY inclusively. |