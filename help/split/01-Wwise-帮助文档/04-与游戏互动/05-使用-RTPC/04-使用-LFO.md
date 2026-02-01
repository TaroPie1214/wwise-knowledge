# 使用 LFO

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [与游戏互动](../00-与游戏互动.md) > [使用 RTPC](00-使用-RTPC.md) > 使用 LFO

## 使用 LFO

LFO（低频振荡器）用于为属性值带来随时间变化的调制。LFO 的属性如下：

| 界面元素 | 描述 |
| --- | --- |
| Depth | 深度。振荡器的幅度变化。最大幅度为 1.0。  单位：%  Default value: 100  Range: 0 to 100 |
| Frequency | 频率。每秒钟的周期数。  单位：Hz  Default value: 1  Range: 0 to 20000  Units: Frequency |
| Waveform | 调制器的波形包含以下选项：  - **Sine** - **Triangle** - **Square** - **Saw up** - **Saw down** - **Random**:**Random** （随机）：选择 Random 将在调制器每次运行时随机应用电平。  Default value: Sine |
| Smoothing | 平滑。对波形进行低通滤波，从而平滑尖锐的边缘。  此参数可降低输出增益（具体取决于您的配置）。对于 LFO 频率为 1 Hz 的方波，平滑值低到 30% 就能看到增益降低。LFO 频率越高，平滑值要设得越低才能看到增益降低。比如，2 Hz = 25%、4 Hz = 20%、8 Hz = 10%。对于三角波或锯齿波，平滑值低到 10% 就能看到增益降低。  单位：%  Default value: 0  Range: 0 to 100 |
| PWM | 脉冲宽度调制。脉冲波的宽度；仅用于Square（方波）波形。  单位：%  Default value: 50  Range: 0 to 100 |
| Attack | 起音。振荡器达到满幅度所用的时间。  单位：s  Default value: 0  Range: 0 to 100000 |
| Initial Phase Offset | 初相。振荡器波形的初始相位。  单位：°  Default value: 0  Range: -180 to 180 |
| Scope | 作用域。定义如何创建 LFO 实例：  - **Voice**:声部。为每个声音/对象播放创建的 LFO 实例。 - **Note/Event**:音符/事件。为每个播放实例或在 MIDI 环境中使用时的音符创建一个 LFO 实例。 - **Game Object**:游戏对象。为每个游戏对象创建一个 LFO 实例。 - **Global**:全局。为整个工程创建单个 LFO。  Default value: Note or Event |

在 Wwise 中，有些属性是可加的（例如 Voice Volume、Voice Pitch），有些是不可加的。 当把一个LFO 添加到加性属性上时，LFO 产生的调制将被叠加到该属性的当前值上。在对不可加属性添加 LFO 时，LFO 调制值代替属性的当前值。

**使用 LFO 调制 Voice Volume 的方法是：**

1. 在 Project Explorer 中，选择要添加 LFO 的对象。
2. In the Primary Editor, go to the RTPC tab.
3. 在 RTPC 列表中，点击 [>>] 按钮。
4. 从选择器菜单中，选择 **Voice Volume**。
5. 点击 X 轴选择器按钮。
6. 从选择器菜单中选择 LFO > Default (Custom)。
7. 点击 [...] 按钮以编辑 LFO 属性。
8. 编辑曲线以设置调制范围。

LFO 对象可以被创建成 Custom 或 ShareSet。Custom 对象是原地保存的，即直接保存在拥有该对象的对象内部。ShareSet 被保存在一个单独的工作单元中，并且可以在多个对象之间进行重用。

|  |  |
| --- | --- |
| [注意] | 注意 |
| LFO 和 Envelope（包络）调制器的处理时间取决于其 RTPC 用法。对于大部分属性，将在每个音频控制帧对调制器进行估值。不过，对于 **Voice Volume**（声部音量）属性，将在每个音频采样帧对这些调制器进行估值。请有选择地使用这些调制器，因为它们会占用相当大一部分平台内存和 CPU 资源。 |

|  |  |
| --- | --- |
| [备注] | 备注 |
| LFO 和 Envelope 调制器的 RTPC 光标并不能指示其所在时间点的具体值，因为该值是由调制器的内部属性决定的。 |

---