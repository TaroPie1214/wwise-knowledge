# Audio command is too large to fit in the command queue. Break the command in smaller pieces.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Audio command is too large to fit in the command queue. Break the command in smaller pieces.

#### Audio command is too large to fit in the command queue. Break the command in smaller pieces.

“音频命令太大，无法装入命令队列。请将命令拆分为多个部分”。若 Wwise SDK API 的单个函数调用对整个命令队列来说太大，则将出现此错误。可能触发此错误的函数一般都可将数组作为参数进行传递。该问题通常是由  [`AK::SoundEngine::SetMultiplePositions`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_ad63431938ab1e605a1f6e7fb013c0128.html) 造成的，可能在单个调用中包含大量位置（上千个）。将数组拆分为多个部分，执行多个函数调用。

---