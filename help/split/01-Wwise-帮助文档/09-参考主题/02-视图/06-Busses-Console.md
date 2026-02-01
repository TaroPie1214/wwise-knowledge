# Busses Console

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [参考主题](../00-参考主题.md) > [视图](00-视图.md) > Busses Console

## Busses Console

The Busses Console gives you quick access to all the controls available for the Audio Busses in the Busses hierarchy. 在声音、音乐或振动进行故障排查、模拟或混音时，您可以快速静音、 Solo 、更改效果器的属性或更改特定总线的音量和音高设置。

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Busses | A list of the Audio Busses within the Busses hierarchy. |
| （电平表） | 每声道峰值电平表。有关扬声器配置和声道的详细信息，请参阅[“了解总线配置”一节](../../05-使用声音和振动来提升游戏体验/02-定义定位/11-了解总线配置.md "了解总线配置")。  信号电平为绿色，表明低于 -6 dB，黄色表明处于 -6 dB 至 0 dB 范围，红色表明高于 0 dB。  电平表数据源既可与当前正在播放的对象同步，也可在加载性能分析会话时与历史数值同步。在电平表显示性能分析会话历史记录时，可使用 Wwise 工具栏上的 **LIVE**（实时）按钮返回当前数值。  |  |  | | --- | --- | | [备注] | 备注 | | 对于 Not Mixing 状态的总线，不会显示电平表。有关各种处理状态的详细信息，请参阅[“了解总线图标和处理状态”一节](../../07-完善工程/01-管理输出/11-完成终混/01-了解总线图标和处理状态.md "了解总线图标和处理状态")章节。 | |
| (Mute and Solo) | 控制对象的 Mute（静音）和 Solo（单独播放）状态，也会显示该对象是否处于被动静音和 Solo 状态。  将对象静音会使其在当前监听中无法听到。让对象 Solo 会使工程中的所有其它对象无声。  粗体的 **M** 或 **S** 表明已为对象主动设置了 Mute 或 Solo 状态。褪色的非粗体 **M** 或 **S** 表明对象的 Mute 或 Solo 状态是由于其它对象状态而被动设置的。  将对象静音会让其子对象被动静音。  让对象 Solo 会使同级对象被动静音，并让子对象和父对象被动 Solo。  |  |  | | --- | --- | | [技巧] | 技巧 | | 在点击 Solo 按钮的同时按住 Ctrl 键，可以强制仅 Solo 该 Solo 按钮所在的对象。 |  |  |  | | --- | --- | | [备注] | 备注 | | Mute 和 Solo 仅用于监视目的，而不会保存在工程中或存储在 SoundBank（声音包）中。 | |
| Bus Volume | 在 Bus 或 Auxiliary Bus 级别的音频信号衰减（电平或振幅）。有关音量的详细信息，请参阅[“了解声部管线”一节](../../07-完善工程/01-管理输出/05-了解声部管线.md "了解声部管线")。  默认值：0  范围：-200 至 200  单位：dB  |  |  | | --- | --- | | [备注] | 备注 | | 默认滑杆范围从 -96 至 +12。您可以通过直接输入值，或在编辑控件上移动鼠标来输入超出限制范围的值。 | |
| Voice Volume（声部音量）。 | 对象输出到总线或发送至辅助总线之前的衰减（电平或振幅）。有关音量的详细信息，请参阅[“了解声部管线”一节](../../07-完善工程/01-管理输出/05-了解声部管线.md "了解声部管线")。  默认值：0 范围：-400 至 400 单位：dB  |  |  | | --- | --- | | [备注] | 备注 | | 默认滑杆范围从 -96 至 +12 dB。您可以通过直接输入值或在编辑控件上移动鼠标来输入超出限制范围的值。 | |
| Voice Pitch | 声部音高。定义音频对象的播放速度。其中：  - 音高 0 = 正常速度。 - 音高 1,200 = 2 倍的速度。 - 音高 2,400 = 4 倍的速度。 - 音高 -1,200 = 0.5 倍的速度。 - 音高 -2,400 = 0.25 倍的速度  |  |  | | --- | --- | | [技巧] | 技巧 | | 1,200 音分相当于一个八度。 |  Default value: 0  Range: -2400 to 2400  Units: Cents |
| Voice Low-pass Filter | 声部低通滤波器。基于指定频率值针对高频进行衰减的递归滤波器。  此滤波器的单位表示低通滤波的百分比，其中 0 表示无低通滤波（信号不受影响）而 100 表示最大衰减。  有关更多详细信息，请参阅 [Wwise 中 LPF 和 HPF 值与截止频率的对应关系](../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/02-定义相对属性（音量、音高、LPF、HPF）/01-Low-pass-和-High-pass-Filter-值与截止频率的关系.md#wwise_lpf_value_cutoff_frequencies "Wwise 中 LPF 和 HPF 值与截止频率的对应关系") 页面。  单位：%  Default value: 0  Range: 0 to 100 |
| Voice High-pass Filter | 声部高通滤波器。基于指定频率针对低频进行衰减的递归滤波器。  此滤波器的单位表示高通滤波的百分比，其中 0 表示无高通滤波（信号不受影响）而 100 表示最大衰减。  有关更多详细信息，请参阅 [Wwise 中 LPF 和 HPF 值与截止频率的对应关系](../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/02-定义相对属性（音量、音高、LPF、HPF）/01-Low-pass-和-High-pass-Filter-值与截止频率的关系.md#wwise_lpf_value_cutoff_frequencies "Wwise 中 LPF 和 HPF 值与截止频率的对应关系") 页面。  单位：%  Default value: 0  Range: 0 to 100 |
| Duck | 闪避。指示正在闪避总线。  如果闪避采取淡入淡出，则在淡入效果开始时 Duck 列中将显示标志，并在淡出效果结束时消失。 |
| BG | 指示总线是否绑定到背景音乐选项，即当用户音乐响动时是否将该总线静音。选择此选项时，如果玩家愿意，当前总线则可替换成玩家自己的音乐。有关详细信息，请参阅[“将音乐替换为玩家自己的音乐”一节](../../03-设置工程/07-建立输出总线的结构/02-定义总线的属性.md#replacing_music_with_player_own_music "将音乐替换为玩家自己的音乐")。  Only one bus in the Busses hierarchy can be used for background music. |
| Bypass | 旁通。指示为相应总线选择了 Bypass All 选项。 |
| Effect | 效果器。作用于总线的效果器类型。  如果应用了多个效果器，则它们将依次列出。  被旁通的效果器呈灰色。 |

**相关主题**

- [*建立输出总线的结构*](../../03-设置工程/07-建立输出总线的结构/00-建立输出总线的结构.md "建立输出总线的结构")
- [“定义总线的属性”一节](../../03-设置工程/07-建立输出总线的结构/02-定义总线的属性.md "定义总线的属性")
- [“完成终混”一节](../../07-完善工程/01-管理输出/11-完成终混/00-完成终混.md "完成终混")

---