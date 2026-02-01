# Mixing Desk 和 Mixing Session

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Sessions 选项卡](../00-Sessions-选项卡.md) > Mixing Desk 和 Mixing Session

### Mixing Desk 和 Mixing Session

Mixing Desk（调音台）是一款灵活强大的调音台，它将各种属性组合到同一个视图中，以便能优化游戏的混音。您可以向 Mixing Desk 中添加任何对象或总线，然后定义通路、应用效果器和衰减 ShareSet、编辑 state 属性，以及修改工程中各个对象和总线的属性。

如果您启动捕获会话，则还可在 Mixing Desk 中查看各个对象的活动，包括某声部何时播放、是否闪避总线以及是否旁通了效果器。还可以将各条总线设为静音，以便在音频混音中微调各个对象。

Mixing Desk 基本上就是一个网格，每列是一个混音器工具栏，每行对应于 Wwise 中的一组常用属性。每个混音器工具栏绑定至一个对象，对象的名称显示在各个工具栏的顶部和底部。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 在 Wwise 中，默认情况下您可以按 **F8** 来切换到 Mixer 布局。 |

混音器工具栏中的各个属性设置都有一个快捷菜单。这些菜单包含与所选属性相关的一组命令。要访问此快捷菜单，只需在混音器工具栏中右击属性设置。您还可以按任何顺序排列混音器工具栏，方法是将它们从一个位置拖至另一个位置。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 当选择多个对象时，修改某个属性（滑杆或者推子）会影响所有选中的对象，并将该对象的值设置为所有其它选中对象的值。但是，当按住 Alt 键并拖动滑杆或推子时，所选对象的值将被偏置而不是设为一个绝对值。 |

#### 结合使用 Control Surface 和 Mixing Desk

您可以将控制器（MIDI 硬件控制器）连接至混音台。有关说明，请参阅“[“理解 Control Surface 的 View Group”一节](../../../../08-使用-Wwise/14-使用控制设备/05-理解-Control-Surface-的-View-Group.md "理解 Control Surface 的 View Group")”。

在右键单击网格之外的区域时，会打开 Mixing Desk 快捷菜单，并显示 **Control Surface Bindings**（控制器绑定）子菜单。在该子菜单中，可选择要将会话中的哪个 State Group（状态组）用于 Mixing Desk 所关联的控制器绑定组。

在将 Control Surface Binding Group 用于 Mixing Desk 时，将默认使用各列中的关联对象进行绑定（**Session Objects** 菜单项）。但如果是从 **Control Surface Bindings** 子菜单中选择 State Group，则将使用该 State Group 的当前状态来绑定属性（如 Voice Volume）。

这在利用 Mixing Desk 测试混音状态时非常有用。您可以使用 **Follow States** 按钮将混音台设为自动跟随当前状态。这会影响控制器绑定。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 您可以通过键盘快捷方式或控制器绑定来执行各种全局命令，允许更改当前用于 Control Surface Bindings 的状态组，而无需使用快捷菜单。 |

