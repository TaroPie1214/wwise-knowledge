# AkCmd_SetState

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_state-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetState结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkStateGroupID](_ak_typedefs_8h_a5b95307c78b6becd02f3cdc4b3968c57.html#a5b95307c78b6becd02f3cdc4b3968c57) | [stateGroupID](struct_ak_cmd___set_state_a5ff1d97386e4c2321b15c5a15b4d8bbc.html#a5ff1d97386e4c2321b15c5a15b4d8bbc) |
|  | ID of the State Group [更多...](struct_ak_cmd___set_state_a5ff1d97386e4c2321b15c5a15b4d8bbc.html#a5ff1d97386e4c2321b15c5a15b4d8bbc) |
|  | |
| [AkStateID](_ak_typedefs_8h_a70ba3fe9852a8785242bf70622c43c34.html#a70ba3fe9852a8785242bf70622c43c34) | [stateID](struct_ak_cmd___set_state_a112c947926cb22f7d39f7688cd1e2318.html#a112c947926cb22f7d39f7688cd1e2318) |
|  | ID of the state [更多...](struct_ak_cmd___set_state_a112c947926cb22f7d39f7688cd1e2318.html#a112c947926cb22f7d39f7688cd1e2318) |
|  | |

## 详细描述

Sets the state of a State Group (by IDs).

This command can fail for the following reasons:

- AK\_InvalidParameter: `stateGroupID` is invalid.

参见
:   - [AkCommand\_SetState](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda6c765e2678326e0d679d2e96c3bc3d35 "See AkCmd_SetState")
    - [AK::SoundEngine::SetState](namespace_a_k_1_1_sound_engine_a68dc9be195962c671b82fbb354b68cc5.html#a68dc9be195962c671b82fbb354b68cc5)
    - [集成详情—— State（状态）](soundengine_states.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [684](_ak_command_types_8h_source.html#l00684) 行定义.