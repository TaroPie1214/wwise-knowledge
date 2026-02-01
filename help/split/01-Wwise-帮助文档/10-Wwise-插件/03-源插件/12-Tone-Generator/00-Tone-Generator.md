# Tone Generator

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > Tone Generator

## Tone Generator

Tone Generator 是一个源插件，您可以通过它为游戏生成多种声音和振动效果器。Wwise Tone Generator 可以用以下类型的波形创建乐音和振动效果器：

- Sine（正弦波）
- Triangular（三角波）
- Square（方波）
- Sawtooth（锯齿波）
- White Noise（白噪声）
- Pink Noise（粉红噪声）

|  |  |
| --- | --- |
| [备注] | 备注 |
| 与很多声音编辑软件不同，Wwise 中的振荡器具有频带限制。这不仅有助于避免超出奈奎斯特频率的谐波导致的不和谐噪音，还可以节省 CPU 和内存占用。对于基频极高的乐音，与没有频带限制的情况相比，只存在较少谐波。 |

您可能注意到了 Source Plug-in Editor 和 Contents Editor 中的一些属性值旁边带有标志。该标志表明属性值是否通过 RTPC 与 Game Parameter 关联。

以下表格介绍了两种 RTPC 标志：

| 标志 | 名称 | 描述 |
| --- | --- | --- |
| |  | | --- | |  | | RTPC - 开启 | 属性值已使用 RTPC 绑定到游戏中的参数值。 |
| |  | | --- | |  | | RTPC - 关闭 | 属性值未与游戏中的参数值绑定。 |

**编辑器**

- [“Source Editor：Tone Generator”一节](01-Source-Editor：Tone-Generator.md "Source Editor：Tone Generator")
- [“Contents Editor：Tone Generator”一节](02-Contents-Editor：Tone-Generator.md "Contents Editor：Tone Generator")

---