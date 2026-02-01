# bEnabled

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkPortalParams](struct_ak_portal_params.html)

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AdjacentRoomBleed](struct_ak_portal_params_a8cca592e2a38f8719b6e5a03eddecb07.html#a8cca592e2a38f8719b6e5a03eddecb07) | | [AkPortalParams](struct_ak_portal_params_a86b5aeface9368b1358e6f06582434b5.html#a86b5aeface9368b1358e6f06582434b5) | | [BackRoom](struct_ak_portal_params_a7647cf1bc4a968287f853293903abc41.html#a7647cf1bc4a968287f853293903abc41) | | [bEnabled](struct_ak_portal_params_ae7b926f081a501061439f8db0de6efba.html#ae7b926f081a501061439f8db0de6efba) | | [Extent](struct_ak_portal_params_a74acf1db3eb64175a9368962bdb56ff6.html#a74acf1db3eb64175a9368962bdb56ff6) | | [FrontRoom](struct_ak_portal_params_a09821f2e2d23fcf23e217694ca12e633.html#a09821f2e2d23fcf23e217694ca12e633) | | [Transform](struct_ak_portal_params_ae76feb71ce65d4044d0de2cb4971ade8.html#ae76feb71ce65d4044d0de2cb4971ade8) | | [◆](#ae7b926f081a501061439f8db0de6efba)bEnabled |  | | --- | | bool AkPortalParams::bEnabled |  Whether or not the portal is active/enabled. For example, this parameter may be used to simulate open/closed doors. Portal diffraction is simulated when at least one portal exists and is active between an emitter and the listener. To simulate a door that opens or closes gradually, use `AK::SpatialAudio::SetPortalObstructionAndOcclusion` to apply occlusion to a portal, according to the door's opening amount.  参见  - [AK::SpatialAudio::SetPortalObstructionAndOcclusion](namespace_a_k_1_1_spatial_audio_a41b9dee6e3af84e5ce3075319e16740d.html#a41b9dee6e3af84e5ce3075319e16740d)  在文件 [AkSpatialAudioTypes.h](_ak_spatial_audio_types_8h_source.html) 第 [633](_ak_spatial_audio_types_8h_source.html#l00633) 行定义. |