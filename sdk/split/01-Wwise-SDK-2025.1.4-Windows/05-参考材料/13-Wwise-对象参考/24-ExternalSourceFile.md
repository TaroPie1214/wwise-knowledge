# ExternalSourceFile

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

ExternalSourceFile

- **Plugin ID**: 56
- **Class ID**: 3670032

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **AnalysisType** | **AnalysisType** | int32 | 0 | [ 0 , 2 ] | false | None | false |
| **Conversion** | Conversion Settings | Reference |  | **可能的类型：**   |  | | --- | | Conversion | | true |  |  |
| **LoudnessNormalizationTarget** | **LoudnessNormalizationTarget** | Real64 | -23 | [ -96 , 0 ] | false | None | false |
| **LoudnessNormalizationType** | **LoudnessNormalizationType** | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Integrated | | 1 | Momentary Max | | false | None | false |
| **OverrideConversion** | Override Conversion Settings | bool | false | None | false | None | false |