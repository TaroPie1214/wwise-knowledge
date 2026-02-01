# Transition not sample-accurate due to incompatible encoding parameters.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Transition not sample-accurate due to incompatible encoding parameters.

#### Transition not sample-accurate due to incompatible encoding parameters.

“因不兼容编码参数导致过渡无法精确到采样点”。若两个声音采用相同的音频格式和不同的编码参数，并设为在精确到采样点的过渡中顺序播放，则将出现此错误。有些启用了硬件加速的编解码器需要声音采用完全相同的编码参数才能执行精确到采样点的过渡。在 Random/Sequence Container（随机/序列容器）、Interactive Music（互动音乐）中或在代码中使用 Dynamic Sequence（动态序列）机制时，可能存在此类过渡。

**推荐的解决步骤：**

- 确认所涉及的声音，并通过更改 Conversion Settings（转码设置）来使所有编码参数保持一致。

---