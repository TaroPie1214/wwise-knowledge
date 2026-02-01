# HDR category: Audio Busses

[Wwise 帮助文档](../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../00-参考主题.md) > [Project Explorer](../../../00-Project-Explorer.md) > [Audio tab](../../00-Audio-tab.md) > [Busses hierarchy](../00-Busses-hierarchy.md) > [Property Editor：Audio Bus](00-Property-Editor：Audio-Bus.md) > HDR category: Audio Busses

##### HDR category: Audio Busses

Using the properties in the HDR category, you can define the HDR behavior for the current bus.

|  |  |
| --- | --- |
| [备注] | 备注 |
| HDR is not available for Main Audio Busses. |

各条 HDR 总线会维护有一个 HDR 窗口，该窗口的位置和宽度分别取决于任意时刻响度最大的声音和工程的音量阈值。有关工程的 Volume Threshold 的详细信息，请参阅 Project Settings 章节。The behavior of the HDR window can be edited in the HDR properties of each HDR bus. 有两组控件；一组控件从电平方面影响窗口的行为（增益计算），另一组控件从时间方面影响窗口的行为（起止响应时间）。

| H DR | |
| --- | --- |
| 界面元素 | 描述 |
| **Specific** | |
| Enable HDR | 启用 HDR。定义总线是否已启用 HDR。  有关详细信息，请参阅 [使用 HDR](../../../../../07-完善工程/01-管理输出/09-使用-HDR/00-使用-HDR.md "使用 HDR") 。  Default value: false |
| **Dynamics** | |
| Threshold | 阈值。定义最小输入电平（单位：dB），超过此电平，HDR 窗口可能会滑动。  有关详细信息，请参阅 [使用 HDR 阈值](../../../../../07-完善工程/01-管理输出/09-使用-HDR/01-设置-HDR-的动态/01-使用-HDR-Threshold.md "使用 HDR Threshold") 。  Default value: 0  Range: -96 to 96 |
| Release Time | 释音时间。定义当目标声音低于当前值时，HDR 窗口复位的速率。  在 Linear Mode（见下文）中，Release TIme 指下降大约 10 分贝所需要的时间（以秒为单位）。  在 Exponential Mode 中，Release TIme 指到达目标值与当前值之差的 0.37 倍（即1/e）处需要的时间（以秒为单位）。  有关详细信息，请参阅 [使用 HDR 起止响应时间](../../../../../07-完善工程/01-管理输出/09-使用-HDR/01-设置-HDR-的动态/02-使用-HDR-起止响应时间.md "使用 HDR 起止响应时间") 。  单位：s  Default value: 0  Range: 0 to 20 |
| HDR Ratio | 比率。此控件的行为类似于音频压缩器中的比率控制。它是衡量 HDR 窗口的定义与峰值之间关系紧密程度的方法。  当 Ratio 的值非常大时，HDR 窗口紧跟峰值，这样一来，输入 HDR 总线的两个声音（一个峰值高出阈值 20 dB，另一个峰值高出阈值 40 dB）只要不是同时播放，输出电平就会同为 0 dBFS。这两个过程的差别在于后一个声音将导致低于阈值的所有声音上产生 -20 dB 的衰减，而前者将导致 -40 dB 的衰减。当比率较低（比如 4）时，峰值为 +20 dB 的声音将产生 +5 dB 的输出，而峰值为 +40 dB 的声音将产生 +10 dB 的输出。对于低于阈值的声音，衰减分别为 -15 dB 和 -30 dB。  因此，使用较低的比率有利于为高于阈值的声音赢回“全局”动态范围，否则这些动态将被 HDR 系统解除。缺点是声音峰值可能会超过阈值，因此您需要在 HDR 总线之后留出足够的裕量空间，以避免出现削波现象。  有关详细信息，请参阅 [使用 HDR 压缩比率](../../../../../07-完善工程/01-管理输出/09-使用-HDR/01-设置-HDR-的动态/03-使用-HDR-Ratio.md "使用 HDR Ratio") 。  Default value: 100  Range: 1 to 100 |
| HDR Release Time Mode | 释音模式。定义窗口释放到下限值时的行为。  - 在 **Linear Mode** 中，窗口顶部在分贝尺度上呈线性移动（即在线性尺度上呈指数变化）。 - 在 **Exponential Mode** 中，它以分贝尺度上呈指数移动。它的速度取决于 Release Time（见上文）。  有关详细信息，请参阅 [使用 HDR 起止响应时间](../../../../../07-完善工程/01-管理输出/09-使用-HDR/01-设置-HDR-的动态/02-使用-HDR-起止响应时间.md "使用 HDR 起止响应时间") 。  Default value: Exponential |
| **Window Top Output Game Parameter** | |
| HDR Window Top Output Game Parameter | HDR 窗口顶部输出游戏参数。定义接收 HDR 窗口位置的 Game Parameter。  有关详细信息，请参阅 [将 HDR 窗口用作输入变量](../../../../../07-完善工程/01-管理输出/09-使用-HDR/06-将-HDR-Window-用作输入变量.md "将 HDR Window 用作输入变量") 。 |
| HDR Output Game Parameter Min | HDR 输出游戏参数最小值。定义 Game Parameter 可设置的最小值。  单位：dB  Default value: 0  Range: -100 to 100 |
| HDR Output Game Parameter Max | HDR 输出游戏参数最大值。定义 Game Parameter 可设置的最大值。  单位：dB  Default value: 100  Range: -100 to 100 |

**相关主题**

- [“理解 HDR”一节](../../../../../07-完善工程/01-管理输出/08-理解-HDR.md "理解 HDR")
- [“Enabling HDR”一节](../../../../../07-完善工程/01-管理输出/09-使用-HDR/00-使用-HDR.md#enabling_hdr_in_project "Enabling HDR")
- [“HDR category”一节](../../../../../08-使用-Wwise/03-了解-Property-Editor/06-HDR-category.md "HDR category")

---