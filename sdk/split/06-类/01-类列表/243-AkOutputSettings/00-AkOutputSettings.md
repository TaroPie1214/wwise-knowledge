# AkOutputSettings

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_output_settings-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkOutputSettings结构体 参考

Platform-independent initialization settings of output devices.
[更多...](struct_ak_output_settings.html#details)

`#include <AkSoundEngineTypes.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkOutputSettings](struct_ak_output_settings_a057960789c35740f5ab7a653d92fc6c0.html#a057960789c35740f5ab7a653d92fc6c0) () |
|  | |
|  | [AkOutputSettings](struct_ak_output_settings_a62fe5204e9347724db24cc64399fdb48.html#a62fe5204e9347724db24cc64399fdb48) (const char \*in\_szDeviceShareSet, [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_idDevice=[AK\_INVALID\_UNIQUE\_ID](_ak_constants_8h_aa512c62662d05d5b50dd08792ed254ec.html#aa512c62662d05d5b50dd08792ed254ec), [AkChannelConfig](struct_ak_channel_config.html) in\_channelConfig=[AkChannelConfig](struct_ak_channel_config.html)(), [AkPanningRule](_ak_enums_8h_a6a7a16f5e74370707bb7bff7fb29a112.html#a6a7a16f5e74370707bb7bff7fb29a112) in\_ePanning=[AkPanningRule\_Speakers](_ak_enums_8h_a6a7a16f5e74370707bb7bff7fb29a112.html#a6a7a16f5e74370707bb7bff7fb29a112a136f30c9cc3bc0be7afbe6223012131b)) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [audioDeviceShareset](struct_ak_output_settings_af1ff3ac68f3fa137c847144117d01535.html#af1ff3ac68f3fa137c847144117d01535) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [idDevice](struct_ak_output_settings_a0e145d97af362b7f3267b64ca0e38054.html#a0e145d97af362b7f3267b64ca0e38054) |
|  | |
| enum [AkPanningRule](_ak_enums_8h_a6a7a16f5e74370707bb7bff7fb29a112.html#a6a7a16f5e74370707bb7bff7fb29a112) | [ePanningRule](struct_ak_output_settings_aaf1191276e3ac40828eeefb1db8767f7.html#aaf1191276e3ac40828eeefb1db8767f7) |
|  | |
| struct [AkChannelConfig](struct_ak_channel_config.html) | [channelConfig](struct_ak_output_settings_a5b546b6116a91f422fc0f61615159c06.html#a5b546b6116a91f422fc0f61615159c06) |
|  | |

## 详细描述

Platform-independent initialization settings of output devices.

在文件 [AkSoundEngineTypes.h](_ak_sound_engine_types_8h_source.html) 第 [218](_ak_sound_engine_types_8h_source.html#l00218) 行定义.