# Property Editor: Auxiliary Busses

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Audio tab](../00-Audio-tab.md) > [Busses hierarchy](00-Busses-hierarchy.md) > Property Editor: Auxiliary Busses

#### Property Editor: Auxiliary Busses

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

| Aux Bus | |
| --- | --- |
| 界面元素 | 描述 |
| **Specific** | |
| Bus Volume | 总线音量。Bus 或 Auxiliary Bus 上的音频信号衰减（电平或振幅）。有关音量的详细信息，请参阅 [理解声部管线](../../../../07-完善工程/01-管理输出/05-了解声部管线.md "了解声部管线") 页面。  |  |  | | --- | --- | | [备注] | 备注 | | 默认滑杆范围从 -96 至 +12。您可以通过直接输入数值或在聚焦于编辑控件之上时滑动鼠标来调到限值以上。Bus Volume 设置默认显示 Vertical Fader。若要切换到 Horizontal Slider，请右键单击 Volume 设置并选择 **Use Horizontal Slider for Volume**。 |  Default value: 0  Range: -200 to 200  Units: dB |
| Bus Configuration | 总线配置。决定采用哪种配置对总线输出进行格式化，其可能会影响总线的处理状态。您可以利用此设置将混音延迟到总线管线的后端，来节省 CPU 和内存资源或减少必须对总线上插入的效果器进行处理的声道数。  其中的可用选项包括：  - **Same as parent** - 该总线沿用父总线的总线配置，并有可能设为 Not Mixing 状态。藉此，可将总线的属性传给其输入而无需任何处理，从而节省 CPU 和内存资源。不过，若总线包含特定功能（如效果器），则会执行相应处理，也就没法节省资源了。有关更多详细信息，请参阅   [了解总线图标和处理状态](../../../../07-完善工程/01-管理输出/11-完成终混/01-了解总线图标和处理状态.md "了解总线图标和处理状态")   页面。 - **Same as main mix** - 该总线沿用总线管线末端 Audio Device 的 Main Mix 的总线配置。此选项允许在运行时由终端灵活地决定总线配置。 - **Same as passthrough mix** - 该总线沿用总线管线末端 Audio Device 的 Passthrough Mix 的总线配置。此选项允许在运行时由终端灵活地决定总线配置。若启用了 3D Audio 且终端支持 Passthrough Mix，则采用 2.0 配置对总线输出进行格式化。否则，会跟选中 **Same as main mix** 一样对总线实施处理。 - **Audio Objects** - 该总线会生成 Audio Object。这些 Audio Object 由音频缓冲区和 Metadata 构成，在满足所有条件的情况下可传给终端来进行渲染以获得空间化效果。  所有顶层总线（如 Main Audio Bus）的 Bus Configuration 都将自动设为 **Defined by device**。这是因为这些总线始终沿用关联 Audio Device 的总线配置。  有关列表中的上述及其他选项的详细信息，请参阅 [了解总线配置](../../../../05-使用声音和振动来提升游戏体验/02-定义定位/11-了解总线配置.md "了解总线配置") 页面。  Default value: Same as parent |

| General | |
| --- | --- |
| 界面元素 | 描述 |
| **Specific** | |
| Override Color | 不沿用颜色。启用 Color 滑块以便更改所选对象的色块。  Default value: false |
| Color | 颜色。在方块中显示对象颜色；如未设置，则显示随机颜色。此键有助于识别显示在坐标图视图中的对象线条。  Default value: 0  Range: 0 to 26 |

**相关主题**

- [“定义总线的相对属性”一节](../../../../03-设置工程/07-建立输出总线的结构/02-定义总线的属性.md#defining_relative_properties_of_bus "定义总线的相对属性")
- [“闪避信号”一节](../../../../03-设置工程/07-建立输出总线的结构/02-定义总线的属性.md#ducking_signals "闪避信号")
- [“将音乐替换为玩家自己的音乐”一节](../../../../03-设置工程/07-建立输出总线的结构/02-定义总线的属性.md#replacing_music_with_player_own_music "将音乐替换为玩家自己的音乐")

---