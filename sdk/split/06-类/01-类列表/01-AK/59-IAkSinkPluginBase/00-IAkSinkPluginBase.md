# IAkSinkPluginBase

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkSinkPluginBase](class_a_k_1_1_i_ak_sink_plugin_base.html)

[所有成员列表](class_a_k_1_1_i_ak_sink_plugin_base-members.html) |
[Public 成员函数](#pub-methods)

AK::IAkSinkPluginBase类 参考abstract

`#include <IAkPlugin.h>`

类 AK::IAkSinkPluginBase 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_sink_plugin_base.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Init](class_a_k_1_1_i_ak_sink_plugin_base_ab13c519292782b8e485912cb85506f25.html#ab13c519292782b8e485912cb85506f25) ([IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator, [IAkSinkPluginContext](class_a_k_1_1_i_ak_sink_plugin_context.html) \*in\_pSinkPluginContext, [IAkPluginParam](class_a_k_1_1_i_ak_plugin_param.html) \*in\_pParams, [AkAudioFormat](struct_ak_audio_format.html) &io\_rFormat)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [IsDataNeeded](class_a_k_1_1_i_ak_sink_plugin_base_a80d001f02f2c602683951e51a795954e.html#a80d001f02f2c602683951e51a795954e) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &out\_uNumFramesNeeded)=0 |
|  | |
| virtual void | [OnFrameEnd](class_a_k_1_1_i_ak_sink_plugin_base_af7035e026261662fb26bc747eaee77af.html#af7035e026261662fb26bc747eaee77af) ()=0 |
|  | |
| virtual bool | [IsStarved](class_a_k_1_1_i_ak_sink_plugin_base_a857a107760429d52b05741e31967d82f.html#a857a107760429d52b05741e31967d82f) ()=0 |
|  | |
| virtual void | [ResetStarved](class_a_k_1_1_i_ak_sink_plugin_base_ae63b9e00dbba73aaa35912bc82fd0e3f.html#ae63b9e00dbba73aaa35912bc82fd0e3f) ()=0 |
|  | Reset the "starvation" flag after [IsStarved()](class_a_k_1_1_i_ak_sink_plugin_base_a857a107760429d52b05741e31967d82f.html#a857a107760429d52b05741e31967d82f) returned true. [更多...](class_a_k_1_1_i_ak_sink_plugin_base_ae63b9e00dbba73aaa35912bc82fd0e3f.html#ae63b9e00dbba73aaa35912bc82fd0e3f) |
|  | |
| virtual [AkSinkPluginType](namespace_a_k_a53ac2a4bfdb06caaa95809e00c062786.html#a53ac2a4bfdb06caaa95809e00c062786) | [GetSinkPluginType](class_a_k_1_1_i_ak_sink_plugin_base_ad440b6790f9c09050efea27facecba21.html#ad440b6790f9c09050efea27facecba21) () const =0 |
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
| - Protected 成员函数 继承自 [AK::IAkPlugin](class_a_k_1_1_i_ak_plugin.html) | |
| virtual | [~IAkPlugin](class_a_k_1_1_i_ak_plugin_a49ab8f8ae589b2b53d6977afbf7703e4.html#a49ab8f8ae589b2b53d6977afbf7703e4) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_plugin_a49ab8f8ae589b2b53d6977afbf7703e4.html#a49ab8f8ae589b2b53d6977afbf7703e4) |
|  | |

## 详细描述

Software interface for sink (audio endpoint) plugins. This interface should not be implemented directly, Plug-ins should either implement:

- [IAkSinkPlugin](class_a_k_1_1_i_ak_sink_plugin.html "Software interface for sink (audio endpoint) plugins."): for audio endpoint that do not support 3D audio, or
- [IAk3DAudioSinkPlugin](class_a_k_1_1_i_ak3_d_audio_sink_plugin.html "Software plug-in interface for sink (audio end point) which supports 3D audio features."): for audio endpoints that support 3D audio features.

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [1204](_i_ak_plugin_8h_source.html#l01204) 行定义.