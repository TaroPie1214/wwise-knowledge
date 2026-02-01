# AkDynamicDialogue.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[命名空间](#namespaces) |
[类型定义](#typedef-members) |
[函数](#func-members)

AkDynamicDialogue.h 文件参考

`#include <AK/SoundEngine/Common/AkSoundEngine.h>`

[浏览源代码.](_ak_dynamic_dialogue_8h_source.html)

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
|  | [AK::SoundEngine](namespace_a_k_1_1_sound_engine.html) |
|  | |
|  | [AK::SoundEngine::DynamicDialogue](namespace_a_k_1_1_sound_engine_1_1_dynamic_dialogue.html) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef bool(\* | [AkCandidateCallbackFunc](_ak_dynamic_dialogue_8h_a6f9f698cc879b61231ecd5e2431b2f81.html#a6f9f698cc879b61231ecd5e2431b2f81)) ([AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_idEvent, [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_idCandidate, void \*in\_cookie) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [AK::SoundEngine::DynamicDialogue::ResolveDialogueEvent](namespace_a_k_1_1_sound_engine_1_1_dynamic_dialogue_a18385d0523eb14ff57bd4ea9f18c08f6.html#a18385d0523eb14ff57bd4ea9f18c08f6) ([AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_eventID, [AkArgumentValueID](_ak_typedefs_8h_a7265e56561ed1bb5b505dd6a13843018.html#a7265e56561ed1bb5b505dd6a13843018) \*in\_aArgumentValues, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumArguments, [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_idSequence=[AK\_INVALID\_PLAYING\_ID](_ak_constants_8h_a5141397d9cce5d9656f58931596d8360.html#a5141397d9cce5d9656f58931596d8360), [AkCandidateCallbackFunc](_ak_dynamic_dialogue_8h_a6f9f698cc879b61231ecd5e2431b2f81.html#a6f9f698cc879b61231ecd5e2431b2f81) in\_candidateCallbackFunc=NULL, void \*in\_pCookie=NULL) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [AK::SoundEngine::DynamicDialogue::ResolveDialogueEvent](namespace_a_k_1_1_sound_engine_1_1_dynamic_dialogue_a40f50c537c8b24244ce1cbe8b68bacf3.html#a40f50c537c8b24244ce1cbe8b68bacf3) (const char \*in\_pszEventName, const char \*\*in\_aArgumentValueNames, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumArguments, [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_idSequence=[AK\_INVALID\_PLAYING\_ID](_ak_constants_8h_a5141397d9cce5d9656f58931596d8360.html#a5141397d9cce5d9656f58931596d8360), [AkCandidateCallbackFunc](_ak_dynamic_dialogue_8h_a6f9f698cc879b61231ecd5e2431b2f81.html#a6f9f698cc879b61231ecd5e2431b2f81) in\_candidateCallbackFunc=NULL, void \*in\_pCookie=NULL) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AK::SoundEngine::DynamicDialogue::GetDialogueEventCustomPropertyValue](namespace_a_k_1_1_sound_engine_1_1_dynamic_dialogue_a57f1aefcc5f2092dc7ef750fe82d811c.html#a57f1aefcc5f2092dc7ef750fe82d811c) ([AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_eventID, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uPropID, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) &out\_iValue) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AK::SoundEngine::DynamicDialogue::GetDialogueEventCustomPropertyValue](namespace_a_k_1_1_sound_engine_1_1_dynamic_dialogue_a27521672e6963afa3537cf1dd99f8d46.html#a27521672e6963afa3537cf1dd99f8d46) ([AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_eventID, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uPropID, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) &out\_fValue) |
|  | |