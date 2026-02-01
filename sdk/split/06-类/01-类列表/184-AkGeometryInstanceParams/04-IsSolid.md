# IsSolid

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkGeometryInstanceParams](struct_ak_geometry_instance_params.html)

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AkGeometryInstanceParams](struct_ak_geometry_instance_params_ab9453ca62f4d4271edf5057e03f5cca5.html#ab9453ca62f4d4271edf5057e03f5cca5) | | [BypassPortalSubtraction](struct_ak_geometry_instance_params_a7d6f9b8fd62c177af0df8d436da700f3.html#a7d6f9b8fd62c177af0df8d436da700f3) | | [GeometrySetID](struct_ak_geometry_instance_params_a8e7503216a7291f52c09825799cdce53.html#a8e7503216a7291f52c09825799cdce53) | | [IsSolid](struct_ak_geometry_instance_params_a05d132d8d90222fdb7a54c5b4c506fb5.html#a05d132d8d90222fdb7a54c5b4c506fb5) | | [PositionAndOrientation](struct_ak_geometry_instance_params_a3287a24b0ce9ff51320b80367d832b31.html#a3287a24b0ce9ff51320b80367d832b31) | | [Scale](struct_ak_geometry_instance_params_ace410bb740f89af9c10c0ecead3ecb27.html#ace410bb740f89af9c10c0ecead3ecb27) | | [UseForReflectionAndDiffraction](struct_ak_geometry_instance_params_a30ef95f856b020642d4a45d43c3df86d.html#a30ef95f856b020642d4a45d43c3df86d) | | [◆](#a05d132d8d90222fdb7a54c5b4c506fb5)IsSolid |  | | --- | | bool AkGeometryInstanceParams::IsSolid |  A solid geometry instance applies transmission loss once for each time a transmission path enters and exits its volume, using the max transmission loss between each hit surface. A non-solid geometry instance is one where each surface is infinitely thin, applying transmission loss at each surface. This option has no effect if the Transmission Operation is set to Max.  在文件 [AkSpatialAudioTypes.h](_ak_spatial_audio_types_8h_source.html) 第 [889](_ak_spatial_audio_types_8h_source.html#l00889) 行定义. |