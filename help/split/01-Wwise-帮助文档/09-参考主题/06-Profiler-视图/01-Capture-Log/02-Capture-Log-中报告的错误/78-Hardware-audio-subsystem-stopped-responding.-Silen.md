# Hardware audio subsystem stopped responding. Silent mode is enabled.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Hardware audio subsystem stopped responding. Silent mode is enabled.

#### Hardware audio subsystem stopped responding. Silent mode is enabled.

“硬件音频系统停止响应。已启用静默模式”。此错误表示音频驱动程序长时间未对 Wwise 做出响应。这通常是因为音频驱动程序崩溃，且重新配置或重置后未通知声音引擎或应用程序。引擎处于安全模式，未选择任何音频设备。音频事件仍将被处理，因此与游戏的同步并未中断。

通常，在系统的音频驱动程序重启后，此错误会自行修复。

在部分系统上（如 iOS 和 Android 手机），因电话呼叫而收到系统中断请求时会出现此错误。在中断结束后，音频一般会恢复。

---