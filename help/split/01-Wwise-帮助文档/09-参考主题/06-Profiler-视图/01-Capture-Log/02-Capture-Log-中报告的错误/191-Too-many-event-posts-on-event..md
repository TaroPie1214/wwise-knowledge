# Too many event posts on event.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Too many event posts on event.

#### Too many event posts on event.

“事件发布条目太多。”[`AK::SoundEngine::PostMIDIOnEvent`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_ab24b5dc8bd4d1adbdc6aa5c98d94d946.html) 函数的参数中的 `AkMIDIPost` 条目太多；无法将整个数组装入命令队列。

**推荐的解决步骤：**

- 减少函数中使用的 `AkMIDIPost` 条目数。
- 增大命令队列内存：在调用 [`AK::SoundEngine::Init`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a9a26da64092b97243844df77cbcdbf5f.html#a27257629833b9481dcfdf5e793d9d037) 之前更改 `AkInitSettings.uCommandQueueSize`。有关初始化设置的详细信息，请参阅[高级声音引擎集成](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine__integration__init__advanced.html)。

---