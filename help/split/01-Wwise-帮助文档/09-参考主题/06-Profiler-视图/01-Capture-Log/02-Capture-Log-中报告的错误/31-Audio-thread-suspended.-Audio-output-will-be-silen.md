# Audio thread suspended. Audio output will be silent.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Audio thread suspended. Audio output will be silent.

#### Audio thread suspended. Audio output will be silent.

“音频线程中止。音频输出将保持静音。”在游戏生命周期内的各个时间点都可能会显示此消息。比如，在操作系统将游戏转到后台时，或在移动设备上的电话呼叫开始时。这并不代表出现了问题。通常只是因为调用了 [`AK::SoundEngine::Suspend`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_afc66d31bf5c6425d841ca3510e2d0539.html)。在发出特定操作系统通知时，Wwise 也会自动触发该消息。在生命周期事件结束后应会继续播放声音，并且会显示 [“Audio thread resumed, audio restarts.”一节](30-Audio-thread-resumed,-audio-restarts..md "Audio thread resumed, audio restarts.")。

---