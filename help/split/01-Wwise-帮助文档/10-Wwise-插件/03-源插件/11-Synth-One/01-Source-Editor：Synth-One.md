# Source Editor：Synth One

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > [Synth One](00-Synth-One.md) > Source Editor：Synth One

### Source Editor：Synth One

Source Editor 显示与 Synth One 插件相关的所有属性。您可以通过修改各种属性值来创建不同的乐音。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 在由 Synth One 创建的纯乐音和其它一次性非循环声音之间过渡时，为了避免出现爆音，请使用 5 ms 的淡入和淡出。 |

| 界面元素 | 描述 |
| --- | --- |
| Name | 用户为该 Synth One 插件所取的名称。 |
| Source Plugin | 源插件。源插件的类型。 |
| Notes | 备注。Synth One 插件的其它相关信息。 |
| **Input（输入）** | |
| Frequency Mode | 频率模式。振荡器的输入频率来源。  **Base Frequency**:用 Base Frequency 属性决定频率。  **MIDI Note**:由接收到的 MIDI 音符事件决定频率。  默认值：Base Frequency  Default value: Base Frequency |
| Base Frequency | 基频。振荡器的输入频率，单位为 Hz；仅当 **Frequency Mode** 设置为 **Base Frequency** 时启用。  默认值：1000 |
| **Oscillators（振荡器）** | |
| Waveform | 振荡器输出的波形类型。  可以使用以下波形：  - Sine - Triangular - Square - Sawtooth  Default value: Sine |
| Transpose | 移调。将输入频率移调，单位为音分。  Default value: 0  Range: -3600 to 3600  Units: Cents |
| Level | 电平。振荡器的输出电平，单位为 dB。该电平值将在合并振荡器之前应用。  Default value: -6.0  Range: -96.0 to 24.0  Units: dB |
| PWM | 脉冲宽度调制，单位为百分比。  请注意，将 PWM 设为 50 将不会进行相关计算，从而提升性能。  Default value: 50  Range: 0.0 to 100.0 |
| Invert | 反转。是否反转振荡器的输出。  Default value: false |
| **Noise（噪声）** | |
| Noise Shape | 噪声形状。所生成的噪声类型。  可用噪声类型：  - White Noise - Pink Noise - Red Noise - Purple Noise  Default value: White Noise |
| Noise Level | 噪声电平。噪声模块的输出电平，单位为 dB。该电平值将应用在噪声模块的输出信号与合并振荡器输出信号进行混合之前。  请注意，将噪声电平设为 -96 将不会进行噪声相关的计算，从而提升性能。  Default value: -96.0  Range: -96.0 to 24.0  Units: dB |
| **Quality** | |
| Over-sampling | 过采样。是否采用过采样来生成振荡器输出。  启用该选项可以提高声音品质，但会降低性能。  Default value: true |
| **Output** | |
| Operation Mode | 模式。如何合并振荡器输出。  提供以下输出模式：  - Mix：各个采样相加 - Ring：各个采样相乘  Default value: Mix |
| FM Amount | 频率调制。该值决定了振荡器 2 的输出信号中，有多少将用于调制振荡器 1 的输出。  请注意，将 FM 设置为 0 将不会进行相关计算，从而提升性能。  Default value: 0  Range: 0 to 100 |
| Output Level | 电平。最终信号的电平，该信号由合并后的振荡器输出信号与噪声发生器的输出信号混合而成。  Default value: 0.0  Range: -96.0 to 24.0  Units: dB |

---