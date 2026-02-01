# 了解 Real-Time Parameter Control (RTPC)

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

了解 Real-Time Parameter Control (RTPC)

您可以使用 Real-Time Parameter Control (RTPC) 来基于游戏中的实时参数变化控制各种 Wwise 对象（声音、容器、控制总线、效果器等）的特定属性。

下面列举了几个有关如何在游戏中使用 RTPC 的例子：

- 在赛车游戏中，可根据车速和发动机每分钟（RPM）转速控制赛车发动机声音的音量和音高。
- 在滑雪游戏中，滑雪板的声音会随着速度和角度不断变化。
- 在设定为户外环境的场景中，可基于风速调节效果器的参数。
- 随机定位多个扬声器中的声音。您可以使用随机定位代码而非 Wwise 中创建的预定义路径驱动 RTPC 来对用户定义的 3D 声音实施左右和前后声像摆位。

除此之外，还可使用 RTPC 来根据游戏中发生的状况调节音频结构的属性。

声音设计师可在 Wwise 设计工具中定义游戏参数的名称和范围。除此之外，声音设计师还可定义 RTPC 曲线。游戏参数值代表 RTPC 曲线的 X 轴。

在声音设计师在 Wwise 设计工具中定义游戏参数和 RTPC 曲线后，游戏程序只需在游戏当中更新各个游戏参数的值即可。声音引擎通过在 RTPC 曲线上对游戏参数当前值（ X 值）取 Y 值来计算属性值。

如需详细了解声音设计师如何看待 RTPC，请参阅[使用 RTPC](https://www.audiokinetic.com/library/edge/?source=Help&id=working_with_rtpcs)。

如需简要了解 RTPC 集成，请参阅 [集成详情——RTPC](soundengine_rtpc.html) 章节。