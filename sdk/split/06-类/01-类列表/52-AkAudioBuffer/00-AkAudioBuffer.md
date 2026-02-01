# AkAudioBuffer

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_audio_buffer-members.html) |
[Public 成员函数](#pub-methods)

AkAudioBuffer类 参考

`#include <AkCommonDefs.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkAudioBuffer](class_ak_audio_buffer_aac745aff63bbeac274bea6c0c47e6589.html#aac745aff63bbeac274bea6c0c47e6589) () |
|  | Constructor. [更多...](class_ak_audio_buffer_aac745aff63bbeac274bea6c0c47e6589.html#aac745aff63bbeac274bea6c0c47e6589) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [ClearData](class_ak_audio_buffer_ac251b19c7795d661780f38c7ea23598d.html#ac251b19c7795d661780f38c7ea23598d) () |
|  | Clear data pointer. [更多...](class_ak_audio_buffer_ac251b19c7795d661780f38c7ea23598d.html#ac251b19c7795d661780f38c7ea23598d) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Clear](class_ak_audio_buffer_a21e1e395050cdc6f1b3c675ecf6047e7.html#a21e1e395050cdc6f1b3c675ecf6047e7) () |
|  | Clear members. [更多...](class_ak_audio_buffer_a21e1e395050cdc6f1b3c675ecf6047e7.html#a21e1e395050cdc6f1b3c675ecf6047e7) |
|  | |
| Channel queries. | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [NumChannels](class_ak_audio_buffer_a4523322478ec9a0f9de0c7c72e65df2f.html#a4523322478ec9a0f9de0c7c72e65df2f) () const |
|  | Get the number of channels. [更多...](class_ak_audio_buffer_a4523322478ec9a0f9de0c7c72e65df2f.html#a4523322478ec9a0f9de0c7c72e65df2f) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [HasLFE](class_ak_audio_buffer_a9ac12a3c62e9c1e734b5a42d68896bf4.html#a9ac12a3c62e9c1e734b5a42d68896bf4) () const |
|  | Returns true if there is an LFE channel present. [更多...](class_ak_audio_buffer_a9ac12a3c62e9c1e734b5a42d68896bf4.html#a9ac12a3c62e9c1e734b5a42d68896bf4) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkChannelConfig](struct_ak_channel_config.html) | [GetChannelConfig](class_ak_audio_buffer_a7601d9b814dbcb9dfe2bfbaa05fcb13b.html#a7601d9b814dbcb9dfe2bfbaa05fcb13b) () const |
|  | |
| Interleaved interface | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [GetInterleavedData](class_ak_audio_buffer_a8b3f75d4e95d5ce9af0b4573fae87510.html#a8b3f75d4e95d5ce9af0b4573fae87510) () |
|  | |
| void | [AttachInterleavedData](class_ak_audio_buffer_a072b617b49c997025b5fd0f29aec4b1a.html#a072b617b49c997025b5fd0f29aec4b1a) (void \*in\_pData, [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) in\_uMaxFrames, [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) in\_uValidFrames) |
|  | Attach interleaved data. Allocation is performed outside. [更多...](class_ak_audio_buffer_a072b617b49c997025b5fd0f29aec4b1a.html#a072b617b49c997025b5fd0f29aec4b1a) |
|  | |
| void | [AttachInterleavedData](class_ak_audio_buffer_a5a4333ede67d1bc632dcf42c2e5aa0a8.html#a5a4333ede67d1bc632dcf42c2e5aa0a8) (void \*in\_pData, [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) in\_uMaxFrames, [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) in\_uValidFrames, [AkChannelConfig](struct_ak_channel_config.html) in\_channelConfig) |
|  | Attach interleaved data with a new channel config. Allocation is performed outside. [更多...](class_ak_audio_buffer_a5a4333ede67d1bc632dcf42c2e5aa0a8.html#a5a4333ede67d1bc632dcf42c2e5aa0a8) |
|  | |

|  |  |
| --- | --- |
| Deinterleaved interface | |
| void \* | [pData](class_ak_audio_buffer_ae7a3a33d874a6b0c73ed87eeb6f895e9.html#ae7a3a33d874a6b0c73ed87eeb6f895e9) |
|  | Start of the audio buffer. [更多...](class_ak_audio_buffer_ae7a3a33d874a6b0c73ed87eeb6f895e9.html#ae7a3a33d874a6b0c73ed87eeb6f895e9) |
|  | |
| [AkChannelConfig](struct_ak_channel_config.html) | [channelConfig](class_ak_audio_buffer_a95922c0554fc1de863f04068f18f54c8.html#a95922c0554fc1de863f04068f18f54c8) |
|  | Channel config. [更多...](class_ak_audio_buffer_a95922c0554fc1de863f04068f18f54c8.html#a95922c0554fc1de863f04068f18f54c8) |
|  | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [uMaxFrames](class_ak_audio_buffer_add4bd03eb65294e497711a42989136a8.html#add4bd03eb65294e497711a42989136a8) |
|  | Number of sample frames the buffer can hold. Access through [AkAudioBuffer::MaxFrames()](class_ak_audio_buffer_a537445dce6e3ed09dd2c337fd73c6b41.html#a537445dce6e3ed09dd2c337fd73c6b41). [更多...](class_ak_audio_buffer_add4bd03eb65294e497711a42989136a8.html#add4bd03eb65294e497711a42989136a8) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [eState](class_ak_audio_buffer_a069d15381980ac4851216e084cf6a0cc.html#a069d15381980ac4851216e084cf6a0cc) |
|  | Execution status [更多...](class_ak_audio_buffer_a069d15381980ac4851216e084cf6a0cc.html#a069d15381980ac4851216e084cf6a0cc) |
|  | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [uValidFrames](class_ak_audio_buffer_ab7f90fd99119b56e92e4cbf3559f98cd.html#ab7f90fd99119b56e92e4cbf3559f98cd) |
|  | Number of valid sample frames in the audio buffer [更多...](class_ak_audio_buffer_ab7f90fd99119b56e92e4cbf3559f98cd.html#ab7f90fd99119b56e92e4cbf3559f98cd) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [HasData](class_ak_audio_buffer_ab50a4432d92125370e2f8d995f5de497.html#ab50a4432d92125370e2f8d995f5de497) () const |
|  | Check if buffer has samples attached to it. [更多...](class_ak_audio_buffer_ab50a4432d92125370e2f8d995f5de497.html#ab50a4432d92125370e2f8d995f5de497) |
|  | |
| [AkSampleType](_ak_common_defs_8h_a58f11a728038d16fe4187612a7a842fb.html#a58f11a728038d16fe4187612a7a842fb) \* | [GetChannel](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uIndex) |
|  | |
| [AkSampleType](_ak_common_defs_8h_a58f11a728038d16fe4187612a7a842fb.html#a58f11a728038d16fe4187612a7a842fb) \* | [GetLFE](class_ak_audio_buffer_a06f9e3184b8664df136f8d123b04cc81.html#a06f9e3184b8664df136f8d123b04cc81) () |
|  | |
| void | [ZeroPadToMaxFrames](class_ak_audio_buffer_a87a1c21f8a106616a7ddfece0ef040cc.html#a87a1c21f8a106616a7ddfece0ef040cc) () |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [AttachContiguousDeinterleavedData](class_ak_audio_buffer_a16e951ef643af18fd45cf647b913f7ec.html#a16e951ef643af18fd45cf647b913f7ec) (void \*in\_pData, [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) in\_uMaxFrames, [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) in\_uValidFrames, [AkChannelConfig](struct_ak_channel_config.html) in\_channelConfig) |
|  | Attach deinterleaved data where channels are contiguous in memory. Allocation is performed outside. [更多...](class_ak_audio_buffer_a16e951ef643af18fd45cf647b913f7ec.html#a16e951ef643af18fd45cf647b913f7ec) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void \* | [DetachContiguousDeinterleavedData](class_ak_audio_buffer_a076fe27514d50b8a6f962bf3cf748e94.html#a076fe27514d50b8a6f962bf3cf748e94) () |
|  | Detach deinterleaved data where channels are contiguous in memory. The address of the buffer is returned and fields are cleared. [更多...](class_ak_audio_buffer_a076fe27514d50b8a6f962bf3cf748e94.html#a076fe27514d50b8a6f962bf3cf748e94) |
|  | |
| bool | [CheckValidSamples](class_ak_audio_buffer_a36ee098e1830eabfb1b086f6c03dba14.html#a36ee098e1830eabfb1b086f6c03dba14) () |
|  | |
| void | [RelocateMedia](class_ak_audio_buffer_a644b564c3a6266ed273ad1be95da6538.html#a644b564c3a6266ed273ad1be95da6538) ([AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \*in\_pNewMedia, [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \*in\_pOldMedia) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [MaxFrames](class_ak_audio_buffer_a537445dce6e3ed09dd2c337fd73c6b41.html#a537445dce6e3ed09dd2c337fd73c6b41) () const |
|  | |
| static [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [StandardToPipelineIndex](class_ak_audio_buffer_a065aaa3af3569b6e19d09f56478eca46.html#a065aaa3af3569b6e19d09f56478eca46) ([AkChannelConfig](struct_ak_channel_config.html) in\_channelConfig, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uChannelIdx) |
|  | |

## 详细描述

Audio buffer structure including the address of an audio buffer, the number of valid frames inside, and the maximum number of frames the audio buffer can hold.

参见
:   - [访问使用 AkAudioBuffer 结构的数据](soundengine_plugins.html#fx_audiobuffer_struct)

在文件 [AkCommonDefs.h](_ak_common_defs_8h_source.html) 第 [309](_ak_common_defs_8h_source.html#l00309) 行定义.