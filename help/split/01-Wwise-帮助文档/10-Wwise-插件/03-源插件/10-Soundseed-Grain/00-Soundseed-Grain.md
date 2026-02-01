# Soundseed Grain

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > Soundseed Grain

## Soundseed Grain

Soundseed Grain 是 Wwise 中的一款粒子合成器源插件。在粒子合成过程中，会分小段播放音频文件（粒化），并为其应用振幅包络（加窗），然后在输出时实施下混。同时，对每个粒子的发射间隔、粒子的时长、源文件的读取速度（相当于音高）、源文件中的位置这些属性进行独立控制，最终的效果即利用单个源文件生成各种各样的声音。另外，由于粒子的发射间隔可能小于其时长，所以粒子之间有时会重叠。

利用此粒子合成工具，设计师可以尽情地发挥创意，并巧妙地设定运行时参数，最终制作出各种新奇有趣的声音。

|  |
| --- |
|  |

本图很好地阐释了粒子合成的一般概念。注意，它并不局限于 Wwise Soundseed Grain。

图片来源：Miraglia, Dusti. “Grain: A Comprehensive And In-Depth First Look Into Propellerhead's New Granular Synth From Reason 10. Should It Really Just Be 'Taken With A ‘Grain’ Of Salt'?” LearnSoundDSine.com, 9 Dec. 2017, learnsounddsine.com/2017/10/22/grain-a-comprehensive-and-in-depth-first-look-into-propellerheads-new-granular-synth-from-reason-10-should-it-really-just-be-taken-with-a-grain-of-salt/。

Soundseed Grain 能单独为每个粒子应用滤波效果，而且还拥有 3D 空间化功能。所有这些参数都可通过 RTPC 和内嵌粒子调制器（Mod 1、Mod 2、Mod 3 和 Mod 4）进行调制和随机化。

### Waveform view

Waveform（波形）视图会按照声道下混样式来显示该插件使用的音频文件波形。在此，可使用 Filename（文件名）字段右侧的“浏览”按钮 [...] 加载新的音频文件。

|  |
| --- |
|  |

