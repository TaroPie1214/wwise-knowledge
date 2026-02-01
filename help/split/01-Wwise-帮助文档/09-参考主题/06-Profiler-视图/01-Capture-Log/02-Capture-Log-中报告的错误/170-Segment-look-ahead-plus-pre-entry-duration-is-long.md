# Segment look-ahead plus pre-entry duration is longer than previous segment in sequence.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Segment look-ahead plus pre-entry duration is longer than previous segment in sequence.

#### Segment look-ahead plus pre-entry duration is longer than previous segment in sequence.

This error occurs when the look-ahead setting cannot be honored by the Interactive
Music system. This can result in music desynchronization.

**可能的原因：**

- 某一流播放片段的时长（含前导段）小于指定预读时间。

**推荐的解决步骤：**

- 更改片段的时长。
- 更改预读时间。请参阅 [“定义 Music Track 的播放行为”一节](../../../../06-创建互动音乐/04-使用-Music-Track-和-Music-Segment/01-定义-Music-Track-的播放行为.md "定义 Music Track 的播放行为")。
- 将片段放入 SoundBank（而非进行流播放）。请参阅 [*管理 SoundBank*](../../../../07-完善工程/07-管理-SoundBank/00-管理-SoundBank.md "管理 SoundBank")。

---