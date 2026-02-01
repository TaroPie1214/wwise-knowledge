# Source Editor：Sine

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > [Sine（正弦波）](00-Sine（正弦波）.md) > Source Editor：Sine

### Source Editor：Sine

Source Editor 中将显示与 Sine 插件相关的所有属性。您可以修改各属性值，来创建不同的乐音和音效。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 在由 Sine 创建的乐音和其它一次性非循环声音之间过渡时，为避免出现爆音，请使用 5 ms 的淡入和淡出效果。 |

| 界面元素 | 描述 |
| --- | --- |
| Name | 名称。用户对此 Sine 插件的命名。 |
| Source Plugin | 源插件。源插件的类型。 |
| Notes | 备注。有关 Sine 插件的其它信息。 |
| **正弦波参数** | |
| Frequency | 乐音的频率。  单位：Hz  Default value: 440.0  Range: 20 to 20000  Units: Frequency |
| Gain | 增益。乐音输出的电平或振幅。  单位：dB  Default value: -12  Range: -96.3 to 0  Units: dB |
| Duration | 乐音时长，期间振幅将一直保持恒定。  单位：s  Default value: 1.0  Range: 0.001 to 3600 |
| |  | | --- | |  |  (Link/Unlink) | 显示是否在所有平台上应用 Channel 选择。 |
| Channel | 用于指定声音的输出声道，包含两个选项：Mono 和 LFE。  Default value: Mono |

---