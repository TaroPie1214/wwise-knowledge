# Source Editor：Tone Generator

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > [Tone Generator](00-Tone-Generator.md) > Source Editor：Tone Generator

### Source Editor：Tone Generator

Source Editor 显示与 Tone Generator 插件相关的所有属性。您可以通过修改各种属性值来创建不同的乐音和振动效果。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 在由 Tone Generator 创建的纯乐音和其它一次性非循环声音之间进行过渡时，为了避免出现爆音，请使用 5 ms 的淡入和淡出。 |

| 界面元素 | 描述 |
| --- | --- |
| Name | 用户为此 Tone Generator 插件所取的名称。 |
| Source Plug-in（源插件） | 源插件。源插件的类型。 |
| Notes | 备注。有关 Tone Generator 插件的其它信息。 |
| **Frequency** | |
| Frequency | 乐音的频率。如果使用了扫频，则该值将作为乐音的起始频率。  Default value: 1000.0  Range: 20 to 20000  Units: Frequency |
| Rand.（随机化）Min | 随机最小值。Frequency 值的偏置，定义乐音的最小可能频率。  由于无法对插件的频率应用 Modifier，因此在为 Tone Generator 插件指定最小和最大偏置值时， Rand Min 和 Rand Max 属性将起到随机化器的作用。 |
| Rand.（随机化）Max | 随机最大值。Frequency 值的偏置，定义乐音的最大可能频率。 |
| Sweep Frequency | 扫频频率。启用时，您可以更改乐音从开始到结束的频率。  Default value: false |
| Stop Frequency | 结束频率。乐音将在此频率处停止。  单位：Hz  Default value: 1000.0  Range: 20 to 20000  Units: Frequency |
| Stop Frequency Random Min | 随机最小值。Frequency 值的偏置，定义乐音的最小可能 Stop Frequency 值。  Default value: 0.0  Range: -12000 to 0 |
| Stop Frequency Random Max | 随机最大值。Stop Frequency 值的偏置，定义乐音的最大可能 Stop Frequency 值。  Default value: 0.0  Range: 0 to 12000 |
| **Interpolation（插值）** | |
| Linear | 线性。从起始频率到结束频率进行线性变化。 |
| Logarithmic | 对数。从起始频率到结束频率的进行呈对数变化。 |
| **Waveform** | |
| Type | 类型。用于创建乐音的波形或噪声类型。  可以使用以下波形：  - Sine - Triangular - Square - Sawtooth - White Noise - Pink Noise  Default value: Sine |
| Gain | 增益。乐音输出的电平或振幅。  单位：dB  Default value: -12.0  Range: -96.3 to 0  Units: dB |
| |  | | --- | |  |  (Link/Unlink) | 显示是否在所有平台上应用 Channel 选择。 |
| Channel | 用于指定乐音的输出声道，包含两个选项：Mono 和 LFE。  Default value: Mono |
| **Duration** | |
| Duration | - **Fixed duration**:乐音时长，期间振幅将一直保持恒定。 - **Envelope**:包络。启用 ADSR 振幅包络控制。如果所有 ADSR 控制均设为 0，则不会播放任何声音。  Default value: Fixed Duration |
| Attack | 起音时长。声音达到最大振幅时所花费的时间。  单位：s  Default value: 0.0  Range: 0 to 3600 |
| Decay | 衰减时长。声音的振幅降至 Sustain level（延音电平）所花费的时间。  单位：s  Default value: 0.0  Range: 0 to 3600 |
| Sustain | 延音时长。乐音保持在 Sustain level 的时间。  单位：s  Default value: 1.0  Range: 0 to 3600 |
| Sustain level | 延音电平。声音振幅保持恒定时的电平。  单位：dB  Default value: -12.0  Range: -96.3 to 0  Units: dB |
| Release | 释音时长。声音的振幅从 Sustain level 降至静音所花费的时间。  单位：s  Default value: 0.0  Range: 0 to 3600 |

---