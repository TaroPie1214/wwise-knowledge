# AkCmd_SetSidechainMixConfig

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_sidechain_mix_config-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetSidechainMixConfig结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [sidechainMixID](struct_ak_cmd___set_sidechain_mix_config_a970ebf99dad62c8cf1cd21c96812300e.html#a970ebf99dad62c8cf1cd21c96812300e) |
|  | SidechainMix Short ID. [更多...](struct_ak_cmd___set_sidechain_mix_config_a970ebf99dad62c8cf1cd21c96812300e.html#a970ebf99dad62c8cf1cd21c96812300e) |
|  | |
| struct [AkChannelConfig](struct_ak_channel_config.html) | [channelConfig](struct_ak_cmd___set_sidechain_mix_config_a7923f17292f514cea8e584aef4933110.html#a7923f17292f514cea8e584aef4933110) |
|  | Desired channel configuration. An invalid configuration (from default constructor) means "as parent". [更多...](struct_ak_cmd___set_sidechain_mix_config_a7923f17292f514cea8e584aef4933110.html#a7923f17292f514cea8e584aef4933110) |
|  | |

## 详细描述

Forces channel configuration for the specified Sidechain Mix.

This command can fail for the following reasons:

- `AK_InvalidParameter` when `sidechainMixID` is an invalid ID.
- `AK_IDNotFound` when the SidechainMix ID is not loaded.

参见
:   - [AkCommand\_SetSidechainMixConfig](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda6e5975488e4da133ebe8d33dc57cba1f "See AkCmd_SetSidechainMixConfig")
    - [AK::SoundEngine::SetSidechainMixConfig](namespace_a_k_1_1_sound_engine_afd4347eabf3e6ef76ab641796d48b2ce.html#afd4347eabf3e6ef76ab641796d48b2ce)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1002](_ak_command_types_8h_source.html#l01002) 行定义.