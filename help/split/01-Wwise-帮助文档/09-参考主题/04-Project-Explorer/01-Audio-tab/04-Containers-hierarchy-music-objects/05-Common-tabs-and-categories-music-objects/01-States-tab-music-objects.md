# States tab: music objects

[Wwise 帮助文档](../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../00-参考主题.md) > [Project Explorer](../../../00-Project-Explorer.md) > [Audio tab](../../00-Audio-tab.md) > [Containers hierarchy: music objects](../00-Containers-hierarchy-music-objects.md) > [Common tabs and categories: music objects](00-Common-tabs-and-categories-music-objects.md) > States tab: music objects

##### States tab: music objects

在 State 选项卡中，您可以将 State 分配给音乐对象，以便进一步定义启用特定状态时的音乐特征。您可以使用默认的 State 属性，可以设置 State 值，也可以为当前音乐对象完全禁用某个 State。对于音乐对象，您还可以指定音乐中允许在哪些时间点响应状态变化。

| General | |
| --- | --- |
| 界面元素 | 描述 |
| [name] | 对象的名称。 |
| (Object Color) | 显示对象的颜色。单击图标可打开颜色选择器。    选择一种颜色并将其应用于对象。在为对象选择某种颜色时，会在选定方块上显示调色板图标，并在右下角标注黄色三角（如图所示）。  若要沿用父对象的颜色，请选中颜色选择器最左侧的方块。 |
| (Mute and Solo) | 控制对象的 Mute（静音）和 Solo（单独播放）状态，也会显示该对象是否处于被动静音和 Solo 状态。  将对象静音会使其在当前监听中无法听到。让对象 Solo 会使工程中的所有其它对象无声。  粗体的 **M** 或 **S** 表明已为对象主动设置了 Mute 或 Solo 状态。褪色的非粗体 **M** 或 **S** 表明对象的 Mute 或 Solo 状态是由于其它对象状态而被动设置的。  将对象静音会让其子对象被动静音。  让对象 Solo 会使同级对象被动静音，并让子对象和父对象被动 Solo。  |  |  | | --- | --- | | [技巧] | 技巧 | | 在点击 Solo 按钮的同时按住 Ctrl 键，可以强制仅 Solo 该 Solo 按钮所在的对象。 |  |  |  | | --- | --- | | [备注] | 备注 | | Mute 和 Solo 仅用于监视目的，而不会保存在工程中或存储在 SoundBank（声音包）中。 | |
| (Show references) | 指示工程中有多少元素包含对对象的直接引用。若存在对对象的引用，则图标显示为橙色；若不存在此类引用，则图标显示为灰色。  通过单击该按钮，可打开 [“Reference View 视图”一节](../../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")，并在 **References to:**（引用:）字段中查看对象的名称。 |

| States（状态） | |
| --- | --- |
| 界面元素 | 描述 |
|  | 打开 State Group 选择器，您可以在其中选择现有 State Group 或创建新的 State Group。 |
|  | 从采用的 State Group 列表中删除所选 State Group。 |
|  | [“State Properties 对话框 ”一节](../../09-State-Properties-对话框.md "State Properties 对话框") 将打开，您可以在其中指定哪些 State 属性适用于该对象。 |
|  | 复制状态值…。打开 Copy States Values 对话框。 |
| **属性列** | |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../../12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../../07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 点击列标题区 **Configure Columns**（配置列）快捷方式（右键点击）选项。p  对于 States 选项卡，会打开 [“State Properties 对话框 ”一节](../../09-State-Properties-对话框.md "State Properties 对话框")而非 Configure Columns 对话框。指定要为此对象使用的 State 属性。 |
| State（状态） | 状态。 分配给当前对象的 State 和 State Group。 |
| 表中显示的 State 属性包括所有在 [“State Properties 对话框 ”一节](../../09-State-Properties-对话框.md "State Properties 对话框") 中选择的对象特定[累积属性](../../../../../14-词汇表.md#glossary_additive_type_properties "Additive Type Property（累积型属性）")。The following rows give only the default State properties for music objects. 有关对象特定属性的信息，请参阅相应的 Property Editor 或 Property Editor 标签页。 | |
| Voice Volume（声部音量）。 | 对于特定状态，当前播放的对象所输出的电平或振幅将如何改变。  默认值：0 范围：-400 至 +400 单位：dB  |  |  | | --- | --- | | [备注] | 备注 | | 默认滑杆范围从 -96 至 +12。您可以通过直接输入值或在编辑控件上移动鼠标来输入超出限制范围的值。 | |
| Voice Low-pass Filter | 声部低通滤波器。基于指定频率值针对高频进行衰减的递归滤波器。  此滤波器的单位表示低通滤波的百分比，其中 0 表示无低通滤波（信号不受影响）而 100 表示最大衰减。  有关更多详细信息，请参阅 [Wwise 中 LPF 和 HPF 值与截止频率的对应关系](../../../../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/02-定义相对属性（音量、音高、LPF、HPF）/01-Low-pass-和-High-pass-Filter-值与截止频率的关系.md#wwise_lpf_value_cutoff_frequencies "Wwise 中 LPF 和 HPF 值与截止频率的对应关系") 页面。  单位：%  Default value: 0  Range: 0 to 100 |
| Voice High-pass Filter | 声部高通滤波器。基于指定频率针对低频进行衰减的递归滤波器。  此滤波器的单位表示高通滤波的百分比，其中 0 表示无高通滤波（信号不受影响）而 100 表示最大衰减。  有关更多详细信息，请参阅 [Wwise 中 LPF 和 HPF 值与截止频率的对应关系](../../../../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/02-定义相对属性（音量、音高、LPF、HPF）/01-Low-pass-和-High-pass-Filter-值与截止频率的关系.md#wwise_lpf_value_cutoff_frequencies "Wwise 中 LPF 和 HPF 值与截止频率的对应关系") 页面。  单位：%  Default value: 0  Range: 0 to 100 |
| Make-up Gain | 补偿增益。声部的音量增益（单位为分贝 (dB)），应用于所有其它音量调整后，。Make-up Gain 在各个 Container 之间是累加的。  请参阅 [理解声部管线](../../../../../07-完善工程/01-管理输出/05-了解声部管线.md "了解声部管线") 以了解声音将如何经过处理、路由以及在哪些环节可以应用音量和效果器。  有关响度归一化的详细信息，请参阅 [使用响度归一化或补偿增益来调节音量](../../../../../07-完善工程/01-管理输出/04-使用-Loudness-Normalization-或-Make-up-Gain-调节音量.md "使用 Loudness Normalization 或 Make-up Gain 调节音量") 。  |  |  | | --- | --- | | [备注] | 备注 | | 默认滑杆范围从 -96 至 +12。您可以通过直接输入值，或在编辑控件上移动鼠标来输入超出限制范围的值。 |  Default value: 0  Range: -200 to 200  Units: dB |
| Change occurs at: | 确定当前音乐对象响应 State 变化的时间点。以下选项可用：  - **Immediate** —— 立即切换状态。 - **Next Grid** —— 切换发生在下一个预定义网格间隔处。网格是可对音乐对象进行虚拟分割的任意方法。 - **Next Bar** —— 切换发生在下一小节处。 - **Next Beat** —— 切换发生在下一拍处。 - **Next Cue** —— 切换发生在下一提示点处。下一提示点可以是 Entry（入口）、Exit（出口）或自定义提示点。 - **Next Custom Cue** —— 切换发生在下一自定义提示点处。 - **Entry Cue** —— 切换发生在入口提示点处。 - **Exit Cue** —— 切换发生在出口提示点处。  如果正在播放多个音乐对象，则会在首次遇到符合条件的机会时，为所有音乐对象应用状态更改。 |

**相关主题**

- [“将 State 指派给对象和总线”一节](../../../../../04-与游戏互动/03-使用-State/03-将-State-指派给对象和总线/00-将-State-指派给对象和总线.md "将 State 指派给对象和总线")
- [“自定义对象的 State 属性”一节](../../../../../04-与游戏互动/03-使用-State/03-将-State-指派给对象和总线/02-自定义对象的-State-属性.md "自定义对象的 State 属性")
- [“为音乐对象设置 State 切换点”一节](../../../../../04-与游戏互动/03-使用-State/03-将-State-指派给对象和总线/01-为音乐对象设置-State-切换点.md "为音乐对象设置 State 切换点")
- [“创建 State Group”一节](../../../../../04-与游戏互动/03-使用-State/01-使用-State.md#working_with_states_creating_state_group "创建 State Group")
- [“创建 State”一节](../../../../../04-与游戏互动/03-使用-State/01-使用-State.md#working_with_states_creating_state "创建 State")

---