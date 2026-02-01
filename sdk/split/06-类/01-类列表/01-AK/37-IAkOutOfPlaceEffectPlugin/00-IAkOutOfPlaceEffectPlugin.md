# IAkOutOfPlaceEffectPlugin

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkOutOfPlaceEffectPlugin](class_a_k_1_1_i_ak_out_of_place_effect_plugin.html)

[所有成员列表](class_a_k_1_1_i_ak_out_of_place_effect_plugin-members.html) |
[Public 成员函数](#pub-methods)

AK::IAkOutOfPlaceEffectPlugin类 参考abstract

Software effect plug-in interface for out-of-place processing (see [创建声音引擎效果器插件](soundengine_plugins_effects.html)).
[更多...](class_a_k_1_1_i_ak_out_of_place_effect_plugin.html#details)

`#include <IAkPlugin.h>`

类 AK::IAkOutOfPlaceEffectPlugin 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_out_of_place_effect_plugin.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual void | [Execute](class_a_k_1_1_i_ak_out_of_place_effect_plugin_afcf5d07295a19209f16538044ac64fef.html#afcf5d07295a19209f16538044ac64fef) ([AkAudioBuffer](class_ak_audio_buffer.html) \*in\_pBuffer, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uInOffset, [AkAudioBuffer](class_ak_audio_buffer.html) \*out\_pBuffer)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [TimeSkip](class_a_k_1_1_i_ak_out_of_place_effect_plugin_a8727a7d95bca7d9a5a7ec21a934d7fb9.html#a8727a7d95bca7d9a5a7ec21a934d7fb9) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &io\_uFrames)=0 |
|  | |
| - Public 成员函数 继承自 [AK::IAkEffectPlugin](class_a_k_1_1_i_ak_effect_plugin.html) | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Init](class_a_k_1_1_i_ak_effect_plugin_ae5a44837c4adddf6ff58fab57453b020.html#ae5a44837c4adddf6ff58fab57453b020) ([IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator, [IAkEffectPluginContext](class_a_k_1_1_i_ak_effect_plugin_context.html) \*in\_pEffectPluginContext, [IAkPluginParam](class_a_k_1_1_i_ak_plugin_param.html) \*in\_pParams, [AkAudioFormat](struct_ak_audio_format.html) &io\_rFormat)=0 |
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
| 额外继承的成员函数 | |
| - Protected 成员函数 继承自 [AK::IAkEffectPlugin](class_a_k_1_1_i_ak_effect_plugin.html) | |
| virtual | [~IAkEffectPlugin](class_a_k_1_1_i_ak_effect_plugin_a97d1c49aeeafb40aade5663e669c9fd7.html#a97d1c49aeeafb40aade5663e669c9fd7) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_effect_plugin_a97d1c49aeeafb40aade5663e669c9fd7.html#a97d1c49aeeafb40aade5663e669c9fd7) |
|  | |
| - Protected 成员函数 继承自 [AK::IAkPlugin](class_a_k_1_1_i_ak_plugin.html) | |
| virtual | [~IAkPlugin](class_a_k_1_1_i_ak_plugin_a49ab8f8ae589b2b53d6977afbf7703e4.html#a49ab8f8ae589b2b53d6977afbf7703e4) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_plugin_a49ab8f8ae589b2b53d6977afbf7703e4.html#a49ab8f8ae589b2b53d6977afbf7703e4) |
|  | |

## 详细描述

Software effect plug-in interface for out-of-place processing (see [创建声音引擎效果器插件](soundengine_plugins_effects.html)).

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [891](_i_ak_plugin_8h_source.html#l00891) 行定义.