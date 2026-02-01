# Playing ID ... not found in function ...

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Playing ID ... not found in function ...

#### Playing ID ... not found in function ...

“未在函数…中找到播放 ID…。”指定函数需要有效的播放 ID 参数才能继续。声音引擎无法识别所提供的标识符。

播放 ID 由函数 [`AK::SoundEngine::PostEvent()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html) 返回。

**可能的原因：**

- 所提供的播放 ID 属于已经完全结束或停止的 Event（事件）。
- `AK::SoundEngine::PostEvent()` 没有返回播放 ID 值。

**推荐的解决步骤：**

- 在游戏代码中找到指定函数调用，并对 Playing ID（播放 ID）值的来源进行调试。
- 打开 Wwise Profiler（性能分析器），确认是否在此调用前停止了 Event（事件）。

---