# IAkPlugin.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members) |
[类型定义](#typedef-members) |
[枚举](#enum-members) |
[变量](#var-members)

IAkPlugin.h 文件参考

`#include <AK/SoundEngine/Common/AkCommonDefs.h>`  
`#include <AK/SoundEngine/Common/IAkRTPCSubscriber.h>`  
`#include <AK/SoundEngine/Common/IAkPluginMemAlloc.h>`  
`#include <AK/SoundEngine/Common/AkFPUtilities.h>`  
`#include <AK/SoundEngine/Common/AkAudioMarker.h>`  
`#include <AK/Tools/Common/AkAssert.h>`  
`#include <AK/Tools/Common/AkLock.h>`  
`#include <AK/Tools/Common/AkPlatformFuncs.h>`  
`#include <AK/Tools/Common/AkMonitorError.h>`  
`#include <AK/Tools/Common/AkRng.h>`  
`#include <AK/SoundEngine/Common/AkSoundEngineExport.h>`  
`#include <AK/SoundEngine/Common/IAkProcessorFeatures.h>`  
`#include <AK/SoundEngine/Common/IAkPlatformContext.h>`  
`#include <AK/SoundEngine/Common/AkMidiTypes.h>`  
`#include <AK/SoundEngine/Common/AkMixerTypes.h>`  
`#include <AK/SoundEngine/Common/AkCallback.h>`  
`#include <AK/AkWwiseSDKVersion.h>`  
`#include <math.h>`  
`#include <xmmintrin.h>`

[浏览源代码.](_i_ak_plugin_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkPluginInfo](struct_ak_plugin_info.html) |
|  | |
| class | [AK::IAkGameObjectPluginInfo](class_a_k_1_1_i_ak_game_object_plugin_info.html) |
|  | Game object information available to plugins. [更多...](class_a_k_1_1_i_ak_game_object_plugin_info.html#details) |
|  | |
| class | [AK::IAkVoicePluginInfo](class_a_k_1_1_i_ak_voice_plugin_info.html) |
|  | Voice-specific information available to plug-ins. [更多...](class_a_k_1_1_i_ak_voice_plugin_info.html#details) |
|  | |
| class | [AK::IAkPluginContextBase](class_a_k_1_1_i_ak_plugin_context_base.html) |
|  | Interface to retrieve contextual information available to all types of plugins. [更多...](class_a_k_1_1_i_ak_plugin_context_base.html#details) |
|  | |
| class | [AK::IAkEffectPluginContext](class_a_k_1_1_i_ak_effect_plugin_context.html) |
|  | |
| class | [AK::IAkSourcePluginContext](class_a_k_1_1_i_ak_source_plugin_context.html) |
|  | |
| class | [AK::IAkMixerPluginContext](class_a_k_1_1_i_ak_mixer_plugin_context.html) |
|  | Interface to retrieve contextual information for a mixer. [更多...](class_a_k_1_1_i_ak_mixer_plugin_context.html#details) |
|  | |
| class | [AK::IAkPluginParam](class_a_k_1_1_i_ak_plugin_param.html) |
|  | |
| class | [AK::IAkPlugin](class_a_k_1_1_i_ak_plugin.html) |
|  | |
| class | [AK::IAkEffectPlugin](class_a_k_1_1_i_ak_effect_plugin.html) |
|  | Software effect plug-in interface (see [创建声音引擎效果器插件](soundengine_plugins_effects.html)). [更多...](class_a_k_1_1_i_ak_effect_plugin.html#details) |
|  | |
| class | [AK::IAkInPlaceEffectPlugin](class_a_k_1_1_i_ak_in_place_effect_plugin.html) |
|  | Software effect plug-in interface for in-place processing (see [创建声音引擎效果器插件](soundengine_plugins_effects.html)). [更多...](class_a_k_1_1_i_ak_in_place_effect_plugin.html#details) |
|  | |
| class | [AK::IAkOutOfPlaceEffectPlugin](class_a_k_1_1_i_ak_out_of_place_effect_plugin.html) |
|  | Software effect plug-in interface for out-of-place processing (see [创建声音引擎效果器插件](soundengine_plugins_effects.html)). [更多...](class_a_k_1_1_i_ak_out_of_place_effect_plugin.html#details) |
|  | |
| class | [AK::IAkInPlaceObjectPlugin](class_a_k_1_1_i_ak_in_place_object_plugin.html) |
|  | |
| class | [AK::IAkOutOfPlaceObjectPlugin](class_a_k_1_1_i_ak_out_of_place_object_plugin.html) |
|  | |
| class | [AK::IAkAudioDeviceEffectPluginContext](class_a_k_1_1_i_ak_audio_device_effect_plugin_context.html) |
|  | |
| class | [AK::IAkAudioDeviceEffectPlugin](class_a_k_1_1_i_ak_audio_device_effect_plugin.html) |
|  | |
| class | [AK::IAkMixerInputContext](class_a_k_1_1_i_ak_mixer_input_context.html) |
|  | Interface to retrieve information about an input of a mix connection (for processing during the SpeakerVolumeMatrix Callback) [更多...](class_a_k_1_1_i_ak_mixer_input_context.html#details) |
|  | |
| class | [AK::IAkSinkPluginContext](class_a_k_1_1_i_ak_sink_plugin_context.html) |
|  | |
| class | [AK::IAkSinkPluginBase](class_a_k_1_1_i_ak_sink_plugin_base.html) |
|  | |
| class | [AK::IAkSinkPlugin](class_a_k_1_1_i_ak_sink_plugin.html) |
|  | Software interface for sink (audio endpoint) plugins. [更多...](class_a_k_1_1_i_ak_sink_plugin.html#details) |
|  | |
| class | [AK::IAk3DAudioSinkPlugin](class_a_k_1_1_i_ak3_d_audio_sink_plugin.html) |
|  | Software plug-in interface for sink (audio end point) which supports 3D audio features. [更多...](class_a_k_1_1_i_ak3_d_audio_sink_plugin.html#details) |
|  | |
| class | [AK::IAkSourcePlugin](class_a_k_1_1_i_ak_source_plugin.html) |
|  | [Wwise](namespace_a_k_1_1_wwise.html) sound engine source plug-in interface (see [创建声音引擎源插件](soundengine_plugins_source.html)). [更多...](class_a_k_1_1_i_ak_source_plugin.html#details) |
|  | |
| class | [AK::IAkPluginService](class_a_k_1_1_i_ak_plugin_service.html) |
|  | Common interface for plug-in services accessed through the global plug-in context [更多...](class_a_k_1_1_i_ak_plugin_service.html#details) |
|  | |
| class | [AK::IAkGlobalPluginContext](class_a_k_1_1_i_ak_global_plugin_context.html) |
|  | |
| class | [AK::IAkPluginServiceMixer](class_a_k_1_1_i_ak_plugin_service_mixer.html) |
|  | Interface for the "Mixer" plug-in service, to handle mixing together of signals, or applying simple transforms [更多...](class_a_k_1_1_i_ak_plugin_service_mixer.html#details) |
|  | |
| class | [AK::IAkPluginServiceRNG](class_a_k_1_1_i_ak_plugin_service_r_n_g.html) |
|  | |
| class | [AK::IAkPluginServiceAudioObjectAttenuation](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation.html) |
|  | Interface for the services related to extracting attenuation curves from audio objects and using them. [更多...](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation.html#details) |
|  | |
| class | [AK::IAkPluginServiceAudioObjectPriority](class_a_k_1_1_i_ak_plugin_service_audio_object_priority.html) |
|  | |
| class | [AK::IAkPluginServiceMarkers](class_a_k_1_1_i_ak_plugin_service_markers.html) |
|  | Interface for the markers service. [更多...](class_a_k_1_1_i_ak_plugin_service_markers.html#details) |
|  | |
| class | [AK::IAkPluginServiceMarkers::IAkMarkerNotificationService](class_a_k_1_1_i_ak_plugin_service_markers_1_1_i_ak_marker_notification_service.html) |
|  | |
| class | [AK::PluginRegistration](class_a_k_1_1_plugin_registration.html) |
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
| #define | [AK\_FLOAT\_TO\_SAMPLETYPE](_i_ak_plugin_8h_a441dc3050f2787f07e0678ab0d258002.html#a441dc3050f2787f07e0678ab0d258002)(\_\_in\_\_)   (\_\_in\_\_) |
|  | This function can be useful to convert from normalized floating point audio samples to HW-pipeline format samples. [更多...](_i_ak_plugin_8h_a441dc3050f2787f07e0678ab0d258002.html#a441dc3050f2787f07e0678ab0d258002) |
|  | |
| #define | [AK\_FLOAT\_TO\_SAMPLETYPE\_NOCLIP](_i_ak_plugin_8h_a07d5040c296cad5ec921b31e5ae71c3c.html#a07d5040c296cad5ec921b31e5ae71c3c)(\_\_in\_\_)   (\_\_in\_\_) |
|  | This function can be useful to convert from normalized floating point audio samples to HW-pipeline format samples when the input is not not to exceed (-1,1) range. [更多...](_i_ak_plugin_8h_a07d5040c296cad5ec921b31e5ae71c3c.html#a07d5040c296cad5ec921b31e5ae71c3c) |
|  | |
| #define | [AK\_SAMPLETYPE\_TO\_FLOAT](_i_ak_plugin_8h_a4ad54d8bc876736abe89364ed6a57bf6.html#a4ad54d8bc876736abe89364ed6a57bf6)(\_\_in\_\_)   (\_\_in\_\_) |
|  | This function can be useful to convert from HW-pipeline format samples to normalized floating point audio samples. [更多...](_i_ak_plugin_8h_a4ad54d8bc876736abe89364ed6a57bf6.html#a4ad54d8bc876736abe89364ed6a57bf6) |
|  | |
| #define | [AK\_DBTOLIN](_i_ak_plugin_8h_a97e15001faba0668ef9311767c8d21e9.html#a97e15001faba0668ef9311767c8d21e9)(\_\_db\_\_)   (powf(10.f,(\_\_db\_\_) \* 0.05f)) |
|  | |
| #define | [AK\_GET\_PLUGIN\_SERVICE\_MIXER](_i_ak_plugin_8h_a4793694b5f18e4334d12f70a4da40e04.html#a4793694b5f18e4334d12f70a4da40e04)(plugin\_ctx)   static\_cast<[AK::IAkPluginServiceMixer](class_a_k_1_1_i_ak_plugin_service_mixer.html)\*>(plugin\_ctx->GetPluginService([AK::PluginServiceType\_Mixer](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99a9946a61f93783dbcfe0534bca5412086))) |
|  | |
| #define | [AK\_GET\_PLUGIN\_SERVICE\_RNG](_i_ak_plugin_8h_a1646ae68919d82f6d6ca9771f3609604.html#a1646ae68919d82f6d6ca9771f3609604)(plugin\_ctx)   static\_cast<[AK::IAkPluginServiceRNG](class_a_k_1_1_i_ak_plugin_service_r_n_g.html)\*>(plugin\_ctx->GetPluginService([AK::PluginServiceType\_RNG](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99a93e55d84981a0b90ed8013c70f079c50))) |
|  | |
| #define | [AK\_GET\_PLUGIN\_SERVICE\_AUDIO\_OBJECT\_ATTENUATION](_i_ak_plugin_8h_ab30b1b82e82518c7bb2f7890e424595a.html#ab30b1b82e82518c7bb2f7890e424595a)(plugin\_ctx)   static\_cast<[AK::IAkPluginServiceAudioObjectAttenuation](class_a_k_1_1_i_ak_plugin_service_audio_object_attenuation.html)\*>(plugin\_ctx->GetPluginService([AK::PluginServiceType\_AudioObjectAttenuation](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99a7f057c026db8cfeae242a805eb38f15b))) |
|  | |
| #define | [AK\_GET\_PLUGIN\_SERVICE\_AUDIO\_OBJECT\_PRIORITY](_i_ak_plugin_8h_ae8bc1832080371d10d6fccfb7f8e9713.html#ae8bc1832080371d10d6fccfb7f8e9713)(plugin\_ctx)   static\_cast<[AK::IAkPluginServiceAudioObjectPriority](class_a_k_1_1_i_ak_plugin_service_audio_object_priority.html)\*>(plugin\_ctx->GetPluginService([AK::PluginServiceType\_AudioObjectPriority](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99a468f48cde731c659d49ef159e49b845f))) |
|  | |
| #define | [AK\_GET\_PLUGIN\_SERVICE\_MARKERS](_i_ak_plugin_8h_aca83a0bac8086bebd99fd3b1290926b5.html#aca83a0bac8086bebd99fd3b1290926b5)(plugin\_ctx)   static\_cast<[AK::IAkPluginServiceMarkers](class_a_k_1_1_i_ak_plugin_service_markers.html)\*>(plugin\_ctx->GetPluginService([AK::PluginServiceType\_Markers](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99acc3dc895483686decb0b9c29294cf956))) |
|  | |
| #define | [AK\_IMPLEMENT\_PLUGIN\_FACTORY](_i_ak_plugin_8h_a13b2972f82acec4f7cedcb073d51619c.html#a13b2972f82acec4f7cedcb073d51619c)(\_pluginName\_, \_plugintype\_, \_companyid\_, \_pluginid\_) |
|  | |
| #define | [AK\_STATIC\_LINK\_PLUGIN](_i_ak_plugin_8h_a8e9fc150137c878499f2200e7e27a256.html#a8e9fc150137c878499f2200e7e27a256)(\_pluginName\_) |
|  | |
| #define | [DEFINE\_PLUGIN\_REGISTER\_HOOK](_i_ak_plugin_8h_a0e58fa7b5f9d73031a83e4667c6f8933.html#a0e58fa7b5f9d73031a83e4667c6f8933)   [AK\_DLLEXPORT](_platforms_2_windows_2_ak_types_8h_ab291f969500ebc378f2344e1477d2dd7.html#ab291f969500ebc378f2344e1477d2dd7) [AK::PluginRegistration](class_a_k_1_1_plugin_registration.html) \* [g\_pAKPluginList](_i_ak_plugin_8h_affa96e9a560e3444da2e5ae0d1fae089.html#affa96e9a560e3444da2e5ae0d1fae089) = NULL; |
|  | |
| #define | [DEFINE\_PLUGIN\_ASSERT\_HOOK](_i_ak_plugin_8h_a8dccaff2aa9c3c49494ac330b4f5bc32.html#a8dccaff2aa9c3c49494ac330b4f5bc32) |
|  | |
| #define | [DEFINEDUMMYASSERTHOOK](_i_ak_plugin_8h_a83c61f38bbc54bbd3ae1d743f1780369.html#a83c61f38bbc54bbd3ae1d743f1780369)   [DEFINE\_PLUGIN\_ASSERT\_HOOK](_i_ak_plugin_8h_a8dccaff2aa9c3c49494ac330b4f5bc32.html#a8dccaff2aa9c3c49494ac330b4f5bc32) |
|  | DEPRECATED: Use DEFINE\_PLUGIN\_ASSERT\_HOOK instead. [更多...](_i_ak_plugin_8h_a83c61f38bbc54bbd3ae1d743f1780369.html#a83c61f38bbc54bbd3ae1d743f1780369) |
|  | |
| #define | [AK\_GET\_SINK\_TYPE\_FROM\_DEVICE\_KEY](_i_ak_plugin_8h_a70622d63c770a7ff30116f99f0d3dee3.html#a70622d63c770a7ff30116f99f0d3dee3)(\_key)   (([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce))(\_key & 0xffffffff)) |
|  | |
| #define | [AK\_GET\_DEVICE\_ID\_FROM\_DEVICE\_KEY](_i_ak_plugin_8h_a1ddf3f4f106c7a3d32e98ad2a6b6319d.html#a1ddf3f4f106c7a3d32e98ad2a6b6319d)(\_key)   (([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce))(\_key >> 32)) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef [AK::IAkPlugin](class_a_k_1_1_i_ak_plugin.html) \*(\* | [AkCreatePluginCallback](_i_ak_plugin_8h_a5fb143c8d06bc9df4c0a4ced1d7a7859.html#a5fb143c8d06bc9df4c0a4ced1d7a7859)) ([AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator) |
|  | Registered plugin creation function prototype. [更多...](_i_ak_plugin_8h_a5fb143c8d06bc9df4c0a4ced1d7a7859.html#a5fb143c8d06bc9df4c0a4ced1d7a7859) |
|  | |
| typedef [AK::IAkPluginParam](class_a_k_1_1_i_ak_plugin_param.html) \*(\* | [AkCreateParamCallback](_i_ak_plugin_8h_adb99175b686d5a1fb37b722312b3cb37.html#adb99175b686d5a1fb37b722312b3cb37)) ([AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator) |
|  | Registered plugin parameter node creation function prototype. [更多...](_i_ak_plugin_8h_adb99175b686d5a1fb37b722312b3cb37.html#adb99175b686d5a1fb37b722312b3cb37) |
|  | |
| typedef [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63)(\* | [AkGetDeviceListCallback](_i_ak_plugin_8h_a37969dcd19e79a5bbe3e511da0e79953.html#a37969dcd19e79a5bbe3e511da0e79953)) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &io\_maxNumDevices, [AkDeviceDescription](struct_ak_device_description.html) \*out\_deviceDescriptions) |
|  | Registered plugin device enumeration function prototype, used for providing lists of devices by plug-ins. [更多...](_i_ak_plugin_8h_a37969dcd19e79a5bbe3e511da0e79953.html#a37969dcd19e79a5bbe3e511da0e79953) |
|  | |

|  |  |
| --- | --- |
| 枚举 | |
| enum | [AK::AkSinkPluginType](namespace_a_k_a53ac2a4bfdb06caaa95809e00c062786.html#a53ac2a4bfdb06caaa95809e00c062786) { [AK::AkSinkPluginType\_Sink](namespace_a_k_a53ac2a4bfdb06caaa95809e00c062786.html#a53ac2a4bfdb06caaa95809e00c062786a05be0a3889fd3e25485aeef42e235e6d), [AK::AkSinkPluginType\_3DAudioSink](namespace_a_k_a53ac2a4bfdb06caaa95809e00c062786.html#a53ac2a4bfdb06caaa95809e00c062786a5db0d076e65382c5f3426536e0f9ba0f) } |
|  | |
| enum | [AK::AkPluginServiceType](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99) {     [AK::PluginServiceType\_Mixer](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99a9946a61f93783dbcfe0534bca5412086) = 0, [AK::PluginServiceType\_RNG](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99a93e55d84981a0b90ed8013c70f079c50) = 1, [AK::PluginServiceType\_AudioObjectAttenuation](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99a7f057c026db8cfeae242a805eb38f15b) = 2, [AK::PluginServiceType\_AudioObjectPriority](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99a468f48cde731c659d49ef159e49b845f) = 3,     [AK::PluginServiceType\_HashTable](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99a997d534c2263e1c8f7726f6e038d46d2) = 4, [AK::PluginServiceType\_Markers](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99acc3dc895483686decb0b9c29294cf956) = 5, [AK::PluginServiceType\_TempAlloc](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99aee6c7322e6ef27b9969c8ab43b3b07b4) = 6, [AK::PluginServiceType\_WavFileWriter](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99a901ac2dc1e4a8a7d11827a063fd7b784) = 7,     [AK::PluginServiceType\_Meter](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99a822d77a52b3b7ccc17268be9f511034b) = 8, [AK::PluginServiceType\_PlatformFuncs](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99aedc16252b07df57890a019b6cb3fe4db) = 9, [AK::PluginServiceType\_MAX](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99a3c80c68d800ef171ba594513ac9719be)   } |
|  | |

|  |  |
| --- | --- |
| 变量 | |
| [AK\_DLLEXPORT](_platforms_2_windows_2_ak_types_8h_ab291f969500ebc378f2344e1477d2dd7.html#ab291f969500ebc378f2344e1477d2dd7) [AK::PluginRegistration](class_a_k_1_1_plugin_registration.html) \* | [g\_pAKPluginList](_i_ak_plugin_8h_affa96e9a560e3444da2e5ae0d1fae089.html#affa96e9a560e3444da2e5ae0d1fae089) |
|  | |

## 详细描述

Software source plug-in and effect plug-in interfaces.

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 中定义.