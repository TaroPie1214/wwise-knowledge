# Contents Editor：Synth One

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > [Synth One](00-Synth-One.md) > Contents Editor：Synth One

### Contents Editor：Synth One

您可以通过 Contents Editor 快速访问与 Synth One 插件相关的一些常用属性。必须点击 Synth One 源才能显示相关列标题。

| 界面元素 | 描述 |
| --- | --- |
| Name | Synth One 插件的名称。 |
| Use | 采用。决定声音对象内的哪个源将会被：  - 将被播放。 - 将被包括在 SoundBank 中。 - 此选项仅在声音对象内具有多个源时才可见。 |
| Frequency Mode | 频率模式。振荡器的输入频率来源。  **Base Frequency**:用 Base Frequency 属性决定频率。  **MIDI Note**:由接收到的 MIDI 音符事件决定频率。  默认值：Base Frequency  Default value: Base Frequency |
| Base Frequency | 基频。振荡器的输入频率，单位为 Hz；仅当 **Frequency Mode** 设置为 **Base Frequency** 时启用。  默认值：1000 |
| Output Level | 电平。最终信号的电平，该信号由合并后的振荡器输出信号与噪声发生器的输出信号混合而成。  Default value: 0.0  Range: -96.0 to 24.0  Units: dB |
| Notes | 备注。Synth One 插件的其它相关信息。 |
|  | 向声音对象中添加新的源。  当您点击 **Add Source**（添加源）按钮时，会显示一个可以添加的[*源插件*](../00-源插件.md "源插件")列表。 |

---