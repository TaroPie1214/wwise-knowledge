# AkCallbackTypes.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[类型定义](#typedef-members) |
[枚举](#enum-members) |
[变量](#var-members)

AkCallbackTypes.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`  
`#include <AK/SoundEngine/Common/AkSoundEngineExport.h>`  
`#include <AK/SoundEngine/Common/AkMidiTypes.h>`  
`#include <AK/SoundEngine/Common/AkSpeakerConfig.h>`

[浏览源代码.](_ak_callback_types_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkSegmentInfo](struct_ak_segment_info.html) |
|  | Structure used to query info on active playing segments. [更多...](struct_ak_segment_info.html#details) |
|  | |
| struct | [AkEventCallbackInfo](struct_ak_event_callback_info.html) |
|  | |
| struct | [AkMIDIEventCallbackInfo](struct_ak_m_i_d_i_event_callback_info.html) |
|  | |
| struct | [AkMarkerCallbackInfo](struct_ak_marker_callback_info.html) |
|  | |
| struct | [AkDurationCallbackInfo](struct_ak_duration_callback_info.html) |
|  | |
| struct | [AkDynamicSequenceItemCallbackInfo](struct_ak_dynamic_sequence_item_callback_info.html) |
|  | |
| struct | [AkSpeakerVolumeMatrixCallbackInfo](struct_ak_speaker_volume_matrix_callback_info.html) |
|  | |
| struct | [AkMusicPlaylistCallbackInfo](struct_ak_music_playlist_callback_info.html) |
|  | |
| struct | [AkMusicSyncCallbackInfo](struct_ak_music_sync_callback_info.html) |
|  | |
| struct | [AkCallbackInfo](struct_ak_callback_info.html) |
|  | |
| struct | [AkBusMeteringCallbackInfo](struct_ak_bus_metering_callback_info.html) |
|  | |
| struct | [AkOutputDeviceMeteringCallbackInfo](struct_ak_output_device_metering_callback_info.html) |
|  | |
| struct | [AkResourceMonitorDataSummary](struct_ak_resource_monitor_data_summary.html) |
|  | Resources data summary structure containing general information about the system [更多...](struct_ak_resource_monitor_data_summary.html#details) |
|  | |
| struct | [AkDynamicSequenceSelectCallbackInfo](struct_ak_dynamic_sequence_select_callback_info.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef [AK::IAkMixerInputContext](class_a_k_1_1_i_ak_mixer_input_context.html) \* | [AkMixerInputContextPtr](_ak_callback_types_8h_ab4f4becf2477fc5b3afc41da781a50bd.html#ab4f4becf2477fc5b3afc41da781a50bd) |
|  | |
| typedef [AK::IAkMixerPluginContext](class_a_k_1_1_i_ak_mixer_plugin_context.html) \* | [AkMixerPluginContextPtr](_ak_callback_types_8h_a9cea4525427dbee2eb129300d2cff556.html#a9cea4525427dbee2eb129300d2cff556) |
|  | |
| typedef [AK::IAkGlobalPluginContext](class_a_k_1_1_i_ak_global_plugin_context.html) \* | [AkGlobalPluginContextPtr](_ak_callback_types_8h_a78d3b9e9a332305cf8487ec47fce631f.html#a78d3b9e9a332305cf8487ec47fce631f) |
|  | |
| typedef [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AkCallbackType\_t](_ak_callback_types_8h_ac7142322467a5cfa6c4367e667808bba.html#ac7142322467a5cfa6c4367e667808bba) |
|  | |
| typedef [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [AkAudioDeviceEvent\_t](_ak_callback_types_8h_af9a7cb85a5672b2dc771b4c428ff5edd.html#af9a7cb85a5672b2dc771b4c428ff5edd) |
|  | |
| typedef [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [AkGlobalCallbackLocation\_t](_ak_callback_types_8h_adf5124feb4fcddf6ff042b60ce2b1b24.html#adf5124feb4fcddf6ff042b60ce2b1b24) |
|  | |
| typedef void(\* | [AkEventCallbackFunc](_ak_callback_types_8h_a276c9e8420fee177debd0838b664d7c7.html#a276c9e8420fee177debd0838b664d7c7)) (enum [AkCallbackType](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732) in\_eType, struct [AkEventCallbackInfo](struct_ak_event_callback_info.html) \*in\_pEventInfo, void \*in\_pCallbackInfo, void \*in\_pCookie) |
|  | |
| typedef [AkEventCallbackFunc](_ak_callback_types_8h_a276c9e8420fee177debd0838b664d7c7.html#a276c9e8420fee177debd0838b664d7c7) | [AkCallbackFunc](_ak_callback_types_8h_af644072775b1cdd813e2d32792a22005.html#af644072775b1cdd813e2d32792a22005) |
|  | |
| typedef void(\* | [AkBusCallbackFunc](_ak_callback_types_8h_a71c3284146db2a0b9f8a76c17813514a.html#a71c3284146db2a0b9f8a76c17813514a)) (struct [AkSpeakerVolumeMatrixCallbackInfo](struct_ak_speaker_volume_matrix_callback_info.html) \*in\_pCallbackInfo, void \*in\_pCookie) |
|  | |
| typedef void(\* | [AkBankCallbackFunc](_ak_callback_types_8h_a5f4438e001923453a9f795eb64946be6.html#a5f4438e001923453a9f795eb64946be6)) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_bankID, const void \*in\_pInMemoryBankPtr, enum [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) in\_eLoadResult, void \*in\_pCookie) |
|  | |
| typedef void(\* | [AkGlobalCallbackFunc](_ak_callback_types_8h_a14f2022125839c43179c0c32381b4486.html#a14f2022125839c43179c0c32381b4486)) ([AkGlobalPluginContextPtr](_ak_callback_types_8h_a78d3b9e9a332305cf8487ec47fce631f.html#a78d3b9e9a332305cf8487ec47fce631f) in\_pContext, enum [AkGlobalCallbackLocation](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676) in\_eLocation, void \*in\_pCookie) |
|  | |
| typedef void(\* | [AkResourceMonitorCallbackFunc](_ak_callback_types_8h_a4d0a0890d6fe6d77f0e915fb46d4793f.html#a4d0a0890d6fe6d77f0e915fb46d4793f)) (const struct [AkResourceMonitorDataSummary](struct_ak_resource_monitor_data_summary.html) \*in\_pdataSummary) |
|  | |
| typedef void(\* | [AkDeviceStatusCallbackFunc](_ak_callback_types_8h_a3da9a1b793119a41c30eda4f5565eef9.html#a3da9a1b793119a41c30eda4f5565eef9)) ([AkGlobalPluginContextPtr](_ak_callback_types_8h_a78d3b9e9a332305cf8487ec47fce631f.html#a78d3b9e9a332305cf8487ec47fce631f) in\_pContext, [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_idAudioDeviceShareset, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_idDeviceID, enum [AkAudioDeviceEvent](_ak_callback_types_8h_a2ccf6d7dc52939aa076ffd63a0501413.html#a2ccf6d7dc52939aa076ffd63a0501413) in\_idEvent, enum [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) in\_AkResult) |
|  | |
| typedef void(\* | [AkBusMeteringCallbackFunc](_ak_callback_types_8h_a76bf3ae5d6d32ddcc3f7e8ebebda5e16.html#a76bf3ae5d6d32ddcc3f7e8ebebda5e16)) ([AkBusMeteringCallbackInfo](struct_ak_bus_metering_callback_info.html) \*in\_pCallbackInfo) |
|  | |
| typedef void(\* | [AkOutputDeviceMeteringCallbackFunc](_ak_callback_types_8h_a7a1b1b3b1ab310205b21452d7117a79e.html#a7a1b1b3b1ab310205b21452d7117a79e)) ([AkOutputDeviceMeteringCallbackInfo](struct_ak_output_device_metering_callback_info.html) \*in\_pCallbackInfo) |
|  | |
| typedef void(\* | [AkCaptureCallbackFunc](_ak_callback_types_8h_ad86cd3539770fef8a06707770b980f25.html#ad86cd3539770fef8a06707770b980f25)) ([AkAudioBuffer](class_ak_audio_buffer.html) &in\_CaptureBuffer, [AkOutputDeviceID](_ak_typedefs_8h_ab608859e8c575f46ce18433e32aa2ccd.html#ab608859e8c575f46ce18433e32aa2ccd) in\_idOutput, void \*in\_pCookie) |
|  | |

|  |  |
| --- | --- |
| 枚举 | |
| enum | [AkCallbackType](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732) {     [AK\_EndOfEvent](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a5ad7a62bfb83e7450cc685b3e51f767a) = 0x0001, [AK\_EndOfDynamicSequenceItem](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a1f3c7ae3783296ae95315c97c9b59f75) = 0x0002, [AK\_Marker](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732ad3d6fcbeb177c536da8eb74d0f132827) = 0x0004, [AK\_Duration](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732ac258a8d8f9d67963d0ad37ecf2b989ad) = 0x0008,     [AK\_SpeakerVolumeMatrix](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a398dd4133debe48731389d00ac8335fe) = 0x0010, [AK\_Starvation](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a392e9c2615d919f2bf9005cf250fef45) = 0x0020, [AK\_MusicPlaylistSelect](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732aec46a37d9cfdef25777042feaf56e265) = 0x0040, [AK\_MusicPlayStarted](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732aa1e3e1e198f859e3dad76009eec3ee29) = 0x0080,     [AK\_MusicSyncBeat](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a62d1f7986a64a7e9980ff82bd7ae9ba4) = 0x0100, [AK\_MusicSyncBar](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732ad7d4cc2283a63337542d49c70e55d9ca) = 0x0200, [AK\_MusicSyncEntry](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732ab29d1a78a0f92336b1c155548bc88d72) = 0x0400, [AK\_MusicSyncExit](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732aa92ff2f82ed7a651772e1f3f1d31c76e) = 0x0800,     [AK\_MusicSyncGrid](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a474f5b9582617f8a4f744e7d47dfa155) = 0x1000, [AK\_MusicSyncUserCue](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732ac827761a64b0d02303ea7eaa98240392) = 0x2000, [AK\_MusicSyncPoint](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732afde5b3e18578530b70f6e1241a552253) = 0x4000, [AK\_MIDIEvent](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a892b851b9525e6a716cc407493e4fc43) = 0x8000,     [AK\_DynamicSequenceSelect](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a5711d007422c8abda1cfc88174a56d11) = 0x10000, [AK\_Callback\_Last](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732af7124365ff82e6bf85d30342db7ba3a2) = 0x20000, [AK\_MusicSyncAll](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732af2fd49e6c33cc7831091387fec8a6fad) = 0x7f00, [AK\_CallbackBits](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a10f963a2036398459952fae79cdf216a) = 0xfffff,     [AK\_EnableGetMusicPlayPosition](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a01580e558008d636179cb7267eb9fd1a) = 0x200000, [AK\_EnableGetSourceStreamBuffering](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a92c8eea5406562f96ad801bd95a3145b) = 0x400000, [AK\_SourceInfo\_Last](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a7079bcc7d0e3ec225e040bd6d90f1fe7) = 0x800000   } |
|  | Type of callback. Used as a bitfield in methods [AK::SoundEngine::PostEvent()](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e) and [AK::SoundEngine::DynamicSequence::Open()](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_ab6daddd96e109dc7669889733ce4f2cc.html#ab6daddd96e109dc7669889733ce4f2cc). [更多...](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732) |
|  | |
| enum | [AkAudioDeviceEvent](_ak_callback_types_8h_a2ccf6d7dc52939aa076ffd63a0501413.html#a2ccf6d7dc52939aa076ffd63a0501413) { [AkAudioDeviceEvent\_Initialization](_ak_callback_types_8h_a2ccf6d7dc52939aa076ffd63a0501413.html#a2ccf6d7dc52939aa076ffd63a0501413aded58c8225ff8b4287352b43cc75990e), [AkAudioDeviceEvent\_Removal](_ak_callback_types_8h_a2ccf6d7dc52939aa076ffd63a0501413.html#a2ccf6d7dc52939aa076ffd63a0501413a47b0e1d9908231971ef43321f94df278), [AkAudioDeviceEvent\_SystemRemoval](_ak_callback_types_8h_a2ccf6d7dc52939aa076ffd63a0501413.html#a2ccf6d7dc52939aa076ffd63a0501413a6053514696e981ac2718cc7cdf2267fe), [AkAudioDeviceEvent\_Last](_ak_callback_types_8h_a2ccf6d7dc52939aa076ffd63a0501413.html#a2ccf6d7dc52939aa076ffd63a0501413a3d7a1e1c7d09fa274056e67f2af7b129) } |
|  | |
| enum | [AkGlobalCallbackLocation](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676) {     [AkGlobalCallbackLocation\_Register](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676a68917ce14320bb481b9ab2cfe6b228b6) = (1 << 0), [AkGlobalCallbackLocation\_Begin](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676af13fd05bf61f00e37dde9b34e8e14a98) = (1 << 1), [AkGlobalCallbackLocation\_PreProcessMessageQueueForRender](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676a75a5fe904855d596a5652cca9025ee41) = (1 << 2), [AkGlobalCallbackLocation\_PostMessagesProcessed](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676a01715b3336f3103915d69d62e30b3b82) = (1 << 3),     [AkGlobalCallbackLocation\_BeginRender](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676ae4e4ee72acf1bdc317a2922caadb9797) = (1 << 4), [AkGlobalCallbackLocation\_EndRender](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676aa8253be90a3fc3c208b61b4f22a1c919) = (1 << 5), [AkGlobalCallbackLocation\_End](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676a8a14506ea05469eece67eeb7f820f997) = (1 << 6), [AkGlobalCallbackLocation\_Term](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676aa5c7eebdf589a1b0ea29989e78e8ea2d) = (1 << 7),     [AkGlobalCallbackLocation\_Monitor](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676afd0151e57cff61f65ef3ae1bad83d651) = (1 << 8), [AkGlobalCallbackLocation\_MonitorRecap](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676ab30108371b0f53285f67c02a27ac8bd5) = (1 << 9), [AkGlobalCallbackLocation\_Init](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676a97caf890959d744c1c088d19c2d02e11) = (1 << 10), [AkGlobalCallbackLocation\_Suspend](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676a5d011e46f7895795e517ae8963753c72) = (1 << 11),     [AkGlobalCallbackLocation\_WakeupFromSuspend](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676afc694c052957b8b0f0016fca4f040786) = (1 << 12), [AkGlobalCallbackLocation\_ProfilerConnect](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676af25ffbaff3659d30f432ebae857d81f5) = (1 << 13), [AkGlobalCallbackLocation\_ProfilerDisconnect](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676ab107d5cd5c67e9af1bdc657e461f673a) = (1 << 14), [AkGlobalCallbackLocation\_Num](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676a3419a6bea89b5f767052ff39dd7251fc) = 15   } |
|  | Bit field of various locations in the audio processing loop where the game can be called back. [更多...](_ak_callback_types_8h_ae7a5e30e1402c7cf90d1b47420911676.html#ae7a5e30e1402c7cf90d1b47420911676) |
|  | |

|  |  |
| --- | --- |
| 变量 | |
| const ::[AkAudioDeviceEvent](_ak_callback_types_8h_a2ccf6d7dc52939aa076ffd63a0501413.html#a2ccf6d7dc52939aa076ffd63a0501413) | [AK::AkAudioDeviceEvent\_Initialization](namespace_a_k_a04ae5715cd9074a90eb0f4c0d3d0b540.html#a04ae5715cd9074a90eb0f4c0d3d0b540) = ::AkAudioDeviceEvent\_Initialization |
|  | |
| const ::[AkAudioDeviceEvent](_ak_callback_types_8h_a2ccf6d7dc52939aa076ffd63a0501413.html#a2ccf6d7dc52939aa076ffd63a0501413) | [AK::AkAudioDeviceEvent\_Removal](namespace_a_k_aaff6bc9a26b4209c044ebbdeefabea7c.html#aaff6bc9a26b4209c044ebbdeefabea7c) = ::AkAudioDeviceEvent\_Removal |
|  | |
| const ::[AkAudioDeviceEvent](_ak_callback_types_8h_a2ccf6d7dc52939aa076ffd63a0501413.html#a2ccf6d7dc52939aa076ffd63a0501413) | [AK::AkAudioDeviceEvent\_SystemRemoval](namespace_a_k_a23c4065192aec134c544b16f3c9412d2.html#a23c4065192aec134c544b16f3c9412d2) = ::AkAudioDeviceEvent\_SystemRemoval |
|  | |
| const ::[AkAudioDeviceEvent](_ak_callback_types_8h_a2ccf6d7dc52939aa076ffd63a0501413.html#a2ccf6d7dc52939aa076ffd63a0501413) | [AK::AkAudioDeviceEvent\_Last](namespace_a_k_afe3d03dff0915f37cdea6f393fa9d011.html#afe3d03dff0915f37cdea6f393fa9d011) = ::AkAudioDeviceEvent\_Last |
|  | |