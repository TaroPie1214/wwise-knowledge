# Vorbis Encoder Parameters

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [ShareSets 选项卡](../00-ShareSets-选项卡.md) > [Conversion Settings Editor](00-Conversion-Settings-Editor.md) > Vorbis Encoder Parameters

#### Vorbis Encoder Parameters

In the Vorbis Encoder Parameters dialog you can define properties for Vorbis audio files. Vorbis 编码器是感知音频编解码器，能在改变比特率的同时稳定地保持指定的品质。在大多数情况下，使用默认模式会在相同比特率下实现最一致的品质。

|  |  |
| --- | --- |
| [备注] | 备注 |
| Audiokinetic 支持的 Vorbis 格式针对交互式媒体和游戏平台进行了优化。它不遵循标准的 Ogg/Vorbis 文件格式。请勿期待媒体播放器或其它标准 Ogg/Vorbis 工具能够正确读取这些流播放。 |

在某些需要严格控制比特率情况下，可以直接定义比特率设置。此功能通过使用一个 bitrate reservoir（位储存池）储存未使用的位，来让比特率以平均值为基准，保持在您指定的范围内。在很多情况下，这会导致品质下降。此选项仅应该在需要严格控制比特率的特定情况下使用。

此外，如果您打算使用 Vorbis 编码器，使用 **Play from elapsed time** 虚声部行为时就需要启用 Seek Table。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 对于Vorbis 编码文件，只有使用 Seek Table 进行转换时，远程连接过程中 Source Editor 的播放光标才起作用。 |

默认情况下，Seek Table 选项将处于关闭状态以节省磁盘空间。请确保在选择此虚声部行为的情况下打开此设置；否则，使用时将不会播放声音。

- For more general information about the Vorbis codec, refer to: <http://vorbis.com/faq>.
- For more technical information on the Vorbis codec, refer to: <http://xiph.org/vorbis/doc/Vorbis_I_spec.html>.

