# IAkGlobalPluginContext

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkGlobalPluginContext](class_a_k_1_1_i_ak_global_plugin_context.html)

[所有成员列表](class_a_k_1_1_i_ak_global_plugin_context-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkGlobalPluginContext类 参考abstract

`#include <IAkPlugin.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [IAkStreamMgr](class_a_k_1_1_i_ak_stream_mgr.html) \* | [GetStreamMgr](class_a_k_1_1_i_ak_global_plugin_context_ae5c194ec87376452acf34f0836211ab3.html#ae5c194ec87376452acf34f0836211ab3) () const =0 |
|  | Retrieve the streaming manager access interface. [更多...](class_a_k_1_1_i_ak_global_plugin_context_ae5c194ec87376452acf34f0836211ab3.html#ae5c194ec87376452acf34f0836211ab3) |
|  | |
| virtual [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [GetMaxBufferLength](class_a_k_1_1_i_ak_global_plugin_context_a1ba5a205d0d845b4cd77306defc6d552.html#a1ba5a205d0d845b4cd77306defc6d552) () const =0 |
|  | |
| virtual bool | [IsRenderingOffline](class_a_k_1_1_i_ak_global_plugin_context_a2208e472445359e2d32f147ae7ff50ff.html#a2208e472445359e2d32f147ae7ff50ff) () const =0 |
|  | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetSampleRate](class_a_k_1_1_i_ak_global_plugin_context_ad42d466f3e556a71e328945ce8e4cdc1.html#ad42d466f3e556a71e328945ce8e4cdc1) () const =0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [PostMonitorMessage](class_a_k_1_1_i_ak_global_plugin_context_a30671527a617fff7175ef739816bd52c.html#a30671527a617fff7175ef739816bd52c) (const char \*in\_pszError, [AK::Monitor::ErrorLevel](namespace_a_k_1_1_monitor_a75374a589b6f43efc84d695d101698de.html#a75374a589b6f43efc84d695d101698de) in\_eErrorLevel)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [RegisterPlugin](class_a_k_1_1_i_ak_global_plugin_context_a2d94926901ecc43539d808af05fe6732.html#a2d94926901ecc43539d808af05fe6732) ([AkPluginType](_ak_enums_8h_af1a95e76b0e2a003e7edb2ad6f4043f4.html#af1a95e76b0e2a003e7edb2ad6f4043f4) in\_eType, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_ulCompanyID, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_ulPluginID, [AkCreatePluginCallback](_i_ak_plugin_8h_a5fb143c8d06bc9df4c0a4ced1d7a7859.html#a5fb143c8d06bc9df4c0a4ced1d7a7859) in\_pCreateFunc, [AkCreateParamCallback](_i_ak_plugin_8h_adb99175b686d5a1fb37b722312b3cb37.html#adb99175b686d5a1fb37b722312b3cb37) in\_pCreateParamFunc)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [RegisterCodec](class_a_k_1_1_i_ak_global_plugin_context_af6b9973f8b035a376209cb29547d5aca.html#af6b9973f8b035a376209cb29547d5aca) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_ulCompanyID, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_ulPluginID, [AkCreateFileSourceCallback](_ak_sound_engine_types_8h_ab1af7c591ff110a96afe92f34cc4e839.html#ab1af7c591ff110a96afe92f34cc4e839) in\_pFileCreateFunc, [AkCreateBankSourceCallback](_ak_sound_engine_types_8h_ae33290ab81b22a844df5c2ab3bf675c2.html#ae33290ab81b22a844df5c2ab3bf675c2) in\_pBankCreateFunc)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [RegisterGlobalCallback](class_a_k_1_1_i_ak_global_plugin_context_a1cbd90dbcb3c0e69a8c80fd4aefc822c.html#a1cbd90dbcb3c0e69a8c80fd4aefc822c) ([AkPluginType](_ak_enums_8h_af1a95e76b0e2a003e7edb2ad6f4043f4.html#af1a95e76b0e2a003e7edb2ad6f4043f4) in\_eType, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_ulCompanyID, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_ulPluginID, [AkGlobalCallbackFunc](_ak_callback_types_8h_a14f2022125839c43179c0c32381b4486.html#a14f2022125839c43179c0c32381b4486) in\_pCallback, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_eLocation=[AkGlobalCallbackLocation\_BeginRender](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676ae4e4ee72acf1bdc317a2922caadb9797), void \*in\_pCookie=NULL)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [UnregisterGlobalCallback](class_a_k_1_1_i_ak_global_plugin_context_a64909d48d5693809ddb5b64b8dabf93a.html#a64909d48d5693809ddb5b64b8dabf93a) ([AkGlobalCallbackFunc](_ak_callback_types_8h_a14f2022125839c43179c0c32381b4486.html#a14f2022125839c43179c0c32381b4486) in\_pCallback, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_eLocation=[AkGlobalCallbackLocation\_BeginRender](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676ae4e4ee72acf1bdc317a2922caadb9797))=0 |
|  | |
| virtual [AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \* | [GetAllocator](class_a_k_1_1_i_ak_global_plugin_context_a9856698ca2c6d1897b7c871e259b93aa.html#a9856698ca2c6d1897b7c871e259b93aa) ()=0 |
|  | Get the default allocator for plugins. This is useful for performing global initialization tasks shared across multiple plugin instances. [更多...](class_a_k_1_1_i_ak_global_plugin_context_a9856698ca2c6d1897b7c871e259b93aa.html#a9856698ca2c6d1897b7c871e259b93aa) |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [SetRTPCValue](class_a_k_1_1_i_ak_global_plugin_context_afd9075833fd9d0d4f3ef1b011f832fe3.html#afd9075833fd9d0d4f3ef1b011f832fe3) ([AkRtpcID](_ak_typedefs_8h_a77a3b6fec7d9181ef8e5bae2b37b80d0.html#a77a3b6fec7d9181ef8e5bae2b37b80d0) in\_rtpcID, [AkRtpcValue](_ak_typedefs_8h_a86459d5c3b5e6055cc885b833661f140.html#a86459d5c3b5e6055cc885b833661f140) in\_value, [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_gameObjectID=[AK\_INVALID\_GAME\_OBJECT](_ak_constants_8h_a82290a98a9cf7901722a69a590aeee34.html#a82290a98a9cf7901722a69a590aeee34), [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) in\_uValueChangeDuration=0, [AkCurveInterpolation](_ak_enums_8h_a77872044bca52a4d20324739154f2399.html#a77872044bca52a4d20324739154f2399) in\_eFadeCurve=[AkCurveInterpolation\_Linear](_ak_enums_8h_a77872044bca52a4d20324739154f2399.html#a77872044bca52a4d20324739154f2399a4bc8df1cfffac8b5239808faf94a112b), bool in\_bBypassInternalValueInterpolation=false)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [SendPluginCustomGameData](class_a_k_1_1_i_ak_global_plugin_context_a0990a4b67942c6cf814d4e159ca61325.html#a0990a4b67942c6cf814d4e159ca61325) ([AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_busID, [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_busObjectID, [AkPluginType](_ak_enums_8h_af1a95e76b0e2a003e7edb2ad6f4043f4.html#af1a95e76b0e2a003e7edb2ad6f4043f4) in\_eType, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uCompanyID, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uPluginID, const void \*in\_pData, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uSizeInBytes)=0 |
|  | |
| virtual void | [ComputeAmbisonicsEncoding](class_a_k_1_1_i_ak_global_plugin_context_ad1a5e85e22b51c76b503a73434889d98.html#ad1a5e85e22b51c76b503a73434889d98) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fAzimuth, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fElevation, [AkChannelConfig](struct_ak_channel_config.html) in\_cfgAmbisonics, [AK::SpeakerVolumes::VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa) out\_vVolumes)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [ComputeWeightedAmbisonicsDecodingFromSampledSphere](class_a_k_1_1_i_ak_global_plugin_context_af398a343e7d94e08f763544f923a3078.html#af398a343e7d94e08f763544f923a3078) (const [AkVector](struct_ak_vector.html) in\_samples[], [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumSamples, [AkChannelConfig](struct_ak_channel_config.html) in\_cfgAmbisonics, [AK::SpeakerVolumes::MatrixPtr](namespace_a_k_1_1_speaker_volumes_a57e0ce3a8225a58dd886853164554074.html#a57e0ce3a8225a58dd886853164554074) out\_mxVolume)=0 |
|  | |
| virtual const [AkAcousticTexture](struct_ak_acoustic_texture.html) \* | [GetAcousticTexture](class_a_k_1_1_i_ak_global_plugin_context_a2594e0911ef6011bf147ed013e98686f.html#a2594e0911ef6011bf147ed013e98686f) ([AkAcousticTextureID](_ak_typedefs_8h_a640f39d008109a599a45485c2964e935.html#a640f39d008109a599a45485c2964e935) in\_AcousticTextureID)=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [ComputeSphericalCoordinates](class_a_k_1_1_i_ak_global_plugin_context_a849a95e404dfaad663683da6229bc977.html#a849a95e404dfaad663683da6229bc977) (const [AkEmitterListenerPair](class_ak_emitter_listener_pair.html) &in\_pair, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) &out\_fAzimuth, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) &out\_fElevation) const =0 |
|  | |
| virtual const [AkPlatformInitSettings](struct_ak_platform_init_settings.html) \* | [GetPlatformInitSettings](class_a_k_1_1_i_ak_global_plugin_context_a0dcbef5e9a4310968eae6e90fc418ee3.html#a0dcbef5e9a4310968eae6e90fc418ee3) () const =0 |
|  | |
| virtual const [AkInitSettings](struct_ak_init_settings.html) \* | [GetInitSettings](class_a_k_1_1_i_ak_global_plugin_context_a7de894919a565dc0d091b12c6c08a2b3.html#a7de894919a565dc0d091b12c6c08a2b3) () const =0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetAudioSettings](class_a_k_1_1_i_ak_global_plugin_context_a99fe726affb887fde52487ba3df7222c.html#a99fe726affb887fde52487ba3df7222c) ([AkAudioSettings](struct_ak_audio_settings.html) &out\_audioSettings) const =0 |
|  | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetIDFromString](class_a_k_1_1_i_ak_global_plugin_context_a3b1f5ea7246fb0e3839c9ab7c80777b1.html#a3b1f5ea7246fb0e3839c9ab7c80777b1) (const char \*in\_pszString) const =0 |
|  | |
| virtual [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) | [PostEventSync](class_a_k_1_1_i_ak_global_plugin_context_ab33f12a001718c88fa6f139203c18a64.html#ab33f12a001718c88fa6f139203c18a64) ([AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_eventID, [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_gameObjectID, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uFlags=0, [AkCallbackFunc](_ak_callback_types_8h_af644072775b1cdd813e2d32792a22005.html#af644072775b1cdd813e2d32792a22005) in\_pfnCallback=NULL, void \*in\_pCookie=NULL, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_cExternals=0, [AkExternalSourceInfo](struct_ak_external_source_info.html) \*in\_pExternalSources=NULL, [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_PlayingID=[AK\_INVALID\_PLAYING\_ID](_ak_constants_8h_a5141397d9cce5d9656f58931596d8360.html#a5141397d9cce5d9656f58931596d8360))=0 |
|  | |
| virtual [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) | [PostMIDIOnEventSync](class_a_k_1_1_i_ak_global_plugin_context_a78a49d311d2b439e646283b8be88e9df.html#a78a49d311d2b439e646283b8be88e9df) ([AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_eventID, [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_gameObjectID, [AkMIDIPost](struct_ak_m_i_d_i_post.html) \*in\_pPosts, [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) in\_uNumPosts, bool in\_bAbsoluteOffsets=false, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uFlags=0, [AkCallbackFunc](_ak_callback_types_8h_af644072775b1cdd813e2d32792a22005.html#af644072775b1cdd813e2d32792a22005) in\_pfnCallback=NULL, void \*in\_pCookie=NULL, [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID=[AK\_INVALID\_PLAYING\_ID](_ak_constants_8h_a5141397d9cce5d9656f58931596d8360.html#a5141397d9cce5d9656f58931596d8360))=0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [StopMIDIOnEventSync](class_a_k_1_1_i_ak_global_plugin_context_a448f80c35d70764785818c846f36c497.html#a448f80c35d70764785818c846f36c497) ([AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_eventID=[AK\_INVALID\_UNIQUE\_ID](_ak_constants_8h_aa512c62662d05d5b50dd08792ed254ec.html#aa512c62662d05d5b50dd08792ed254ec), [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_gameObjectID=[AK\_INVALID\_GAME\_OBJECT](_ak_constants_8h_a82290a98a9cf7901722a69a590aeee34.html#a82290a98a9cf7901722a69a590aeee34), [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID=[AK\_INVALID\_PLAYING\_ID](_ak_constants_8h_a5141397d9cce5d9656f58931596d8360.html#a5141397d9cce5d9656f58931596d8360))=0 |
|  | |
| virtual [IAkPlatformContext](class_a_k_1_1_i_ak_platform_context.html) \* | [GetPlatformContext](class_a_k_1_1_i_ak_global_plugin_context_a30092cae52c9cc349f0470813cf23489.html#a30092cae52c9cc349f0470813cf23489) () const =0 |
|  | |
| virtual [IAkPluginService](class_a_k_1_1_i_ak_plugin_service.html) \* | [GetPluginService](class_a_k_1_1_i_ak_global_plugin_context_ac9cfbfdf2d01551973f6a2d2fa0bd79a.html#ac9cfbfdf2d01551973f6a2d2fa0bd79a) ([AkPluginServiceType](namespace_a_k_af21d087f0ff78d7b237ee1b3e4ca0d99.html#af21d087f0ff78d7b237ee1b3e4ca0d99) in\_pluginService) const =0 |
|  | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetBufferTick](class_a_k_1_1_i_ak_global_plugin_context_a5da76be02e2e833451729d87294ab501.html#a5da76be02e2e833451729d87294ab501) () const =0 |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkGlobalPluginContext](class_a_k_1_1_i_ak_global_plugin_context_ace097f601c3e0f4c3ab16d87acfb81c2.html#ace097f601c3e0f4c3ab16d87acfb81c2) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_global_plugin_context_ace097f601c3e0f4c3ab16d87acfb81c2.html#ace097f601c3e0f4c3ab16d87acfb81c2) |
|  | |

## 详细描述

Global plug-in context used for plug-in registration/initialization. Games query this interface from the sound engine, via [AK::SoundEngine::GetGlobalPluginContext](namespace_a_k_1_1_sound_engine_a3fa34f66e9111147d8c4c0f5ba1f2175.html#a3fa34f66e9111147d8c4c0f5ba1f2175). Plug-ins query it via [IAkPluginContextBase::GlobalContext](class_a_k_1_1_i_ak_plugin_context_base_af02337aeaffd800ffce912a6c4231e0f.html#af02337aeaffd800ffce912a6c4231e0f).

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [1441](_i_ak_plugin_8h_source.html#l01441) 行定义.