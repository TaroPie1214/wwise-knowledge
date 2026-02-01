# AkWavDefs.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[枚举](#enum-members) |
[函数](#func-members) |
[变量](#var-members)

AkWavDefs.h 文件参考

`#include <AK/SoundEngine/Common/AkSpeakerConfig.h>`  
`#include <AK/SoundEngine/Common/AkTypes.h>`  
`#include <string.h>`

[浏览源代码.](_ak_wav_defs_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkChunkHeader](struct_ak_chunk_header.html) |
|  | Standard WAV chunk header [更多...](struct_ak_chunk_header.html#details) |
|  | |
| struct | [ChunkSize64](struct_chunk_size64.html) |
|  | |
| struct | [DataSize64](struct_data_size64.html) |
|  | |
| struct | [WaveFormat](struct_wave_format.html) |
|  | |
| struct | [PcmWaveFormat](struct_pcm_wave_format.html) |
|  | |
| struct | [WaveFormatEx](struct_wave_format_ex.html) |
|  | |
| struct | [WaveFormatExtensible](struct_wave_format_extensible.html) |
|  | |
| struct | [WaveFormatExtensible::GUID](struct_wave_format_extensible_1_1_g_u_i_d.html) |
|  | |
| struct | [WemFormatExtensible](struct_wem_format_extensible.html) |
|  | |
| struct | [SamplerChunk](struct_sampler_chunk.html) |
|  | |
| struct | [SampleLoop](struct_sample_loop.html) |
|  | |
| struct | [WaveCue](struct_wave_cue.html) |
|  | |
| struct | [ChnaAudioId](struct_chna_audio_id.html) |
|  | |
| struct | [ChnaChunk](struct_chna_chunk.html) |
|  | |
| struct | [AkWAVStructs::AkWaveFileHeader](struct_ak_w_a_v_structs_1_1_ak_wave_file_header.html) |
|  | |
| struct | [AkWAVStructs::AkSamplerOneLoop](struct_ak_w_a_v_structs_1_1_ak_sampler_one_loop.html) |
|  | |
| struct | [AkWAVStructs::AkWaveMarker](struct_ak_w_a_v_structs_1_1_ak_wave_marker.html) |
|  | |
| struct | [AkWAVStructs::IrMetadata](struct_ak_w_a_v_structs_1_1_ir_metadata.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
|  | [AkWAVStructs](namespace_ak_w_a_v_structs.html) |
|  | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |

|  |  |
| --- | --- |
| 枚举 | |
| enum | [AkWAVStructs::ChunkType](namespace_ak_w_a_v_structs_a616c8f03b14d6a2139cb3c551312069f.html#a616c8f03b14d6a2139cb3c551312069f) {     [AkWAVStructs::ChunkType\_FMT](namespace_ak_w_a_v_structs_a616c8f03b14d6a2139cb3c551312069f.html#a616c8f03b14d6a2139cb3c551312069fa9e42773858e1d5fa2ecd5afd33422969) = 1 << 0, [AkWAVStructs::ChunkType\_DATA](namespace_ak_w_a_v_structs_a616c8f03b14d6a2139cb3c551312069f.html#a616c8f03b14d6a2139cb3c551312069fa69fe052c01b68f3087966fe1a865753a) = 1 << 1, [AkWAVStructs::ChunkType\_SMPL](namespace_ak_w_a_v_structs_a616c8f03b14d6a2139cb3c551312069f.html#a616c8f03b14d6a2139cb3c551312069fa6ba8afe12fc7c28acdd85177489195c4) = 1 << 2, [AkWAVStructs::ChunkType\_CUE](namespace_ak_w_a_v_structs_a616c8f03b14d6a2139cb3c551312069f.html#a616c8f03b14d6a2139cb3c551312069fa7049f9ebe9fdcefba8277ce2f3b8f630) = 1 << 3,     [AkWAVStructs::ChunkType\_LIST](namespace_ak_w_a_v_structs_a616c8f03b14d6a2139cb3c551312069f.html#a616c8f03b14d6a2139cb3c551312069face9e9c3f4a7df23da08483d070aea216) = 1 << 4, [AkWAVStructs::ChunkType\_IRMD](namespace_ak_w_a_v_structs_a616c8f03b14d6a2139cb3c551312069f.html#a616c8f03b14d6a2139cb3c551312069fa9ec4e7208cf998c566f2af18f7664566) = 1 << 5, [AkWAVStructs::ChunkType\_HASH](namespace_ak_w_a_v_structs_a616c8f03b14d6a2139cb3c551312069f.html#a616c8f03b14d6a2139cb3c551312069faedc4567866c39b411c91377093c2f0af) = 1 << 7, [AkWAVStructs::ChunkType\_JUNK](namespace_ak_w_a_v_structs_a616c8f03b14d6a2139cb3c551312069f.html#a616c8f03b14d6a2139cb3c551312069fac6858be32432661870e5a54e08aa10b3) = 1 << 8,     [AkWAVStructs::ChunkType\_CHNA](namespace_ak_w_a_v_structs_a616c8f03b14d6a2139cb3c551312069f.html#a616c8f03b14d6a2139cb3c551312069fa18da978f6ab2998f94c39e44b90a8a6c) = 1 << 9, [AkWAVStructs::ChunkType\_AXML](namespace_ak_w_a_v_structs_a616c8f03b14d6a2139cb3c551312069f.html#a616c8f03b14d6a2139cb3c551312069fa6d6361aab061064b6d73456c91f6c3f1) = 1 << 10, [AkWAVStructs::ChunkType\_AKDM](namespace_ak_w_a_v_structs_a616c8f03b14d6a2139cb3c551312069f.html#a616c8f03b14d6a2139cb3c551312069faf7e260a45c7cd0b44c1fda8e50873964) = 1 << 11, [AkWAVStructs::ChunkType\_IXML](namespace_ak_w_a_v_structs_a616c8f03b14d6a2139cb3c551312069f.html#a616c8f03b14d6a2139cb3c551312069fa7df0ea49a36edc3884d769bbb93b2220) = 1 << 12,     [AkWAVStructs::ChunkType\_Required](namespace_ak_w_a_v_structs_a616c8f03b14d6a2139cb3c551312069f.html#a616c8f03b14d6a2139cb3c551312069fa186ef278b8acc7d7538cd32d8785b4c5) = ChunkType\_FMT | ChunkType\_DATA, [AkWAVStructs::ChunkType\_ALL](namespace_ak_w_a_v_structs_a616c8f03b14d6a2139cb3c551312069f.html#a616c8f03b14d6a2139cb3c551312069fab967ea9b1534f260d6faf0ae2fe0ee00) = 0xffffffff   } |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| [AkChannelConfig](struct_ak_channel_config.html) | [AK::SetChannelConfigFromWaveFormatExtensible](namespace_a_k_a8871e2566c734001c2a9499368894df4.html#a8871e2566c734001c2a9499368894df4) (const [WaveFormatExtensible](struct_wave_format_extensible.html) &in\_wfmext) |
|  | |

|  |  |
| --- | --- |
| 变量 | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [RIFXChunkId](_ak_wav_defs_8h_ab6561ee9a6de1d401c802e8fdd7646d3.html#ab6561ee9a6de1d401c802e8fdd7646d3) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('R', 'I', 'F', 'X') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [RIFFChunkId](_ak_wav_defs_8h_a26d25269199ab3653af1df7f812e4f66.html#a26d25269199ab3653af1df7f812e4f66) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('R', 'I', 'F', 'F') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [RF64ChunkId](_ak_wav_defs_8h_aa054ad478cc788629c07c30272cf0331.html#aa054ad478cc788629c07c30272cf0331) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('R', 'F', '6', '4') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [BW64ChunkId](_ak_wav_defs_8h_a4bb17560226181309b1493707f6f825f.html#a4bb17560226181309b1493707f6f825f) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('B', 'W', '6', '4') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [ds64ChunkId](_ak_wav_defs_8h_a84a4a4379bca21f764c0e1c29199e94d.html#a84a4a4379bca21f764c0e1c29199e94d) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('d', 's', '6', '4') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [WAVEChunkId](_ak_wav_defs_8h_a5ee37bc5853a8c447b424e2820f77f9c.html#a5ee37bc5853a8c447b424e2820f77f9c) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('W', 'A', 'V', 'E') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [PLUGINChunkId](_ak_wav_defs_8h_a28ad80d02ee657c90ad1cf43ec47ef9d.html#a28ad80d02ee657c90ad1cf43ec47ef9d) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('P', 'L', 'U', 'G') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [MIDIChunkId](_ak_wav_defs_8h_ac99de6b0cc64fe6402dcee8481bf44c0.html#ac99de6b0cc64fe6402dcee8481bf44c0) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('M', 'I', 'D', 'I') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [fmtChunkId](_ak_wav_defs_8h_afd8a3ec24ef2c9b82095e9541332f881.html#afd8a3ec24ef2c9b82095e9541332f881) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('f', 'm', 't', ' ') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [dataChunkId](_ak_wav_defs_8h_a8c2f6d4c1bbf4f89bd1c69267300177a.html#a8c2f6d4c1bbf4f89bd1c69267300177a) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('d', 'a', 't', 'a') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [cueChunkId](_ak_wav_defs_8h_afae88602eb6ac8423955d930df29962c.html#afae88602eb6ac8423955d930df29962c) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('c', 'u', 'e', ' ') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [LISTChunkId](_ak_wav_defs_8h_a3ceeab91ddc8f5f798b9f67fde098476.html#a3ceeab91ddc8f5f798b9f67fde098476) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('L', 'I', 'S', 'T') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [adtlChunkId](_ak_wav_defs_8h_a69ecefda2d39d1aea18ef2c4d89d7a8c.html#a69ecefda2d39d1aea18ef2c4d89d7a8c) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('a', 'd', 't', 'l') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [lablChunkId](_ak_wav_defs_8h_ae21c6013eb329e307492fd8853a58c4b.html#ae21c6013eb329e307492fd8853a58c4b) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('l', 'a', 'b', 'l') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [smplChunkId](_ak_wav_defs_8h_a22affaeb11878aac8c4a6802cb50728e.html#a22affaeb11878aac8c4a6802cb50728e) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('s', 'm', 'p', 'l') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [junkChunkId](_ak_wav_defs_8h_a7dfde78d3da3aea09178fdea2461cc00.html#a7dfde78d3da3aea09178fdea2461cc00) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('j', 'u', 'n', 'k') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [axmlChunkId](_ak_wav_defs_8h_ae85f12a458a96fc6b06b71f3217ef70a.html#ae85f12a458a96fc6b06b71f3217ef70a) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('a', 'x', 'm', 'l') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [chnaChunkId](_ak_wav_defs_8h_a98c491c1c92b322c11cf348b095df62e.html#a98c491c1c92b322c11cf348b095df62e) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('c', 'h', 'n', 'a') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [iXMLChunkId](_ak_wav_defs_8h_a96f0e0b2d94a435ecf1e7b332c516656.html#a96f0e0b2d94a435ecf1e7b332c516656) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('i', 'X', 'M', 'L') |
|  | |
| constexpr [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [extensibleWavFormat](_ak_wav_defs_8h_aacaab399e8b149098daddb5f42097f6e.html#aacaab399e8b149098daddb5f42097f6e) = 0xFFFE |
|  | |
| constexpr [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [floatWavFormat](_ak_wav_defs_8h_a0f1faf1220bbc4b79b5829cb5199c27d.html#a0f1faf1220bbc4b79b5829cb5199c27d) = 0x0003 |
|  | |
| constexpr [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [pcmWavFormat](_ak_wav_defs_8h_a77a3c4b1228bc56ddbe89267caa877dd.html#a77a3c4b1228bc56ddbe89267caa877dd) = 0x0001 |
|  | |
| constexpr [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [kWavHashSize](_ak_wav_defs_8h_a91c6bf29753f0abf79b6117db7795679.html#a91c6bf29753f0abf79b6117db7795679) = 16 |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [akdChunkId](_ak_wav_defs_8h_a623578e08a6a5466a73dc3db37688b69.html#a623578e08a6a5466a73dc3db37688b69) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('a', 'k', 'd', ' ') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [hashChunkId](_ak_wav_defs_8h_a618a0e5c9ce00c86f1dade75cfb1b9a9.html#a618a0e5c9ce00c86f1dade75cfb1b9a9) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('h', 'a', 's', 'h') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [seekChunkId](_ak_wav_defs_8h_a5cf0bbc770b4fa27a51f9d08098d082f.html#a5cf0bbc770b4fa27a51f9d08098d082f) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('s', 'e', 'e', 'k') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [irmdChunkId](_ak_wav_defs_8h_a40955481bed6ba295d5c1f1f8b3f1e41.html#a40955481bed6ba295d5c1f1f8b3f1e41) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('i', 'r', 'm', 'd') |
|  | |
| constexpr [AkFourcc](_platforms_2_windows_2_ak_types_8h_a5d907bb8f0cf3bd704ed1d8dcc324e31.html#a5d907bb8f0cf3bd704ed1d8dcc324e31) | [akdmChunkId](_ak_wav_defs_8h_a342a0ce5148e5f40debac9bfc028bfbe.html#a342a0ce5148e5f40debac9bfc028bfbe) = [AkmmioFOURCC](_platforms_2_windows_2_ak_types_8h_a0cf9803e16149592491e424d2fc4f042.html#a0cf9803e16149592491e424d2fc4f042)('a', 'k', 'd', 'm') |
|  | |
| static constexpr [WaveFormatExtensible::GUID](struct_wave_format_extensible_1_1_g_u_i_d.html) | [G\_KSDATAFORMAT\_SUBTYPE\_PCM](_ak_wav_defs_8h_a6e6fe5e8374013529333dc64365d0840.html#a6e6fe5e8374013529333dc64365d0840) = { 0x0001, 0x0000, 0x0010, { 0x80, 0x00, 0x00, 0xaa, 0x00, 0x38, 0x9b, 0x71 } } |
|  | |
| static constexpr [WaveFormatExtensible::GUID](struct_wave_format_extensible_1_1_g_u_i_d.html) | [G\_KSDATAFORMAT\_SUBTYPE\_IEEE\_FLOAT](_ak_wav_defs_8h_a56f5def93aa32e4bf146c732cae5c69c.html#a56f5def93aa32e4bf146c732cae5c69c) = { 0x0003, 0x0000, 0x0010, { 0x80, 0x00, 0x00, 0xaa, 0x00, 0x38, 0x9b, 0x71 } } |
|  | |

## 详细描述

Basic definitions for WAV / WEM file parsers.

在文件 [AkWavDefs.h](_ak_wav_defs_8h_source.html) 中定义.