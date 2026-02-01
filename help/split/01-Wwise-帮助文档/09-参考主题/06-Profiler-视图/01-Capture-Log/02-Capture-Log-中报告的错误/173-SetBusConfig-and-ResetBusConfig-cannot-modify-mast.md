# SetBusConfig and ResetBusConfig cannot modify master bus speaker configuration, it is dictated by the output device.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > SetBusConfig and ResetBusConfig cannot modify master bus speaker configuration, it is dictated by the output device.

#### SetBusConfig and ResetBusConfig cannot modify master bus speaker configuration, it is dictated by the output device.

This error originates from [`AK::SoundEngine::SetBusConfig`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_aa4da48bc7fe7adc10f42272f62fd33fe.html) and indicates that the `audioNodeID` parameter points to a Bus that is a Main Audio Bus (top-most level in the hierarchy). Main Audio Busses take their speaker configuration from the hardware they output to.

**推荐的解决步骤：**

- 仅提供子总线 ID。确认 Wwise 工程中的总线结构。
- 检查总线名称/ID 有无拼写错误。

---