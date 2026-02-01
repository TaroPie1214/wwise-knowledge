# State Group Property Editor

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Game Syncs 选项卡](../00-Game-Syncs-选项卡.md) > [States（状态）](00-States（状态）.md) > State Group Property Editor

#### State Group Property Editor

在 State Group Property Editor（状态组属性编辑器）中，您可以定义在同一 State Group 中两个 State 之间切换所需要的时间。例如，两个状态之间的音量可能有所不同，这时就可以定义需要过多久才应用第二个 State 的音量。可以选择对 State Group 内所有 state 使用默认过渡时间，也可以为 State Group 中的单个 state 设置自定义过渡时间。

| 界面元素 | 描述 |
| --- | --- |
| Name | State Group 的名称。 |
| Notes | 备注。State Group 的其它信息。 |
| **Transitions（过渡）** | |
| Default Transition Time | 默认过渡时间。State Group 中所有 State 之间的过渡时长。  Default value: 1  Range: 0 to 60 |
| **Custom Transition Time（自定义过渡时间）** | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| From | 源。过渡的源 State。 |
| Time | 时间。所选源 state 和目标 state 之间的过渡时长。 |
| 操作 | 目标。过渡的目标 State。  过渡的源 State 和目标 State 不得相同。 |
| （双向） | 指定该过渡时间是否将用于双向过渡。  选中该复选框后，过渡时间将同时用于两个 State 之间的正向和反向过渡。例如，当从源 state 过渡至目标 state 时，将应用您定义的过渡时间，反向过渡时也是这样。  取消选择后，过渡时间是单向的，即从左至右。即仅当从源 state 过渡至目标 state 时才应用过渡时间，在方向相反（从目标状态过渡至源状态）时不应用。 |
|  | 在 Custom Transition Time 表格中添加新条目，您可以在该表格中修改各个 state 之间的过渡时间。 |
|  | 移除 Custom Transition Time 表中的所选条目。 |

**相关主题**

- [“创建 State Group”一节](../../../../04-与游戏互动/03-使用-State/01-使用-State.md#working_with_states_creating_state_group "创建 State Group")
- [“创建 State”一节](../../../../04-与游戏互动/03-使用-State/01-使用-State.md#working_with_states_creating_state "创建 State")
- [“Defining transitions for all States in a State Group”一节](../../../../04-与游戏互动/03-使用-State/02-为-State-Group-内的-State-之间的切换设置过渡.md#defining_transitions_for_all_states_in_state_group "Defining transitions for all States in a State Group")
- [“Customizing transitions between States in a State Group”一节](../../../../04-与游戏互动/03-使用-State/02-为-State-Group-内的-State-之间的切换设置过渡.md#customizing_transitions_between_states_in_state_group "Customizing transitions between States in a State Group")

---