# Copy State Values（复制状态属性值）

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Game Syncs 选项卡](../00-Game-Syncs-选项卡.md) > [States（状态）](00-States（状态）.md) > Copy State Values（复制状态属性值）

#### Copy State Values（复制状态属性值）

The Copy States Values dialog allows you to copy the property settings from one custom State to another. 您可以将 State 值复制到同一 State Group 中的现有或新建 State。

| 界面元素 | 描述 |
| --- | --- |
| State Group | 状态组。State Group 的名称 |
| （State Group 选择器） | 显示工程中 State Group 的完整列表。  当您选择 State Group 时，其名称会显示在 State Group 字段中。 |
| From | 源。要复制属性值的源 state 名称。 |
| （State 选择器） | 显示所选 State Group 内的 State 列表。  当您选择 State 时，其名称会显示在 From 字段中。 |
| 操作 | 目标。State 值将被复制到的目标 State 名称。 |
| （State 选择器） | 显示所选 State Group 内的 state 列表。  要在所选 State Group 内创建新的 state，请点击“New”选项。  当您选择 State 时，其名称会显示在 To 字段中。 |
| **受影响的对象** | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Use | 使用。确定哪些对象将复制 State 值。 |
| Object Name | 对象名称。工程中采用了所选 State Group 的对象名称。  该列表中的对象是将受新复制 State 属性值影响的对象。 |
| 操作 | 动作。指定在将 State 值复制到 To 字段中所选 State 后的操作。可执行以下两种操作：  - **Overwrite existing state values** —— 当目标对象已使用自定义 state 属性时，这些属性将被所复制的属性设置覆盖。 - **Create new state values** —— 当对象使用默认 state 属性时，将使用复制的属性设置创建一个自定义版本。 |
|  | 选择列表中的所有对象。 |
|  | 取消选择列表中的所有对象。 |
|  | 将自定义属性设置将从源 state 复制到目标 state。 |
|  | Closes the dialog without copying the custom property settings. |

**相关主题**

- [“在 State 之间复制属性值”一节](../../../../04-与游戏互动/03-使用-State/03-将-State-指派给对象和总线/03-在-State-之间复制属性值.md "在 State 之间复制属性值")
- [“在对象之间复制 State Group”一节](../../../../04-与游戏互动/03-使用-State/03-将-State-指派给对象和总线/04-在对象之间复制-State-Group.md "在对象之间复制 State Group")

---