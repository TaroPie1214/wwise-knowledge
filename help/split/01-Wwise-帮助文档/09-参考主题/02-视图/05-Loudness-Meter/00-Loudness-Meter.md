# Loudness Meter

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [视图](../00-视图.md) > Loudness Meter

## Loudness Meter

Loudness Meter 提供了测量音频信号的响度级别和响度范围的标准方法。它基于以下标准：

- **EBU R128**
- **ITU-R BS.1770-4**

有关响度的详细信息，请参阅[“监控信号电平”一节](../../../07-完善工程/01-管理输出/11-完成终混/02-监控信号电平.md "监控信号电平")。

Loudness Meter 会显示以下元素：

| 界面元素 | 描述 |
| --- | --- |
| Momentary | 瞬时。使用长度为 0.4 秒的滑动矩形时间窗计算响度电平。测量不使用门限（not gated）。  依据工具栏上的 Show Live Data（显示实时数据）状态，瞬时值既可为当前测量的值，也可为时间光标所在位置的值。 |
| Short-term | 短时。使用长度为 3 秒的滑动矩形时间窗计算响度电平。测量不使用门限（not gated）。  依据工具栏上的 Show Live Data（显示实时数据）状态，短时值既可为当前测量的值，也可为时间光标所在位置的值。 |
| Momentary and short-term graph | 瞬时和短时坐标图。瞬时值和短时值的坐标图。只有在打开性能分析器捕获会话时才会激活该坐标图。您可以使用 Wwise 工具栏上的 Start Capture（开始捕获）按钮来开始收集瞬时值和短时值。  在显示捕获会话时，可单击坐标图来检视之前的瞬时值和短时值。在调节时间光标时，其他性能分析视图也会受到影响。 |
| Measure | 测量。开始或停止测量积分响度。若激活，则测量**积分响度**和**响度范围**。Measure 状态不会对瞬时响度或短时响度产生影响。 |
| Reset | 重置。重置当前测量。此操作相当于单击 **Measure** 两次来先开始再停止测量。在重置测量时会重置积分响度和响度范围。 |
| Integrated | 积分。测量期间计算得出的响度级。积分响度使用门限（忽略所有 -70 LUFS 以下的值），并依据瞬时响度进行长期测量（在整个测量期间持续积分）。单击 Measure（测量）按钮时开始测量，再次单击该按钮即停止测量。若要重新开始测量，请单击 Reset（重置）按钮。 |
| Loudness Range (LRA) | 响度范围 LRA。响度范围是统计计算得出的声音内容的动态范围，该范围对应于使用门限（所有低于 -70 LUFS 的值都会被忽略）的积分响度测量结果。响度范围从宏观尺度上测量响度变化，单位为 LU（响度单位）。  单击 **Measure**（测量）按钮时开始测量，再次单击该按钮即停止测量。若要重新开始测量，请单击 **Reset**（重置）按钮。 |

### 响度表监视

您可以直接在 Loudness Meter 或 Performance Monitor（性能监控器）中适时捕获以下响度级：

- Momentary Loudness Level - Instance A
- Momentary Loudness Level - Instance B
- Momentary Loudness Level - Instance C
- Momentary Loudness Level - Instance D
- Short-Term Loudness Level - Instance A
- Short-Term Loudness Level - Instance B
- Short-Term Loudness Level - Instance C
- Short-Term Loudness Level - Instance D

有关详细信息，请参阅[“在 Wwise 中测量响度”一节](../../../07-完善工程/01-管理输出/11-完成终混/02-监控信号电平.md#measuring_loudness_in_wwise "在 Wwise 中测量响度")。

---