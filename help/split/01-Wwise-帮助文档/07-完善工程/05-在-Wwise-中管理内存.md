# 在 Wwise 中管理内存

[Wwise 帮助文档](../00-Wwise-帮助文档.md) > [完善工程](00-完善工程.md) > 在 Wwise 中管理内存

## 在 Wwise 中管理内存

- All memory allocations are categorized based on their use in the sound engine.
- The default implementation of the memory manager uses the categories to direct allocations to one of multiple memory arenas. Each memory arena, also known as AkMemoryArena, can be configured for different production requirements and memory mangement strategies.

For more detailed information on memory management see:

- [Memory Manager](https://www.audiokinetic.com/library/edge/?source=SDK&id=memorymanager.html)
- [关于降低内存用量的技巧](https://www.audiokinetic.com/library/edge/?source=SDK&id=goingfurther_optimizingmempools_reducing_memory.html)
- [Information for Configuring Memory Arenas](https://www.audiokinetic.com/library/edge/?source=SDK&id=goingfurther_memoryarenas.html)

---