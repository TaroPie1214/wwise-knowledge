# Audio Device Meter

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [参考主题](../00-参考主题.md) > [视图](00-视图.md) > Audio Device Meter

## Audio Device Meter

Audio Device Meter（音频设备电平表）视图会显示 Audio Device 的三种输出流的电平：

- Main mix
- Passthrough
- Objects

Main mix 和 Passthrough 电平表会显示各个声道的值，Objects 电平表会显示各个 System Audio Object 的值。如需了解音频如何被分为这三个输出流，请参阅 [“System Audio Device 的作用”一节](../../03-设置工程/07-建立输出总线的结构/03-了解基于对象的音频/02-System-Audio-Device-的作用.md "System Audio Device 的作用")。

电平表的颜色为：

- 绿色，低于 -6 dB
- 黄色，从 -6 dB 至 0 dB
- 红色，高于 0 dB

电平表数据源既可与当前正在播放的对象同步，也可在加载性能分析会话时与历史数值同步。在电平表显示性能分析会话历史记录时，可使用 Wwise 工具栏上的 **LIVE**（实时）按钮返回当前数值。

有关详细信息，请参阅[“监控信号电平”一节](../../07-完善工程/01-管理输出/11-完成终混/02-监控信号电平.md "监控信号电平")。

有关 Audio Device Meter Instance（A、B、C 或 D）的详细信息，请参阅[“了解 Selection Channel 和 Meter Instance”一节](../../02-入门/04-个性化您的工作空间/01-处理视图/01-了解-Selection-Channel-和-Meter-Instance.md "了解 Selection Channel 和 Meter Instance")

Audio Device Meter 视图会显示以下元素：

| 界面元素 | 描述 |
| --- | --- |
| [name] | 名称。Audio Device 的名称。 |
|  | 打开 Project Explorer - Browser（工程资源管理器 - 浏览器）。可在其中指定要测量哪个 Audio Device 的电平。“浏览”按钮仅在视图浮动时可用。 |
| Main mix | 主混音。显示 Main Mix（主混音）的各个声道的电平。 |
| Passthrough | 直通。显示 Passthrough Mix（直通混音）的两个声道的电平。 |
| Objects | 对象。显示各个 System Audio Object（系统音频对象）的电平。 |

---