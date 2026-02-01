# Property Editor: Music Switch Container（属性编辑器：音乐开关容器）

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Audio tab](../00-Audio-tab.md) > [Containers hierarchy: music objects](00-Containers-hierarchy-music-objects.md) > Property Editor: Music Switch Container（属性编辑器：音乐开关容器）

#### Property Editor: Music Switch Container（属性编辑器：音乐开关容器）

The Property Editor contains the properties and behavior options for the selected Music Switch Container. 音乐对象属性决定了音乐在游戏中的听觉效果。音乐对象行为决定了在游戏任一时刻播放哪些音乐片段。

The General properties include relative properties, such as volume and Low-Pass Filter, as well as behaviors, including Switch type, tempo, and time signature.

有关绝对属性和相对属性的完整说明，请参阅[“About the properties of music objects”一节](../../../../06-创建互动音乐/02-Building-your-interactive-music-hierarchies/03-About-the-properties-of-music-objects.md "About the properties of music objects")。

For a description of the States, Transitions, and Stingers tabs, as well as the MIDI and
Advanced properties, refer to [“Common tabs and categories: music objects”一节](05-Common-tabs-and-categories-music-objects/00-Common-tabs-and-categories-music-objects.md "Common tabs and categories: music objects").

| General | |
| --- | --- |
| 界面元素 | 描述 |
| [name] | 对象的名称。 |
| (Object Color) | 显示对象的颜色。单击图标可打开颜色选择器。    选择一种颜色并将其应用于对象。在为对象选择某种颜色时，会在选定方块上显示调色板图标，并在右下角标注黄色三角（如图所示）。  若要沿用父对象的颜色，请选中颜色选择器最左侧的方块。 |
| (Mute and Solo) | 控制对象的 Mute（静音）和 Solo（单独播放）状态，也会显示该对象是否处于被动静音和 Solo 状态。  将对象静音会使其在当前监听中无法听到。让对象 Solo 会使工程中的所有其它对象无声。  粗体的 **M** 或 **S** 表明已为对象主动设置了 Mute 或 Solo 状态。褪色的非粗体 **M** 或 **S** 表明对象的 Mute 或 Solo 状态是由于其它对象状态而被动设置的。  将对象静音会让其子对象被动静音。  让对象 Solo 会使同级对象被动静音，并让子对象和父对象被动 Solo。  |  |  | | --- | --- | | [技巧] | 技巧 | | 在点击 Solo 按钮的同时按住 Ctrl 键，可以强制仅 Solo 该 Solo 按钮所在的对象。 |  |  |  | | --- | --- | | [备注] | 备注 | | Mute 和 Solo 仅用于监视目的，而不会保存在工程中或存储在 SoundBank（声音包）中。 | |
| (Show references) | 指示工程中有多少元素包含对对象的直接引用。若存在对对象的引用，则图标显示为橙色；若不存在此类引用，则图标显示为灰色。  通过单击该按钮，可打开 [“Reference View 视图”一节](../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")，并在 **References to:**（引用:）字段中查看对象的名称。 |
|  | Enter text in the search field to find specific properties or property groups. Results are displayed as you type. The search is not case-sensitive and searches all properties associated with an object, even if their category is not selected for display.  When a search is active, an **x** appears at the far-right side of the field and all category buttons are unavailable. Click the **x** to clear the search. |
| (Only Show Modified) | When selected, only properties that have been modified from their default value are displayed and all category filter buttons are unavailable. If a search is active, it is only applied to modified properties.  Modified properties are displayed with an orange band at the left side of the property list and at the left side of the corresponding category button. |
| (Show/Hide Category Filters) | Opens a list of all categories associated with the object currently loaded in the Property Editor. For each category selected in the list, a corresponding button is displayed at the top of the list of properties. Select these buttons to display the related properties. Ctrl+click or Shift+click to select multiple buttons.  **Always Show Additional Properties** expands the less frequently used properties, which are collapsed by default. |
| (More Options) | Opens the following options:  - **Reset Expand/Collapse to Default**: Returns to the default expansion. - **Collapse All**: Collapses all categories and groups in the Property Editor. - **Expand All**: Expands all categories and groups in the Property Editor. |
| (Open Property Editor Settings) | Opens the [“Object Property Settings”一节](../../12-搜索和工程全局编辑/06-Object-Property-Settings.md "Object Property Settings") dialog, which allows you to configure which properties are available for display in the Property Editor. |
| (Open in New Window) | Duplicates the Property Editor as a floating view. An instance of the editor remains in the Object Tab. |

| Music Switch Container | |
| --- | --- |
| 界面元素 | 描述 |
| **Specific** | |
| Playback Speed | 播放速度。调整音乐对象内容的播放速度：  - 若值等于 1，则正常播放 - 若值小于 1，则减速播放 - 若值大于 1，则加速播放  对于不同的媒体类型，Playback Speed 会产生不同的影响：  - WAV：播放内容时，音高将变高或变低。 - MIDI：播放内容时，速度将变快或变慢。  |  |  | | --- | --- | | [备注] | 备注 | | 此值与上级对象的 Playback Speed 相乘决定对象的实际播放速度。 |  |  |  | | --- | --- | | [备注] | 备注 | | 在 Interactive Music 播放实例期间，会将活跃 Segment 的实际播放速度应用于同一播放实例的所有在播 Segment。这在应用交叉淡变的情况下在两个段落之间实施过渡时尤其重要。淡入（现在活跃）的 Segment 的播放速度会应用于淡出（之前活跃）的 Segment。 |  Default value: 1  Range: 0.25 to 4 |
| **Switch** | |
| Mode | 模式。在运行时触发的状态或切换开关有不只一条预定义路径可以匹配的情况下，指定声音引擎将选择哪条路径。  - **Best Match** – 最佳匹配。选择与运行时触发的状态或切换开关最匹配的路径。如果不能完全匹配，则将会选择具有最少通配符 (\*) 的路径。 - **Weighted** – 加权。基于各路径的权重值，随机选择匹配路径之一。  因为在路径中可以使用通配符（\*），所以可能同时有几条预定义的路径都能够匹配在运行时触发的状态或切换开关。  Default value: Best Match |
| Continue to play on Switch change | 切换开关改变时继续播放。决定在触发新的 Switch 时是否继续播放多个 Switch 中的音乐对象。  如果选择了此选项并且音乐对象位于两个 Switch 中，则音乐对象将继续播放，就像 Switch 没有发生切换一样。如果 Switch 发生切换但没有选择此选项，则音乐对象将在下一同步点停止播放，然后再从头开始播放。  Default value: true |
| **Time** | |
| Override parent | 不沿用父项。选择继承父对象的时间设置行为，还是在当前层级结构中自行定义。未勾选时，时间设置控制将不可用。  对于顶层对象，此选项将不可用。  Default value: false |
| Tempo | 速度。音乐对象的曲速和节拍。此设置应与原始音乐源（Source）的速度匹配。  速度和拍号设置将决定 Music Editor（音乐编辑器）中的时间标尺刻度，让您轻松地将同步点设定在下一拍、小节或网格处。  单位：BPM  Default value: 120  Range: 1 to 400 |
| Time Signature | 拍号。小节的节拍数量和长度。此设置应与原始音乐源（Source）的拍号匹配。  Default value: 4  Range: 1 to 64 |
| Time Signature | 拍号。小节的节拍数量和长度。此设置应与原始音乐源（Source）的拍号匹配。  Default value: 4 |
| **Time > Grid** | |
| Frequency | Music Segment 的网格线将按照指定的时长间隔进行划分。这将为音乐段落添加另一个划分精度，让您在为音乐过渡、状态更改和插播乐句定义同步点时，有更大的灵活性。  选择了 Next Grid（下一格）选项时，Frequency 和 Offset（偏置）设置将影响状态更改、过渡和插播乐句的行为。  Default value: 4 Bars |
| Offset | 偏置。针对指定频率值进行的偏置。您可以从列表中选择标准偏置值，或创建自定义偏置值（单位为毫秒）。  Default value: No |
| Offset Ms | 偏置 (ms)。按毫秒显示偏置。在指定 Custom 偏置时适用。  Default value: 0  Range: 0 to 99999 |

| General | |
| --- | --- |
| 界面元素 | 描述 |
| **Specific** | |
| Override Color | 不沿用颜色。启用 Color 滑块以便更改所选对象的色块。  Default value: false |
| Color | 颜色。在方块中显示对象颜色；如未设置，则显示随机颜色。此键有助于识别显示在坐标图视图中的对象线条。  Default value: 0  Range: 0 to 26 |
| Inclusion | 启用。决定是否在生成 SoundBank 时在其中包含相应元素。如勾选，则包含该元素。如未勾选，则不会包含该元素。  为了针对各个平台来优化声音设计，有时需在特定平台上弃用某些元素。在默认情况下，此复选框会应用于所有平台。使用复选框左侧的 [Link 标志](../../../../08-使用-Wwise/03-了解-Property-Editor/11-使用-Property-Editor.md#linking_unlinking_property_values "Linking or unlinking property values") 来取消链接相应元素。然后，便可根据平台来自定义复选框的状态。  若取消选中此选项，则将禁用编辑器中的属性和行为选项。  Default value: true |
| **Voice** | |
| Voice Volume | 对象输出到总线或发送至辅助总线之前的衰减（电平或振幅）。有关音量的详细信息，请参阅 [理解声部管线](../../../../07-完善工程/01-管理输出/05-了解声部管线.md "了解声部管线") 页面。  |  |  | | --- | --- | | [备注] | 备注 | | 默认滑杆范围从 -96 至 +12 dB。您可以通过直接输入值或在编辑控件上移动鼠标来输入超出限制范围的值。 |  Default value: 0  Range: -200 to 200  Units: dB |
| Voice Low-pass Filter | 声部低通滤波器。基于指定频率值针对高频进行衰减的递归滤波器。  此滤波器的单位表示低通滤波的百分比，其中 0 表示无低通滤波（信号不受影响）而 100 表示最大衰减。  有关更多详细信息，请参阅 [Wwise 中 LPF 和 HPF 值与截止频率的对应关系](../../../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/02-定义相对属性（音量、音高、LPF、HPF）/01-Low-pass-和-High-pass-Filter-值与截止频率的关系.md#wwise_lpf_value_cutoff_frequencies "Wwise 中 LPF 和 HPF 值与截止频率的对应关系") 页面。  单位：%  Default value: 0  Range: 0 to 100 |
| Voice High-pass Filter | 声部高通滤波器。基于指定频率针对低频进行衰减的递归滤波器。  此滤波器的单位表示高通滤波的百分比，其中 0 表示无高通滤波（信号不受影响）而 100 表示最大衰减。  有关更多详细信息，请参阅 [Wwise 中 LPF 和 HPF 值与截止频率的对应关系](../../../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/02-定义相对属性（音量、音高、LPF、HPF）/01-Low-pass-和-High-pass-Filter-值与截止频率的关系.md#wwise_lpf_value_cutoff_frequencies "Wwise 中 LPF 和 HPF 值与截止频率的对应关系") 页面。  单位：%  Default value: 0  Range: 0 to 100 |
| Make-up Gain | 补偿增益。声部的音量增益（单位为分贝 (dB)），应用于所有其它音量调整后，。Make-up Gain 在各个 Container 之间是累加的。  请参阅 [理解声部管线](../../../../07-完善工程/01-管理输出/05-了解声部管线.md "了解声部管线") 以了解声音将如何经过处理、路由以及在哪些环节可以应用音量和效果器。  有关响度归一化的详细信息，请参阅 [使用响度归一化或补偿增益来调节音量](../../../../07-完善工程/01-管理输出/04-使用-Loudness-Normalization-或-Make-up-Gain-调节音量.md "使用 Loudness Normalization 或 Make-up Gain 调节音量") 。  |  |  | | --- | --- | | [备注] | 备注 | | 默认滑杆范围从 -96 至 +12。您可以通过直接输入值，或在编辑控件上移动鼠标来输入超出限制范围的值。 |  Default value: 0  Range: -96 to 96  Units: dB |

**相关主题**

- [“指定对象的输出连线”一节](../../../../07-完善工程/01-管理输出/01-指定对象的输出连线.md "指定对象的输出连线")
- [*管理效果器*](../../../../05-使用声音和振动来提升游戏体验/04-管理效果器/00-管理效果器.md "管理效果器")
- [“将 Music Switch Container 与 Game Sync 关联”一节](../../../../06-创建互动音乐/03-定义音乐对象播放行为/03-定义-Music-Switch-Container-的内容和行为.md#associating_music_switch_container_to_one_or_more_game_syncs "将 Music Switch Container 与 Game Sync 关联")
- [“定义 Music Switch Container 内各个音乐对象的行为”一节](../../../../06-创建互动音乐/03-定义音乐对象播放行为/03-定义-Music-Switch-Container-的内容和行为.md#defining_behaviors_of_music_objects_within_music_switch_containers "定义 Music Switch Container 内各个音乐对象的行为")
- [“定义音乐对象的 Time Settings”一节](../../../../06-创建互动音乐/03-定义音乐对象播放行为/01-定义音乐对象的-Time-Settings.md "定义音乐对象的 Time Settings")

---