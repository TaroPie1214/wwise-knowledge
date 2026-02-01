# Wwise RoomVerb

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise RoomVerb

- **Plugin ID**: 118
- **Class ID**: 7733251

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **CenterLevel** | Center Level | Real32 | 0 | [ -96.3 , 0 ] | true | Additive | false |
| **DCFilterCutFreq** | **DCFilterCutFreq** | Real32 | 40 | None | false | None | false |
| **DecayTime** | Decay Time | Real32 | 1.2 | [ 0.2 , 10 ] | true | Exclusive | false |
| **Density** | Density | Real32 | 80 | [ 0 , 100 ] | true | None | false |
| **DensityDelayMax** | **DensityDelayMax** | Real32 | 50 | None | false | None | false |
| **DensityDelayMin** | **DensityDelayMin** | Real32 | 8 | None | false | None | false |
| **DensityDelayRdmPerc** | **DensityDelayRdmPerc** | Real32 | 2 | None | false | None | false |
| **Diffusion** | Diffusion | Real32 | 100 | [ 0 , 100 ] | true | Additive | false |
| **DiffusionDelayMax** | **DiffusionDelayMax** | Real32 | 15 | None | false | None | false |
| **DiffusionDelayRdmPerc** | **DiffusionDelayRdmPerc** | Real32 | 5 | None | false | None | false |
| **DiffusionDelayScalePerc** | **DiffusionDelayScalePerc** | Real32 | 66 | None | false | None | false |
| **DryLevel** | Dry Level | Real32 | -96.3 | [ -96.3 , 0 ] | true | Additive | false |
| **ERFrontBackDelay** | ER Rear Delay | Real32 | 0 | [ 0 , 100 ] | true | None | false |
| **ERLevel** | ER Level | Real32 | -20 | [ -96.3 , 0 ] | true | Additive | false |
| **ERPattern** | **ERPattern** | int32 | 23 | [ 0 , 30 ] | false | None | false |
| **EnableEarlyReflections** | Enable Early Reflections | bool | true | None | true | None | false |
| **EnableToneControls** | Enable Tone | bool | false | None | true | None | false |
| **Filter1Curve** | Filter Band 1 Curve | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Low shelf | | 1 | Peaking | | 2 | High shelf | | true | None | false |
| **Filter1Freq** | Filter Band 1 Frequency | Real32 | 100 | [ 20 , 20000 ] | true | Exclusive | false |
| **Filter1Gain** | Filter Band 1 Gain | Real32 | 0 | [ -32 , 32 ] | true | Additive | false |
| **Filter1InsertPos** | Filter Band 1 Insert | int32 | 3 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Off | | 1 | ER only | | 2 | Reverb only | | 3 | ER + Reverb | | true | None | false |
| **Filter1Q** | Filter Band 1 Q | Real32 | 1 | [ 0.1 , 10 ] | true | Exclusive | false |
| **Filter2Curve** | Filter Band 2 Curve | int32 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Low shelf | | 1 | Peaking | | 2 | High shelf | | true | None | false |
| **Filter2Freq** | Filter Band 2 Frequency | Real32 | 1000 | [ 20 , 20000 ] | true | Exclusive | false |
| **Filter2Gain** | Filter Band 2 Gain | Real32 | 0 | [ -32 , 32 ] | true | Additive | false |
| **Filter2InsertPos** | Filter Band 2 Insert | int32 | 3 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Off | | 1 | ER only | | 2 | Reverb only | | 3 | ER + Reverb | | true | None | false |
| **Filter2Q** | Filter Band 2 Q | Real32 | 1 | [ 0.1 , 10 ] | true | Exclusive | false |
| **Filter3Curve** | Filter Band 3 Curve | int32 | 2 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Low shelf | | 1 | Peaking | | 2 | High shelf | | true | None | false |
| **Filter3Freq** | Filter Band 3 Frequency | Real32 | 10000 | [ 20 , 20000 ] | true | Exclusive | false |
| **Filter3Gain** | Filter Band 3 Gain | Real32 | 0 | [ -32 , 32 ] | true | Additive | false |
| **Filter3InsertPos** | Filter Band 3 Insert | int32 | 3 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Off | | 1 | ER only | | 2 | Reverb only | | 3 | ER + Reverb | | true | None | false |
| **Filter3Q** | Filter Band 3 Q | Real32 | 1 | [ 0.1 , 10 ] | true | Exclusive | false |
| **FrontLevel** | Front Level | Real32 | 0 | [ -96.3 , 0 ] | true | Additive | false |
| **HFDamping** | HF Damping | Real32 | 2.25 | [ 0.5 , 10 ] | true | Exclusive | false |
| **InputCenterLevel** | Center Input Level | Real32 | 0 | [ -96.3 , 0 ] | true | None | false |
| **InputLFELevel** | LFE Input Level | Real32 | -96.3 | [ -96.3 , 0 ] | true | None | false |
| **LFELevel** | LFE Level | Real32 | -96.3 | [ -96.3 , 0 ] | true | Additive | false |
| **PreDelay** | Pre Delay | Real32 | 25 | [ 0 , 1000 ] | true | Exclusive | false |
| **Quality** | Quality | int32 | 8 | [ 2 , 16 ] | true | None | false |
| **RearLevel** | Rear Level | Real32 | 0 | [ -96.3 , 0 ] | true | Additive | false |
| **ReverbLevel** | Reverb Level | Real32 | -20 | [ -96.3 , 0 ] | true | Additive | false |
| **ReverbUnitInputDelay** | **ReverbUnitInputDelay** | Real32 | 100 | None | false | None | false |
| **ReverbUnitInputDelayRmdPerc** | **ReverbUnitInputDelayRmdPerc** | Real32 | 50 | None | false | None | false |
| **RoomShape** | Room Shape | Real32 | 100 | [ 0 , 100 ] | true | None | false |
| **RoomShapeMax** | **RoomShapeMax** | Real32 | 0.8 | None | false | None | false |
| **RoomShapeMin** | **RoomShapeMin** | Real32 | 0.1 | None | false | None | false |
| **RoomSize** | ER Room Size | Real32 | 0 | [ -100 , 100 ] | true | None | false |
| **StereoWidth** | Stereo Width | Real32 | 180 | [ 0 , 180 ] | true | Additive | false |