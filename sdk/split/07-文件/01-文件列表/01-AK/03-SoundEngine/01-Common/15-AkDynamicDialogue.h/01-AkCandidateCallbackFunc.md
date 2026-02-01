# AkCandidateCallbackFunc

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)
- [AkDynamicDialogue.h](_ak_dynamic_dialogue_8h.html)

|  |  |  |  |
| --- | --- | --- | --- |
| |  | | --- | | [AkCandidateCallbackFunc](_ak_dynamic_dialogue_8h_a6f9f698cc879b61231ecd5e2431b2f81.html#a6f9f698cc879b61231ecd5e2431b2f81) | | [◆](#a6f9f698cc879b61231ecd5e2431b2f81)AkCandidateCallbackFunc |  | | --- | | typedef bool( \* AkCandidateCallbackFunc) ([AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_idEvent, [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_idCandidate, void \*in\_cookie) |  Callback prototype used with dialogue event resolution. This function is called for every candidate in a ResolveDialogueEvent execution.  返回  true to accept candidate, false to reject.  参见  - [AK::SoundEngine::DynamicDialogue::ResolveDialogueEvent()](namespace_a_k_1_1_sound_engine_1_1_dynamic_dialogue_a18385d0523eb14ff57bd4ea9f18c08f6.html#a18385d0523eb14ff57bd4ea9f18c08f6)  在文件 [AkDynamicDialogue.h](_ak_dynamic_dialogue_8h_source.html) 第 [37](_ak_dynamic_dialogue_8h_source.html#l00037) 行定义. |