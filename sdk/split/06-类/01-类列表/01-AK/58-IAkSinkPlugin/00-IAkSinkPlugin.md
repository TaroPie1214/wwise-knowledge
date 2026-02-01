# IAkSinkPlugin

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkSinkPlugin](class_a_k_1_1_i_ak_sink_plugin.html)

[所有成员列表](class_a_k_1_1_i_ak_sink_plugin-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkSinkPlugin类 参考abstract

Software interface for sink (audio endpoint) plugins.
[更多...](class_a_k_1_1_i_ak_sink_plugin.html#details)

`#include <IAkPlugin.h>`

类 AK::IAkSinkPlugin 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_sink_plugin.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual void | [Consume](class_a_k_1_1_i_ak_sink_plugin_a72ea6266f695a0672ee0af6eaca81342.html#a72ea6266f695a0672ee0af6eaca81342) ([AkAudioBuffer](class_ak_audio_buffer.html) \*in\_pInputBuffer, [AkRamp](struct_ak_ramp.html) in\_gain)=0 |
|  | |
| virtual [AkSinkPluginType](namespace_a_k_a53ac2a4bfdb06caaa95809e00c062786.html#a53ac2a4bfdb06caaa95809e00c062786) | [GetSinkPluginType](class_a_k_1_1_i_ak_sink_plugin_aaeddc063d9af4884466d63021d6157ae.html#aaeddc063d9af4884466d63021d6157ae) () const override final |
|  | |
| - Public 成员函数 继承自 [AK::IAkSinkPluginBase](class_a_k_1_1_i_ak_sink_plugin_base.html) | |
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
| virtual | [~IAkSinkPlugin](class_a_k_1_1_i_ak_sink_plugin_a618d074e159bc05447ae15d90a843826.html#a618d074e159bc05447ae15d90a843826) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_sink_plugin_a618d074e159bc05447ae15d90a843826.html#a618d074e159bc05447ae15d90a843826) |
|  | |
| - Protected 成员函数 继承自 [AK::IAkPlugin](class_a_k_1_1_i_ak_plugin.html) | |
| virtual | [~IAkPlugin](class_a_k_1_1_i_ak_plugin_a49ab8f8ae589b2b53d6977afbf7703e4.html#a49ab8f8ae589b2b53d6977afbf7703e4) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_plugin_a49ab8f8ae589b2b53d6977afbf7703e4.html#a49ab8f8ae589b2b53d6977afbf7703e4) |
|  | |

## 详细描述

Software interface for sink (audio endpoint) plugins.

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [1256](_i_ak_plugin_8h_source.html#l01256) 行定义.