# 认识 Project Explorer 视图

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > 认识 Project Explorer 视图

## 认识 Project Explorer 视图

Project Explorer 是管理 Wwise 工程中所有元素的工具。在它的各个选项卡中，您可以创建、重命名、剪切、复制、粘贴和删除选项卡层级结构中显示的独特元素。各个选项卡还包含工具栏，您可以通过它快速将父对象和子对象添加到工程层级结构。在此中心位置，您可以组织和管理 Wwise 工程的各种元素，包括音频、音乐和振动素材、Bus、Event、SoundBank、Game Sync 等。

在 Project Explorer 中，您还可以将工程元素分成工作单元，让团队的每个成员同时处理工程的不同部分。有关创建工作单元的详细信息，请参阅[“将工程分成 Work Units”一节](../../03-设置工程/04-Working-with-a-team/01-将工程分成-Work-Units.md "将工程分成 Work Units")/>。

Project Explorer 包含以下选项卡：

- **Audio** —— 包含工程中的所有声音、音乐、振动和 Bus 结构。
- **Events** —— 包含工程中的所有事件（动作和对白）。
- **SoundBanks**  —— 包括工程中的所有 SoundBank。
- **Game Syncs** —— 包含工程中的所有 State、Switch、Trigger 和 Game Parameter。
- **ShareSets** —— 包含工程中的所有效果和 Attenuation ShareSet。
- **Sessions** —— 包含工程中的所有 Soundcaster 会话。
- **Queries** —— 包含工程中的所有查询。

To navigate through the different levels in the Project Explorer, you can expand and
collapse the groups by clicking the expander arrows beside each object. Hold Ctrl while
clicking the expander arrow to expand/collapse all child nodes.

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| Press the right and left arrow keys or the plus (+) and minus (-) keys in the number pad to expand or collapse a selected group one node level. 此外，还可按下数字小键盘中的斜线 (/) 和星号 (\*) 键，来展开和折叠分组内的所有子节点。 |

![](../../../images/pe_expand_work_unit.png)

|  |  |
| --- | --- |
|  | 展开 Work Unit。 |
|  | Work Unit 的内容。 |

## Visual elements in the Project Explorer

Wwise 使用不同的图标表示工程中的各个对象和元素，方便您在 Project Explorer 和界面其它位置中找到不同对象和元素类型。有关所有图标的完整列表和描述，请参阅[“理解 Wwise 中的视觉元素”一节](../../02-入门/03-Wwise-界面基础知识/01-理解-Wwise-中的视觉元素.md "理解 Wwise 中的视觉元素")。

Project Explorer 中还使用其它可视元素（例如颜色）来帮助识别特定对象的状态。例如，对象的颜色可指明它是否具有相关源，或者是否针对特定平台进行了转码。下表包含 Project Explorer 中使用的可视元素的列表。

