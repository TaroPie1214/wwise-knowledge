# Maximum number of hardware-accelerated voices reached. Voice will not play.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Maximum number of hardware-accelerated voices reached. Voice will not play.

#### Maximum number of hardware-accelerated voices reached. Voice will not play.

“硬件加速声部达到最大数量。将不会播放声部”。同时播放了太多使用了硬件加速音频格式的声部。

**可能的原因：**

- “启用了硬件加速的声部达到最大数量。将不会播放声部”。同时播放了太多采用硬件加速的音频格式的声部。有些音频格式可能会自动选择在特定平台上使用硬件加速。
- 您使用了大量启用了硬件加速的多声道声音。在有些平台上，声道数量允许超出限值。比如，同时解码的单声道/立体声音频源可以多于 5.1 或 7.1 音频源。
- 虚声部阈值设得太低。

**推荐的解决步骤：**

- 针对有些声音使用不同的转码设置。请参阅章节来了解对不同平台和用例来说哪种转码设置效果最佳。
- 限制最多允许同时播放多少个采用硬件加速的音频格式的声音。
- 针对启用了硬件加速的声音使用单声道或立体声音频源。
- 将虚声部阈值设得高一些。

---