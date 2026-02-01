# AkCmd_SA_SetMaxDiffractionPaths

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_max_diffraction_paths-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetMaxDiffractionPaths结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [maxDiffractionPaths](struct_ak_cmd___s_a___set_max_diffraction_paths_aa2a264a5a58a5b44b2052a6d3435e470.html#aa2a264a5a58a5b44b2052a6d3435e470) |
|  | Maximum number of reflection paths. Valid range [0..32] [更多...](struct_ak_cmd___s_a___set_max_diffraction_paths_aa2a264a5a58a5b44b2052a6d3435e470.html#aa2a264a5a58a5b44b2052a6d3435e470) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___s_a___set_max_diffraction_paths_a6fc9aad8d90f04cb63e0ea62a91be2b2.html#a6fc9aad8d90f04cb63e0ea62a91be2b2) |
|  | Game Object ID. Set `AK_INVALID_GAME_OBJECT` to affect all Game Objects, effectivly updating `AkSpatialAudioInitSettings::uMaxDiffractionPaths`. Pass a valid Game Object ID to override the init setting for a specific Game Object. [更多...](struct_ak_cmd___s_a___set_max_diffraction_paths_a6fc9aad8d90f04cb63e0ea62a91be2b2.html#a6fc9aad8d90f04cb63e0ea62a91be2b2) |
|  | |

## 详细描述

Set the maximum number of computed diffraction paths. Pass a valid Game Object ID to to `gameObjectID` to affect a specific game object and override the value set in `AkSpatialAudioInitSettings::uMaxDiffractionPaths`. Pass `AK_INVALID_GAME_OBJECT` to apply the same limit to all Game Objects (that have not previously been passed to `AkCmd_SA_SetMaxDiffractionPaths`), updating the value set for `AkSpatialAudioInitSettings::uMaxDiffractionPaths`.

This command can fail for the following reasons:

- AK\_InvalidParameter: `gameObjectID` is not valid or `maxDiffractionPaths` is not within the accepted range.
- AK\_IDNotFound: `gameObjectID` is specified but is not a registered game object.

参见
:   - [AkCommand\_SA\_SetMaxDiffractionPaths](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdae45c60d0299a7854e24161950a276165)
    - [AkSpatialAudioInitSettings::uMaxDiffractionPaths](struct_ak_spatial_audio_init_settings_a94f819cee9905b9745f9d628aedf7cf2.html#a94f819cee9905b9745f9d628aedf7cf2)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1900](_ak_command_types_8h_source.html#l01900) 行定义.