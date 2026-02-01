# 使用 HDR

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理输出](../00-管理输出.md) > 使用 HDR

## 使用 HDR

在 Wwise 中，用户需要选择总线，以将其用作 HDR 电平与满量程（设备）音量之间的转换器。该 HDR 总线使用的输入电平是您在 Wwise 中设置的逻辑电平。因此，连线至 HDR 总线的声音可将其音量设置为远超过 0 dB。而唯一被考虑的因素是其在 HDR 窗口中的位置，该位置由 HDR 总线根据正在播放的内容动态放置。因此，HDR 总线通过提供与音频限幅器/压缩器类似的控制，起到了逻辑限幅器/压缩器的作用。它具有起止响应时间曲线（极小的启动时间、用户定义的释放时间）以控制 HDR 窗口如何及时滑动。它也拥有一个阈值，该阈值可被视为 HDR 窗口可以滑至的最低位置。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 在过去的文献中，HDR 音频系统通常将输入端音量以声压级单位 (dB SPL) 来表达。dB SPL 以分贝为单位，其参考值 (0 dB SPL) 与人类的听觉阈值相对应。Wwise 中没有 SPL 的概念，因为它添加了不必要的复杂性、让界面凌乱，且不会让系统变得更为实用。输入端参考值为任意值，由您来对其进行定义。若要使用 dB SPL，则可将声音结构的音量直接设为正的 dB SPL 值。另一方面，Wwise 中的音量推子的默认范围最高仅为 +12 dB，因此更为实际的做法是选择另一个参考值，然后进行减法运算，为所需的 SPL 值找到对应的分贝值。例如，您可能决定将 100 dB SPL 作为 0 dB 参考值。则 80 dB SPL 声音的音量推子应该被置为 -20 dB，而 130 dB SPL 声音的音量推子应该被置为 +30 dB，以此类推。相应地，您还需要设置 HDR 总线阈值。 |

### Enabling HDR

You can enable HDR on any bus except Auxiliary Busses and Main Audio Busses. If you
enable HDR on a bus, the HDR properties of that bus are also applied to its
children. Any changes you make to the HDR properties of the child bus are not
used.

The volume of all sound structures routed to an HDR bus, or to one of its
children, is affected by the HDR properties of that bus. All other sounds in your
project are not affected by HDR.

**为Audio Bus 启用 HDR 的方法如下:**

1. 打开与 Audio Bus（音频总线）对应的 Property Editor（属性编辑器）。
2. In the Property Editor, click the eye icon and then select **HDR**.

   The HDR category is not available if you have selected an Auxiliary Bus or a Main Audio
   Bus.

   ![](../../../../images/enable_hdr.png)

   The HDR category filter is displayed.

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | If the HDR properties have yellow caution symbols, you are working with a child bus and the child HDR properties will not be used. The child inherits the parent HDR properties. |
3. Select the **HDR** category filter.
4. Select the **HDR** check box to enable HDR.

如上所述，HDR 窗口顶部的声音将以 0 dBFS 输出。使用 HDR 总线的总线音量推子按比例来缩小 HDR 系统的输出后，再将其与工程中的其它非 HDR 声音进行混音。

### 将声音输出到 HDR 总线

To have objects in the Containers hierarchy use the HDR system, you must route the objects to an HDR bus.

**To route an object to an HDR bus:**

1. Inspect the object to show its content.
2. In the Property Editor, go to the Output bus group.
3. 选择 HDR 总线作为 **Output bus**。

### 监控窗口

Voice Monitor 视图显示声部的音量及其包络（如果可见）。

**理解并调试 HDR 系统的方法如下：**

1. 打开 Voice Monitor 视图。
2. 将 HDR 总线拖入视图中。
3. 将 Mode 设置为 Bus input 或 Bus output。Bus input 模式以分贝来显示在进行 HDR 压缩前，HDR 总线输入端的声部电平；而 Bus output 模式则显示在 HDR 压缩和总线输出增益之后， HDR 总线的输出电平。本文档中的大部分图示都是 Voice Monitor 视图的“两端”的屏幕截图。

---