# Sound Engine is not initialized yet or Init bank has not been loaded. Function: ...

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Sound Engine is not initialized yet or Init bank has not been loaded. Function: ...

#### Sound Engine is not initialized yet or Init bank has not been loaded. Function: ...

“声音引擎尚未初始化或没有加载 Init 音频包。函数: …。”在通过调用 [`AK::SoundEngine::Init`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a9a26da64092b97243844df77cbcdbf5f.html#a27257629833b9481dcfdf5e793d9d037) 完成声音引擎初始化之前，大部分函数都无法调用。在完成加载 Init SoundBank（音频包）之前，很多函数都不会起任何作用。

**推荐的解决步骤：**

- 更改函数调用的顺序，确保在 AK::SoundEngine::Init 和 Init.bnk 文件加载之后调用指定函数。
- 使用  [`AK::SoundEngine::LoadBank`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a496b9917fe035f301bcff0accd61f80f.html) 的回调功能来获知 Init.bnk 文件完成加载的时间，并在此之后执行相应调用。
- 使用  [`AK::SoundEngine::RegisterAudioDeviceStatusCallback`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a3f31beb89a4f3ef42475b0849020abe3.html) 来获知第一个 Audio Device 的就绪时间，并在此之后执行相应调用。

---