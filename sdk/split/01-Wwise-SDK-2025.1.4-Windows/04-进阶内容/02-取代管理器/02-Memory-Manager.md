# Memory Manager

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Memory Manager

Wwise 声音引擎的所有模块都通过 [AK::MemoryMgr](namespace_a_k_1_1_memory_mgr.html) 接口访问内存。声音引擎的客户程序负责此接口的初始化和终止。

SDK 以 静态库 （AkMemoryMgr.lib）的方式提供了一个默认实现。为了使用此库，客户端需要包含 AkModule.h 头文件并调用 [AK::MemoryMgr::Init](namespace_a_k_1_1_memory_mgr_a570a4ed4f667c187d21a821d846f4567.html#a570a4ed4f667c187d21a821d846f4567) 初始化函数。

请参阅 [构建配置](goingfurther_builds.html) 了解有关 AkMemoryMgr.lib 和其它库的使用的更多信息。

# 初始化

在默认实现中，可使用 [AK::MemoryMgr::GetDefaultSettings](namespace_a_k_1_1_memory_mgr_ada3c244e4c16e6863cec97eef039319b.html#ada3c244e4c16e6863cec97eef039319b "Obtain the default initialization settings for the default implementation of the Memory Manager.") 获取默认初始化设置。

## 使用默认内存分配器

在默认情况下，所有内存都是由 Wwise 通过内置 AkMemoryArena 分配的。各个 AkMemoryArena 可使用 `AkMemSettings::memoryArenaSettings` 数组单独进行配置。最多可配置四个 AkMemoryArena：

- `AkMemoryMgrArena_Primary`：大部分内存类别所用的默认 AkMemoryArena。
- `AkMemoryMgrArena_Media`：该 AkMemoryArenaMedia 用于 Media 内存类别的内存分配（一般在加载 SoundBank 时实现）。
- `AkMemoryMgrArena_Profiler`：该 AkMemoryArenaMedia 用于 Profiler 和 Monitor Queue 内存类别的内存分配。Release 构建配置中没有此 AkMemoryArena。
- `AkMemoryMgrArena_Device`：该 AkMemoryArena 用于处理特定于设备的内存分配。只有使用设备特定内存实施音频处理的平台（即定义了 `AK_DEVICE_MEMORY_SUPPORTED` 的平台）有此 AkMemoryArena。

建议为各个 AkMemoryArena 实现以下回调以便集成到游戏引擎中。这样 AkMemoryArena 便可根据需要利用回调来获取和释放内存跨度。

- `AkMemoryArenaSettings::fnMemAllocSpan`
- `AkMemoryArenaSettings::fnMemFreeSpan`

另外，还可使用 `AkMemoryArenaSettings::uMemReservedLimit` 对各个 AkMemoryArena 可预留多少内存设定限制。

如需了解配置 AkMemoryArena 时可用的其他设置，请参阅 [AkMemoryArena 的配置和调整](goingfurther_memoryarenas.html) 章节。

## 使用自定义内存分配器

若要全部改用自定义内存分配器，请重写以下各项回调：

- [AkMemSettings::pfInitForThread](struct_ak_mem_settings_a64de7db44eeaaf01011d473529667b7d.html#a64de7db44eeaaf01011d473529667b7d "(Optional) Thread-specific allocator initialization hook.")
- [AkMemSettings::pfTermForThread](struct_ak_mem_settings_adec2f9a28716236a5e1b2c7a258b8c6e.html#adec2f9a28716236a5e1b2c7a258b8c6e "(Optional) Thread-specific allocator termination hook.")
- [AkMemSettings::pfTrimForThread](struct_ak_mem_settings_afbf907696820f2fd30f88af36620bdd8.html#afbf907696820f2fd30f88af36620bdd8 "(Optional) Thread-specific allocator \"trimming\" hook. Used to relinquish memory resources when thread...")
- [AkMemSettings::pfMalloc](struct_ak_mem_settings_a7b0974f6f5480a8fd549d5350b960079.html#a7b0974f6f5480a8fd549d5350b960079 "(Optional) Memory allocation hook.")
- [AkMemSettings::pfMalign](struct_ak_mem_settings_a71352af10d5b691094fb319ab5e36b38.html#a71352af10d5b691094fb319ab5e36b38 "(Optional) Memory allocation hook.")
- [AkMemSettings::pfRealloc](struct_ak_mem_settings_a6ccdc83c31c9dfdc5b9d22423bd7aee9.html#a6ccdc83c31c9dfdc5b9d22423bd7aee9 "(Optional) Memory allocation hook.")
- [AkMemSettings::pfFree](struct_ak_mem_settings_a3acf39bd77470f4b6adf8441b5f8ddd2.html#a3acf39bd77470f4b6adf8441b5f8ddd2 "(Optional) Memory allocation hook.")
- [AkMemSettings::pfTotalReservedMemorySize](struct_ak_mem_settings_ad1f86b301a24dceb8622a9ee74466bcb.html#ad1f86b301a24dceb8622a9ee74466bcb "(Optional) Memory allocation statistics hook.")
- [AkMemSettings::pfSizeOfMemory](struct_ak_mem_settings_a27eaf83daea702267d7d71e734cba836.html#a27eaf83daea702267d7d71e734cba836 "(Optional) Memory allocation statistics hook.")

在设置 `AkMemType_Device` 位后，上述分配函数必须通过返回设备内存来与该位协调一致。

|  |  |
| --- | --- |
|  | **备注:** 在使用自定义内存分配器时，无法在 Wwise 中对 AkMemoryArena 实施性能分析。 |

## 配置以便进行调试

使用以下设置来启用额外的运行时调试功能：

- [AkMemSettings::uMemoryDebugLevel](struct_ak_mem_settings_ae97967db68ec10e8410af9f776f89e0d.html#ae97967db68ec10e8410af9f776f89e0d "Default 0 disabled. 1 debug enabled. 2 stomp allocator enabled. 3 stomp allocator and debug enabled....")

该不透明值允许自定义实现根据需要定义任意数量的内存调试功能。The default implementation provides three levels.

- Level 1 enables basic runtime memory debugging including; capturing **FILE** and **LINE** for each allocation, tracking callstacks where possible for each allocation, reporting leaks in a detailed manner upon shutdown and some very light integrity checks. This is light enough that you can run this during development by default.
- 级别 2 允许使用 Stomp 分配器，可为每项分配使用离散的虚拟内存页，并设法捕获所有越界写入。该级别的实现非常慢，而且会占用大量资源。因此，建议不要在开发当中默认启用，而只在尝试查明内存 stomp 原因时启用。
- Level 3 enables both runtime debugging and the stomp allocator.

使用以下设置将所有分配转储到文件中（注意，此时须将 [AkMemSettings::uMemoryDebugLevel](struct_ak_mem_settings_ae97967db68ec10e8410af9f776f89e0d.html#ae97967db68ec10e8410af9f776f89e0d "Default 0 disabled. 1 debug enabled. 2 stomp allocator enabled. 3 stomp allocator and debug enabled....") 设为 1，并采用非 Release 配置）：

- [AK::MemoryMgr::DumpToFile](namespace_a_k_1_1_memory_mgr_a4f48ed6707ab2f2341f4a81f1c6053d7.html#a4f48ed6707ab2f2341f4a81f1c6053d7)

注：声音引擎使用 [AK::IAkStreamMgr::CreateStd()](class_a_k_1_1_i_ak_stream_mgr_a1de2a7935a2d3cddb71e7cc7f48effd6.html#a1de2a7935a2d3cddb71e7cc7f48effd6) 打开播放流以供写入。若使用 Stream Manager 的默认实现，则在底层 IO 接口 [AK::StreamMgr::IAkLowLevelIOHook::BatchOpen()](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a0abfde848b599b5e5b8e8ed63dc8b555.html#a0abfde848b599b5e5b8e8ed63dc8b555) 的实现中执行文件打开功能。

使用以下设置来监控专门为调试分配的内存池（Release 配置中并不会使用这些内存池）：

- [AkMemSettings::pfDebugMalloc](struct_ak_mem_settings_aa7ad0e0dd66eaf23d3721301fc516be6.html#aa7ad0e0dd66eaf23d3721301fc516be6 "(Optional) Memory allocation debugging hook. Used for tracking calls to pfMalloc.")
- [AkMemSettings::pfDebugMalign](struct_ak_mem_settings_ab590383aaeabbb4d198151f9041f7517.html#ab590383aaeabbb4d198151f9041f7517 "(Optional) Memory allocation debugging hook. Used for tracking calls to pfMalign.")
- [AkMemSettings::pfDebugRealloc](struct_ak_mem_settings_ad1a6c086b143f9a84de67a552b2a63dd.html#ad1a6c086b143f9a84de67a552b2a63dd "(Optional) Memory allocation debugging hook. Used for tracking calls to pfRealloc.")
- [AkMemSettings::pfDebugFree](struct_ak_mem_settings_ac50c4db30282223a2de087fc2d40b88c.html#ac50c4db30282223a2de087fc2d40b88c "(Optional) Memory allocation debugging hook. Used for tracking calls to pfFree.")

上述调试函数并不能替代分配函数；它们只是针对各个内存分配事件的通知回调。

有关更多信息，请参阅以下各节：

- [示例](samplecode.html) ：查看示例代码并了解有关在游戏中初始化 Memory Manager 的详细信息。
- [加载 SoundBank](soundengine_banks_loading.html) ：了解有关 SoundBank 内存用量的详细信息。
- [优化内存利用效率](goingfurther_optimizingmempools.html) ：了解有关如何优化内存利用效率的信息。

# 取代内存管理器

客户端可提供 [AK::MemoryMgr](namespace_a_k_1_1_memory_mgr.html) 接口的自定义实现。AkMemoryMgr.h 中定义的所有函数全部都要实现。AkModule.h 在 [AK::MemoryMgr](namespace_a_k_1_1_memory_mgr.html) 命名空间中定义的函数不必实现，因为它们只针对内存管理器的默认实现。

跟在改写 `AkMemSettings` 的各个分配函数时一样，要想编写新的 [AK::MemoryMgr](namespace_a_k_1_1_memory_mgr.html) 实现，必须注意在设置 `AkMemType_Device` 位后通过返回设备内存来与该位协调一致。设备内存分配仅适用于部分平台，且必须与特定参数协调一致（详见平台特定章节）。