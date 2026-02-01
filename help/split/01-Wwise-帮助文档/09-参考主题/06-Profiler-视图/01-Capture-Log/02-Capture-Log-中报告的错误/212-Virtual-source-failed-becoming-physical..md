# Virtual source failed becoming physical.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Virtual source failed becoming physical.

#### Virtual source failed becoming physical.

“虚声源未能变为实声源”。若之前播放的声部被归入虚声部，然后请求再次变为实声部（有声），则可能出现此错误。With hardware codecs such as ATRAC9 and Opus, the hardware limitations may have been reached while the voice was virtual.

**可能的原因：**

- 硬件编解码器因硬件限制而无法重新初始化。
- 内存不足，无法分配工作数据。这种情况下，Capture Log（捕获日志）中此错误之前应会出现 Insufficient Memory（内存不足）错误。

**推荐的解决步骤：**

- 利用 Playback Limit（播放限制）管理实声部，并为新的声部预留空间。此目标有时可能无法实现。
- 增大内存限值：在调用  [`AK::SoundEngine::Init`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a9a26da64092b97243844df77cbcdbf5f.html#a27257629833b9481dcfdf5e793d9d037) 之前更改  [`AkMemSettings.uMemAllocationSizeLimit`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_mem_settings_ab95afe86b5ae21cf432d6ca030703055.html#ab95afe86b5ae21cf432d6ca030703055)。有关初始化设置的详细信息，请参阅[高级声音引擎集成](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine__integration__init__advanced.html)。

---