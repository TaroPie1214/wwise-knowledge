# Plug-in media unavailable.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Plug-in media unavailable.

#### Plug-in media unavailable.

“插件媒体不可用”。此错误表示需要附加媒体来运行所列插件（源、效果器、混音器或 sink），但未加载或未找到媒体。此为 AK Convolution Reverb 常见错误，但其他第三方插件也可能发生。

**可能的原因：**

- 未在 SoundBank（音频包）中包含媒体。
- 未加载包含媒体的 SoundBank。
- 在将媒体添加到工程中之后，没有重新生成并重新部署包含媒体的 SoundBank。

**推荐的解决步骤：**

- 在 SoundBank 内容编辑器中，确认媒体包含在音频包中。若不包含，请将总线或 ShareSet（共享集）拖放到音频包上。
- 在 Wwise Advanced Profiler（高级性能分析器）中，确认已成功加载 SoundBank（SoundBanks 或 Voices Graph 选项卡中）。若未成功加载，请查看 Capture Log（捕获日志）中的错误，并调查 SoundBank 错误。
- 在主机上重新生成并重新部署 SoundBank。

---