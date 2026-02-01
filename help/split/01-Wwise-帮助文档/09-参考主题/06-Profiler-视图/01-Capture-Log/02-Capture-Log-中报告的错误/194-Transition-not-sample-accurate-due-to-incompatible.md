# Transition not sample-accurate due to incompatible audio formats.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Transition not sample-accurate due to incompatible audio formats.

#### Transition not sample-accurate due to incompatible audio formats.

“因不兼容音频格式导致过渡无法精确到采样点”。若两个声音采用不同的音频格式，并设为在精确到采样点的过渡中顺序播放，则将出现此错误。有些启用了硬件加速的编解码器依赖于硬件来执行精确到采样点的过渡；因此，过渡中的所有声音需要使用相同的硬件。在 Random/Sequence Container（随机/序列容器）、Interactive Music（互动音乐）中或在代码中使用 Dynamic Sequence（动态序列）机制时，可能存在此类过渡。

**推荐的解决步骤：**

- 确认所涉及的声音，并通过更改 Conversion Settings（转码设置）将其设为相同的音频格式。

---