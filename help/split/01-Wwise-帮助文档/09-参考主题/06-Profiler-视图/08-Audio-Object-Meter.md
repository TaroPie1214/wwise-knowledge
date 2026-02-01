# Audio Object Meter

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [参考主题](../00-参考主题.md) > [Profiler 视图](00-Profiler-视图.md) > Audio Object Meter

## Audio Object Meter

Audio Object Meter（音频对象电平表）以扩展视图的形式提供了当前所选 Audio Object 的测量数据。要想在此视图中显示内容，必须在 [“Audio Object List”一节](06-Audio-Object-List.md "Audio Object List") 中选择 Audio Object。此视图中显示的信息基于当前性能分析器光标时间。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若要在此视图中显示信息，则须在 [“Profiler Settings”一节](../01-工程/10-Profiler-Settings.md "Profiler Settings") 中启用 **Audio Object Data** 以捕获数据，同时在捕获会话中选择时间点。 |

| 界面元素 | 描述 |
| --- | --- |
|  | Click the View Settings icon in the upper right corner of the view to open the [“Profiler Settings”一节](../01-工程/10-Profiler-Settings.md "Profiler Settings") dialog, where you can specify the type of data to capture. |
| The metered object | 被测量对象。显示被测量 Audio Object 的名称。 |
| Peak/RMS | 峰值/均方根。定义采用哪种模式来显示电平表。  - **Peak**：标准显示模式。显示各个声道。这些值代表绘制区域的峰值 PCM 值，单位：分贝。 - **RMS**：显示 RMS（均方根）值。折叠所有声道。这些值代表绘制区域的峰值 RMS 值。 |
| Meter | 电平表。用于显示 Audio Object 电平的标准电平表。 |

**相关主题**

- [“了解基于对象的音频”一节](../../03-设置工程/07-建立输出总线的结构/03-了解基于对象的音频/00-了解基于对象的音频.md "了解基于对象的音频")
- [“对 Audio Object 实施性能分析”一节](../../07-完善工程/06-性能分析/12-对-Audio-Object-实施性能分析.md "对 Audio Object 实施性能分析")

---