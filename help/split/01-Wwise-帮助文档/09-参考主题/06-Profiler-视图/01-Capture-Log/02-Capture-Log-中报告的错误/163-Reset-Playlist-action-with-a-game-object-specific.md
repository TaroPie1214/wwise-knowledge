# Reset Playlist action with a game object specific scope is ignored on a global container.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Reset Playlist action with a game object specific scope is ignored on a global container.

#### Reset Playlist action with a game object specific scope is ignored on a global container.

“全局容器上游戏对象作用域的‘重置播放列表’动作不起作用。”Sequence Container（序列容器）或 Random Container（随机容器）的播放列表始终特定于游戏对象。因此，若容器设置了 Reset Playlist 动作而其 Scope 属性设为了 Global，则发送相应 Event 不起任何作用。

**推荐的解决步骤：**

- 从 Event（事件）移除 Reset Playlist（重置播放列表）动作。
- 将容器的 Scope（作用域）属性改为 Game Object（游戏对象）。

---