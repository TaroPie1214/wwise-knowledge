# Property Editor: Main Audio and Main Secondary Busses

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Audio tab](../00-Audio-tab.md) > [Busses hierarchy](00-Busses-hierarchy.md) > Property Editor: Main Audio and Main Secondary Busses

#### Property Editor: Main Audio and Main Secondary Busses

The Property Editor contains the exact same properties for Main Audio Busses and Main Secondary Busses. 这是您为工程中的所有不同声音和音乐结构定义 Volume、LFE、Pitch 和 Low-Pass Filter 的最终层级。Where the Main Audio Bus final output is the primary audio system (be that a handheld device, television, or more elaborate speaker setup), the secondary main bus final output is a complementary audio output that might be available, such as a game controller. 这可以在 Audio Device 属性中选择， 仅在每个总线层级结构的最高级别可用。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 某些选项并非在所有平台上都可用。 |

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

| Bus | |
| --- | --- |
| 界面元素 | 描述 |
| **Specific** | |
| Bus Volume | 总线音量。Bus 或 Auxiliary Bus 上的音频信号衰减（电平或振幅）。有关音量的详细信息，请参阅 [理解声部管线](../../../../07-完善工程/01-管理输出/05-了解声部管线.md "了解声部管线") 页面。  |  |  | | --- | --- | | [备注] | 备注 | | 默认滑杆范围从 -96 至 +12。您可以通过直接输入数值或在聚焦于编辑控件之上时滑动鼠标来调到限值以上。Bus Volume 设置默认显示 Vertical Fader。若要切换到 Horizontal Slider，请右键单击 Volume 设置并选择 **Use Horizontal Slider for Volume**。 |  Default value: 0  Range: -200 to 200  Units: dB |
| **Audio Device** | |
| Audio Device | 音频设备。用于输出该总线所生成音频的音频设备。选择 Audio Device 部分中定义的现有 Audio Device ShareSet。若要使用第三方 Audio Device 插件，则可能需要先创建 ShareSet。  |  |  | | --- | --- | | [备注] | 备注 | | 若工程适用平台不支持指定的 Audio Device，则此字段将高亮显示为蓝色。同时，警告消息将指示无效的平台。此外，若尝试为无效的平台生成 SoundBank，则 [SoundBank Generation 选项卡](../../../02-视图/03-Logs-视图/00-Logs-视图.md#soundbank_generation_log "SoundBank Generation 选项卡") 中也将显示警告消息。 | |

| General | |
| --- | --- |
| 界面元素 | 描述 |
| **Specific** | |
| Override Color | 不沿用颜色。启用 Color 滑块以便更改所选对象的色块。  Default value: false |
| Color | 颜色。在方块中显示对象颜色；如未设置，则显示随机颜色。此键有助于识别显示在坐标图视图中的对象线条。  Default value: 0  Range: 0 to 26 |
| **Voice** | |
| Voice Volume | 对象输出到总线或发送至辅助总线之前的衰减（电平或振幅）。有关音量的详细信息，请参阅 [理解声部管线](../../../../07-完善工程/01-管理输出/05-了解声部管线.md "了解声部管线") 页面。  |  |  | | --- | --- | | [备注] | 备注 | | 默认滑杆范围从 -96 至 +12 dB。您可以通过直接输入值或在编辑控件上移动鼠标来输入超出限制范围的值。 |  Default value: 0  Range: -200 to 200  Units: dB |
| Voice Pitch | 声部音高。定义音频对象的播放速度。其中：  - 音高 0 = 正常速度。 - 音高 1,200 = 2 倍的速度。 - 音高 2,400 = 4 倍的速度。 - 音高 -1,200 = 0.5 倍的速度。 - 音高 -2,400 = 0.25 倍的速度  |  |  | | --- | --- | | [技巧] | 技巧 | | 1,200 音分相当于一个八度。 |  Default value: 0  Range: -2400 to 2400  Units: Cents |
| Voice Low-pass Filter | 声部低通滤波器。基于指定频率值针对高频进行衰减的递归滤波器。  此滤波器的单位表示低通滤波的百分比，其中 0 表示无低通滤波（信号不受影响）而 100 表示最大衰减。  有关更多详细信息，请参阅 [Low-pass 和 High-pass Filter 值与截止频率的关系](../../../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/02-定义相对属性（音量、音高、LPF、HPF）/01-Low-pass-和-High-pass-Filter-值与截止频率的关系.md "Low-pass 和 High-pass Filter 值与截止频率的关系") 。  Default value: 0  Range: 0 to 100 |
| Voice High-pass Filter | 声部高通滤波器。基于指定频率针对低频进行衰减的递归滤波器。  此滤波器的单位表示高通滤波的百分比，其中 0 表示无高通滤波（信号不受影响）而 100 表示最大衰减。  Default value: 0  Range: 0 to 100 |
| Make-up Gain | 补偿增益。声部的音量增益（单位为分贝 (dB)），应用于所有其它音量调整后，。Make-up Gain 在各个 Container 之间是累加的。  请参阅 [理解声部管线](../../../../07-完善工程/01-管理输出/05-了解声部管线.md "了解声部管线") 以了解声音将如何经过处理、路由以及在哪些环节可以应用音量和效果器。  有关响度归一化的详细信息，请参阅 [使用响度归一化或补偿增益来调节音量](../../../../07-完善工程/01-管理输出/04-使用-Loudness-Normalization-或-Make-up-Gain-调节音量.md "使用 Loudness Normalization 或 Make-up Gain 调节音量") 。  |  |  | | --- | --- | | [备注] | 备注 | | 默认滑杆范围从 -96 至 +12。您可以通过直接输入值，或在编辑控件上移动鼠标来输入超出限制范围的值。 |  Default value: 0  Range: -200 to 200  Units: dB |

**相关主题**

- [“定义相对属性（音量、音高、LPF、HPF）”一节](../../../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/02-定义相对属性（音量、音高、LPF、HPF）/00-定义相对属性（音量、音高、LPF、HPF）.md "定义相对属性（音量、音高、LPF、HPF）")

---