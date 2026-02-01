# Audio command queue is full, blocking caller. Reduce number of calls to sound engine or boost command queue memory.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Audio command queue is full, blocking caller. Reduce number of calls to sound engine or boost command queue memory.

#### Audio command queue is full, blocking caller. Reduce number of calls to sound engine or boost command queue memory.

“音频命令队列已满，调用程序被阻止。请减少声音引擎调用或增大命令队列内存”。音频命令队列是一种将所有 API 调用从游戏传递至内部声音引擎的机制。在 Performance Monitor（性能监控器）视图中，可监控此内存缓冲区。在此缓冲区装满命令后，将暂时阻止游戏线程继续添加其他命令。这样做是为了避免因 API 调用丢失而导致游戏和声音引擎之间出现同步问题。不过这可能会造成游戏帧率出现短暂的下降。

**可能的原因：**

- 单个游戏帧中的 API 执行的调用太多。这是报告此错误时最常见的原因。该问题通常是由  [`SetPosition`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a789e25bda32d1e11849afb6584942455.html)、  [`SetRTPCValue`](https://www.audiokinetic.com/library/edge/?source=SDK&id=class_a_k_1_1_i_ak_global_plugin_context_afd9075833fd9d0d4f3ef1b011f832fe3.html)、  [`SetSwitch`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a9c9d57ba7b3af2b896e26297a7657264.html) 等函数的冗余调用造成的。此外，若在启动实际游戏进程之前设置关卡、创建大量 Game Object（游戏对象）、设置位置和 RTPC，也会出现此问题。
- 所执行的 API 调用包含大量参数数组，需要占用很大内存（如  [`SetMultiplePositions`](https://www.audiokinetic.com/library/edge/?source=SDK&id=ak__soundengine__setmultiplepositions.html) 或 Spatial Audio 几何构造调用）。
- 音频处理线程非常繁忙，导致无法处理命令。在这种情况下，会同时出现 Voice Starvation（声部匮乏）错误。
- 音频处理线程被阻止或锁死。这表示游戏或 Wwise 出现了问题。

**推荐的解决步骤：**

- 分析游戏执行的 API 调用：打开 [Profiler Settings](../../../01-工程/10-Profiler-Settings.md "Profiler Settings") (Alt-G)，并启用 **API Calls**（API 调用）。这样可以识别哪个游戏进程在向队列大量输送 API 调用。
- 检查游戏中 Wwise 的 Game Sync（游戏同步器）更新方式，包括 State（状态）、Switch（切换开关）、Game Parameter（游戏参数）。仅在必要时更新这些参数。
- 在游戏帧内添加  [`AK::SoundEngine::RenderAudio`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_afe54af0f5be38be061e8a3c7d7642bb1.html) 调用，以便将游戏帧拆分为多个音频帧。RenderAudio 只作为同一游戏帧内一系列 API 调用的结束位置标记。它会触发音频命令队列处理，并更新内部声音引擎状态。但是，该函数调用并不会渲染实际的音频。
- 确保音频处理线程拥有足够高的 CPU 处理优先级（线程名为 `AK::EventMgrThread`，其优先级由 `AkPlatformInitSettings::threadLEngine` 设定）。若是因此造成的问题，则游戏会同时出现大量 Voice Starvation 错误。
- 将调试器连接至游戏，并确认线程（即 `AK::EventMgrThread`）确实在运行。若未运行，则表示游戏已丢失所有声音。出现此问题时，请联系 Audiokinetic 技术支持部门。
- 增大命令队列内存（请参阅 [AkInitSettings::uCommandQueueSize](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_init_settings_afd6ada0769c6316e7950961c38cc09d0.html#afd6ada0769c6316e7950961c38cc09d0) ）。

**另请参阅：**

- [“Profiler Settings”一节](../../../01-工程/10-Profiler-Settings.md "Profiler Settings")

---