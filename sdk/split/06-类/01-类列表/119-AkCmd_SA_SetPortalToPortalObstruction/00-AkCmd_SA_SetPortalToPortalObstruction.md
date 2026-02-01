# AkCmd_SA_SetPortalToPortalObstruction

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_portal_to_portal_obstruction-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetPortalToPortalObstruction结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkPortalID](_ak_spatial_audio_types_8h_a8e9c611850968a9aed0bc88bc71cd992.html#a8e9c611850968a9aed0bc88bc71cd992) | [portalID0](struct_ak_cmd___s_a___set_portal_to_portal_obstruction_a931b5e9a83d734f12a6d85cbde8a361b.html#a931b5e9a83d734f12a6d85cbde8a361b) |
|  | Portal ID [更多...](struct_ak_cmd___s_a___set_portal_to_portal_obstruction_a931b5e9a83d734f12a6d85cbde8a361b.html#a931b5e9a83d734f12a6d85cbde8a361b) |
|  | |
| [AkPortalID](_ak_spatial_audio_types_8h_a8e9c611850968a9aed0bc88bc71cd992.html#a8e9c611850968a9aed0bc88bc71cd992) | [portalID1](struct_ak_cmd___s_a___set_portal_to_portal_obstruction_ad44902497911abf7fd680172cb8225c4.html#ad44902497911abf7fd680172cb8225c4) |
|  | Portal ID [更多...](struct_ak_cmd___s_a___set_portal_to_portal_obstruction_ad44902497911abf7fd680172cb8225c4.html#ad44902497911abf7fd680172cb8225c4) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [obstruction](struct_ak_cmd___s_a___set_portal_to_portal_obstruction_ace49b27bc3e319f618c40955a6fcdfc8.html#ace49b27bc3e319f618c40955a6fcdfc8) |
|  | Obstruction value. Valid range 0.f-1.f [更多...](struct_ak_cmd___s_a___set_portal_to_portal_obstruction_ace49b27bc3e319f618c40955a6fcdfc8.html#ace49b27bc3e319f618c40955a6fcdfc8) |
|  | |

## 详细描述

Set the obstruction value of the path between two portals that has been created by Spatial Audio. The obstruction value is applied on one of the path segments of the sound between the emitter and the listener. Diffraction must be enabled on the sound for a diffraction path to be created. Also, there should not be any portals between the two provided ID parameters. The obstruction value is used to simulate objects between the portals that are obstructing the sound. Send an obstruction value of 0 to ensure the value is removed from the internal data structure.

This command can fail for the following reasons:

- AK\_InvalidParameter: `portalID0` or `portalID1` are not valid IDs, or obstruction is not within the accepted range.

参见
:   - [AkCommand\_SA\_SetPortalToPortalObstruction](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda4aae41be47961288e58ebc69544f2c8a)
    - [AkCmd\_SA\_SetPortalObstructionAndOcclusion](struct_ak_cmd___s_a___set_portal_obstruction_and_occlusion.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1643](_ak_command_types_8h_source.html#l01643) 行定义.