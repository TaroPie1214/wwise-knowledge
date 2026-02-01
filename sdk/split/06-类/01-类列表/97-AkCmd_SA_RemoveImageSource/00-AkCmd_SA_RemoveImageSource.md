# AkCmd_SA_RemoveImageSource

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___remove_image_source-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_RemoveImageSource结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [imageSourceID](struct_ak_cmd___s_a___remove_image_source_a4a02b8c706d89d8e3205e17d0fa31894.html#a4a02b8c706d89d8e3205e17d0fa31894) |
|  | The ID of the image source to remove. [更多...](struct_ak_cmd___s_a___remove_image_source_a4a02b8c706d89d8e3205e17d0fa31894.html#a4a02b8c706d89d8e3205e17d0fa31894) |
|  | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [auxBusID](struct_ak_cmd___s_a___remove_image_source_a72ada8148a8be5af40088aa4c8b89749.html#a72ada8148a8be5af40088aa4c8b89749) |
|  | Aux bus that was passed to SetImageSource. [更多...](struct_ak_cmd___s_a___remove_image_source_a72ada8148a8be5af40088aa4c8b89749.html#a72ada8148a8be5af40088aa4c8b89749) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___s_a___remove_image_source_a3bd3409a44c3fa6dae965fa175e40e4f.html#a3bd3409a44c3fa6dae965fa175e40e4f) |
|  | Game object ID that was passed to SetImageSource. [更多...](struct_ak_cmd___s_a___remove_image_source_a3bd3409a44c3fa6dae965fa175e40e4f.html#a3bd3409a44c3fa6dae965fa175e40e4f) |
|  | |

## 详细描述

Remove an individual reflection image source that was previously added via `SetImageSource`.

This command can fail for the following reasons:

- AK\_InvalidParameter: `imageSourceID` is invalid
- AK\_IDNotFound: `gameObjectID` was specified but is not registered.

参见
:   - [AkCommand\_SA\_RemoveImageSource](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda86b00d30d5a55d227d41fbbe2cf536ca "See AkCmd_SA_RemoveImageSource")
    - [AkCmd\_SA\_SetImageSource](struct_ak_cmd___s_a___set_image_source.html)
    - [AkCmd\_SA\_ClearImageSources](struct_ak_cmd___s_a___clear_image_sources.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1410](_ak_command_types_8h_source.html#l01410) 行定义.