# AkCmd_SA_SetPortal

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_portal-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetPortal结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkPortalID](_ak_spatial_audio_types_8h_a8e9c611850968a9aed0bc88bc71cd992.html#a8e9c611850968a9aed0bc88bc71cd992) | [portalID](struct_ak_cmd___s_a___set_portal_afac4103defe6f73e251524fec43ab7ba.html#afac4103defe6f73e251524fec43ab7ba) |
|  | Unique portal ID, chosen by the client. [更多...](struct_ak_cmd___s_a___set_portal_afac4103defe6f73e251524fec43ab7ba.html#afac4103defe6f73e251524fec43ab7ba) |
|  | |
| struct [AkPortalParams](struct_ak_portal_params.html) | [params](struct_ak_cmd___s_a___set_portal_a82272669d4394126346d7f4bf69b405b.html#a82272669d4394126346d7f4bf69b405b) |
|  | Parameter for the portal. [更多...](struct_ak_cmd___s_a___set_portal_a82272669d4394126346d7f4bf69b405b.html#a82272669d4394126346d7f4bf69b405b) |
|  | |

## 详细描述

Add or update an acoustic portal. A portal is an opening that connects two or more rooms to simulate the transmission of reverberated (indirect) sound between the rooms. This function may be called multiple times with the same ID to update the parameters of the portal. The ID (`portalID`) must be chosen in the same manner as `AkGameObjectID's`, as they are in the same ID-space. The spatial audio lib manages the registration/unregistration of internal game objects for portals that use these IDs, and therefore must not collide.

Optionally, you can associate a name to the portal for profiling purposes. Call AK\_CommandBuffer\_AddString after adding the command to attach a name to the portal:

```
auto cmd = (AkCmd_SA_SetPortal*)AK_CommandBuffer_Add(buffer, AkCommand_SA_SetPortal);
// Fill command...
AK_CommandBuffer_AddString(buffer, "Portal 1");
```

This command can fail for the following reasons:

- AK\_InvalidParameter: `portalID` or some portal parameters are not valid.
- AK\_InsufficientMemory: Not enough memory to complete the operation.

参见
:   - [AkCommand\_SA\_SetPortal](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaab60efabdb8c16ad7c30c9c1bd8ee6cf)
    - [AkPortalID](_ak_spatial_audio_types_8h_a8e9c611850968a9aed0bc88bc71cd992.html#a8e9c611850968a9aed0bc88bc71cd992)
    - [AkPortalParams](struct_ak_portal_params.html)
    - [AkCmd\_SA\_RemovePortal](struct_ak_cmd___s_a___remove_portal.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1570](_ak_command_types_8h_source.html#l01570) 行定义.