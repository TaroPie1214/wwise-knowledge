# Job worker function was called more often than it was requested. Check your sound engine integration.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Job worker function was called more often than it was requested. Check your sound engine integration.

#### Job worker function was called more often than it was requested. Check your sound engine integration.

“作业辅助函数被调用的次数比请求的次数多。检查声音引擎集成。”声音引擎的作业管理程序会通过提供辅助函数回调来向游戏发送有关 CPU 时间的请求。它希望游戏针对每个请求调用一次该函数。

否则，在执行音频处理的过程中会出现问题。

**可能的原因：**

- 若 Capture Log（捕获日志）中显示此消息，则表示游戏在声音引擎没有明确发出请求的情况下调用了辅助函数回调。

**推荐的解决步骤：**

- 查看 SDK 文档中有关[并行执行音频渲染作业](https://www.audiokinetic.com/library/edge/?source=SDK&id=goingfurther_eventmgrthread.html#eventmgrthread_jobmgr)的要求，并确认游戏是否完全符合所述要求。

---