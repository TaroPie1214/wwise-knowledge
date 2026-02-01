# 理解 Wwise 中的视觉元素

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [入门](../00-入门.md) > [Wwise 界面基础知识](00-Wwise-界面基础知识.md) > 理解 Wwise 中的视觉元素

## 理解 Wwise 中的视觉元素

Wwise 使用多种图标或视觉标识，以帮助在界面中呈现不同的元素。以下表格说明了 Wwise 中所用的不同视觉元素。

| 图标 | Name | 代表 |
| --- | --- | --- |
|  | Physical Folder（实文件夹） | 物理文件夹。该文件夹代表磁盘上的实际目录。所有 Wwise Work Unit 都存放在 Physical Folder 内。 |
|  | Virtual Folder（虚拟文件夹） | 可以在整个 Project Explorer 中添加虚拟文件夹，用来将项目元素分组。 |
| **Busses Hierarchy Icons** | | |
|  | Audio Bus（音频总线） | 一种声音对象分组，您可通过它处理游戏内不同的结构。例如，您可将所有环境声结构编组为一个音频总线，将所有玩家角色声音结构编组为另一个音频总线。 |
|  | Auxiliary Bus | 辅助总线。对工程中各处的声音对象进行细分，以便调节音量、总线配置、定位和 RTPC，并在回馈到父级 Audio Bus 前应用效果器或状态。在 Auxiliary Bus 中无法调节闪避、HDR 和声部混音。 |
| (Audio Bus)    (Auxiliary Bus) | Mixing | Wwise 可将该处理状态应用于 Audio Bus 和 Auxiliary Bus。对于 Mixing 状态的总线，会将其属性传递给发送到总线和子总线的对象。在这种情况下，将对总线上定义的所有效果器进行处理，最终采用基于声道的格式予以输出。  |  |  | | --- | --- | | [注意] | 注意 | | 在将声音发送到 Mixing 状态的总线时，会忽略与该声音关联的元数据或将其用在基于声道的混音中。此元数据既无法恢复也不能再用于 Audio Object 处理器或终端。 |  有关更多详细信息，请参阅 [“了解总线图标和处理状态”一节](../../07-完善工程/01-管理输出/11-完成终混/01-了解总线图标和处理状态.md "了解总线图标和处理状态") 章节。 |
| (Audio Bus)    (Auxiliary Bus) | Processing Audio Objects | Wwise 可将该处理状态应用于 Audio Bus 和 Auxiliary Bus。此类总线的所有属性都会传递给发送到总线和子总线的对象。在这种情况下，将对总线上定义的所有效果器进行处理，最终作为 Audio Object 予以输出。  有关更多详细信息，请参阅 [“了解总线图标和处理状态”一节](../../07-完善工程/01-管理输出/11-完成终混/01-了解总线图标和处理状态.md "了解总线图标和处理状态") 章节。 |
| (Audio Bus) | Not Mixing | Wwise 可将该处理状态应用于 Audio Bus。对于 Not Mixing 状态的总线，会将其属性传递给发送到总线和子总线的对象，但不会实施任何处理，也不会修改对象及子对象的格式。在这种情况下，将在声部层级把 Not Mixing 状态的总线上设定的所有属性应用于所发送的对象。  有关更多详细信息，请参阅 [“了解总线图标和处理状态”一节](../../07-完善工程/01-管理输出/11-完成终混/01-了解总线图标和处理状态.md "了解总线图标和处理状态") 章节。 |
| (Audio Bus)    (Auxiliary Bus) | Processing | Wwise 可将该处理状态应用于 Audio Bus 和 Auxiliary Bus。在 Wwise 声音引擎连接到终端并接收有关支持格式的信息时，将把该总线的处理状态解析为 Mixing 或 Processing Audio Objects。  |  |  | | --- | --- | | [备注] | 备注 | | When profiling in Wwise, the resolved status will be displayed in the Property Editor, but not in the Project Explorer. |  有关更多详细信息，请参阅 [“了解总线图标和处理状态”一节](../../07-完善工程/01-管理输出/11-完成终混/01-了解总线图标和处理状态.md "了解总线图标和处理状态") 章节。 |
| **Containers Hierarchy Icons** | | |
|  | Audio Source（音频源） | 音频文件与对象之间的独立抽象层。它链接到工程中导入的音频文件，并且音频源层级也是设置 Conversion Settings（针对活跃游戏平台）的位置。 |
|  | Source Plug-in（源插件） | 由 Wwise 外部的源插件创建的音频源。 |
|  | Sound SFX（音效声） | 包含声音效果的声音对象。 |
|  | Sound Voice（语音声） | 包含旁白或角色对话的声音对象。 |
|  | Work Unit（工作单元） | 可以通过独有的 XML 文件将工程拆分成独立单元，以便您团队中的不同成员同时处理工程的不同部分。这些 XML 文件可通过版本控制系统轻松管理。 |
|  | Property Container | A hierarchical structure of one or more sounds, containers, or Property Containers. You can use a Property Container to apply properties to all objects below it. |
|  | Blend Container（混合容器） | 该组中的对象或容器将被同时播放。在 Blend Container 中的声音和容器能够被编组到 Blend Track（混合轨）中，然后通过使用 RTPC 把这些声音的属性映射到游戏参数值上。在同一条Blend Track上的各个对象之间也可以基于游戏参数值来进行交叉淡变。 |
|  | Random Container （随机容器） | 该组中的的对象或容器将被随机播放。 |
|  | Sequence Container （序列容器） | 该组中的的对象或容器将根据特定顺序或播放列表播放。 |
|  | Switch Container（切换容器） | 该组中的对象或容器会被组织成与一系列切换开关或状态相符，当游戏调用相应的切换开关或状态时就会播放。 |
|  | Music Track （音乐轨） | 可以包含多个独立音乐片段音乐对象，并以波形形式显示它们，使您能够在音乐片段中以视觉方式进行调整。 |
|  | Music Track - Random Step （音乐轨 - 随机步进） | 每次播放其父段落时，将按随机顺序播放其子音乐轨。 |
|  | Music Track - Sequence Step （音乐轨 - 序列步进） | 每次播放其父级段落时，都将按照顺序播放其子音轨。 |
|  | Music Track - Switch | 将根据指定 Switch/State Group 中相关联的 Switch/State 来播放其子音轨。 |
|  | Music Segment （音乐段落） | 包含音乐轨的音乐对象，可使用同步点进行调整，在互动音乐中实现音乐编排。 |
|  | Music Playlist Container （音乐播放列表容器） | 由若干个段落按特定方式构成的一个编组，会按随机顺序或特定顺序播放这些段落。 |
|  | Music Switch Container（音乐切换容器） | 由若干个音乐段落和容器构成的一个编组，它们被组织成与一系列切换开关或状态相符，当游戏调用相应的切换开关或状态时就会播放。 |
| **其它工程元素图标** | | |
|  | Event | 触发游戏中音频或振动的方法，使用一个或一系列动作（如播放、静音和暂停）来控制若干个 Wwise 对象。 |
|  | Dialogue Event（对白事件） | A method to trigger audio, which may or may not be dialogue, or motion in game using a combination of State/Switch Groups and States/Switches arranged into paths that have been assigned to an object in the Wwise Containers hierarchy. |
|  | SoundBank | 事件、Wwise 对象和媒体的编组，可在游戏中特定时刻一起加载至游戏平台内存中。 |
|  | Switch Group （切换开关组） | 将相关的切换开关进行分组，用来管理游戏内指定元素在不同条件下的替代选项。 |
|  | Switch（切换开关） | 切换选项，用于游戏内指定元素在特定条件下播放声音。 |
|  | State Group | 将相关的状态进行分组，用来管理游戏环境中的全局更改。 |
|  | State（状态） | 对游戏音频属性所做的全局偏置或调整，使其符合游戏中物理及环境条件的变化。 |
|  | Game Parameter (RTPC) （游戏参数 (RTPC)） | 游戏中的参数，如赛车游戏中的速度和 RPM，可使用 RTPC 映射至 Wwise 属性值。 |
|  | Trigger （触发器） | 可由游戏中的特定操作触发播放的一小段音乐。 |
|  | Effect ShareSet （效果共享集） | 音频效果插件设定，可用于增强游戏中音频效果。这些设定保存为共享集，可在工程间共享。 |
|  | Attenuation ShareSet （衰减共享集） | 基于音源与听者之间相对距离而进行的音量衰减设定。这些设定保存为共享集，可在工程间共享。 |
|  | Conversion Settings ShareSet （转码设置共享集） | 转码设定包括采样率、音频格式和通道数量，可帮助定义音频输出的整体品质。这些设定已保存为共享集，可在工程间应用及共享。 |
|  | Soundcaster Session（声音选角器会话） | 按特定顺序集合一组声音、音乐、振动和事件模块，并与相关的游戏同步器设置一同保存，用来对游戏音频进行模拟。 |
|  | Mixing Session（混音会话） | 将一组总线或对象，与其各自属性一起在调音台界面内保存，用来对游戏的混音进行微调。 |
|  | Query （查询） | 一组特定的搜索条件，用于查找特定对象或对象元素。 |
| **Property Editor 和 Effect Editor 分隔器** | | |
|  | No split | 不分隔。编辑器将在一个标签页中显示信息。 |
|  | Column split | 列分隔。编辑器将在纵向面板中分左右两个标签页显示信息。 |
|  | Row split | 行分隔。编辑器将在横向面板中分上下两个标签页显示信息。 |
| **属性值标志** | | |

