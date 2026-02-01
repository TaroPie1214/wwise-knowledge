# Could not allocate effect.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Could not allocate effect.

#### Could not allocate effect.

“无法分配效果器”。此错误表示没有足够的内存，无法为插件参数分配所需内存。此错误之前通常会出现 Insufficient Memory（内存不足）错误。

**可能的原因：**

- 总计可用 Wwise 内存太少。
- 运行时加载和创建的对象太多。
- 在自定义插件开发过程中出现错误。

**推荐的解决步骤：**

- 增加可用内存总量：在调用 [`AK::MemoryMgr::Init`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_memory_mgr_a570a4ed4f667c187d21a821d846f4567.html) 之前增大 [`AkMemSettings::uMemAllocationSizeLimit`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_mem_settings_ab95afe86b5ae21cf432d6ca030703055.html)。
- 减少通过 SoundBank（音频包）加载的对象数量。

**另请参阅：**

- [“Memory allocation failed.”一节](115-Memory-allocation-failed..md "Memory allocation failed.")
- [高级声音引擎集成](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine__integration__init__advanced.html)：了解有关初始化设置的详细信息。

---