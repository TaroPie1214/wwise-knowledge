# Parametric EQ（参数均衡器）

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [Audio Device 效果器插件](../00-Audio-Device-效果器插件.md) > [Mastering Suite](00-Mastering-Suite.md) > Parametric EQ（参数均衡器）

### Parametric EQ（参数均衡器）

Parametric EQ 模块用于均衡不同频率的信号，最多支持六个 EQ 频段。

![](../../../../../images/sms_param_eq.png)

每个 EQ 频段都可单独进行控制和禁用，

并分别提供有多种滤波器模式可供配置。您可以根据滤波器模式来设置截止频率、谐振 Q 值和增益参数。下表简要列出了根据为给定频段选择的滤波器模式都可配置哪些参数。

| Filter Mode | Cut-off Frequency | Resonant Q Value | Gain |
| --- | --- | --- | --- |
| [“Off”一节](01-Parametric-EQ（参数均衡器）.md#mastering_suite_module_param_eq_mode_off "Off") | 不适用 | 不适用 | 不适用 |
| [“Low pass resonant (two-pole)”一节](01-Parametric-EQ（参数均衡器）.md#mastering_suite_module_param_eq_mode_low_pass_2p "Low pass resonant (two-pole")") | 可配置 | 可配置 | 不适用 |
| [“High pass resonant (two-pole)”一节](01-Parametric-EQ（参数均衡器）.md#mastering_suite_module_param_eq_mode_high_pass_2p "High pass resonant (two-pole")") | 可配置 | 可配置 | 不适用 |
| [“Peak (notch)”一节](01-Parametric-EQ（参数均衡器）.md#mastering_suite_module_param_eq_mode_peak "Peak (notch")") | 可配置 | 可配置 | 可配置 |
| [“High shelf”一节](01-Parametric-EQ（参数均衡器）.md#mastering_suite_module_param_eq_mode_high_shelf "High shelf") | 可配置 | 不适用 | 可配置 |
| [“Low shelf”一节](01-Parametric-EQ（参数均衡器）.md#mastering_suite_module_param_eq_mode_low_shelf "Low shelf") | 可配置 | 不适用 | 可配置 |
| [“Low pass one-pole”一节](01-Parametric-EQ（参数均衡器）.md#mastering_suite_module_param_eq_mode_low_pass_1p "Low pass one-pole") | 可配置 | 不适用 | 不适用 |
| [“High pass one-pole”一节](01-Parametric-EQ（参数均衡器）.md#mastering_suite_module_param_eq_mode_high_pass_1p "High pass one-pole") | 可配置 | 不适用 | 不适用 |

#### Off

滤波器按原样输出输入信号。

#### Low pass resonant (two-pole)

此滤波器会滤除高频信号，其在截止频率附近出现音量峰值（可配置）。它的滚降速率快于 Low Pass (One-Pole) 滤波器，为每个八度 -12 dB。

在该滤波器模式下，可以参数形式设置截止频率和 Q 值：

- 截止频率定义会在多高的频率出现滚降。
- Q 值按照如下方式控制滤波器谐振（Q 值越高，截止频率附近的信号衰减得越厉害）：

  - 在 Q=0.7 时，滤波器不会出现谐振峰值。音量在截止频率处的减小幅度为 -3 dB。
  - 在 Q=1.0 时，滤波器在截止频率以下出现谐振峰值。截止频率处的音量为 0 dB。
  - 在 Q=2.0 时，滤波器在截止频率处出现谐振峰值 (+6 dB)。

#### High pass resonant (two-pole)

此滤波器会滤除低频信号，其在截止频率附近出现谐振峰值（可配置）。它跟 Low Pass Resonant (Two-Pole) 滤波器相似，只不过会衰减截止频率以下的信号。

在该滤波器模式下，可以参数形式设置截止频率和 Q 值。

有关截止频率和 Q 参数的特性，请参见 [“Low pass resonant (two-pole)”一节](01-Parametric-EQ（参数均衡器）.md#mastering_suite_module_param_eq_mode_low_pass_2p "Low pass resonant (two-pole")") 滤波器模式。

#### Peak (notch)

此滤波器只会衰减截止频率附近的信号，而允许截止频率以上/以下的信号通过。

在该滤波器模式下，可以参数形式设置截止频率、Q 值和增益：

- 截止频率控制相对于输入音量的输出音量会在多高的频率出现峰值。
- Q 值控制受滤波器影响的频段宽度（以截止频率为中心）。Q 值越低，受影响的频段宽度越宽（峰值曲线越平坦）。Q 值越高，受影响的频段宽度越窄（峰值曲线越陡峭）。
- 增益控制截止频率处的音量增益（单位为 dB）。

#### High shelf

此滤波器会增大/减小高频信号的音量。频率在过渡频段以下的信号不受影响。

在该滤波器模式下，可以参数形式设置截止频率和增益：

- 截止频率控制过渡频段的中心频率。
- 增益控制过渡频段之后的音量增减幅度（单位为 dB）。

增益在截止频率处降低一半。

#### Low shelf

此滤波器与 [“High shelf”一节](01-Parametric-EQ（参数均衡器）.md#mastering_suite_module_param_eq_mode_high_shelf "High shelf") 滤波器正好相反，它会增大/减小低频信号的音量。频率在过渡频段以上的信号不受影响。

#### Low pass one-pole

此滤波器会滤除高频信号。

在该滤波器模式下，可以参数形式设置截止频率。

音量在指定频率处的减小幅度为 -3 dB，滚降速率为每个八度 -6 dB。也就是说，两倍截止频率处的输出为 -6 dB。在此之后频率每翻一倍，相对于输入音量的输出音量就会缓慢减小 6 dB。

#### High pass one-pole

此滤波器与 [“Low pass one-pole”一节](01-Parametric-EQ（参数均衡器）.md#mastering_suite_module_param_eq_mode_low_pass_1p "Low pass one-pole") 滤波器正好相反，它会滤除低频信号。

---