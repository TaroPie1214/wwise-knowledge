# Rescheduling music clips because a track was modified.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Rescheduling music clips because a track was modified.

#### Rescheduling music clips because a track was modified.

“因音轨修改而无法重新安排音乐片段”。在播放过程中修改音轨时，将出现此错误。通常在 Wwise 与游戏相连时出现。这会导致音序器重新安排片段，并造成音乐不同步。

**可能的原因：**

- 在播放过程中修改了音乐结构。
- 游戏音乐结构与 Wwise 工程中的音乐结构不同（旧内容）。

**推荐的解决步骤：**

- 重新生成并重新部署音乐 SoundBank。

---