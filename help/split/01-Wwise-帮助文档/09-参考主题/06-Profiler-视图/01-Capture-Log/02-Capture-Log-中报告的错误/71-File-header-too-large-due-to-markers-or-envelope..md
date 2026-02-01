# File header too large due to markers or envelope.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > File header too large due to markers or envelope.

#### File header too large due to markers or envelope.

“标记点或包络导致文件头过大。”无法启动当前播放的文件，因为解析标记点或音量包络数据（用于 HDR 处理）需要太多内存或超出文件格式头限制。在这种情况下，无法读取文件。

**可能的原因：**

- 在 Source 选项中启用了瞬态自动标记功能。若阈值太精细，可能会生成太多标记点。
- 在生成包络时采用了精细的阈值，导致生成了太多包络控制点。
- 原始文件包含太多标记点。
- 原始文件包含大的数据标记点。这种情况常见于包含用来对口型的动画数据的文件。

**推荐的解决步骤：**

- 在 Wwise 的 Source Editor（源编辑器）中，更改自动标记选项。然后，重新生成并重新部署 SoundBank（音频包）。
- 移除来自源文件的无用标记点。
- 在 Wwise 的 Source Editor（源编辑器）中，更改自动包络分析选项。然后，重新生成并重新部署 SoundBank（音频包）。

---