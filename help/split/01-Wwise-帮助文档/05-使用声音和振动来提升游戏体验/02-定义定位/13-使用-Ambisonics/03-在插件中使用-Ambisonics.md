# 在插件中使用 Ambisonics

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../../00-使用声音和振动来提升游戏体验.md) > [定义定位](../00-定义定位.md) > [使用 Ambisonics](00-使用-Ambisonics.md) > 在插件中使用 Ambisonics

### 在插件中使用 Ambisonics

Wwise 插件 API 使用 [`AK_ChannelConfigType_Ambisonic`](https://www.audiokinetic.com/library/edge/?source=SDK&id=_ak_speaker_config_8h_a9e3e31d9ff388daa593222da7672a999.html) 暴露了 Ambisonics 声道配置。因此，在[创建新的插件](https://www.audiokinetic.com/library/?source=SDK&id=goingfurther__newplugins.html)时，开发者可以使用 Ambisonics Bed。

#### Using ambisonics with Effects

Wwise 中所有独立处理声道的效果器（如 Compressor、Guitar Distortion 和 Parametric EQ 插件）都支持 Ambisonics。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 为了保留空间声场，应该在“linked channels（声道链接）”模式下使用压缩效果器。 |

相反，混响效果器对于声道的处理则不同。They typically downmix the input channel, reverberate it, and upmix the reverberated output by mixing more or less decorrelated signals into the output channels. RoomVerb 和 AK Convolution Reverb 可以应用于 Ambisonics 声部/总线。They take the W (omni) channel, reverberate it, and upmix it by mixing decorrelated signals to the omni and directional channels. Matrix Reverb 如应用于 Ambisonics 声部/总线会无法初始化。

---