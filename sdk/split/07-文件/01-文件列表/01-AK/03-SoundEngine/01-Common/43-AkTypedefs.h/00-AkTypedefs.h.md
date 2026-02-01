# AkTypedefs.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[命名空间](#namespaces) |
[类型定义](#typedef-members)

AkTypedefs.h 文件参考

`#include <AK/SoundEngine/Common/AkNumeralTypes.h>`

[浏览源代码.](_ak_typedefs_8h_source.html)

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
|  | [AK::SpeakerVolumes](namespace_a_k_1_1_speaker_volumes.html) |
|  | Multi-channel volume definitions and services. |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) |
|  | Unique 32-bit ID [更多...](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkStateID](_ak_typedefs_8h_a70ba3fe9852a8785242bf70622c43c34.html#a70ba3fe9852a8785242bf70622c43c34) |
|  | State ID [更多...](_ak_typedefs_8h_a70ba3fe9852a8785242bf70622c43c34.html#a70ba3fe9852a8785242bf70622c43c34) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkStateGroupID](_ak_typedefs_8h_a5b95307c78b6becd02f3cdc4b3968c57.html#a5b95307c78b6becd02f3cdc4b3968c57) |
|  | State group ID [更多...](_ak_typedefs_8h_a5b95307c78b6becd02f3cdc4b3968c57.html#a5b95307c78b6becd02f3cdc4b3968c57) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) |
|  | A unique identifier generated whenever a PostEvent is called (or when a Dynamic Sequence is created). This identifier serves as a handle to control and interact with individual playback instances, such as stopping a specific instance, and is the ID used in the EndOfEvent callback (see AkCallbackType). [更多...](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) |
|  | |
| typedef [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) |
|  | Time in ms [更多...](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) |
|  | |
| typedef [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [AkPortNumber](_ak_typedefs_8h_a4ab1a0ac2afbade7049afe246459f0ce.html#a4ab1a0ac2afbade7049afe246459f0ce) |
|  | Port number [更多...](_ak_typedefs_8h_a4ab1a0ac2afbade7049afe246459f0ce.html#a4ab1a0ac2afbade7049afe246459f0ce) |
|  | |
| typedef [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [AkPitchValue](_ak_typedefs_8h_ae6a727d55d279f691a0b95c651c15985.html#ae6a727d55d279f691a0b95c651c15985) |
|  | Pitch value [更多...](_ak_typedefs_8h_ae6a727d55d279f691a0b95c651c15985.html#ae6a727d55d279f691a0b95c651c15985) |
|  | |
| typedef [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [AkVolumeValue](_ak_typedefs_8h_a1cbfaa9928bc0ac91853d04fcba6c617.html#a1cbfaa9928bc0ac91853d04fcba6c617) |
|  | Volume value( also apply to LFE ) [更多...](_ak_typedefs_8h_a1cbfaa9928bc0ac91853d04fcba6c617.html#a1cbfaa9928bc0ac91853d04fcba6c617) |
|  | |
| typedef [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) |
|  | Game object ID [更多...](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) |
|  | |
| typedef [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [AkLPFType](_ak_typedefs_8h_a2cc45412d6a5527f94c0f5a6da620c04.html#a2cc45412d6a5527f94c0f5a6da620c04) |
|  | Low-pass filter type [更多...](_ak_typedefs_8h_a2cc45412d6a5527f94c0f5a6da620c04.html#a2cc45412d6a5527f94c0f5a6da620c04) |
|  | |
| typedef [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [AkMemPoolId](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) |
|  | Memory pool ID [更多...](_ak_typedefs_8h_a58f62d75df808bf7c4e56b81c4025696.html#a58f62d75df808bf7c4e56b81c4025696) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkPluginID](_ak_typedefs_8h_ad1d16d137b445ef6f7c2dd5ff1c9a6d8.html#ad1d16d137b445ef6f7c2dd5ff1c9a6d8) |
|  | Source or effect plug-in ID [更多...](_ak_typedefs_8h_ad1d16d137b445ef6f7c2dd5ff1c9a6d8.html#ad1d16d137b445ef6f7c2dd5ff1c9a6d8) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkCodecID](_ak_typedefs_8h_ae3cd7c34d31c81aa8ac649ac3a0e2206.html#ae3cd7c34d31c81aa8ac649ac3a0e2206) |
|  | Codec plug-in ID [更多...](_ak_typedefs_8h_ae3cd7c34d31c81aa8ac649ac3a0e2206.html#ae3cd7c34d31c81aa8ac649ac3a0e2206) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkAuxBusID](_ak_typedefs_8h_a90cfd84c4feec568941a46c13aa964e0.html#a90cfd84c4feec568941a46c13aa964e0) |
|  | Auxilliary bus ID [更多...](_ak_typedefs_8h_a90cfd84c4feec568941a46c13aa964e0.html#a90cfd84c4feec568941a46c13aa964e0) |
|  | |
| typedef [AkInt16](_ak_numeral_types_8h_a20960d2f96e0ecd7debd52d6633ecaac.html#a20960d2f96e0ecd7debd52d6633ecaac) | [AkPluginParamID](_ak_typedefs_8h_a4cb8ff0b7014efdaa21697f4ef928926.html#a4cb8ff0b7014efdaa21697f4ef928926) |
|  | Source or effect plug-in parameter ID [更多...](_ak_typedefs_8h_a4cb8ff0b7014efdaa21697f4ef928926.html#a4cb8ff0b7014efdaa21697f4ef928926) |
|  | |
| typedef [AkInt8](_ak_numeral_types_8h_a9a599c17e641b222c21ab7f853990a48.html#a9a599c17e641b222c21ab7f853990a48) | [AkPriority](_ak_typedefs_8h_a6fd4ce3da8a0654b665da32c63623433.html#a6fd4ce3da8a0654b665da32c63623433) |
|  | Priority [更多...](_ak_typedefs_8h_a6fd4ce3da8a0654b665da32c63623433.html#a6fd4ce3da8a0654b665da32c63623433) |
|  | |
| typedef [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [AkDataCompID](_ak_typedefs_8h_a9f44ff8ad27ebbc7541c7567a7ec29f8.html#a9f44ff8ad27ebbc7541c7567a7ec29f8) |
|  | Data compression format ID [更多...](_ak_typedefs_8h_a9f44ff8ad27ebbc7541c7567a7ec29f8.html#a9f44ff8ad27ebbc7541c7567a7ec29f8) |
|  | |
| typedef [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [AkDataTypeID](_ak_typedefs_8h_a2c2492d7eac66159d80f80d69c8ccd64.html#a2c2492d7eac66159d80f80d69c8ccd64) |
|  | Data sample type ID [更多...](_ak_typedefs_8h_a2c2492d7eac66159d80f80d69c8ccd64.html#a2c2492d7eac66159d80f80d69c8ccd64) |
|  | |
| typedef [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [AkDataInterleaveID](_ak_typedefs_8h_a25f0ba8543113ea7b34ce6cb143e14ee.html#a25f0ba8543113ea7b34ce6cb143e14ee) |
|  | Data interleaved state ID [更多...](_ak_typedefs_8h_a25f0ba8543113ea7b34ce6cb143e14ee.html#a25f0ba8543113ea7b34ce6cb143e14ee) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkSwitchGroupID](_ak_typedefs_8h_a2b8749ca2320f1ee1c4ebe6b7cf1db26.html#a2b8749ca2320f1ee1c4ebe6b7cf1db26) |
|  | Switch group ID [更多...](_ak_typedefs_8h_a2b8749ca2320f1ee1c4ebe6b7cf1db26.html#a2b8749ca2320f1ee1c4ebe6b7cf1db26) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkSwitchStateID](_ak_typedefs_8h_abcf085b986c625421604d4fc0acd7f1e.html#abcf085b986c625421604d4fc0acd7f1e) |
|  | Switch ID [更多...](_ak_typedefs_8h_abcf085b986c625421604d4fc0acd7f1e.html#abcf085b986c625421604d4fc0acd7f1e) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkRtpcID](_ak_typedefs_8h_a77a3b6fec7d9181ef8e5bae2b37b80d0.html#a77a3b6fec7d9181ef8e5bae2b37b80d0) |
|  | Real time parameter control ID [更多...](_ak_typedefs_8h_a77a3b6fec7d9181ef8e5bae2b37b80d0.html#a77a3b6fec7d9181ef8e5bae2b37b80d0) |
|  | |
| typedef [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [AkRtpcValue](_ak_typedefs_8h_a86459d5c3b5e6055cc885b833661f140.html#a86459d5c3b5e6055cc885b833661f140) |
|  | Real time parameter control value [更多...](_ak_typedefs_8h_a86459d5c3b5e6055cc885b833661f140.html#a86459d5c3b5e6055cc885b833661f140) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkBankID](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349) |
|  | Run time bank ID [更多...](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkBankType](_ak_typedefs_8h_a365fb591a961a6db1e5eb9a1a18dc555.html#a365fb591a961a6db1e5eb9a1a18dc555) |
|  | Run time bank type [更多...](_ak_typedefs_8h_a365fb591a961a6db1e5eb9a1a18dc555.html#a365fb591a961a6db1e5eb9a1a18dc555) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkFileID](_ak_typedefs_8h_adff75ad09d4237d128c034afd17f3b35.html#adff75ad09d4237d128c034afd17f3b35) |
|  | Integer-type file identifier [更多...](_ak_typedefs_8h_adff75ad09d4237d128c034afd17f3b35.html#adff75ad09d4237d128c034afd17f3b35) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkDeviceID](_ak_typedefs_8h_a9fb6f04697979f304a7b2b4f405e8260.html#a9fb6f04697979f304a7b2b4f405e8260) |
|  | I/O device ID [更多...](_ak_typedefs_8h_a9fb6f04697979f304a7b2b4f405e8260.html#a9fb6f04697979f304a7b2b4f405e8260) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkTriggerID](_ak_typedefs_8h_a901799fa6607134b3677918a7014f662.html#a901799fa6607134b3677918a7014f662) |
|  | Trigger ID [更多...](_ak_typedefs_8h_a901799fa6607134b3677918a7014f662.html#a901799fa6607134b3677918a7014f662) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkArgumentValueID](_ak_typedefs_8h_a7265e56561ed1bb5b505dd6a13843018.html#a7265e56561ed1bb5b505dd6a13843018) |
|  | Argument value ID [更多...](_ak_typedefs_8h_a7265e56561ed1bb5b505dd6a13843018.html#a7265e56561ed1bb5b505dd6a13843018) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkChannelMask](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) |
|  | Channel mask (similar to extensibleWavFormat). Bit values are defined in [AkSpeakerConfig.h](_ak_speaker_config_8h.html). [更多...](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkModulatorID](_ak_typedefs_8h_a0525f44019828799131883cdbe613d40.html#a0525f44019828799131883cdbe613d40) |
|  | Modulator ID [更多...](_ak_typedefs_8h_a0525f44019828799131883cdbe613d40.html#a0525f44019828799131883cdbe613d40) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkAcousticTextureID](_ak_typedefs_8h_a640f39d008109a599a45485c2964e935.html#a640f39d008109a599a45485c2964e935) |
|  | Acoustic Texture ID [更多...](_ak_typedefs_8h_a640f39d008109a599a45485c2964e935.html#a640f39d008109a599a45485c2964e935) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkImageSourceID](_ak_typedefs_8h_aa8cb517b34d4fc2a5ad99c122136db30.html#aa8cb517b34d4fc2a5ad99c122136db30) |
|  | Image Source ID [更多...](_ak_typedefs_8h_aa8cb517b34d4fc2a5ad99c122136db30.html#aa8cb517b34d4fc2a5ad99c122136db30) |
|  | |
| typedef [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [AkOutputDeviceID](_ak_typedefs_8h_ab608859e8c575f46ce18433e32aa2ccd.html#ab608859e8c575f46ce18433e32aa2ccd) |
|  | Audio Output device ID [更多...](_ak_typedefs_8h_ab608859e8c575f46ce18433e32aa2ccd.html#ab608859e8c575f46ce18433e32aa2ccd) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkPipelineID](_ak_typedefs_8h_aa1f98bb2addc6fbfe759902751548cbc.html#aa1f98bb2addc6fbfe759902751548cbc) |
|  | Unique node (bus, voice) identifier for profiling. [更多...](_ak_typedefs_8h_aa1f98bb2addc6fbfe759902751548cbc.html#aa1f98bb2addc6fbfe759902751548cbc) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkRayID](_ak_typedefs_8h_a6b3ca56233651c0a07ca61993688a888.html#a6b3ca56233651c0a07ca61993688a888) |
|  | Unique (per emitter) identifier for an emitter-listener ray. [更多...](_ak_typedefs_8h_a6b3ca56233651c0a07ca61993688a888.html#a6b3ca56233651c0a07ca61993688a888) |
|  | |
| typedef [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [AkAudioObjectID](_ak_typedefs_8h_a6cadc0376ae4f945438db69f6306f21a.html#a6cadc0376ae4f945438db69f6306f21a) |
|  | Audio Object ID [更多...](_ak_typedefs_8h_a6cadc0376ae4f945438db69f6306f21a.html#a6cadc0376ae4f945438db69f6306f21a) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkJobType](_ak_typedefs_8h_a1cc301d7b3b1af3e3051df12fb484e68.html#a1cc301d7b3b1af3e3051df12fb484e68) |
|  | Job type identifier [更多...](_ak_typedefs_8h_a1cc301d7b3b1af3e3051df12fb484e68.html#a1cc301d7b3b1af3e3051df12fb484e68) |
|  | |
| typedef [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [AkCacheID](_ak_typedefs_8h_a5acf1fe33348412dca7d40b4fd007d98.html#a5acf1fe33348412dca7d40b4fd007d98) |
|  | Stream cache block ID. [更多...](_ak_typedefs_8h_a5acf1fe33348412dca7d40b4fd007d98.html#a5acf1fe33348412dca7d40b4fd007d98) |
|  | |
| typedef [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [AkVertIdx](_ak_typedefs_8h_a1a95c4ca5bc0ed5ed18a1c3a0411c4f6.html#a1a95c4ca5bc0ed5ed18a1c3a0411c4f6) |
|  | Index of vertex in SA geometry [更多...](_ak_typedefs_8h_a1a95c4ca5bc0ed5ed18a1c3a0411c4f6.html#a1a95c4ca5bc0ed5ed18a1c3a0411c4f6) |
|  | |
| typedef [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [AkTriIdx](_ak_typedefs_8h_ac81a13a3296704cf7a21c3d34241bf88.html#ac81a13a3296704cf7a21c3d34241bf88) |
|  | Index of triangle in SA geometry [更多...](_ak_typedefs_8h_ac81a13a3296704cf7a21c3d34241bf88.html#ac81a13a3296704cf7a21c3d34241bf88) |
|  | |
| typedef [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [AkSurfIdx](_ak_typedefs_8h_a1d462cf28f5a36878db54c59ab410fc0.html#a1d462cf28f5a36878db54c59ab410fc0) |
|  | Index of surface in SA geometry [更多...](_ak_typedefs_8h_a1d462cf28f5a36878db54c59ab410fc0.html#a1d462cf28f5a36878db54c59ab410fc0) |
|  | |
| typedef [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \* | [AkSpeakerVolumesMatrixPtr](_ak_typedefs_8h_afcd81d4c2e56d86764346716eca7fe4c.html#afcd81d4c2e56d86764346716eca7fe4c) |
|  | |
| typedef [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \* | [AkSpeakerVolumesVectorPtr](_ak_typedefs_8h_ae5106b590fd07a400e9844ec024b22ed.html#ae5106b590fd07a400e9844ec024b22ed) |
|  | Constant volume vector. Access each element with the standard bracket [] operator. [更多...](_ak_typedefs_8h_ae5106b590fd07a400e9844ec024b22ed.html#ae5106b590fd07a400e9844ec024b22ed) |
|  | |
| typedef const [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \* | [AkSpeakerVolumesConstVectorPtr](_ak_typedefs_8h_a865e7f76e37097d6798cfe7c1d4d7368.html#a865e7f76e37097d6798cfe7c1d4d7368) |
|  | Constant volume matrix. Access each input channel vector with [AK::SpeakerVolumes::Matrix::GetChannel()](namespace_a_k_1_1_speaker_volumes_1_1_matrix_a77aabf10ae35e9ccd346662e29fba169.html#a77aabf10ae35e9ccd346662e29fba169). [更多...](_ak_typedefs_8h_a865e7f76e37097d6798cfe7c1d4d7368.html#a865e7f76e37097d6798cfe7c1d4d7368) |
|  | |
| typedef const [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \* | [AkSpeakerVolumesConstMatrixPtr](_ak_typedefs_8h_a87ee08540492a1d21b387b9e691afce1.html#a87ee08540492a1d21b387b9e691afce1) |
|  | Opaque data structure for storing a collection of external sources. Refer to API in [AK/SoundEngine/Common/AkExternalSourceArray.h](_ak_external_source_array_8h.html) to learn how to manipulate this data structure. [更多...](_ak_typedefs_8h_a87ee08540492a1d21b387b9e691afce1.html#a87ee08540492a1d21b387b9e691afce1) |
|  | |
| typedef void \* | [AkExternalSourceArray](_ak_typedefs_8h_a335692278dd11e40d41d21307ca37d34.html#a335692278dd11e40d41d21307ca37d34) |
|  | |
| using | [AK::SpeakerVolumes::VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa) = [AkSpeakerVolumesMatrixPtr](_ak_typedefs_8h_afcd81d4c2e56d86764346716eca7fe4c.html#afcd81d4c2e56d86764346716eca7fe4c) |
|  | |
| using | [AK::SpeakerVolumes::MatrixPtr](namespace_a_k_1_1_speaker_volumes_a57e0ce3a8225a58dd886853164554074.html#a57e0ce3a8225a58dd886853164554074) = [AkSpeakerVolumesVectorPtr](_ak_typedefs_8h_ae5106b590fd07a400e9844ec024b22ed.html#ae5106b590fd07a400e9844ec024b22ed) |
|  | |
| using | [AK::SpeakerVolumes::ConstVectorPtr](namespace_a_k_1_1_speaker_volumes_a095cabe0d4b9f1339e578eeb8a348064.html#a095cabe0d4b9f1339e578eeb8a348064) = [AkSpeakerVolumesConstVectorPtr](_ak_typedefs_8h_a865e7f76e37097d6798cfe7c1d4d7368.html#a865e7f76e37097d6798cfe7c1d4d7368) |
|  | |
| using | [AK::SpeakerVolumes::ConstMatrixPtr](namespace_a_k_1_1_speaker_volumes_ab18a1b6d7ea27c2c3760092d577d0a80.html#ab18a1b6d7ea27c2c3760092d577d0a80) = [AkSpeakerVolumesConstMatrixPtr](_ak_typedefs_8h_a87ee08540492a1d21b387b9e691afce1.html#a87ee08540492a1d21b387b9e691afce1) |
|  | |