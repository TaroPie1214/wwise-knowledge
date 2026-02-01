# Creating audio Conversion Settings ShareSets

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理输出](../00-管理输出.md) > [对音频文件做转码](00-对音频文件做转码.md) > Creating audio Conversion Settings ShareSets

### Creating audio Conversion Settings ShareSets

您应当基于您项目和各个活跃平台的需求来创建用于管理转码设置的 ShareSet。。您在此处的许多选择都可能对音频工程的性能和品质产生重大影响。在对工程中的对象应用 ShareSets 后，您可以随时回来调整转码设置 ShareSet，以在平台和游戏的约束下取得最佳的品质。在您导入音频文件时，您还可以复用在此为多语言和源版本定义的 ShareSet 来加速这一过程。

您可以将其中一个 ShareSet 用作工程的默认转码设置。有关详细信息，请参阅[“指定 Default Conversion Settings”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/02-定义工程的转码设置.md#specifying_default_conversion_settings "指定 Default Conversion Settings")。

Conversion Settings Editor 分为两大区域：

- **Setting**：Audio Source 上方的区域。在此区域中您可以针对每个平台设置转码设置，包括采样率、音频格式和声道数量。
- **Result**：此区域中列出您的所有音频源。在此区域中您可以比较原始源和转码源，包括声道数量、采样率和文件大小。

![](../../../../../images/conversion_settings_editor.png)

音频转码过程保留了原始文件中的相同音高和时长；不过您可以为您的转码定义以下属性：

- 声道数量（请参阅下文的 [“About audio channels”一节](01-Creating-audio-Conversion-Settings-ShareSets.md#about_audio_channels "About audio channels")。）
- 左右混音
- 采样率 （请参阅下文的 [“关于采样率”一节](01-Creating-audio-Conversion-Settings-ShareSets.md#about_sample_rates "关于采样率")。）
- 音频格式 （请参阅下文的 [“About audio formats”一节](01-Creating-audio-Conversion-Settings-ShareSets.md#about_audio_formats "About audio formats")。）
- 音频格式品质
- 采样率转码品质

您还可以指定您是否要：

- 为对口型或字幕**Insert a filename marker**（插入文件名标记）；
- [**Remove DC offset**](02-Removing-DC-offsets.md "Removing DC offsets")（移除直流偏置）；

  |  |  |
  | --- | --- |
  | [注意] | 注意 |
  | 对于循环声音，建议保留 DC 偏置。移除机制采用高通滤波器。因此，其可能会以不同的方式修改循环的第一个和最后一个样本。在连续播放第一个和最后一个样本时，这样可能会导致信号中断进而产生可辨的咔哒声。 |
- **Apply dither**（应用抖动）；或者
- **Allow channel upmix**（允许声道上混），这意味着当声道被标为 **Stereo** 或 **Stereo drop** 时单声道源文件将转换成立体声。

  |  |  |
  | --- | --- |
  | [备注] | 备注 |
  | 如果未选择此选项，则无论 **Channel** 设置是什么，单声道源文件都将保留单声道。 |

#### About audio channels

在对多声道音频源进行转码时，必须决定要保留哪些声道。有关详细信息，请参阅[“Channel Configuration”一节](../../../03-设置工程/05-管理工程中的媒体文件/01-导入的过程/01-支持哪些媒体文件？.md#channel_configuration "Channel Configuration")。

您可以自由选择以下声道选项。不过，只有 ADPCM、WEM Opus、PCM 和 Vorbis 音频格式支持多声道文件的所有配置。在音频格式不支持所选声道选项时，Wwise 会将内容下混为下一个支持的配置。

| 声道选项 | 描述 | 备注 |
| --- | --- | --- |
| As Input | 保留与原始媒体文件相同的音频声道数量。 | 部分平台可能不支持某些音频格式，这时会将多声道文件下混为立体声文件。 |
| Mono | 所有声道全部混音为一个声道。 | L-R Mix 只用于从立体声到单声道的转换。其它声道配置根据[“下混行为”一节](../12-下混行为/00-下混行为.md "下混行为")下混。  LFE 声道总是要丢弃。 |
| Mono drop | 除第一个声道外，丢弃所有声道。 | 根据原始文件的声道配置，第一个声道可以是左声道，也可以是中置声道。 |
| Stereo | 所有声道混音为左前和右前声道。 | L-R Mix 只用于从单声道到立体声的转换。其它声道配置根据[“下混行为”一节](../12-下混行为/00-下混行为.md "下混行为")下混。  LFE 声道总是要丢弃。 |
| Stereo drop | 除定义为左声道或右声道外，丢弃所有其它声道。 | 如果没有定义左声道或右声道，但定义了中置声道（单声道），则会发生以下转换：  左 = 0.707C 右 = 0.707C  转码结果文件将是原始文件的两倍大。 |
| 5.1 | 强制转码为 5.1。 | 保留 Left、Right、Center、LFE、Surround Right 和 Surround Left 声道。  将标准高度声道（如有）下混到匹配的声道中。  若输入格式未包含全部所需声道，则最终输出将生成 5.1 内容，但不会在未提供内容的声道中填充任何声音。 |
| 5.1Drop | 弃用 Left、Right、Center、LFE、Surround Left 和 Surround Right 以外的所有声道。 |  |
| 7.1 | 强制转码为 7.1。 | 保留 Left、Right、Center、LFE、Surround Right、Surround Left、Back Left 和 Back Right 声道。  将标准高度声道（如有）下混到匹配的声道中。  若输入格式未包含全部所需声道，则最终输出将生成 7.1 内容，但不会在未提供内容的声道中填充任何声音。 |
| 7.1Drop | 弃用 Left、Right、Center、LFE、Surround Left、Surround Right、Back Left 和 Back Right 以外的所有声道。 |  |

注意，Wwise 不会实施任何多声道编码；它会直接将 LPCM 数据提供给采用立体声、5.1 或 7.1 环绕声配置的主机或系统。游戏机或系统一旦收到 LPCM 数据，就可以使用这些游戏机或系统支持的几乎任何格式输出这些数据，包括 Dolby、DTS 或 DPL2 格式。不过的确存在一些限制，包括：

- Android 和 iOS 平台仅支持立体声输出。
- Switch 平台仅支持立体声和 5.1 环绕声输出。
- Mac 和 tvOS 平台仅支持立体声及 5.1 和 7.1 环绕声输出。
- 其他平台（如 Windows、PlayStation 4、PlayStation 5、Xbox One 和 Xbox Series X）本身在输出端最高支持 7.1 声道。Wwise 可以支持所有标准声道配置（最高 13.1 声道）和匿名配置（最多 256 个声道）。注意，这些配置需要使用特殊的 sink 插件，这些插件可以解释这些配置或将它们传递到专用硬件。

#### 关于采样率

采样率决定数字音频信号每秒的采样次数。在决定选择什么采样率时，需要考虑许多因素。和其它品质/性能问题一样，设置采样率也是一项保持平衡的艺术。为了给您尽量多的控制，Wwise 为您提供了大量不同的采样率转码选项：

- **As Input** —— 使用与原始音频文件相同的采样率对文件做转码。如果特定平台或音频格式不支持该采样率，则会改用最接近的可用采样率。
- **Auto (Low/Medium/High)** —— 在对文件执行 FFT 分析后，使用 Wwise 选定的采样率对文件做转码。低、中、高品质设置之间的区别在于算法使用的截止阈值不同。You can tweak the quality level of each setting by defining their threshold values in the Project Settings dialog. 有关 Wwise 执行的自动采样率检测的详细信息，请参阅[“定义 Sample Rate Automatic Detection 设置”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/02-定义工程的转码设置.md#defining_sample_rate_automatic_detection_settings "定义 Sample Rate Automatic Detection 设置")。
- **300 to 48,000** -- 300 至 48,000。使用特定采样率对文件做转码。各个平台的采样率范围各不相同，最高 48,000 Hz。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 对于 **As Input** 和 **Auto**，您可以通过 **Min Sample Rate** 和 **Max Sample Rate** 分组框进一步限定采样率。 |

#### About audio formats

Wwise 支持以下音频格式。藉此，可更加灵活、可控地应对各个平台的限制：

- **[ADPCM](../../../14-词汇表.md#glossary_adpcm "ADPCM (Adaptive Differential Pulse Code Modulation")")**  —— 一种音频文件编码方法，可对声音信号和由对该声音信号做的预测之间的差异进行量化。ADPCM 量化步长是自适应的，与直接量化信号的 PCM 编码不同。基本上，ADPCM 以音质为代价，显著缩减了容量和 CPU 占用量。因此，它通常用于移动平台。
- **[WEM Opus](../../../14-词汇表.md#glossary_opus "Opus")**  – 一个所有平台均支持的低延迟音频编解码器，针对语音和通用音频进行了优化。就压缩时的音质损失而言，WEM Opus 要优于其他编解码器。利用 Bitrate（比特率）设置可以平衡数据压缩效率和感知声音品质。比特率越大，声音品质越好。此版本为 Opus 规格的标准应用，只不过存储在专门的容器中，在从磁盘进行流播放时寻址和循环效率更高。WEM Opus 解码器需要大量前滚缓冲才能开始解码，所以可能会占用大量 CPU 和流播放资源。因此，它不适合需要大量寻址或循环的情况，比如复杂的互动音乐、精确到采样点的循环或按照指定触发速率播放的容器。不过，为了弥补这一缺点，部分平台上会实施硬件加速的解码。
- **[PCM](../../../14-词汇表.md#glossary_pcm "PCM（脉冲编码调制）")** - Linear pulse-code modulation encoding, which is also referred to as uncompressed digital audio. PCM offers the best quality and performance at the expense of storage size. By default Wwise converts audio to a bit depth of 16, but you can select a conversion option to preserve 24-bit material at full resolution.
- **[Vorbis](../../../14-词汇表.md#glossary_vorbis "Vorbis")**  —— 一种感知编码方法，支持以固定和可变比特率编码音频文件，同时保持极好的感知声音品质。通过使用 Quality Factor 设置或指定每声道的最大、最小和平均比特率来控制数据压缩效率和感知声音品质之间的平衡。Vorbis 编码器可能需要使用寻址表。有关详细信息，请参阅[“结合 Vorbis 编码器使用 Seek Table”一节](05-转码技巧和窍门.md#using_seek_tables_with_vorbis_encoder "结合 Vorbis 编码器使用 Seek Table")。

  Audiokinetic 的 Vorbis 专用版本针对所有平台进行了高度优化。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 出于所有权方面的考虑，还有几种 Wwise 支持的平台专用音频格式在本页面中并未提到。授权用户可登录 Audiokinetic 官网并转到相应页面来查看这些格式的详细信息。 |

每种格式各有长短，您选择的格式取决于特定游戏的 CPU 和内存限制。有关何时使用哪种音频格式的进一步探讨，请参阅[“音频格式”一节](05-转码技巧和窍门.md#audio_formats "音频格式")。

#### About DC offsets

使用直流偏置滤波器是移除直流偏置的好办法，因为直流偏置可影响 Wwise 中的音量并产生副作用。不过，有的情况下不得移除直流偏置，例如精确到采样点的容器。在其它情况下，例如在声音归一化为 0 dB 的情况下，您可能需要消除直流偏置，也可能不需要。在转码过程中，默认移除直流偏置。You can, however, disable this setting if needed in the Conversion Settings dialog.

|  |  |
| --- | --- |
| [注意] | 注意 |
| 若直接从音频源生成振动效果，则移除 DC 偏置可能会更改控制器的振动输出。 |

**创建音频转码设置 ShareSet：**

1. 在 Project Explorer 中，切换到 ShareSets 选项卡。
2. 在 Conversion Settings 部分，选择您要创建新 ShareSet 的工作单元。
3. 在 Project Explorer 工具栏中，单击 **Conversion Settings** 图标 ![](../../../../../images/Conversion_Settings_icon.png)。

   选定的工作单元中创建一个新的转码设置 ShareSet。
4. 为 ShareSet 取一个恰当的名称，然后按 **Enter**。
5. 双击新建的 ShareSet 以将它加载到 Conversion Settings Editor 中。
6. 通过选择以下其中一个选项为各个平台指定声道：

   - **As Input** —— 保留与原始媒体文件相同的音频声道数。
   - **Mono** —— 将所有声道混音到一个单声道中。
   - **Mono drop** —— 丢弃除第一个声道外的所有声道。
   - **Stereo ——** 将所有声道混音到左前和右前声道。
   - **Stereo drop** —— 丢弃除左声道和右声道之外的所有声道。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 1. 在默认情况下，声道设置跨所有平台链接。要为特定平台设定唯一的声道设置，首先取消链接属性，然后定义设置。 2. 如果您不想增加单声道文件的声道数，则确保禁用 **Allow channel upmix** 选项。 |
7. 如果您将立体声源转换为单声道或者相反，则可以使用 L-R Mix 设置来指定分配给左声道和右声道的信号功率电平。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 在默认情况下，所有平台之间的 L-R Mix 设置是断开链接的。要为特定平台指定通用的 L-R Mix 设置，首先要链接属性，然后定义设置。 |
8. 在 Sample Rate 列表中选择转码期间每秒采样音频文件的频率。根据游戏的具体情形，您可以选择以下其中一个选项：

   - **As Input** —— 使用与原始文件相同的采样率来对文件转码。如果特定平台或音频格式不支持该采样率，则会改用最接近的可用采样率。
   - **Auto (Low/Medium/High)** —— 在对文件执行 FFT 分析后，使用 Wwise 所选的采样率对文件做转码。低、中、高品质设置之间的区别是截止阈值，该值可识别的频率可用于确定文件转码的最佳采样率。You can tweak the quality level of each setting by defining their threshold values in the Project Settings dialog. 有关 Wwise 执行的自动采样率检测的详细信息，请参阅[“定义 Sample Rate Automatic Detection 设置”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/02-定义工程的转码设置.md#defining_sample_rate_automatic_detection_settings "定义 Sample Rate Automatic Detection 设置")。
   - **300 to 48,000** —— 使用特定采样率对文件做转码。各个平台的采样率范围各不相同，最高 48,000 Hz。
9. 如果将 **Sample Rate** 设为 **As Input** 或 **Auto**，则使用 **Min Sample Rate** 和 **Max Sample Rate** 条目来限制转码采样率。
10. 在 Format（格式）列表中，选择转码所用的音频格式。

    |  |  |
    | --- | --- |
    | [备注] | 备注 |
    | 有些音频格式包含可修改的编码参数。在选用这些音频格式时，Adv. 列中会显示 **Edit** 按钮。单击 **Edit** 按钮可修改所选音频格式的编码参数。For a complete description of the encoding parameters for each audio format, click the Help button in the corresponding dialog. 有关为 Vorbis 音频格式选择参数的最佳做法，请参阅参考文档中的 Vorbis Encoder Parameter 页面。 |
11. 在 Sample rate conversion quality 列表中选择用于转码文件采样率的方法。您可以选择以下其中一种选项：

    - **Normal (Faster)** —— 以高出 Best 选项三到六倍的速度进行高品质转码。
    - **High (Slower)** —— 产生最高品质的转码。

    |  |  |
    | --- | --- |
    | [备注] | 备注 |
    | 如果您希望内容中包含高频分量并且您正在转码到低于 24 kHz 的采样率，则建议使用 High 选项。 |
12. 如果您想在各个转码结果文件的开头创建一个标记，则从 Insert Filename Marker 列表中选择 **Yes**。

    此标记只包含文件名，不包含文件的路径和扩展名。在您将动作绑定到声音引擎中播放的声音上时（例如对口型或制作字幕），让名称能看得见会非常有用。
13. 如果您不想在转码过程中移除直流偏置，则取消勾选 **Remove DC Offset** 复选框。

    在默认情况下此选项为勾选状态。在大多数情况下，应该选择移除所有直流偏置。但是在有些情况下，可能不需要消除直流偏置，这些情况包括：

    - 将添加到精确到采样点的容器的声音。
    - 归一化为 0 dB 的声音。

      有关直流偏置如何影响 Wwise 中的音频信号的详细信息，请参阅[“Removing DC offsets”一节](02-Removing-DC-offsets.md "Removing DC offsets")。

    |  |  |
    | --- | --- |
    | [注意] | 注意 |
    | 如果您直接从音频源中生成振动，则应注意移除直流偏置将改变振动输出。 |
14. 如果您不想在比特率转码期间应用抖动，则应取消选择 **Apply Dither** 复选框。

    抖动是在量化之前添加到信号中的噪声，目的是减少量化过程导致的失真和噪声调制。只有在分辨率变化时（例如从 24 位变为 16 位）才应用抖动。
15. 关闭 Conversion Settings Editor。

    您指定的设置将自动保存，现在可将 ShareSet 指派到工程层级结构中的若干个对象上。
16. 根据工程中所需的转码设置 ShareSet 数量，重复执行步骤 1-14 若干次。

    |  |  |
    | --- | --- |
    | [备注] | 备注 |
    | 在填充 Audio Source 表格前，必须将转码设置 ShareSet 指派到对象，然后使用这些设置对音频文件转码。For more information on assigning a Conversion Settings ShareSet to an object, refer to [“Assigning Conversion Settings ShareSets to objects”一节](03-Assigning-Conversion-Settings-ShareSets-to-objects.md "Assigning Conversion Settings ShareSets to objects"). |

---