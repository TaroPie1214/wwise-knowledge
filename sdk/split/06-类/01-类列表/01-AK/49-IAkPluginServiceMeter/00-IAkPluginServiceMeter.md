# IAkPluginServiceMeter

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPluginServiceMeter](class_a_k_1_1_i_ak_plugin_service_meter.html)

[所有成员列表](class_a_k_1_1_i_ak_plugin_service_meter-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkPluginServiceMeter类 参考abstract

Interface for the "Meter" plug-in service, to handle metering of signals in various ways
[更多...](class_a_k_1_1_i_ak_plugin_service_meter.html#details)

`#include <IAkPluginServiceMeter.h>`

类 AK::IAkPluginServiceMeter 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_plugin_service_meter.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual AkMeterCtx \* | [InitMeter](class_a_k_1_1_i_ak_plugin_service_meter_adf42f7d1d35bffcd97b8aec573fc3094.html#adf42f7d1d35bffcd97b8aec573fc3094) ([AkChannelConfig](struct_ak_channel_config.html) in\_channelCfg, [AkMeteringFlags](_ak_enums_8h_a29f798f121cb4138f9c92f8421d5e729.html#a29f798f121cb4138f9c92f8421d5e729) in\_meterFlags)=0 |
|  | |
| virtual void | [TermMeter](class_a_k_1_1_i_ak_plugin_service_meter_ad22a7cf491ae60098088b2650d5dfa40.html#ad22a7cf491ae60098088b2650d5dfa40) (AkMeterCtx \*io\_pMeter)=0 |
|  | |
| virtual [AK::AkMetering](struct_a_k_1_1_ak_metering.html) \* | [MeterBuffer](class_a_k_1_1_i_ak_plugin_service_meter_aefff7a4de4806261c24e8cb27278f0f7.html#aefff7a4de4806261c24e8cb27278f0f7) (AkMeterCtx \*io\_pMeter, [AkAudioBuffer](class_ak_audio_buffer.html) \*in\_pAudioBuffer, [AkRamp](struct_ak_ramp.html) in\_gain)=0 |
|  | |
| virtual void | [ComputePeaks](class_a_k_1_1_i_ak_plugin_service_meter_a5e36986e729d24b682c12bb41252e243.html#a5e36986e729d24b682c12bb41252e243) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \*out\_pfChannelPeaks, const [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \*\*in\_ppfData, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uMaxFrames, [AkRamp](struct_ak_ramp.html) in\_gain)=0 |
|  | |
| virtual void | [ComputeMeanSquares](class_a_k_1_1_i_ak_plugin_service_meter_a58fb1f1e93a8fd06fd0e6e2d418faabf.html#a58fb1f1e93a8fd06fd0e6e2d418faabf) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \*out\_pfChannelMeanSquares, const [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) \*\*in\_ppfData, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uMaxFrames, [AkRamp](struct_ak_ramp.html) in\_gain)=0 |
|  | |
| virtual [AK::AkMetering](struct_a_k_1_1_ak_metering.html) \* | [GetMetering](class_a_k_1_1_i_ak_plugin_service_meter_ac59adb44ddbec78b98de0ab4bbea1f8d.html#ac59adb44ddbec78b98de0ab4bbea1f8d) (AkMeterCtx \*io\_pMeter)=0 |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkPluginServiceMeter](class_a_k_1_1_i_ak_plugin_service_meter_a285b656d1e552aeec160fb68ba266eea.html#a285b656d1e552aeec160fb68ba266eea) () |
|  | |
| - Protected 成员函数 继承自 [AK::IAkPluginService](class_a_k_1_1_i_ak_plugin_service.html) | |
| virtual | [~IAkPluginService](class_a_k_1_1_i_ak_plugin_service_af880be6eab8f4f3cd124ec8db8b562de.html#af880be6eab8f4f3cd124ec8db8b562de) () |
|  | |

## 详细描述

Interface for the "Meter" plug-in service, to handle metering of signals in various ways

在文件 [IAkPluginServiceMeter.h](_i_ak_plugin_service_meter_8h_source.html) 第 [42](_i_ak_plugin_service_meter_8h_source.html#l00042) 行定义.