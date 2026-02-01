# Transform

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkPortalParams](struct_ak_portal_params.html)

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AdjacentRoomBleed](struct_ak_portal_params_a8cca592e2a38f8719b6e5a03eddecb07.html#a8cca592e2a38f8719b6e5a03eddecb07) | | [AkPortalParams](struct_ak_portal_params_a86b5aeface9368b1358e6f06582434b5.html#a86b5aeface9368b1358e6f06582434b5) | | [BackRoom](struct_ak_portal_params_a7647cf1bc4a968287f853293903abc41.html#a7647cf1bc4a968287f853293903abc41) | | [bEnabled](struct_ak_portal_params_ae7b926f081a501061439f8db0de6efba.html#ae7b926f081a501061439f8db0de6efba) | | [Extent](struct_ak_portal_params_a74acf1db3eb64175a9368962bdb56ff6.html#a74acf1db3eb64175a9368962bdb56ff6) | | [FrontRoom](struct_ak_portal_params_a09821f2e2d23fcf23e217694ca12e633.html#a09821f2e2d23fcf23e217694ca12e633) | | [Transform](struct_ak_portal_params_ae76feb71ce65d4044d0de2cb4971ade8.html#ae76feb71ce65d4044d0de2cb4971ade8) | | [◆](#ae76feb71ce65d4044d0de2cb4971ade8)Transform |  | | --- | | struct [AkWorldTransform](struct_ak_world_transform.html) AkPortalParams::Transform |  Portal's position and orientation in the 3D world. Position vector is the center of the opening. OrientationFront vector must be unit-length and point along the normal of the portal, and must be orthogonal to Up. It defines the local positive-Z dimension (depth/transition axis) of the portal, used by Extent. OrientationTop vector must be unit-length and point along the top of the portal (tangent to the wall), must be orthogonal to Front. It defines the local positive-Y direction (height) of the portal, used by Extent.  在文件 [AkSpatialAudioTypes.h](_ak_spatial_audio_types_8h_source.html) 第 [608](_ak_spatial_audio_types_8h_source.html#l00608) 行定义. |