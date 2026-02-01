# Taking a closer look at the FutzBox Lo-Fi Distortion Effect plug-in

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [合作伙伴插件](../00-合作伙伴插件.md) > [McDSP FutzBox Lo-Fi Distortion 插件](00-McDSP-FutzBox-Lo-Fi-Distortion-插件.md) > Taking a closer look at the FutzBox Lo-Fi Distortion Effect plug-in

## Taking a closer look at the FutzBox Lo-Fi Distortion Effect plug-in

### Separating noise and audio signals

正如上一节中所述，音频信号和噪声源具有单独的一套滤波设置。它主要用于将音频与噪声分开，以便两个信号彼此减少竞争。例如在使用高通滤波器时，可将噪声限制在 10 kHz 以上的频率。然后便可对经过修改或失真处理的音频进行滤波和均衡，消除超过 10 kHz 频率的主要内容（对于普通对白并不难，不过您明白意思就行）。

注意，SIM 声音特质会应用于整个失真信号，以使传入音频和噪声发生器输出得到进一步处理后听上去来自于同一个源。比如，次品收音机中的背景噪声一般与其总体输出音频具有大致相同的声音特质。

### SIM tuning

合成冲激模型（SIM）是实际冲激响应的有效模拟。此外，它们没有内部延迟，可实时操控。位于 SIM 控件模块的 Tuning（调谐）控件可调整各个 SIM 的各种参数来获得各种声音结果。各个 SIM 具有一组各自的调谐参数。

使用 SIM 调谐控件可调节给定 SIM 以更好地适应特定应用。许多 SIM 在调谐控件扫过整个范围时将形成有趣的相位效应。此效果对于自动化可能非常有用 – 声音体验在播放期间始终一致，且运动效果能让失真更加逼真。

### Audio signal EQ using resonant filters

FutzBox 音频处理的第一阶段是高通和低通滤波器。这些滤波器包括可控共振（滤波器 Q）。最大提升大约为 24 dB。这些峰值对于强调信号频谱的部分频段非常有效。

### Dialogue and vocal distortion

使用 FutzBox 可实现各种失真效果。有关创建适宜的失真对白和人声音轨的一些常用技巧包括：

- 使用高通音频滤波器衰减音频的低端。
- 在各种失真模式下单独或同时试听 Distortion Amount 和 Rectify 控制。
- 使用 EQ 为失真音频增添“临场感”。
- 在 SIM Preset 接近所需设置时，使用 SIM 分区的 Scale 控件体验一下效果。

最后，请勿忘记使用 Output 控件对修改版音频和原始音频的电平进行平衡。这样失真音频和原始音频之间的过渡会显得更加平滑。

### Creating low fidelity version of music

如果想让制作的音乐听上去像是在老式电子管收音机中播放一样，则 FutzBox 非常适合产生此类效果。进一步来说，如果音乐应该具有时代感（如 1940 年代的管弦乐），则谨慎使用 FutzBox 有利于使原始数字录音尽可能地复古。

在音乐制作中使用音频/鼓循环是常见做法，而 FutzBox 非常适合操控此类音频源。如果两小节强节奏需要一些额外的冲击力，FutzBox 则可提供各种各样的声音。

### Signal dropout effects

当任何门限设置过于激进（阈值过高，起音时间、时长和释音时间太短）时，可能会导致输入音频无法通过输出。FutzBox 门限特别适合此类应用。Attack、Hold 和 Release 控件的范围可能导致获得较差的门限设置。当结合 FutzBox 中的其它效果器使用时，可逼真地模拟许多通信设备中常见的信号丢包效果。

---