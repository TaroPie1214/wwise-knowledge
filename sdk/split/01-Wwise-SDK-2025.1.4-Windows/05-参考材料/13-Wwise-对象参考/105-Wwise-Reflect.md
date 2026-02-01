# Wwise Reflect

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Reflect

- **Plugin ID**: 171
- **Class ID**: 11206659

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **BaseTextureFrequency** | **BaseTextureFrequency** | Real32 | 250 | [ 20 , 1000 ] | false | None | false |
| **CenterPerc** | Output Center % | Real32 | 100 | [ 0 , 100 ] | true | Additive | false |
| **CurveUsageMask** | Curve Usage | Uint32 | 0 | [ 0 , 127 ] | false | None | false |
| **DecorrAlgorithmSelect** | Mode | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Favor Performance | | 1 | Favor Quality | | true | None | false |
| **DecorrFilterMaxReflectionOrder** | Decorrelator Max Reflection Order | Uint32 | 1 | [ 0 , 4 ] | false | None | false |
| **DecorrHardwareAcceleration** | Use Hardware Acceleration | bool | false | None | false | None | false |
| **DecorrStrength** | Strength | Real32 | 0.0 | [ 0 , 100.0 ] | true | None | false |
| **DecorrStrengthSource** | Use Strength From | int32 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Textures | | 1 | Reflect UI (Global) | | false | None | false |
| **DecorrWindowWidth** | Decorr Filter Sparsity | Uint32 | 7 | [ 1 , 30 ] | false | None | false |
| **DelayErrorTolerance** | Delay Error Tolerance | Real32 | 25 | [ 0 , 100 ] | true | Additive | false |
| **DiffractionWarping** | Diffraction | Real32 | 0 | [ -100 , 100 ] | true | Additive | false |
| **DistanceThreshold** | Distance Threshold | Real32 | 0 | [ 0 , 2147483648 ] | false | Additive | false |
| **DistanceWarping** | Distance | Real32 | 0 | [ -100 , 100 ] | true | Additive | false |
| **Dry** | Dry | Real32 | -96 | [ -96 , 24 ] | false | None | false |
| **FadeTime** | Image Source Fade Time | Real32 | 500 | [ 0 , 10000 ] | true | None | false |
| **FusingTime** | Direct Sound Max Delay | Real32 | 20 | [ 0 , 1000 ] | true | Additive | false |
| **HardwareProcessing** | Hardware Processing | bool | false | None | false | None | false |
| **MaterialFilteringSelect** | Material Filtering | Uint32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Favor Performance | | 1 | Favor Quality | | false | None | false |
| **MaxDistance** | Max Distance | Real32 | 1000 | [ 1 , 2147483648 ] | false | None | false |
| **MaxImageSourceDelayTime** | Max Image Source Delay Time | Real32 | 1000 | [ 0 , 30000 ] | false | None | false |
| **MaxReflections** | Max Reflections | Real32 | 0 | [ 0 , 1024 ] | false | None | false |
| **OutputChannelConfig** | Output Config | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Same as main mix | | 3840 | Same as passthrough mix | | 16641 | Mono | | 12546 | Stereo | | 28931 | 3.0 | | 6304004 | 4.0 | | 6353158 | 5.1 | | 6549768 | 7.1 | | 90239240 | 5.1.2 | | 761327882 | 5.1.4 | | 90435850 | 7.1.2 | | 761524492 | 7.1.4 | | 516 | Ambisonics 1st order | | 521 | Ambisonics 2nd order | | 528 | Ambisonics 3rd order | | 769716491 | Auro 10.1 | | 803270924 | Auro 11.1 | | 803467534 | Auro 13.1 | | 33025 | LFE | | true | None | false |
| **ParamFilterCutoff** | Delay Smoothing | Real32 | 0.5 | [ 0 , 1 ] | true | Additive | false |
| **ParamFilterType** | Smoothing Type | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | IIR | | 1 | FIR | | false | None | false |
| **PitchThreshold** | Pitch Limit | Real32 | 300 | [ 0 , 9600 ] | true | Additive | false |
| **SpeedOfSound** | Speed of Sound | Real32 | 345 | [ 0.001 , 2147483648 ] | true | Additive | false |
| **StereoDecorrelation** | Widen Stereo Field | bool | false | None | true | None | false |
| **ThresholdMode** | Threshold Mode | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Continuous | | 1 | Step | | false | None | false |
| **Wet** | Output Level | Real32 | 0 | [ -96 , 24 ] | true | Additive | false |