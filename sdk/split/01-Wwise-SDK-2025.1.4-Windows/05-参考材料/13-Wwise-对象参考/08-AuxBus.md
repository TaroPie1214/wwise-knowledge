# AuxBus

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

AuxBus

- **Plugin ID**: 61
- **Class ID**: 3997712

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **3DPosition** | 3D Position | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Emitter | | 1 | Emitter with Automation | | 2 | Listener with Automation | | true | None | false |
| **3DSpatialization** | 3D Spatialization | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | Position | | 2 | Position + Orientation | | true | None | false |
| **Attenuation** | Attenuation | Reference |  | **可能的类型：**   |  | | --- | | Attenuation | | true |  |  |
| **AttenuationDistanceScaling** | Distance Scaling % | Real32 | 1 | [ 0.01 , 100 ] | true | Multiplicative | false |
| **BusChannelConfig** | Bus Configuration | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Same as parent | | 3584 | Same as main mix | | 3840 | Same as passthrough mix | | 768 | Audio Objects | | 16641 | 1.0 | | 12546 | 2.0 | | 45315 | 2.1 | | 28931 | 3.0 | | 6304004 | 4.0 | | 6353158 | 5.1 | | 6549768 | 7.1 | | 90239240 | 5.1.2 | | 761327882 | 5.1.4 | | 90435850 | 7.1.2 | | 761524492 | 7.1.4 | | 516 | Ambisonics 1st order | | 521 | Ambisonics 2nd order | | 528 | Ambisonics 3rd order | | 537 | Ambisonics 4th order | | 548 | Ambisonics 5th order | | 769716491 | Auro 10.1 | | 803270924 | Auro 11.1 | | 803467534 | Auro 13.1 | | 33025 | LFE | | true | None | true |
| **BusVolume** | Bus Volume | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **BypassEffect** | Bypass All Effects | bool | false | None | true | Boolean | true |
| **CenterPercentage** | Center % | int32 | 100 | [ 0 , 100 ] | true | Exclusive | true |
| **Color** | Color | int16 | 0 | [ 0 , 26 ] | true | None | false |
| **Effects** | Effects | List |  | **可能的类型：**   |  | | --- | | EffectSlot | |  |  |  |
| **EnableAttenuation** | Enable Attenuation | bool | true | None | true | Boolean | false |
| **EnableDiffraction** | Diffraction and Transmission | bool | false | None | true | None | false |
| **GameAuxSendDSF** | Game-Defined Auxiliary Sends DSF | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **GameAuxSendHPF** | Game-Defined Auxiliary Sends HPF | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **GameAuxSendLPF** | Game-Defined Auxiliary Sends LPF | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **GameAuxSendVolume** | Game-Defined Auxiliary Sends Volume | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **Highpass** | Voice HPF | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **HoldEmitterPositionOrientation** | Hold Emitter Position and Orientation | bool | false | None | true | None | false |
| **HoldListenerOrientation** | Hold Listener Orientation | bool | false | None | true | None | false |
| **ListenerRelativeRouting** | Listener Relative Routing | bool | false | None | true | None | false |
| **Lowpass** | Voice LPF | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **Metadata** | Metadata | List |  | **可能的类型：**   |  | | --- | | MetadataSlot | |  |  |  |
| **OutputBusDualshelf** | Output Bus DSF | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **OutputBusHighpass** | Output Bus HPF | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **OutputBusLowpass** | Output Bus LPF | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **OutputBusVolume** | Output Bus Volume | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **OverrideColor** | Override Color | bool | false | None | true | None | false |
| **Pitch** | Voice Pitch | int32 | 0 | [ -2400 , 2400 ] | true | Additive | true |
| **RTPC** | RTPC | List |  | **可能的类型：**   |  | | --- | | RTPC | |  |  |  |
| **ReflectionsAuxSend** | Early Reflections Auxiliary Send | Reference |  | **可能的类型：**   |  | | --- | | AuxBus | | true |  |  |
| **ReflectionsVolume** | Early Reflections Send Volume | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **SpeakerPanning** | Speaker Panning | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Direct Assignment | | 1 | Balance-Fade | | 2 | Steering | | true | None | false |
| **SpeakerPanning3DSpatializationMix** | Speaker Panning / 3D Spatialization Mix | int32 | 100 | [ 0 , 100 ] | true | Exclusive | false |
| **UseGameAuxSends** | Use Game-Defined Auxiliary Sends | bool | false | None | true | None | false |
| **UserAuxSend0** | User-Defined Auxiliary Send 0 | Reference |  | **可能的类型：**   |  | | --- | | AuxBus | | true |  |  |
| **UserAuxSend1** | User-Defined Auxiliary Send 1 | Reference |  | **可能的类型：**   |  | | --- | | AuxBus | | true |  |  |
| **UserAuxSend2** | User-Defined Auxiliary Send 2 | Reference |  | **可能的类型：**   |  | | --- | | AuxBus | | true |  |  |
| **UserAuxSend3** | User-Defined Auxiliary Send 3 | Reference |  | **可能的类型：**   |  | | --- | | AuxBus | | true |  |  |
| **UserAuxSendHPF0** | User-Defined Auxiliary HPF 0 | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **UserAuxSendHPF1** | User-Defined Auxiliary HPF 1 | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **UserAuxSendHPF2** | User-Defined Auxiliary HPF 2 | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **UserAuxSendHPF3** | User-Defined Auxiliary HPF 3 | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **UserAuxSendLPF0** | User-Defined Auxiliary LPF 0 | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **UserAuxSendLPF1** | User-Defined Auxiliary LPF 1 | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **UserAuxSendLPF2** | User-Defined Auxiliary LPF 2 | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **UserAuxSendLPF3** | User-Defined Auxiliary LPF 3 | int16 | 0 | [ 0 , 100 ] | true | Additive | true |
| **UserAuxSendVolume0** | User-Defined Auxiliary Send Volume 0 | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **UserAuxSendVolume1** | User-Defined Auxiliary Send Volume 1 | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **UserAuxSendVolume2** | User-Defined Auxiliary Send Volume 2 | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **UserAuxSendVolume3** | User-Defined Auxiliary Send Volume 3 | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |
| **Volume** | Voice Volume | Real64 | 0 | [ -200 , 200 ] | true | Additive | true |