# Mastering Suite

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [Audio Device 效果器插件](../00-Audio-Device-效果器插件.md) > Mastering Suite

## Mastering Suite

Mastering Suite 是一款免费插件，专门提供相应功能来对混音实施修正，以便在不同的终端上进行播放。这款多合一 Audio Device 效果器插件包含四个模块：[“Parametric EQ（参数均衡器）”一节](01-Parametric-EQ（参数均衡器）.md "Parametric EQ（参数均衡器）")、[“Multiband Compressor”一节](02-Multiband-Compressor.md "Multiband Compressor")、[“Master Volume”一节](03-Master-Volume.md "Master Volume") 和 [“Limiter”一节](04-Limiter.md "Limiter")。您可以根据所连终端和输出环境的特性来调节这些模块，从而提升音频输出的整体品质。

### 安装

若要使用 Mastering Suite，必须在 Wwise 上安装该插件。参见[安装付费和合作伙伴插件](https://www.audiokinetic.com/library/wwise_launcher/?source=InstallGuide&id=installing_integrated_plugins)。该插件需要获取授权才能激活并顺利生成 SoundBank（音频包）。如需从 Audiokinetic 获取免费授权，请访问[插件：Mastering Suite](https://www.audiokinetic.com/products/plug-ins/mastering-suite/)页面。

在安装插件后，会默认将 Mastering Suite 出厂素材添加到新建的工程。使用 [“Import Factory Assets”一节](../../../09-参考主题/01-工程/06-Import-Factory-Assets.md "Import Factory Assets") 对话框将其添加到现有工程。

### 用途

Mastering Suite 插件专门用在音频管线的末端。因此，其仅可插入到 System Audio Device（系统音频设备）的最后一个效果器插槽上。您可以在 Audio Device Editor（音频设备编辑器）的 Effects（效果器）选项卡中完成此操作。请参阅 [“Audio Device Editor：Effects”一节](../../../09-参考主题/04-Project-Explorer/01-Audio-tab/01-Audio-Devices/03-Audio-Device-Editor：Effects.md "Audio Device Editor：Effects")。

![](../../../../images/sms_insert.png)

出厂素材针对常见用例提供以下 ShareSet（共享集）：

- Headphones
- HomeCinema
- HomeCinemaHeightBoost
- NightMode
- NightModeStrong
- SoundBar
- TV

|  |  |
| --- | --- |
| [注意] | 注意 |
| 1. Only one instance of the Mastering Suite is supported at any time. This plug-in only    operates on the full mix, and is therefore categorized as an Audio    Device Effect. See [“了解声部管线”一节](../../../07-完善工程/01-管理输出/05-了解声部管线.md "了解声部管线") for    more details on the Wwise voice pipeline. 2. Mastering Suite is designed to use a speaker-based output configuration of up to 7.1.4    channels. Using other types of output configurations such as Ambisonics    causes the plug-in initialization to fail. |

|  |
| --- |
|  |

1. **[“Parametric EQ（参数均衡器）”一节](01-Parametric-EQ（参数均衡器）.md "Parametric EQ（参数均衡器）")**：可针对每个频段来配置滤波器模式、频率、谐振和增益。
2. **[“Multiband Compressor”一节](02-Multiband-Compressor.md "Multiband Compressor")**：可针对每个频段来配置频率、起音/释音时间、阈值、比率、补偿增益和拐点。
3. **[“Master Volume”一节](03-Master-Volume.md "Master Volume")**：可调节每个声道的音量设置。
4. **[“Limiter”一节](04-Limiter.md "Limiter")**：可选择软拐点、硬拐点和高级限幅模式。

这四个模块之间相互链接，其中禁用的模块将被视为旁通状态。每个模块在左上角都设有一个复选框。这样方便禁用不需要的模块或单独监听特定模块带来的效果。

|  |
| --- |
|  |

---