# Transition not sample-accurate, the new source is shorter than two audio frames. Use a software codec to support this case.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Transition not sample-accurate, the new source is shorter than two audio frames. Use a software codec to support this case.

#### Transition not sample-accurate, the new source is shorter than two audio frames. Use a software codec to support this case.

“过渡无法精确到采样点，新的源短于两个音频帧。使用软件编解码器来提供相应支持。”若 Sequence Container（序列容器）或 Random Container（随机容器）在两个声音之间设置了精确到采样点的过渡，但因第二个声音太短导致硬件解码器无法正确加以处理，则将出现此错误。短的声音是指其短于两个音频帧。音频帧的长度在声音引擎初始化时由 [`AkInitSettings.uNumSamplesPerFrame`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_init_settings_a2438a18ece872c83175f70d7f70d659b.html) 的值定义。该值通常为 512 或 1024 个采样（10 ms 或 21.1 ms）。

**推荐的解决步骤：**

- 为两个声音使用软件编解码器（Vorbis、ADPCM 或 PCM）。
- 确保精确到采样点的过渡中涉及的所有声音均长于两帧。
- 在 Sequence Container（序列容器）或 Random Container（随机容器）中使用别的过渡类型。

---