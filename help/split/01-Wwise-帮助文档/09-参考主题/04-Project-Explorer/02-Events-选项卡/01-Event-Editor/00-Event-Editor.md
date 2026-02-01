# Event Editor

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Events 选项卡](../00-Events-选项卡.md) > Event Editor

### Event Editor

在 Event Editor（事件编辑器）中，可管理工程内的 Action Event（动作事件）。Action Event 包含应用于不同对象或结构的各种动作，如 Play（播放）、Pause All（全部暂停）和 Stop All（全部停止）。这些 Event 会集成到游戏引擎中，并在游戏的不同时间点触发。每个 Event 都可包含多个 Action。您可以进一步为各个动作指定特定属性并应用特定条件。

Event Editor 中采用以下颜色来帮助识别 Event 内各个对象的状态：

- **白色**：适用于当前平台中所含对象。
- **灰色**：适用于当前平台中未包含的对象。
- **红色**：适用于缺少关联对象的 Event Action。若没有目标对象或无法找到指定目标，则 Target（目标）字段将显示红色边框。同时，对象名称也会显示为红色。

| 界面元素 | 描述 |
| --- | --- |
| Name | 名称。Event 的名称。各个 Event 的名称不可重复。 |
| Event ID | 事件 ID。与 Event 关联的标识号。Wwise 会为每个 Event 指派一个唯一的编号。  在游戏引擎不支持文本字符串时，可在工程中使用 Event ID 来代替 Event 名称。 |
| Notes | 备注。为 Event 附加的额外信息，方便进一步说明。 |
| Event Action | 事件动作。Event Editor 主窗格。此处可列出、添加、移除和编辑 Event 的 Action。 |
|  | 点击列标题区 **Configure Columns**（配置列）快捷方式（右键点击）选项。p  这时会打开 [“Object Property Settings”一节](../../12-搜索和工程全局编辑/06-Object-Property-Settings.md "Object Property Settings") 对话框。Select the individual properties for every possible Wwise object type that you want to display as a column. |
| 图标 | 图标可以代表单个 Action 类型，或按逻辑划分的一组 Action 类型。  **下面详细列出了各种不同图标：**   - 播放声音1 - : Stop - : Pause - : Resume - : Break - : Seek - : Post Event - : Volume - : Pitch - : LPF - : HPF - : Mute - : Game Parameter - : State - : Switch - : Trigger - : Bypass - : Reset Envelope - : Reset Playlist |
| Path | 路径。所选 Event 在工程层级结构内的位置。Event 旁边的方格中会列出 Action、Target 或例外数（设置 All 类型动作时）。  此字段为只读字段。 |
| Inclusion | 启用。决定是否在生成 SoundBank 时在其中包含相应元素。如勾选，则包含该元素。如未勾选，则不会包含该元素。  为了针对各个平台来优化声音设计，有时需在特定平台上弃用某些元素。在默认情况下，此复选框会应用于所有平台。使用复选框左侧的 [Link 标志](../../../../08-使用-Wwise/03-了解-Property-Editor/11-使用-Property-Editor.md#linking_unlinking_property_values "Linking or unlinking property values") 来取消链接相应元素。然后，便可根据平台来自定义复选框的状态。  若取消选中此选项，则将禁用编辑器中的属性和行为选项。  Default value: true |
| Notes | 备注。向特定 Event Action 添加的额外信息或注释。 |
| **Playback Limit（播放数限制）** | |
| For a complete description of the Event Limiting set of properties, See [“Event Limiting”一节](../../../../04-与游戏互动/01-管理-Event/04-Event-Limiting.md "Event Limiting"). | |
| Limit | The maximum number of concurrent instances of an Event that is allowed by the Event Limiting before Post Event commands are discarded. A value of 0 (displayed as Infinite) disables the property. |
| Cooldown Time | The time duration, in seconds, for which new Post Event commands will be discarded after a Post Event command is successfully processed. A value of 0 seconds disables the property. |
| Scope | The scope for which the Event Limiting properties are applied to Events. |
| **Event 属性** | |
| 有关 Event 属性列的完整列表和描述，请参阅 [“Event Action 列表”一节](01-Event-Action-列表.md "Event Action 列表") 参考表中的“Action 属性”列。 | |
| [Action 属性] | 该上下文窗格显示所选 Event Action 的所有属性。所列属性因 Event Action 列表中所选 Action 类型而异。可按照与 [“Multi Editor”一节](../../12-搜索和工程全局编辑/03-Multi-Editor.md "Multi Editor") 中大致相同的方式编辑这些设置。  若要查看各种 Event Action 属性的描述，直接单击下一页面（[“Event Action 列表”一节](01-Event-Action-列表.md "Event Action 列表")）中的相应 Action 链接即可。 |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Name | 名称。属性或行为的名称。此处所列属性或行为基于所选 Event Action。 |
| Value | 值。该属性值适用于所选 Event Action 的属性。这可以包括数值，但也可以是用于启用或禁用某些行为或属性的复选框。  对于数值字段（如音量），可指定更改相对属性还是绝对属性。在值之后添加 + 或 - 符号，可为所选对象属性创建偏置。在值之前添加符号，则会将对象属性更改为该绝对值。  根据情况，Value 列左侧可能会显示 Link（链接）标志，表示其是否适用于多个平台。详情请参阅 [“Linking or unlinking property values”一节](../../../../08-使用-Wwise/03-了解-Property-Editor/11-使用-Property-Editor.md#linking_unlinking_property_values "Linking or unlinking property values")。 |
|  | 在向 Event 添加 Action 时显示完整的选项列表。  为此，可打开并浏览 [“Project Explorer - Browser”一节](../../08-Project-Explorer-Browser.md "Project Explorer - Browser")，然后选择对象以自动应用相关 Action。或者，直接从列表分组中选择 Action。 |
|  | 移除所选 Event Action。 |
|  | [“Project Explorer - Browser”一节](../../08-Project-Explorer-Browser.md "Project Explorer - Browser") 将打开，可在其中选择想要为所选 Event Action 指派的 Target 的对象。 |
|  | Opens the [“Project Explorer - Browser”一节](../../08-Project-Explorer-Browser.md "Project Explorer - Browser") where you can select the target object that you want to **not** be included in the currently selected "All" type Action. 该例外会与其他例外一起直接显示在 Action 下方。Target 属性用于指定例外对象。例外列表可折叠或展开。不过，例外数量会始终显示在 Path 和 Target 字段中。 |

**相关主题**

- [“Event Action 列表”一节](01-Event-Action-列表.md "Event Action 列表")
- [“创建新的 Event”一节](../../../../04-与游戏互动/01-管理-Event/02-创建-Event.md#creating_new_event "创建新的 Event")
- [“将 Action 添加到 Event”一节](../../../../04-与游戏互动/01-管理-Event/02-创建-Event.md#adding_actions_to_an_event "将 Action 添加到 Event")
- [“将目标指派给 Event Action”一节](../../../../04-与游戏互动/01-管理-Event/02-创建-Event.md#assigning_objects_to_event_actions "将目标指派给 Event Action")
- [“定义 Event Action 的作用域”一节](../../../../04-与游戏互动/01-管理-Event/02-创建-Event.md#defining_scope_of_an_event_action "定义 Event Action 的作用域")
- [“设置 Event Action 的属性”一节](../../../../04-与游戏互动/01-管理-Event/02-创建-Event.md#setting_properties_for_an_event_action "设置 Event Action 的属性")
- [“播放 Event”一节](../../../../04-与游戏互动/01-管理-Event/02-创建-Event.md#playing_back_an_event "播放 Event")
- [“重命名事件”一节](../../../../04-与游戏互动/01-管理-Event/03-处理-Event.md#renaming_an_event "重命名事件")
- [“从 Event 中移除 Action”一节](../../../../04-与游戏互动/01-管理-Event/03-处理-Event.md#removing_actions_from_an_event "从 Event 中移除 Action")
- [“替换指派给 Event Action 的目标”一节](../../../../04-与游戏互动/01-管理-Event/03-处理-Event.md#replacing_objects_assigned_to_event_actions "替换指派给 Event Action 的目标")
- [“删除 Event”一节](../../../../04-与游戏互动/01-管理-Event/03-处理-Event.md#deleting_events "删除 Event")

---