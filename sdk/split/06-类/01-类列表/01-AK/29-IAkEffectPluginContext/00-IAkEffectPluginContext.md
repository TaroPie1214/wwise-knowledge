# IAkEffectPluginContext

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkEffectPluginContext](class_a_k_1_1_i_ak_effect_plugin_context.html)

[所有成员列表](class_a_k_1_1_i_ak_effect_plugin_context-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkEffectPluginContext类 参考abstract

`#include <IAkPlugin.h>`

类 AK::IAkEffectPluginContext 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_effect_plugin_context.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual bool | [IsSendModeEffect](class_a_k_1_1_i_ak_effect_plugin_context_ab8ec44868a3781a40320336c2eedf82e.html#ab8ec44868a3781a40320336c2eedf82e) () const =0 |
|  | |
| virtual [IAkVoicePluginInfo](class_a_k_1_1_i_ak_voice_plugin_info.html) \* | [GetVoiceInfo](class_a_k_1_1_i_ak_effect_plugin_context_a65bf3ee948fceba3225fe2a3f501cab5.html#a65bf3ee948fceba3225fe2a3f501cab5) ()=0 |
|  | |
| virtual [IAkMixerPluginContext](class_a_k_1_1_i_ak_mixer_plugin_context.html) \* | [GetMixerCtx](class_a_k_1_1_i_ak_effect_plugin_context_a003265e118a7fac508d5a47a94f95f20.html#a003265e118a7fac508d5a47a94f95f20) ()=0 |
|  | |
| For object processors: | |
| Output object management. | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [CreateOutputObjects](class_a_k_1_1_i_ak_effect_plugin_context_a96f65eb02b520f2ca5af497e645971a0.html#a96f65eb02b520f2ca5af497e645971a0) ([AkChannelConfig](struct_ak_channel_config.html) in\_channelConfig, [AkAudioObjects](struct_ak_audio_objects.html) &io\_objects)=0 |
|  | |
| virtual void | [GetOutputObjects](class_a_k_1_1_i_ak_effect_plugin_context_ad0b9c549569b25dea349d2a352f02e58.html#ad0b9c549569b25dea349d2a352f02e58) ([AkAudioObjects](struct_ak_audio_objects.html) &io\_objects)=0 |
|  | |
| For effects: | |
| Sidechain mix management. | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetSidechainMixChannelConfig](class_a_k_1_1_i_ak_effect_plugin_context_ae9aed89a6cf7530e7cc3a011eb683f45.html#ae9aed89a6cf7530e7cc3a011eb683f45) ([AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_uSidechainId, [AkChannelConfig](struct_ak_channel_config.html) \*out\_pChannelCfg)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [SendToSidechainMix](class_a_k_1_1_i_ak_effect_plugin_context_a3143735cd105b3b7673ee11179756ed7.html#a3143735cd105b3b7673ee11179756ed7) ([AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_uSidechainId, [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) in\_uSidechainScopeId, [AkAudioBuffer](class_ak_audio_buffer.html) \*in\_pAudioBuffer)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [ReceiveFromSidechainMix](class_a_k_1_1_i_ak_effect_plugin_context_ae9c831158402c426f22a3a59e2938dd3.html#ae9c831158402c426f22a3a59e2938dd3) ([AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_uSidechainId, [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) in\_uSidechainScopeId, [AkAudioBuffer](class_ak_audio_buffer.html) \*io\_pAudioBuffer)=0 |
|  | |
| - Public 成员函数 继承自 [AK::IAkPluginContextBase](class_a_k_1_1_i_ak_plugin_context_base.html) | |
| virtual [IAkGlobalPluginContext](class_a_k_1_1_i_ak_global_plugin_context.html) \* | [GlobalContext](class_a_k_1_1_i_ak_plugin_context_base_af02337aeaffd800ffce912a6c4231e0f.html#af02337aeaffd800ffce912a6c4231e0f) () const =0 |
|  | |
| virtual [IAkGameObjectPluginInfo](class_a_k_1_1_i_ak_game_object_plugin_info.html) \* | [GetGameObjectInfo](class_a_k_1_1_i_ak_plugin_context_base_a4c26b12664c7a9b73b6efc363a74a2e3.html#a4c26b12664c7a9b73b6efc363a74a2e3) ()=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetOutputID](class_a_k_1_1_i_ak_plugin_context_base_a34644116256a32c1ea4763411502aded.html#a34644116256a32c1ea4763411502aded) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &out\_uOutputID, [AkPluginID](_ak_typedefs_8h_ad1d16d137b445ef6f7c2dd5ff1c9a6d8.html#ad1d16d137b445ef6f7c2dd5ff1c9a6d8) &out\_uDevicePlugin) const =0 |
|  | |
| virtual void | [GetPluginMedia](class_a_k_1_1_i_ak_plugin_context_base_a36514f7827919ee6c85a56295141297a.html#a36514f7827919ee6c85a56295141297a) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_dataIndex, [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \*&out\_rpData, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &out\_rDataSize)=0 |
|  | |
| virtual void | [GetPluginCustomGameData](class_a_k_1_1_i_ak_plugin_context_base_ac1312db4f8b44c176e9064f258c020a3.html#ac1312db4f8b44c176e9064f258c020a3) (void \*&out\_rpData, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &out\_rDataSize)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [PostMonitorData](class_a_k_1_1_i_ak_plugin_context_base_a417bd7aecedf5ed80a47615f053694d1.html#a417bd7aecedf5ed80a47615f053694d1) (void \*in\_pData, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uDataSize)=0 |
|  | |
| virtual bool | [CanPostMonitorData](class_a_k_1_1_i_ak_plugin_context_base_a5b687dfb16b2a2103a0f7f1c636d6433.html#a5b687dfb16b2a2103a0f7f1c636d6433) ()=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [PostMonitorMessage](class_a_k_1_1_i_ak_plugin_context_base_a0a546e54d0b286da2a28da3ab606b067.html#a0a546e54d0b286da2a28da3ab606b067) (const char \*in\_pszError, [AK::Monitor::ErrorLevel](namespace_a_k_1_1_monitor_a75374a589b6f43efc84d695d101698de.html#a75374a589b6f43efc84d695d101698de) in\_eErrorLevel)=0 |
|  | |
| virtual [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [GetDownstreamGain](class_a_k_1_1_i_ak_plugin_context_base_a013711c35020c07ddaccc0af056de569.html#a013711c35020c07ddaccc0af056de569) ()=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetParentChannelConfig](class_a_k_1_1_i_ak_plugin_context_base_a95001097b7f9ea30cb3167b14390c7f2.html#a95001097b7f9ea30cb3167b14390c7f2) ([AkChannelConfig](struct_ak_channel_config.html) &out\_channelConfig) const =0 |
|  | |
| virtual [IAkProcessorFeatures](class_a_k_1_1_i_ak_processor_features.html) \* | [GetProcessorFeatures](class_a_k_1_1_i_ak_plugin_context_base_a21803ca5364dfaf2fd15114f9e362cf3.html#a21803ca5364dfaf2fd15114f9e362cf3) ()=0 |
|  | Return an interface to query processor specific features. [更多...](class_a_k_1_1_i_ak_plugin_context_base_a21803ca5364dfaf2fd15114f9e362cf3.html#a21803ca5364dfaf2fd15114f9e362cf3) |
|  | |
| virtual [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [GetAudioNodeID](class_a_k_1_1_i_ak_plugin_context_base_a9e34e7ea7024748bffb8bea5ea3eb652.html#a9e34e7ea7024748bffb8bea5ea3eb652) () const =0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetSinkChannelConfig](class_a_k_1_1_i_ak_plugin_context_base_a6caf99e5702a3e38ef7f45dea644605e.html#a6caf99e5702a3e38ef7f45dea644605e) ([AkChannelConfig](struct_ak_channel_config.html) &out\_sinkConfig, [Ak3DAudioSinkCapabilities](struct_ak3_d_audio_sink_capabilities.html) &out\_3dAudioCaps) const =0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetOutputDeviceInfo](class_a_k_1_1_i_ak_plugin_context_base_a63d145ee193a2498bd18c36d1da22f85.html#a63d145ee193a2498bd18c36d1da22f85) ([AkOutputDeviceInfo](struct_ak_output_device_info.html) &out\_outputDeviceInfo) const =0 |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkEffectPluginContext](class_a_k_1_1_i_ak_effect_plugin_context_a993d03fa58554d45b1eaa0c31f467248.html#a993d03fa58554d45b1eaa0c31f467248) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_effect_plugin_context_a993d03fa58554d45b1eaa0c31f467248.html#a993d03fa58554d45b1eaa0c31f467248) |
|  | |
| - Protected 成员函数 继承自 [AK::IAkPluginContextBase](class_a_k_1_1_i_ak_plugin_context_base.html) | |
| virtual | [~IAkPluginContextBase](class_a_k_1_1_i_ak_plugin_context_base_a8b6799a3216c6fbf95b253e13bf167d6.html#a8b6799a3216c6fbf95b253e13bf167d6) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_plugin_context_base_a8b6799a3216c6fbf95b253e13bf167d6.html#a8b6799a3216c6fbf95b253e13bf167d6) |
|  | |

## 详细描述

Interface to retrieve contextual information for an effect plug-in.

参见
:   - [AK::IAkEffectPlugin::Init()](soundengine_plugins_effects.html#iakmonadiceffect_init)

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [369](_i_ak_plugin_8h_source.html#l00369) 行定义.