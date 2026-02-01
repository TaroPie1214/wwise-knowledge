# Using RTPCs to fine-tune the audio mix

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [与游戏互动](../00-与游戏互动.md) > [使用 RTPC](00-使用-RTPC.md) > Using RTPCs to fine-tune the audio mix

## Using RTPCs to fine-tune the audio mix

动态混音在电子游戏中十分常见。我们经常会使用实时参数控制、混音事件和混音器快照来控制音频焦点。Another powerful tool for achieving clarity in games is side-chaining using Game Parameters and RTPCs.

旁链压缩会监控音频信号的电平，并用来操控另一音频信号。比如，在电台广播中，DJ 说话时会自动降低音乐的音量。在音乐制作中，经常使用旁链压缩来控制低频的能量。比如，在底鼓演奏时快速降低贝斯的音量。

### Game application

旁链压缩对游戏来说是非常强大的工具，它方便控制玩家关注焦点，并减少喧闹环境下的嘈杂声。另外对于同类对象，它还有助于安排优先级并获得清晰的混音。

当播放的重要声音中存在瞬态信号时，旁链压缩会按照瞬态形状来降低次要声音的音量。

![](../../../../images/side_chaining.png)

|  |  |
| --- | --- |
|  | 这个是重要声音。其 Output Bus 上插入有 Meter 效果器。 |
|  | 这些是次要声音。其 Output Bus 的音量会随着所测声音的音量的增大而减小。 |

通常，会先在同类对象之间设置优先级系统，再在不同类别之间设置优先级系统。例如，按照这一规则，游戏可判定玩家角色 (PC) 的武器声比非玩家角色 (NPC) 的武器声更重要。然后，旁链压缩就可设置为 PC 武器声播放时降低 NPC 武器声的音量。PC 和 NPC 之间的武器声非常相似；但是，在这种情况下，系统需要确保始终将 PC 声音作为玩家的主要关注焦点。

按照这一理念推断，游戏可判定附近爆炸声应作为主要关注焦点，优先于 PC 和 NPC 武器声。同样地，关键对白应优先于音效声（包括武器声和爆炸声）。

以下图表显示了这一系统的层级结构。

|  |
| --- |
|  |

### Setting up side-chaining with RTPCs in Wwise

在 Wwise 中，可利用实时参数控制 (RTPC) 和 Meter 效果器轻松设置侧链压缩。以下示例分三步介绍了如何让 PC Weapon 音频总线的信号自动压缩 NPC Weapon 音频总线的信号音量。

1. **创建 Game Parameter**：首先，创建一个游戏参数（即 PC\_Weapon\_Volume），并将取值区间设为 -48 ~ 0，近似代表游戏的动态范围。该游戏参数将被用作总线之间的沟通渠道。

   ![](../../../../images/create_game_parameter.png)
2. **在总线上插入 Meter 效果器**：然后，对于需要确保信号清晰可闻的总线（本例中为 PC\_Weapon 总线），为其插入 Meter 效果器，并选择 Output Game Parameter（输出游戏参数）。

   ![](../../../../images/meter_effect.png)

   Meter 效果器会监控输入的音频信号。在将效果器用于旁链压缩时，将使用 Mode（模式）、Attack（起音）、Release（释音）和 Hold（保持）参数来降低输出信号的响应速度，并将平滑处理后的值发送给游戏参数（本例中为 PC\_Weapon\_Volume）。
3. **创建 RTPC 曲线**：最后，为需要衰减的总线创建 RTPC 曲线。在本例中，先将总线音量关联至 PC\_Weapon\_Volume 游戏参数，然后创建衰减曲线。X 轴代表 Meter 效果器计算得出的 RMS 信号，Y 轴代表 NPC Weapon 音频总线音量的衰减量。

   ![](../../../../images/create_rtpc.png)

若要使用旁链压缩构建总线层级结构，只需重复上述三个简单步骤即可。

### Other applications

因为 Meter 效果器输出的是通用游戏参数，所以任何可关联至 RTPC 的属性都可由旁链压缩驱动。例如，可以用旁链压缩控制 EQ 频段的增益，从而对特定频段进行陷波处理。再如，可以驱动 Compressor 效果器的阈值、修改 Flanger 效果器的 LFO 频率或者增大 FutzBox Lo-Fi 效果器的失真强度。

In addition to the Meter Effect, the Multiband Meter Effect is available to easily measure the audio across specific frequency bands, which might be useful for specific manipulation of EQ bands. 有关详细信息，请参阅[“Multiband Meter”一节](../../10-Wwise-插件/04-效果器插件/13-Multiband-Meter.md "Multiband Meter")。

|  |  |
| --- | --- |
| [备注] | 备注 |
| This topic describes how to use Game Parameters and RTPCs to set up and configure side-chaining in order to control various aspects of the audio mix. Wwise also has Sidechain Mixes available as a separate system, described in [“Using Sidechain Mixes with Effects”一节](../../05-使用声音和振动来提升游戏体验/04-管理效果器/04-Using-Sidechain-Mixes-with-Effects.md "Using Sidechain Mixes with Effects"), which might be desirable for some applications due to greater precision, or ease of use. |

---