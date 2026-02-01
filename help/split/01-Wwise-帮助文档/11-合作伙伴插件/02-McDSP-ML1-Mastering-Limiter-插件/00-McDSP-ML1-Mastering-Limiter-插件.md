# McDSP ML1 Mastering Limiter 插件

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [合作伙伴插件](../00-合作伙伴插件.md) > McDSP ML1 Mastering Limiter 插件

## McDSP ML1 Mastering Limiter 插件

McDSP ML1 Mastering Limiter（母带限幅器）插件可控制信号峰值，同时提升整体声音电平。You can apply the ML1 effect to the Main Audio Bus to quickly achieve stunning results for any game.

![](../../../images/ml1_front_high_res.png)

|  |  |
| --- | --- |
| [备注] | 备注 |
| Audiokinetic 的 McDSP ML1 Mastering Limiter 版本中使用的算法与 ProTools 略有不同。这些变化旨在满足以下特定条件：在处理过载的输入信号（最多 +12 dB）时，让输出中产生大量的削波失真。 |

Ceiling（上限）控件可设置最大输出电平。Threshold 控件确定限幅器开始检测信号峰值的电平。Ceiling 和 Threshold 间的电平差是作用于输入音频的最大增益量。强信号峰值通常将受到限制，而低信号电平会被抬升。两类信号都不会超出 Ceiling 控件电平。

Knee（拐点）控件可调整输入信号电平增强和输入信号限幅之间的过渡。在常规的限幅器中，信号电平将持续增加，直到达到输出上限。这使得音频变得更响亮，但是可能会产生大量的失真。在输出上限之前设置软拐点可减少失真量并使限幅器更加透明。

Release（释音）控件决定限幅器从信号峰值削减恢复的速度。释音越快，限幅器输出电平越强。ML1 限幅器的另一个独特控件 —— Mode（模式）控件 —— 可设置限幅器处理峰值和整个信号功率的方式。Release 时长和 Mode 设置的不同组合能让 ML1 具有多种风格。从富有冲击力的鼓噪声到微妙的人声限幅，ML1 Mastering Limiter 全都可以做到。

McDSP ML1 插件包含一系列属性，其中很多属性可实时编辑，并可使用 RTPC 映射至特定游戏参数。 属性值旁边有一个特殊标志，显示它是否使用 RTPC。

下表介绍了两种 RTPC 标志：

| 标志 | Name | 描述 |
| --- | --- | --- |
| |  | | --- | |  | | RTPC - 开启 | 属性值已使用 RTPC 绑定到游戏中的参数值。 |
| |  | | --- | |  | | RTPC - 关闭 | 属性值未与游戏中的参数值绑定。 |

另外还准备了大量[“预设”一节](../../09-参考主题/04-Project-Explorer/11-预设/00-预设.md "预设") ，让您能快速上手。您可以原封不动地使用这些预设，也可以从它们出发来做出原创性的效果。

|  |  |
| --- | --- |
| [备注] | 备注 |
| The McDSP effects are available in all versions of Wwise. However, they require a separate license. See the [Wwise McDSP Plug-in](https://www.audiokinetic.com/wwise/plugins/mcdsp) product page. |

---