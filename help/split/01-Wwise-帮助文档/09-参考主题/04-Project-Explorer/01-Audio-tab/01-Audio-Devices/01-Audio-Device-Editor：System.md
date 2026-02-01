# Audio Device Editor：System

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Audio tab](../00-Audio-tab.md) > [Audio Devices](00-Audio-Devices.md) > Audio Device Editor：System

#### Audio Device Editor：System

Audio Device Editor（音频设备编辑器）中包含一系列与 Audio Device 关联的属性。您可以实时修改其中的很多属性，并使用编辑器的 Effects（效果器）选项卡插入效果器。

下表列出并描述了 System Audio Device 所对应 Audio Device Editor 中包含的所有界面元素。

| General | |
| --- | --- |
| 界面元素 | 描述 |
| [name] | 名称。Audio Device 的名称。 |
| (Object Color) | 显示对象的颜色。单击图标可打开颜色选择器。    选择一种颜色并将其应用于对象。在为对象选择某种颜色时，会在选定方块上显示调色板图标，并在右下角标注黄色三角（如图所示）。  若要沿用父对象的颜色，请选中颜色选择器最左侧的方块。 |
| Inclusion | 启用。决定是否在生成 SoundBank 时在其中包含相应元素。如勾选，则包含该元素。如未勾选，则不会包含该元素。  为了针对各个平台来优化声音设计，有时需在特定平台上弃用某些元素。在默认情况下，此复选框会应用于所有平台。使用复选框左侧的 [Link 标志](../../../../08-使用-Wwise/03-了解-Property-Editor/11-使用-Property-Editor.md#linking_unlinking_property_values "Linking or unlinking property values") 来取消链接相应元素。然后，便可根据平台来自定义复选框的状态。  若取消选中此选项，则将禁用编辑器中的属性和行为选项。  Default value: true |
| (Show references) | 指示工程中有多少元素包含对对象的直接引用。若存在对对象的引用，则图标显示为橙色；若不存在此类引用，则图标显示为灰色。  通过单击该按钮，可打开 [“Reference View 视图”一节](../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")，并在 **References to:**（引用:）字段中查看对象的名称。 |
| Notes | 备注。有关 Audio Device 的其他信息。 |
|  | 设置 Audio Device Editor 中选定标签页的显示方式。默认情况下，整体面板中仅显示一个选定标签页。不过，您可以通过单击分隔器按钮将面板沿横向或纵向一分为二，显示两个不同的标签页。当前所选选项将以高亮背景色显示。  |  |  | | --- | --- | | [备注] | 备注 | | 无法同时在两个面板中显示同一标签页。若选中的标签页已在另一面板中显示，则另一面板将自动显示另一标签页。 | |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
| Allow 3D Audio | 允许 3D 音频。若启用该选项，则允许 Audio Device 尝试激活终端的 3D Audio 功能。若禁用该选项，则将停用所有 3D Audio 功能。  |  |  | | --- | --- | | [备注] | 备注 | | 启用该选项并不意味着一定会激活 3D Audio；只有在平台支持的情况下才会激活 3D Audio。 |  有关更多详细信息，请参阅 [了解基于对象的音频](../../../../03-设置工程/07-建立输出总线的结构/03-了解基于对象的音频/00-了解基于对象的音频.md "了解基于对象的音频") 页面。  Default value: false |
| Main Mix Configuration for Binauralization | 针对双耳合成的主混音配置。在激活 3D Audio 时，若终端使用针对双耳合成优化的 3D Audio 技术（比如在用户使用耳机时），则将此声道配置指派给 Main Mix。  Default value: Use Game-Defined Settings |
| Main Mix Configuration for Home Theater | 针对家庭影院的主混音配置。在激活 3D Audio 时，若终端使用针对家庭影院装置优化的 3D Audio 技术，则将此声道配置指派给 Main Mix。  Default value: Use Game-Defined Settings |
| Allow System Audio Objects | 允许系统音频对象。在激活 3D Audio 并启用该选项的情况下，若终端支持的 Audio Object 数量大于指定的阈值（即 **Minimum System Audio Objects Required** 的值），则允许 Audio Device 将 System Audio Object 发送到终端。  若禁用该选项，则禁止发送各个 System Audio Object。  在禁用时，会将 Audio Object 混音到 Main Mix，同时保留其空间特性。在这种情况下，最终的空间精度将取决于 Main Mix 的配置。  Default value: true |
| Minimum System Audio Objects Requirement | 最低系统音频对象要求。定义终端至少要支持多少个 System Audio Object，声音引擎才会生成 System Audio Object。  您可以使用此属性来确保将系统的 3D 音频处理能力保持在一定的水平。比如，在将该值设为 50 的情况下，若平台无法做到至少同时支持 50 个 Audio Object，则禁止其使用 System Audio Object。藉此，可避免尝试播放的对象超出系统支持的数量，进而导致对部分对象实施不同的混音处理。在这种情况下，将无法保证每次播放音频时都会产生相同的效果。  因此，该值应略微大于游戏在任意时刻可能播放的 System Audio Object 数量。  Default value: 32  Range: 0 to 65535 |
| Override Color | 不沿用颜色。启用 Color 滑块以便更改所选对象的色块。  Default value: false |
| Color | 参见上述说明。 |
| Inclusion | 参见上述说明。 |
| Audio > Effects | 音频 > 效果器。可插入或旁通的效果器。 |
| **Device Info** | |
| Is 3D Audio Active | 已激活 3D Audio。指示终端是否激活了 3D Audio 功能。 |
| Is Passthrough Active | 已激活直通。指示终端是否接收单独的 Passthrough Mix 以在终端旁通 3D 音频处理。 |
| Available System Audio Objects | 可用系统音频对象。终端支持的 System Audio Object 数量。 |
| System Audio Objects Used | 已用系统音频对象。当前正在播放的 System Audio Object 的数量。 |
| Main Mix Channel Configuration | 主混音声道配置。发送到系统终端的 Main Mix 的声道配置。 |
| Passthrough Channel Configuration | 直通声道配置。发送到系统终端的 Passthrough Mix 的声道配置。 |
| Main Mix Buffer Size | 主混音缓冲区大小。每个音频帧的采样数。 |

---