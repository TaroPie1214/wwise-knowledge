# Seek table is not present, or seek table granularity is larger than the maximum decode buffer size. Conversion settings may need to be updated.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Seek table is not present, or seek table granularity is larger than the maximum decode buffer size. Conversion settings may need to be updated.

#### Seek table is not present, or seek table granularity is larger than the maximum decode buffer size. Conversion settings may need to be updated.

声音引擎无法在 Vorbis 编码编码源中进行跳转。Vorbis 编解码器是可变比特率编解码器；因此，要跳转到特定位置，您需要 Seek Table。

**可能的原因：**

- 对于未启用 Seek Table 的 Vorbis 编码声音，调用了带有 Seek 行为的事件。
- 为某个 Vorbis 编码声音调用了  [`AK::SoundEngine::SeekOnEvent`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a602a2d51d394c55e1896d3ffa521adff.html)，但该声音没有启用 Seek Table。
- 对于没有使用 Seek Table 的 Vorbis 编码声音，其 Advanced Settings 中虚声部行为采用了 **Play from elapsed time**。
- 该声音的长度短于寻址表粒度。
- 解码缓冲区限值小于寻址表粒度。

**推荐的解决步骤：**

- 在声音的 Conversion Setting 中添加 Seek Table。

  |  |  |
  | --- | --- |
  | [备注] | 备注 |
  | 通常，可通过增加寻址表来解决这一问题。在应用以下所列的其他解决方案时要谨慎，尤其是在更改虚声部设置的时候。 |
- 减小寻址表粒度的帧数，或者选择帧大小较小的 ShareSet。
- 在声音的 **Conversion Setting** 中更改编解码器类型。
- 在声音的 Advanced Settings（高级设置）中将 Virtual voice behavior（虚声部行为）改为除 **Play from elapsed time**（继续播放，如同从未停止播放一样）外的其他选项。
- 避免在此声音上做跳转。

---