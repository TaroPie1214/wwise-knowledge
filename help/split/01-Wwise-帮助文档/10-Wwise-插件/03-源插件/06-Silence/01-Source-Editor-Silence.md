# Source Editor: Silence

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > [Silence](00-Silence.md) > Source Editor: Silence

### Source Editor: Silence

Source Editor 中显示与 Silence 插件相关的所有属性。您可以通过修改属性值来添加不同长度的空白信号源。

| 界面元素 | 描述 |
| --- | --- |
| Name | 名称。用户对此 Silence 插件的命名。 |
| Source Plug-in（源插件） | 源插件。源插件的类型。 |
| Notes | 备注。Silence 插件的其它信息。 |
| **Length（长度）** | |
| Duration | 空白信号的时长。  单位：s  Default value: 1.0  Range: 0.001 to 3600 |
| Random Min | 随机化最小值。对 Duration 值进行偏置，定义空白信号源的最小可能长度。  由于您无法对空白信号源插件应用 Randomizer，因此 Rand Min 和 Rand Max 属性可以用来指定随机化的最小和最大偏置值。  单位：s  Default value: 0.0  Range: -3600 to 0 |
| Random Max | An offset from the Duration value that defines the maximum possible length of the silence.  由于您无法对空白信号源插件应用 Randomizer，因此 Rand Min 和 Rand Max 属性可以用来指定随机化的最小和最大偏置值。  单位：s  Default value: 0.0  Range: 0 to 3600 |

---