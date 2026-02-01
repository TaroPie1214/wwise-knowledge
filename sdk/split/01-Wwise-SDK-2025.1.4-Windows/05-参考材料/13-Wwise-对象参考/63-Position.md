# Position

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Position

- **Plugin ID**: 12
- **Class ID**: 786448

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **NewPathForEachSound** | Use new path for each sound | bool | false | None | true | None | false |
| **PanX** | Pan Left-Right (3D) | Real64 | 0 | [ -100 , 100 ] | true | Additive | false |
| **PanY** | Pan Front-Rear (3D) | Real64 | 35 | [ -100 , 100 ] | true | Additive | false |
| **PanZ** | Pan Up-Down (3D) | Real64 | 0 | [ -100 , 100 ] | true | Additive | false |
| **PlayMechanismLoop** | Loop | bool | true | None | true | None | false |
| **PlayMechanismRandomOrSequence** | Random or Sequence | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Sequence | | 1 | Random | | true | None | false |
| **PlayMechanismStepOrContinuous** | Play Mode | int16 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Continuous | | 1 | Step | | true | None | false |
| **PlayMechanismTransitionTime** | Transition time | Real64 | 1 | None | true | None | false |
| **PlayMechanismTransitionUse** | Transition use | bool | true | None | true | None | false |
| **RTPC** | RTPC | List |  | **可能的类型：**   |  | | --- | | RTPC | |  |  |  |