# IAkSourcePlugin

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkSourcePlugin](class_a_k_1_1_i_ak_source_plugin.html)

[所有成员列表](class_a_k_1_1_i_ak_source_plugin-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkSourcePlugin类 参考abstract

[Wwise](namespace_a_k_1_1_wwise.html) sound engine source plug-in interface (see [创建声音引擎源插件](soundengine_plugins_source.html)).
[更多...](class_a_k_1_1_i_ak_source_plugin.html#details)

`#include <IAkPlugin.h>`

类 AK::IAkSourcePlugin 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_source_plugin.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Init](class_a_k_1_1_i_ak_source_plugin_a101429095bd300db35cb0795254a9a53.html#a101429095bd300db35cb0795254a9a53) ([IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator, [IAkSourcePluginContext](class_a_k_1_1_i_ak_source_plugin_context.html) \*in\_pSourcePluginContext, [IAkPluginParam](class_a_k_1_1_i_ak_plugin_param.html) \*in\_pParams, [AkAudioFormat](struct_ak_audio_format.html) &io\_rFormat)=0 |
|  | |
| virtual [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [GetDuration](class_a_k_1_1_i_ak_source_plugin_a4c8275d25be4ecd749f826e01eb2146d.html#a4c8275d25be4ecd749f826e01eb2146d) () const =0 |
|  | |
| virtual [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [GetEnvelope](class_a_k_1_1_i_ak_source_plugin_a784c7888972589c6950733c1e973a4dc.html#a784c7888972589c6950733c1e973a4dc) () const |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [StopLooping](class_a_k_1_1_i_ak_source_plugin_a90b20371bc8108b3732d41b143a6b1d1.html#a90b20371bc8108b3732d41b143a6b1d1) () |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Seek](class_a_k_1_1_i_ak_source_plugin_ad2df8301433c4e8e6451e2ef4d784902.html#ad2df8301433c4e8e6451e2ef4d784902) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)) |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [TimeSkip](class_a_k_1_1_i_ak_source_plugin_ab6e9eccafd2116ff234f78298ae845c7.html#ab6e9eccafd2116ff234f78298ae845c7) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &) |
|  | |
| virtual void | [Execute](class_a_k_1_1_i_ak_source_plugin_ab23f5541d13b0d126131d83ae48b2588.html#ab23f5541d13b0d126131d83ae48b2588) ([AkAudioBuffer](class_ak_audio_buffer.html) \*io\_pBuffer)=0 |
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
| virtual | [~IAkSourcePlugin](class_a_k_1_1_i_ak_source_plugin_a368a77ffe75c52a3d545e9c3e54b6ab5.html#a368a77ffe75c52a3d545e9c3e54b6ab5) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_source_plugin_a368a77ffe75c52a3d545e9c3e54b6ab5.html#a368a77ffe75c52a3d545e9c3e54b6ab5) |
|  | |
| - Protected 成员函数 继承自 [AK::IAkPlugin](class_a_k_1_1_i_ak_plugin.html) | |
| virtual | [~IAkPlugin](class_a_k_1_1_i_ak_plugin_a49ab8f8ae589b2b53d6977afbf7703e4.html#a49ab8f8ae589b2b53d6977afbf7703e4) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_plugin_a49ab8f8ae589b2b53d6977afbf7703e4.html#a49ab8f8ae589b2b53d6977afbf7703e4) |
|  | |

## 详细描述

[Wwise](namespace_a_k_1_1_wwise.html) sound engine source plug-in interface (see [创建声音引擎源插件](soundengine_plugins_source.html)).

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [1308](_i_ak_plugin_8h_source.html#l01308) 行定义.