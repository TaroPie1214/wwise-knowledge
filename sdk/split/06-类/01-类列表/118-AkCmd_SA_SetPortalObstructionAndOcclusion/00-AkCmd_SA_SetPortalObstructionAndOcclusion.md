# AkCmd_SA_SetPortalObstructionAndOcclusion

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_portal_obstruction_and_occlusion-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetPortalObstructionAndOcclusion结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkPortalID](_ak_spatial_audio_types_8h_a8e9c611850968a9aed0bc88bc71cd992.html#a8e9c611850968a9aed0bc88bc71cd992) | [portalID](struct_ak_cmd___s_a___set_portal_obstruction_and_occlusion_abb54e21225dfe4737fb752fd3443856b.html#abb54e21225dfe4737fb752fd3443856b) |
|  | Portal ID. [更多...](struct_ak_cmd___s_a___set_portal_obstruction_and_occlusion_abb54e21225dfe4737fb752fd3443856b.html#abb54e21225dfe4737fb752fd3443856b) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [obstruction](struct_ak_cmd___s_a___set_portal_obstruction_and_occlusion_a8551c621d020c951df48c8aad0a2cd04.html#a8551c621d020c951df48c8aad0a2cd04) |
|  | Obstruction value. Valid range 0.f-1.f [更多...](struct_ak_cmd___s_a___set_portal_obstruction_and_occlusion_a8551c621d020c951df48c8aad0a2cd04.html#a8551c621d020c951df48c8aad0a2cd04) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [occlusion](struct_ak_cmd___s_a___set_portal_obstruction_and_occlusion_af70a5fead6ecd30b20b06a6a7b7449c1.html#af70a5fead6ecd30b20b06a6a7b7449c1) |
|  | Occlusion value. Valid range 0.f-1.f [更多...](struct_ak_cmd___s_a___set_portal_obstruction_and_occlusion_af70a5fead6ecd30b20b06a6a7b7449c1.html#af70a5fead6ecd30b20b06a6a7b7449c1) |
|  | |
| bool | [transition](struct_ak_cmd___s_a___set_portal_obstruction_and_occlusion_ad3182705238e513070847a7b468a42ae.html#ad3182705238e513070847a7b468a42ae) |
|  | Transition obstruction and occlusion through portals. Default false [更多...](struct_ak_cmd___s_a___set_portal_obstruction_and_occlusion_ad3182705238e513070847a7b468a42ae.html#ad3182705238e513070847a7b468a42ae) |
|  | |

## 详细描述

Set the obstruction and occlusion value for a portal that has been registered with Spatial Audio. Portal obstruction simulates objects that block the direct sound path between the portal and the listener, but allows indirect sound to pass around the obstacle. For example, use portal obstruction when a piece of furniture blocks the line of sight of the portal opening. Portal obstruction is applied to the connection between the emitter and the listener, and only affects the dry signal path. Portal occlusion simulates a complete blockage of both the direct and indirect sound through a portal. For example, use portal occlusion for opening or closing a door or window. Portal occlusion is applied to the connection between the emitter and the first room in the chain, as well as the connection between the emitter and listener. Portal occlusion affects both the dry and wet (reverberant) signal paths. If you are using built-in game parameters to drive RTPCs, the obstruction and occlusion values set here do not affect the RTPC values. This behavior is intentional and occurs because RTPCs only provide one value per game object, but a single game object can have multiple paths through different Portals, each with different obstruction and occlusion values. To apply detailed obstruction to specific sound paths but not others, use `AkCmd_SA_SetGameObjectToPortalObstruction` and `AkCmd_SA_SetPortalToPortalObstruction`. To apply occlusion and obstruction to the direct line of sight between the emitter and listener use `AkCmd_SetObjectObstructionAndOcclusion`.

This command can fail for the following reasons:

- AK\_InvalidParameter: `portalID` is not valid, or `obstruction` / `occlusion` values are out of range.
- AK\_IDNotFound: `portalID` is not a registered portal.

参见
:   - [AkCommand\_SA\_SetPortalObstructionAndOcclusion](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda41645e1bc17a24982eb5b4a5bf3e29ec)
    - [AkCmd\_SA\_SetGameObjectToPortalObstruction](struct_ak_cmd___s_a___set_game_object_to_portal_obstruction.html)
    - [AkCmd\_SA\_SetPortalToPortalObstruction](struct_ak_cmd___s_a___set_portal_to_portal_obstruction.html)
    - [AkCmd\_SetObjectObstructionAndOcclusion](struct_ak_cmd___set_object_obstruction_and_occlusion.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1601](_ak_command_types_8h_source.html#l01601) 行定义.