|  |  |  |
| --- | --- | --- |
|  | Link | 链接。属性值已链接到其它有效游戏平台的值。 |
|  | Unlink | 取消链接。属性值没有链接到其它有效游戏平台的值。 |
|  | Partial Unlink | 部分取消链接。当前平台的属性值已链接到其它有效平台，但其它平台的若干个相应值已取消链接。 |
|  | Link Mixed | 有些选定的对象具有不同的链接状态。有些可能是链接的，而另一些则是取消链接或部分取消链接的。 |

|  |  |  |
| --- | --- | --- |
|  | RTPC 已禁用 | 该属性值未绑定至游戏内参数值。 |
|  | RTPC 已启用 | 游戏内参数值已绑定至该属性值。这意味着，例如游戏赛车的速度可直接绑定至 Wwise 中的音调属性。当游戏中的赛车速度提高时，Wwise 中的音调也将实时提高。 |
|  | RTPC 部分启用 | Multi Editor 中只有部分对象为该属性绑定了游戏参数值。Property Editor 或 Contents Editor 中不会看到这个标识。 |

|  |  |  |
| --- | --- | --- |
|  | Randomizer 已启用 | 随机化器效果已应用到的属性值。 |
|  | Randomizer 已禁用 | 尚未应用随机化器效果的属性值。 |
|  | 随机化器 Mixed | Multi Editor 中只有部分对象为该属性值启用了 Randomizer 效果。Property Editor 或 Contents Editor 中不会看到这个标识。 |

