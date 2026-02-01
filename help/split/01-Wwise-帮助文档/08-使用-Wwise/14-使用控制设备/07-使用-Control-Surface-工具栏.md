# 使用 Control Surface 工具栏

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > [使用控制设备](00-使用控制设备.md) > 使用 Control Surface 工具栏

## 使用 Control Surface 工具栏

在 Control Surface Session 处于活跃状态时，Wwise 界面顶部会显示 Control Surface Toolbar。您可以通过在 Control Surface Bindings 视图或 Control Surface Session Object Tab 中单击“激活”按钮来打开和关闭工具栏。

![](../../../../images/control_surface_toolbar.png)

|  |  |
| --- | --- |
|  | Control Surface Toolbar |
|  | 激活/停用 Control Surface Session |

Control Surface Toolbar 包含以下元素（从左向右排列）：

| 界面元素 | 描述 |
| --- | --- |
| 活跃 Control Surface Session | 显示当前活跃的 Control Surface Session。双击可在 Object Tab 中打开会话。 |
|  | 打开 Control Surface Session 列表。可通过从列表中选择会话来切换到不同的会话。 |
| 当前选中对象 | 显示当前选定对象。 |
| Last Property Changed | 显示上次使用 Control Surface Binding 修改的对象、属性和值（用滑杆表示）。 |
| 已加载的绑定组 | 这些按钮显示以下各[绑定组](04-创建-Control-Surface-Binding.md#binding_groups "绑定项存储在三个不同组内，每个组都具有定义目标对象的不同机制。")是否处于活跃状态:  - Global：全局。目标对象在全局绑定中定义。 - Current Selection：当前选中对象。目标对象为当前选中对象。 - View Group：视图组。目标对象通过指定视图在指定组中加载。比如，按钮可能会显示为 `YourGroup:Soundcaster`，表示工程中定义了名为 YourGroup 的 View Group 且其用在 SoundCaster 内。不同视图中可能会定义多个 View Group，因此有时会显示不止一个按钮。  单击分组名称可激活或停用分组。颜色变化用以指示分组状态：  - Active（活跃）：橙色 - Inactive：不活跃。灰色 |
|  | 停用 Control Surface Session 并关闭 Control Surface Toolbar。 |

---