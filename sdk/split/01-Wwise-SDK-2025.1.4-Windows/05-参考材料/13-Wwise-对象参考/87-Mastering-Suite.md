# Mastering Suite

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Mastering Suite

- **Plugin ID**: 186
- **Class ID**: 12189699

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **compressorBand1Attack** | Compressor Attack (Band 1) | Real32 | 0.01 | [ 0.01 , 0.5 ] | true | None | false |
| **compressorBand1Enabled** | Compressor Band 1 Enabled | bool | true | None | true | None | false |
| **compressorBand1Knee** | Compressor Knee (Band 1) | Real32 | 0 | [ 0 , 20 ] | true | None | false |
| **compressorBand1MakeupGain** | Compressor Makeup Gain (Band 1) | Real32 | 0 | [ -18 , 18 ] | true | None | false |
| **compressorBand1Ratio** | Compressor Ratio (Band 1) | Real32 | 1 | [ 1 , 30 ] | true | None | false |
| **compressorBand1Release** | Compressor Release (Band 1) | Real32 | 0.1 | [ 0.01 , 5 ] | true | None | false |
| **compressorBand1Threshold** | Compressor Threshold (Band 1) | Real32 | 0 | [ -60 , 0 ] | true | None | false |
| **compressorBand2Attack** | Compressor Attack (Band 2) | Real32 | 0.01 | [ 0.01 , 0.5 ] | true | None | false |
| **compressorBand2Enabled** | Compressor Band 2 Enabled | bool | true | None | true | None | false |
| **compressorBand2Knee** | Compressor Knee (Band 2) | Real32 | 0 | [ 0 , 20 ] | true | None | false |
| **compressorBand2MakeupGain** | Compressor Makeup Gain (Band 2) | Real32 | 0 | [ -18 , 18 ] | true | None | false |
| **compressorBand2Ratio** | Compressor Ratio (Band 2) | Real32 | 1 | [ 1 , 30 ] | true | None | false |
| **compressorBand2Release** | Compressor Release (Band 2) | Real32 | 0.1 | [ 0.01 , 5 ] | true | None | false |
| **compressorBand2Threshold** | Compressor Threshold (Band 2) | Real32 | 0 | [ -60 , 0 ] | true | None | false |
| **compressorBand3Attack** | Compressor Attack (Band 3) | Real32 | 0.01 | [ 0.01 , 0.5 ] | true | None | false |
| **compressorBand3Enabled** | Compressor Band 3 Enabled | bool | true | None | true | None | false |
| **compressorBand3Knee** | Compressor Knee (Band 3) | Real32 | 0 | [ 0 , 20 ] | true | None | false |
| **compressorBand3MakeupGain** | Compressor Makeup Gain (Band 3) | Real32 | 0 | [ -18 , 18 ] | true | None | false |
| **compressorBand3Ratio** | Compressor Ratio (Band 3) | Real32 | 1 | [ 1 , 30 ] | true | None | false |
| **compressorBand3Release** | Compressor Release (Band 3) | Real32 | 0.1 | [ 0.01 , 5 ] | true | None | false |
| **compressorBand3Threshold** | Compressor Threshold (Band 3) | Real32 | 0 | [ -60 , 0 ] | true | None | false |
| **compressorBand4Attack** | Compressor Attack (Band 4) | Real32 | 0.01 | [ 0.01 , 0.5 ] | true | None | false |
| **compressorBand4Enabled** | Compressor Band 4 Enabled | bool | true | None | true | None | false |
| **compressorBand4Knee** | Compressor Knee (Band 4) | Real32 | 0 | [ 0 , 20 ] | true | None | false |
| **compressorBand4MakeupGain** | Compressor Makeup Gain (Band 4) | Real32 | 0 | [ -18 , 18 ] | true | None | false |
| **compressorBand4Ratio** | Compressor Ratio (Band 4) | Real32 | 1 | [ 1 , 30 ] | true | None | false |
| **compressorBand4Release** | Compressor Release (Band 4) | Real32 | 0.1 | [ 0.01 , 5 ] | true | None | false |
| **compressorBand4Threshold** | Compressor Threshold (Band 4) | Real32 | 0 | [ -60 , 0 ] | true | None | false |
| **compressorCrossoverFrequency1** | Compressor Crossover Frequency 1 | Real32 | 150 | [ 10 , 24000 ] | true | None | false |
| **compressorCrossoverFrequency2** | Compressor Crossover Frequency 2 | Real32 | 1000 | [ 10 , 24000 ] | true | None | false |
| **compressorCrossoverFrequency3** | Compressor Crossover Frequency 3 | Real32 | 6000 | [ 10 , 24000 ] | true | None | false |
| **compressorLinkMode** | Compressor Link Mode | int32 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | No link | | 1 | All channels | | 2 | Partial link | | true | None | false |
| **compressorLinkStereoPairs** | Compressor Stereo Link | bool | false | None | true | None | false |
| **compressorLinkStrength** | Compressor Link Strength | Real32 | 0 | [ 0 , 100 ] | true | None | false |
| **compressorNumBands** | Compressor Band Count | int32 | 4 | [ 1 , 4 ] | true | None | false |
| **limiterAttack** | Limiter Attack | Real32 | 0 | [ 0 , 2.6 ] | true | None | false |
| **limiterLinkChannels** | Limiter Channel Link | bool | true | None | true | None | false |
| **limiterMode** | Limiter Mode | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Soft | | 1 | Hard | | 2 | Advanced | | true | None | false |
| **limiterOutputGain** | Limiter Output Gain | Real32 | 0 | [ 0 , 30 ] | true | None | false |
| **limiterRelease** | Limiter Release | Real32 | 0 | [ 0 , 5 ] | true | None | false |
| **limiterThreshold** | Limiter Threshold | Real32 | 0 | [ -30 , 0 ] | true | None | false |
| **masterVolumeChannel1** | Master Volume Channel Left | Real32 | 0 | [ -100 , 12 ] | true | None | false |
| **masterVolumeChannel10** | Master Volume Channel Height Back Left | Real32 | 0 | [ -100 , 12 ] | true | None | false |
| **masterVolumeChannel11** | Master Volume Channel Height Front Right | Real32 | 0 | [ -100 , 12 ] | true | None | false |
| **masterVolumeChannel12** | Master Volume Channel Low Frequency Effects | Real32 | 0 | [ -100 , 12 ] | true | None | false |
| **masterVolumeChannel2** | Master Volume Channel Right | Real32 | 0 | [ -100 , 12 ] | true | None | false |
| **masterVolumeChannel3** | Master Volume Channel Center | Real32 | 0 | [ -100 , 12 ] | true | None | false |
| **masterVolumeChannel4** | Master Volume Channel Surround Left | Real32 | 0 | [ -100 , 12 ] | true | None | false |
| **masterVolumeChannel5** | Master Volume Channel Surround Right | Real32 | 0 | [ -100 , 12 ] | true | None | false |
| **masterVolumeChannel6** | Master Volume Channel Back Left | Real32 | 0 | [ -100 , 12 ] | true | None | false |
| **masterVolumeChannel7** | Master Volume Channel Back Right | Real32 | 0 | [ -100 , 12 ] | true | None | false |
| **masterVolumeChannel8** | Master Volume Channel Height Front Left | Real32 | 0 | [ -100 , 12 ] | true | None | false |
| **masterVolumeChannel9** | Master Volume Channel Height Front Right | Real32 | 0 | [ -100 , 12 ] | true | None | false |
| **moduleEnableCompressor** | Compressor Module Enabled | bool | true | None | true | None | false |
| **moduleEnableLimiter** | Limiter Module Enabled | bool | true | None | true | None | false |
| **moduleEnableMasterVolume** | Master Volume Module Enabled | bool | true | None | true | None | false |
| **moduleEnableParamEQ** | Param EQ Module Enabled | bool | true | None | true | None | false |
| **paramBand1Enabled** | Param EQ Band 1 Enabled | bool | true | None | true | None | false |
| **paramBand1FilterMode** | Param EQ Filter Mode (Band 1) | int32 | 5 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 1 | Low pass | | 2 | High pass | | 3 | Peak | | 4 | High shelf | | 5 | Low shelf | | 6 | Low pass one-pole | | 7 | High pass one-pole | | true | None | false |
| **paramBand1Frequency** | Param EQ Frequency (Band 1) | Real32 | 100 | [ 10 , 24000 ] | true | None | false |
| **paramBand1Gain** | Param EQ Gain (Band 1) | Real32 | 0 | [ -20 , 20 ] | true | None | false |
| **paramBand1Resonance** | Param EQ Resonance (Band 1) | Real32 | 1 | [ 0.1 , 12 ] | true | None | false |
| **paramBand2Enabled** | Param EQ Band 2 Enabled | bool | true | None | true | None | false |
| **paramBand2FilterMode** | Param EQ Filter Mode (Band 2) | int32 | 3 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 1 | Low pass | | 2 | High pass | | 3 | Peak | | 4 | High shelf | | 5 | Low shelf | | 6 | Low pass one-pole | | 7 | High pass one-pole | | true | None | false |
| **paramBand2Frequency** | Param EQ Frequency (Band 2) | Real32 | 200 | [ 10 , 24000 ] | true | None | false |
| **paramBand2Gain** | Param EQ Gain (Band 2) | Real32 | 0 | [ -20 , 20 ] | true | None | false |
| **paramBand2Resonance** | Param EQ Resonance (Band 2) | Real32 | 1 | [ 0.1 , 12 ] | true | None | false |
| **paramBand3Enabled** | Param EQ Band 3 Enabled | bool | true | None | true | None | false |
| **paramBand3FilterMode** | Param EQ Filter Mode (Band 3) | int32 | 3 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 1 | Low pass | | 2 | High pass | | 3 | Peak | | 4 | High shelf | | 5 | Low shelf | | 6 | Low pass one-pole | | 7 | High pass one-pole | | true | None | false |
| **paramBand3Frequency** | Param EQ Frequency (Band 3) | Real32 | 500 | [ 10 , 24000 ] | true | None | false |
| **paramBand3Gain** | Param EQ Gain (Band 3) | Real32 | 0 | [ -20 , 20 ] | true | None | false |
| **paramBand3Resonance** | Param EQ Resonance (Band 3) | Real32 | 1 | [ 0.1 , 12 ] | true | None | false |
| **paramBand4Enabled** | Param EQ Band 4 Enabled | bool | true | None | true | None | false |
| **paramBand4FilterMode** | Param EQ Filter Mode (Band 4) | int32 | 4 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 1 | Low pass | | 2 | High pass | | 3 | Peak | | 4 | High shelf | | 5 | Low shelf | | 6 | Low pass one-pole | | 7 | High pass one-pole | | true | None | false |
| **paramBand4Frequency** | Param EQ Frequency (Band 4) | Real32 | 1000 | [ 10 , 24000 ] | true | None | false |
| **paramBand4Gain** | Param EQ Gain (Band 4) | Real32 | 0 | [ -20 , 20 ] | true | None | false |
| **paramBand4Resonance** | Param EQ Resonance (Band 4) | Real32 | 1 | [ 0.1 , 12 ] | true | None | false |
| **paramBand5Enabled** | Param EQ Band 5 Enabled | bool | false | None | true | None | false |
| **paramBand5FilterMode** | Param EQ Filter Mode (Band 5) | int32 | 3 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 1 | Low pass | | 2 | High pass | | 3 | Peak | | 4 | High shelf | | 5 | Low shelf | | 6 | Low pass one-pole | | 7 | High pass one-pole | | true | None | false |
| **paramBand5Frequency** | Param EQ Frequency (Band 5) | Real32 | 3000 | [ 10 , 24000 ] | true | None | false |
| **paramBand5Gain** | Param EQ Gain (Band 5) | Real32 | 0 | [ -20 , 20 ] | true | None | false |
| **paramBand5Resonance** | Param EQ Resonance (Band 5) | Real32 | 1 | [ 0.1 , 12 ] | true | None | false |
| **paramBand6Enabled** | Param EQ Band 6 Enabled | bool | false | None | true | None | false |
| **paramBand6FilterMode** | Param EQ Filter Mode (Band 6) | int32 | 3 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 1 | Low pass | | 2 | High pass | | 3 | Peak | | 4 | High shelf | | 5 | Low shelf | | 6 | Low pass one-pole | | 7 | High pass one-pole | | true | None | false |
| **paramBand6Frequency** | Param EQ Frequency (Band 6) | Real32 | 6000 | [ 10 , 24000 ] | true | None | false |
| **paramBand6Gain** | Param EQ Gain (Band 6) | Real32 | 0 | [ -20 , 20 ] | true | None | false |
| **paramBand6Resonance** | Param EQ Resonance (Band 6) | Real32 | 1 | [ 0.1 , 12 ] | true | None | false |
| **paramEqNumBands** | Param EQ Band Count | int32 | 4 | [ 1 , 6 ] | true | None | false |