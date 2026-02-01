# Limiter

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [Audio Device 效果器插件](../00-Audio-Device-效果器插件.md) > [Mastering Suite](00-Mastering-Suite.md) > Limiter

### Limiter

Limiter 模块用于控制音量以免其超出用户定义的阈值。

![](../../../../../images/sms_limiter.png)

Link Channels（链接声道）复选框允许在声道之间链接各项 Limiter 属性。在默认情况下，此选项处于未选中状态。这时会对各个声道单独进行限幅。

可用的 Limiter 模式有三种：[“Hard-knee limiter”一节](04-Limiter.md#mastering_suite_module_limiter_hard_knee "Hard-knee limiter")、[“Soft-knee limiter”一节](04-Limiter.md#mastering_suite_module_limiter_soft_knee "Soft-knee limiter") 和 [“Advanced limiter”一节](04-Limiter.md#mastering_suite_module_limiter_advanced "Advanced limiter")。可用参数因模式而异（详见下表）。

| Limiter Mode | Attack | Release | Gain | Latency |
| --- | --- | --- | --- | --- |
| [“Soft-knee limiter”一节](04-Limiter.md#mastering_suite_module_limiter_soft_knee "Soft-knee limiter") | 可配置 | 可配置 | 不适用 | 不适用 |
| [“Hard-knee limiter”一节](04-Limiter.md#mastering_suite_module_limiter_hard_knee "Hard-knee limiter") | 不适用 | 不适用 | 不适用 | 不适用 |
| [“Advanced limiter”一节](04-Limiter.md#mastering_suite_module_limiter_advanced "Advanced limiter") | 不适用 | 可配置 | 可配置 | 2.67 ms |

#### Soft-knee limiter

When the audio signal exceeds the threshold level, the soft-knee limiter temporarily allows the threshold to be exceeded, and gradually changes the audio signal back to the threshold level over the specified attack time. 在音频信号的电平降到阈值以下时，则会在指定的释音时间内逐渐停止信号衰减。

The soft-knee limiter keeps distortion to a minimum and produces natural-sounding results. 不过，除非为阈值和起音时间设置一定的余量，否则其将无法正常工作。If the threshold is too high, or if the attack time is too long, the soft-knee limiter operates in the same way as the [“Hard-knee limiter”一节](04-Limiter.md#mastering_suite_module_limiter_hard_knee "Hard-knee limiter") when the signal reaches 0 dB.

#### Hard-knee limiter

With the hard-knee limiter, audio signals are cut off at the threshold value. 这对信号只在短时间内超出阈值的情况比较有用，但若频繁超出阈值，则可能会出现严重失真。

#### Advanced limiter

The advanced limiter is the most transparent of the three limiters while allowing more control over the output. 这是因为信号并不会超出阈值。*It achieves this by introducing a small latency of 2.67 ms.* This allows the limiter to automatically configure the attack and react to peaks smoothly, before the input reaches the threshold. 在此模式下，可配置阈值、释音时段和输出增益。

|  |  |
| --- | --- |
| [注意] | 注意 |
| *The advanced limiter mode is not supported when mixing with Audio Objects.* For performance reasons, the advanced limiter mode is replaced by the soft limiter mode when mixing with Audio Objects.  *这一限制不适用于 PS5，该平台在硬件中实施处理。* |

---