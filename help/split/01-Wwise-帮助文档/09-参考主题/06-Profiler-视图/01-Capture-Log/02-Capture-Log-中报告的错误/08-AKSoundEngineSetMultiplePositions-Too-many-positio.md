# AK::SoundEngine::SetMultiplePositions: Too many positions.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > AK::SoundEngine::SetMultiplePositions: Too many positions.

#### AK::SoundEngine::SetMultiplePositions: Too many positions.

“AK::SoundEngine::SetMultiplePositions: 位置太多。”[`AK::SoundEngine::SetMultiplePositions`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_ad63431938ab1e605a1f6e7fb013c0128.html) 的 `in_pPositions` 参数数组太大，无法装入命令队列。

**推荐的解决步骤：**

- 减少此函数中使用的位置数量。
- 增大命令队列内存：在调用 [`AK::SoundEngine::Init`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a9a26da64092b97243844df77cbcdbf5f.html#a27257629833b9481dcfdf5e793d9d037) 之前更改 [`AkInitSettings.uCommandQueueSize`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_init_settings_afd6ada0769c6316e7950961c38cc09d0.html)。有关初始化设置的详细信息，请参阅[高级声音引擎集成](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine__integration__init__advanced.html)。

---