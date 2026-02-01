# Switch Group Property Editor

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Game Syncs 选项卡](../00-Game-Syncs-选项卡.md) > [Switches（切换开关）](00-Switches（切换开关）.md) > Switch Group Property Editor

#### Switch Group Property Editor

在 Switch Group Property Editor（切换开关组属性编辑器）中，可将 Switch Group 内的各个 Switch 映射至特定的 Game Parameter（游戏参数）。>采用映射后，游戏传来的参数值将决定 Switch Container 内的哪个 Swtich 将激活，从而播放不同的声音、音乐或振动对象。而后根据游戏传递的参数值切换 Switch。

| 界面元素 | 描述 |
| --- | --- |
| Name | Switch Group 的名称。 |
| Notes | 备注。Switch Group 的其它信息。 |
| **Game Parameter（游戏参数）** | |
| Use Game Parameter | 使用游戏参数。决定 Switch Group 内的 Switch 是否映射至 Game Parameter 值。  如存在映射，则 Switch 可以由游戏传递的参数值驱动。  Default value: false |
| (坐标图) | 游戏参数（X 轴）和 Wwise 中 Switch Group 内各个 Switch（Y 轴）之间关系的图形化表示。 |
|  | 基于坐标图视图的中心进行放大。 |
|  | 将坐标图视图重置为默认的 1:1 缩放比例。 |
|  | 基于坐标图视图的中心进行缩小。 |
| **坐标** | |
| X | 所选控制点的 X 轴坐标。  如果选择了多个控制点，则字段显示 0 值，这时可以针对所有已选控制点的当前值，进行统一的增大或减小。例如，如果您选择两个控制点并在 X 文本框中输入 -5，则两个控制点都将向左移动 5 个单位。 |
| Y | 所选控制点的 Y 轴坐标。  如果选择了多个控制点，则字段显示 0 值，这时可以针对所有已选控制点的当前值，进行统一的增大或减小。例如，如果您选择两个控制点并在 Y 文本框中输入 -5，则两个控制点都将向下移动 5 个单位。 |
| （游戏参数） | 映射到此 Switch Group 内不同 Switch 的 Game Parameter 或 MIDI 控制器。  |  |  | | --- | --- | | [备注] | 备注 | | 若使用了 MIDI 控制器，则仅可在 MIDI 播放情境下使用 Switch Group。A MIDI playback context is any object in the Containers hierarchy that is played as a result of a MIDI note-on/off event.  比如，包含 MIDI 片段并指定了 Switch Container 作为其 MIDI 目标的 Interactive Music Segment。MIDI 片段的每个 "Note-On"/"Note-Off" Event 都会指向具有关联 MIDI 播放情境的 Switch Container。并且，指定的 MIDI 控制器（控制 Switch Group）上的每个 MIDI 控制器 Event 都会更新具有关联 MIDI 播放情境的 Switch Group。 | |
|  | Opens the New Switch dialog where you can name the Switch that you want to create. |

**相关主题**

- [“Creating Switch Groups”一节](../../../../04-与游戏互动/04-使用-Switch/01-使用-Switch.md#creating_switch_group "Creating Switch Groups")
- [“Deleting Switches or Switch Groups”一节](../../../../04-与游戏互动/04-使用-Switch/01-使用-Switch.md#deleting_switch_group_switch "Deleting Switches or Switch Groups")
- [“Creating Switches”一节](../../../../04-与游戏互动/04-使用-Switch/01-使用-Switch.md#creating_switch "Creating Switches")
- [“定义 Switch Container 的类型”一节](../../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/03-定义-Switch-Container-的内容和行为.md#defining_type_of_switch_container "定义 Switch Container 的类型")
- [“将 Game Parameter 值映射到 Switch”一节](../../../../04-与游戏互动/04-使用-Switch/02-将-Game-Parameter-值映射到-Switch.md "将 Game Parameter 值映射到 Switch")

---