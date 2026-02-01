# AkCmd_SetEffect

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_effect-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetEffect结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [nodeID](struct_ak_cmd___set_effect_a454ed19e18b0d11a73d43184aa42a596.html#a454ed19e18b0d11a73d43184aa42a596) |
|  | ID of the bus, Container node, or output device. When `nodeType` is set to `AkNodeType_AudioDevice`, a value of 0 designates the main (default) output. [更多...](struct_ak_cmd___set_effect_a454ed19e18b0d11a73d43184aa42a596.html#a454ed19e18b0d11a73d43184aa42a596) |
|  | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [nodeType](struct_ak_cmd___set_effect_ac529dc4b5a53ab5505c335711df720b0.html#ac529dc4b5a53ab5505c335711df720b0) |
|  | Type of node that `nodeID` refers to. Must be a valid value from the `AkNodeType` enumeration. [更多...](struct_ak_cmd___set_effect_ac529dc4b5a53ab5505c335711df720b0.html#ac529dc4b5a53ab5505c335711df720b0) |
|  | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [fxIndex](struct_ak_cmd___set_effect_aae447998ec54d06ba0ceb663df10a643.html#aae447998ec54d06ba0ceb663df10a643) |
|  | Effect slot index (0-254) [更多...](struct_ak_cmd___set_effect_aae447998ec54d06ba0ceb663df10a643.html#aae447998ec54d06ba0ceb663df10a643) |
|  | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [fxSharesetID](struct_ak_cmd___set_effect_aaa55cd13388e3215180b5748d3222f3c.html#aaa55cd13388e3215180b5748d3222f3c) |
|  | ShareSet ID of the effect; pass AK\_INVALID\_UNIQUE\_ID to clear the Effect slot [更多...](struct_ak_cmd___set_effect_aaa55cd13388e3215180b5748d3222f3c.html#aaa55cd13388e3215180b5748d3222f3c) |
|  | |

## 详细描述

Sets an Effect ShareSet at the specified slot of a container, bus, or output device.

|  |  |
| --- | --- |
|  | **备注:** Replacing effects is preferably done through a Set Effect Event Action. |

This operation adds a reference on the audio node to an existing ShareSet.

To specify a bus, set `nodeType` to `AkNodeType_Bus`. The bus can be an Audio Bus or an Auxiliary Bus.

To specify an output device, set `nodeType` to `AkNodeType_AudioDevice`. The ID can refer to a specific ID returned by `AK::SoundEngine::GetOutputID` or 0 to designate the main (default) output device. In this case, only audio device effect sharesets are accepted.

When specifying any other container (e.g. Switch, Blend, Sound SFX, etc.) set `nodeType` to `AkNodeType_Default`.

|  |  |
| --- | --- |
|  | **备注:** This function has unspecified behavior when adding an Effect to a currently playing Bus which does not have any Effects, or removing the last Effect on a currently playing bus. |

|  |  |
| --- | --- |
|  | **备注:** This function will replace existing Effects on the node. If the target node is not at the top of the hierarchy and is in the Containers hierarchy, the option "Override Parent" in the Effect section in Wwise must be enabled for this node, otherwise the parent's Effect will still be the one in use and SetEffect will have no impact. |

This command can fail for the following reasons:

- `AK_InvalidParameter` when `nodeID` is an invalid ID, or when `fxIndex` or `nodeType` is out of range.
- `AK_IDNotFound` when either the Node ID or the Shareset ID are not present in the Init bank.
- `AK_RenderedFX` when the current effect in the slot is rendered at bank-generation time (rendered effects cannot be replaced).
- `AK_NotCompatible` when `nodeType` is `AkNodeType_AudioDevice` and the effect shareset is not an output device effect.
- `AK_InsufficientMemory` when there is not enough memory to complete the operation.

参见
:   - [AkCommand\_SetEffect](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaa0443ddf9f9de5f5ebac01ccc66ea1f8 "See AkCmd_SetEffect")
    - [AK::SoundEngine::SetActorMixerEffect](namespace_a_k_1_1_sound_engine_a00256bfd86c2bed14c626922fc4417b0.html#a00256bfd86c2bed14c626922fc4417b0)
    - [AK::SoundEngine::SetBusEffect](namespace_a_k_1_1_sound_engine_aabbeadd26d528e82003a0c143908d825.html#aabbeadd26d528e82003a0c143908d825)
    - [AK::SoundEngine::SetOutputDeviceEffect](namespace_a_k_1_1_sound_engine_ad455f291883c352a87b5b03da64549aa.html#ad455f291883c352a87b5b03da64549aa)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1046](_ak_command_types_8h_source.html#l01046) 行定义.