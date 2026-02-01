# Unknown IO device error. .. returned .. on file ...

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Unknown IO device error. .. returned .. on file ...

#### Unknown IO device error. .. returned .. on file ...

“未知 IO 设备错误”。此错误表示在 I/O 设备上执行 Read（读取）或 Write（写入）操作时出现错误。The actual error is device-specific and reported in the message. 若游戏运用自行实现的 I/O 挂钩，则可能出现此错误。

**推荐的解决步骤：**

- 将调试程序连接至 I/O 挂钩代码。
- If you do not have a custom I/O hook, contact Audiokinetic Support.

---