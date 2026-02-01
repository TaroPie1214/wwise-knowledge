# AkCmd_SetListenerSpatialization

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_listener_spatialization-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetListenerSpatialization结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [listenerID](struct_ak_cmd___set_listener_spatialization_a47c45eca97634a82178e93ffc49a50e6.html#a47c45eca97634a82178e93ffc49a50e6) |
|  | Listener Game Object ID. [更多...](struct_ak_cmd___set_listener_spatialization_a47c45eca97634a82178e93ffc49a50e6.html#a47c45eca97634a82178e93ffc49a50e6) |
|  | |
| struct [AkChannelConfig](struct_ak_channel_config.html) | [channelConfig](struct_ak_cmd___set_listener_spatialization_a975c61e0bf15feb94961b2a3f35623b7.html#a975c61e0bf15feb94961b2a3f35623b7) |
|  | Channel configuration associated with volumes. When valid, an array of volume offsets is expected to follow the command. [更多...](struct_ak_cmd___set_listener_spatialization_a975c61e0bf15feb94961b2a3f35623b7.html#a975c61e0bf15feb94961b2a3f35623b7) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [isSpatialized](struct_ak_cmd___set_listener_spatialization_a5bdbccc5b1774c5f3703735c4a4cc0fb.html#a5bdbccc5b1774c5f3703735c4a4cc0fb) |
|  | Spatialization toggle, 0 = not spatialized [更多...](struct_ak_cmd___set_listener_spatialization_a5bdbccc5b1774c5f3703735c4a4cc0fb.html#a5bdbccc5b1774c5f3703735c4a4cc0fb) |
|  | |

## 详细描述

Sets a listener's spatialization parameters. This lets you define listener-specific volume offsets for each audio channel. If `isSpatialized` is false, the volumes array is used for this listener (3D positions have no effect on the speaker distribution). Otherwise, the volumes array is added to the speaker distribution computed for this listener.

备注
:   - If a sound is mixed into a bus that has a different speaker configuration than `channelConfig`, standard up/downmix rules apply.
    - Sounds with 3D Spatialization set to None will not be affected by these parameters.

When `channelConfig` is set to a valid channel config, the Sound Engine expects an array of `AkReal32` objects after the command. The number of items must correspond to the number of channels in `channelConfig`. For example:

```
AkReal32 volumes[2] = { 1.0f, 1.0f };
auto cmd = (AkCmd_SetListenerSpatialization*)AK_CommandBuffer_Add(buffer, AkCommand_SetListenerSpatialization);
cmd->channelConfig.SetStandard(AK_SPEAKER_SETUP_STEREO);
AK_CommandBuffer_AddArray(buffer, sizeof(AkReal32), cmd->channelConfig.uNumChannels, volumes);
```

When `channelConfig` is left to an invalid config, no volume array is expected to follow, and the command acts as a simple spatialization toggle.

This command can fail for the following reasons:

- AK\_InvalidParameter: `listenerID` is outside the valid range, `channelConfig` is invalid, incomplete volumes array after the command
- AK\_InsufficientMemory: Not enough memory to process the command
- AK\_IDNotFound: `gameObjectID` is not a registered game object ID.

参见
:   - [AkCommand\_SetListenerSpatialization](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda7030c079fc10a94cb71f3a98ef265e45 "See AkCmd_SetListenerSpatialization")
    - [AK\_CommandBuffer\_AddArray](_ak_command_buffer_8h_a7512f07e3e8f24cf4ed15bebf3a6392e.html#a7512f07e3e8f24cf4ed15bebf3a6392e)
    - [音量偏置与空间化](soundengine_listeners.html#soundengine_listeners_spatial)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [416](_ak_command_types_8h_source.html#l00416) 行定义.