# Wwise Convolution Reverb

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Convolution Reverb

- **Plugin ID**: 127
- **Class ID**: 8323075

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **AlgoTypeSelect** | Reverb Type | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Reverb | | 1 | Filter | | true | None | false |
| **CenterLevel** | Reverb Center Level | Real32 | 0 | [ -96.3 , 0 ] | true | Additive | false |
| **ChannelConfigOverride** | Channel Configuration Override | int64 | 0 | None | true | None | false |
| **DryLevel** | Dry Level | Real32 | -96.3 | [ -96.3 , 24 ] | true | Additive | false |
| **FrontLevel** | Reverb Front Level | Real32 | 0 | [ -96.3 , 0 ] | true | Additive | false |
| **FrontRearDelay** | Rear Delay | Real32 | 0 | [ 0 , 200 ] | true | None | false |
| **FullPrecisionMedia** | Full Precision Convolution (Slow) | bool | false | None | false | None | false |
| **HardwareAcceleration** | HW Acceleration | bool | false | None | true | None | true |
| **IRChannelSelect** | IR Channels | int32 | 4 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Stereo | | 1 | Mixdown | | 2 | Left only | | 3 | Right only | | 4 | As Input | | true | None | true |
| **IRConvolutionSmooth** | IR Smooth | Real32 | 0 | [ 0 , 100 ] | true | None | false |
| **IRConvolutionSmoothMax** | IR Convolution Smooth | Real32 | 100 | None | false | None | false |
| **IRConvolutionStart** | IR Convolution Begin | Real64 | 0 | [ 0 , 20 ] | false | None | false |
| **IRConvolutionStop** | IR Convolution End | Real64 | 0 | [ 0 , 20 ] | false | None | false |
| **IRConvolutionThreshold** | IR Threshold | Real32 | -75 | [ -144 , -30 ] | true | None | true |
| **IRGraphicEQAutomate** | IR Enable EQ | bool | false | None | true | None | false |
| **IRLPFAutomate** | IR Automate LPF | bool | false | None | true | None | false |
| **IRLPFSlope** | **IRLPFSlope** | int32 | 6 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 6 |  | | 12 |  | | 18 |  | | 24 |  | | false | None | false |
| **IRLRMix** | IR Balance | Real32 | 0 | [ -100 , 100 ] | true | None | true |
| **IRLevel** | IR Volume | Real32 | 0 | [ -96.3 , 24 ] | true | None | false |
| **IRLevelAutomate** | IR Automate Volume | bool | true | None | true | None | false |
| **IRStretch** | IR Stretch | Real32 | 100 | [ 50 , 200 ] | true | None | false |
| **InputCenterLevel** | Center Input Level | Real32 | 0 | [ -96.3 , 0 ] | true | Additive | false |
| **InputLFELevel** | LFE Input Level | Real32 | -96.3 | [ -96.3 , 0 ] | true | Additive | false |
| **InputStereoWidth** | Input Spread | Real32 | 0 | [ 0 , 180 ] | true | Additive | false |
| **InputThreshold** | Input Threshold | Real32 | -60 | [ -96.3 , 30.0 ] | true | None | true |
| **LFELevel** | Reverb LFE Level | Real32 | -96.3 | [ -96.3 , 0 ] | true | Exclusive | false |
| **PreDelay** | Pre Delay | Real32 | 0 | [ 0 , 1000 ] | true | Exclusive | false |
| **RearLevel** | Reverb Rear Level | Real32 | 0 | [ -96.3 , 0 ] | true | Additive | false |
| **SoundEngineBlockSize** | Block Size | int32 | 1024 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 256 | 256 | | 512 | 512 | | 1024 | 1024 | | 2048 | 2048 | | true | None | true |
| **SoundEngineSampleRateDefault** | **SoundEngineSampleRateDefault** | int32 | 48000 | [ 24000 , 48000 ] | false | None | false |
| **SoundEngineSampleRateMac** | **SoundEngineSampleRateMac** | int32 | 48000 | [ 24000 , 48000 ] | false | None | false |
| **SoundEngineSampleRateiOS** | **SoundEngineSampleRateiOS** | int32 | 48000 | [ 24000 , 48000 ] | false | None | false |
| **StereoWidth** | Output Spread | Real32 | 180 | [ 0 , 180 ] | true | Additive | false |
| **WetLevel** | Wet Level | Real32 | 0 | [ -96.3 , 24 ] | true | Additive | false |