| 界面元素 | 描述 |
| --- | --- |
| Quality Factor | 品质因数。压缩文件品质表示为十进制浮点值， -2 作为一个超低设置，相对于恒定品质更注重低比特率，而 0.0 的目的是产生一直稳定的品质结果。  更高的品质设置意味着：  - 需要更多的磁盘空间 - 更好的音频品质 - 产生稳定一致的品质结果  Vorbis 可变比特率编解码器将在改变比特率的同时，稳定地保持您指定的编码品质。高压缩率可能导致品质下降。为了获得更高的品质就要降低压缩率，请选择较大的品质数值。  默认值：+4 范围：-2 至 +10  对于低于 0 的品质编码设置，每个立体声文件的Vorbis 解码器将占用 24 KB 的底层引擎内存。 |
| Managed Bitrate | 定制比特率。管理各个声道的平均比特率，以及最小和最大比特率。  尽管 Vorbis 编解码器原生支持可变比特率，它也支持限定最小值和最大值来“管理”流播放比特率，以及让其趋近平均值的功能。以上功能仅应在要求限制比特率时才能使用，例如要限制文件流播放的带宽时。虽然差别通常较小，但定制比特率模式的输出效果相比可变比特率编码（使用相等比特率）的效果要逊色。  |  |  | | --- | --- | | [备注] | 备注 | | 请注意，当设置得太过或将比特率限制在极小范围内都可能影响输出品质，结果会极其糟糕。 | |
| Average bitrate (kbps per channel) | 平均比特率（每声道 kbps）。平均比特率值，位储存池将以此为参考值来跟踪编码比特率。  默认值：64  范围：16 至 240 单位：每声道 kbps |
| Min bitrate (kbps per channel) | 最小比特率（每声道 kbps）。编码声道的最小比特率。  默认值：64  范围：16 至 240  单位：每声道 kbps  Vorbis 编解码器支持的有效比特率范围有限，具体取决于编码文件的采样率。有效范围相关的详细信息，请查阅[“Valid Vorbis Bitrate Setting”一节](02-Vorbis-Encoder-Parameters.md#valid_vorbis_bitrate_settings "Valid Vorbis Bitrate Setting")。 |
| Max bitrate (kbps per channel) | 最大比特率（每声道 kbps）。编码声道的最大比特率。  默认值：64  范围：16 至 240  单位：每声道 kbps  Vorbis 编解码器支持的有效比特率范围有限，具体取决于编码文件的采样率。有效范围相关的详细信息，请查阅[“Valid Vorbis Bitrate Setting”一节](02-Vorbis-Encoder-Parameters.md#valid_vorbis_bitrate_settings "Valid Vorbis Bitrate Setting")。 |
| Advanced Settings | 高级设置。启用存储池（reservoir）设置的功能。  此功能应仅供具有编码专业知识的用户使用。 |
| Bit reservoir time | 位储存池时间。位储存池在跟踪比特率时将使用的最小/最大比特率限制。在此范围内，位储存池通过控制音频帧大小和改变比特率，可以让起伏较大的比特率趋于平均。  默认值：2  范围：0 至 10  单位：秒 |
| Reservoir bias factor | 位储存池偏差因数。此设置影响位储存池如何进行位存储 —— 设置较高时，将导致低比特率情况下可以储存更多的位。设置越低，比特率变化时储存的位也会越少。  默认值：0.1 范围：0 至 1 |
| Average track slew time | 平均跟踪转换时间。位储存池跟踪器在响应最小和最大比特率时间时的过渡时长。  默认值：1.5  范围：0 至 10  单位：秒 |
| Seek table granularity (sample frames) | Seek Table（文件定位表）粒度（采样帧）。这些设置用于确定音频文件将使用多少 Seek 位置或关键帧。Seek Table 通常用于选择了 Play from elapsed time 选项的虚声部。设置越低，声音恢复时间将越靠近准确的剩余时间。  默认：16,384  范围：1,024 至 32,768  单位：PCM 帧（每帧为 1/采样频率） |
|  | Closes the Vorbis Encoder Parameters dialog and saves your settings. |
|  | Closes the Vorbis Encoder Parameters dialog without saving your settings. |

  

##### Valid Vorbis Bitrate Setting

有效 Vorbis 比特率设置。比特率控制是使用位储存池算法来实现的。在编码过程中，编码器将固定大小的储存池用作编码“储蓄帐户”。在音频帧采样小于目标比特率时，未使用的位将被储存到池中，以供将来的音频帧使用。当帧采样大于目标比特率时，则会从池中提取“存储”的位。编码控制将防止储存池变为负值（在指定了最大比特率时）或超过上限（在指定了最小比特率时）。“平均比特率”作为长范围比特率跟踪时的基准点，即根据帧采样大于或小于设定的平均值，来调整编码器的比特率大小。

Vorbis 编解码器支持的有效比特率范围有限，具体取决于编码文件的采样率。如果比特率设置（平均值、最小值、最大值）超出编码文件的有效范围，则这些值将会被设置成有效范围内最接近的值，一则警告将在转码对话框中将出现，并显示用于编码的实际比特率。Refer to the table below to determine valid bitrates for given sample rates.

| 采样（Hz） | 单声道最小值（kbps） | 单声道最大值（kbps） | 立体声最小值（kbps / 声道） | 立体声最大值（kbps / 声道） |
| --- | --- | --- | --- | --- |
| 8,000 | 8 | 42 | 5 | 32 |
| 10,000 | 14 | 50 | 8 | 44 |
| 12,000 | 14 | 50 | 8 | 44 |
| 14,000 | 14 | 50 | 8 | 44 |
| 16,000 | 16 | 100 | 10 | 86 |
| 18,000 | 16 | 100 | 10 | 86 |
| 20,000 | 22 | 90 | 14 | 86 |
| 22,050 | 22 | 90 | 14 | 86 |
| 24,000 | 22 | 90 | 14 | 86 |
| 28,000 | 24 | 190 | 14 | 190 |
| 32,000 | 24 | 190 | 14 | 190 |
| 36,000 | 24 | 190 | 14 | 190 |
| 44,100 | 26 | 240 | 16 | 250 |
| 48,000 | 26 | 240 | 16 | 250 |

---