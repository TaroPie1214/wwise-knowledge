# Source Editor：Impacter

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > [Impacter](00-Impacter.md) > Source Editor：Impacter

### Source Editor：Impacter

Source Editor（源编辑器）会显示所有与 Impacter 插件关联的属性。

如需概括了解 Impacter 插件，请参阅 [“Impacter”一节](00-Impacter.md "Impacter") 章节。

| 界面元素 | 描述 |
| --- | --- |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Name | 名称。用户为此 Impacter 插件实例设定的名称。 |
| Source Plugin | 源插件。源插件的类型。 |
| Notes | 备注。有关 Impacter 插件的其他信息。 |
|  | 设置 Source Editor 中选定标签页的显示方式。默认情况下，整体面板中仅显示一个选定标签页。不过，您可以通过单击分隔器按钮将面板沿横向或纵向一分为二，显示两个不同的标签页。当前所选选项将以高亮背景色显示。  |  |  | | --- | --- | | [备注] | 备注 | | 无法同时在两个面板中显示同一标签页。若选中的标签页已在另一面板中显示，则另一面板将自动显示另一标签页。 | |
| **Effect Settings** | |
| **File Input** | |
| Audio Source | 音频源。音频源文件的名称。 |
| Impact Selection | 撞击选择。选择将哪个撞击分层添加到 SoundBank 以供随机挑选用来合成。  若有多个撞击分层，则随机选择时始终避免播放之前播放的撞击分层。  撞击分层包含分析当中剩余用来驱动合成的音频。其可与来自其他文件的主体分层结合用来进行交叉合成。  若 Solo 撞击分层，则会在设计工具中单独将其选中以供试听。Solo 设置不会应用于 SoundBank。  最多 64 个文件。 |
| Body Selection | 主体选择。选择将哪些主体分层添加到 SoundBank 以供随机挑选用来合成。  若只有一个撞击分层，则随机选择时仅避免重复播放之前播放的主体分层。  主体分层包含通过音频分析提取的一系列合成参数。其可与来自其他文件的撞击分层结合用来进行交叉合成。  若 Solo 主体分层，则会在设计工具中单独将其选中以供试听。Solo 设置不会应用于 SoundBank。  最多 64 个文件。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../../09-参考主题/04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../../09-参考主题/04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../../09-参考主题/04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../../09-参考主题/04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 添加文件。允许浏览其他文件。 |
|  | 删除所有文件。从插件中删除所有文件。 |
| **Impact Params** | |
| Mass | 质量。以独特方式对声音实施时间拉伸、音高变换或信号压缩，来改变听者对发声体大小或重量的直观感受。仅在撞击的开头应用 RTPC 更新。  Default value: 1.0  Range: 0.01 to 2.0 |
| Mass Random | 质量随机。对 Mass 参数施加正的随机偏置。  Default value: 0.0  Range: 0.0 to 2.0 |
| Velocity | 速度。影响撞击的强度，进而改变声音的音色和振幅。仅在撞击的开头应用 RTPC 更新。  Default value: 1.0  Range: 0.05 to 1.0 |
| Velocity Random | 速度随机。对 Velocity 参数施加负的随机偏置。  Default value: 0.0  Range: -1.0 to 0 |
| Position | 位置。塑造声音的音色，产生在表面多个不同位置发生撞击的效果。仅在撞击的开头应用 RTPC 更新。  Default value: 0.0  Range: 0.0 to 1.0 |
| Position Random | 位置随机。对 Impact Position 参数施加正的随机偏置。  Default value: 0.0  Range: 0.0 to 1.0 |
| Roughness | 粗糙度。为声音增添金属般的不和谐效果。仅在撞击的开头应用 RTPC 更新。  Default value: 0  Range: 0.0 to 1.0 |
| Roughness Random | 粗糙度随机。对 Roughness 参数施加正的随机偏置。  Default value: 0.0  Range: 0.0 to 1.0 |
| Min Duration | 最小时长。设置循环或结束播放事件之前的最小时长。若最小时长大于撞击分层，则附加无声内容。仅在撞击的开头应用 RTPC 更新。  Default value: 0.0  Range: 0.0 to 10.0 |
| Output Level | 输出电平。应用于最终信号的电平。仅在撞击的开头应用 RTPC 更新。  Default value: 0  Range: -96 to 24  Units: dB |

---