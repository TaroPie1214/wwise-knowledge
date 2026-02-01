# Wwise Parametric EQ

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Parametric EQ

- **Plugin ID**: 105
- **Class ID**: 6881283

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **AttackTimeBand1** | Band 1 Dynamics Attack | Real32 | 0.1 | [ 0 , 2 ] | true | Additive | false |
| **AttackTimeBand2** | Band 2 Dynamics Attack | Real32 | 0.1 | [ 0 , 2 ] | true | Additive | false |
| **AttackTimeBand3** | Band 3 Dynamics Attack | Real32 | 0.1 | [ 0 , 2 ] | true | Additive | false |
| **AttackTimeBand4** | Band 4 Dynamics Attack | Real32 | 0.1 | [ 0 , 2 ] | true | Additive | false |
| **AttackTimeBand5** | Band 5 Dynamics Attack | Real32 | 0.1 | [ 0 , 2 ] | true | Additive | false |
| **AttackTimeBand6** | Band 6 Dynamics Attack | Real32 | 0.1 | [ 0 , 2 ] | true | Additive | false |
| **AttackTimeBand7** | Band 7 Dynamics Attack | Real32 | 0.1 | [ 0 , 2 ] | true | Additive | false |
| **AttackTimeBand8** | Band 8 Dynamics Attack | Real32 | 0.1 | [ 0 , 2 ] | true | Additive | false |
| **BandListen** | Listen to Band | int32 | 0 | [ 0 , 8 ] | false | None | false |
| **DynamicsEnableBand1** | Band 1 Enable Dynamics | bool | false | None | true | None | false |
| **DynamicsEnableBand2** | Band 2 Enable Dynamics | bool | false | None | true | None | false |
| **DynamicsEnableBand3** | Band 3 Enable Dynamics | bool | false | None | true | None | false |
| **DynamicsEnableBand4** | Band 4 Enable Dynamics | bool | false | None | true | None | false |
| **DynamicsEnableBand5** | Band 5 Enable Dynamics | bool | false | None | true | None | false |
| **DynamicsEnableBand6** | Band 6 Enable Dynamics | bool | false | None | true | None | false |
| **DynamicsEnableBand7** | Band 7 Enable Dynamics | bool | false | None | true | None | false |
| **DynamicsEnableBand8** | Band 8 Enable Dynamics | bool | false | None | true | None | false |
| **DynamicsListen** | Listen to Dynamics Band | int32 | 0 | [ 0 , 8 ] | false | None | false |
| **DynamicsSidechainRef** | Sidechain Mix Source | Reference |  | **可能的类型：**   |  | | --- | | SidechainMix | | true |  |  |
| **FilterTypeBand1** | Band 1 Filter Type | int32 | 4 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Low Pass Flat | | 1 | High Pass Flat | | 7 | Low Pass Q | | 8 | High Pass Q | | 2 | Band Pass | | 3 | Notch | | 6 | Peaking | | 4 | Low Shelf | | 5 | High Shelf | | true | Exclusive | false |
| **FilterTypeBand2** | Band 2 Filter Type | int32 | 6 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Low Pass Flat | | 1 | High Pass Flat | | 7 | Low Pass Q | | 8 | High Pass Q | | 2 | Band Pass | | 3 | Notch | | 6 | Peaking | | 4 | Low Shelf | | 5 | High Shelf | | true | Exclusive | false |
| **FilterTypeBand3** | Band 3 Filter Type | int32 | 6 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Low Pass Flat | | 1 | High Pass Flat | | 7 | Low Pass Q | | 8 | High Pass Q | | 2 | Band Pass | | 3 | Notch | | 6 | Peaking | | 4 | Low Shelf | | 5 | High Shelf | | true | Exclusive | false |
| **FilterTypeBand4** | Band 4 Filter Type | int32 | 6 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Low Pass Flat | | 1 | High Pass Flat | | 7 | Low Pass Q | | 8 | High Pass Q | | 2 | Band Pass | | 3 | Notch | | 6 | Peaking | | 4 | Low Shelf | | 5 | High Shelf | | true | Exclusive | false |
| **FilterTypeBand5** | Band 5 Filter Type | int32 | 6 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Low Pass Flat | | 1 | High Pass Flat | | 7 | Low Pass Q | | 8 | High Pass Q | | 2 | Band Pass | | 3 | Notch | | 6 | Peaking | | 4 | Low Shelf | | 5 | High Shelf | | true | Exclusive | false |
| **FilterTypeBand6** | Band 6 Filter Type | int32 | 6 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Low Pass Flat | | 1 | High Pass Flat | | 7 | Low Pass Q | | 8 | High Pass Q | | 2 | Band Pass | | 3 | Notch | | 6 | Peaking | | 4 | Low Shelf | | 5 | High Shelf | | true | Exclusive | false |
| **FilterTypeBand7** | Band 7 Filter Type | int32 | 6 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Low Pass Flat | | 1 | High Pass Flat | | 7 | Low Pass Q | | 8 | High Pass Q | | 2 | Band Pass | | 3 | Notch | | 6 | Peaking | | 4 | Low Shelf | | 5 | High Shelf | | true | Exclusive | false |
| **FilterTypeBand8** | Band 8 Filter Type | int32 | 6 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Low Pass Flat | | 1 | High Pass Flat | | 7 | Low Pass Q | | 8 | High Pass Q | | 2 | Band Pass | | 3 | Notch | | 6 | Peaking | | 4 | Low Shelf | | 5 | High Shelf | | true | Exclusive | false |
| **FrequencyBand1** | Band 1 Frequency | Real32 | 60 | [ 20 , 20000 ] | true | Exclusive | false |
| **FrequencyBand2** | Band 2 Frequency | Real32 | 90 | [ 20 , 20000 ] | true | Exclusive | false |
| **FrequencyBand3** | Band 3 Frequency | Real32 | 300 | [ 20 , 20000 ] | true | Exclusive | false |
| **FrequencyBand4** | Band 4 Frequency | Real32 | 600 | [ 20 , 20000 ] | true | Exclusive | false |
| **FrequencyBand5** | Band 5 Frequency | Real32 | 900 | [ 20 , 20000 ] | true | Exclusive | false |
| **FrequencyBand6** | Band 6 Frequency | Real32 | 3000 | [ 20 , 20000 ] | true | Exclusive | false |
| **FrequencyBand7** | Band 7 Frequency | Real32 | 6000 | [ 20 , 20000 ] | true | Exclusive | false |
| **FrequencyBand8** | Band 8 Frequency | Real32 | 9000 | [ 20 , 20000 ] | true | Exclusive | false |
| **GainBand1** | Band 1 Gain | Real32 | 0 | [ -24 , 24 ] | true | Additive | false |
| **GainBand2** | Band 2 Gain | Real32 | 0 | [ -24 , 24 ] | true | Additive | false |
| **GainBand3** | Band 3 Gain | Real32 | 0 | [ -24 , 24 ] | true | Additive | false |
| **GainBand4** | Band 4 Gain | Real32 | 0 | [ -24 , 24 ] | true | Additive | false |
| **GainBand5** | Band 5 Gain | Real32 | 0 | [ -24 , 24 ] | true | Additive | false |
| **GainBand6** | Band 6 Gain | Real32 | 0 | [ -24 , 24 ] | true | Additive | false |
| **GainBand7** | Band 7 Gain | Real32 | 0 | [ -24 , 24 ] | true | Additive | false |
| **GainBand8** | Band 8 Gain | Real32 | 0 | [ -24 , 24 ] | true | Additive | false |
| **NumBands** | Number of Bands | int32 | 3 | [ 1 , 8 ] | true | None | false |
| **OnOffBand1** | Band 1 Enable | bool | true | None | true | Exclusive | false |
| **OnOffBand2** | Band 2 Enable | bool | true | None | true | Exclusive | false |
| **OnOffBand3** | Band 3 Enable | bool | false | None | true | Exclusive | false |
| **OnOffBand4** | Band 4 Enable | bool | false | None | true | Exclusive | false |
| **OnOffBand5** | Band 5 Enable | bool | false | None | true | Exclusive | false |
| **OnOffBand6** | Band 6 Enable | bool | false | None | true | Exclusive | false |
| **OnOffBand7** | Band 7 Enable | bool | false | None | true | Exclusive | false |
| **OnOffBand8** | Band 8 Enable | bool | false | None | true | Exclusive | false |
| **OutputLevel** | Output Gain | Real32 | 0 | [ -24 , 24 ] | true | Additive | false |
| **ProcessLFE** | Process LFE | bool | true | None | true | None | false |
| **QFactorBand1** | Band 1 Quality Factor | Real32 | 1 | [ 0.025 , 100 ] | true | Exclusive | false |
| **QFactorBand2** | Band 2 Quality Factor | Real32 | 1 | [ 0.025 , 100 ] | true | Exclusive | false |
| **QFactorBand3** | Band 3 Quality Factor | Real32 | 1 | [ 0.025 , 100 ] | true | Exclusive | false |
| **QFactorBand4** | Band 4 Quality Factor | Real32 | 1 | [ 0.025 , 100 ] | true | Exclusive | false |
| **QFactorBand5** | Band 5 Quality Factor | Real32 | 1 | [ 0.025 , 100 ] | true | Exclusive | false |
| **QFactorBand6** | Band 6 Quality Factor | Real32 | 1 | [ 0.025 , 100 ] | true | Exclusive | false |
| **QFactorBand7** | Band 7 Quality Factor | Real32 | 1 | [ 0.025 , 100 ] | true | Exclusive | false |
| **QFactorBand8** | Band 8 Quality Factor | Real32 | 1 | [ 0.025 , 100 ] | true | Exclusive | false |
| **RangeBand1** | Band 1 Dynamics Range | Real32 | 0 | [ -30 , 30 ] | true | Exclusive | false |
| **RangeBand2** | Band 2 Dynamics Range | Real32 | 0 | [ -30 , 30 ] | true | Exclusive | false |
| **RangeBand3** | Band 3 Dynamics Range | Real32 | 0 | [ -30 , 30 ] | true | Exclusive | false |
| **RangeBand4** | Band 4 Dynamics Range | Real32 | 0 | [ -30 , 30 ] | true | Exclusive | false |
| **RangeBand5** | Band 5 Dynamics Range | Real32 | 0 | [ -30 , 30 ] | true | Exclusive | false |
| **RangeBand6** | Band 6 Dynamics Range | Real32 | 0 | [ -30 , 30 ] | true | Exclusive | false |
| **RangeBand7** | Band 7 Dynamics Range | Real32 | 0 | [ -30 , 30 ] | true | Exclusive | false |
| **RangeBand8** | Band 8 Dynamics Range | Real32 | 0 | [ -30 , 30 ] | true | Exclusive | false |
| **ReleaseTimeBand1** | Band 1 Dynamics Release | Real32 | 0.1 | [ 0 , 2 ] | true | Additive | false |
| **ReleaseTimeBand2** | Band 2 Dynamics Release | Real32 | 0.1 | [ 0 , 2 ] | true | Additive | false |
| **ReleaseTimeBand3** | Band 3 Dynamics Release | Real32 | 0.1 | [ 0 , 2 ] | true | Additive | false |
| **ReleaseTimeBand4** | Band 4 Dynamics Release | Real32 | 0.1 | [ 0 , 2 ] | true | Additive | false |
| **ReleaseTimeBand5** | Band 5 Dynamics Release | Real32 | 0.1 | [ 0 , 2 ] | true | Additive | false |
| **ReleaseTimeBand6** | Band 6 Dynamics Release | Real32 | 0.1 | [ 0 , 2 ] | true | Additive | false |
| **ReleaseTimeBand7** | Band 7 Dynamics Release | Real32 | 0.1 | [ 0 , 2 ] | true | Additive | false |
| **ReleaseTimeBand8** | Band 8 Dynamics Release | Real32 | 0.1 | [ 0 , 2 ] | true | Additive | false |
| **RolloffRateBand1** | Band 1 Rolloff | int32 | 12 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 12 | 12 dB/oct | | 24 | 24 dB/oct | | 36 | 36 dB/oct | | 48 | 48 dB/oct | | true | None | false |
| **RolloffRateBand2** | Band 2 Rolloff | int32 | 12 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 12 | 12 dB/oct | | 24 | 24 dB/oct | | 36 | 36 dB/oct | | 48 | 48 dB/oct | | true | None | false |
| **RolloffRateBand3** | Band 3 Rolloff | int32 | 12 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 12 | 12 dB/oct | | 24 | 24 dB/oct | | 36 | 36 dB/oct | | 48 | 48 dB/oct | | true | None | false |
| **RolloffRateBand4** | Band 4 Rolloff | int32 | 12 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 12 | 12 dB/oct | | 24 | 24 dB/oct | | 36 | 36 dB/oct | | 48 | 48 dB/oct | | true | None | false |
| **RolloffRateBand5** | Band 5 Rolloff | int32 | 12 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 12 | 12 dB/oct | | 24 | 24 dB/oct | | 36 | 36 dB/oct | | 48 | 48 dB/oct | | true | None | false |
| **RolloffRateBand6** | Band 6 Rolloff | int32 | 12 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 12 | 12 dB/oct | | 24 | 24 dB/oct | | 36 | 36 dB/oct | | 48 | 48 dB/oct | | true | None | false |
| **RolloffRateBand7** | Band 7 Rolloff | int32 | 12 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 12 | 12 dB/oct | | 24 | 24 dB/oct | | 36 | 36 dB/oct | | 48 | 48 dB/oct | | true | None | false |
| **RolloffRateBand8** | Band 8 Rolloff | int32 | 12 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 12 | 12 dB/oct | | 24 | 24 dB/oct | | 36 | 36 dB/oct | | 48 | 48 dB/oct | | true | None | false |
| **SidechainScope** | Sidechain Mix Scope | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Global | | 1 | Game Object | | true | None | false |
| **ThresholdBand1** | Band 1 Dynamics Threshold | Real32 | 0 | [ -60 , 24 ] | true | Additive | false |
| **ThresholdBand2** | Band 2 Dynamics Threshold | Real32 | 0 | [ -60 , 24 ] | true | Additive | false |
| **ThresholdBand3** | Band 3 Dynamics Threshold | Real32 | 0 | [ -60 , 24 ] | true | Additive | false |
| **ThresholdBand4** | Band 4 Dynamics Threshold | Real32 | 0 | [ -60 , 24 ] | true | Additive | false |
| **ThresholdBand5** | Band 5 Dynamics Threshold | Real32 | 0 | [ -60 , 24 ] | true | Additive | false |
| **ThresholdBand6** | Band 6 Dynamics Threshold | Real32 | 0 | [ -60 , 24 ] | true | Additive | false |
| **ThresholdBand7** | Band 7 Dynamics Threshold | Real32 | 0 | [ -60 , 24 ] | true | Additive | false |
| **ThresholdBand8** | Band 8 Dynamics Threshold | Real32 | 0 | [ -60 , 24 ] | true | Additive | false |