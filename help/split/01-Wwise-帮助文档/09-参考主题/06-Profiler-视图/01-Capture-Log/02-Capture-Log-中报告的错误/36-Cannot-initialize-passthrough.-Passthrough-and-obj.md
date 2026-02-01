# Cannot initialize passthrough. Passthrough and objects will be disabled.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Cannot initialize passthrough. Passthrough and objects will be disabled.

#### Cannot initialize passthrough. Passthrough and objects will be disabled.

“无法初始化直通属性。将禁用直通属性及相应对象。”若无法初始化 3D 对象处理器，则可能会出现此错误。在这种情况下，将改为在 Main Mix（主混音）中对对象的音频实施混音。

**可能的原因：**

- 3D Audio 处理库或硬件被另一进程占用（通常为 Unreal 或 Unity）。

**推荐的解决步骤：**

- 确保禁用 Unreal 或 Unity 的音频系统。

---