| 界面元素 | 描述 |
| --- | --- |
| (Mixing Session 选择器) | 工程中当前存在的混音会话列表。  所选混音会话的名称会显示在对应字段内。 |
| Editing States | 编辑状态。与混音会话中的对象相关联的各个 State Group 的名称和相应 State。  当前所选状态会更改 Mixing Desk 中正在编辑的 State。 |
| Follow States | 若启用，则混音会话跟随游戏中的 State 变化。若禁用，则混音会话中的 State 将不跟随游戏中的 State 变化。 |
| Push States | When enabled, each time you change a State in the Editing States pane of the mixing session, the State also changes in the game, the Transport Control, and the Soundcaster. |
|  | Opens the Copy States Values dialog where you can copy the property settings from one State to another within the same State Group. |
| Activity | 活动。使用一系列图标指示总线或对象内是否存在任何音频活动。  您可以使用以下图标来监视各个对象或总线的活动：  - **Voice Playback** —— 指示正在播放对象。对于总线，它指示正在播放的声部信号正在通过总线。 - **Ducking** —— 指示是否正在闪避总线。 - **Effect Bypass**（效果器旁通）：指示插入的 Effect 是否被旁通。 |
| (Mute and Solo) | 控制对象的 Mute（静音）和 Solo（单独播放）状态，也会显示该对象是否处于被动静音和 Solo 状态。  将对象静音会使其在当前监听中无法听到。让对象 Solo 会使工程中的所有其它对象无声。  粗体的 **M** 或 **S** 表明已为对象主动设置了 Mute 或 Solo 状态。褪色的非粗体 **M** 或 **S** 表明对象的 Mute 或 Solo 状态是由于其它对象状态而被动设置的。  将对象静音会让其子对象被动静音。  让对象 Solo 会使同级对象被动静音，并让子对象和父对象被动 Solo。  |  |  | | --- | --- | | [技巧] | 技巧 | | 在点击 Solo 按钮的同时按住 Ctrl 键，可以强制仅 Solo 该 Solo 按钮所在的对象。 |  |  |  | | --- | --- | | [备注] | 备注 | | Mute 和 Solo 仅用于监视目的，而不会保存在工程中或存储在 SoundBank（声音包）中。 | |
| （电平表） | 每声道峰值电平表。有关扬声器配置和声道的详细信息，请参阅[“了解总线配置”一节](../../../../05-使用声音和振动来提升游戏体验/02-定义定位/11-了解总线配置.md "了解总线配置")。  信号电平为绿色，表明低于 -6 dB，黄色表明处于 -6 dB 至 0 dB 范围，红色表明高于 0 dB。  电平表数据源既可与当前正在播放的对象同步，也可在加载性能分析会话时与历史数值同步。在电平表显示性能分析会话历史记录时，可使用 Wwise 工具栏上的 **LIVE**（实时）按钮返回当前数值。  |  |  | | --- | --- | | [备注] | 备注 | | 对于 Not Mixing 状态的总线，不会显示电平表。有关各种处理状态的详细信息，请参阅[“了解总线图标和处理状态”一节](../../../../07-完善工程/01-管理输出/11-完成终混/01-了解总线图标和处理状态.md "了解总线图标和处理状态")章节。 | |
| 在将对象作为调音台通道条添加到 Mixing Session 中时，若与对象关联的属性设置为显示在 [“Mixing Desk Settings 对话框”一节](01-Mixing-Desk-Settings-对话框.md "Mixing Desk Settings 对话框") 中，则 Mixing Desk 会列出所有这些属性。有关这些属性的详细信息，请参阅对象的对应 Property Editor 文档（[“Busses hierarchy”一节](../../01-Audio-tab/02-Busses-hierarchy/00-Busses-hierarchy.md "Busses hierarchy")、[“Containers hierarchy: sound and motion objects”一节](../../01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/00-Containers-hierarchy-sound-and-motion-objects.md "Containers hierarchy: sound and motion objects") 或 [“Containers hierarchy: music objects”一节](../../01-Audio-tab/04-Containers-hierarchy-music-objects/00-Containers-hierarchy-music-objects.md "Containers hierarchy: music objects") 页面下）。 | |
|  | 加宽混音器工具栏。 |
|  | 将混音器工具栏重置为默认宽度。 |
|  | 缩窄混音器工具栏。 |

  

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 若选中多个调音台通道条（按住 Shift 或 Ctrl 并单击通道条标题栏），则修改 Volume（音量）、Pitch（音高）、Low-pass filter（低通滤波器）或 High-pass filter（高通滤波器）时会影响全部所选对象。 |

**相关主题**

- [“使用 Mixing Desk 进行混音”一节](../../../../07-完善工程/01-管理输出/11-完成终混/07-使用-Mixing-Desk-进行混音.md "使用 Mixing Desk 进行混音")
- [“了解 Mixing Desk”一节](../../../../07-完善工程/01-管理输出/11-完成终混/04-了解-Mixing-Desk.md "了解 Mixing Desk")
- [“自定义 Mixing Desk 中显示的信息”一节](../../../../07-完善工程/01-管理输出/11-完成终混/06-自定义-Mixing-Desk-中显示的信息.md "自定义 Mixing Desk 中显示的信息")
- [“创建 Mixing Session”一节](../../../../07-完善工程/01-管理输出/11-完成终混/05-建立-Mixing-Session.md#creating_mixing_session "创建 Mixing Session")
- [“将对象/总线添加到 Mixing Session”一节](../../../../07-完善工程/01-管理输出/11-完成终混/05-建立-Mixing-Session.md#adding_objects_busses_to_mixing_session "将对象/总线添加到 Mixing Session")
- [“对 Mixing Session 内的通道条重新排序”一节](../../../../07-完善工程/01-管理输出/11-完成终混/05-建立-Mixing-Session.md#reording_mixing_strips_within_mixing_session "对 Mixing Session 内的通道条重新排序")
- [“在 Mixing Session 内调节通道条的宽度”一节](../../../../07-完善工程/01-管理输出/11-完成终混/05-建立-Mixing-Session.md#resizing_mixing_strips_within_mixing_session "在 Mixing Session 内调节通道条的宽度")
- [“从 Mixing Session 中移除通道条”一节](../../../../07-完善工程/01-管理输出/11-完成终混/05-建立-Mixing-Session.md#removing_mixing_strips_from_mixing_session "从 Mixing Session 中移除通道条")

---