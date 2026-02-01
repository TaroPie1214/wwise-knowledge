# Insufficient Space to Load Bank.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Insufficient Space to Load Bank.

#### Insufficient Space to Load Bank.

“空间不足，无法加载音频包”。可用内存不足，无法加载 SoundBank（音频包）中包含的全部对象。请注意，此错误与 SoundBank 的 Event（事件）和 Structure（结构）部分有关，而与 Media（媒体）部分无关。

**推荐的解决步骤：**

- 将 SoundBank 拆分为多个小的 SoundBank，并在恰当时机动态加载。
- 卸载未使用的 SoundBank。
- 增加可用内存总量：在调用 [`AK::MemoryMgr::Init`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_memory_mgr_a570a4ed4f667c187d21a821d846f4567.html) 之前增大 [`AkMemSettings::uMemAllocationSizeLimit`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_mem_settings_ab95afe86b5ae21cf432d6ca030703055.html)。

---