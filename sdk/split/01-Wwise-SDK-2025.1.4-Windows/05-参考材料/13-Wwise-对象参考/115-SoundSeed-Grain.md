# SoundSeed Grain

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

SoundSeed Grain

- **Plugin ID**: 183
- **Class ID**: 11993090

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Amplitude** | Amplitude | Real32 | 100 | [ 0 , 100 ] | true | Additive | false |
| **AmplitudeMod1Depth** | Amplitude Mod 1 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **AmplitudeMod1Quantization** | Amplitude Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **AmplitudeMod2Depth** | Amplitude Mod 2 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **AmplitudeMod2Quantization** | Amplitude Mod 2 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **AmplitudeMod3Depth** | Amplitude Mod 3 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **AmplitudeMod3Quantization** | Amplitude Mod 3 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **AmplitudeMod4Depth** | Amplitude Mod 4 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **AmplitudeMod4Quantization** | Amplitude Mod 4 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **Attack** | Attack | Real32 | 10 | [ 0 , 5000 ] | true | Additive | false |
| **AttackMod1Depth** | Attack Mod 1 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **AttackMod1Quantization** | Attack Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **AttackMod2Depth** | Attack Mod 2 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **AttackMod2Quantization** | Attack Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **AttackMod3Depth** | Attack Mod 3 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **AttackMod3Quantization** | Attack Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **AttackMod4Depth** | Attack Mod 4 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **AttackMod4Quantization** | Attack Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **Azimuth** | Azimuth | Real32 | 0 | [ -180 , 180 ] | true | Additive | false |
| **AzimuthMod1Depth** | Azimuth Mod 1 Amount | Real32 | 0 | [ 0 , 180 ] | true | Additive | false |
| **AzimuthMod1Quantization** | Azimuth Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **AzimuthMod2Depth** | Azimuth Mod 2 Amount | Real32 | 0 | [ 0 , 180 ] | true | Additive | false |
| **AzimuthMod2Quantization** | Azimuth Mod 2 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **AzimuthMod3Depth** | Azimuth Mod 3 Amount | Real32 | 0 | [ 0 , 180 ] | true | Additive | false |
| **AzimuthMod3Quantization** | Azimuth Mod 3 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **AzimuthMod4Depth** | Azimuth Mod 4 Amount | Real32 | 0 | [ 0 , 180 ] | true | Additive | false |
| **AzimuthMod4Quantization** | Azimuth Mod 4 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **Duration** | Duration | Real32 | 1000 | [ 0.02 , 10000.0 ] | true | Additive | false |
| **DurationLink** | Duration Link | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Duration Multiplier | | 1 | Duration | | 2 | MIDI Duration | | true | None | false |
| **DurationMod1Depth** | Duration Mod 1 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **DurationMod1Quantization** | Duration Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **DurationMod2Depth** | Duration Mod 2 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **DurationMod2Quantization** | Duration Mod 2 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **DurationMod3Depth** | Duration Mod 3 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **DurationMod3Quantization** | Duration Mod 3 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **DurationMod4Depth** | Duration Mod 4 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **DurationMod4Quantization** | Duration Mod 4 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **DurationMultiplier** | Duration Multiplier | Real32 | 1 | [ 0.001 , 1000 ] | true | Additive | false |
| **DurationMultiplierMod1Depth** | Duration Multiplier Mod 1 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **DurationMultiplierMod1Quantization** | Duration Multiplier Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **DurationMultiplierMod2Depth** | Duration Multiplier Mod 2 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **DurationMultiplierMod2Quantization** | Duration Multiplier Mod 2 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **DurationMultiplierMod3Depth** | Duration Multiplier Mod 3 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **DurationMultiplierMod3Quantization** | Duration Multiplier Mod 3 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **DurationMultiplierMod4Depth** | Duration Multiplier Mod 4 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **DurationMultiplierMod4Quantization** | Duration Multiplier Mod 4 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **Elevation** | Elevation | Real32 | 0 | [ -90 , 90 ] | true | Additive | false |
| **ElevationMod1Depth** | Elevation Mod 1 Amount | Real32 | 0 | [ 0 , 90.0 ] | true | Additive | false |
| **ElevationMod1Quantization** | Elevation Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **ElevationMod2Depth** | Elevation Mod 2 Amount | Real32 | 0 | [ 0 , 90.0 ] | true | Additive | false |
| **ElevationMod2Quantization** | Elevation Mod 2 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **ElevationMod3Depth** | Elevation Mod 3 Amount | Real32 | 0 | [ 0 , 90.0 ] | true | Additive | false |
| **ElevationMod3Quantization** | Elevation Mod 3 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **ElevationMod4Depth** | Elevation Mod 4 Amount | Real32 | 0 | [ 0 , 90.0 ] | true | Additive | false |
| **ElevationMod4Quantization** | Elevation Mod 4 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **EnvelopeType** | Grain Envelope Shape | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Linear | | 1 | Constant Power | | 2 | Exponential | | 3 | Raised Cosine | | true | None | false |
| **FilterFreq** | Filter Cutoff | Real32 | 20000 | [ 20 , 20000 ] | true | Exclusive | false |
| **FilterFreqMod1Depth** | Filter Cutoff Mod 1 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **FilterFreqMod1Quantization** | Filter Cutoff Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **FilterFreqMod2Depth** | Filter Cutoff Mod 2 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **FilterFreqMod2Quantization** | Filter Cutoff Mod 2 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **FilterFreqMod3Depth** | Filter Cutoff Mod 3 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **FilterFreqMod3Quantization** | Filter Cutoff Mod 3 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **FilterFreqMod4Depth** | Filter Cutoff Mod 4 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **FilterFreqMod4Quantization** | Filter Cutoff Mod 4 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **FilterQ** | Filter Q | Real32 | 0.707 | [ 0.1 , 100 ] | true | Additive | false |
| **FilterQMod1Depth** | Filter Q Mod 1 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **FilterQMod1Quantization** | Filter Q Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **FilterQMod2Depth** | Filter Q Mod 2 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **FilterQMod2Quantization** | Filter Q Mod 2 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **FilterQMod3Depth** | Filter Q Mod 3 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **FilterQMod3Quantization** | Filter Q Mod 3 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **FilterQMod4Depth** | Filter Q Mod 4 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **FilterQMod4Quantization** | Filter Q Mod 4 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **FilterType** | Filter Type | int32 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | LPF6 | | 1 | LPF12 | | 2 | HPF6 | | 3 | HPF12 | | 4 | BP | | true | None | false |
| **GrainRate** | Emissions per Second | Real32 | 1 | [ 0.02 , 20000 ] | true | Exclusive | false |
| **GrainRateMod1Depth** | Emissions per Second Mod 1 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **GrainRateMod1Quantization** | Emissions per Second Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **GrainRateMod2Depth** | Emissions per Second Mod 2 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **GrainRateMod2Quantization** | Emissions per Second Mod 2 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **GrainRateMod3Depth** | Emissions per Second Mod 3 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **GrainRateMod3Quantization** | Emissions per Second Mod 3 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **GrainRateMod4Depth** | Emissions per Second Mod 4 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **GrainRateMod4Quantization** | Emissions per Second Mod 4 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **GrainTime** | Time between Emissions | Real32 | 1000 | [ 0.05 , 50000 ] | true | Exclusive | false |
| **GrainTimeMod1Depth** | Time Between Emissions Mod 1 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **GrainTimeMod1Quantization** | Time Between Emissions Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **GrainTimeMod2Depth** | Time Between Emissions Mod 2 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **GrainTimeMod2Quantization** | Time Between Emissions Mod 2 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **GrainTimeMod3Depth** | Time Between Emissions Mod 3 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **GrainTimeMod3Quantization** | Time Between Emissions Mod 3 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **GrainTimeMod4Depth** | Time Between Emissions Mod 4 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **GrainTimeMod4Quantization** | Time Between Emissions Mod 4 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **MarkerSelect** | Position | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **MarkerSelectMod1Depth** | Position Mod 1 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **MarkerSelectMod1Quantization** | Position Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **MarkerSelectMod2Depth** | Position Mod 2 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **MarkerSelectMod2Quantization** | Position Mod 2 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **MarkerSelectMod3Depth** | Position Mod 3 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **MarkerSelectMod3Quantization** | Position Mod 3 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **MarkerSelectMod4Depth** | Position Mod 4 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **MarkerSelectMod4Quantization** | Position Mod 4 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **MaxNumGrains** | Max Number of Grains | int32 | 256 | [ 1 , 2048 ] | true | None | false |
| **MidiMapTranspose** | Map MIDI to Grain Pitch | bool | 0 | None | true | None | false |
| **ModAmount1** | Modulator 1 Output | Real32 | 100 | [ -100 , 100 ] | true | Additive | false |
| **ModAmount2** | Modulator 2 Output | Real32 | 100 | [ -100 , 100 ] | true | Additive | false |
| **ModAmount3** | Modulator 3 Output | Real32 | 100 | [ -100 , 100 ] | true | Additive | false |
| **ModAmount4** | Modulator 4 Output | Real32 | 100 | [ -100 , 100 ] | true | Additive | false |
| **ModPeriod1** | Modulator 1 Period | Real32 | 1000 | [ 0.05 , 120000 ] | true | Exclusive | false |
| **ModPeriod2** | Modulator 2 Period | Real32 | 1000 | [ 0.05 , 120000 ] | true | Exclusive | false |
| **ModPeriod3** | Modulator 3 Period | Real32 | 1000 | [ 0.05 , 120000 ] | true | Exclusive | false |
| **ModPeriod4** | Modulator 4 Period | Real32 | 1000 | [ 0.05 , 120000 ] | true | Exclusive | false |
| **ModRate1** | Modulator 1 Frequency | Real32 | 20000 | [ 0.008 , 20000 ] | true | Exclusive | false |
| **ModRate2** | Modulator 2 Frequency | Real32 | 20000 | [ 0.008 , 20000 ] | true | Exclusive | false |
| **ModRate3** | Modulator 3 Frequency | Real32 | 20000 | [ 0.008 , 20000 ] | true | Exclusive | false |
| **ModRate4** | Modulator 4 Frequency | Real32 | 20000 | [ 0.008 , 20000 ] | true | Exclusive | false |
| **ModSelect1** | Modulator 1 Time/Freq | int32 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Period | | 1 | Frequency | | true | None | false |
| **ModSelect2** | Modulator 2 Time/Freq | int32 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Period | | 1 | Frequency | | true | None | false |
| **ModSelect3** | Modulator 3 Time/Freq | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Period | | 1 | Frequency | | true | None | false |
| **ModSelect4** | Modulator 4 Time/Freq | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Period | | 1 | Frequency | | true | None | false |
| **ModWaveform1** | Modulator 1 Waveform | int32 | 5 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Sine | | 1 | Triangle | | 2 | Square | | 3 | Saw up | | 4 | Saw down | | 5 | Random | | 6 | Sine+ | | 7 | Triangle+ | | 8 | Square+ | | 9 | Saw up+ | | 10 | Saw down+ | | 11 | Random+ | | true | Exclusive | false |
| **ModWaveform2** | Modulator 2 Waveform | int32 | 5 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Sine | | 1 | Triangle | | 2 | Square | | 3 | Saw up | | 4 | Saw down | | 5 | Random | | 6 | Sine+ | | 7 | Triangle+ | | 8 | Square+ | | 9 | Saw up+ | | 10 | Saw down+ | | 11 | Random+ | | true | Exclusive | false |
| **ModWaveform3** | Modulator 3 Waveform | int32 | 9 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Sine | | 1 | Triangle | | 2 | Square | | 3 | Saw up | | 4 | Saw down | | 5 | Random | | 6 | Sine+ | | 7 | Triangle+ | | 8 | Square+ | | 9 | Saw up+ | | 10 | Saw down+ | | 11 | Random+ | | true | Exclusive | false |
| **ModWaveform4** | Modulator 4 Waveform | int32 | 9 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Sine | | 1 | Triangle | | 2 | Square | | 3 | Saw up | | 4 | Saw down | | 5 | Random | | 6 | Sine+ | | 7 | Triangle+ | | 8 | Square+ | | 9 | Saw up+ | | 10 | Saw down+ | | 11 | Random+ | | true | Exclusive | false |
| **Offset** | Offset | Real32 | 0 | [ -100 , 100 ] | true | Additive | false |
| **OffsetMod1Depth** | Offset Mod 1 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **OffsetMod1Quantization** | Offset Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **OffsetMod2Depth** | Offset Mod 2 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **OffsetMod2Quantization** | Offset Mod 2 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **OffsetMod3Depth** | Offset Mod 3 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **OffsetMod3Quantization** | Offset Mod 3 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **OffsetMod4Depth** | Offset Mod 4 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **OffsetMod4Quantization** | Offset Mod 4 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **OutputChannelConfig** | Output Config | int32 | 16641 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 16641 | Mono | | 12546 | Stereo | | 28931 | 3.0 | | 6304004 | 4.0 | | 6353158 | 5.1 | | 6549768 | 7.1 | | 90239240 | 5.1.2 | | 761327882 | 5.1.4 | | 90435850 | 7.1.2 | | 761524492 | 7.1.4 | | 516 | Ambisonics 1st order | | 521 | Ambisonics 2nd order | | 528 | Ambisonics 3rd order | | 537 | Ambisonics 4th order | | 548 | Ambisonics 5th order | | 769716491 | Auro 10.1 | | 803270924 | Auro 11.1 | | 803467534 | Auro 13.1 | | 33025 | LFE | | true | None | false |
| **OutputLevel** | Output Level | Real32 | 0 | [ -96 , 24 ] | true | Additive | false |
| **PositioningSelect** | Channels | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Direct Speaker Assignment | | 1 | 3D Spatialization | | true | None | false |
| **QuantizeToMarkers** | Snap to markers | bool | 0 | None | true | None | false |
| **Release** | Release | Real32 | 10 | [ 0 , 5000 ] | true | Additive | false |
| **ReleaseMod1Depth** | Release Mod 1 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **ReleaseMod1Quantization** | Release Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **ReleaseMod2Depth** | Release Mod 2 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **ReleaseMod2Quantization** | Release Mod 2 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **ReleaseMod3Depth** | Release Mod 3 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **ReleaseMod3Quantization** | Release Mod 3 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **ReleaseMod4Depth** | Release Mod 4 Amount | Real32 | 0 | [ -10 , 10 ] | true | Additive | false |
| **ReleaseMod4Quantization** | Release Mod 4 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **SelectFreqTimeGrain** | Select Freq/Time | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Time between Emissions | | 1 | Emissions per Second | | 2 | MIDI Emissions per Second | | true | None | false |
| **Speed** | Speed | Real32 | 1 | [ -4 , 4 ] | true | Additive | false |
| **SpeedMod1Depth** | Speed Mod 1 Amount | Real32 | 0 | [ 0 , 4 ] | true | Additive | false |
| **SpeedMod1Quantization** | Speed Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **SpeedMod2Depth** | Speed Mod 2 Amount | Real32 | 0 | [ 0 , 4 ] | true | Additive | false |
| **SpeedMod2Quantization** | Speed Mod 2 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **SpeedMod3Depth** | Speed Mod 3 Amount | Real32 | 0 | [ 0 , 4 ] | true | Additive | false |
| **SpeedMod3Quantization** | Speed Mod 3 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **SpeedMod4Depth** | Speed Mod 4 Amount | Real32 | 0 | [ 0 , 4 ] | true | Additive | false |
| **SpeedMod4Quantization** | Speed Mod 4 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **Spread** | Spread | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **SpreadMod1Depth** | Spread Mod 1 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **SpreadMod1Quantization** | Spread Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **SpreadMod2Depth** | Spread Mod 2 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **SpreadMod2Quantization** | Spread Mod 2 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **SpreadMod3Depth** | Spread Mod 3 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **SpreadMod3Quantization** | Spread Mod 3 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **SpreadMod4Depth** | Spread Mod 4 Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **SpreadMod4Quantization** | Spread Mod 4 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | true | None | false |
| **Transpose** | Pitch | Real32 | 0 | [ -4800 , 4800 ] | true | Additive | false |
| **TransposeMod1Depth** | Pitch Mod 1 Amount | Real32 | 0 | [ 0 , 4800 ] | true | Additive | false |
| **TransposeMod1Quantization** | Pitch Mod 1 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **TransposeMod2Depth** | Pitch Mod 2 Amount | Real32 | 0 | [ 0 , 4800 ] | true | Additive | false |
| **TransposeMod2Quantization** | Pitch Mod 2 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **TransposeMod3Depth** | Pitch Mod 3 Amount | Real32 | 0 | [ 0 , 4800 ] | true | Additive | false |
| **TransposeMod3Quantization** | Pitch Mod 3 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **TransposeMod4Depth** | Pitch Mod 4 Amount | Real32 | 0 | [ 0 , 4800 ] | true | Additive | false |
| **TransposeMod4Quantization** | Pitch Mod 4 Quantization | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | (-1, 1) | | 2 | (-1, 0, 1) | | 3 | Chromatic | | 4 | Major | | 5 | Minor | | 6 | Pentatonic | | true | None | false |
| **TransposeRoot** | Root MIDI Note | int32 | 60 | [ 0 , 127 ] | true | None | false |
| **WindowMode** | Window Mode | int32 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Independent Attack and Release | | 1 | Release Same as Attack | | true | None | false |