# AkInitSettings::uNumSamplesPerFrame value unsupported by Opus hardware decoder. Supported size: 256, 512 and 1024. Opus will be disabled.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > AkInitSettings::uNumSamplesPerFrame value unsupported by Opus hardware decoder. Supported size: 256, 512 and 1024. Opus will be disabled.

#### AkInitSettings::uNumSamplesPerFrame value unsupported by Opus hardware decoder. Supported size: 256, 512 and 1024. Opus will be disabled.

“AkInitSettings::uNumSamplesPerFrame 值不受 Opus 硬件解码器支持。支持的值: 256、512 和 1024。将禁用 Opus。”Opus 硬件解码器仅支持所列的三个缓冲区大小值。否则，所有使用 Opus 的声音都会显示错误且无法播放。

**推荐的解决步骤：**

- 在调用 [`AK::SoundEngine::Init`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a9a26da64092b97243844df77cbcdbf5f.html#a27257629833b9481dcfdf5e793d9d037) 之前，将 `AkInitSettings::uNumSamplesPerFrame` 改为 256、512 或 1024。

---