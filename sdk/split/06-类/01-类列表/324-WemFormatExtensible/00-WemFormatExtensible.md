# WemFormatExtensible

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_wem_format_extensible-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

WemFormatExtensible结构体 参考

`#include <AkWavDefs.h>`

类 WemFormatExtensible 继承关系图:

![](../../../images/struct_wem_format_extensible.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| [AkChannelConfig](struct_ak_channel_config.html) | [GetChannelConfig](struct_wem_format_extensible_a8d18fa0af989bb2ab0720664b4623a70.html#a8d18fa0af989bb2ab0720664b4623a70) () const |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [wSamplesPerBlock](struct_wem_format_extensible_af0e60db639a3b9af2becd078d2b09a57.html#af0e60db639a3b9af2becd078d2b09a57) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uChannelConfig](struct_wem_format_extensible_a60942e9f564efb8f512c3789ce04bb19.html#a60942e9f564efb8f512c3789ce04bb19) |
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

WEM format header: equivalent to [WaveFormatExtensible](struct_wave_format_extensible.html), with an [AkChannelConfig](struct_ak_channel_config.html) instead of dwChannelMask+SubFormat. Codecs that require format-specific chunks should extend this structure.

在文件 [AkWavDefs.h](_ak_wav_defs_8h_source.html) 第 [166](_ak_wav_defs_8h_source.html#l00166) 行定义.