# 使用 Ambisonics

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../../00-使用声音和振动来提升游戏体验.md) > [定义定位](../00-定义定位.md) > 使用 Ambisonics

## 使用 Ambisonics

Ambisonics 是一种环绕声技术，可以覆盖水平面以及听者上方和下方的区域。B-format 声场通过球谐函数来表示，能够独立于扬声器配置发挥效果。可以想见，这样就能轻松实现声音跟随听者的旋转。对于声音设计师所需的更加全方位的环绕声表现形式，比如在提供环境声或进行 VR 研发时，Ambisonics 都是可行的选择。<片段1100>

利用 Wwise，可执行以下操作：

- 按照 FuMa 格式（最高三阶）或 AmbiX 格式（最高五阶）导入并播放 B-format 素材。
- 将其他总线配置编码为 Ambisonics 格式，并将 Ambisonics 解码为其他总线配置。
- 使用效果器插件来自定义 Ambisonics 解码。
- 使用 Binauralizer 效果器插件（如 Auro Headphone 和 Resonance Audio）将 Ambisonics 信号转码为立体声信号。
- 使用效果器插件（除了 Stereo Delay 和 Matrix Reverb）来像其他格式一样处理 Ambisonics 信号。
- 将 Ambisonic Bed 传给支持 Ambisonics 的音频设备。支持 Ambisonics 的平台越来越多，此输出可在任一所述平台上播放。
- 使用 Recorder 插件将 Ambisonics 总线的信号录制到磁盘上并重新导入。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| Wwise 示例工程中提供了几个有关 [Ambisonics 用法](https://www.audiokinetic.com/library/edge/?source=SampleProject&id=example_ambisonics)的示例。 |

**使用 Ambisonic 文件的方法如下：**

1. 导入录制的 B-format Ambisonic 文件，该格式像其他音频文件一样，可以保存为 WAV 或 AMB。有关详细信息，请参阅[“导入媒体文件”一节](../../../03-设置工程/05-管理工程中的媒体文件/02-导入媒体文件/00-导入媒体文件.md "导入媒体文件")。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 若要导入 Ambisonics 文件（AMB、AmbiX 和 WAV 文件）并确认 Wwise 已将其正确识别为 Ambisonics，请打开 Source Editor（源编辑器）并查看或编辑 Channel Configuration Override（改写声道配置）菜单中的值。若要打开 Source Editor，请在 Contents Editor（内容编辑器）内双击 SFX（音效）、Music Track（音乐轨）或 Voice（语音）图标。（Views 菜单 > Contents Editor 或 Shift+O）。 |
2. 与其他声音对象一样，请指定适当的 Audio Bus 作为 **Output Bus**。请参阅 [“指定对象的输出连线”一节](../../../07-完善工程/01-管理输出/01-指定对象的输出连线.md "指定对象的输出连线") 了解详细信息。
3. 若要创建球面声场，请将声音对象的 Spread（散布）设为 100%。有关详细信息，请参阅 [“定义各种对象属性的衰减曲线”一节](../07-应用衰减/03-定义各种对象属性的衰减曲线.md "定义各种对象属性的衰减曲线") 章节。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 在被视作声场并结合使用 3D Spatialization 时，倘若 Spread 保留设为默认值 0，Ambisonics 会像其他多声道文件一样收缩成单声道点声源。 |

Wwise 将根据需要为各声道混音。有关详细信息，请参阅[“对 Ambisonics 进行子混音”一节](04-对-Ambisonics-进行子混音.md "对 Ambisonics 进行子混音")。

**创建 Ambisonics 输出：**

1. 将 Audio Bus 设为以下 Ambisonics 总线配置：

   - **Ambisonics 1st Order**（4 声道）
   - **Ambisonics 2nd Order**（9 声道）
   - **Ambisonics 3rd Order**（16 声道）
   - **Ambisonics 4th Order**（25 声道）
   - **Ambisonics 5th Order**（36 声道）

   有关声道配置的更多信息，请参阅 [Available Ambisonics Bus Configurations table](../11-了解总线配置.md#available_ambisonics_bus_configurations)。

   对于通过上述 Audio Bus 输出的源文件，Wwise 会将其混音并适配 Ambisonic 输出。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | If your Sound Engine Audio System specified in the Authoring Audio Preferences dialog is an Audio Device that supports ambisonics, then you can skip this initial step because the Main Audio Bus will already be set to ambisonics. 请参阅 [“Selecting audio output devices”一节](../../../02-入门/04-个性化您的工作空间/05-Setting-authoring-audio-preferences.md#setting_output_devices "Selecting audio output devices")。 |
2. 指定一个支持 Ambisonic 声道配置的最终输出设备，例如 3D 双耳系统。

   若不是支持 Ambisonics 的输出，则 Wwise 将自动把对应的声道输出解码为适用的标准输出。有关详细信息，请参阅[“对 Ambisonics 进行子混音”一节](04-对-Ambisonics-进行子混音.md "对 Ambisonics 进行子混音")。

---