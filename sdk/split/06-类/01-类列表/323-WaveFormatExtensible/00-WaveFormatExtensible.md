# WaveFormatExtensible

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_wave_format_extensible-members.html) |
[类](#nested-classes) |
[Public 属性](#pub-attribs)

WaveFormatExtensible结构体 参考

`#include <AkWavDefs.h>`

类 WaveFormatExtensible 继承关系图:

![](../../../images/struct_wave_format_extensible.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [GUID](struct_wave_format_extensible_1_1_g_u_i_d.html) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| union { |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219)   [wValidBitsPerSample](struct_wave_format_extensible_a66fffe3eef617468cc0274a8cf76653e.html#a66fffe3eef617468cc0274a8cf76653e) |
|  | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219)   [wSamplesPerBlock](struct_wave_format_extensible_a21eabd42fe88ea0a035b766872f4af07.html#a21eabd42fe88ea0a035b766872f4af07) |
|  | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219)   [wReserved](struct_wave_format_extensible_af3d50a6340eac703d4a4bc29cb3a4735.html#af3d50a6340eac703d4a4bc29cb3a4735) |
|  | |
| } | [Samples](struct_wave_format_extensible_ae3ff6a5a7ab053c7c2c99dc85e9f271a.html#ae3ff6a5a7ab053c7c2c99dc85e9f271a) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [dwChannelMask](struct_wave_format_extensible_a0ab1acd573cc198ab1f0ff47b1d9a431.html#a0ab1acd573cc198ab1f0ff47b1d9a431) |
|  | |
| struct [WaveFormatExtensible::GUID](struct_wave_format_extensible_1_1_g_u_i_d.html) | [SubFormat](struct_wave_format_extensible_a6d3efa7484f005c3578839c2fb8f45b0.html#a6d3efa7484f005c3578839c2fb8f45b0) |
|  | |
| - Public 属性 继承自 [WaveFormatEx](struct_wave_format_ex.html) | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [cbSize](struct_wave_format_ex_a0a2212cc53609483df343eb5647ff895.html#a0a2212cc53609483df343eb5647ff895) |
|  | |
| - Public 属性 继承自 [PcmWaveFormat](struct_pcm_wave_format.html) | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [wBitsPerSample](struct_pcm_wave_format_a3d19ba47dca11caa2fae441f5cf1ea94.html#a3d19ba47dca11caa2fae441f5cf1ea94) |
|  | |
| - Public 属性 继承自 [WaveFormat](struct_wave_format.html) | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [wFormatTag](struct_wave_format_a6614dedc4fbe2af294397f87ba04fa85.html#a6614dedc4fbe2af294397f87ba04fa85) |
|  | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [nChannels](struct_wave_format_a86f2e9a79dc040a377fbc799f6a08205.html#a86f2e9a79dc040a377fbc799f6a08205) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [nSamplesPerSec](struct_wave_format_ad19cd9342d86b9176ea244297998a98b.html#ad19cd9342d86b9176ea244297998a98b) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [nAvgBytesPerSec](struct_wave_format_a8fcd34ed99e99bf78c0a15b97afd6b3e.html#a8fcd34ed99e99bf78c0a15b97afd6b3e) |
|  | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [nBlockAlign](struct_wave_format_a4aadd3afb2d0d15f9d76ab3bee6f927e.html#a4aadd3afb2d0d15f9d76ab3bee6f927e) |
|  | |

## 详细描述

在文件 [AkWavDefs.h](_ak_wav_defs_8h_source.html) 第 [130](_ak_wav_defs_8h_source.html#l00130) 行定义.