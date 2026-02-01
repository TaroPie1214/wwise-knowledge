# Source Editor: Soundseed Grain

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > [Soundseed Grain](00-Soundseed-Grain.md) > Source Editor: Soundseed Grain

### Source Editor: Soundseed Grain

Source Editor（源编辑器）会显示所有与 Soundseed Grain 插件相关的属性。

在此页面的前半部分，我们先了解下该插件的 Effect Settings（效果器设置）选项卡。不过，Soundseed Grain 插件与其他插件有所不同，它还包含了另外两个选项卡。对此，我们将在下文 [“Source settings”一节](02-Source-Editor-Soundseed-Grain.md#ssg_source_settings "Source settings") 部分加以说明。

如需概括了解 Soundseed Grain 插件，请参阅 [“Soundseed Grain”一节](00-Soundseed-Grain.md "Soundseed Grain")。

| 界面元素 | 描述 |
| --- | --- |
| Name | 名称。用户为此 Soundseed Grain 插件实例设定的名称。 |
| Source Plug-in（源插件） | 源插件。源插件的类型。 |
| Notes | 备注。有关 Soundseed Grain 插件的其他信息。 |
| Filename | 文件名。粒子合成器所要使用的音频源文件（WAV 或 AMB）。单击该字段右侧的“浏览”按钮可选择文件。 |
| **Grains** | |
| Time between Emissions | 发射间隔。粒子的发射间隔，单位为 ms。  需将 Select Freq/Time 设为 **Time Between Emissions**。  Default value: 1000  Range: 0.05 to 50000 |
| Emissions per Second | 每秒发射个数。每秒发射的粒子数。  需将 Select Freq/Time 设为 **Emissions per Second**。  Default value: 1  Range: 0.02 to 20000  Units: Frequency |
| Duration Link | 在选择 **Duration Multiplier** 时，可将粒子时长指定为发射间隔的倍数。在选择 **Duration** 时，粒子时长完全独立于发射间隔。在选择 **MIDI Duration** 时，若通过 MIDI 音符触发合成器，则使用音符长度覆盖粒子时长。在调制 Duration 属性时，将调制 **MIDI Duration**。  Default value: Duration Multiplier |
| Duration Multiplier | 时长倍数。粒子时长相对于发射速率(使用 Emissions per Second 或 Time Between Emissions 设定)的倍数。此控件仅在 Duration Link 设为 Duration Multiplier 时可用。  在设为 1 时，实际粒子时长等于粒子发射间隔；此时，包络释音与包络起音重叠，粒子之间前后接合。在小于 1 时，粒子之间会有间隙；在大于 1 时，粒子将相互堆叠。  Default value: 1  Range: 0.001 to 1000 |
| Duration | 时长。粒子时长，单位为 ms。此控件仅在 Duration Link 设为 Duration 时可用。  |  |  | | --- | --- | | [备注] | 备注 | | 粒子包络的释音部分未计入粒子时长，所以粒子实际可能会更长一些。 |  Default value: 1000  Range: 0.02 to 10000.0 |
| Amplitude | 振幅。粒子的振幅，单位为百分比。  用调制器控制此控件，可以用于调节粒子的相对电平。  |  |  | | --- | --- | | [备注] | 备注 | | 若有效振幅降至零以下，则听到的结果是振幅回升，但信号会 180 度反相。 |  Default value: 100  Range: 0 to 100 |
| Attack | 起音。粒子包络的起音时间，单位为 ms。在 Window Mode 为 **Release Same as Attack** 时，Release 时间等于 Attack 时间。  Attack 包络从粒子开始位置算起，所以计入粒子时长；包络的释音部分(Release)从粒子结束位置算起，故而不计入粒子时长。  您可以使用 Grain Visualizer 窗口左上角的图柄来更改 Attack 时间。  |  |  | | --- | --- | | [备注] | 备注 | | 若 Attack 时间长于粒子时长，则播放粒子时不会达到其最大音量，而会按 Attack 被截断时的对应包络电平播放。 |  Default value: 10  Range: 0 to 5000 |
| |  | | --- | |  |  Window Mode | 若选择独立设置 Attack 和 Release，则可为包络 Attack 和 Release 时间设置不同的值。  默认值：Release Same as Attack |
| Release | 释音。粒子包络的释音时间，单位为 ms。在 Window Mode 为 **Release Same as Attack** 时，将忽略该设置。  释音包络从粒子结束位置算起，所以不计入粒子时长；包络的起音部分(Attack)从粒子开始位置算起，故而计入粒子时长。  您可以使用 Grain Visualizer 窗口右下角的图柄来更改释音时间。  Default value: 10  Range: 0 to 5000 |
| Grain Envelope Shape | 粒子包络形状。定义粒子包络中 Attack 和 Release 部分的形状。  可用选项包括：  - Linear - Constant Power - Exponential - Raised Cosine  Default value: Linear |
| **播放** | |
| Position | 粒子在源文件中的读取位置。该位置表示为文件时长的百分比。  若选中 Snap to markers 且存在标记，则将粒子的有效开始位置设到最靠近此控件所设位置的标记。  Default value: 0  Range: 0 to 100 |
| Snap to Markers | 对齐到标记。若选中该选项且存在标记，则将选定粒子的开始位置设到最靠近 Position 位置的标记。  Default value: false |
| Offset% | 粒子在源文件中的读取位置。该位置表示为文件时长的百分比。  此位置偏置仅在选中 Snap to markers 时生效，它会从最靠近 Position 的标记进一步偏置粒子开始位置。  Default value: 0  Range: -100 to 100 |
| Pitch | 音高。粒子移调所基于的音高，单位为音分。  在值大于 0 时，将加快播放速度；在值小于 0 时，将减慢播放速度。  有效播放速度同时取决于粒子 Speed。  Default value: 0  Range: -4800 to 4800  Units: Cents |
| Map MIDI to Grain Pitch | 将 MIDI 映射至粒子音高。在设置时，若通过 MIDI 音符触发合成器，则将相对于 Root 的音符值添加至粒子 Pitch。  Default value: false |
| Root MIDI Note | MIDI 根音。定义 MIDI 根音以便根据输入的 MIDI 音符值生成 Pitch 偏置。  Default value: 60  Range: 0 to 127 |
| Speed | 速度。粒子的播放速度。  - 在速度等于 1 时，将按照与原始声音相同的速度播放粒子。 - 在速度大于 1 时，将按照比原始声音快的速度播放粒子，因此其音高会偏高。 - 在速度小于 1 但为正值时，将按照比原始声音慢的速度播放粒子，因此其音高会偏低。 - 在速度为负值时，将反向播放粒子。  粒子播放的有效速度同时取决于粒子 Pitch。  Default value: 1  Range: -4 to 4 |
| **Filter** | |
| Filter Type | 滤波器类型。应用于各个粒子的滤波器类型。  - LPF6: 一阶(每个八度 6 dB)低通滤波器。在应用此滤波器时，参数 Filter Q 不起作用。 - LPF12: 二阶(每个八度 12 dB)低通滤波器。 - HPF6: 一阶(每个八度 6 dB)高通滤波器。在应用此滤波器时，参数 Filter Q 不起作用。 - HPF12: 二阶(每个八度 12 dB)高通滤波器。 - BP: 二阶(每侧每个八度 6 dB)带通滤波器。在应用此滤波器时，参数 Filter Q 不起作用。  Default value: LPF12 |
| Filter Cutoff | 滤波器截止频率。粒子滤波器的截止频率或中心频率，单位为 Hz。  Default value: 20000  Range: 20 to 20000  Units: Frequency |
| Filter Q | 滤波器 Q。粒子滤波器的品质因数。此值越大，滤波器在滤波器截止频率附近的振幅就越大。  Filter Q 仅在 Filter Type 设为 **LPF12**， **HPF12** 或 **BP** 时生效。  Default value: 0.707  Range: 0.1 to 100 |
| **定位** | |
| Channels | 定义是否将粒子空间化，使其匹配 Output Config 中指定的合成器输出声道配置，还是直接进行指派。  - Direct Speaker Assignment: 不应用空间化或声像摆位。若 Output Config 包含中置声道，则将单声道文件输出至中置声道，否则输出至左前和右前声道。通常，会将输入声道映射至相同的输出声道；若输出配置中不存在这些声道，则将弃用所述输入。 - 3D Spatialization: 使用 Azimuth、Elevation 和 Spread，将粒子 3D 空间化，适配合成器的输出配置。注意，Output Config 须包含多个声道，空间化才会起作用。  Default value: Direct Speaker Assignment |
| Azimuth | 方位角。粒子空间定位的方位角，单位为度，正值表示向右。  此控件需要将 Channels 设为 **3D Spatialization**，仅在合成器的 Output Config 设为多声道配置时有效。  Default value: 0  Range: -180 to 180 |
| Elevation | 高度角。粒子空间定位的高度角，单位为度，正值表示向上。  此控件需要将 Channels 设为 **3D Spatialization**，仅在合成器的 Output Config 设为多声道配置时有效。  Default value: 0  Range: -90 to 90 |
| Spread | 散布。空间化定位中使用的粒子散布，单位为百分比。此项相当于 Wwise 中的 Attenuation Spread。  此控件需要将 Channels 设为 **3D Spatialization**，仅在合成器的 Output Config 设为多声道配置时有效。  Default value: 0  Range: 0 to 100 |
| **Output** | |
| Output Config | 输出配置。合成器输出强制使用的声道配置。  利用多声道输出配置，可轻松创建 3D 环境声。为此，可将声音定位设为 3D，并将 Attenuation ShareSet 设为在近距离位置使用 Spread。在设计合成器时，请使用 **3D Spatialization** 并调制 Azimuth 和 Elevation (如适用)，以此将输出设为最大环绕程度。在捕获数据并播放声音时，Effect 的 VU Meter 中会显示声道配置。  |  |  | | --- | --- | | [备注] | 备注 | | Wwise 会根据声音的定位设置对合成器的输出信号进一步实施声像摆位或空间化。 |  |  |  | | --- | --- | | [备注] | 备注 | | 若在播放过程中更改输出配置，则新的配置到下次播放合成器时才会生效。 |  Default value: Mono |
| Output Level | 输出电平。应用于最终信号的电平。  Default value: 0  Range: -96 to 24  Units: dB |
| **VU Meter** | |
|  | A per channel peak meter, which meters the signal at the output of the synthesizer, and its channel configuration matches that which is set in the [Output](02-Source-Editor-Soundseed-Grain.md#output) group. 有关扬声器配置和声道的详细信息，请参阅[“了解总线配置”一节](../../../05-使用声音和振动来提升游戏体验/02-定义定位/11-了解总线配置.md "了解总线配置")。   信号电平为绿色，表明低于 -6 dB，黄色表明处于 -6 dB 至 0 dB 范围，红色表明高于 0 dB。 |
| **Envelope Visualizer** | |
|  | Envelope Visualizer（包络观察器）方便预览粒子包络的形状和重叠情况。重叠量取决于发射速率、粒子时长和释音时间。这些值尚未经过 RTPC 或调制，所以实际结果可能会有所不同。 |
| |  |  | | --- | --- | | [备注] | 备注 | | 以下各行是 Modulator 1 的属性说明。不过，所有四个 Modulator 同样适用。 | | |
| **Grain Modulators（左侧窗格）** | |
| Modulator 1 Waveform | 调制器 1 - 波形。Modulator 1 的波形类型。  可用波形类型包括：  - Sine: 双极正弦波 - Triangle: 双极三角波 - Square: 双极方波 - Saw up: 双极上锯齿波 - Saw down: 双极下锯齿波 - Random: 双极正弦波 - Sine+: 单极正弦波 - Triangle+: 单极三角波 - Square+: 单极方波 - Saw up+: 单极上锯齿波 - Saw down+: 单极下锯齿波 - Random+: 单极正弦波  Default value: Random |
| Modulator 1 Time/Freq | 指定如何定义振荡速率：时间(即周期，单位为 ms)或频率(Hz)。  Default value: Frequency |
| Modulator Period | 调制器 - 周期。Modulator 的周期，单位为 ms。  Default value: 1000  Range: 0.05 to 120000 |
| Modulator 1 Output | 调制器 1 - 输出。Modulator 1 的输出电平。在设为负值时，将反转调制器的极性。  Default value: 100  Range: -100 to 100 |
| **Modulator Assignment（右侧窗格）**  |  |  | | --- | --- | | [备注] | 备注 | | 以下各行描述了各种 Property 选择下的 Amount 和 Quantization 列。 | | |
| **Amount** | |
| Amplitude Modulation | 振幅 - 调制。应用于 Amplitude 的调制量。  调制量的单位为百分比，可高于或低于原始值(因所选调制器波形而异)。在设为负值时，将反转调制器的输出信号(即反转极性)。  |  |  | | --- | --- | | [备注] | 备注 | | 在采用双极调制器时，可降至 0 以下。比如，在设为 -50% 时，将按照原始电平的 50% 播放粒子，但会反转信号的极性。 |  Default value: 0  Range: 0 to 100 |
| Attack Modulation | 起音 - 调制。应用于 Attack 的调制量。  调制量的单位为八度，可高于或低于原始值(因所选调制器波形而异)。在上调一个八度时，会将起音时长减半；在下调一个八度时，会将起音时长加倍。在设为负值时，将反转调制器的输出信号(即反转极性)。  Default value: 0  Range: -10 to 10 |
| Azimuth Modulation | 方位角 - 调制。应用于 Azimuth 的调制量。  调制量的单位为度，可高于或低于原始值(因所选调制器波形而异)。在设为负值时，将反转调制器的输出信号(即反转极性)。  Default value: 0  Range: 0 to 180 |
| Duration Modulation | 时长 - 调制。应用于 Duration 的调制量。  调制量的单位为八度，可高于或低于原始值(因所选调制器波形而异)。在上调一个八度时，时长将会减半；在下调一个八度时，时长将会加倍。在设为负值时，将反转调制器的输出信号(即反转极性)。  Default value: 0  Range: -10 to 10 |
| Duration Multiplier Modulation | 时长倍数 - 调制。应用于 Duration Multiplier 的调制量。  调制量的单位为八度，可高于或低于原始值(因所选调制器波形而异)。在上调一个八度时，时长将会减半(即时长倍数减半)；在下调一个八度时，时长将会加倍。在设为负值时，将反转调制器的输出信号(即反转极性)。  Default value: 0  Range: -10 to 10 |
| Elevation Modulation | 高度角 - 调制。应用于 Elevation 的调制量。  调制量的单位为度，可高于或低于原始值(因所选调制器波形而异)。在设为负值时，将反转调制器的输出信号(即反转极性)。  Default value: 0  Range: 0 to 90.0 |
| Filter Cutoff Modulation | 滤波器截止频率 - 调制。应用于 Filter Cutoff 的调制量。  调制量的单位为八度，可高于或低于原始值(因所选调制器波形而异)。在设为负值时，将反转调制器的输出信号(即反转极性)。  Default value: 0  Range: -10 to 10 |
| Filter Modulation | 滤波器 Q - 调制。应用于 Filter Q 的调制量。  调制量表示为 Q 偏置，可高于或低于原始值(因所选调制器波形而异)。在设为负值时，将反转调制器的输出信号(即反转极性)。  Default value: 0  Range: 0 to 100 |
| Emissions per Second Modulation | 每秒发射个数 - 调制。应用于 Emissions per Second 的调制量。  调制量的单位为八度，可高于或低于原始值(因所选调制器波形而异)。在设为负值时，将反转调制器的输出信号(即反转极性)。  Default value: 0  Range: -10 to 10 |
| Time Between Emissions Modulation | 发射间隔 - 调制。应用于 Time Between Emissions 的调制量。  调制量的单位为八度，可高于或低于原始值(因所选调制器波形而异)。在上调一个八度时，时长将会减半；在下调一个八度时，时长将会加倍。在设为负值时，将反转调制器的输出信号(即反转极性)。  |  |  | | --- | --- | | [备注] | 备注 | | Time Between Emissions Mod 1 的值与 Emissions Per Second Mod 1 相同。换句话说，若将 Select Freq/Time 设为 **Frequency**，则相同的值会产生等量的调制。 |  Default value: 0  Range: -10 to 10 |
| Position Modulation | 位置 - 调制。应用于 Position 的调制量。  调制量表示为文件时长的百分比，可高于或低于原始值(因所选调制器波形而异)。在设为负值时，将反转调制器的输出信号(即反转极性)。  Default value: 0  Range: 0 to 100 |
| Offset Modulation | 偏置 - 调制。应用于 Offset 的调制量。  调制量表示为文件时长的百分比，可高于或低于原始值(因所选调制器波形而异)。在设为负值时，将反转调制器的输出信号(即反转极性)。  Default value: 0  Range: 0 to 100 |
| Release Modulation | 释音 - 调制。应用于 Release 的调制量。  调制量的单位为八度，可高于或低于原始值(因所选调制器波形而异)。在上调一个八度时，会将释音时长减半；在下调一个八度时，会将释音时长加倍。在设为负值时，将反转调制器的输出信号(即反转极性)。  Default value: 0  Range: -10 to 10 |
| Speed Modulation | 速度 - 调制。应用于 Speed 的调制量。  调制量表示为速度偏置，可高于或低于原始值(因所选调制器波形而异)。在设为负值时，将反转调制器的输出信号(即反转极性)。  Default value: 0  Range: 0 to 4 |
| Spread Modulation | 散布 - 调制。应用于 Spread 的调制量。  调制量表示为偏置，可高于或低于原始值(因所选调制器波形而异)。在设为负值时，将反转调制器的输出信号(即反转极性)。  Default value: 0  Range: 0 to 100 |
| Pitch Modulation | 音高 - 调制。应用于 Pitch 的调制量。  调制量的单位为音分，可高于或低于原始值(因所选调制器波形而异)。在设为负值时，将反转调制器的输出信号(即反转极性)。  Default value: 0  Range: 0 to 4800 |
| **Quantization（量化）** | |
| Amplitude Quantization | 应用于 **Amplitude** 的调制量化。  此属性值可用的量化方案包括:  - None: 无量化。 - (-1, 1): 量化至调制器波形的顶部和底部。 - (-1, 0, 1): 量化至调制器波形的顶部、中间和底部。Middle 仅适用于双极波形，对应基准 **Amplitude** 值。  Default value: None |
| Attack Quantization | 应用于 Attack 的调制量化。  此属性值可用的量化方案包括:  - None: 无量化。 - (-1, 1): 量化至调制器波形的顶部和底部。 - (-1, 0, 1): 量化至调制器波形的顶部、中间和底部。Middle 仅适用于双极波形，对应基准 **Attack** 值。 - Chromatic: 仅允许量化为半音(1/12 个八度)。比如，若将调制量设为 0.5 个八度，则允许在基准 Attack 时长的基础上调制 {-6、-5、-4、-3、-2、-1、0、1、2、3、4、5、6} 个半音(参见下方备注)。 - Major: 仅允许量化为大调音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Attack 时长的基础上调制 {-5、-3、-1、0、2、4、5} 个半音(参见下方备注)。 - Minor: 仅允许量化为小调音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Attack 时长的基础上调制 {-5、-4、-2、0、2、3、5} 个半音(参见下方备注)。 - Pentatonic: 仅允许量化为五声音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Attack 时长的基础上调制 {-5、-2、0、3、5} 个半音(参见下方备注)。  |  |  | | --- | --- | | [备注] | 备注 | | 在此，下调一个八度相当于将时间拉长 2 倍。同样地，下调一个半音相当于将时间拉长 2 开 12 次方倍(1.059 倍)。 |  Default value: None |
| Azimuth Quantization | 应用于 Azimuth 的调制量化。  此属性值可用的量化方案包括:  - None: 无量化。 - (-1, 1): 量化至调制器波形的顶部和底部。 - (-1, 0, 1): 量化至调制器波形的顶部、中间和底部。Middle 仅适用于双极波形，对应基准 Azimuth 值。  Default value: None |
| Duration Quantization | 应用于 Duration 的调制量化。  此属性值可用的量化方案包括:  - None: 无量化。 - (-1, 1): 量化至调制器波形的顶部和底部。 - (-1, 0, 1): 量化至调制器波形的顶部、中间和底部。Middle 仅适用于双极波形，对应基准 Duration 值。 - Chromatic: 仅允许量化为半音(1/12 个八度)。比如，若将调制量设为 0.5 个八度，则允许在基准 Duration 的基础上调制 {-6、-5、-4、-3、-2、-1、0、1、2、3、4、5、6} 个半音(参见下方备注)。 - Major: 仅允许量化为大调音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Duration 的基础上调制 {-5、-3、-1、0、2、4、5} 个半音(参见下方备注)。 - Minor: 仅允许量化为小调音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Duration 的基础上调制 {-5、-4、-2、0、2、3、5} 个半音(参见下方备注)。 - Pentatonic: 仅允许量化为五声音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Duration 的基础上调制 {-5、-2、0、3、5 } 个半音(参见下方备注)。  |  |  | | --- | --- | | [备注] | 备注 | | 下调一个八度相当于将时间拉长 2 倍。同样地，下调一个半音相当于将时间拉长 2 开 12 次方倍(1.059 倍)。 |  Default value: None |
| Duration Multiplier Quantization | 应用于 Duration Multiplier 的调制量化。  此属性值可用的量化方案包括:  - None: 无量化。 - (-1, 1): 量化至调制器波形的顶部和底部。 - (-1, 0, 1): 量化至调制器波形的顶部、中间和底部。Middle 仅适用于双极波形，对应基准 **Duration Multiplier** 值。  Default value: None |
| Elevation Quantization | 应用于 Elevation 的调制量化。  此属性值可用的量化方案包括:  - None: 无量化。 - (-1, 1): 量化至调制器波形的顶部和底部。 - (-1, 0, 1): 量化至调制器波形的顶部、中间和底部。Middle 仅适用于双极波形，对应基准 Elevation 值。  Default value: None |
| Filter Cutoff Quantization | 应用于 Filter Cutoff 的调制量化。  此属性值可用的量化方案包括:  - None: 无量化。 - (-1, 1): 量化至调制器波形的顶部和底部。 - (-1, 0, 1): 量化至调制器波形的顶部、中间和底部。Middle 仅适用于双极波形，对应基准 Filter Cutoff 值。 - Chromatic: 仅允许量化为半音(1/12 个八度)。比如，若将调制量设为 0.5 个八度，则允许在基准 Filter Cutoff 频率的基础上调制 {-6、-5、-4、-3、-2、-1、0、1、2、3、4、5、6} 个半音。 - Major: 仅允许量化为大调音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Filter Cutoff 频率的基础上调制 {-5、-3、-1、0、2、4、5} 个半音。 - Minor: 仅允许量化为小调音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Filter Cutoff 频率的基础上调制 {-5、-4、-2、0、2、3、5} 个半音。 - Pentatonic: 仅允许量化为五声音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Filter Cutoff 频率的基础上调制 {-5、-2、0、3、5 } 个半音。  Default value: None |
| Filter Quantization | 应用于 Filter Q 的调制量化。  此属性值可用的量化方案包括:  - None: 无量化。 - (-1, 1): 量化至调制器波形的顶部和底部。 - (-1, 0, 1): 量化至调制器波形的顶部、中间和底部。Middle 仅适用于双极波形，对应基准 Filter Q 值。  Default value: None |
| Emissions per Second Quantization | 应用于 Emissions per Second 的调制量化。  此属性值可用的量化方案包括:  - None: 无量化。 - (-1, 1): 量化至调制器波形的顶部和底部。 - (-1, 0, 1): 量化至调制器波形的顶部、中间和底部。Middle 仅适用于双极波形，对应基准 Emissions per Second 值。 - Chromatic: 仅允许量化为半音(1/12 个八度)。比如，若将调制量设为 0.5 个八度，则允许在基准 Emissions per Second 频率的基础上调制 {-6、-5、-4、-3、-2、-1、0、1、2、3、4、5、6} 个半音。 - Major: 仅允许量化为大调音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Emissions per Second 频率的基础上调制 {-5、-3、-1、0、2、4、5} 个半音。 - Minor: 仅允许量化为小调音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Emissions per Second 频率的基础上调制 {-5、-4、-2、0、2、3、5} 个半音。 - Pentatonic: 仅允许量化为五声音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Emissions per Second 频率的基础上调制 {-5、-2、0、3、5 } 个半音。  Default value: None |
| Time Between Emissions Quantization | 应用于 Time Between Emissions 的调制量化。  此属性值可用的量化方案包括:  - None: 无量化。 - (-1, 1): 量化至调制器波形的顶部和底部。 - (-1, 0, 1): 量化至调制器波形的顶部、中间和底部。Middle 仅适用于双极波形，对应基准 Time Between Emissions 值。 - Chromatic: 仅允许量化为半音(1/12 个八度)。比如，若将调制量设为 0.5 个八度，则允许在基准 Time Between Emissions 时长的基础上调制 {-6、-5、-4、-3、-2、-1、0、1、2、3、4、5、6} 个半音(参见下方备注)。 - Major: 仅允许量化为大调音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Time Between Emissions 时长的基础上调制 {-5、-3、-1、0、2、4、5} 个半音(参见下方备注)。 - Minor: 仅允许量化为小调音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Time Between Emissions 时长的基础上调制 {-5、-4、-2、0、2、3、5} 个半音(参见下方备注)。 - Pentatonic: 仅允许量化为五声音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Time Between Emissions 时长的基础上调制 {-5、-2、0、3、5} 个半音(参见下方备注)。  |  |  | | --- | --- | | [备注] | 备注 | | Time Between Emissions 调制等同于 Emissions per Second 调制。因此，相同的调制值会产生一样的行为。在此，下调一个八度相当于将时间拉长 2 倍。同样地，下调一个半音相当于将时间拉长 2 开 12 次方倍(1.059 倍)。 |  Default value: None |
| Position Quantization | 应用于 Position 的调制量化。  此属性值可用的量化方案包括:  - None: 无量化。 - (-1, 1): 量化至调制器波形的顶部和底部。 - (-1, 0, 1): 量化至调制器波形的顶部、中间和底部。Middle 仅适用于双极波形，对应基准 Position 值。  Default value: None |
| Offset Quantization | 应用于 Offset 的调制量化。  此属性值可用的量化方案包括:  - None: 无量化。 - (-1, 1): 量化至调制器波形的顶部和底部。 - (-1, 0, 1): 量化至调制器波形的顶部、中间和底部。Middle 仅适用于双极波形，对应基准 Offset 值。  Default value: None |
| Release Quantization | 应用于 Release 的调制量化。  此属性值可用的量化方案包括:  - None: 无量化。 - (-1, 1): 量化至调制器波形的顶部和底部。 - (-1, 0, 1): 量化至调制器波形的顶部、中间和底部。Middle 仅适用于双极波形，对应基准 Release 值。 - Chromatic: 仅允许量化为半音(1/12 个八度)。比如，若将调制量设为 0.5 个八度，则允许在基准 Release 时长的基础上调制 {-6、-5、-4、-3、-2、-1、0、1、2、3、4、5、6} 个半音(参见下方备注)。 - Major: 仅允许量化为大调音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Release 时长的基础上调制 {-5、-3、-1、0、2、4、5} 个半音(参见下方备注)。 - Minor: 仅允许量化为小调音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Release 时长的基础上调制 {-5、-4、-2、0、2、3、5} 个半音(参见下方备注)。 - Pentatonic: 仅允许量化为五声音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Release 时长的基础上调制 {-5、-2、0、3、5} 个半音(参见下方备注)。  |  |  | | --- | --- | | [备注] | 备注 | | 在此，下调一个八度相当于将时间拉长 2 倍。同样地，下调一个半音相当于将时间拉长 2 开 12 次方倍(1.059 倍)。 |  Default value: None |
| Speed Quantization | 应用于 Speed 的调制量化。  此属性值可用的量化方案包括:  - None: 无量化。 - (-1, 1): 量化至调制器波形的顶部和底部。 - (-1, 0, 1): 量化至调制器波形的顶部、中间和底部。Middle 仅适用于双极波形，对应基准 Speed 值。  Default value: None |
| Spread Quantization | 应用于 Spread 的调制量化。  此属性值可用的量化方案包括:  - None: 无量化。 - (-1, 1): 量化至调制器波形的顶部和底部。 - (-1, 0, 1): 量化至调制器波形的顶部、中间和底部。Middle 仅适用于双极波形，对应基准 Spread 值。  Default value: None |
| Pitch Quantization | 应用于 Pitch 的调制量化。  此属性值可用的量化方案包括:  - None: 无量化。 - (-1, 1): 量化至调制器波形的顶部和底部。 - (-1, 0, 1): 量化至调制器波形的顶部、中间和底部。Middle 仅适用于双极波形，对应基准 Pitch 值。 - Chromatic: 仅允许量化为半音(1/12 个八度)。比如，若将调制量设为 0.5 个八度，则允许在基准 Pitch 的基础上调制 {-6、-5、-4、-3、-2、-1、0、1、2、3、4、5、6} 个半音。 - Major: 仅允许量化为大调音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Pitch 的基础上调制 {-5、-3、-1、0、2、4、5} 个半音。 - Minor: 仅允许量化为小调音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Pitch 的基础上调制 {-5、-4、-2、0、2、3、5} 个半音。 - Pentatonic: 仅允许量化为五声音阶的音程。比如，若将调制量设为 0.5 个八度，则允许在基准 Pitch 的基础上调制 {-5、-2、0、3、5 } 个半音。  Default value: None |

#### Source settings

此插件可同时用来管理媒体，所以 Source Editor 中另外设置了两个选项卡：

**Source tab**

在 Source（源）选项卡中，可以看到熟悉的 Wwise [Source Editor](../../../09-参考主题/04-Project-Explorer/01-Audio-tab/06-Source-Editor：音频源.md "Source Editor：音频源") 界面，其中的侧面板显示了 Soundseed Grain 特定属性。在此，可编辑 Trim（修剪）、Fade（淡变）和 Marker（标记），就像在 Wwise 中编辑标准源一样。注意，此处所做全部更改均会保存为“前期效果”。也就是说，它会影响存入 SoundBank（音频包）之前的媒体。因此，假如更改了 Trim，那么在运行时插件使用的源文件将会是修剪后的文件。

|  |  |
| --- | --- |
| [注意] | 注意 |
| Moving the Trim cursors changes the meaning of the Position setting, since it depends on the audio file's duration. |

在 Source 选项卡中，可添加和编辑标记。若要查看完整的源文件标记列表，请单击 **Edit Markers in List View**（在列表视图中打开标记）。

  

在 Effect Settings 选项卡中，选中 **Snap to markers**，将有效的粒子开始位置设到最近的标记。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若存在标记，则在源音频文件坐标图的 Effect Settings 选项卡中显示为蓝色竖线。 |

  

**Conversion tab**

在 Conversion（转码）选项卡中，可选择专门用于该插件的 Conversion ShareSet，以便在将媒体存入 SoundBank 之前进行编码。Soundseed Grain 支持所有声道下混和采样率选项，不过仅限于 PCM、ADPCM 和 Vorbis 编解码器。

|  |  |
| --- | --- |
| [警告] | 警告 |
| 目前，Soundseed Grain 仅支持在运行时解码 PCM、ADPCM 和 Vorbis 文件。若在 Conversion 选项卡中为 Soundseed Grain Sound SFX（音效）选择其他编解码器（如 Opus），则会导致其无法播放，并且 [“Capture Log”一节](../../../09-参考主题/06-Profiler-视图/01-Capture-Log/00-Capture-Log.md "Capture Log") 中也会显示错误消息。 |

  

|  |  |
| --- | --- |
| [备注] | 备注 |
| 请不要将 ADPCM 用于每声道帧数小于 64 的文件。 |

|  |  |
| --- | --- |
| [备注] | 备注 |
| 需要使用寻址表来解码 Vorbis 文件。对于长度短于最小寻址表大小（每声道 1,024 个采样）的文件，请勿使用 Vorbis 格式。 |

为此，您可以选择其他编解码器，然后让游戏在将 SoundBank 加载到内存中时执行解码。有关 Decode Bank 流程的更多详细信息，请参阅 SDK 文档中的 [`AK::SoundEngine::DecodeBank`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a2d99e91099dba3eae8b2c67f9582bc01.html)。

---