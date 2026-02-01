# Cannot seek in sound that is within a continuous container with special transitions.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Cannot seek in sound that is within a continuous container with special transitions.

#### Cannot seek in sound that is within a continuous container with special transitions.

“连续容器包含特殊过渡，无法在声音中寻址”。若 Random/Sequence Container 设为 Continuous，且 Transition Type 设为 XFade (amp)、XFade (power)、Trigger Rate 或 Sample Accurate，则请求针对所述容器寻址时将发生此错误。这些过渡可能会要求在尚未准备好播放的声音中寻址（过渡的第二个声音）。

**推荐的解决步骤：**

- 对于要在 Continuous 模式下播放 Random/Sequence Container 的 Event，避免调用 [`AK::SoundEngine::SeekOnEvent()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a602a2d51d394c55e1896d3ffa521adff.html)。

---