# AkCommandTypes.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[类型定义](#typedef-members) |
[枚举](#enum-members)

AkCommandTypes.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`  
`#include <AK/SoundEngine/Common/AkCallbackTypes.h>`  
`#include <AK/SpatialAudio/Common/AkSpatialAudioTypes.h>`

[浏览源代码.](_ak_command_types_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkCmd\_PostEvent](struct_ak_cmd___post_event.html) |
|  | |
| struct | [AkCmd\_RegisterGameObject](struct_ak_cmd___register_game_object.html) |
|  | |
| struct | [AkCmd\_UnregisterGameObject](struct_ak_cmd___unregister_game_object.html) |
|  | |
| struct | [AkCmd\_Callback](struct_ak_cmd___callback.html) |
|  | |
| struct | [AkCmd\_SetRTPC](struct_ak_cmd___set_r_t_p_c.html) |
|  | |
| struct | [AkCmd\_ResetRTPC](struct_ak_cmd___reset_r_t_p_c.html) |
|  | |
| struct | [AkCmd\_SetPosition](struct_ak_cmd___set_position.html) |
|  | |
| struct | [AkCmd\_SetMultiplePositions](struct_ak_cmd___set_multiple_positions.html) |
|  | |
| struct | [AkCmd\_SetListeners](struct_ak_cmd___set_listeners.html) |
|  | |
| struct | [AkCmd\_SetDefaultListeners](struct_ak_cmd___set_default_listeners.html) |
|  | |
| struct | [AkCmd\_ResetListeners](struct_ak_cmd___reset_listeners.html) |
|  | |
| struct | [AkCmd\_SetListenerSpatialization](struct_ak_cmd___set_listener_spatialization.html) |
|  | |
| struct | [AkCmd\_SetGameObjectAuxSendValues](struct_ak_cmd___set_game_object_aux_send_values.html) |
|  | |
| struct | [AkCmd\_SetGameObjectOutputBusVolume](struct_ak_cmd___set_game_object_output_bus_volume.html) |
|  | |
| struct | [AkCmd\_SetScalingFactor](struct_ak_cmd___set_scaling_factor.html) |
|  | |
| struct | [AkCmd\_SetObjectObstructionAndOcclusion](struct_ak_cmd___set_object_obstruction_and_occlusion.html) |
|  | |
| struct | [AkCmd\_SetMultipleObstructionAndOcclusion](struct_ak_cmd___set_multiple_obstruction_and_occlusion.html) |
|  | |
| struct | [AkCmd\_SetDistanceProbe](struct_ak_cmd___set_distance_probe.html) |
|  | |
| struct | [AkCmd\_StopAll](struct_ak_cmd___stop_all.html) |
|  | |
| struct | [AkCmd\_ExecuteActionOnEvent](struct_ak_cmd___execute_action_on_event.html) |
|  | |
| struct | [AkCmd\_ExecuteActionOnPlayingID](struct_ak_cmd___execute_action_on_playing_i_d.html) |
|  | |
| struct | [AkCmd\_SeekOnEvent](struct_ak_cmd___seek_on_event.html) |
|  | |
| struct | [AkCmd\_SetState](struct_ak_cmd___set_state.html) |
|  | |
| struct | [AkCmd\_SetSwitch](struct_ak_cmd___set_switch.html) |
|  | |
| struct | [AkCmd\_PostTrigger](struct_ak_cmd___post_trigger.html) |
|  | |
| struct | [AkCmd\_PostMIDIOnEvent](struct_ak_cmd___post_m_i_d_i_on_event.html) |
|  | |
| struct | [AkCmd\_StopMIDIOnEvent](struct_ak_cmd___stop_m_i_d_i_on_event.html) |
|  | |
| struct | [AkCmd\_DynamicSequence\_Open](struct_ak_cmd___dynamic_sequence___open.html) |
|  | |
| struct | [AkCmd\_DynamicSequence\_Op](struct_ak_cmd___dynamic_sequence___op.html) |
|  | |
| struct | [AkCmd\_DynamicSequence\_Seek](struct_ak_cmd___dynamic_sequence___seek.html) |
|  | |
| struct | [AkCmd\_AddOutput](struct_ak_cmd___add_output.html) |
|  | |
| struct | [AkCmd\_RemoveOutput](struct_ak_cmd___remove_output.html) |
|  | |
| struct | [AkCmd\_ReplaceOutput](struct_ak_cmd___replace_output.html) |
|  | |
| struct | [AkCmd\_SetBusAudioDevice](struct_ak_cmd___set_bus_audio_device.html) |
|  | |
| struct | [AkCmd\_SetBusConfig](struct_ak_cmd___set_bus_config.html) |
|  | |
| struct | [AkCmd\_ResetBusConfig](struct_ak_cmd___reset_bus_config.html) |
|  | |
| struct | [AkCmd\_ResetGlobalValues](struct_ak_cmd___reset_global_values.html) |
|  | |
| struct | [AkCmd\_SetSidechainMixConfig](struct_ak_cmd___set_sidechain_mix_config.html) |
|  | |
| struct | [AkCmd\_SetEffect](struct_ak_cmd___set_effect.html) |
|  | |
| struct | [AkCmd\_SetOutputVolume](struct_ak_cmd___set_output_volume.html) |
|  | |
| struct | [AkCmd\_SetPanningRule](struct_ak_cmd___set_panning_rule.html) |
|  | |
| struct | [AkCmd\_SetSpeakerAngles](struct_ak_cmd___set_speaker_angles.html) |
|  | |
| struct | [AkCmd\_ControlOutputCapture](struct_ak_cmd___control_output_capture.html) |
|  | |
| struct | [AkCmd\_AddOutputCaptureMarker](struct_ak_cmd___add_output_capture_marker.html) |
|  | |
| struct | [AkCmd\_ControlOfflineRendering](struct_ak_cmd___control_offline_rendering.html) |
|  | |
| struct | [AkCmd\_SetRandomSeed](struct_ak_cmd___set_random_seed.html) |
|  | |
| struct | [AkCmd\_ControlEventStreamCache](struct_ak_cmd___control_event_stream_cache.html) |
|  | |
| struct | [AkCmd\_ControlSuspendedState](struct_ak_cmd___control_suspended_state.html) |
|  | |
| struct | [AkCmd\_MuteBackgroundMusic](struct_ak_cmd___mute_background_music.html) |
|  | |
| struct | [AkCmd\_SendPluginCustomGameData](struct_ak_cmd___send_plugin_custom_game_data.html) |
|  | |
| struct | [AkCmd\_SA\_RegisterListener](struct_ak_cmd___s_a___register_listener.html) |
|  | |
| struct | [AkCmd\_SA\_UnregisterListener](struct_ak_cmd___s_a___unregister_listener.html) |
|  | |
| struct | [AkCmd\_SA\_SetImageSource](struct_ak_cmd___s_a___set_image_source.html) |
|  | |
| struct | [AkCmd\_SA\_RemoveImageSource](struct_ak_cmd___s_a___remove_image_source.html) |
|  | |
| struct | [AkCmd\_SA\_ClearImageSources](struct_ak_cmd___s_a___clear_image_sources.html) |
|  | |
| struct | [AkCmd\_SA\_SetGeometry](struct_ak_cmd___s_a___set_geometry.html) |
|  | |
| struct | [AkCmd\_SA\_RemoveGeometry](struct_ak_cmd___s_a___remove_geometry.html) |
|  | |
| struct | [AkCmd\_SA\_SetGeometryInstance](struct_ak_cmd___s_a___set_geometry_instance.html) |
|  | |
| struct | [AkCmd\_SA\_RemoveGeometryInstance](struct_ak_cmd___s_a___remove_geometry_instance.html) |
|  | |
| struct | [AkCmd\_SA\_SetRoom](struct_ak_cmd___s_a___set_room.html) |
|  | |
| struct | [AkCmd\_SA\_RemoveRoom](struct_ak_cmd___s_a___remove_room.html) |
|  | |
| struct | [AkCmd\_SA\_SetPortal](struct_ak_cmd___s_a___set_portal.html) |
|  | |
| struct | [AkCmd\_SA\_SetPortalObstructionAndOcclusion](struct_ak_cmd___s_a___set_portal_obstruction_and_occlusion.html) |
|  | |
| struct | [AkCmd\_SA\_SetGameObjectToPortalObstruction](struct_ak_cmd___s_a___set_game_object_to_portal_obstruction.html) |
|  | |
| struct | [AkCmd\_SA\_SetPortalToPortalObstruction](struct_ak_cmd___s_a___set_portal_to_portal_obstruction.html) |
|  | |
| struct | [AkCmd\_SA\_RemovePortal](struct_ak_cmd___s_a___remove_portal.html) |
|  | |
| struct | [AkCmd\_SA\_SetReverbZone](struct_ak_cmd___s_a___set_reverb_zone.html) |
|  | |
| struct | [AkCmd\_SA\_RemoveReverbZone](struct_ak_cmd___s_a___remove_reverb_zone.html) |
|  | |
| struct | [AkCmd\_SA\_SetGameObjectInRoom](struct_ak_cmd___s_a___set_game_object_in_room.html) |
|  | |
| struct | [AkCmd\_SA\_UnsetGameObjectInRoom](struct_ak_cmd___s_a___unset_game_object_in_room.html) |
|  | |
| struct | [AkCmd\_SA\_SetGameObjectRadius](struct_ak_cmd___s_a___set_game_object_radius.html) |
|  | |
| struct | [AkCmd\_SA\_SetEarlyReflectionsAuxSend](struct_ak_cmd___s_a___set_early_reflections_aux_send.html) |
|  | |
| struct | [AkCmd\_SA\_SetEarlyReflectionsVolume](struct_ak_cmd___s_a___set_early_reflections_volume.html) |
|  | |
| struct | [AkCmd\_SA\_SetAdjacentRoomBleed](struct_ak_cmd___s_a___set_adjacent_room_bleed.html) |
|  | |
| struct | [AkCmd\_SA\_SetReflectionsOrder](struct_ak_cmd___s_a___set_reflections_order.html) |
|  | |
| struct | [AkCmd\_SA\_SetDiffractionOrder](struct_ak_cmd___s_a___set_diffraction_order.html) |
|  | |
| struct | [AkCmd\_SA\_SetMaxGlobalReflectionPaths](struct_ak_cmd___s_a___set_max_global_reflection_paths.html) |
|  | |
| struct | [AkCmd\_SA\_SetMaxEmitterRoomAuxSends](struct_ak_cmd___s_a___set_max_emitter_room_aux_sends.html) |
|  | |
| struct | [AkCmd\_SA\_SetMaxDiffractionPaths](struct_ak_cmd___s_a___set_max_diffraction_paths.html) |
|  | |
| struct | [AkCmd\_SA\_SetSmoothingConstant](struct_ak_cmd___s_a___set_smoothing_constant.html) |
|  | |
| struct | [AkCmd\_SA\_SetTransmissionOperation](struct_ak_cmd___s_a___set_transmission_operation.html) |
|  | |
| struct | [AkCmd\_SA\_SetNumberOfPrimaryRays](struct_ak_cmd___s_a___set_number_of_primary_rays.html) |
|  | |
| struct | [AkCmd\_SA\_SetLoadBalancingSpread](struct_ak_cmd___s_a___set_load_balancing_spread.html) |
|  | |
| struct | [AkCmd\_SA\_ResetStochasticEngine](struct_ak_cmd___s_a___reset_stochastic_engine.html) |
|  | |
| struct | [AkCommandBufferHeader](struct_ak_command_buffer_header.html) |
|  | Describes the data written at the beginning of any initialized command buffer. [更多...](struct_ak_command_buffer_header.html#details) |
|  | |
| struct | [AkCommandHeader](struct_ak_command_header.html) |
|  | Describes the data written at the beginning of each command in the command buffer [更多...](struct_ak_command_header.html#details) |
|  | |
| struct | [AkCommandBufferIterator](struct_ak_command_buffer_iterator.html) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [AkCommand\_t](_ak_command_types_8h_a0ed0dc74e5d2f23c676b705b31df3a1b.html#a0ed0dc74e5d2f23c676b705b31df3a1b) |
|  | |
| typedef void(\* | [AkCommandCallbackFunc](_ak_command_types_8h_adf806f94d5311616d788b6b479caac85.html#adf806f94d5311616d788b6b479caac85)) (void \*in\_pCookie) |
|  | |

|  |  |
| --- | --- |
| 枚举 | |
| enum | [AkCommand](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfd) {     [AkCommand\_EndOfBuffer](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdae9b1f348be80c2343121cfc1c80071c4) = 0, [AkCommand\_PostEvent](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaf20e9790432e3db005cd602adcf4d962), [AkCommand\_RegisterGameObject](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdafa6120328cdb73a0745a5777863dc0d4), [AkCommand\_UnregisterGameObject](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda90baf8a9598a8ec1b5935193d903ff7d),     [AkCommand\_Callback](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda9c28c3bfda569b533e34991b305792b6), [AkCommand\_SetRTPC](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda95aa5709b8fff06b947d3eda020b1189), [AkCommand\_ResetRTPC](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda6d3735e6380fd7a9c984dfd131175740), [AkCommand\_SetPosition](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdabd296114ddc48a2c39a7554dc94ae9cc),     [AkCommand\_SetListeners](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda28d2e0777e20fd3e1041437522db6431), [AkCommand\_SetDefaultListeners](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdac1477710c8ff85a24e53f09213edf55d), [AkCommand\_ResetListeners](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda03865610c80e1789db0c82c82387871d), [AkCommand\_SetListenerSpatialization](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda7030c079fc10a94cb71f3a98ef265e45),     [AkCommand\_SetGameObjectAuxSendValues](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaf61a2cd81ebb15c5cbaaeef537b500e2), [AkCommand\_SetGameObjectOutputBusVolume](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda24263a6c13160d3d91c9c4e2b64c9fb9), [AkCommand\_SetObjectObstructionAndOcclusion](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdad108c7253238706e2a133e0408237b31), [AkCommand\_SetMultipleObstructionAndOcclusion](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdadd3a1055f0c89a3c9f1b9a253b162569),     [AkCommand\_SetScalingFactor](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaf4f3a64d5fd69388c71ac9da5876898e), [AkCommand\_SetMultiplePositions](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda5c97cb38cc9ea4849a512bfe412ffdf5), [AkCommand\_SetDistanceProbe](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda2a961fd1d14bca560cbf82c84a95a0b3), [AkCommand\_StopAll](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdac83100924ce85da8060bfb1f37495f33),     [AkCommand\_ExecuteActionOnEvent](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda4a336431099a6b1b69da4821db6054ea), [AkCommand\_ExecuteActionOnPlayingID](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaa3a60c9caa80d51a5ebaf4da42b10e0d), [AkCommand\_SeekOnEvent](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda40a0393356c4b66df7f74c67f771553e), [AkCommand\_SetState](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda6c765e2678326e0d679d2e96c3bc3d35),     [AkCommand\_SetSwitch](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda91fc7767a8843230844ea1945fab2ae2), [AkCommand\_PostTrigger](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda2435ca4e862f810f7d574e6930912c67), [AkCommand\_PostMIDIOnEvent](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdabb16fb8c53fb070bf174b991f33669b2), [AkCommand\_StopMIDIOnEvent](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda76e2dddc50d0b803e288031d7fd805a2),     [AkCommand\_DynamicSequence\_Open](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda716005c85cf0d59989839e210ac0accc), [AkCommand\_DynamicSequence\_Op](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdab920c51e91c01699883765d7db7553da), [AkCommand\_DynamicSequence\_Seek](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda063663ffa99f8efc9e4762af684c329a), [AkCommand\_AddOutput](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda3254436f52efd13b0a86d9176b751196),     [AkCommand\_RemoveOutput](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda6ac7a9a5ab95715129a8db52fc759d94), [AkCommand\_ReplaceOutput](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda9b3a7bf26e01fa4633f070ee51fa8f68), [AkCommand\_SetBusAudioDevice](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda3a6b55b2d0117c80d088f6e8c0fa0e05), [AkCommand\_SetBusConfig](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda357393637deca3073f1069c487ec2f35),     [AkCommand\_ResetBusConfig](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda3981d5be95b56289ecea8159627d88be), [AkCommand\_SetEffect](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaa0443ddf9f9de5f5ebac01ccc66ea1f8), [AkCommand\_SetOutputVolume](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda5dbc56647ce74caf407b644af45bf878), [AkCommand\_SetPanningRule](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaa7648b9699df4a9a1eadc038bd091b20),     [AkCommand\_SetSpeakerAngles](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaa41934308a8d68a347574bdc560648c4), [AkCommand\_ControlOutputCapture](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda75650a8b2cf3567fe5842c944e13c277), [AkCommand\_AddOutputCaptureMarker](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda32b68ae6b1020f48263203dd7c413de4), [AkCommand\_ControlOfflineRendering](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdab86dae96b811481c1afdab0901ee2f8f),     [AkCommand\_SetRandomSeed](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaaa8c84981c5163f6ac622e554b30b8f4), [AkCommand\_ControlEventStreamCache](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaad5c3276c6f28ec03634c9744edfeb7d), [AkCommand\_ControlSuspendedState](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdad2f7398168a1013b7cf3587228d709a0), [AkCommand\_MuteBackgroundMusic](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda43238d249fbfc13a76ae8b2ed1eb3208),     [AkCommand\_SendPluginCustomGameData](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdabf0e7dc9ceb02348eeb4ebfea428b713), [AkCommand\_SetSidechainMixConfig](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda6e5975488e4da133ebe8d33dc57cba1f), [AkCommand\_ResetGlobalValues](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda2dd0c0e44915f982cfa5197f645b31ad), [AkCommand\_SA\_Begin](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdad60684f0070fa5346544c67ae70b77c0),     [AkCommand\_SA\_RegisterListener](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda5f600d5e7728ae29e9287fed9102fb3f) = AkCommand\_SA\_Begin, [AkCommand\_SA\_UnregisterListener](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda7c244e6a4352f39fa3290b5e89d1fbb8), [AkCommand\_SA\_SetImageSource](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda96e5c87f8383997d06c0a1f11e5785a6), [AkCommand\_SA\_RemoveImageSource](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda86b00d30d5a55d227d41fbbe2cf536ca),     [AkCommand\_SA\_ClearImageSources](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdab9c9e823ee2075c3e38467cb782563b6), [AkCommand\_SA\_SetGeometry](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdacf9e1e3901df98eef024523667c08107), [AkCommand\_SA\_RemoveGeometry](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaa1851ceec5647ed78e07ffc63b039ca7), [AkCommand\_SA\_SetGeometryInstance](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda68b96460ab326896fd8475d8917ea47b),     [AkCommand\_SA\_RemoveGeometryInstance](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda26c62f270a2d1afd6028ea5c71397cd7), [AkCommand\_SA\_SetRoom](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdabd09c21c56c233f2e066d563ef805e60), [AkCommand\_SA\_RemoveRoom](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdae0c715a7f738173db9f1bcd37527e46f), [AkCommand\_SA\_SetPortal](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaab60efabdb8c16ad7c30c9c1bd8ee6cf),     [AkCommand\_SA\_RemovePortal](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdab24bbd80c36f3ad5acf6c3e4b49a2a92), [AkCommand\_SA\_SetPortalObstructionAndOcclusion](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda41645e1bc17a24982eb5b4a5bf3e29ec), [AkCommand\_SA\_SetGameObjectToPortalObstruction](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda8e838c56d866f19ba7e78c605fb6dbc2), [AkCommand\_SA\_SetPortalToPortalObstruction](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda4aae41be47961288e58ebc69544f2c8a),     [AkCommand\_SA\_SetReverbZone](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda86d714befda425a13f49fda43a4135ac), [AkCommand\_SA\_RemoveReverbZone](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda85cefe1c9b0727657556423a3b0cbde4), [AkCommand\_SA\_SetGameObjectInRoom](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaac74bf305672b4e89a7a0ce7d6426099), [AkCommand\_SA\_UnsetGameObjectInRoom](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdad33ecf98c98456b2f85a0080ad816aa8),     [AkCommand\_SA\_SetGameObjectRadius](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaaaa4a14c77692f932cca22c7b94a85a1), [AkCommand\_SA\_SetAdjacentRoomBleed](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda86df5bc019e8cbb02209dd5e100577cc), [AkCommand\_SA\_SetEarlyReflectionsAuxSend](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda7d75744918d1479e1daf3e0649307928), [AkCommand\_SA\_SetEarlyReflectionsVolume](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaedcd8ce98045d86fac9ece68985e80b4),     [AkCommand\_SA\_SetReflectionsOrder](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdab8233281b4b6133266e3e951aa556185), [AkCommand\_SA\_SetDiffractionOrder](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda3c84762eb77d1612fbccfbaf56a9ed26), [AkCommand\_SA\_SetMaxGlobalReflectionPaths](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdae705bd68d00b3b29749b94c65bdeecd4), [AkCommand\_SA\_SetMaxEmitterRoomAuxSends](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda9a691fd3b8c9725ae922cd41b8b9a980),     [AkCommand\_SA\_SetMaxDiffractionPaths](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdae45c60d0299a7854e24161950a276165), [AkCommand\_SA\_SetSmoothingConstant](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda74f7939f2b23c98a42c66d8154760b1c), [AkCommand\_SA\_SetTransmissionOperation](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda92a149b06115f44168c4471d091445b2), [AkCommand\_SA\_SetNumberOfPrimaryRays](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda1f07872d2b05e65e2bbf1d3b034f3033),     [AkCommand\_SA\_SetLoadBalancingSpread](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda42a4a33357945ca8fb23cbf45170dbd7), [AkCommand\_SA\_ResetStochasticEngine](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdac59a4659855bcd97cb9741d62d1d14ee), [AkCommand\_SA\_End](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda5e0e0dc6b0b8bc73b1449424db37cae7), [AkCommand\_NUM](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda09a1cc1886a59c00542637ae2c740eb0) = AkCommand\_SA\_End   } |
|  | IDs for commands that can be sent to the sound engine. Each command has an associated structure that defines its payload. [更多...](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfd) |
|  | |