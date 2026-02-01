# Invalid file header.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Invalid file header.

#### Invalid file header.

文件头无效。流播放文件无法解码，因为文件头已损坏或它不是支持的文件类型。涉及的声音会显示在此错误报告中。

**可能的原因：**

- 文件损坏。
- 转码文件时所用 Wwise 版本有误。
- AkExternalSource 使用了非 WEM 格式的文件。

**推荐的解决步骤：**

- 重新转码并重新复制文件。
- 使用与游戏中所用 Sound Engine（声音引擎）匹配的 Wwise 版本。
- 针对 AkExternalSource 使用 WEM 文件。
- 将原始文件和转码后文件发送给 Audiokinetic 技术支持部门以供分析。

---