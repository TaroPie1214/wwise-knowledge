# AkCmd_SA_SetGameObjectToPortalObstruction

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_game_object_to_portal_obstruction-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetGameObjectToPortalObstruction结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___s_a___set_game_object_to_portal_obstruction_a4d1068d1f1c589d7f70650d543db208d.html#a4d1068d1f1c589d7f70650d543db208d) |
|  | Game object ID [更多...](struct_ak_cmd___s_a___set_game_object_to_portal_obstruction_a4d1068d1f1c589d7f70650d543db208d.html#a4d1068d1f1c589d7f70650d543db208d) |
|  | |
| [AkPortalID](_ak_spatial_audio_types_8h_a8e9c611850968a9aed0bc88bc71cd992.html#a8e9c611850968a9aed0bc88bc71cd992) | [portalID](struct_ak_cmd___s_a___set_game_object_to_portal_obstruction_af761e0cffe4ae00d2fb2041ffca7fc3f.html#af761e0cffe4ae00d2fb2041ffca7fc3f) |
|  | Portal ID [更多...](struct_ak_cmd___s_a___set_game_object_to_portal_obstruction_af761e0cffe4ae00d2fb2041ffca7fc3f.html#af761e0cffe4ae00d2fb2041ffca7fc3f) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [obstruction](struct_ak_cmd___s_a___set_game_object_to_portal_obstruction_a302da28ed9cb9952429d514fab9dcbae.html#a302da28ed9cb9952429d514fab9dcbae) |
|  | Obstruction value. Valid range 0.f-1.f [更多...](struct_ak_cmd___s_a___set_game_object_to_portal_obstruction_a302da28ed9cb9952429d514fab9dcbae.html#a302da28ed9cb9952429d514fab9dcbae) |
|  | |

## 详细描述

Set the obstruction value of the path between a game object and a portal that has been created by Spatial Audio. The obstruction value is applied on one of the path segments of the sound between the emitter and the listener. Diffraction must be enabled on the sound for a diffraction path to be created. Also, there should not be any portals between the provided game object and portal ID parameters. The obstruction value is used to simulate objects between the portal and the game object that are obstructing the sound. Send an obstruction value of 0 to ensure the value is removed from the internal data structure.

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` or `portalID` are not valid IDs, or `obstruction` is not within the accepted range.
- AK\_IDNotFound: `gameObjectID` is not a registered game object or `portalID` is not a registered portal.

参见
:   - [AkCommand\_SA\_SetGameObjectToPortalObstruction](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda8e838c56d866f19ba7e78c605fb6dbc2)
    - [AkCmd\_SA\_SetPortalObstructionAndOcclusion](struct_ak_cmd___s_a___set_portal_obstruction_and_occlusion.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1623](_ak_command_types_8h_source.html#l01623) 行定义.