# AkPluginInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_plugin_info-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkPluginInfo结构体 参考

`#include <IAkPlugin.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkPluginInfo](struct_ak_plugin_info_a9a713e821198d5a5d13a505f1a7a28df.html#a9a713e821198d5a5d13a505f1a7a28df) () |
|  | Constructor for default values [更多...](struct_ak_plugin_info_a9a713e821198d5a5d13a505f1a7a28df.html#a9a713e821198d5a5d13a505f1a7a28df) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkPluginType](_ak_enums_8h_af1a95e76b0e2a003e7edb2ad6f4043f4.html#af1a95e76b0e2a003e7edb2ad6f4043f4) | [eType](struct_ak_plugin_info_a3ba9f6803016c5467ea437cb921214c5.html#a3ba9f6803016c5467ea437cb921214c5) |
|  | Plug-in type [更多...](struct_ak_plugin_info_a3ba9f6803016c5467ea437cb921214c5.html#a3ba9f6803016c5467ea437cb921214c5) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uBuildVersion](struct_ak_plugin_info_acbe924820d397d496920384724aa4a39.html#acbe924820d397d496920384724aa4a39) |
|  | Plug-in build version, must match the AK\_WWISESDK\_VERSION\_COMBINED macro from [AkWwiseSDKVersion.h](_ak_wwise_s_d_k_version_8h.html). Prevents usage of plugins compiled for other versions, avoiding crashes or data issues. [更多...](struct_ak_plugin_info_acbe924820d397d496920384724aa4a39.html#acbe924820d397d496920384724aa4a39) |
|  | |
| bool | [bIsInPlace](struct_ak_plugin_info_a70fb541431bdc08cdb490a926ccc3ee4.html#a70fb541431bdc08cdb490a926ccc3ee4) |
|  | Buffer usage (in-place or not). If true, and the plug-in is an insert effect, it should implement IAkInPlaceEffectPlugin, otherwise it should implement IAkOutOfPlaceEffectPlugin. If it is an object processor (see CanProcessObjects, below), it should implement IAkInPlaceObjectPlugin or IAkOutOfPlaceObjectPlugin respectively. [更多...](struct_ak_plugin_info_a70fb541431bdc08cdb490a926ccc3ee4.html#a70fb541431bdc08cdb490a926ccc3ee4) |
|  | |
| bool | [bCanChangeRate](struct_ak_plugin_info_a2b7dda9208b4817d238f207055b40e99.html#a2b7dda9208b4817d238f207055b40e99) |
|  | True for effects whose sample throughput is different between input and output. Effects that can change rate need to be out-of-place (!bIsInPlace), and cannot exist on busses. [更多...](struct_ak_plugin_info_a2b7dda9208b4817d238f207055b40e99.html#a2b7dda9208b4817d238f207055b40e99) |
|  | |
| bool | [bReserved](struct_ak_plugin_info_a2ef7278e26b80f2559e8699b0cad72b9.html#a2ef7278e26b80f2559e8699b0cad72b9) |
|  | Legacy bIsAsynchronous plug-in flag, now unused. Preserved for plug-in backward compatibility. bReserved should be false for all plug-in. [更多...](struct_ak_plugin_info_a2ef7278e26b80f2559e8699b0cad72b9.html#a2ef7278e26b80f2559e8699b0cad72b9) |
|  | |
| bool | [bCanProcessObjects](struct_ak_plugin_info_abb27da271e4dc15b9b3ef9cb3316cfd3.html#abb27da271e4dc15b9b3ef9cb3316cfd3) |
|  | Plug-in can process audio objects. They must implement IAkInPlaceObjectPlugin or IAkOutOfPlaceObjectPlugin, depending on if they work in-place or out-of-place. Out-of-place object processors only work on busses. [更多...](struct_ak_plugin_info_abb27da271e4dc15b9b3ef9cb3316cfd3.html#abb27da271e4dc15b9b3ef9cb3316cfd3) |
|  | |
| bool | [bIsDeviceEffect](struct_ak_plugin_info_ae041826945a2c7d2c3606d15cd68910c.html#ae041826945a2c7d2c3606d15cd68910c) |
|  | Plug-in can process final mixes and objects right before sending them to the audio device for output. Plug-ins that process the main mix, passthrough mix and objects directly at the end of the pipeline must implement IAkAudioDeviceEffectPlugin. Audio device effect plug-ins must be in place (bIsInPlace = true) and must be able to process objects (bCanProcessObjects = true). [更多...](struct_ak_plugin_info_ae041826945a2c7d2c3606d15cd68910c.html#ae041826945a2c7d2c3606d15cd68910c) |
|  | |
| bool | [bCanRunOnObjectConfig](struct_ak_plugin_info_a71e4ca49ae60dc03241ca6fb86eec8a7.html#a71e4ca49ae60dc03241ca6fb86eec8a7) |
|  | Plug-in can run on bus with Audio Object configuration. Effect plug-ins are instantiated once per Audio Objects on those busses. While this may be fine for effects such as EQs, it is an user error for effects such as reverbs, or for any effect that is non-linear. Effects that return false will fail to initialize when created on busses with Audio Object Configuration. [更多...](struct_ak_plugin_info_a71e4ca49ae60dc03241ca6fb86eec8a7.html#a71e4ca49ae60dc03241ca6fb86eec8a7) |
|  | |
| bool | [bUsesGainAttribute](struct_ak_plugin_info_ada2e875962c620119cf8433f704bd696.html#ada2e875962c620119cf8433f704bd696) |
|  | Plug-in knows how to process objects separately from the cumulativeGain of the object (or the processing of the object's audio is independent of the overall object gain). bCanProcessObjects must also be true, as this relies on Object Metadata. [更多...](struct_ak_plugin_info_ada2e875962c620119cf8433f704bd696.html#ada2e875962c620119cf8433f704bd696) |
|  | |

## 详细描述

Plug-in information structure.

备注
:   The bIsInPlace field is only relevant for effect plug-ins.

参见
:   - [AK::IAkPlugin::GetPluginInfo()](soundengine_plugins.html#iakeffect_geteffectinfo)

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [61](_i_ak_plugin_8h_source.html#l00061) 行定义.