在 Waveform 视图右下角，可以看到 Wave 文件的有效时长（如插件所示）。在 Source（源）选项卡中更改文件的 Trim（修剪）点时，该时长会随之变化。有关 Soundseed Grain 媒体管理的更多详细信息，请参阅“[“Source settings”一节](02-Source-Editor-Soundseed-Grain.md#ssg_source_settings "Source settings")”。在设置 Playback Position（播放位置）对应的调制器（见“[“Using saw up mode for scanning file/implement time scaling effects”一节](01-Soundseed-Grain-tips.md#Using_saw_up_mod_for_scanning_file "Using saw up mode for scanning file/implement time scaling effects")”）时，可以参考文件时长。

通过拖动 Position（位置）和 Offset（偏置）光标（Offset 仅在选中 Snap to markers 时显示），可以快速、精准地更改对应的 Position 和 Offset 属性（见“[“控件”一节](00-Soundseed-Grain.md#ssg_playback)”）。

在激活工具栏中的 Start Capture/Stop Capture（开始捕获/停止捕获）按钮来捕获数据时，Grain Visualizer（粒子观察器）会叠加显示在 Waveform 视图之上，并显示文件中每个粒子的瞬时位置。其中，矩形的透明度代表了粒子包络的音量。有关数据捕获的更多详细信息，请参阅“[“从声音引擎捕获数据”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/00-从声音引擎捕获数据.md "从声音引擎捕获数据")”。

### 控件

The Soundseed Grain plug-in has six groups of controls, described below.

|  |
| --- |
|  |

**Grains**

In the Grains group you can define the time between each grain's emission, the grains' duration, and the shape of the envelope. 这些设置会直观地显示在 Envelope Visualizer 中。

您可以通过指定粒子的发射间隔或发射速率（频率）来设置粒子发声。另外，也可使用 MIDI 音符来控制相关属性（见“[“使用 MIDI”一节](00-Soundseed-Grain.md#Using_MIDI "使用 MIDI")”）。在 Select Freq/Time（选择频率/时间）下拉菜单中，可通过选择相应的菜单项来指定设置方式。粒子发射间隔和粒子时长的值可从很低设到很高，而且还能精确到采样点，不受 Wwise 声音引擎的帧大小（控制速率）的限制。

您可以通过选择相应的菜单项来设置粒子的时长：

- **Time between Emissions**（发射间隔）：直接设定值。
- **Emissions per second**（每秒发射次数）：发射间隔的倍数。
- **MIDI Duration**（MIDI 时长）。

**播放**

The Playback group exposes controls to define position in the source audio file where grains are read. 其中，Position（位置）用来定义源音频文件中粒子的开始位置（表示为文件时长的百分比）。在顺序读取文件时，Speed（速度）和 Pitch（音高）则用来控制读取方向和速度。在将 Speed 绝对值设为大于或小于 1 时，将导致音高升高或降低。在将 Speed 设为负值时，将反向读取源音频文件。

在粒子的读取位置跨过 100%（反向时为 0%）时，将折回 0%（反向时为 100%）。

在设有标记时，通过选中 Snap to markers（对齐到标记），可将标记位置作为粒子开始位置。标记可手动导入和编辑，也可自动指派给源音频文件中的 Transient（瞬态峰）。有关标记的更多详细信息，请参阅 [Source 选项卡](02-Source-Editor-Soundseed-Grain.md#ssg_source_settings "Source settings")。

**Filter**

每个粒子都有一个独立的滤波器，The Filter group controls it. 因为要将滤波器单独应用于每个粒子，所以最好结合调制器使用该滤波器。假如要对整条输出统一实施滤波（比如为所有粒子应用相同的滤波器设置），为了提升 Wwise 的性能，最好使用 EQ 插入效果器。

**定位**

This group defines the behavior with multichannel output. The output channel configuration is set in the Output group below. 在选择 Direct Speaker Assignment（直接指派扬声器）时，将把源文件的各个声道原样指派给合成器输出的对应声道；在选择 3D Spatialization（3D 空间化）时，则会使用 Azimuth（方位角）、Elevation（高度角）和 Spread（散布）对每个粒子实施空间化处理（“[“Source Editor: Soundseed Grain”一节](02-Source-Editor-Soundseed-Grain.md "Source Editor: Soundseed Grain")”中对此有明确说明，具体可在 Wwise 的“[“Contextual Help”一节](../../../09-参考主题/02-视图/08-Contextual-Help.md "Contextual Help")”视图中查看）。

**Output**

Output（输出）分组框用于选择输出声道配置和合成器的整体电平。

在默认情况下，会在创建合成器后将默认的 Envelope（包络）指派给 Output Level（输出电平）。对于 MIDI，在触发 Note Off（音符关）事件时会停止合成器 。

**VU Meter**

This meters the signal at the output of the synthesizer, and its channel configuration matches that which is set in the Output group.

### Envelope visualizer

|  |
| --- |
|  |

Envelope Visualizer（包络观察器）方便预览粒子包络的形状和重叠情况。重叠量取决于发射速率、粒子时长和释音时间。这些值尚未经过 RTPC 或调制，所以实际结果可能会有所不同。

通过拖动此窗口顶部和底部的图柄，可编辑 Attack（起音）和 Release（释音）时间。In order to have asymmetrical windows, you first need to unlink Release from Attack by disabling the "link" button to the left of the Release parameter in the Grains group.

起音时间从粒子的开始位置算起，所以计入粒子的时长；释音时间从粒子的结束位置算起，故而不计入粒子的时长。

### Grain modulators and modulator assignment

|  |
| --- |
|  |

Soundseed Grain 设有 4 个 LFO / Randomizer，可指派给任何属性。除了内嵌到了粒子合成器的设置窗口中，这些所谓的 Grain Modulator（粒子调制器）还有一个主要特性，就是其取值在整个粒子持续期间保持不变。比如，在将某个粒子调制器指派给 Filter Cutoff（滤波器截止频率）时，每个粒子的滤波器截止频率在其持续期间都会保持不变。另一方面，它又有很高的响应频率。假如发射速率非常快，比方说每 100 毫秒发射一次，它会按此速度准确地为每个粒子返回一个新值。这些 LFO 会在每次发射粒子时调整一次属性，但并不受 Wwise 的控制速率（声音引擎的缓冲区大小）限制，因此可以及时地改变属性。

在左侧窗格中，可定义 Grain Modulator 的属性。在此，可选择各种双极波形和单极波形 (+)，并按照时间或频率来设置 LFO 速度。

在右侧窗格中，可指定将调制器指派给哪些属性。在此，可将属性指派给一个或多个调制器，并根据需要设定调制量。调制 Amount（数量）代表的含义因属性而异。总的来说，频率（Emission、Filter Cutoff 等）相关调制量一般按八度度量，而 Position、Pitch 和 Speed 的调制量通常按对应属性的单位度量（比如 Pitch 按音分度量）。如有疑问，请单击对应行的 Amount 滑杆，并查看 [“Contextual Help”一节](../../../09-参考主题/02-视图/08-Contextual-Help.md "Contextual Help") 视图。

在针对某项指派设定调制 Amount 之后，会应用 Quantization（量化）。比方说，为 Pitch 应用 Major（大调）量化，并将调制 Amount 设为 500 音分。对于单极调制，允许的 Pitch 偏置将为 0、200、400 和 500（对应 C Major 音阶的 C-D-E-F）；对于双极调制，则为 -500、-300、-100、0、200、400 和 500（对应 C Major 音阶的 G-A-B-C-D-E-F）。

在将 Grain Modulator 应用于某项属性时，该属性滑杆旁边的 Modulation（调制）图标会亮起。

|  |
| --- |
|  |

### 滑杆反馈

在捕获数据时，在滑杆的编辑区间下方会以亮线显示经过 RTPC 和调制后的当前滑杆值。在亮线快速移动时，以较深颜色显示的区间相比当前值会滞后。此行为与 VU 电平表相似。另外，因为插件内嵌了粒子调制器，所以滑杆的数值显示下方会显示深色区间。该区间直接受该属性的粒子调制 Amount 控制，这在调制速率大于粒子发射速率时非常有用。有关更多详细信息，请参阅上文的“Grain Modulator 和 Modulator Assignment”章节。

### 使用 MIDI

您可以通过 [Interactive Music](../../../06-创建互动音乐/00-创建互动音乐.md "创建互动音乐")（互动音乐）或 [Control Surface](../../../08-使用-Wwise/14-使用控制设备/00-使用控制设备.md "使用控制设备")（控制器）发送的 MIDI Event（MIDI 事件）来触发 Soundseed Grain 实例。同样地，也可设定由游戏或 SDK 发送 MIDI 音符。在合成器内，可根据需要灵活运用 MIDI 音符。比如，将 MIDI 音符的频率用作粒子发射速率。为此，可将 Select Freq/Time 下拉菜单设为 MIDI Emissions Per Second（每秒 MIDI 发射次数）。此外，也可同时另行使用 MIDI 音符的频率来控制粒子的时长。比方说，A1 (55 Hz) 对应 18.182 ms。为此，可将 Duration（时长）菜单设为 **MIDI Duration**（MIDI 时长）。另外，还可使用 MIDI 音符来控制粒子的 Pitch 偏置。为此，可选中 **MIDI Pitch**（MIDI 音高）复选框，并设定偏置基于哪个 Root note（根音）。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 在结合 MIDI 使用 Soundseed Grain 时，可能会希望让合成器按照上述方式处理音符追踪，而不是让 Wwise Pitch Shift 对合成器的整条输出信号统一实施音高变换。因此，对于应用了该插件的声音，请务必在 MIDI 选项卡中**禁用** Note Tracking（音符跟踪）。 |

**相关主题**

- [“Soundseed Grain tips”一节](01-Soundseed-Grain-tips.md "Soundseed Grain tips")
- [“Source Editor: Soundseed Grain”一节](02-Source-Editor-Soundseed-Grain.md "Source Editor: Soundseed Grain")
- [“Contents Editor: Soundseed Grain plug-in”一节](03-Contents-Editor-Soundseed-Grain-plug-in.md "Contents Editor: Soundseed Grain plug-in")

---