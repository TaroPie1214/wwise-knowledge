# Bank Load Failed.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Bank Load Failed.

#### Bank Load Failed.

“音频包加载失败”。此为一般性错误消息，表示 SoundBank（音频包）加载失败。SoundBank 的任何内容都无法播放。

**可能的原因：**

- 找不到 SoundBank 文件（在此之前应会出现 File Not Found 错误）。
- SoundBank 由其它版本的 Wwise 生成（在此之前应会出现 Wrong Bank Version 错误）。此错误会声明 SoundBank 和 SDK 版本。
- SoundBank 文件损坏。
- 在加载 SoundBank 时，出现 I/O 错误。

**推荐的解决步骤：**

- 若使用 Wwise 中提供的默认 I/O 代码，请确认 SetBasePath 或 AddBasePath 调用指向正确的目录。
- 确保使用合适版本的 Wwise 正确地生成 SoundBank。
- 若使用 Unity 或 Unreal，请确保将 Unity 或 Unreal 内的 Wwise Integration 更新至与设计工具相同的版本。
- 确保正确地生成 SoundBank 并将其部署到目标上。
- 若使用自定义 I/O 挂钩，请调试自定义 I/O 挂钩代码。

---