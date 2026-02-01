# Switch ... is bound to RTPC ... It can not be set directly.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Switch ... is bound to RTPC ... It can not be set directly.

#### Switch ... is bound to RTPC ... It can not be set directly.

“切换开关…绑定到了 RTPC…。无法直接进行设置。”若通过 Event 或函数调用显式设置 Switch 值，但对应 Switch Group 由 RTPC 驱动，则将出现此错误。在这种情况下，将忽略 Switch 值。

**推荐的解决步骤：**

- 避免在 Event（事件）中的 Set Switch（设置切换开关）动作中使用该 Switch Group（切换开关组）。
- 避免在  [`SetSwitch`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a9c9d57ba7b3af2b896e26297a7657264.html) 函数调用中使用该 Switch Group（切换开关组）。
- 在 Wwise 工程内的 Switch Group（切换开关组）定义中取消选中 **Use Game Parameter**（使用游戏参数）选项。

---