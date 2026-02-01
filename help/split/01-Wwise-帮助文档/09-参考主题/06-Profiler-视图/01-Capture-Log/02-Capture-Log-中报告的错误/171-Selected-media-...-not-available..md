# Selected media ... not available.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Selected media ... not available.

#### Selected media ... not available.

“所选媒体…不可用。”选择了要播放的声音，但没有加载对应媒体。该声音和媒体文件的 ID 会显示在同一行中。

**可能的原因：**

- 声音结构和声音媒体在两个不同的 SoundBank 中，但只加载了结构。
- 声音结构和声音媒体在两个不同的 SoundBank 中，在更改媒体文件后没有使用相同的内容生成两者。
- 从旧的构建版本加载了有些 SoundBank，其包含过期数据。

**推荐的解决步骤：**

- 找到并确保提前加载包含所需媒体文件的 SoundBank（音频包）。
- 确保通过重新生成来更新 SoundBank（音频包）。
- 确保在测试主机上正确部署所有 SoundBank（音频包）。

---