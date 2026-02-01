# 调制器 LFO

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [ShareSets 选项卡](../00-ShareSets-选项卡.md) > [Modulator Editor 视图](00-Modulator-Editor-视图.md) > 调制器 LFO

#### 调制器 LFO

下表列出了低频振荡器（LFO）调制器的属性。有关使用 LFO 调制器的详细信息，请参阅[“使用 LFO”一节](../../../../04-与游戏互动/05-使用-RTPC/04-使用-LFO.md "使用 LFO")。

| 界面元素 | 描述 |
| --- | --- |
| Name | 名称。调制器共享集的名称。 |
| Shared by | 共享对象。当前采用所选共享集的对象列表。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
| Notes | 备注。有关已应用的共享集或调制器设置的详细信息。 |

| 界面元素 | 描述 |
| --- | --- |
| Depth | 深度。振荡器的幅度变化。最大幅度为 1.0。  单位：%  Default value: 100  Range: 0 to 100 |
| Frequency | 频率。每秒钟的周期数。  单位：Hz  Default value: 1  Range: 0 to 20000  Units: Frequency |
| Waveform | 调制器的波形包含以下选项：  - **Sine** - **Triangle** - **Square** - **Saw up** - **Saw down** - **Random**:**Random** （随机）：选择 Random 将在调制器每次运行时随机应用电平。  Default value: Sine |
| Smoothing | 平滑。对波形进行低通滤波，从而平滑尖锐的边缘。  此参数可降低输出增益（具体取决于您的配置）。对于 LFO 频率为 1 Hz 的方波，平滑值低到 30% 就能看到增益降低。LFO 频率越高，平滑值要设得越低才能看到增益降低。比如，2 Hz = 25%、4 Hz = 20%、8 Hz = 10%。对于三角波或锯齿波，平滑值低到 10% 就能看到增益降低。  单位：%  Default value: 0  Range: 0 to 100 |
| PWM | 脉冲宽度调制。脉冲波的宽度；仅用于Square（方波）波形。  单位：%  Default value: 50  Range: 0 to 100 |
| Attack | 起音。振荡器达到满幅度所用的时间。  单位：s  Default value: 0  Range: 0 to 100000 |
| Initial Phase Offset | 初相。振荡器波形的初始相位。  单位：°  Default value: 0  Range: -180 to 180 |
| Scope | 作用域。定义如何创建 LFO 实例：  - **Voice**:声部。为每个声音/对象播放创建的 LFO 实例。 - **Note/Event**:音符/事件。为每个播放实例或在 MIDI 环境中使用时的音符创建一个 LFO 实例。 - **Game Object**:游戏对象。为每个游戏对象创建一个 LFO 实例。 - **Global**:全局。为整个工程创建单个 LFO。  Default value: Note or Event |

|  |  |
| --- | --- |
| [备注] | 备注 |
| LFO 和 Envelope 调制器的 RTPC 光标并不能指示其所在时间点的具体值，因为该值是由调制器的内部属性决定的。 |

**相关主题**

- [“Modulator Editor 视图”一节](00-Modulator-Editor-视图.md "Modulator Editor 视图")

---