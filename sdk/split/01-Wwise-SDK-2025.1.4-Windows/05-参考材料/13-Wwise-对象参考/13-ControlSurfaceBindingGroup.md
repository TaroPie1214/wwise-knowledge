# ControlSurfaceBindingGroup

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

ControlSurfaceBindingGroup

- **Plugin ID**: 68
- **Class ID**: 4456464

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Color** | Color | int16 | 0 | [ 0 , 26 ] | true | None | false |
| **GroupType** | Group Type | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Global | | 2 | User Binding Group | | 3 | User Binding Group Root | | 4 | Current Selection | | false | None | false |
| **HardwareControllerKey** | Controller Assignment | string |  | None | false | None | false |
| **ObjectIndexInView** | Object Index in View | int32 | 1 | [ 1 , 128 ] | true | None | false |
| **OverrideColor** | Override Color | bool | false | None | true | None | false |
| **TargetClassID** | Target Class ID | int32 | 0 | None | false | None | false |
| **TargetName** | Property | string |  | None | false | None | false |
| **TargetType** | Target Type | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Property | | 1 | Action | | 2 | Command | | false | None | false |