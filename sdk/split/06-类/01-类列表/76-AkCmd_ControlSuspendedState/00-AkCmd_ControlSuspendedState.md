# AkCmd_ControlSuspendedState

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___control_suspended_state-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_ControlSuspendedState结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [isSuspended](struct_ak_cmd___control_suspended_state_a77ed713d76108adfab8589e7fc0327f5.html#a77ed713d76108adfab8589e7fc0327f5) |
|  | Whether to suspend or wake up the Sound Engine. [更多...](struct_ak_cmd___control_suspended_state_a77ed713d76108adfab8589e7fc0327f5.html#a77ed713d76108adfab8589e7fc0327f5) |
|  | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [renderWhileSuspended](struct_ak_cmd___control_suspended_state_a1c3840a403c553e0fec657dbf1a7ef62.html#a1c3840a403c553e0fec657dbf1a7ef62) |
|  | ///< If set to true, audio processing will still occur while suspended, but not outputted. When set to false, no audio will be processed at all, even when [AK::SoundEngine::RenderAudio](namespace_a_k_1_1_sound_engine_afe54af0f5be38be061e8a3c7d7642bb1.html#afe54af0f5be38be061e8a3c7d7642bb1) is called. [更多...](struct_ak_cmd___control_suspended_state_a1c3840a403c553e0fec657dbf1a7ef62.html#a1c3840a403c553e0fec657dbf1a7ef62) |
|  | |
| [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) | [transitionTime](struct_ak_cmd___control_suspended_state_a3c211e4c9ebe56722532261a20aae9ba.html#a3c211e4c9ebe56722532261a20aae9ba) |
|  | Delay the transition. During transition to suspended state, a fade-out is applied to the audio output. When 0, the suspend takes effect immediately but audio may glitch. [更多...](struct_ak_cmd___control_suspended_state_a3c211e4c9ebe56722532261a20aae9ba.html#a3c211e4c9ebe56722532261a20aae9ba) |
|  | |

## 详细描述

Puts the sound engine in background mode, where audio isn't processed anymore. Required when the platform has a background mode or some suspended state.

When suspended, the sound engine will process API messages (like PostEvent and SetSwitch) only when [AK::SoundEngine::RenderAudio](namespace_a_k_1_1_sound_engine_afe54af0f5be38be061e8a3c7d7642bb1.html#afe54af0f5be38be061e8a3c7d7642bb1) is called. It is recommended to match the `renderWhileSuspended` parameter with the behavior of the rest of your game:

- If your game still runs in background and you must keep some kind of coherent state between the audio engine and game, then allow rendering.
- If you want to minimize CPU when in background, then don't allow rendering and never call RenderAudio from the game.

Use the same command with `isSuspended` set to false when your application receives the message from the OS that the process is back in foreground.

Consult [处理系统专用事件](workingwithsdks_system_calls.html) to learn when it is appropriate to call this function for each platform.

参见
:   - [AkCommand\_ControlSuspendedState](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdad2f7398168a1013b7cf3587228d709a0 "See AkCmd_ControlSuspendedState")
    - [AK::SoundEngine::Suspend](namespace_a_k_1_1_sound_engine_afc66d31bf5c6425d841ca3510e2d0539.html#afc66d31bf5c6425d841ca3510e2d0539)
    - [AK::SoundEngine::WakeupFromSuspend](namespace_a_k_1_1_sound_engine_a9244da1d4d0deedcabdaaae863fcff47.html#a9244da1d4d0deedcabdaaae863fcff47)
    - [处理系统专用事件](workingwithsdks_system_calls.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1274](_ak_command_types_8h_source.html#l01274) 行定义.