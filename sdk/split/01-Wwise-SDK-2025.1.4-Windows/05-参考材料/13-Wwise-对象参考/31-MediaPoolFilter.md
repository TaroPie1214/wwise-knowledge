# MediaPoolFilter

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

MediaPoolFilter

- **Plugin ID**: 88
- **Class ID**: 5767184

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# Properties, References, Lists

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **AudioDescription** | 说明 | string |  | None | true | None | false |
| **AudioSimilarityPath** | Similar To | string |  | None | true | None | false |
| **AudioSimilarityRegionEnd** | Region End | Real64 | 0 | None | false | None | false |
| **AudioSimilarityRegionStart** | Region Start | Real64 | 0 | None | false | None | false |
| **CriteriaType** | Criteria Type | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Field | | 1 | Audio Description | | 2 | Audio Similarity | | false | None | false |
| **FieldName** | Field | string |  | None | true | None | false |
| **IncludeFilter** | Include | bool | true | None | true | None | false |
| **OperatorNumeric** | Operator | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 4 | <</td> | | 1 | <= | | 3 | != | | 0 | = | | 5 | > | | 2 | >= | | true | None | false |
| **OperatorText** | Operator | int32 | 2 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | != | | 1 | = | | 2 | contains | | 3 | starts with | | 4 | ends with | | 5 | matches regex | | true | None | false |
| **ValueDouble** | 值 | Real64 | 0 | None | true | None | false |
| **ValueInteger** | 值 | Uint64 | 0 | None | true | None | false |
| **ValueText** | 值 | string |  | None | true | None | false |
| **Weight** | Weight | Real64 | 1 | [ 0 , 2.0 ] | true | None | false |