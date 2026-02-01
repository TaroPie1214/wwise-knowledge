# Conversion

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Conversion

- **Plugin ID**: 55
- **Class ID**: 3604496

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **AllowChannelUpmix** | Allow Channel Upmix | bool | true | None | true | None | true |
| **Channels** | Channels | int32 | 4 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Mono | | 1 | Stereo | | 2 | Mono Drop | | 3 | Stereo Drop | | 4 | As Input | | true | None | true |
| **Color** | Color | int16 | 0 | [ 0 , 26 ] | true | None | false |
| **LRMix** | LR Mix | Real64 | 0 | [ -100 , 100 ] | true | None | true |
| **MaxSampleRate** | Maximum Sample Rate | int32 | 48000 | None | true | None | true |
| **MinSampleRate** | Minimum Sample Rate | int32 | 0 | None | true | None | true |
| **OverrideColor** | Override Color | bool | false | None | true | None | false |
| **RemoveDCOffset** | Remove DC Offset | bool | false | None | true | None | true |
| **SRConversionQuality** | Sample Rate Conversion Method | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Normal | | 1 | High | | true | None | true |
| **SampleRate** | Sample Rate | int32 | 0 | None | true | None | true |
| **UseDither** | Use Dither | bool | false | None | true | None | true |
| **UseFilenameMarker** | Use Filename Marker | bool | false | None | true | None | true |