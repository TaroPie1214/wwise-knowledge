# Extent

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkPortalParams](struct_ak_portal_params.html)

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AdjacentRoomBleed](struct_ak_portal_params_a8cca592e2a38f8719b6e5a03eddecb07.html#a8cca592e2a38f8719b6e5a03eddecb07) | | [AkPortalParams](struct_ak_portal_params_a86b5aeface9368b1358e6f06582434b5.html#a86b5aeface9368b1358e6f06582434b5) | | [BackRoom](struct_ak_portal_params_a7647cf1bc4a968287f853293903abc41.html#a7647cf1bc4a968287f853293903abc41) | | [bEnabled](struct_ak_portal_params_ae7b926f081a501061439f8db0de6efba.html#ae7b926f081a501061439f8db0de6efba) | | [Extent](struct_ak_portal_params_a74acf1db3eb64175a9368962bdb56ff6.html#a74acf1db3eb64175a9368962bdb56ff6) | | [FrontRoom](struct_ak_portal_params_a09821f2e2d23fcf23e217694ca12e633.html#a09821f2e2d23fcf23e217694ca12e633) | | [Transform](struct_ak_portal_params_ae76feb71ce65d4044d0de2cb4971ade8.html#ae76feb71ce65d4044d0de2cb4971ade8) | | [◆](#a74acf1db3eb64175a9368962bdb56ff6)Extent |  | | --- | | struct [AkExtent](struct_ak_extent.html) AkPortalParams::Extent |  Portal extent. Defines the dimensions of the portal relative to its center; all components must be positive numbers. The shape described by these extents is used to "cut out" the opening shape of room geometry. Geometry that overlaps the portal extent is effectively ignored. The depth dimension is used to perform transitions between connected rooms by manipulating game-defined auxiliary sends. The depth dimension is also used to place game objects into rooms while they are inside the portals.  参见  - [AkExtent](struct_ak_extent.html)  在文件 [AkSpatialAudioTypes.h](_ak_spatial_audio_types_8h_source.html) 第 [608](_ak_spatial_audio_types_8h_source.html#l00608) 行定义. |