| 可视元素 | 示例 | 用途 | 选项卡 |
| --- | --- | --- | --- |
| 星号 | |  | | --- | |  | | 对工作单元中的一个或多个工程元素进行了更改。保存工程时，星号将消失。 | 全部 |
| Link 图标 | |  | | --- | |  | | Link 图标为灰色时，表示该对象设置适用于所有平台。Wwise 可以让您同时针对多个平台进行制作，其方法是链接（Link）和取消链接（Unlink）与对象相关联的大多数属性值。默认情况下，对于所有活动平台，所有属性值都是链接在一起的，因此属性在各平台上的值相同。取消链接属性值可让您为特定平台自定义属性值。  关于链接和取消链接的详细信息，请参阅[“Customizing object properties per platform”一节](../../07-完善工程/02-管理平台和语言版本/01-Authoring-across-platforms.md#customizing_object_properties_per_platform "Customizing object properties per platform")。 | 音频和 ShareSet（用于效果器和 Audio Device） |
| 复选标记 | |  | | --- | |  | | 当对象名称旁边显示复选标记时，当前平台中包含该对象。当没有显示复选标记时，当前平台中不包含该对象。 | 音频和 ShareSet（用于效果器和 Audio Device） |
| 对象名称为红色 | |  | | --- | |  | | 创建了一个 Sound SFX 或音乐音轨，但没有与源相关联。 | Audio |
| 对象名称为蓝色 | |  | | --- | |  | | 与源相关联的 Sound SFX 或 Music Track 尚未针对当前平台进行转码。 | Audio |
| 对象名称为白色 | |  | | --- | |  | | 与源相关联的声音或音乐轨尚未针对当前平台进行转码。 | Audio |

若使用了版本控制插件，则 Project Explorer 中的 Work Unit（工作单元）上方将显示专用叠加图标以便识别工程文件的状态。例如，标记为 Add、Check-out 和 Check-in 的文件将使用不同的图标。有关叠加图标的详细信息，请参阅[“利用版本控制插件管理工程文件”一节](../../03-设置工程/04-Working-with-a-team/05-利用版本控制插件管理工程文件.md "利用版本控制插件管理工程文件")。

## 在 Project Explorer 中工作

在 Project Explorer 中，您可以使用快捷菜单执行标准的 Windows 资源管理器（或 Mac Finder）命令，例如重命名、剪切、复制和粘贴。您还可以在选项卡内拖放工程元素，或者将工程元素拖放到 Wwise 界面中的其它视图中。请记住，每当您移动对象时，将影响父子关系。有关创建和管理这些元素及其关系的信息，请参阅以下各节：

- [“Building sound and motion hierarchies”一节](../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/03-Building-sound-and-motion-hierarchies.md "Building sound and motion hierarchies")
- [*Building your interactive music hierarchies*](../../06-创建互动音乐/02-Building-your-interactive-music-hierarchies/00-Building-your-interactive-music-hierarchies.md "Building your interactive music hierarchies")
- [*管理 Event*](../../04-与游戏互动/01-管理-Event/00-管理-Event.md "管理 Event")
- [*管理动态对话*](../../04-与游戏互动/02-管理动态对话/00-管理动态对话.md "管理动态对话")
- [*管理 SoundBank*](../../07-完善工程/07-管理-SoundBank/00-管理-SoundBank.md "管理 SoundBank")
- [“使用 Switch”一节](../../04-与游戏互动/04-使用-Switch/01-使用-Switch.md "使用 Switch")
- [*使用 State*](../../04-与游戏互动/03-使用-State/00-使用-State.md "使用 State")
- [*使用 RTPC*](../../04-与游戏互动/05-使用-RTPC/00-使用-RTPC.md "使用 RTPC")
- [*使用 Trigger*](../../04-与游戏互动/06-使用-Trigger.md "使用 Trigger")
- [*将 State 和 State Group 用于动态对话*](../../04-与游戏互动/07-将-State-和-State-Group-用于动态对话.md "将 State 和 State Group 用于动态对话")
- [*管理效果器*](../../05-使用声音和振动来提升游戏体验/04-管理效果器/00-管理效果器.md "管理效果器")
- [“管理多份衰减”一节](../../05-使用声音和振动来提升游戏体验/02-定义定位/07-应用衰减/01-管理多份衰减.md "管理多份衰减")
- [“Building simulations”一节](../../07-完善工程/03-创建模拟/01-Building-simulations.md "Building simulations")
- [“Creating queries”一节](../11-使用-Search、Query-和-Reference/03-Working-with-queries.md#creating_query "Creating queries")

除了标准命令之外，Project Explorer 快捷菜单还由例如包含和排除之类的命令，以及当前选项卡的特定命令，例如 Audio 选项卡中导入和转码音频文件的命令，和 SoundBank 选项卡中导入 SoundBank Definition 的命令。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 您可以在同一布局中同时打开多份 Project Explorer。 |

---