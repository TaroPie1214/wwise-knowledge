# Reset Playlist action on a continuous container is ignored.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Reset Playlist action on a continuous container is ignored.

#### Reset Playlist action on a continuous container is ignored.

“连续容器上设置的‘重置播放列表’动作不起作用。”将 Sequence Container（序列容器）或 Random Container（随机容器）设为了连续播放，但无法在播放时修改播放列表。

**推荐的解决步骤：**

- 从 Event（事件）移除 Reset Playlist（重置播放列表）动作。
- 停止播放容器，接着重置播放列表，然后重新开始播放容器。

---