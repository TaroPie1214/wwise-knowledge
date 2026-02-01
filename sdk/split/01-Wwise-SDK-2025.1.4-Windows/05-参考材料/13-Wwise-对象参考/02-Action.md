# Action

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Action

- **Plugin ID**: 5
- **Class ID**: 327696

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **AbsoluteOrRelative** | Absolute/Relative | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Absolute | | 1 | Relative | | true | None | false |
| **ActionType** | 类型 | int16 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 1 | /Play | | 2 | /Stop/Stop | | 3 | /Stop/Stop All | | 7 | /Pause/Pause | | 8 | /Pause/Pause All | | 9 | /Pause/Resume | | 10 | /Pause/Resume All | | 34 | /Break | | 36 | /Seek/Seek | | 37 | /Seek/Seek All | | 41 | /Post Event | | 11 | ---/Bus Volume/Set Bus Volume | | 14 | /Bus Volume/Reset Bus Volume | | 15 | /Bus Volume/Reset Bus Volume All | | 12 | /Voice Volume/Set Voice Volume | | 16 | /Voice Volume/Reset Voice Volume | | 17 | /Voice Volume/Reset Voice Volume All | | 13 | /Voice Pitch/Set Voice Pitch | | 18 | /Voice Pitch/Reset Pitch | | 19 | /Voice Pitch/Reset Pitch All | | 26 | /Voice LPF/Set LPF | | 27 | /Voice LPF/Reset LPF | | 28 | /Voice LPF/Reset LPF All | | 29 | /Voice HPF/Set HPF | | 30 | /Voice HPF/Reset HPF | | 31 | /Voice HPF/Reset HPF All | | 4 | /Mute/Mute | | 5 | /Mute/UnMute | | 6 | /Mute/UnMute All | | 38 | ---/Game Parameter/Set Game Parameter | | 39 | /Game Parameter/Reset Game Parameter | | 20 | /States/Enable State | | 21 | /States/Disable State | | 22 | /States/Set State | | 23 | /Set Switch | | 35 | /Trigger | | 40 | /Release Envelope | | 42 | /Reset Playlist | | 50 | ---/Bypass Effect/Set - Bypass Effect Slot | | 51 | /Bypass Effect/Reset - Bypass Effect Slot | | 52 | /Bypass Effect/Reset - Bypass Effect Slot - All | | 53 | /Bypass Effect/---Set - Bypass All Effects | | 54 | /Bypass Effect/Reset - Bypass All Effects | | 55 | /Bypass Effect/Reset - Bypass All Effects - All | | 56 | /Bypass Effect/---Reset - All Effect Bypasses | | 57 | /Bypass Effect/Reset - All Effect Bypasses - All | | 43 | ---/Set Effect/Set Effect | | 44 | /Set Effect/Reset Set Effect | | 45 | /Set Effect/Reset Set Effect All | | true | None | false |
| **ApplyToDynamicSequence** | Apply to Dynamic Sequences | bool | true | None | true | None | false |
| **ApplyToStateTransition** | Apply to State Transitions | bool | true | None | true | None | false |
| **BypassFlag** | Bypass | bool | true | None | true | None | false |
| **BypassGameParameterInternalTransition** | Bypass Game Parameter Interpolation | bool | false | None | true | None | false |
| **Delay** | Delay | Real64 | 0 | [ 0 , 600 ] | true | None | false |
| **EffectSlot** | Effect Slot | int16 | 0 | [ 0 , 254 ] | true | None | false |
| **FadeInCurve** | Fade-in Curve | int16 | 4 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Logarithmic (Base 3) | | 1 | Sine | | 2 | Logarithmic (Base 1.41) | | 3 | Inverted S-Curve | | 4 | Linear | | 5 | S-Curve | | 6 | Exponential (Base 1.41) | | 7 | Reciprocal Sine | | 8 | Exponential (Base 3) | | true | None | false |
| **FadeOutCurve** | Fade-out Curve | int16 | 4 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Logarithmic (Base 3) | | 1 | Sine | | 2 | Logarithmic (Base 1.41) | | 3 | Inverted S-Curve | | 4 | Linear | | 5 | S-Curve | | 6 | Exponential (Base 1.41) | | 7 | Reciprocal Sine | | 8 | Exponential (Base 3) | | true | None | false |
| **FadeTime** | Fade Time | Real64 | 0 | [ 0 , 60 ] | true | None | false |
| **GameParameterValue** | Game Parameter Value | Real64 | 0 | None | true | None | false |
| **Highpass** | Voice HPF | int16 | 0 | [ -100 , 100 ] | true | None | false |
| **Inclusion** | Inclusion | bool | true | None | true | None | true |
| **Lowpass** | Voice LPF | int16 | 0 | [ -100 , 100 ] | true | None | false |
| **MasterResume** | Master Resume | bool | false | None | true | None | false |
| **PauseDelayedResumeAction** | Include Delayed Resume Actions | bool | true | None | true | None | false |
| **Pitch** | Voice Pitch | int32 | 0 | [ -4800 , 4800 ] | true | None | false |
| **Probability** | Probability | Real64 | 100 | [ 0 , 100 ] | true | None | false |
| **ResumeStateTransition** | Resume State Transitions | bool | true | None | true | None | false |
| **Scope** | Scope | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Game Object | | 1 | Global | | true | None | false |
| **SeekPercent** | Seek Percent | Real64 | 0 | [ 0 , 100 ] | true | None | false |
| **SeekTime** | Seek Time | Real64 | 0 | [ 0 , 3600 ] | true | None | false |
| **SeekToMarker** | Seek to Nearest Marker | bool | false | None | true | None | false |
| **SeekType** | Seek Type | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Percent | | 1 | Time | | true | None | false |
| **Target** | Target | Reference |  | None | true |  |  |
| **TargetEffect** | Target Effect | Reference |  | **可能的类型：**   |  | | --- | | Effect | | true |  |  |
| **Volume** | Volume | Real64 | 0 | [ -200 , 200 ] | true | None | false |