# IAkSinkPluginContext

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkSinkPluginContext](class_a_k_1_1_i_ak_sink_plugin_context.html)

[所有成员列表](class_a_k_1_1_i_ak_sink_plugin_context-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkSinkPluginContext类 参考abstract

`#include <IAkPlugin.h>`

类 AK::IAkSinkPluginContext 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_sink_plugin_context.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual bool | [IsPrimary](class_a_k_1_1_i_ak_sink_plugin_context_a5d58583faf36a78c237f2f761c8594d3.html#a5d58583faf36a78c237f2f761c8594d3) ()=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [SignalAudioThread](class_a_k_1_1_i_ak_sink_plugin_context_ad0efd9efdaa789dc4d1bde887119272b.html#ad0efd9efdaa789dc4d1bde887119272b) ()=0 |
|  | |
| virtual [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [GetNumRefillsInVoice](class_a_k_1_1_i_ak_sink_plugin_context_adfdd36812a616fe5c028b610e3bbf8a6.html#adfdd36812a616fe5c028b610e3bbf8a6) ()=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [ComputePositioning](class_a_k_1_1_i_ak_sink_plugin_context_acd63722fe98287b2a61f5fe161d9042b.html#acd63722fe98287b2a61f5fe161d9042b) (const [AkPositioningData](struct_ak_positioning_data.html) &in\_posData, [AkChannelConfig](struct_ak_channel_config.html) in\_inputConfig, [AkChannelConfig](struct_ak_channel_config.html) in\_outputConfig, [AK::SpeakerVolumes::MatrixPtr](namespace_a_k_1_1_speaker_volumes_a57e0ce3a8225a58dd886853164554074.html#a57e0ce3a8225a58dd886853164554074) out\_mxVolumes)=0 |
|  | |
| virtual [AkPanningRule](_ak_enums_8h_a6a7a16f5e74370707bb7bff7fb29a112.html#a6a7a16f5e74370707bb7bff7fb29a112) | [GetPanningRule](class_a_k_1_1_i_ak_sink_plugin_context_a96a5371f48fcb34ba6fd2e9fddee8bf5.html#a96a5371f48fcb34ba6fd2e9fddee8bf5) () const =0 |
|  | Returns the panning rule for the output device to which the sink plug-in is attached. [更多...](class_a_k_1_1_i_ak_sink_plugin_context_a96a5371f48fcb34ba6fd2e9fddee8bf5.html#a96a5371f48fcb34ba6fd2e9fddee8bf5) |
|  | |
| virtual void | [SetOutputDeviceInfoCustomData](class_a_k_1_1_i_ak_sink_plugin_context_ae772afa489bbda9f1f328309c0d9b25a.html#ae772afa489bbda9f1f328309c0d9b25a) (void \*in\_pCustomData)=0 |
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
| virtual | [~IAkSinkPluginContext](class_a_k_1_1_i_ak_sink_plugin_context_a8cb48fd2e25d49e0c8cc16411e91bf37.html#a8cb48fd2e25d49e0c8cc16411e91bf37) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_sink_plugin_context_a8cb48fd2e25d49e0c8cc16411e91bf37.html#a8cb48fd2e25d49e0c8cc16411e91bf37) |
|  | |
| - Protected 成员函数 继承自 [AK::IAkPluginContextBase](class_a_k_1_1_i_ak_plugin_context_base.html) | |
| virtual | [~IAkPluginContextBase](class_a_k_1_1_i_ak_plugin_context_base_a8b6799a3216c6fbf95b253e13bf167d6.html#a8b6799a3216c6fbf95b253e13bf167d6) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_plugin_context_base_a8b6799a3216c6fbf95b253e13bf167d6.html#a8b6799a3216c6fbf95b253e13bf167d6) |
|  | |

## 详细描述

Interface to retrieve contextual information for a sink plugin.

参见
:   - [AK::IAkSinkPlugin](class_a_k_1_1_i_ak_sink_plugin.html "Software interface for sink (audio endpoint) plugins.")

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [1132](_i_ak_plugin_8h_source.html#l01132) 行定义.