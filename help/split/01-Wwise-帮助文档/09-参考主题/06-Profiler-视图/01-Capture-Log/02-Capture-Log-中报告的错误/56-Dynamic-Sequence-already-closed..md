# Dynamic Sequence already closed.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Dynamic Sequence already closed.

#### Dynamic Sequence already closed.

“动态序列已关闭”。曾尝试操作 Dynamic Sequence（动态序列），但该序列已关闭。确保所有 Dynamic Sequence 函数调用均在  [`AK::SoundEngine::DynamicSequence::Close`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_ab204d963f6b81abc102a6d6b8272b591.html) 之前执行。Wwise 收到调用后，您可以确认其先后顺序：打开 [Profiler Settings](../../../01-工程/10-Profiler-Settings.md "Profiler Settings")（性能分析器设置），并启用 **API Calls**（API 调用）。

---