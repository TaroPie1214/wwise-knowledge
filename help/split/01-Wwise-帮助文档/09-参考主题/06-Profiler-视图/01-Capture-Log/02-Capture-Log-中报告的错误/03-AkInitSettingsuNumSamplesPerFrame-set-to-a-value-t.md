# AkInitSettings::uNumSamplesPerFrame set to a value that is not 256, 512, or 1024. 3D Audio will be disabled.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > AkInitSettings::uNumSamplesPerFrame set to a value that is not 256, 512, or 1024. 3D Audio will be disabled.

#### AkInitSettings::uNumSamplesPerFrame set to a value that is not 256, 512, or 1024. 3D Audio will be disabled.

“AkInitSettings::uNumSamplesPerFrame 被设为了 256、512 和 1024 以外的值。将禁用 3D 音频。”在 System Audio Device 属性中启用了 Allow 3D Audio，但音频帧大小与 3D 音频硬件不兼容。其要求音频帧大小为 256、512 或 1024 个采样。任何其他值都将导致此错误。

**推荐的解决步骤：**

- 在调用 [`AK::SoundEngine::Init`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a9a26da64092b97243844df77cbcdbf5f.html#a27257629833b9481dcfdf5e793d9d037) 之前，将 `AkInitSettings::uNumSamplesPerFrame` 改为 256、512 或 1024。
- 若不想使用 3D Audio，请在 Wwise 工程的 System Audio Device（系统音频设备）设置中取消选中 **Allow 3D Audio**（允许 3D 音频）。

---