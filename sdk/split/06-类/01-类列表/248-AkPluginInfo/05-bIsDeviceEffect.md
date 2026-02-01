# bIsDeviceEffect

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkPluginInfo](struct_ak_plugin_info.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AkPluginInfo](struct_ak_plugin_info_a9a713e821198d5a5d13a505f1a7a28df.html#a9a713e821198d5a5d13a505f1a7a28df) | | [bCanChangeRate](struct_ak_plugin_info_a2b7dda9208b4817d238f207055b40e99.html#a2b7dda9208b4817d238f207055b40e99) | | [bCanProcessObjects](struct_ak_plugin_info_abb27da271e4dc15b9b3ef9cb3316cfd3.html#abb27da271e4dc15b9b3ef9cb3316cfd3) | | [bCanRunOnObjectConfig](struct_ak_plugin_info_a71e4ca49ae60dc03241ca6fb86eec8a7.html#a71e4ca49ae60dc03241ca6fb86eec8a7) | | [bIsDeviceEffect](struct_ak_plugin_info_ae041826945a2c7d2c3606d15cd68910c.html#ae041826945a2c7d2c3606d15cd68910c) | | [bIsInPlace](struct_ak_plugin_info_a70fb541431bdc08cdb490a926ccc3ee4.html#a70fb541431bdc08cdb490a926ccc3ee4) | | [bReserved](struct_ak_plugin_info_a2ef7278e26b80f2559e8699b0cad72b9.html#a2ef7278e26b80f2559e8699b0cad72b9) | | [bUsesGainAttribute](struct_ak_plugin_info_ada2e875962c620119cf8433f704bd696.html#ada2e875962c620119cf8433f704bd696) | | [eType](struct_ak_plugin_info_a3ba9f6803016c5467ea437cb921214c5.html#a3ba9f6803016c5467ea437cb921214c5) | | [uBuildVersion](struct_ak_plugin_info_acbe924820d397d496920384724aa4a39.html#acbe924820d397d496920384724aa4a39) | | [◆](#ae041826945a2c7d2c3606d15cd68910c)bIsDeviceEffect |  | | --- | | bool AkPluginInfo::bIsDeviceEffect |  Plug-in can process final mixes and objects right before sending them to the audio device for output. Plug-ins that process the main mix, passthrough mix and objects directly at the end of the pipeline must implement IAkAudioDeviceEffectPlugin. Audio device effect plug-ins must be in place (bIsInPlace = true) and must be able to process objects (bCanProcessObjects = true).  在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [82](_i_ak_plugin_8h_source.html#l00082) 行定义. |