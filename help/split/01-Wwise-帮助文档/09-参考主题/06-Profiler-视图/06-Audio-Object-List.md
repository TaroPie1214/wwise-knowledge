# Audio Object List

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [参考主题](../00-参考主题.md) > [Profiler 视图](00-Profiler-视图.md) > Audio Object List

## Audio Object List

Audio Object List（音频对象列表）视图提供了总线管线内 Audio Object 的详细信息。视图以树状结构显示了在当前性能分析器光标时间位置实例化的总线和 Audio Object。

Audio Object List 还可显示总线的不同效果器处理阶段。总线上插入的效果器可修改、删除或创建 Audio Object。比如，Reflect 可根据游戏数据创建新的 Audio Object。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若要在此视图中显示信息，则须在 [“Profiler Settings”一节](../01-工程/10-Profiler-Settings.md "Profiler Settings") 中启用 **Audio Object Data** 以捕获数据，同时在捕获会话中选择时间点。 |

|  |  |
| --- | --- |
| [备注] | 备注 |
| Audio Object List 视图中不显示 Not Mixing 状态的总线。有关总线处理状态的详细信息，请参阅[“了解总线图标和处理状态”一节](../../07-完善工程/01-管理输出/11-完成终混/01-了解总线图标和处理状态.md "了解总线图标和处理状态")章节。 |

| 筛选器工具栏 | |
| --- | --- |
| This view includes a filtering toolbar, which allows you to reduce the amount of information displayed in the view so you can focus on specific elements. 有关更多详细信息，请参阅 [“在性能分析视图中筛选数据”一节](../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/03-在性能分析视图中筛选数据.md "在性能分析视图中筛选数据") 章节。 | |
|  | |
|  | **Unlink Filter**：禁止在多个筛选器视图之间同步。 |
|  | **Text Filter**：通过指定文本来筛选内容。系统会将您所指定的字词与内容中所含名称或字符串的开头进行匹配。键入的字词越多，显示的结果越细化。匹配项不区分大小写。有关高级用法的信息，请参阅“[“使用性能分析器筛选器表达式”一节](../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/04-使用性能分析器筛选器表达式.md "使用性能分析器筛选器表达式")”。 |
|  | **Object Filter**：通过指定 Wwise 对象来筛选内容。系统会将您所指定的 Wwise 工程对象与视图中的内容进行匹配。同时，还会依据对象关系（如父子对象关系和输出总线关系）对内容进行匹配。 |
|  | **Browse Object Filter**：显示 Project Explorer 浏览器，以便选择所要筛选的对象。 |
|  | **Mute/Solo Filtering**：若启用，则从结果中排除激活了 Mute 的对象，而只显示激活了 Solo 的对象。 |
|  | **Options**：显示其他操作。 |

| 界面元素 | 描述 |
| --- | --- |
|  | Click the View Settings icon in the upper right corner of the view to open the [“Profiler Settings”一节](../01-工程/10-Profiler-Settings.md "Profiler Settings") dialog, where you can specify the type of data to capture. |
| Item | 条目。显示设备、总线、阶段和 Audio Object 的名称。若 Audio Object 本身没有名称，则显示发起对象 (Instigator) 的名称。 |
| Game Object | 游戏对象。显示与条目关联的游戏对象的名称。对于总线，该项为与总线关联的游戏对象（如有）。对于 Audio Object，该项为与 Instigator 关联的游戏对象。 |
| Pipeline ID | 管线 ID。对于总线，显示总线的管线 ID。  对于 Audio Object，显示 Audio Object 的 Instigator 的管线 ID。  Instigator 是指用来创建 Audio Object 的管线元素。Instigator 既可以是总线管线元素，也可以是声部管线元素。Instigator 还可定义 Audio Object 上插入的元数据。  在有些情况下，Audio Object 可引用已经不存在的 Instigator。比如对于效果器尾音，用来创建 Audio Object 的管线元素就可能已被终止。在这种情况下，名称可能只能引用管线 ID。这时可通过在筛选器工具栏中前缀 pipelineId: 来在 Voice Monitor（声部监控器）中查找管线元素。 |
|  | 仅在列表中显示处于 Pre-Effects stage（效果器前处理阶段）的 Audio Object。Pre-Effects stage 设在对效果器进行处理之前。在对总线实施混音时（详见[“了解总线图标和处理状态”一节](../../07-完善工程/01-管理输出/11-完成终混/01-了解总线图标和处理状态.md "了解总线图标和处理状态")章节），Pre-Effects stage 位于混音阶段之后。 |
|  | 仅在列表中显示处于 Post-Effects stage（效果器后处理阶段）的 Audio Object。  Post-Effects stage 设在对所有效果器进行处理之后。  若总线上未插入效果器，则 Pre-Effects stage 和 Post-Effects stage 没有区别。 |
|  | 显示处于各个效果器处理阶段（包括 Pre-Effects stage）的 Audio Object。  在这种情况下，将监控各个效果器前后的所有 Audio Object。 |
|  | 定义采用哪种模式来显示电平表。  - **Peak**：标准显示模式。显示各个声道。这些值代表绘制区域的峰值 PCM 值，单位：分贝。 - **RMS**：显示 RMS（均方根）值。折叠所有声道。这些值代表绘制区域的峰值 RMS 值。 |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
|  | 在有 Instigator 对象时，可使用这些按钮来控制 Instigator 对象的 Mute 和 Solo 状态，并显示 Instigator 对象的隐式 Mute 和 Solo 状态。  若 Instigator 对象设为 Mute 状态，则在当前监控会话中将该 Instigator 对象静音。若 Instigator 对象设为 Solo 状态，则将工程中除此之外的所有其他对象静音。  粗体 **M** 或 **S** 表示将 Instigator 对象显式设为了 Mute 或 Solo 状态。淡色非粗体 **M** 或 **S** 表示通过另一对象的状态将 Instigator 对象隐式设为了 Mute 或 Solo 状态。  若 Instigator 对象隐式设为 Mute 状态，则将子级对象静音。  若 Instigator 对象隐式设为 Solo 状态，则将同级对象静音，并将子级和父级对象隐式设为 Solo 状态。  |  |  | | --- | --- | | [备注] | 备注 | | Mute 和 Solo 仅用于监视目的，而不会保存在工程中或存储在 SoundBank（声音包）中。 | |
|  | 在 [“Audio Object 3D Viewer”一节](05-Audio-Object-3D-Viewer/00-Audio-Object-3D-Viewer.md "Audio Object 3D Viewer") 中显示处于效果器处理阶段的对象时，Visibility（可见性）图标为激活状态 ()；在没有显示所述对象时，图标为停用状态 ()。 |
| Item | 参见上述说明。 |
| Game Object | 参见上述说明。 |
| Audio Object ID | 音频对象 ID。显示 Audio Object 的唯一 ID。每次将 Audio Object 发送到父总线或辅助总线时其 ID 都会改变。Audio Object 经由效果器处理时 Audio Object ID 也会改变。 |
| Pipeline ID | 参见上述说明。 |
| 3D Spatialization | 3D 空间化。指示 Audio Object 是否应用了 3D 空间化效果。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |

**相关主题**

- [“了解基于对象的音频”一节](../../03-设置工程/07-建立输出总线的结构/03-了解基于对象的音频/00-了解基于对象的音频.md "了解基于对象的音频")
- [“对 Audio Object 实施性能分析”一节](../../07-完善工程/06-性能分析/12-对-Audio-Object-实施性能分析.md "对 Audio Object 实施性能分析")

---