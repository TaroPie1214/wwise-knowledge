# Dynamic Sequence ID not found.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Dynamic Sequence ID not found.

#### Dynamic Sequence ID not found.

“未找到动态序列 ID”。曾尝试操作 Sequence ID（序列 ID）对应的 Dynamic Sequence（动态序列），但该序列从未打开。确保针对该 Sequence ID 的所有 Dynamic Sequence 函数调用均在成功调用  [`AK::SoundEngine::DynamicSequence::Open`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_ae1255816f8ed9f3e1020f2075f12c690.html) 之后执行。Wwise 收到调用后，您可以确认其先后顺序：打开 [Profiler Settings](../../../01-工程/10-Profiler-Settings.md "Profiler Settings")（性能分析器设置），并启用 **API Calls**（API 调用）。

---