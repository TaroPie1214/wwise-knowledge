# Wwise Recorder (ADM)

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Recorder (ADM)

- **Plugin ID**: 198
- **Class ID**: 12976131

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# Properties, References, Lists

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ApplyDownstreamVolume** | Apply Downstream Volume | bool | false | None | true | None | false |
| **AuthoringFilename** | **AuthoringFilename** | string | AKRecorderADM-s.wav | None | false | None | false |
| **ChannelCount** | Channel Count | int16 | 64 | [ 2 , 128 ] | true | None | false |
| **GameFilename** | **GameFilename** | string |  | None | false | None | false |
| **Hold** | Hold | bool | false | None | true | Exclusive | false |
| **MainMixChannelConfig** | Main Mix Channel Configuration | int32 | 6549768 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 12546 | 2.0 | | 28931 | 3.0 | | 6320389 | 5.0 | | 6353158 | 5.1 | | 6549768 | 7.1 | | 761524492 | 7.1.4 | | true | None | false |
| **Passthrough** | Enable Passthrough Mix | bool | false | None | true | None | false |
| **PreserveExtraBeds** | Preserve Extra Beds | bool | false | None | true | None | false |
| **Profile** | Profile | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | EBU TECH 3392 ADM BROADCAST PRODUCTION PROFILE | | 1 | Dolby Atmos® Master ADM Profile Version 1.1 | | false | None | false |