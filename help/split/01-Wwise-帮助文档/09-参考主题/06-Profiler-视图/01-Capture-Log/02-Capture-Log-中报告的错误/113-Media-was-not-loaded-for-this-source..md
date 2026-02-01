# Media was not loaded for this source.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Media was not loaded for this source.

#### Media was not loaded for this source.

“未针对此源加载媒体”。Wwise 期待找到媒体以便播放声音，但媒体并未加载。在 SoundBank（音频包）拆分为 Structure（结构）和 Media（媒体）时，可能出现此错误。因为加载了 Structure 音频包，所以可触发 Event（事件）。但是，若未加载 Media 音频包，将无法播放任何声音。

**可能的原因：**

- SoundBank 加载失败。
- [`PrepareBank()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a3b2589f5d1e30e4a8a69c62d9ee78547.html) 或 [`PrepareEvent()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a98b617d05618e6d18680d198845ff3d7.html) 调用失败。
- SoundBank 没有更新。

**推荐的解决步骤：**

- 在 Capture Log（捕获日志）中查看 SoundBank 失败的相关线索。
- 在 Capture Log 中查看 [`PrepareEvent()`](https://www.audiokinetic.com/library/edge/?id=namespace_a_k_1_1_sound_engine_aec68a4bc3d55b101daffa3de01893a95.htmlsource=SDK&id=namespace_a_k_1_1_sound_engine_a9acdc9745d7277f83131cdfff9b482ad.html) 或 [`PrepareEvent()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a98b617d05618e6d18680d198845ff3d7.html) 失败的相关线索。

---