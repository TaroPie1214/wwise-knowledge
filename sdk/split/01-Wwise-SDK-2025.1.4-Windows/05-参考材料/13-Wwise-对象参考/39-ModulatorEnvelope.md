# ModulatorEnvelope

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

ModulatorEnvelope

- **Plugin ID**: 65
- **Class ID**: 4259856

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Color** | Color | int16 | 0 | [ 0 , 26 ] | true | None | false |
| **EnvelopeAttackCurve** | Attack Curve | Real64 | 50 | [ 0 , 100 ] | true | Exclusive | false |
| **EnvelopeAttackTime** | Attack Time | Real64 | 0.2 | [ 0 , 10000 ] | true | Exclusive | false |
| **EnvelopeAutoRelease** | Auto Release | bool | false | None | true | None | false |
| **EnvelopeDecayTime** | Decay Time | Real64 | 0.2 | [ 0 , 10000 ] | true | Exclusive | false |
| **EnvelopeReleaseTime** | Release Time | Real64 | 0.5 | [ 0 , 10000 ] | true | Exclusive | false |
| **EnvelopeStopPlayback** | Stop Playback After Release | bool | true | None | true | None | false |
| **EnvelopeSustainLevel** | Sustain Level | Real64 | 100 | [ 0 , 100 ] | true | Exclusive | false |
| **EnvelopeSustainTime** | Maximum Sustain Time | Real64 | 0 | [ 0 , 10000 ] | true | Exclusive | false |
| **EnvelopeTriggerOn** | Trigger On | int32 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 1 | Play | | 2 | Note-Off | | true | None | false |
| **ModulatorScope** | Scope | int32 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Voice | | 1 | Note or Event | | true | None | false |
| **OverrideColor** | Override Color | bool | false | None | true | None | false |
| **RTPC** | RTPC | List |  | **可能的类型：**   |  | | --- | | RTPC | |  |  |  |