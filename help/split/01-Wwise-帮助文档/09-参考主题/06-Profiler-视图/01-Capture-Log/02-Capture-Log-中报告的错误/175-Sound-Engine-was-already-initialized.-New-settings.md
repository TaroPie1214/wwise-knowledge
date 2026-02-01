# Sound Engine was already initialized. New settings ignored.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Sound Engine was already initialized. New settings ignored.

#### Sound Engine was already initialized. New settings ignored.

“声音引擎已经初始化。新的设置不起作用。”在调用 [`AK::SoundEngine::Init`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a9a26da64092b97243844df77cbcdbf5f.html#a27257629833b9481dcfdf5e793d9d037) 时，若声音引擎仍处于活跃状态，则将出现此错误。这种情况不受支持。若想更改引擎的全局参数，必须先终止引擎，然后重新初始化。

---