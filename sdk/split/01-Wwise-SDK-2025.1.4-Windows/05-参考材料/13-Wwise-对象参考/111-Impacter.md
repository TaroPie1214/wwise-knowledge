# Impacter

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Impacter

- **Plugin ID**: 184
- **Class ID**: 12058626

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ExcitationMask** | Impact Inclusion | Uint64 | 18446744073709551615 | None | false | None | false |
| **ExcitationSelectionMode** | Impact Selection Mode | int16 | 1 | [ 0 , 2 ] | false | None | false |
| **FMDepth** | Roughness | Real32 | 0 | [ 0.0 , 1.0 ] | true | Additive | false |
| **FMDepthRandom** | Roughness Random | Real32 | 0.0 | [ 0.0 , 1.0 ] | true | None | false |
| **FileExcitation** | Impact Media File | int32 | 0 | [ 0 , 64 ] | false | None | false |
| **FileModel** | Body Media File | int32 | 0 | [ 0 , 64 ] | false | None | false |
| **ImpactPosition** | Impact Position | Real32 | 0.0 | [ 0.0 , 1.0 ] | true | Additive | false |
| **ImpactPositionRandom** | Impact Position Random | Real32 | 0.0 | [ 0.0 , 1.0 ] | true | None | false |
| **Mass** | Mass | Real32 | 1.0 | [ 0.01 , 2.0 ] | true | Exclusive | false |
| **MassRandom** | Mass Random | Real32 | 0.0 | [ 0.0 , 2.0 ] | true | None | false |
| **MinDuration** | Min Duration | Real32 | 0.0 | [ 0.0 , 10.0 ] | true | Additive | false |
| **ModelMask** | Body Inclusion | Uint64 | 18446744073709551615 | None | false | None | false |
| **ModelSelectionMode** | Body Selection Mode | int16 | 1 | [ 0 , 2 ] | false | None | false |
| **NumFiles** | **NumFiles** | int32 | 0 | None | false | None | false |
| **OutputLevel** | Output Level | Real32 | 0 | [ -96 , 24 ] | true | Additive | false |
| **Velocity** | Velocity | Real32 | 1.0 | [ 0.05 , 1.0 ] | true | Exclusive | false |
| **VelocityRandom** | Velocity Random | Real32 | 0.0 | [ -1.0 , 0 ] | true | None | false |