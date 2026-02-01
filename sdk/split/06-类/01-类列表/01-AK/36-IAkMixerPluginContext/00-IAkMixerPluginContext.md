# IAkMixerPluginContext

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkMixerPluginContext](class_a_k_1_1_i_ak_mixer_plugin_context.html)

[所有成员列表](class_a_k_1_1_i_ak_mixer_plugin_context-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkMixerPluginContext类 参考abstract

Interface to retrieve contextual information for a mixer.
[更多...](class_a_k_1_1_i_ak_mixer_plugin_context.html#details)

`#include <IAkPlugin.h>`

类 AK::IAkMixerPluginContext 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_mixer_plugin_context.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetBusType](class_a_k_1_1_i_ak_mixer_plugin_context_abe2510dba2f915737d69ea4a45e72e13.html#abe2510dba2f915737d69ea4a45e72e13) ()=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetSpeakerAngles](class_a_k_1_1_i_ak_mixer_plugin_context_a46eff2d4344780db20b65cb2e42e1cf7.html#a46eff2d4344780db20b65cb2e42e1cf7) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \*io\_pfSpeakerAngles, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &io\_uNumAngles, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) &out\_fHeightAngle)=0 |
|  | |
| Services. | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [ComputeSpeakerVolumesDirect](class_a_k_1_1_i_ak_mixer_plugin_context_ab9131df4725689003defce52077eb72f.html#ab9131df4725689003defce52077eb72f) ([AkChannelConfig](struct_ak_channel_config.html) in\_inputConfig, [AkChannelConfig](struct_ak_channel_config.html) in\_outputConfig, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fCenterPerc, [AK::SpeakerVolumes::MatrixPtr](namespace_a_k_1_1_speaker_volumes_a57e0ce3a8225a58dd886853164554074.html#a57e0ce3a8225a58dd886853164554074) out\_mxVolumes)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [ComputeSpeakerVolumesPanner](class_a_k_1_1_i_ak_mixer_plugin_context_adb6fd73743e8ad4bc3a647bbc2323710.html#adb6fd73743e8ad4bc3a647bbc2323710) ([AkSpeakerPanningType](_ak_enums_8h_a229e1503503cb92fbca8a437196b283f.html#a229e1503503cb92fbca8a437196b283f) in\_ePannerType, const [AkVector](struct_ak_vector.html) &in\_position, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fCenterPct, [AkChannelConfig](struct_ak_channel_config.html) in\_inputConfig, [AkChannelConfig](struct_ak_channel_config.html) in\_outputConfig, [AK::SpeakerVolumes::MatrixPtr](namespace_a_k_1_1_speaker_volumes_a57e0ce3a8225a58dd886853164554074.html#a57e0ce3a8225a58dd886853164554074) out\_mxVolumes)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [ComputePlanarVBAPGains](class_a_k_1_1_i_ak_mixer_plugin_context_a1cad9bd59dda2df033b92bdbaf3f9551.html#a1cad9bd59dda2df033b92bdbaf3f9551) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fAngle, [AkChannelConfig](struct_ak_channel_config.html) in\_outputConfig, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fCenterPerc, [AK::SpeakerVolumes::VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa) out\_vVolumes)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [InitSphericalVBAP](class_a_k_1_1_i_ak_mixer_plugin_context_a5d3cf606abd7108bff1e8b6511bef02b.html#a5d3cf606abd7108bff1e8b6511bef02b) ([AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator, const [AkSphericalCoord](struct_ak_spherical_coord.html) \*in\_SphericalPositions, const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_NbPoints, void \*&out\_pPannerData)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [ComputeSphericalVBAPGains](class_a_k_1_1_i_ak_mixer_plugin_context_aa7c859ee24ba912f6663304facdbf332.html#aa7c859ee24ba912f6663304facdbf332) (void \*in\_pPannerData, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fAzimuth, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fElevation, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels, [AK::SpeakerVolumes::VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa) out\_vVolumes)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [TermSphericalVBAP](class_a_k_1_1_i_ak_mixer_plugin_context_a103424aa75d6663b8abcbb56751f1211.html#a103424aa75d6663b8abcbb56751f1211) ([AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAllocator, void \*in\_pPannerData)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Compute3DPositioning](class_a_k_1_1_i_ak_mixer_plugin_context_aa3aebb0cd836c0dcab14e3d862e13626.html#aa3aebb0cd836c0dcab14e3d862e13626) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fAngle, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fElevation, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fSpread, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fFocus, [AkChannelConfig](struct_ak_channel_config.html) in\_inputConfig, [AkChannelMask](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) in\_uInputChanSel, [AkChannelConfig](struct_ak_channel_config.html) in\_outputConfig, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fCenterPerc, [AK::SpeakerVolumes::MatrixPtr](namespace_a_k_1_1_speaker_volumes_a57e0ce3a8225a58dd886853164554074.html#a57e0ce3a8225a58dd886853164554074) out\_mxVolumes)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Compute3DPositioning](class_a_k_1_1_i_ak_mixer_plugin_context_a4fe30d2b6c07aa4c9ccd5c694bd540b7.html#a4fe30d2b6c07aa4c9ccd5c694bd540b7) (const [AkWorldTransform](struct_ak_world_transform.html) &in\_emitter, const [AkWorldTransform](struct_ak_world_transform.html) &in\_listener, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fCenterPerc, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fSpread, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fFocus, [AkChannelConfig](struct_ak_channel_config.html) in\_inputConfig, [AkChannelMask](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) in\_uInputChanSel, [AkChannelConfig](struct_ak_channel_config.html) in\_outputConfig, [AK::SpeakerVolumes::MatrixPtr](namespace_a_k_1_1_speaker_volumes_a57e0ce3a8225a58dd886853164554074.html#a57e0ce3a8225a58dd886853164554074) out\_mxVolumes)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [ComputePositioning](class_a_k_1_1_i_ak_mixer_plugin_context_a0d39528d0bf01ec4e08bc20956dfce2c.html#a0d39528d0bf01ec4e08bc20956dfce2c) (const [AkPositioningData](struct_ak_positioning_data.html) &in\_posData, [AkChannelConfig](struct_ak_channel_config.html) in\_inputConfig, [AkChannelConfig](struct_ak_channel_config.html) in\_outputConfig, [AK::SpeakerVolumes::MatrixPtr](namespace_a_k_1_1_speaker_volumes_a57e0ce3a8225a58dd886853164554074.html#a57e0ce3a8225a58dd886853164554074) out\_mxVolumes)=0 |
|  | |
| Metering. | |
| virtual void | [EnableMetering](class_a_k_1_1_i_ak_mixer_plugin_context_a05e249899e23040caee9d36d7935409c.html#a05e249899e23040caee9d36d7935409c) ([AkMeteringFlags](_ak_enums_8h_a29f798f121cb4138f9c92f8421d5e729.html#a29f798f121cb4138f9c92f8421d5e729) in\_eFlags)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [RegisterAnonymousConfig](class_a_k_1_1_i_ak_mixer_plugin_context_a34798c9b84c516c80967adabf7c30524.html#a34798c9b84c516c80967adabf7c30524) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels, const [AkSphericalCoord](struct_ak_spherical_coord.html) \*in\_SphericalPositions)=0 |
|  | |
| virtual void | [UnregisterAnonymousConfig](class_a_k_1_1_i_ak_mixer_plugin_context_ad4b4511df5923ad9f35874b85fa8926d.html#ad4b4511df5923ad9f35874b85fa8926d) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetAnonymousConnections](class_a_k_1_1_i_ak_mixer_plugin_context_a4e1f287753cfecb1d08f88980f733f92.html#a4e1f287753cfecb1d08f88980f733f92) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uSpeakerIndexToQuery, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) \*out\_pNeighborIndices, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &io\_uNumNeighbors)=0 |
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
| virtual | [~IAkMixerPluginContext](class_a_k_1_1_i_ak_mixer_plugin_context_af112bb684e49f55584d5715f5a6fc0d4.html#af112bb684e49f55584d5715f5a6fc0d4) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_mixer_plugin_context_af112bb684e49f55584d5715f5a6fc0d4.html#af112bb684e49f55584d5715f5a6fc0d4) |
|  | |
| - Protected 成员函数 继承自 [AK::IAkPluginContextBase](class_a_k_1_1_i_ak_plugin_context_base.html) | |
| virtual | [~IAkPluginContextBase](class_a_k_1_1_i_ak_plugin_context_base_a8b6799a3216c6fbf95b253e13bf167d6.html#a8b6799a3216c6fbf95b253e13bf167d6) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_plugin_context_base_a8b6799a3216c6fbf95b253e13bf167d6.html#a8b6799a3216c6fbf95b253e13bf167d6) |
|  | |

## 详细描述

Interface to retrieve contextual information for a mixer.

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [486](_i_ak_plugin_8h_source.html#l00486) 行定义.