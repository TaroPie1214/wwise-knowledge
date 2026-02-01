# Not a valid Switch value ... in group ...

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Not a valid Switch value ... in group ...

#### Not a valid Switch value ... in group ...

“分组…中的切换开关值…无效。”表示 Switch Container 已触发播放但无法播放任何声音。

**可能的原因：**

- 在工程中， **Assigned Objects**（指派的对象）窗口中的 Switch Container（切换开关容器）内没有与 Switch Value 关联的声音。
- 在工程中，Switch Container 的属性中没有定义 Default Switch/State（默认切换开关/状态），或者未针对游戏中的 Game Object（游戏对象）设置 Switch Value。
- 在游戏中，在Game Object（游戏对象）上设置了 Switch Value，但 Assigned Objects（指派的对象）分区中没有任何与之关联的 Assigned Object。

---