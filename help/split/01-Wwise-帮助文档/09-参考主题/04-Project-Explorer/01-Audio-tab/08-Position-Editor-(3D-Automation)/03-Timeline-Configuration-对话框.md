# Timeline Configuration 对话框

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Audio tab](../00-Audio-tab.md) > [Position Editor (3D Automation)](00-Position-Editor-(3D-Automation).md) > Timeline Configuration 对话框

#### Timeline Configuration 对话框

The Timeline Configuration dialog is where you define the properties and behaviors of the Position Editor timeline. 您可以定义时间线的长度、新控制点键之间的时间间隔，以及缩短或延长时间线时现有关键帧如何反应。

| 界面元素 | 描述 |
| --- | --- |
| Length（长度） | 长度。定义时间线的长度，格式为 mm:ss.ms。时间线的最大长度为 59:59:999。 |
| Stretch proportionally | 当更改时间线的长度时，现有控制点键将重新定位，以保持它们在时间线上的相对位置。  该选项仅当时间线处于 Non-Linear 模式时才可用。 |
| Preserve key values | 保留键值。更改时间线的长度时，时间线上的控制点键保留各自的位置。  超出新时间线长度的控制点键将被删除。  该选项仅当时间线处于 Non-Linear 模式时才可用。 |
| Insert Key Every | 每隔 ... 插入键。每隔确定在时间线上插入控制点键时控制点键之间的时长。该选项仅作用于非线性模式。  默认值为一秒 (00:01:000)。 |
|  | Closes the Time Configuration dialog and applies the settings you selected. |
|  | Closes the Time Configuration dialog without applying any changes to the timeline. |

**相关主题**

- [“Changing the path duration”一节](../../../../05-使用声音和振动来提升游戏体验/02-定义定位/08-使用动画路径定义空间定位/01-使用动画路径.md#changing_path_duration "Changing the path duration")
- [“Configuring the positioning timeline”一节](../../../../08-使用-Wwise/08-认识时间线/02-Configuring-the-positioning-timeline.md "Configuring the positioning timeline")

---