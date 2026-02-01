# Seek table required to seek in Opus sources. Please update conversion settings.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Seek table required to seek in Opus sources. Please update conversion settings.

#### Seek table required to seek in Opus sources. Please update conversion settings.

“寻址表要求在 OpusNX 源中寻址。请更新转码设置。”声音引擎无法在 Opus 编码源中寻址。Opus 编解码器是一种可变码率编解码器；因此，需要使用寻址表来寻址到特定位置。

**可能的原因：**

- 针对没有寻址表的 Opus 编码声音发送了带有 Seek（寻址）动作的 Event（事件）。
- 针对没有寻址表的 Opus 编码声音调用了 [`AK::SoundEngine::SeekOnEvent`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a602a2d51d394c55e1896d3ffa521adff.html)。
- 对于没有寻址表的 Opus 编码声音，Advanced Settings（高级设置）中的 Virtual voice behavior（虚声部行为）设为了 **Play from elapsed time**（继续播放，如同从未停止播放一样）。
- 该声音的长度短于寻址表粒度。

**推荐的解决步骤：**

- 在声音的 Conversion Setting 中添加 Seek Table。

  |  |  |
  | --- | --- |
  | [注意] | 注意 |
  | 一般可通过添加寻址表来解决这一问题。在应用以下所列的其他解决方案时要谨慎，尤其是在更改 Virtual Voice 设置的时候。 |
- 在声音的 **Conversion Setting** 中更改编解码器类型。
- 在声音的 Advanced Settings（高级设置）中将 Virtual voice behavior（虚声部行为）改为除 **Play from elapsed time**（继续播放，如同从未停止播放一样）外的其他选项。
- 减小寻址表粒度的帧数，或者选择帧大小较小的 ShareSet。
- 避免在此声音上做跳转。

---