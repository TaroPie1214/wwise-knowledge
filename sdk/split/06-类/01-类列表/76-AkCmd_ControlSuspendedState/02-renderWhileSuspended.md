# renderWhileSuspended

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkCmd\_ControlSuspendedState](struct_ak_cmd___control_suspended_state.html)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| |  | | --- | | [isSuspended](struct_ak_cmd___control_suspended_state_a77ed713d76108adfab8589e7fc0327f5.html#a77ed713d76108adfab8589e7fc0327f5) | | [renderWhileSuspended](struct_ak_cmd___control_suspended_state_a1c3840a403c553e0fec657dbf1a7ef62.html#a1c3840a403c553e0fec657dbf1a7ef62) | | [transitionTime](struct_ak_cmd___control_suspended_state_a3c211e4c9ebe56722532261a20aae9ba.html#a3c211e4c9ebe56722532261a20aae9ba) | | [◆](#a1c3840a403c553e0fec657dbf1a7ef62)renderWhileSuspended |  | | --- | | [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) AkCmd\_ControlSuspendedState::renderWhileSuspended |  ///< If set to true, audio processing will still occur while suspended, but not outputted. When set to false, no audio will be processed at all, even when [AK::SoundEngine::RenderAudio](namespace_a_k_1_1_sound_engine_afe54af0f5be38be061e8a3c7d7642bb1.html#afe54af0f5be38be061e8a3c7d7642bb1) is called.  在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1277](_ak_command_types_8h_source.html#l01277) 行定义. |