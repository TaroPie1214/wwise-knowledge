# 使用 Performance Monitor 进行监控和故障排查

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [完善工程](../00-完善工程.md) > [性能分析](00-性能分析.md) > 使用 Performance Monitor 进行监控和故障排查

## 使用 Performance Monitor 进行监控和故障排查

Wwise 设计工具与音频引擎紧密集成，因此游戏过程中，您可以实时监控大量的关键表现指标。Game Profiler（游戏性能分析器）还可与 SoundCaster、Game Simulator 和其他 WAAPI 应用结合使用，以便在将设计或原型整合到游戏中之前对其性能进行监控。

Wwise 捕获声音引擎活动的相关信息时，Performance Monitor（性能监控器）中会实时显示性能图表，对应的实际数量和百分比也会显示在右侧的 Performance Data（性能数据）列表中。

这些曲线可以让您快速找到游戏中音频性能超过限制的地方，例如平台限制。组合使用 Performance Monitor、Advanced Profiler 和 Capture Log，可以帮您诊断和解决潜在的问题。

Performance Monitor 允许自定义，即可以设置其中显示哪些性能指标和数值。有关自定义 Performance Monitor 的详细信息，请参阅[“自定义 Performance Monitor”一节](09-使用-Performance-Monitor-进行监控和故障排查.md#customizing_performance_monitor "自定义 Performance Monitor")。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 您可以在捕获数据时监控性能，或者启动 Capture Session，在图表中移动光标来调查问题。若想在捕获数据的同时监控性能，须单击 Show Live Data 按钮 ，来让 Capture Log 和 Performance Monitor 与捕获时间保持同步。 |

**监控性能的方法如下：**

1. 连接到远程设备。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 如果正在使用 Soundcaster 对模块或原型进行性能分析，将在您播放不同模块时捕获信息。 |
2. 执行以下操作之一：

   - 在菜单栏中点击 **Layouts** > **Profiler**（布局 > 性能分析）。
   - 按 **F6** 键。

   Profiler 布局将显示 。
3. 点击工具栏中的 **Start Capture** ![](../../../../images/btn_start_capture.png)（开始捕获）按钮。

   Wwise 将显示声音引擎捕获信息相关的平台性能曲线。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 实心方块表明此处捕获的信息已超过限制，曲线顶部的长方块表明当前值高出最大允许值，底部的方块表明当前值低于最小允许值。 |
4. 将 Performance Monitor（性能监控器）的时间光标拖到坐标图上提示性能问题的位置。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 在曲线视图中移动光标时，Capture Log 的位置以及 Performance Data 面板和 Advanced Profiler 中显示的数据会自动更新。 |
5. 通过 Advanced Profiler 中的时间光标（白色圆圈）找出导致问题的事件、动作或其它声音引擎活动，或按住 Shift 并点击 Capture Log 中的条目，来将所有性能分析视图与此时间戳同步。
6. 要编辑对象和事件的内容或属性，请双击 Capture Log 中的条目。相应事件或对象将在 Event Editor（事件编辑器）或 Property Editor（属性编辑器）中打开，在其中进行所需修改即可。
7. 查看 Advanced Profiler 各选项卡，可以获取该引擎活动条目的详细性能信息。
8. 要将 Performance Monitor 中的曲线数值保存为文本文件，请右键点击曲线并选择 **Save All Counters to File**（将所有数值保存到文件）。数值将保存为制表符分割的文本文件，其中包含从捕获开始直至当前的所有数值，记录间隔为 200 ms。

### 自定义 Performance Monitor

有些时候，您可能需要同时监控多个关键指标，而另一些时候则可能只想关注一个特定方面。为了满足不同监控会话的需求，可以增加和删除 Performance Monitor 中的数值显示。

**修改 Performance Monitor 显示内容的方法如下：**

1. 在 Performance Monitor 标题栏中，点击 View Settings 图标。

   这时会打开 Performance Monitor Settings（性能监控器设置）对话框。
2. 在 Show In Graph（显示曲线）列中，选择希望显示在 Performance Monitor 坐标图中的数值。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 若要查看各项数值的说明，请单击 Performance Monitor Settings 对话框中的 Help 图标。 |
3. 在 Show In List（在列表中显示）列中，选择希望显示在 Performance Data 列表中的数值。
4. 为您选择的数值设置最小和最大值，即数值所对应曲线图的纵坐标范围。
5. 单击 **OK**（确定）。

   Performance Monitor 将会更新，仅显示您选择的数值。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 如果您选择了 Profiler Settings 中禁用的数据类型，则 Performance Monitor 将不会显示该类型的图表。有关更改 Profiler 设置的详细信息，请参阅[“指定要捕获的信息类型”一节](07-从声音引擎捕获数据/01-指定要捕获的信息类型.md "指定要捕获的信息类型")。 |

---