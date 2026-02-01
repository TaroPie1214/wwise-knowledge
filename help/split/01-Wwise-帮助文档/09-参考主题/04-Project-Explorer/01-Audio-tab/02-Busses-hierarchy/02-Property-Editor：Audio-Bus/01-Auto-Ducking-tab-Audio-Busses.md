# Auto-Ducking tab: Audio Busses

[Wwise 帮助文档](../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../00-参考主题.md) > [Project Explorer](../../../00-Project-Explorer.md) > [Audio tab](../../00-Audio-tab.md) > [Busses hierarchy](../00-Busses-hierarchy.md) > [Property Editor：Audio Bus](00-Property-Editor：Audio-Bus.md) > Auto-Ducking tab: Audio Busses

##### Auto-Ducking tab: Audio Busses

Use the Auto-Ducking tab to configure ducking. 在该选项卡中命名当前正在编辑属性的相应总线。该总线为当前总线，其会压低其他总线的音量。若要选择要闪避的总线，请单击 **Insert**（插入）。

| General | |
| --- | --- |
| 界面元素 | 描述 |
| [name] | 对象的名称。 |
| (Object Color) | 显示对象的颜色。单击图标可打开颜色选择器。    选择一种颜色并将其应用于对象。在为对象选择某种颜色时，会在选定方块上显示调色板图标，并在右下角标注黄色三角（如图所示）。  若要沿用父对象的颜色，请选中颜色选择器最左侧的方块。 |
| (Mute and Solo) | 控制对象的 Mute（静音）和 Solo（单独播放）状态，也会显示该对象是否处于被动静音和 Solo 状态。  将对象静音会使其在当前监听中无法听到。让对象 Solo 会使工程中的所有其它对象无声。  粗体的 **M** 或 **S** 表明已为对象主动设置了 Mute 或 Solo 状态。褪色的非粗体 **M** 或 **S** 表明对象的 Mute 或 Solo 状态是由于其它对象状态而被动设置的。  将对象静音会让其子对象被动静音。  让对象 Solo 会使同级对象被动静音，并让子对象和父对象被动 Solo。  |  |  | | --- | --- | | [技巧] | 技巧 | | 在点击 Solo 按钮的同时按住 Ctrl 键，可以强制仅 Solo 该 Solo 按钮所在的对象。 |  |  |  | | --- | --- | | [备注] | 备注 | | Mute 和 Solo 仅用于监视目的，而不会保存在工程中或存储在 SoundBank（声音包）中。 | |
| (Show references) | 指示工程中有多少元素包含对对象的直接引用。若存在对对象的引用，则图标显示为橙色；若不存在此类引用，则图标显示为灰色。  通过单击该按钮，可打开 [“Reference View 视图”一节](../../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")，并在 **References to:**（引用:）字段中查看对象的名称。 |

| Auto-Ducking | |
| --- | --- |
| 界面元素 | 描述 |
| Recovery Time | 恢复时间。从当前总线内的音频信号终止到闪避信号的淡入效果开始所需要的时间。  单位：s  Default value: 1  Range: 0 to 10 |
| Maximum ducking volume | 最大闪避音量。决定当前总线最多可将所列总线的音量降低多少。使用滑杆在 0 ~ -96 之间选择数值。若要在 -97 ~ -200 之间选择数值，请使用键盘或鼠标滚轮。  Default value: -96  Range: -200 to 0  Units: dB |
|  | 打开 Project Explorer —— Browser，您可以在此选择要添加到自动闪避列表中的音频总线。  The **Main Audio Bus** cannot be selected, and an Audio Bus cannot duck itself or any of its parent busses. |
|  | 移除。从要被当前总线闪避的总线列表中删除选定总线。 |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Busses | 总线。 Audio Bus 的名称。 |
| Volume | 音量。指定在闪避过程中要将总线的音量降低多少 dB。滑杆范围为 -96 ~ 0，默认设为 -6。若要设为 -96 以下的值，请使用键盘。 |
| Fade Out | 淡出。从原始音量淡出至闪避音量所需要的时间。 |
| Fade In | 淡入。从闪避音量淡入至原始音量所需要的时间。 |
| Curve | 曲线。用于定义信号淡出并重新淡入的曲线形状。 |
| Target | 目标。定义闪避系统的目标属性。  以下是两个可能值：  - **Bus Volume**（总线音量）：直接以最终总线音量为目标。 - **Voice Volume**（声部音量）：以总线中正在播放的音频对象为目标。该项会同时影响作用于目标音频对象的发送。 |

**相关主题**

- [“闪避信号”一节](../../../../../03-设置工程/07-建立输出总线的结构/02-定义总线的属性.md#ducking_signals "闪避信号")

---