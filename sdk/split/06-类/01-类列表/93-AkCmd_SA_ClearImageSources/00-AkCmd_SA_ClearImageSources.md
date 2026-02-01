# AkCmd_SA_ClearImageSources

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___clear_image_sources-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_ClearImageSources结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [auxBusID](struct_ak_cmd___s_a___clear_image_sources_a67eeff163e34d7d6e51fd723571d8ceb.html#a67eeff163e34d7d6e51fd723571d8ceb) |
|  | Aux bus that was passed to SetImageSource, or AK\_INVALID\_AUX\_ID to match all aux busses. [更多...](struct_ak_cmd___s_a___clear_image_sources_a67eeff163e34d7d6e51fd723571d8ceb.html#a67eeff163e34d7d6e51fd723571d8ceb) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___s_a___clear_image_sources_a9d247c9fede4384d2f0055674bc4abcc.html#a9d247c9fede4384d2f0055674bc4abcc) |
|  | Game object ID that was passed to SetImageSource, or AK\_INVALID\_GAME\_OBJECT to match all game objects. [更多...](struct_ak_cmd___s_a___clear_image_sources_a9d247c9fede4384d2f0055674bc4abcc.html#a9d247c9fede4384d2f0055674bc4abcc) |
|  | |

## 详细描述

Remove all image sources matching `auxBusID` and `gameObjectID` that were previously added via `SetImageSource`. Both `auxBusID` and `gameObjectID` can be treated as wild cards matching all aux buses and/or all game object, by passing `AK_INVALID_AUX_ID` and/or `AK_INVALID_GAME_OBJECT`, respectively.

This command can fail for the following reasons:

- AK\_IDNotFound: `gameObjectID` was specified but is not registered.

参见
:   - [AkCommand\_SA\_ClearImageSources](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdab9c9e823ee2075c3e38467cb782563b6 "See AkCmd_SA_ClearImageSources")
    - [AkCmd\_SA\_SetImageSource](struct_ak_cmd___s_a___set_image_source.html)
    - [AkCmd\_SA\_RemoveImageSource](struct_ak_cmd___s_a___remove_image_source.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1427](_ak_command_types_8h_source.html#l01427) 行定义.