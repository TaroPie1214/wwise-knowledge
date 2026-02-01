# Query

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [SoundEngine](namespace_a_k_1_1_sound_engine.html)
- [Query](namespace_a_k_1_1_sound_engine_1_1_query.html)

[类](#nested-classes)

AK::SoundEngine::Query 命名空间参考

|  |  |
| --- | --- |
| 类 | |
| struct | [GameObjDst](struct_a_k_1_1_sound_engine_1_1_query_1_1_game_obj_dst.html) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| Game Objects | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetPosition](namespace_a_k_1_1_sound_engine_1_1_query_a11b05ff925874e08c7a61e42fd77d79e.html#a11b05ff925874e08c7a61e42fd77d79e) ([AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_GameObjectID, AkSoundPosition &out\_rPosition) |
|  | |
| Listeners | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetListeners](namespace_a_k_1_1_sound_engine_1_1_query_a55f23a77943741c12ac83e408914b22d.html#a55f23a77943741c12ac83e408914b22d) ([AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_GameObjectID, [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) \*out\_ListenerObjectIDs, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &oi\_uNumListeners) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetListenerPosition](namespace_a_k_1_1_sound_engine_1_1_query_a0bec0fba57ed758d4c53e3b6e8335ae7.html#a0bec0fba57ed758d4c53e3b6e8335ae7) ([AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_uListenerID, AkListenerPosition &out\_rPosition) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetListenerSpatialization](namespace_a_k_1_1_sound_engine_1_1_query_af7c6175f6c711203ada6ecd9ea0eb7d9.html#af7c6175f6c711203ada6ecd9ea0eb7d9) ([AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_uListenerID, bool &out\_rbSpatialized, [AK::SpeakerVolumes::VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa) &out\_pVolumeOffsets, [AkChannelConfig](struct_ak_channel_config.html) &out\_channelConfig) |
|  | |

|  |  |
| --- | --- |
| Game Syncs | |
| enum | [RTPCValue\_type](namespace_a_k_1_1_sound_engine_1_1_query_a59744f5b2f507550a0484fb228934f54.html#a59744f5b2f507550a0484fb228934f54) {     [RTPCValue\_Default](namespace_a_k_1_1_sound_engine_1_1_query_a59744f5b2f507550a0484fb228934f54.html#a59744f5b2f507550a0484fb228934f54ac385897091f46227b0107774139766fe), [RTPCValue\_Global](namespace_a_k_1_1_sound_engine_1_1_query_a59744f5b2f507550a0484fb228934f54.html#a59744f5b2f507550a0484fb228934f54a2a69aa4f30ccb5fa27ef5af3803ee911), [RTPCValue\_GameObject](namespace_a_k_1_1_sound_engine_1_1_query_a59744f5b2f507550a0484fb228934f54.html#a59744f5b2f507550a0484fb228934f54a863caab9110740da13912979a98e06e1), [RTPCValue\_PlayingID](namespace_a_k_1_1_sound_engine_1_1_query_a59744f5b2f507550a0484fb228934f54.html#a59744f5b2f507550a0484fb228934f54aaaf9d13f39a5ed92676225a5c83a5899),     [RTPCValue\_Unavailable](namespace_a_k_1_1_sound_engine_1_1_query_a59744f5b2f507550a0484fb228934f54.html#a59744f5b2f507550a0484fb228934f54a35b3aaef8126ae8a830d46ba792bebb3), [RTPCValue\_Last](namespace_a_k_1_1_sound_engine_1_1_query_a59744f5b2f507550a0484fb228934f54.html#a59744f5b2f507550a0484fb228934f54a4839056a31b89bbc88ede17664ad24ed)   } |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetRTPCValue](namespace_a_k_1_1_sound_engine_1_1_query_a1149dfe866412f53644e3236639ba951.html#a1149dfe866412f53644e3236639ba951) ([AkRtpcID](_ak_typedefs_8h_a77a3b6fec7d9181ef8e5bae2b37b80d0.html#a77a3b6fec7d9181ef8e5bae2b37b80d0) in\_rtpcID, [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_gameObjectID, [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID, [AkRtpcValue](_ak_typedefs_8h_a86459d5c3b5e6055cc885b833661f140.html#a86459d5c3b5e6055cc885b833661f140) &out\_rValue, [RTPCValue\_type](namespace_a_k_1_1_sound_engine_1_1_query_a59744f5b2f507550a0484fb228934f54.html#a59744f5b2f507550a0484fb228934f54) &io\_rValueType) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetRTPCValue](namespace_a_k_1_1_sound_engine_1_1_query_a9c6fcd3a81e3d1dd4a05aa22658533f5.html#a9c6fcd3a81e3d1dd4a05aa22658533f5) (const char \*in\_pszRtpcName, [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_gameObjectID, [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID, [AkRtpcValue](_ak_typedefs_8h_a86459d5c3b5e6055cc885b833661f140.html#a86459d5c3b5e6055cc885b833661f140) &out\_rValue, [RTPCValue\_type](namespace_a_k_1_1_sound_engine_1_1_query_a59744f5b2f507550a0484fb228934f54.html#a59744f5b2f507550a0484fb228934f54) &io\_rValueType) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetSwitch](namespace_a_k_1_1_sound_engine_1_1_query_a936ecebe49d276b0f05f0c6cb2ee7369.html#a936ecebe49d276b0f05f0c6cb2ee7369) ([AkSwitchGroupID](_ak_typedefs_8h_a2b8749ca2320f1ee1c4ebe6b7cf1db26.html#a2b8749ca2320f1ee1c4ebe6b7cf1db26) in\_switchGroup, [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_gameObjectID, [AkSwitchStateID](_ak_typedefs_8h_abcf085b986c625421604d4fc0acd7f1e.html#abcf085b986c625421604d4fc0acd7f1e) &out\_rSwitchState) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetSwitch](namespace_a_k_1_1_sound_engine_1_1_query_a12e2dc05676b8d5155fe1e153f4c1097.html#a12e2dc05676b8d5155fe1e153f4c1097) (const char \*in\_pstrSwitchGroupName, [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_GameObj, [AkSwitchStateID](_ak_typedefs_8h_abcf085b986c625421604d4fc0acd7f1e.html#abcf085b986c625421604d4fc0acd7f1e) &out\_rSwitchState) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetState](namespace_a_k_1_1_sound_engine_1_1_query_acf1d46072687826dbc1ff2116a4234c8.html#acf1d46072687826dbc1ff2116a4234c8) ([AkStateGroupID](_ak_typedefs_8h_a5b95307c78b6becd02f3cdc4b3968c57.html#a5b95307c78b6becd02f3cdc4b3968c57) in\_stateGroup, [AkStateID](_ak_typedefs_8h_a70ba3fe9852a8785242bf70622c43c34.html#a70ba3fe9852a8785242bf70622c43c34) &out\_rState) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetState](namespace_a_k_1_1_sound_engine_1_1_query_aaae9fb933d31dd078dd0c0a44cd23c36.html#aaae9fb933d31dd078dd0c0a44cd23c36) (const char \*in\_pstrStateGroupName, [AkStateID](_ak_typedefs_8h_a70ba3fe9852a8785242bf70622c43c34.html#a70ba3fe9852a8785242bf70622c43c34) &out\_rState) |
|  | |

|  |  |
| --- | --- |
| Environments | |
| typedef [AkArray](class_ak_array.html)< [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560), [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) > | [AkGameObjectsList](namespace_a_k_1_1_sound_engine_1_1_query_ab4718e5e7bee8b286818de6cffa2d1b3.html#ab4718e5e7bee8b286818de6cffa2d1b3) |
|  | |
| typedef [AkArray](class_ak_array.html)< [GameObjDst](struct_a_k_1_1_sound_engine_1_1_query_1_1_game_obj_dst.html), const [GameObjDst](struct_a_k_1_1_sound_engine_1_1_query_1_1_game_obj_dst.html) & > | [AkRadiusList](namespace_a_k_1_1_sound_engine_1_1_query_aa14caa1a935b5a7868e4ae0c994ef3a3.html#aa14caa1a935b5a7868e4ae0c994ef3a3) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetGameObjectAuxSendValues](namespace_a_k_1_1_sound_engine_1_1_query_a4e9c405d1759b2a3546460cfd84e3fae.html#a4e9c405d1759b2a3546460cfd84e3fae) ([AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_gameObjectID, [AkAuxSendValue](struct_ak_aux_send_value.html) \*out\_paAuxSendValues, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &io\_ruNumSendValues) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetGameObjectDryLevelValue](namespace_a_k_1_1_sound_engine_1_1_query_ae4ade41e74de2cafd00b62a41551ecf8.html#ae4ade41e74de2cafd00b62a41551ecf8) ([AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_EmitterID, [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_ListenerID, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) &out\_rfControlValue) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetObjectObstructionAndOcclusion](namespace_a_k_1_1_sound_engine_1_1_query_a4ab61d81c26dbfb4b277d175866114b8.html#a4ab61d81c26dbfb4b277d175866114b8) ([AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_EmitterID, [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_ListenerID, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) &out\_rfObstructionLevel, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) &out\_rfOcclusionLevel) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [QueryAudioObjectIDs](namespace_a_k_1_1_sound_engine_1_1_query_ad760c9a7f1596231d185d8ee931231f4.html#ad760c9a7f1596231d185d8ee931231f4) ([AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_eventID, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &io\_ruNumItems, [AkObjectInfo](struct_ak_object_info.html) \*out\_aObjectInfos) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [QueryAudioObjectIDs](namespace_a_k_1_1_sound_engine_1_1_query_a09fd71a799d732ffe45c7c3c013f2ae2.html#a09fd71a799d732ffe45c7c3c013f2ae2) (const char \*in\_pszEventName, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &io\_ruNumItems, [AkObjectInfo](struct_ak_object_info.html) \*out\_aObjectInfos) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetPositioningInfo](namespace_a_k_1_1_sound_engine_1_1_query_a58bb2a69318ddee9d168c0e57fd2dac4.html#a58bb2a69318ddee9d168c0e57fd2dac4) ([AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_ObjectID, [AkPositioningInfo](struct_ak_positioning_info.html) &out\_rPositioningInfo) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetActiveGameObjects](namespace_a_k_1_1_sound_engine_1_1_query_a5e88783ff67bfcea2a765cd3adc5e3bd.html#a5e88783ff67bfcea2a765cd3adc5e3bd) ([AkGameObjectsList](namespace_a_k_1_1_sound_engine_1_1_query_ab4718e5e7bee8b286818de6cffa2d1b3.html#ab4718e5e7bee8b286818de6cffa2d1b3) &io\_GameObjectList) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) bool | [GetIsGameObjectActive](namespace_a_k_1_1_sound_engine_1_1_query_aa04fff7b61cd2cd4df6c0cf0af00e58d.html#aa04fff7b61cd2cd4df6c0cf0af00e58d) ([AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_GameObjId) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetMaxRadius](namespace_a_k_1_1_sound_engine_1_1_query_a8cc7c4191a91375d58d6a2de118aece4.html#a8cc7c4191a91375d58d6a2de118aece4) ([AkRadiusList](namespace_a_k_1_1_sound_engine_1_1_query_aa14caa1a935b5a7868e4ae0c994ef3a3.html#aa14caa1a935b5a7868e4ae0c994ef3a3) &io\_RadiusList) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [GetMaxRadius](namespace_a_k_1_1_sound_engine_1_1_query_a257016dc8f3521df049859cc4d27aeec.html#a257016dc8f3521df049859cc4d27aeec) ([AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_GameObjId) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [GetEventIDFromPlayingID](namespace_a_k_1_1_sound_engine_1_1_query_a1c53c91b9b54140ac48977ee25ae6387.html#a1c53c91b9b54140ac48977ee25ae6387) ([AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [GetGameObjectFromPlayingID](namespace_a_k_1_1_sound_engine_1_1_query_aef86db60a23116c39e1728b1e633e379.html#aef86db60a23116c39e1728b1e633e379) ([AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetPlayingIDsFromGameObject](namespace_a_k_1_1_sound_engine_1_1_query_a8263cb018517fadf2220ca00d88f907f.html#a8263cb018517fadf2220ca00d88f907f) ([AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_GameObjId, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &io\_ruNumIDs, [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) \*out\_aPlayingIDs) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetCustomPropertyValue](namespace_a_k_1_1_sound_engine_1_1_query_abc7d9c5bb2c0b01c80d369c6ee479510.html#abc7d9c5bb2c0b01c80d369c6ee479510) ([AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_ObjectID, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uPropID, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) &out\_iValue) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetCustomPropertyValue](namespace_a_k_1_1_sound_engine_1_1_query_afb39b6453d12956a0cccf19ddb1f16ab.html#afb39b6453d12956a0cccf19ddb1f16ab) ([AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_ObjectID, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uPropID, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) &out\_fValue) |
|  | |

## 详细描述

[Query](namespace_a_k_1_1_sound_engine_1_1_query.html) namespace

备注
:   The functions in this namespace are thread-safe, unless stated otherwise. We recommend that you use these functions in development builds only, because they can cause CPU spikes.

|  |  |
| --- | --- |
|  | **警告:** The functions in this namespace might stall for several milliseconds before returning because they cannot execute while the main sound engine tick is running. They should therefore not be called from any game-critical thread, such as the main game loop. However, if the function definition states that it does not require the main audio lock, no delay should occur.  There might be a significant delay between a Sound Engine call, such as PostEvent, and the information being returned in a [Query](namespace_a_k_1_1_sound_engine_1_1_query.html), such as GetIsGameObjectActive. |