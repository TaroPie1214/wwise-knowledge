# No marker in file; seeking to specified location.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > No marker in file; seeking to specified location.

#### No marker in file; seeking to specified location.

“文件中无标记；寻址到指定位置”。已请求在声音中寻址并对齐至标记。但文件中并无标记。在使用  [`AK::SoundEngine::SeekOnEvent`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a602a2d51d394c55e1896d3ffa521adff.html) 时，可能会出现此问题。受此影响的声音将显示在 Wwise Object（Wwise 对象）列中。将寻址到函数调用中指定的时间，而非按要求对齐至标记。

**推荐的解决步骤：**

- 在 Source Editor（源编辑器）中打开文件，并查看有无标记。若没有，请使用外部工具添加标记。
- 将  [`AK::SoundEngine::SeekOnEvent`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a602a2d51d394c55e1896d3ffa521adff.html) 的 `in_bSeekToNearestMarker` 参数设为 false。

---