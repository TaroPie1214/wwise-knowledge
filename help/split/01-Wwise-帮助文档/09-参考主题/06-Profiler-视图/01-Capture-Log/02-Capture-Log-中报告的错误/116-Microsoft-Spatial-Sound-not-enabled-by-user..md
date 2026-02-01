# Microsoft Spatial Sound not enabled by user.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Microsoft Spatial Sound not enabled by user.

#### Microsoft Spatial Sound not enabled by user.

“用户未启用 Microsoft Spatial Sound。”若声音引擎被初始化为了使用 3D Audio Object（3D 音频对象），但却禁用了 Windows Sound Setting **Spatial Sound**，则将报告此错误。在这种情况下，将把所有 Audio Object 下混到音频 Bed。

此项只是信息性消息。这时仍可继续游戏，但声音不会是 3D 的。

**推荐的解决步骤：**

- 在 Windows Sound Settings 菜单中，选择 **Spatial Sound (Off)** 来切换 Spatial Sound 的使用状态。

---