# Audio Bus tab and Auxiliary Bus tab: busses

[Wwise 帮助文档](../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../00-参考主题.md) > [Project Explorer](../../../00-Project-Explorer.md) > [Audio tab](../../00-Audio-tab.md) > [Busses hierarchy](../00-Busses-hierarchy.md) > [Common tabs and categories: Busses hierarchy objects](00-Common-tabs-and-categories-Busses-hierarchy-object.md) > Audio Bus tab and Auxiliary Bus tab: busses

##### Audio Bus tab and Auxiliary Bus tab: busses

In the Audio Bus or Auxiliary Bus tab, there is a bus meter (if processing), bus status
information, and the HDR Window (if HDR is enabled for the bus).

| 总线专用 | |
| --- | --- |
| 界面元素 | 描述 |
| （电平表） | 每声道峰值电平表。有关扬声器配置和声道的详细信息，请参阅[“了解总线配置”一节](../../../../../05-使用声音和振动来提升游戏体验/02-定义定位/11-了解总线配置.md "了解总线配置")。  信号电平为绿色，表明低于 -6 dB，黄色表明处于 -6 dB 至 0 dB 范围，红色表明高于 0 dB。  电平表数据源既可与当前正在播放的对象同步，也可在加载性能分析会话时与历史数值同步。在电平表显示性能分析会话历史记录时，可使用 Wwise 工具栏上的 **LIVE**（实时）按钮返回当前数值。  |  |  | | --- | --- | | [备注] | 备注 | | 对于 Not Mixing 状态的总线，不会显示电平表。有关各种处理状态的详细信息，请参阅[“了解总线图标和处理状态”一节](../../../../../07-完善工程/01-管理输出/11-完成终混/01-了解总线图标和处理状态.md "了解总线图标和处理状态")章节。 | |

| Bus Status (Authoring) | |
| --- | --- |
| 界面元素 | 描述 |
| Processing | 处理。根据 Wwise 中对工程的设定来显示总线的处理状态；运行时的处理状态可能会有所不同。有关如何确定处理状态的详细信息，请参阅[“了解总线图标和处理状态”一节](../../../../../07-完善工程/01-管理输出/11-完成终混/01-了解总线图标和处理状态.md "了解总线图标和处理状态")章节。 |
| Bus Config. | 总线配置。根据 Wwise 中对工程的设定来显示 Pre-Effects stage（效果器前处理阶段）的总线配置；运行时的总线配置可能会有所不同。  The displayed value is read-only. You can change it with the Configuration property in the Property Editor for the selected Audio Bus or Auxiliary Bus. See [“Property Editor：Audio Bus”一节](../02-Property-Editor：Audio-Bus/00-Property-Editor：Audio-Bus.md "Property Editor：Audio Bus") or [“Property Editor: Auxiliary Busses”一节](../03-Property-Editor-Auxiliary-Busses.md "Property Editor: Auxiliary Busses").  在对总线实施混音时，会在执行混音后进入 Pre-Effects stage，但此时并不会对效果器进行处理。比如，在将总线的总线配置设为 2.0 时，会先将所有输入混音为立体声配置，然后才会将效果器添加到立体声信号中。也就是说，Bus Config. 字段显示的是两个阶段之间的总线配置。 |
| Out Config. | 输出配置。显示 Post-Effects stage（效果器后处理阶段）的总线配置。在此之前已实施混音并对效果器进行了处理。其依据为 Wwise 中对工程的设定；运行时的总线配置可能会有所不同。  因为效果器有可能会改变总线配置，所以 Out Config. 跟 Bus Config. 未必相同。比如，对于应用有 Reflect 插件的总线。其 Bus Config. 可能为 1.0，而 Out Config. 却为 Audio Objects（音频对象）。  若总线上未插入效果器，则 Bus Config. 和 Out Config. 完全相同。若总线上插入了效果器，则 Out Config. 默认显示 Unknown（未知），除非正在对来自声音引擎的捕获数据实施分析。在这种情况下，将显示实际的 Out Config.。 |

| HDR | |
| --- | --- |
| 界面元素 | 描述 |
| HDR Window | 显示 -96 db 到 96 db 的完整窗口范围，其中适用的 HDR 阈值范围将显示为浅蓝色矩形。Only visible when the bus is HDR enabled. 请参阅 [“Enabling HDR”一节](../../../../../07-完善工程/01-管理输出/09-使用-HDR/00-使用-HDR.md#enabling_hdr_in_project "Enabling HDR")。 |

---