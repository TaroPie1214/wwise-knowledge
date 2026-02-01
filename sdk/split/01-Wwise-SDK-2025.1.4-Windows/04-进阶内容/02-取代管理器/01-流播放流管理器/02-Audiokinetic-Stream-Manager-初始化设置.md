# Audiokinetic Stream Manager 初始化设置

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Audiokinetic Stream Manager 初始化设置

|  |
| --- |
| **Default Streaming Manager Information**    本章专门介绍高级 Stream Manager API 的默认实现。  Stream Manager 和 [AK::StreamMgr::Create()](namespace_a_k_1_1_stream_mgr_af9d67dd0e502e5603a2921099916e2ab.html#af9d67dd0e502e5603a2921099916e2ab) 方法的初始化设置专门针对 Audiokinetic 的实现，在 [AkStreamMgrModule.h](_ak_stream_mgr_module_8h.html) 中定义。 |

以下是 Stream Manager 默认实现的初始化设置描述。 您一定需要调整游戏的这些设置，才能充分利用 I/O 和内存资源。

# Stream Manager 设置

[AkStreamMgrSettings](struct_ak_stream_mgr_settings.html) 结构定义整个 Stream Manager 所需的设置。每个小节中指定的默认值即为 [AK::StreamMgr::GetDefaultSettings()](namespace_a_k_1_1_stream_mgr_a50fe8111fcb883651390fab6e9dc5ebc.html#a50fe8111fcb883651390fab6e9dc5ebc) 返回的值。这些默认值可能并不适用于您的系统。[I/O 技巧、故障排除和优化](streamingmanager_tips.html) 中包含的信息可以帮助您选择最佳值。

# 流播放设备设置

[AkDeviceSettings](struct_ak_device_settings.html) 结构定义了使用 [AK::CreateDevice()](namespace_a_k_1_1_stream_mgr_a64a22d377d25137222fbb66ff21965d5.html#a64a22d377d25137222fbb66ff21965d5) 创建的各个设备所需的设置。每个小节中所示的默认值即为 [AK::StreamMgr::GetDefaultDeviceSettings()](namespace_a_k_1_1_stream_mgr_a7d01e09a9bb6b6d34c2bb8f4c8995214.html#a7d01e09a9bb6b6d34c2bb8f4c8995214) 返回的值。这些默认值可能并不适用于您的系统。

## I/O 内存大小

[AkDeviceSettings::uIOMemorySize](struct_ak_device_settings_a75893592924a59881fe2cbca4e4ddd04.html#a75893592924a59881fe2cbca4e4ddd04 "Size of memory for I/O (for automatic streams). It is passed directly to AK::MemoryMgr::Malign(),...") 是为设备的自动流所保留的内存总大小。设备创建一个专用内存池，自动流 I/O 数据将写入其中。如果您不打算使用自动流，则可以将值指定为零。但请注意，声音引擎会需要使用自动流来播放流音频文件。AkDeviceSettings::pIOMemory、AkDeviceSettings::uIOMemoryAlignment 和 [AkDeviceSettings::ePoolAttributes](struct_ak_device_settings_ac765faebf4d47270efbe33cc762192cb.html#ac765faebf4d47270efbe33cc762192cb "Attributes for I/O memory. Here, specify the allocation type (AkMemType_Device, and so on)....") 是直接传递到内存池创建方法 AK::MemoryMgr::CreatePool() 的额外参数。

默认值：

- [AkDeviceSettings::pIOMemory](struct_ak_device_settings_a3a99efb65d353954df652c007ac761c5.html#a3a99efb65d353954df652c007ac761c5): NULL（内存池由设备分配）
- [AkDeviceSettings::uIOMemorySize](struct_ak_device_settings_a75893592924a59881fe2cbca4e4ddd04.html#a75893592924a59881fe2cbca4e4ddd04 "Size of memory for I/O (for automatic streams). It is passed directly to AK::MemoryMgr::Malign(),..."): 2 MB
- AkDeviceSettings::uIOMemoryAlignment：4（在 Windows 下 - 取决于平台）
- AkDeviceSettings::ePoolAttributes：AkMalloc（在 Windows 下 - 取决于平台）

## 粒度

粒度由 [AkDeviceSettings::uGranularity](struct_ak_device_settings_abd4879bfd150b9a2f898102e3815dbe2.html#abd4879bfd150b9a2f898102e3815dbe2 "I/O requests granularity (typical bytes/request).") 指定。它定义发送到 Low-Level I/O 的标准请求大小，无论其来自标准流（分片操作）还是自动流（单一流缓冲区的大小）。自动流使用的缓冲区数量不定，具体数量取决于可用的内存量。可用于自动流的缓冲区总数等于  
[AkDeviceSettings::uIOMemorySize](struct_ak_device_settings_a75893592924a59881fe2cbca4e4ddd04.html#a75893592924a59881fe2cbca4e4ddd04 "Size of memory for I/O (for automatic streams). It is passed directly to AK::MemoryMgr::Malign(),...") / AkDeviceSettings::uGranularity。

|  |  |
| --- | --- |
|  | **技巧:** 为避免内存原因而导致干涸，应至少将流缓冲区数量加倍。因此，I/O 内存池应至少设置为 2 \* uGranularity \* nominal\_number\_of\_streams  注意，每个流所需的实际缓冲区数量是变动的，具体取决于流启发式算法和设备的目标缓冲长度（请参阅 AkDeviceSettings::fTargetAutoStmBufferLength）。确定您所需要的 I/O 内存大小的正确方式是计算最极端场景中所有流所需的吞吐量之和，然后乘以 fTargetAutoStmBufferLength。在实践中，更简单的方法是首先选取一个大值，通过 Wwise Profiler 分析您的游戏，然后使用 Streaming Devices 选项卡中报告的 I/O 占用率最大值。 |

默认值：16 KB

## I/O 线程属性

所有高层设备都使用单独的线程将传输请求发布给名为“AK::IOThread”的 Low-Level I/O。您可以使用 [AkDeviceSettings::threadProperties](struct_ak_device_settings_a66496eabd7bf4cd482f2ef9925e489c4.html#a66496eabd7bf4cd482f2ef9925e489c4 "Scheduler thread properties.") 来为此线程指定属性。每个平台的 [AkThreadProperties](struct_ak_thread_properties.html) 在 SDK/include/AK/Tools/{Platform name}/AkPlatformFuncs.h 中定义。此方法通常指定线程优先级和处理器。

|  |  |
| --- | --- |
|  | **技巧:** I/O 调度程序线程应具有高优先级，因为它不会使用大量 CPU：大部分时间它都在等待为流服务，或者等待磁盘控制器。然而，当需要选择任务并将其发布给 Low-Level I/O 时，应保证它能够快速执行，以使存储设备吞吐量最大化。 |

默认值：针对平台的默认线程属性（由 [AKPLATFORM::AkGetDefaultThreadProperties()](namespace_a_k_p_l_a_t_f_o_r_m_af8ca5269595a1270425d165061ec182a.html#af8ca5269595a1270425d165061ec182a) 返回）的优先级等于 AK\_THREAD\_PRIORITY\_ABOVE\_NORMAL（在 AkPlatformFuncs.h 中定义）。

## 目标缓冲长度

[AkDeviceSettings::fTargetAutoStmBufferLength](struct_ak_device_settings_af396c1626da7df1bbb6d9129e132b02f.html#af396c1626da7df1bbb6d9129e132b02f "Targetted automatic stream buffer length (ms). When a stream reaches that buffering,...") 是设备 I/O 调度程度的启发式算法，仅适用于自动流。它为每个流指定了应该达到的理想缓冲时间，单位：毫秒。Stream Manager 为指定流执行 I/O，直至达到该缓冲长度。会使用流的吞吐量启发式算法，将时间值转换成缓冲区大小。例如，以 44.1 KHz 采样的 16 位立体声需要 172.3 KB/s 的吞吐量。如果目标缓冲长度设为 380 毫秒，则该流的目标缓冲大小约为 64 KB。缓冲越多，流干涸的可能性越小。另一方面，I/O 调度程序会更繁忙，并占用更多的 CPU 和更大的流 I/O 池内存。最佳值主要取决于底层存储设备带宽和可用于流播放的内存量。高速设备应使用较小的缓冲长度，而慢速设备或吞吐量有较大标准差（例如由寻址导致）的设备应使用较大长度。当所有自动流达到它们的目标缓冲长度，而且没有待执行的标准流操作时，I/O 调度程序将闲置。

|  |  |
| --- | --- |
|  | **技巧:** 理想的目标缓冲长度与底层设备传输数据的时间成正比。在合理的条件下，可以尝试先使用足够大的 I/O 内存大小，并指定能够保证 Wwise Profiler 中不出现源干涸通知的最小缓冲长度值。确定后，您就可以继而将 I/O 内存大小降低到峰值占用值。 |

默认值：380 毫秒。

## 并行 I/O 传输的最大数量

[AkDeviceSettings::uMaxConcurrentIO](struct_ak_device_settings_af49f8b3af816b58296e952b20de2d7a3.html#af49f8b3af816b58296e952b20de2d7a3 "Maximum number of transfers that can be sent simultaneously to the Low-Level I/O.") concerns asynchronous low-level devices only. 它是流播放设备在同时并行发布给 Low-Level I/O 传输的最大数量。达到这一极限时，即使流缓冲低于其目标，I/O 线程也将停止向 Low-Level I/O 发布请求。您可以使用此值来安全地分配跟踪各待执行传输所需的静态结构数组。

|  |  |
| --- | --- |
|  | **技巧:** If you specify 1, you get the same behavior as with a synchronous device, with asynchronous handshaking instead. 如果您的 I/O 管理器仅提供异步 API，这可能非常有用。  您也许想将此参数开大，但这样做存在缺点。流播放设备的调度程序会根据检查底层请求时每个流的状态来发布底层请求。如果您让它发送大量请求，并让它们长时间保留在 Low-Level I/O 中，那么期间情况发生改变的可能性较大。例如，流声音可能停止播放或者停止循环。这些情况下，传输将被取消，并且 I/O 数据一旦接收到就会被刷新，这可能导致大量的带宽浪费。  大量的并行请求只可用于吞吐量与请求量不呈线性关系的设备。例如，某些 DMA 控制器可以编程为处理大量传输，但它们的完成时刻通常与编程设定的传输量无关。 |

Default: 8.

## 使用流缓存

[AkDeviceSettings::bUseStreamCache](struct_ak_device_settings_aaa0e8dc2b18f827559aaf8672705dd49.html#aaa0e8dc2b18f827559aaf8672705dd49 "If true, the device attempts to reuse I/O buffers that have already been streamed from disk....") 决定是否启用数据缓存。

流播放设备支持将数据缓存到它们的流播放池中。对内存块执行 I/O 操作时，文件元数据将被附加。如果同一流或内容相同的流需要数据块在差不多在同一位置对应于同一文件的相同位置，则将直接使用原有数据块，从而避免从 Low-Level I/O 传输。

须知，关键数据结构在创建设备时就已经预先分配（从 Stream Manager 内存池中分配）。在运行时用完内存将导致 I/O 线程以高优先级空转，从而对游戏性能带来灾难性的影响。

通过流数据缓存，特定内存块可能同时具有多个引用。内存块引用是预分配关键数据结构的一个例子。

通过调用 `AK::SoundEngine::PinEventInStreamCache()` ，用户可请求某些 Event 将其媒体寄存到流缓存中，以便在需要时以零延迟马上进行播放。若在调用 `AK::SoundEngine::PinEventInStreamCache()` 时数据没有存到缓存中，则将以低优先级自动流方式对数据进行流传输。锁定的每个媒体文件的长度（单位：毫秒）可以使用 Wwise 设计工具中的预读滑块进行自定义。数据会一直保存在内存中，直到用户通过调用 `AK::SoundEngine::UnpinEventInStreamCache()` 释放媒体。

[AkDeviceSettings::bUseStreamCache](struct_ak_device_settings_aaa0e8dc2b18f827559aaf8672705dd49.html#aaa0e8dc2b18f827559aaf8672705dd49 "If true, the device attempts to reuse I/O buffers that have already been streamed from disk....") 指定设备是否应尝试重复使用已从磁盘进行流传输的 IO 缓冲区。这在对较短的循环声音进行流播放时非常有用。缺点是在分配内存时会临时占用大量 CPU 资源，而且 StreamManager 内存池中的内存用量会略高。

默认：false（禁用缓存）。