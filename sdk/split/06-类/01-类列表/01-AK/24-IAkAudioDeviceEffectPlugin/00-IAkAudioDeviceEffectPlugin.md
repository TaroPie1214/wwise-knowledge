# IAkAudioDeviceEffectPlugin

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkAudioDeviceEffectPlugin](class_a_k_1_1_i_ak_audio_device_effect_plugin.html)

[所有成员列表](class_a_k_1_1_i_ak_audio_device_effect_plugin-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkAudioDeviceEffectPlugin类 参考abstract

`#include <IAkPlugin.h>`

类 AK::IAkAudioDeviceEffectPlugin 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_audio_device_effect_plugin.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Init](class_a_k_1_1_i_ak_audio_device_effect_plugin_ac2b7ed06052a176e4445b743e7b3dfe7.html#ac2b7ed06052a176e4445b743e7b3dfe7) ([IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator, [IAkAudioDeviceEffectPluginContext](class_a_k_1_1_i_ak_audio_device_effect_plugin_context.html) \*in\_pEffectPluginContext, [IAkPluginParam](class_a_k_1_1_i_ak_plugin_param.html) \*in\_pParams, const [AkAudioFormat](struct_ak_audio_format.html) &in\_rFormat, const [Ak3DAudioSinkCapabilities](struct_ak3_d_audio_sink_capabilities.html) &in\_3dCapabilities)=0 |
|  | |
| virtual void | [Execute](class_a_k_1_1_i_ak_audio_device_effect_plugin_abcd7834c6db0840f824a35690bbfe89f.html#abcd7834c6db0840f824a35690bbfe89f) ([AkAudioBuffer](class_ak_audio_buffer.html) \*io\_pMainMix, [AkAudioBuffer](class_ak_audio_buffer.html) \*io\_pPassthroughMix, const [AkAudioObjects](struct_ak_audio_objects.html) &io\_objects, [AkRamp](struct_ak_ramp.html) &io\_gain)=0 |
|  | |
| - Public 成员函数 继承自 [AK::IAkPlugin](class_a_k_1_1_i_ak_plugin.html) | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Term](class_a_k_1_1_i_ak_plugin_a29db8d2afc4fe2571c2c75deb00a359d.html#a29db8d2afc4fe2571c2c75deb00a359d) ([IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Reset](class_a_k_1_1_i_ak_plugin_a08c841c8b811acb993acd0353bd9db75.html#a08c841c8b811acb993acd0353bd9db75) ()=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetPluginInfo](class_a_k_1_1_i_ak_plugin_a5c4cdef6822950045b66834528bd1b55.html#a5c4cdef6822950045b66834528bd1b55) ([AkPluginInfo](struct_ak_plugin_info.html) &out\_rPluginInfo)=0 |
|  | |
| virtual bool | [SupportMediaRelocation](class_a_k_1_1_i_ak_plugin_a0f93c3ed9f133524d8c2b36a00876152.html#a0f93c3ed9f133524d8c2b36a00876152) () const |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [RelocateMedia](class_a_k_1_1_i_ak_plugin_aa63887024a5f2e2ff8f1fb98e864e129.html#aa63887024a5f2e2ff8f1fb98e864e129) ([AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \*, [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \*) |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkAudioDeviceEffectPlugin](class_a_k_1_1_i_ak_audio_device_effect_plugin_abc06ddb57fc9b1bd172f7a3ea0498c47.html#abc06ddb57fc9b1bd172f7a3ea0498c47) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_audio_device_effect_plugin_abc06ddb57fc9b1bd172f7a3ea0498c47.html#abc06ddb57fc9b1bd172f7a3ea0498c47) |
|  | |
| - Protected 成员函数 继承自 [AK::IAkPlugin](class_a_k_1_1_i_ak_plugin.html) | |
| virtual | [~IAkPlugin](class_a_k_1_1_i_ak_plugin_a49ab8f8ae589b2b53d6977afbf7703e4.html#a49ab8f8ae589b2b53d6977afbf7703e4) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_plugin_a49ab8f8ae589b2b53d6977afbf7703e4.html#a49ab8f8ae589b2b53d6977afbf7703e4) |
|  | |

## 详细描述

Audio device effect plug-in interface. Implement this interface for in-place effects that must be applied at the very end of the pipeline. Audio device effects are applied right before sending audio buffers (main mix, passthrough and objects) to the audio device output through IAkSinkPlugin/IAk3DAudioSinkPlugin. The format of the audio buffers passed to the effect matches the format requested by the sink plug-in. This means that audio device effects must be in-place; they cannot change io\_rFormat in [Init()](class_a_k_1_1_i_ak_audio_device_effect_plugin_ac2b7ed06052a176e4445b743e7b3dfe7.html#ac2b7ed06052a176e4445b743e7b3dfe7).

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [976](_i_ak_plugin_8h_source.html#l00976) 行定义.