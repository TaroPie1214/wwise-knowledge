# AkCmd_SA_RemovePortal

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___remove_portal-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_RemovePortal结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkPortalID](_ak_spatial_audio_types_8h_a8e9c611850968a9aed0bc88bc71cd992.html#a8e9c611850968a9aed0bc88bc71cd992) | [portalID](struct_ak_cmd___s_a___remove_portal_afd6a9fce21d1497a3d5d0f43952833e8.html#afd6a9fce21d1497a3d5d0f43952833e8) |
|  | ID of portal to be removed, which was originally specified by [AkCmd\_SA\_SetPortal](struct_ak_cmd___s_a___set_portal.html). [更多...](struct_ak_cmd___s_a___remove_portal_afd6a9fce21d1497a3d5d0f43952833e8.html#afd6a9fce21d1497a3d5d0f43952833e8) |
|  | |

## 详细描述

Remove a portal.

This command can fail for the following reasons:

- AK\_InvalidParameter: `portalID` is not valid.
- AK\_IDNotFound: Provided `portalID` is not recognized as a registered portal ID.

参见
:   - [AkCommand\_SA\_RemovePortal](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdab24bbd80c36f3ad5acf6c3e4b49a2a92)
    - [AkPortalID](_ak_spatial_audio_types_8h_a8e9c611850968a9aed0bc88bc71cd992.html#a8e9c611850968a9aed0bc88bc71cd992)
    - [AK::SpatialAudio::SetPortal](namespace_a_k_1_1_spatial_audio_aeffa58bec3569a1bac5feac3e0c370d9.html#aeffa58bec3569a1bac5feac3e0c370d9)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1660](_ak_command_types_8h_source.html#l01660) 行定义.