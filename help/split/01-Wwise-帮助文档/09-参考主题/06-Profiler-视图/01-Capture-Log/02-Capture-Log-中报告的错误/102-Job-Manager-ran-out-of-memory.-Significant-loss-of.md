# Job Manager ran out of memory. Significant loss of performance or instability may occur.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Job Manager ran out of memory. Significant loss of performance or instability may occur.

#### Job Manager ran out of memory. Significant loss of performance or instability may occur.

“作业管理程序耗尽内存。可能会出现严重的性能下降或不稳定问题。”在关键内存分配过程中，声音引擎的 Job Manager 系统耗尽内存。因为此内存分配不允许失败，所以在成功之前会一直重试，在此期间将会冻结音频渲染。

**可能的原因：**

- 在关键 Job Manager 分配期间，[`AK::MemoryMgr`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_memory_mgr.html) 耗尽内存。

**推荐的解决步骤：**

- 要想避免这一问题，可在声音引擎初始化期间为 Job Manager 分配预先分配一定数量的内存片。在声音引擎的初始化设置中增大内存片数量或增大这些内存片的大小。对此，可参阅 SDK 文档中的[降低 Job Manager 内存用量](https://www.audiokinetic.com/library/edge/?source=SDK&id=goingfurther_eventmgrthread.html#eventmgrthread_jobmgr_memory)。
- 确保游戏对 [`AK::MemoryMgr`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_memory_mgr.html) 的实现不会对 ID 为 `AkMemID_JobMgr` 的分配施加硬性限制。

---