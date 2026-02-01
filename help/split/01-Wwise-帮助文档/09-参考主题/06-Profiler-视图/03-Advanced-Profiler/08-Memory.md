# Memory

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > [Advanced Profiler](00-Advanced-Profiler.md) > Memory

### Memory

内存。Advanced Profiler — Memory 选项卡显示有关 Wwise 声音引擎如何管理内存的信息。信息中会指示内存管理器追踪的各个内存类别。

|  |  |
| --- | --- |
| [备注] | 备注 |
| The Memory tab only tracks how much memory has been allocated by the memory manager in Wwise, but does not track how much memory has been reserved from the system. Use the [“Memory Arenas”一节](09-Memory-Arenas.md "Memory Arenas") tab to monitor memory reservation and fragmentation. |

| 界面元素 | 描述 |
| --- | --- |
| **全局统计信息** | |
| Used | 用量。所有类别的内存总量。 |
| Total Reserved | The total amount of memory reserved by the memory manager across all memory arenas. |
| **类别表** | |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Category Name | 类别名称。内存类别的名称。The categories and subcategories are defined as follows:  - **Game Object**: Registered emitter objects as well as others. - **Integration**: Allocations specific to game engine integrations, like callbacks or capturing audio output. - **Job Manager**: Allows for asynchronously rendering audio buffers over single and multiple cores. - **Media**: Compressed and uncompressed media in memory. This value increases if you decode your SoundBanks on load. - **Object**:  - **Event**: Events and Actions.   - **Object**: Memory allocations that have not been categorized or don't fit with other categories.   - **Structure**: Mainly the hierarchical structure and container settings. - **Processing**:  - **Processing**: Audio buffers for decompression, applying     Effects, mixing, and DSP. This value is directly influenced by the     number of physical voices and busses.   - **Processing (Plug-in)**: Allocations for plug-ins like AK Convolution Reverb, RoomVerb, and Time Stretch. - **Profiler**:  - **Monitor Queue**: Fixed-size allocation for Profiler connection     data.   - **Profiler**: Everything other than Monitor Queue, for example, debug names for objects. - **Sound Engine**: Basic initialization of the   sound engine and other systems used for sound engine management. - **Spatial Audio**:  - **Geometry**: Geometry sent to Wwise.   - **Reflection/Diffraction Paths**: Mainly the memorization of propagation.   - **Spatial Audio**: Various other memory allocations. - **Streaming**:  - **Streaming**: Supportive costs of streaming. For example, there's a cost for each file opened.   - **Streaming I/O**: Fixed-size buffer into which streamed media chunks are loaded. - **Temp**:  - **Temp (Audio Render)**: Pool of memory to manage temporary allocations. |
| Used | 用量。各个内存类别当前的内存用量。 |
| Peak Used | 峰值用量。自内存管理器初始化以来各个内存类别的峰值内存用量。 |
| Allocs | 分配数。自内存管理器初始化以来执行的分配数。  若此数值递增，则表示内存管理器当前正在分配内存。 |
| Frees | 释放数。自内存管理器初始化以来执行的释放数。  若此数值递增，则表示内存管理器当前正在释放内存。 |
| Cur. Allocs | 当前分配的内存块的数量。Current Alloc 值是通过 Alloc 的数目减去 Free 的数目得到的。  若此数值递增或递减，则表示内存管理器当前正在分配或释放内存。 |

**相关主题**

- [“连接至本地/远程游戏系统”一节](../../../07-完善工程/06-性能分析/06-连接至本地远程游戏系统.md "连接至本地/远程游戏系统")
- [“从声音引擎捕获数据”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/00-从声音引擎捕获数据.md "从声音引擎捕获数据")
- [“使用 Performance Monitor 进行监控和故障排查”一节](../../../07-完善工程/06-性能分析/09-使用-Performance-Monitor-进行监控和故障排查.md "使用 Performance Monitor 进行监控和故障排查")

---