|  |  |  |
| --- | --- | --- |
|  | State 已禁用 | 此属性值未与 State 绑定。 |
|  | State 已启用 | State Group 已与此属性值绑定。也就是说，所述属性（如 Volume）可能会随应用的 State 变化。 |
|  | State 混合情形 | State Group 绑定到了 Multi Editor 中加载的一个或多个对象（并非全部）的属性值。Property Editor 或 Contents Editor 中不会看到这个标识。 |

|  |  |  |
| --- | --- | --- |
| **属性底色** | | |
|  | "Unsupported feature (不支持的功能)" | 如果某一属性被显示为蓝色，则表示该功能在当前平台中不支持。 |
| **预设图标** | | |
|  | Save Preset （保存预设） | 该命令可将视图内所有值的当前状态保存至预设。 |
|  | Load Preset （加载预设） | 该命令可加载之前保存的预设。 |
| **"Source Control（版本控制）"** | | |
|  | "Source Control（版本控制）" | 已选中控件。在已选中控件周围显示的焦点边框（在使用 Wwise Classic 主题时显示为白色）。 |
| **视图图标** | | |
|  | Help | 帮助。该命令用于显示与特定视图、窗口或对话框相关的参考主题。The reference topic could be either online or offline, depending on your settings in the Help menu. 请参阅 [“Setting the Wwise documentation preferences”一节](../04-个性化您的工作空间/04-设置用户偏好.md#setting_documentation_preferences "Setting the Wwise documentation preferences")。 |
|  | View Settings （视图设置） | 视图设置。该命令用于显示包含一系列设置的对话框，以便定义要在视图中显示哪些内容。 |
|  | Selection Channel | 选定通道。该命令用于将视图切换至特定 Selection Channel (1-4)。  有关详细信息，请参阅 [“了解 Selection Channel 和 Meter Instance”一节](../04-个性化您的工作空间/01-处理视图/01-了解-Selection-Channel-和-Meter-Instance.md "了解 Selection Channel 和 Meter Instance") 章节。 |
|  | Close View | 该命令可关闭浮动视图。 |
| **Voice Inspector 图标** | | |
|  | Project Value | 工程值。在未连接游戏时，影响声部管线音量的基准音量值。 |
|  | SoundBank Value | 音频包值。在连接游戏时，影响声部管线音量的基准音量值。 |
|  | Live Value | 实时值。在连接游戏时，影响声部管线音量的属性值改变。 |
|  | API | 影响声部管线音量的API 调用。 |
|  | HDR | 影响声部管线音量的 HDR 窗口改变。 |
|  | 闪避 | 闪避。影响声部管线音量的闪避（降低音量）行为。 |
|  | Fade | 淡变。淡入或淡出：仅会在执行操作的过程中未显示时显示。 |
|  | Attenuation Distance | 衰减距离。影响声部管线音量的发声体与听者之间的距离。 |
|  | Blend Track（混合轨） | 混合音轨。影响声部管线音量的混合音轨。 |
|  | Cone Attenuation | 声锥衰减。影响声部管线音量的声锥角度衰减。 |
|  | Ray | 射线。影响声部管线音量的发声体与听者之间的射线距离。 |
|  | Occlusion or Transmission Loss | A ray occlusion or transmission, which drives a contribution to the voice pipeline. |
|  | Obstruction or Diffraction | A ray obstruction or diffraction, which drives a contribution to the voice pipeline. |
|  | Volume | 音量。影响声部管线音量的 Volume 属性/滑杆变化。 |
|  | Send Volume | 发送音量。影响声部管线音量的 Aux Bus Send Volume 属性/滑杆变化。 |
|  | Output Bus Volume | 输出总线音量。影响声部管线音量的 Output Bus Volume 属性/滑杆变化。 |
|  | Bus Volume | 总线音量。影响声部管线音量的 Bus Volume 属性/滑杆变化。 |
|  | Make-up Gain | 补偿增益。影响声部管线音量的音量补偿增益，在所有其他音量调节之后应用于声部。  |  |  | | --- | --- | | [备注] | 备注 | | 与其他音量调节不同，Make-up Gain 是在声部进行所有其他音量调节之后才应用于信号的。 | |
|  | Volume Mute | 音量 - 静音。Event 中影响声部管线音量的 Mute 动作。 |
|  | Volume Pause | 音量 - 暂停。Event 中影响声部管线音量的 Pause 动作。 |
|  | Low Pass | 低通。影响声部管线的 LPF 设置。 |
|  | Send Low Pass | 发送 - 低通。影响声部管线的辅助发送总线 LPF 设置。 |
|  | Output Bus Low Pass | 输出总线 - 低通。影响声部管线的输出总线 LPF 设置。 |
|  | High Pass | 高通。影响声部管线的 HPF 设置。 |
|  | Send High Pass | 发送 - 高通。影响声部管线的辅助发送总线 HPF 设置。 |
|  | Output Bus High Pass | 输出总线 - 高通。影响声部管线的输出总线 HPF 设置。 |
|  | Send Dual Shelf | A DSF, from an aux bus send, which drives a contribution to the voice pipeline. |
|  | Output Bus Dual Shelf | A DSF on the output bus, which drives a contribution to the voice pipeline. |
|  | Multiple Properties | 多项属性。影响声部管线 Volume、LPF 和 HPF 的多项属性。 |
|  | Send Multiple Properties | 发送 - 多项属性。影响声部管线的辅助发送总线的多项属性。 |
|  | Output Bus Multiple Properties | 输出总线 - 多项属性。影响声部管线的输出总线的多项属性。 |

---