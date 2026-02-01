# Memory Arenas

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > [Advanced Profiler](00-Advanced-Profiler.md) > Memory Arenas

### Memory Arenas

The Advanced Profiler - Memory Arenas tab displays information about how memory is managed when using the default memory allocator. This tab is primarily used to monitor the total memory reserved for the Wwise sound engine, and to review memory fragmentation over time. For more information about tuning memory arenas, see [Configuration and Tuning of AkMemoryArenas](https://www.audiokinetic.com/library/edge/?source=SDK&id=goingfurther_memoryarenas.html).

| 界面元素 | 描述 |
| --- | --- |
| **全局统计信息** | |
| Total Heap Used | The sum of used memory across all arenas. |
| Total Reserved | The total amount of memory reserved across all arenas. |
| Num Spans Reserved | The total number of spans reserved across all arenas. |
| **Heap Details** | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Name/Span Address Name | The name of the memory arena is listed for the root nodes. The different memory arenas are as follows:  - **Primary**: The default memory arena used by most memory categories. - **Media**: The memory arena used for memory allocations that go to the Media memory category, usually from loading SoundBanks. - **Profiler**: The memory arena used for memory allocations that go to the Profiler and Monitor Queue memory category. This memory arena does not exist in the Release build configuration. - **Device**: The memory arena used for handling any device-specific memory allocations. This is present only on specific platforms that use device-specific memory for audio processing.  Below each memory arena name, all of the spans that belong to the memory arena is listed. Each span is identified by the location of its address in memory in the runtime being profiled. |
| Used | The amount of memory used for the arena as a whole, or the amount of memory used in each span. |
| Free | The amount of free memory available across all spans in the arena, or the amount of memory available in each span. Free memory is characterized by any memory that is reserved but unused. |
| Reserved | The amount of reserved memory across all spans in the arena, or the amount of memory reserved by each span. |
| Largest Free/Fragmentation | The largest contiguous free space of memory across every span in the arena is listed for the root nodes of the tree. This is the largest memory allocation that the arena can service before it needs to request a new span or recycle an unused span.  For each span, a map is displayed, which shows the portions of the span that have memory allocated. The map is up to 32 cells in length, each representing the amount of reserved space that is used. Spans with a reserved size that is not a power-of-two have fewer visible cells. For example, a span that is 4MiB in size shows 32 cells, each representing 128KiB of memory, but a span that is 6MiB in size only shows 24 cells, each representing 256KiB of memory. |
| Allocs | The number of allocations that the memory arena has performed since initialization, including small-block allocations, or the number of allocations that each span has performed since initialization of the span. |
| Frees | The number of deallocations that the memory arena has performed since initialization, including small-block allocations, or the number of deallocations that each span has performed since initialization of the span. |
| Cur. Allocs | The number of memory allocations the memory arena currently has active, including small-block allocations, or the number of active allocations for each span. |
| Type | The span type, between Base, Medium, Large, and Huge. Base spans are created when the memory arena is initialized, Medium spans are secondary spans that are created on demand as memory is required, Large spans are secondary spans for allocations of a certain size (but are only present when support for Large allocations is enabled), and Huge spans are secondary spans that were created for a single memory allocation. This column is empty for memory arenas, and is only populated for span rows. |
| User Data | The value of the user data provided from the callback to allocate a new span, or just a hyphen if zero was returned. This column is empty for memory arenas, and is only populated for span rows. |
| **Small Block Allocator (SBA) Details** | |
| Name/Small Block Size Class | The name of the memory arena for the root items in the tree, or the different size classes for the SBA. |
| Used | The amount of memory used by the SBA in the arena, or the amount of memory used in each SBA size class. |
| Free | The amount of memory that is reserved and unused for the entire SBA in the arena, or the amount of memory that is reserved and unused for just the SBA size class. |
| Reserved | The amount of memory that is reserved for the entire SBA in the arena, or the amount of memory that is reserved for just the SBA size class. |
| SBA Spans Reserved | The number of spans that are reserved for the entire SBA in the arena, or the number of spans that are reserved for just the SBA size class. |
| Allocs | The number of allocations that have been performed for the entire SBA in the arena since initialization, or the number of allocations that have been performed for just the SBA size class. |
| Frees | The number of deallocations that have been performed for the entire SBA in the arena since initialization, or the number of deallocations that have been performed for just the SBA size class. |
| Cur. Allocs | The number of allocations that are currently active for the entire SBA in the arena, or the number of allocations that are currently active for just the SBA size class. |

**相关主题**

- [*在 Wwise 中管理内存*](../../../07-完善工程/05-在-Wwise-中管理内存.md "在 Wwise 中管理内存")

---