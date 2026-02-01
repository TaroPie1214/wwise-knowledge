# DynamicSequence

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [SoundEngine](namespace_a_k_1_1_sound_engine.html)
- [DynamicSequence](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence.html)

[类](#nested-classes) |
[类型定义](#typedef-members) |
[函数](#func-members) |
[变量](#var-members)

AK::SoundEngine::DynamicSequence 命名空间参考

|  |  |
| --- | --- |
| 类 | |
| class | [Playlist](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist.html) |
|  | |
| class | [PlaylistItem](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item.html) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [DynamicSequenceType](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_a8a2d2e9917fc300d080436c871b03b51.html#a8a2d2e9917fc300d080436c871b03b51) = ::[AkDynamicSequenceType](_ak_enums_8h_ab4eb43aa36ac35ebfbb93d22d1667d7b.html#ab4eb43aa36ac35ebfbb93d22d1667d7b) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) | [Open](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_ab6daddd96e109dc7669889733ce4f2cc.html#ab6daddd96e109dc7669889733ce4f2cc) ([AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_gameObjectID, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uFlags=0, [AkCallbackFunc](_ak_callback_types_8h_af644072775b1cdd813e2d32792a22005.html#af644072775b1cdd813e2d32792a22005) in\_pfnCallback=NULL, void \*in\_pCookie=NULL, [AkDynamicSequenceType](_ak_enums_8h_ab4eb43aa36ac35ebfbb93d22d1667d7b.html#ab4eb43aa36ac35ebfbb93d22d1667d7b) in\_eDynamicSequenceType=[AkDynamicSequenceType\_SampleAccurate](_ak_enums_8h_ab4eb43aa36ac35ebfbb93d22d1667d7b.html#ab4eb43aa36ac35ebfbb93d22d1667d7ba479a583eefb6b793b7935694be36c574)) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Close](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_ab204d963f6b81abc102a6d6b8272b591.html#ab204d963f6b81abc102a6d6b8272b591) ([AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Play](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_ae2ac4c400d0145c6c25e050d752064bd.html#ae2ac4c400d0145c6c25e050d752064bd) ([AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID, [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) in\_uTransitionDuration=0, [AkCurveInterpolation](_ak_enums_8h_a77872044bca52a4d20324739154f2399.html#a77872044bca52a4d20324739154f2399) in\_eFadeCurve=[AkCurveInterpolation\_Linear](_ak_enums_8h_a77872044bca52a4d20324739154f2399.html#a77872044bca52a4d20324739154f2399a4bc8df1cfffac8b5239808faf94a112b)) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Pause](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_afd87604f8cea6b836be5b657f74723f3.html#afd87604f8cea6b836be5b657f74723f3) ([AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID, [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) in\_uTransitionDuration=0, [AkCurveInterpolation](_ak_enums_8h_a77872044bca52a4d20324739154f2399.html#a77872044bca52a4d20324739154f2399) in\_eFadeCurve=[AkCurveInterpolation\_Linear](_ak_enums_8h_a77872044bca52a4d20324739154f2399.html#a77872044bca52a4d20324739154f2399a4bc8df1cfffac8b5239808faf94a112b)) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Resume](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_aa34180ccd604c29cd9222de08a449b4a.html#aa34180ccd604c29cd9222de08a449b4a) ([AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID, [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) in\_uTransitionDuration=0, [AkCurveInterpolation](_ak_enums_8h_a77872044bca52a4d20324739154f2399.html#a77872044bca52a4d20324739154f2399) in\_eFadeCurve=[AkCurveInterpolation\_Linear](_ak_enums_8h_a77872044bca52a4d20324739154f2399.html#a77872044bca52a4d20324739154f2399a4bc8df1cfffac8b5239808faf94a112b)) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Stop](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_a3153fbaab7c917914f2a60183523b1cc.html#a3153fbaab7c917914f2a60183523b1cc) ([AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID, [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) in\_uTransitionDuration=0, [AkCurveInterpolation](_ak_enums_8h_a77872044bca52a4d20324739154f2399.html#a77872044bca52a4d20324739154f2399) in\_eFadeCurve=[AkCurveInterpolation\_Linear](_ak_enums_8h_a77872044bca52a4d20324739154f2399.html#a77872044bca52a4d20324739154f2399a4bc8df1cfffac8b5239808faf94a112b)) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Break](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_af617483dfd98415dc7ea72e7e6b06bea.html#af617483dfd98415dc7ea72e7e6b06bea) ([AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Seek](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_a46c6c751e936d15f1c75434d3319395f.html#a46c6c751e936d15f1c75434d3319395f) ([AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID, [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) in\_iPosition, bool in\_bSeekToNearestMarker) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Seek](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_abd84bf191b179757783866af71579a04.html#abd84bf191b179757783866af71579a04) ([AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fPercent, bool in\_bSeekToNearestMarker) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetPauseTimes](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_aefe109a63354e0412208794d71ccd2cc.html#aefe109a63354e0412208794d71ccd2cc) ([AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &out\_uTime, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &out\_uDuration) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetPlayingItem](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_a4745e6aa6b7d71c503baa91c5bf70a80.html#a4745e6aa6b7d71c503baa91c5bf70a80) ([AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID, [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) &out\_audioNodeID, void \*&out\_pCustomInfo) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [Playlist](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist.html) \* | [LockPlaylist](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_af72d304486f19cc81d24c4488c6ea652.html#af72d304486f19cc81d24c4488c6ea652) ([AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [UnlockPlaylist](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_aa7b7bbc2b6158423a0006682b44b40c5.html#aa7b7bbc2b6158423a0006682b44b40c5) ([AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_playingID) |
|  | |

|  |  |
| --- | --- |
| 变量 | |
| const [AkDynamicSequenceType](_ak_enums_8h_ab4eb43aa36ac35ebfbb93d22d1667d7b.html#ab4eb43aa36ac35ebfbb93d22d1667d7b) | [DynamicSequenceType\_SampleAccurate](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_a29abede8e9ee442173b39c996d864f61.html#a29abede8e9ee442173b39c996d864f61) = [AkDynamicSequenceType\_SampleAccurate](_ak_enums_8h_ab4eb43aa36ac35ebfbb93d22d1667d7b.html#ab4eb43aa36ac35ebfbb93d22d1667d7ba479a583eefb6b793b7935694be36c574) |
|  | |
| const [AkDynamicSequenceType](_ak_enums_8h_ab4eb43aa36ac35ebfbb93d22d1667d7b.html#ab4eb43aa36ac35ebfbb93d22d1667d7b) | [DynamicSequenceType\_NormalTransition](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_af70621dcdeb613a079c4bc3faa502c51.html#af70621dcdeb613a079c4bc3faa502c51) = [AkDynamicSequenceType\_NormalTransition](_ak_enums_8h_ab4eb43aa36ac35ebfbb93d22d1667d7b.html#ab4eb43aa36ac35ebfbb93d22d1667d7ba05d99bd1f34ee60c44e579f47868efd1) |
|  | |
| const [AkDynamicSequenceType](_ak_enums_8h_ab4eb43aa36ac35ebfbb93d22d1667d7b.html#ab4eb43aa36ac35ebfbb93d22d1667d7b) | [DynamicSequenceType\_Last](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_a9ded312e4655775006c59d8803c81ddd.html#a9ded312e4655775006c59d8803c81ddd) = [AkDynamicSequenceType\_Last](_ak_enums_8h_ab4eb43aa36ac35ebfbb93d22d1667d7b.html#ab4eb43aa36ac35ebfbb93d22d1667d7ba42d9e1324f1d94a5deab87eff1dafe06) |
|  | |

## 详细描述

Dynamic Sequence namespace. Use the Dynamic Sequence API to play and sequence Dialogue Events dynamically, according to a set of rules and conditions. For more information, see [集成 Dynamic Dialogue](integrating_elements_dynamicdialogue.html) and [Understanding the Dynamic Dialogue System](https://www.audiokinetic.com/library/edge/?source=Help&id=understanding_dynamic_dialogue_system).

备注
:   The functions in this namespace are thread-safe, unless stated otherwise.