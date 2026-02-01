# Transition not sample-accurate due to source starvation.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Transition not sample-accurate due to source starvation.

#### Transition not sample-accurate due to source starvation.

“因源匮乏而导致过渡无法精确到采样点”。若在两个声音之间出现精确到采样点的过渡时刚好发生 Source Starvation（源匮乏）错误，则将出现此错误。此情况只有在将第二个声音设为从磁盘进行流播放时才会发生。在 Random/Sequence Container（随机/序列容器）、Interactive Music（互动音乐）中或在代码中使用 Dynamic Sequence（动态序列）机制时，可能存在此类过渡。在此之前应会出现 Source Starvation 错误。声音将停止。

**推荐的解决步骤：**

- 为第二个声音使用 [Zero Latency](../../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/01-定义对象的播放行为/00-定义对象的播放行为.md#streaming_media "流播放媒体")（零延迟）机制。
- 选择不要流播放第二个声音，而是将其放入 SoundBank（音频包）。
- 审查是否只是当时使用的磁盘流数量太多，Wwise 或游戏中其他模块都可能导致此情况。通常会在游戏引擎层级来平衡各模块之间的流播放要求。如需详细了解 Wwise Streaming Manager（流播放管理器）操作，请参阅： [流播放/流管理器](https://www.audiokinetic.com/library/edge/?source=SDK&id=streamingdevicemanager.html) 。

---