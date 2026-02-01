# Seeking after end of file. Playback will stop.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Seeking after end of file. Playback will stop.

#### Seeking after end of file. Playback will stop.

“在文件结束后寻址。将停止播放。”在使用 [`AK::SoundEngine::SeekOnEvent`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a602a2d51d394c55e1896d3ffa521adff.html) 且 SeekPercent 参数高于 100% 或 Position 参数大于声音文件长度时，可能会出现此错误。

**推荐的解决步骤：**

- 确认 [`AK::SoundEngine::SeekOnEvent`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a602a2d51d394c55e1896d3ffa521adff.html) 函数的参数。若在 [Profiler Settings](../../../01-工程/10-Profiler-Settings.md "Profiler Settings")（性能分析器设置）中启用了 **API Calls**（API 调用），则可在 Capture Log（捕获日志）中此错误附近查找哪些调用参数出现了问题。
- 确认声音文件的长度。错误行应会指向有问题的声音，直接双击 Wwise Object（Wwise 对象）列即可转至 Sound（声音）部分。

**另请参阅：**

- [`AK::SoundEngine::SeekOnEvent`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a602a2d51d394c55e1896d3ffa521adff.html)

---