# Non-compliant device memory detected. Device memory is required for hardware acceleration.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Non-compliant device memory detected. Device memory is required for hardware acceleration.

#### Non-compliant device memory detected. Device memory is required for hardware acceleration.

“检测到不合要求的设备内存。硬件加速需要使用设备内存。”声音引擎所用的 Memory Manager 分配了不合要求的设备内存。设备内存是具有特殊属性的平台特定虚拟内存段；有些硬件加速的解码操作需要这些属性。通常会在使用硬件音频解码器时出现这种情况。

**可能的原因：**

- 游戏采用对 `AK::MemoryMgr` 的默认实现，但却为设备内存分配回调提供了错误的初始化设置。
- 游戏采用对 `AK::MemoryMgr` 的自定义实现，而其没有正确实现设备内存分配函数。

**推荐的解决步骤：**

- 查看 SDK 文档中有关[如何正确覆盖默认 Memory Manager](https://www.audiokinetic.com/library/edge/?source=SDK&id=memorymanager.html) 的要求，并确认游戏是否完全符合所述要求。

---