# Music system is stopped because a music playlist is modified.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Music system is stopped because a music playlist is modified.

#### Music system is stopped because a music playlist is modified.

“因音乐播放列表修改，导致音乐系统停止。”在播放过程中修改 Music Playlist（音乐播放列表）或容器时，将发生此错误。此错误通常在 Wwise 与游戏相连时出现。

**可能的原因：**

- 在播放过程中修改了音乐结构。
- 游戏音乐结构与 Wwise 工程中的音乐结构不同（旧内容）。

**推荐的解决步骤：**

- 重新生成并重新部署音乐 SoundBank。

---