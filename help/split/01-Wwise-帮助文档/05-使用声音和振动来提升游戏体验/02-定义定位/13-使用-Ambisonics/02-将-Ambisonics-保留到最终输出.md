# 将 Ambisonics 保留到最终输出

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../../00-使用声音和振动来提升游戏体验.md) > [定义定位](../00-定义定位.md) > [使用 Ambisonics](00-使用-Ambisonics.md) > 将 Ambisonics 保留到最终输出

### 将 Ambisonics 保留到最终输出

在其中一条总线的 Bus Configuration（总线配置）设为 Ambisonics 时，Wwise 将生成 Ambisonics 信号。这些信号会被解码，也就是说只要 Ambisonics 总线的父总线将 Bus Configuration 设为标准多声道配置（如立体声或 5.1），信号就会被转换为这种标准的配置格式。

The Main Audio Bus inherits the configuration of the endpoint, which depends on the platform and is usually detected automatically. 大部分平台仅支持少数几种输出配置。通常是立体声、5.1 和 7.1。So, in general, the Main Audio Bus has a standard channel configuration, which forces decoding of child ambisonic busses to this configuration. 也就是说，在大部分情况下，Wwise 不会默认输出 Ambisonics 信号。

不过，可编写自定义 Audio Device（音频设备）插件来声明 Ambisonics 配置。In this case, the Main Audio Bus would have an ambisonics Bus Configuration and Wwise would preserve, not decode, the ambisonics signal.

|  |  |
| --- | --- |
| [备注] | 备注 |
| 有些终端支持 Ambisonics 信号。In these cases, the Main Audio Bus can inherit an ambisonics configuration. 有关详细信息，请参阅 [Wwise SDK](https://www.audiokinetic.com/library/edge/?source=SDK&id=index.html) 文档中的平台特定章节。 |

另外，若只想让 Wwise 将 Ambisonics 信号保存到文件中，可直接在 Ambisonics 总线上插入 [“Recorder 插件”一节](../../../10-Wwise-插件/04-效果器插件/17-Recorder-插件.md "Recorder 插件")。生成的文件将采用 FuMa 或 AmbiX 格式，其 Ambisonics 阶数等于 Recorder 所在总线的阶数。

---