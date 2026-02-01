# Lower engine command list is full.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Lower engine command list is full.

#### Lower engine command list is full.

“底层引擎命令列表已满。”此错误表示内部进程耗尽了内存。在此之前通常会出现 Insufficient Memory（内存不足）错误。

**推荐的解决步骤：**

- 增大内存限值：在调用  [`AK::SoundEngine::Init`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a9a26da64092b97243844df77cbcdbf5f.html#a27257629833b9481dcfdf5e793d9d037) 之前更改  [`AkMemSettings.uMemAllocationSizeLimit`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_mem_settings_ab95afe86b5ae21cf432d6ca030703055.html#ab95afe86b5ae21cf432d6ca030703055)。有关初始化设置的详细信息，请参阅[高级声音引擎集成](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine__integration__init__advanced.html)。
- 利用 Playback Limit（播放限制）和 Virtual Voice（虚声部）来终止声部，从而优化内存管理。

---