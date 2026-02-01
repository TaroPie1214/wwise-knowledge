# SearchCriteria

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

SearchCriteria

- **Plugin ID**: 33
- **Class ID**: 2162704

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Attenuation** | Attenuation | string |  | None | true | None | false |
| **ConditionalOperator** | Conditional Operator | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 |  | | 1 |  | | false | None | false |
| **Conversion** | Conversion Settings | string |  | None | true | None | false |
| **CurveType** | Curve Type | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 1 |  | | 2 |  | | 3 |  | | 4 |  | | 5 |  | | 6 |  | | 7 |  | | 8 |  | | 9 |  | | 10 |  | | 11 |  | | 12 |  | | 13 |  | | 14 |  | | 15 |  | | 16 |  | | 17 |  | | 18 |  | | 19 |  | | 20 |  | | 21 |  | | 22 |  | | 23 |  | | false | None | false |
| **CurveUsage** | Curve Usage | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 |  | | 1 |  | | 2 |  | | 3 |  | | false | None | false |
| **DefaultSwitchState** | Default Switch | string |  | None | true | None | false |
| **Effect** | Effect | string |  | None | true | None | false |
| **EffectClassID** | Effect | string |  | None | true | None | false |
| **ErrorResult** | Error | string |  | None | false | None | false |
| **EventsReferencedInOperator** | Events Referenced In Operator | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | No SoundBank | | 1 | One SoundBank | | 2 | Many SoundBanks | | false | None | false |
| **GameParameter** | Game Parameter | string |  | None | true | None | false |
| **HasEmptyAssignation** | Has Empty Assignation | bool | true | None | true | None | false |
| **Inclusion** | Language Inclusion | bool | false | None | true | None | false |
| **IsChecked** | Checked/Unchecked | bool | false | None | true | None | false |
| **IsLinked** | Link/Unlink | bool | true | None | true | None | false |
| **IsSourceOfOverride** | Is source of Override | bool | true | None | true | None | false |
| **IsSpecialSearch** | Checked/Unchecked | bool | false | None | true | None | false |
| **IsUsed** | Used/Unused | bool | false | None | true | None | false |
| **LeftValue** | Left Value | Real64 | 0 | None | true | None | false |
| **LogicalOperator** | Logical Operator | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 |  | | 1 |  | | false | None | false |
| **Metadata** | Metadata | string |  | None | true | None | false |
| **MetadataClassID** | Metadata | string |  | None | true | None | false |
| **Mode** | Mode | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Define Custom | | 1 | Use ShareSets | | false | None | false |
| **MusicSegment** | Music Segment | string |  | None | true | None | false |
| **NumericOperator** | Numeric Operator | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | == | | 1 | <</td> | | 2 | > | | 3 | != | | 4 | range | | false | None | false |
| **ObjectReferenced** | Object referenced | string |  | None | true | None | false |
| **OutputBus** | Output Bus | string |  | None | true | None | false |
| **PropertyName** | Property | string |  | None | true | None | false |
| **RTPCOperator** | RTPC Operator | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Has RTPC on | | 1 | Does not have RTPC on | | false | None | false |
| **RightValue** | Right Value | Real64 | 0 | None | true | None | false |
| **RndSeqContainerType** | Random/Sequence Container Type | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 |  | | 1 |  | | false | None | false |
| **SRConversionQuality** | Sample Rate Conversion Method | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Normal | | 1 | High | | false | None | false |
| **SampleRateConversionType** | Sample Rate Conversion Type | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 |  | | 1 |  | | 2 |  | | 3 |  | | false | None | false |
| **SoundType** | Sound Type | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 |  | | 1 |  | | false | None | false |
| **SourceAudioFormat** | Audio Format | string |  | None | true | None | false |
| **SourceChannelsLFEOption** | LFE Option | int32 | -1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | -1 |  | | 0 |  | | 1 |  | | false | None | false |
| **SourceChannelsOthersCount** | Other Channels Count | int32 | 0 | None | true | None | false |
| **SourceChannelsOthersOption** | Other Channels Option | int32 | -1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | -1 |  | | 0 |  | | 1 |  | | 2 |  | | 3 |  | | 4 |  | | 5 |  | | false | None | false |
| **SourceLanguage** | Language | string |  | None | true | None | false |
| **SourceType** | Source Type | string |  | None | true | None | false |
| **State** | State | string |  | None | true | None | false |
| **StateGroup** | State Group | string |  | None | true | None | false |
| **StatePropertyUsage** | Define State Values | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 |  | | 1 |  | | 2 |  | | false | None | false |
| **SwitchGroup** | Switch Group | string |  | None | true | None | false |
| **SwitchingOperator** | Switching Operator | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 |  | | 1 |  | | false | None | false |
| **Trigger** | Trigger | string |  | None | true | None | false |
| **UIntValue** | UInt Value | Uint32 | 0 | [ 0 , 4294967295 ] | true | None | false |
| **UserString** | Text | string |  | None | true | None | false |
| **UsingOperator** | Using Operator | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Is Using | | 1 | Is Not Using | | false | None | false |