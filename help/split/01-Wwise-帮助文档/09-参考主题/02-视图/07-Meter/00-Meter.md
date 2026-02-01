# Meter

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [视图](../00-视图.md) > Meter

## Meter

Meter（电平表）视图可显示三种不同的电平：

- Peak
- True Peak（真峰值，如 ITU-R BS.1770-4 所定义）
- RMS（均方根）

每种电平显示各个声道的值。有关扬声器配置和声道的详细信息，请参阅[“了解总线配置”一节](../../../05-使用声音和振动来提升游戏体验/02-定义定位/11-了解总线配置.md "了解总线配置")。

电平表的颜色分为：

- 绿色，低于 -6 dB
- 黄色，从 -6 dB 至 0 dB
- 红色，高于 0 dB

电平表数据源既可与当前正在播放的对象同步，也可在加载性能分析会话时与历史数值同步。在电平表显示性能分析会话历史记录时，可使用 Wwise 工具栏上的 **LIVE**（实时）按钮返回当前数值。

有关详细信息，请参阅[“监控信号电平”一节](../../../07-完善工程/01-管理输出/11-完成终混/02-监控信号电平.md "监控信号电平")。

有关 Meter Instance（A、B、C 或 D）的详细信息，请参阅[“了解 Selection Channel 和 Meter Instance”一节](../../../02-入门/04-个性化您的工作空间/01-处理视图/01-了解-Selection-Channel-和-Meter-Instance.md "了解 Selection Channel 和 Meter Instance")

Meter 会显示以下元素：

| 界面元素 | 描述 |
| --- | --- |
| Peak | 峰值 。峰值电平表测量 PCM（脉冲编码调制）信号在极短时间内的最大值或最小值。（单位：dBFS） |
| True Peak | 真峰值。真峰值是在模拟域中对数字信号的最大峰值的估计值。此值对于确保数模转换器没有饱和非常有用。（单位：dBTP）  按 ITU-R BS.1770-4 规范实现真峰值。 |
| Root mean square (RMS) | 均方根。RMS 电平以峰值表值测量，并取极短时间段内的平均值。 |
| 3D Meter | 在 3D Meter 模式下，会以三维球体来表示 Ambisonics 信号的方向性。它会计算球体上每一虚拟扬声器位置的峰值电平。最后，依据球体上的各个采样位置生成热图。最后，依据球体上的各个采样位置生成热图。A heatmap representation is then generated from each of the positions on the sphere. 3D Meter 模式目前仅适用于采用 Ambisonics 总线配置的总线。  有关 3D Meter 模式的详细信息，请参阅 [“3D Meter”一节](01-3D-Meter.md "3D Meter")。 |

---