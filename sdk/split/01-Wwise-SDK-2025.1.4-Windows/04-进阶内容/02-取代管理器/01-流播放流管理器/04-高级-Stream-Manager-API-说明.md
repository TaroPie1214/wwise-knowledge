# 高级 Stream Manager API 说明

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

高级 Stream Manager API 说明

# 简介

Wwise 声音引擎使用 Stream Manager 来加载 SoundBank 和读取流音频文件。如果您还没有 I/O 管理器，还欢应您将它用于所有游戏 I/O。如果您不将它直接当作客户端使用，仅通过实施 Low-Level I/O 挂钩将 Wwise I/O 集成到游戏中，则您可以跳过本章。

# Stream Manager 主要接口

Stream Manager 的主要接口通过用来创建流播放对象的 [AK::IAkStreamMgr](class_a_k_1_1_i_ak_stream_mgr.html) 进行定义。

## Stream Manager 实例化

在使用 Stream Manager 之前，您需要将其实例化。

|  |
| --- |
| **Default Streaming Manager Information**    Stream Manager 实例化与特定实现相关。Audiokinetic 的 Stream Manager 的默认实现函数在 [AkStreamMgrModule.h](_ak_stream_mgr_module_8h.html): [AK::StreamMgr::Create()](namespace_a_k_1_1_stream_mgr_af9d67dd0e502e5603a2921099916e2ab.html#af9d67dd0e502e5603a2921099916e2ab) 中定义。您需要将特定的实现设置传递给它（请参阅 [Audiokinetic Stream Manager 初始化设置](streamingmanager_settings.html) 了解初始化设置的说明）。 |

## 高级流播放设备

|  |
| --- |
| **Default Streaming Manager Information**    在创建和使用流对象之前，您需要创建高级流播放设备，此概念仅针对 Audiokinetic 的 Stream Manager 默认实现。高级流播放设备即为 I/O 调度器，它在自己的线程中运行，将与其相关的流对象集中起来，并向 Low-Level I/O 发送数据传输请求。高级设备通常被简称为设备。游戏使用特定的标志和设置创建若干个设备，最好是在初始化时创建。有关初始化设置的更多详情，请参阅 [Audiokinetic Stream Manager 初始化设置](streamingmanager_settings.html) [一节。AK::StreamMgr::CreateDevice()](namespace_a_k_1_1_stream_mgr_a64a22d377d25137222fbb66ff21965d5.html#a64a22d377d25137222fbb66ff21965d5) 返回设备 ID，出于文件定位和设备分配目的， Low-Level I/O 应保存此设备 ID 。（请参阅 [文件位置解析](streamingmanager_lowlevel.html#streamingmanager_lowlevel_location) 一节了解更多信息。）此设备 ID 必须传递给 [AK::StreamMgr::DestroyDevice()](namespace_a_k_1_1_stream_mgr_a6af0f503def99f59b5ed7c903d919106.html#a6af0f503def99f59b5ed7c903d919106) [才能正确终止设备。跟所有针对特定实现的函数一样，AK::StreamMgr::CreateDevice()](namespace_a_k_1_1_stream_mgr_a64a22d377d25137222fbb66ff21965d5.html#a64a22d377d25137222fbb66ff21965d5) 和 [AK::StreamMgr::DestroyDevice()](namespace_a_k_1_1_stream_mgr_a6af0f503def99f59b5ed7c903d919106.html#a6af0f503def99f59b5ed7c903d919106) 在文件头 [AkStreamMgrModule.h](_ak_stream_mgr_module_8h.html) 中定义。 |

## 创建流

Stream Manager 的主要 API 在很大程度上说是流创建方法的集合。根据文件标识符和设置，它们创建一个流对象并向其返回一个接口，所有流操作都将通过此接口执行。In this API, it is possible to identify a stream file either by file name (string) or by file ID (integer). This choice is wrapped into the structure [AkFileOpenData](struct_ak_file_open_data.html). Only one method should be used to designate a file. If both are used, the string method will be preferred.

|  |  |
| --- | --- |
|  | **备注:** Low-Level I/O 接口的 Open() 方法使用文件标识符来创建文件描述符。 |

除文件标识符外，流创建方法还接受指向包含文件定位标记的 [AkFileSystemFlags](struct_ak_file_system_flags.html "File system flags for file descriptors mapping.") 结构的指针，

|  |
| --- |
| **Default Streaming Manager Information**    并原封不动传递给 Low-Level I/O。请参阅 [SoundBank](streamingmanager_lowlevel.html#streamingmanager_lowlevel_location_soundbanks) 、[流播放音频文件](streamingmanager_lowlevel.html#streamingmanager_lowlevel_location_streamedfiles) 和 [基本文件定位](streamingmanager_lowlevel.html#streamingmanager_lowlevel_default_implementation_walkthrough_file_location) 各节了解有关 [AkFileSystemFlags](struct_ak_file_system_flags.html "File system flags for file descriptors mapping.") 以及声音引擎如何使用它们的更多详情。 |

流创建方法中还有另一个参数：in\_bSyncOpen，当用户（例如声音引擎）需要文件句柄封装在流对象中并在此调用期间打开时，它们将返回 True。如果返回 False，意味着它们允许 Stream Manager 延迟打开文件，文件即有可能被延迟打开。如果延迟打开但打开失败，则 [AK::IAkStdStream::Read()](class_a_k_1_1_i_ak_std_stream_a2b12fb0cd1beb3c1d77c8206a8b5796d.html#a2b12fb0cd1beb3c1d77c8206a8b5796d) 或 [AK::IAkAutoStream::GetBuffer()](class_a_k_1_1_i_ak_auto_stream_aa8197d63b8e758acb075a437103e573c.html#aa8197d63b8e758acb075a437103e573c) 的下一次调用将返回 AK\_Fail，

|  |  |
| --- | --- |
|  | **备注:** 这不是致命错误。对于已经流播放的音频文件，声音引擎返回 False。如果 GetBuffer() 返回 False，则会将视此为 I/O 错误并正常地销毁流。 |

|  |
| --- |
| **Default Streaming Manager Information**    参数 in\_bSyncOpen 直接传递给 Low-Level I/O。请参阅 [延迟打开](streamingmanager_lowlevel.html#streamingmanager_lowlevel_location_deferred_open) 了解有关此标志在 Low-Level I/O 中产生结果的详情。 |

[AK::IAkStreamMgr::CreateStd()](class_a_k_1_1_i_ak_stream_mgr_a1de2a7935a2d3cddb71e7cc7f48effd6.html#a1de2a7935a2d3cddb71e7cc7f48effd6) 创建标准流，而 [AK::IAkStreamMgr::CreateAuto()](class_a_k_1_1_i_ak_stream_mgr_afe30a576bd859ff4e9b60a3f8e1710fb.html#afe30a576bd859ff4e9b60a3f8e1710fb) 创建自动流。下面是这两种流的描述。

## 销毁流

两种流对象均定义有 Destroy() 方法，供您调用来释放流所占用的资源。释放后您将不可再使用此对象。

|  |
| --- |
| **Default Streaming Manager Information**    在默认的 Stream Manager 中，AK::IAkStdStream::Destroy() 和 [AK::IAkAutoStream::Destroy()](class_a_k_1_1_i_ak_auto_stream_a7371eb45a24988fc3d5372bc15c77db7.html#a7371eb45a24988fc3d5372bc15c77db7) 仅用于在流对象上设置标志，实际的销毁操作由 I/O 线程随后执行。I/O 线程被唤醒时，将首先检查所有打开的流，查找下一个要将 I/O 请求发布给 Low-Level I/O 的流，并清理所有废弃流。此时才会释放内存，并调用 [AK::StreamMgr::IAkLowLevelIOHook::Close()](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a7a50a7a5fa624691d7bb7608753dc096.html#a7a50a7a5fa624691d7bb7608753dc096)（其中释放文件句柄）。  预定要销毁的流对象向 I/O 线程发出信号，当 Low-Level I/O 中再也没有等待其执行的 I/O 传输时，就会将它们释放。  如果正在进行流性能分析，I/O 线程将等待监控线程允许，然后再处理流对象。监控线程每 200 毫秒执行一次性能分析过程。 |

# 标准流

调用 [AK::IAkStreamMgr::CreateStd()](class_a_k_1_1_i_ak_stream_mgr_a1de2a7935a2d3cddb71e7cc7f48effd6.html#a1de2a7935a2d3cddb71e7cc7f48effd6) 将创建标准流对象，通过返回的 [AK::IAkStdStream](class_a_k_1_1_i_ak_std_stream.html) 接口可以控制该对象。

## 定义

标准流使用基本的读/写机制来控制 I/O 操作。当调用 [AK::IAkStdStream::Read()](class_a_k_1_1_i_ak_std_stream_a2b12fb0cd1beb3c1d77c8206a8b5796d.html#a2b12fb0cd1beb3c1d77c8206a8b5796d) 或 [AK::IAkStdStream::Write()](class_a_k_1_1_i_ak_std_stream_af983e5aec5edd20b88a6b01e466d8779.html#af983e5aec5edd20b88a6b01e466d8779) 时，I/O 请求将排队进入调度程序，并且其状态将被流设置为 AK\_StmStatusPending. 用户传递请求的传输大小和缓冲区的地址后，其状态将被流设置为 AK\_StmStatusCompleted 或 AK\_StmStatusError。下一操作将在现有位置将加上实际传输大小所得的新位置处执行。要强制使用另一位置，必须在初始化新传输前使用 [AK::IAkStdStream::SetPosition()](class_a_k_1_1_i_ak_std_stream_a5d0c3c6c525a882d89558b1aae485360.html#a5d0c3c6c525a882d89558b1aae485360) 方法。

I/O 操作一次只能执行一个。后续操作需要通过调用 [AK::IAkStdStream::Read()](class_a_k_1_1_i_ak_std_stream_a2b12fb0cd1beb3c1d77c8206a8b5796d.html#a2b12fb0cd1beb3c1d77c8206a8b5796d) 或 [AK::IAkStdStream::Write()](class_a_k_1_1_i_ak_std_stream_af983e5aec5edd20b88a6b01e466d8779.html#af983e5aec5edd20b88a6b01e466d8779) 来显式地初始化。使用完流后，必须调用 [AK::IAkStdStream::Destroy()](class_a_k_1_1_i_ak_std_stream_aaa6bca57f4a01a98dff95f68b1320403.html#aaa6bca57f4a01a98dff95f68b1320403)，接口将变为无效。

|  |
| --- |
| **Default Streaming Manager Information**    读\写调用最终在 Low-Level I/O 中执行 I/O 传输。如果客户端请求的大小大于流播放设备的粒度（AkDeviceSettings::uGranularity），则传输将被拆分。流将保持在 AK\_StmStatusPending 或 AK\_StmStatusIdle 状态，直到整个传输结束或发生错误，或满足文件结束条件。 |

此接口还提供其他方法，包括设置查询、访问当前状态或位置，以及访问供先前操作使用的缓冲区。

## 标准流数据访问机制

标准流操作可以通过两种不同的方式启动：

- 同步：在 `AK::IAkStdStream::Read()` 或 `AK::IAkStdStream::Write()` 的 in\_bWait 参数为 true 时，方法会马上中断流操作，直到完成所有 I/O。
- 异步：在 `AK::IAkStdStream::Read()` 或 `AK::IAkStdStream::Write()` 的 in\_bWait 参数为 false 时，方法会在完成 I/O 前返回结果。这时将异步完成剩余操作。可通过调用 `AK::IAkStdStream::GetStatus()` 来轮询流的状态，直到返回 AK\_StmStatusCompleted。或者，通过调用 `AK::IAkStdStream::WaitForPendingOperation()` 来中断流操作，并等待完成异步任务。对于读取操作，为了安全地访问数据，之后可调用 `AK::IAkStdStream::GetData()` ，或读取初次调用 `AK::IAkStdStream::Read()` 的过程中所提供的缓冲区。

## 创建设置

在创建标准流时，您需要指定打开模式（AkOpenMode）。打开模式指定了流是否可用于读取、写入或者两者均可。显然，对于只为读取而打开的流调用 [AK::IAkStdStream::Write()](class_a_k_1_1_i_ak_std_stream_af983e5aec5edd20b88a6b01e466d8779.html#af983e5aec5edd20b88a6b01e466d8779) 将失败。

您还可以使用 [AK::IAkStdStream::SetStreamName()](class_a_k_1_1_i_ak_std_stream_a95c36cbf662e531c10f90165de1fd576.html#a95c36cbf662e531c10f90165de1fd576) 为流指定名称。字符串复制至流对象中，并可以通过 [AK::IAkStdStream::GetInfo()](class_a_k_1_1_i_ak_std_stream_a744adfcaf87eb5bf4962dbf4556a6201.html#a744adfcaf87eb5bf4962dbf4556a6201) 查询。

|  |
| --- |
| **Default Streaming Manager Information**    流名称就是 Wwise Advanced Profiler 的 Streaming 选项卡中所显示的名称。 |

## 启发式算法

标准流的启发式算法根据每个操作而异。

[AK::IAkStdStream::Read()](class_a_k_1_1_i_ak_std_stream_a2b12fb0cd1beb3c1d77c8206a8b5796d.html#a2b12fb0cd1beb3c1d77c8206a8b5796d) 和 [AK::IAkStdStream::Write()](class_a_k_1_1_i_ak_std_stream_af983e5aec5edd20b88a6b01e466d8779.html#af983e5aec5edd20b88a6b01e466d8779) 需要知道操作的优先级和截止时间（单位：毫秒）。一般而言，Stream Manager 会先处理具有较短截止时间的操作。当应用程序需要的 I/O 带宽超过存储设备能够提供的范围时，将先处理高优先级流。截止时间为零意味着现在就需要数据，因此 I/O 已经迟了。在这种情况下，将先处理它，然后再处理低优先级的其它流。

|  |  |
| --- | --- |
|  | **备注:** 声音引擎的 Bank Manager 使用标准流。它在自己的缓冲区中读取和解析 SoundBank 数据。声音引擎 API 中提供一个方法来指定加载 SoundBank [时的平均吞吐量和优先级：AK::SoundEngine::SetBankLoadIOSettings()](namespace_a_k_1_1_sound_engine_ab8f05d2ee628529bb2bde9dab2d56047.html#ab8f05d2ee628529bb2bde9dab2d56047)。（请参阅 Wwise 声音引擎中的 SoundBank 一节了解更多信息。）Bank Manager 调用 [AK::IAkStdStream::Read()](class_a_k_1_1_i_ak_std_stream_a2b12fb0cd1beb3c1d77c8206a8b5796d.html#a2b12fb0cd1beb3c1d77c8206a8b5796d)，在调用结束时解析数据，然后进行读取。该方法将使用作为参数的优先级，并根据用户指定的吞吐量来计算操作的截止时间：  fDeadline = uBufferSize / fUserSpecifiedThroughput;  标准流操作的截止时间和自动流的平均吞吐量相当于 Stream Manager 的 I/O 调度程序。通过游戏中的音频流和其他流的这一功能，声音引擎用户即可减轻 I/O 的库加载负担。 |

## 常见缺点和其他注意事项

### 块大小

“块大小”是在 Stream Manager 级别对读取和寻址粒度以及缓冲区对齐的底层限制。这些流接口中的 `AK::IAkStdStream::GetBlockSize()` 方法可以查询 Low-Level I/O，向其传递与流相关的文件描述符，并返回给调用方。请参阅 Low-Level I/O 一节了解有关文件描述符和 `AK::StreamMgr::IAkLowLevelIOHook::GetBlockSize()` 方法的更多详情。有些存储设备对数据传输大小有限制。例如，在 Win32 平台上，具有 FILE\_FLAG\_UNBUFFERED 标志的已打开文件所允许的传输大小，是物理设备扇区大小的数倍。如果读取或写入操作请求的传输大小不是块大小的倍数，则操作将失败。查询读取大小是否是 `AK::IAkStdStream::GetBlockSize()` 返回值的倍数应由高级接口用户负责。`AK::IAkStdStream::SetPosition()` 也受相同的限制。但它会自动锁定到块下限，并返回实际的文件位置偏差。

一般而言，游戏是 Stream Manager 的用户。因为游戏也会实现底层 I/O 子模块，所以已经清楚允许使用的传输大小。声音引擎不清楚存储设备限制，因此它总是将标准流读取大小锁定到块大小边界上。

### 当流状态为待定时调用的方法

当流处于 AK\_StmStatusPending 状态时，如果调用 [AK::IAkStdStream::Read()](class_a_k_1_1_i_ak_std_stream_a2b12fb0cd1beb3c1d77c8206a8b5796d.html#a2b12fb0cd1beb3c1d77c8206a8b5796d) 和 [AK::IAkStdStream::Write()](class_a_k_1_1_i_ak_std_stream_af983e5aec5edd20b88a6b01e466d8779.html#af983e5aec5edd20b88a6b01e466d8779)[，操作将失败。AK::IAkStdStream::GetPosition()](namespace_a_k_1_1_sound_engine_1_1_query_a11b05ff925874e08c7a61e42fd77d79e.html#a11b05ff925874e08c7a61e42fd77d79e) 和 [AK::IAkStdStream::SetPosition()](class_a_k_1_1_i_ak_std_stream_a5d0c3c6c525a882d89558b1aae485360.html#a5d0c3c6c525a882d89558b1aae485360) 将产生不确定的结果，因为这些结果可能发生在 I/O 传输结束之前，也可能在结束之后。但它们不会阻塞 I/O。

当传输处于待定状态时，可以使用 [AK::IAkStdStream::Cancel()](class_a_k_1_1_i_ak_std_stream_a12c0a90ec223f7d03d265094b0319c88.html#a12c0a90ec223f7d03d265094b0319c88)，但我们不建议使用它，因为性能将受到影响。此方法向调用方确认没有 I/O 处于待定状态。如果在向 Low-Level I/O 发送请求前执行调用，任务将从队列中移除。但如果请求已发送给 Low-Level I/O，调用方在 I/O 结束前将一直被阻塞。

|  |  |
| --- | --- |
|  | **技巧:** 在销毁流前（AK::IAkStdStream::Destroy()），用户无需显式调用 [AK::IAkStdStream::Cancel()](class_a_k_1_1_i_ak_std_stream_a12c0a90ec223f7d03d265094b0319c88.html#a12c0a90ec223f7d03d265094b0319c88)。然而，为了获得最佳性能，只有当流未处于 AK\_StmStatusPending 状态时用户才应调用 Destroy()。 |

# 自动流

调用 [AK::IAkStreamMgr::CreateAuto()](class_a_k_1_1_i_ak_stream_mgr_afe30a576bd859ff4e9b60a3f8e1710fb.html#afe30a576bd859ff4e9b60a3f8e1710fb) 将创建一个自动流对象，通过返回的 [AK::IAkAutoStream](class_a_k_1_1_i_ak_auto_stream.html) 接口可控制该对象。

## 定义

自动流仅用于输入。它们之所以被称为自动流是因为 I/O 请求将“在后台”发送给 Low-Level I/O，用户无需进行任何显式的函数调用。流内存归 Stream Manager 所有，并通过查询流内存地址来访问流数据。当流内存的区域分配给用户时，该区域将保持锁定状态，直至被显式释放。同时，内部调度程序在未锁定的内存中执行数据传输。在创建时，流处于闲置状态。从用户调用 [AK::IAkAutoStream::Start()](class_a_k_1_1_i_ak_auto_stream_ae9d58aa42a893863f8fe85a5ee45d638.html#ae9d58aa42a893863f8fe85a5ee45d638) 时开始将执行 I/O 请求的自动调度。通过调用 [AK::IAkAutoStream::Stop()](class_a_k_1_1_i_ak_auto_stream_ad1b80ad36a23b15e96f697685f710b1f.html#ad1b80ad36a23b15e96f697685f710b1f) 可以停止或暂停流，而再次调用 [AK::IAkAutoStream::Start()](class_a_k_1_1_i_ak_auto_stream_ae9d58aa42a893863f8fe85a5ee45d638.html#ae9d58aa42a893863f8fe85a5ee45d638) 将使它继续工作。

|  |  |
| --- | --- |
|  | **注意:** 流停止时请勿调用 GetBuffer()。在尝试从流中获取缓冲区之前，应总是调用 [Start()](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_state_a9802053bd44c7926486300763e602293.html#a9802053bd44c7926486300763e602293a681b2db48f90de72b60f64c23e183690 "Start")。 |

通过调用 [AK::IAkAutoStream::GetBuffer()](class_a_k_1_1_i_ak_auto_stream_aa8197d63b8e758acb075a437103e573c.html#aa8197d63b8e758acb075a437103e573c) 可以访问数据。如果已从 Low-Level I/O 中读取数据，此方法将返回 AK\_DataReady、包含该数据的缓冲区的地址及其大小。当不再需要缓冲区时，可以通过调用 [AK::IAkAutoStream::ReleaseBuffer()](class_a_k_1_1_i_ak_auto_stream_a4676200056afb266b730f25d5262d2c8.html#a4676200056afb266b730f25d5262d2c8) 来释放它。于是用户所见的流位置将增加释放缓冲区的大小增量。用户可以通过调用 [AK::IAkAutoStream::SetPosition()](class_a_k_1_1_i_ak_auto_stream_a3bbe9d9fe0f933ee75da2adfbfbc9e38.html#a3bbe9d9fe0f933ee75da2adfbfbc9e38) 来强制使用另外的位置。AK::IAkAutoStream::GetBuffer() 的下一次调用将从该位置开始。

|  |  |
| --- | --- |
|  | **注意:** 更改流位置可能导致一些数据被删除。自动流最适于顺序存取。其中有启发式算法来指定循环，帮助 Stream Manager 高效地管理流内存。有关更多信息，请参阅 [常见缺陷和其他注意事项](streamingmanager_highlevel.html#streamingmanager_highlevel_autostreams_watchout) 一节。 |

|  |  |
| --- | --- |
|  | **注意:** 如果 Low-Level I/O 报告错误，流将进入错误模式。自动流无法从其错误状态中恢复，AK::IAkAutoStream::GetBuffer() 将总是返回 AK\_Fail。 |

## 自动流数据存取机制

自动流中的数据可以采用两种不同的方式进行存取：

- 阻塞方式即 [AK::IAkAutoStream::GetBuffer()](class_a_k_1_1_i_ak_auto_stream_aa8197d63b8e758acb075a437103e573c.html#aa8197d63b8e758acb075a437103e573c)
- 轮询方式即 [AK::IAkAutoStream::GetBuffer()](class_a_k_1_1_i_ak_auto_stream_aa8197d63b8e758acb075a437103e573c.html#aa8197d63b8e758acb075a437103e573c)

[AK::IAkAutoStream::GetBuffer()](class_a_k_1_1_i_ak_auto_stream_aa8197d63b8e758acb075a437103e573c.html#aa8197d63b8e758acb075a437103e573c) 有 4 种可能的返回代码：

- AK\_DataReady
- AK\_NoMoreData
- AK\_NoDataReady
- AK\_Fail

如果用户收到填有数据的缓冲区，则此方法将返回 AK\_DataReady 或 AK\_NoMoreData。如果流缓冲区为空，AK::IAkAutoStream::GetBuffer() 将返回 AK\_NoDataReady，大小为零，缓冲区地址为空。如果 Low-Level I/O 报告错误或者使用无效的参数调用方法，则将返回 AK\_Fail。

如果收到的是文件的最后一个缓冲区，则返回 AK\_NoMoreData 而非 AK\_DataReady。Stream Manager 通过比较当前位置（用户所见位置）和 Low-Level I/O 所提供的文件描述符结构中的文件大小成员，来判断它是否是最后一个缓冲区。此后再调用 [AK::IAkAutoStream::GetBuffer()](class_a_k_1_1_i_ak_auto_stream_aa8197d63b8e758acb075a437103e573c.html#aa8197d63b8e758acb075a437103e573c) 将返回 AK\_NoMoreData，大小为零。

每次调用 [AK::IAkAutoStream::GetBuffer()](class_a_k_1_1_i_ak_auto_stream_aa8197d63b8e758acb075a437103e573c.html#aa8197d63b8e758acb075a437103e573c) 都会提供一个新缓冲区。缓冲区必须通过调用 [AK::IAkAutoStream::ReleaseBuffer()](class_a_k_1_1_i_ak_auto_stream_a4676200056afb266b730f25d5262d2c8.html#a4676200056afb266b730f25d5262d2c8) 来进行显式释放。释放的顺序就是使用 GetBuffer() 接收它们的顺序。释放后，缓冲区的地址将变为无效。当客户端不再持有缓冲区时，ReleaseBuffer() 返回 AK\_Fail，但这不是致命错误。

|  |  |
| --- | --- |
|  | **技巧:** 如果可能，请一次只获取一个缓冲区。这可以为 Stream Manager 提供更多的空间来执行 I/O。一次使用多个缓冲区的策略，一般留给需要访问环形/双缓冲区的硬件或其他接口。如果您打算对流一次使用多个缓冲区，应该传递正确的启发式算法（ [AkAutoStmHeuristics::uMinNumBuffers](struct_ak_auto_stm_heuristics_aeda0fa45777364065a470210b54bffea.html#aeda0fa45777364065a470210b54bffea) ）来进行通知。 |

|  |  |
| --- | --- |
|  | **注意:** 使用自动流时的一个常见错误是忘记调用 ReleaseBuffer()。 |

成功的 GetBuffer() 调用所得的缓冲区大小由 Stream Manager 决定。但它必须是块大小的倍数，除非达到了底层文件的末尾。您还可以使用缓冲限制（请参见 AkAutoStmBufSettings）来强制规定 GetBuffer() 返回的大小，将在创建时传递。

|  |  |
| --- | --- |
|  | **注意:** 注意，强制规定缓冲区大小可能造成性能欠佳，因为可能会浪费流内存或带宽。 另外也可能不支持用户指定的限制。IAkStreamMgr::CreateAuto() 将返回 AK\_Fail。 |

|  |
| --- |
| **Default Streaming Manager Information**    此大小通常为高层设备创建设置中指定的粒度，但流文件结束时例外。 |

### 阻塞

在 in\_bWait 标志设置为 True 的情况下，调用 [AK::IAkAutoStream::GetBuffer()](class_a_k_1_1_i_ak_auto_stream_aa8197d63b8e758acb075a437103e573c.html#aa8197d63b8e758acb075a437103e573c) 将导致用户被阻塞，直至数据准备就绪。因此该方法无法返回 AK\_NoDataReady。如果最后一个缓冲区也已经被获取和释放，此方法将立即返回 AK\_NoMoreData，大小为零。

### 轮询

调用 [AK::IAkAutoStream::GetBuffer()](class_a_k_1_1_i_ak_auto_stream_aa8197d63b8e758acb075a437103e573c.html#aa8197d63b8e758acb075a437103e573c) 时将 in\_bWait 标志设为 False 后，用户可以通过评估返回的代码来尝试获取数据。如果返回的代码是 AK\_NoDataReady，用户应执行其他任务并稍后再试。

## 创建设置

自动流实例化的设置比标准流要多，其中包括缓冲区大小限制和启发式算法。这些设置会帮助 Stream Manager 分配最佳的内存量，并对数据传输请求进行优先级排序。

### 缓冲区限制

有些设置是用户指定的内存相关限制。缓冲区大小可以直接指定。如果您想让 Stream Manager 在限制范围内选择缓冲区大小，可以指定最小的缓冲区或块大小，也可以两者都指定。缓冲区大小将是块大小的倍数。

|  |  |
| --- | --- |
|  | **技巧:** 缓冲区限制是可选的，一般不应使用，这样 Stream Manager 能够最高效地管理流内存。有些平台上，声音引擎使用解码硬件时将用到缓冲区限制。这些解码器一次通常需要访问 2 个缓冲区，有特定的字节对齐方式（块大小）和最小缓冲区大小。 |

|  |
| --- |
| **Default Streaming Manager Information**    当前的实现不允许自定义自动流缓冲区的大小超出设备粒度。（请参阅 [Audiokinetic Stream Manager 初始化设置](streamingmanager_settings.html) 了解有关粒度的更多详情。） |

### 启发式算法

必须提供启发式算来帮助 Stream Manager 执行调度和内存分配。自动流启发式算法是在创建时根据每个流专门指定的，对于确保最佳表现非常重要。它们可随时通过 [AK::IAkAutoStream::GetHeuristics()](class_a_k_1_1_i_ak_auto_stream_a8017b864cb413b545e685b2fa1acfe65.html#a8017b864cb413b545e685b2fa1acfe65) 和 [AK::IAkAutoStream::SetHeuristics()](class_a_k_1_1_i_ak_auto_stream_a0991f4a2b25e6c2fcf5fc4e04cfeaebc.html#a0991f4a2b25e6c2fcf5fc4e04cfeaebc) 来查询和更改。

- 吞吐量：平均吞吐量即决定了 I/O 调度程序的截止时间，因为调度程序知道它有多少数据可供特定流使用。这相当于标准流的各操作专用截止时间启发式。
- 优先级：通常在应用程序所需的 I/O 带宽超出存储设备可提供范围的情况下适用。在这种情况下，Stream Manager 将试图满足优先级更高的流请求。这相当于标准流的各操作专用优先级启发式。
- 循环：您可以在循环流中指定循环位置。这可以帮助 Stream Manager 管理它的内存。在释放循环后，比较好的做法是重新将启发式算法设置为“非循环”（设置 uLoopEnd 为 0）。注意，它只是一个启发式算法：除非客户端调用 [SetPosition()](namespace_a_k_1_1_sound_engine_a789e25bda32d1e11849afb6584942455.html#a789e25bda32d1e11849afb6584942455)，否则不应更改流位置。然而，对于循环启发式算法，意外地更改位置通常会导致数据被刷新。
- uMinClientBuffers：它指示客户端计划同时持有多少个缓冲区。通常同时应至持有一个缓冲区，但有时可能需要同时持有 2 个缓冲区。在这种情况下，请将 uMinClientBuffers 设置为 2。Stream Manager 应尝试使用至少 (uMinClientBuffers + 1) 个缓冲区来对流进行缓冲。注意，为 uMinClientBuffers 指定 0（默认值）相当于 1。

## 常见缺陷和其他注意事项

### 块大小

在选择缓冲区大小前，Stream Manager 总是先向 Low-Level I/O 查询给定文件的块大小，以确保缓冲区大小是块大小的倍数。因此，自动流的用户不必关心底层块大小，除非它们强制流进入到另一个位置。在这种情况下，它们需要考虑从 [AK::IAkAutoStream::GetBlockSize()](class_a_k_1_1_i_ak_auto_stream_a6869aba1d6b9301a3f59468166a8fb7c.html#a6869aba1d6b9301a3f59468166a8fb7c) 获得的块大小或者 [AK::IAkAutoStream::SetPosition()](class_a_k_1_1_i_ak_auto_stream_a3bbe9d9fe0f933ee75da2adfbfbc9e38.html#a3bbe9d9fe0f933ee75da2adfbfbc9e38) 所返回的实际绝对偏置。

### 流位置

流位置是从用户的角度来评估的，可以通过 Get/SetPosition() 方法进行查询和设置。在计算位置时不会考虑从 Low-Level I/O 传输到 Stream Manager 缓冲区的数据。用户释放缓冲区时将对其进行更新。如果调用 [AK::IAkAutoStream::SetPosition()](class_a_k_1_1_i_ak_auto_stream_a3bbe9d9fe0f933ee75da2adfbfbc9e38.html#a3bbe9d9fe0f933ee75da2adfbfbc9e38) 时已有数据从 Low-Level I/O 传出，它们一般会被刷新。

|  |  |
| --- | --- |
|  | **备注:** 用户应尽可能避免调用 [AK::IAkAutoStream::SetPosition()](class_a_k_1_1_i_ak_auto_stream_a3bbe9d9fe0f933ee75da2adfbfbc9e38.html#a3bbe9d9fe0f933ee75da2adfbfbc9e38)。如果必须使用，则应尽早调用。例如，在声音引擎中，当循环声源从 Stream Manager 获取缓冲区时，它会查看其中是否包含循环结尾。如果包含，则立即调用 [AK::IAkAutoStream::SetPosition()](class_a_k_1_1_i_ak_auto_stream_a3bbe9d9fe0f933ee75da2adfbfbc9e38.html#a3bbe9d9fe0f933ee75da2adfbfbc9e38)（即早在 ReleaseBuffer() 之前调用），从而最大限度地降低传输无用数据的风险。另外，指定循环启发式算法可以帮助内部调度程序对 Low-Level I/O 请求做出更好的决策。 |

|  |  |
| --- | --- |
|  | **技巧:** 在锁定或未锁定缓冲区的情况下均可调用 [AK::IAkAutoStream::SetPosition()](class_a_k_1_1_i_ak_auto_stream_a3bbe9d9fe0f933ee75da2adfbfbc9e38.html#a3bbe9d9fe0f933ee75da2adfbfbc9e38)，但建议尽早更改位置，以便最大限度地降低徒劳无功地传输数据的风险。正确地停止流还有助于将带宽浪费最小化。  [AK::IAkAutoStream::SetPosition()](class_a_k_1_1_i_ak_auto_stream_a3bbe9d9fe0f933ee75da2adfbfbc9e38.html#a3bbe9d9fe0f933ee75da2adfbfbc9e38) 不会释放被客户端占据的缓冲区。客户端通过显式调用 ReleaseBuffer() [来决定何时应该释放缓冲区。AK::IAkAutoStream::SetPosition()](namespace_a_k_1_1_sound_engine_a789e25bda32d1e11849afb6584942455.html#a789e25bda32d1e11849afb6584942455) 实际上指示的是对于 GetBuffer() 的**下一次调用**时客户端所期望的位置。  [AK::IAkAutoStream::GetPosition()](class_a_k_1_1_i_ak_auto_stream_ae7fa6bd56c493b906e294618b47be39e.html#ae7fa6bd56c493b906e294618b47be39e) 返回客户端当前占据的第一个缓冲区的位置。如果客户端并未持有缓冲区，它将返回下一次调用 GetBuffer() 时获取的缓冲区位置。 |

[AK::IAkAutoStream::GetBuffer()](class_a_k_1_1_i_ak_auto_stream_aa8197d63b8e758acb075a437103e573c.html#aa8197d63b8e758acb075a437103e573c) 的 AK\_NoMoreData [返回代码是根据流位置来确定的。AK::IAkAutoStream::GetPosition()](namespace_a_k_1_1_sound_engine_1_1_query_a11b05ff925874e08c7a61e42fd77d79e.html#a11b05ff925874e08c7a61e42fd77d79e) 返回的out\_bEndOfStream 可选标志也将绑定到流位置。当且仅当以下条件下，它才会返回 True

- uLoopEnd heuristics 设置为 0（无循环），
- 不再有数据从 Low-Level I/O 传输，
- 用户已经释放其所有缓冲区。

### 阻塞待定底层操作的方法

自动流 API 的设计不会使用户阻塞 Low-Level I/O 的待定事务，除非阻止 [AK::IAkAutoStream::GetBuffer()](class_a_k_1_1_i_ak_auto_stream_aa8197d63b8e758acb075a437103e573c.html#aa8197d63b8e758acb075a437103e573c) 调用。甚至 [AK::IAkAutoStream::Destroy()](class_a_k_1_1_i_ak_auto_stream_a7371eb45a24988fc3d5372bc15c77db7.html#a7371eb45a24988fc3d5372bc15c77db7) 也不会阻塞。通常而言，如果流在销毁时仍在与 Low-Level I/O 交流，它将继续留存于内部，直至 Low-Level I/O 的当前传输结束。

# 覆盖 Stream Manager

要覆盖整个 Stream Manager，游戏必须实现 [IAkStreamMgr.h](_i_ak_stream_mgr_8h.html) 中定义的所有接口。此实现应遵守本节中所述的规则。

您可以将静态库 AkStreamMgr.lib 替换成游戏自己的库。创建函数以及针对实现的其他设置和定义（例如 Low-Level I/O API）位于 [AkStreamMgrModule.h](_ak_stream_mgr_module_8h.html) 中，因此不是 Stream Manager 的组成部分。

## 链接声音引擎

声音引擎通过调用其内联的静态 [AK::IAkStreamMgr::Get()](class_a_k_1_1_i_ak_stream_mgr_ac650db9915bd06d5eebc1852e0d0cd6e.html#ac650db9915bd06d5eebc1852e0d0cd6e) 方法来访问 Stream Manager，该方法将返回指向 [AK::IAkStreamMgr](class_a_k_1_1_i_ak_stream_mgr.html) 接口（它是 [AK::IAkStreamMgr](class_a_k_1_1_i_ak_stream_mgr.html) 的保护成员）的指针。自定义实现只能声明一个变量（AK::IAkStreamMgr::m\_pStreamMgr），链接将自动执行。如果 Stream Manager 和声音引擎没有在同一个可执行文件或 DLL 中链接在一起，则 [AK::IAkStreamMgr::m\_pStreamMgr](class_a_k_1_1_i_ak_stream_mgr_a85c6043c1a45f13b7df2f05729248b1f.html#a85c6043c1a45f13b7df2f05729248b1f) 必须拥有 \_\_dllexport 属性。可以使用 AKSTREAMMGR\_API 宏，并在自定义 Stream Manager 库的编译程序设置中定义 AKSTREAMMGR\_EXPORTS。

## 性能分析

还需要实现性能分析接口，以允许与声音引擎的非 AK\_OPTIMIZED 版本进行链接。此接口一目了然。实现它后即可在 Wwise 中执行性能分析。如果不需要性能分析，AK::IAkStreamMgr::GetStreamMgrProfile() 应返回 NULL，即可使用空代码实现接口。在这种情况下，Wwise 中将不显示任何性能分析信息。

# 代码示例

以下代码用于说明一些注意事项，使用代码比文字更能解释清楚。当您想要更改或不沿用 Stream Manager 时，将尤其有用。此代码有意写得非常复杂，它指出了您应该特别注意的一些问题。

// 注意：为了简明起见，我们假设测试文件小于 4Gb（其位置基于 32 位）。

// 标准流的用法和注意事项。

// 如果测试成功（即如果 Stream Manager 表现正常），则此函数返回 True。

bool BasicStdStreamTest(

const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \* in\_pszFilename

)

{

// 基本的标准流测试。

bool bSuccess = true;

[AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) iCurPosition;

const [AkInt64](_ak_numeral_types_8h_a3f2533eb6fb2011f230af7474daabc6c.html#a3f2533eb6fb2011f230af7474daabc6c) POSITION\_BEGIN = 0;

// 为读取操作创建流对象。

[AK::IAkStdStream](class_a_k_1_1_i_ak_std_stream.html) \* pStream;

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) eResult = [AK::IAkStreamMgr::Get](class_a_k_1_1_i_ak_stream_mgr_ac650db9915bd06d5eebc1852e0d0cd6e.html#ac650db9915bd06d5eebc1852e0d0cd6e)()->[CreateStd](class_a_k_1_1_i_ak_stream_mgr_a1de2a7935a2d3cddb71e7cc7f48effd6.html#a1de2a7935a2d3cddb71e7cc7f48effd6)(

in\_pszFilename, // 应用流标识符（文件名）。

NULL, // 无文件系统标志：我们提供完整路径，无需任何文件位置解析逻辑。

[AK\_OpenModeRead](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7ab35230305828a2d0aee87a3190ff661f), // 创建设置：打开模式。

pStream, // 返回的流接口。

true ); // 需要同步打开文件。

// 检查返回代码。

if ( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

printf( "Failed creating stream.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

// 提供内存。

const int BUFFER\_SIZE = 8192;

unsigned char pBuffer[BUFFER\_SIZE];

// 在尝试读取之前，不知道 Low-Level I/O 模块的用户

// 应确保它们的读取大小符合块大小限制。此测试假定

// BUFFER\_SIZE 是块大小的倍数。如果不是，将不会继续。

if ( BUFFER\_SIZE % pStream->[GetBlockSize](class_a_k_1_1_i_ak_std_stream_a1121f1b371a613e020d38b99e65e7a2b.html#a1121f1b371a613e020d38b99e65e7a2b)() != 0 )

{

printf( "Low-Level storage device requirements are not compatible with this test.\n");

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

//

// 读取缓冲区中的 BUFFER\_SIZE 字节。阻塞读取操作。

//

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uSizeTransferred;

eResult = pStream->[Read](class_a_k_1_1_i_ak_std_stream_a2b12fb0cd1beb3c1d77c8206a8b5796d.html#a2b12fb0cd1beb3c1d77c8206a8b5796d)(

pBuffer,

BUFFER\_SIZE,

true, // 阻塞

[AK\_DEFAULT\_PRIORITY](_ak_constants_8h_ab390e82d48949e194e1a1a24675b067e.html#ab390e82d48949e194e1a1a24675b067e), // 默认优先级。

0, // 截止时间为 0：现在请求数据（当然会延迟）。

uSizeTransferred );

// 检查返回代码。

if ( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

printf( "Read failed.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

// 测试：如果未到达文件末尾，则读取大小应等于请求大小。验证。

bool bReachedEOF;

pStream->[GetPosition](class_a_k_1_1_i_ak_std_stream_a7d43a89fb7bc5db13285a2669ec912fa.html#a7d43a89fb7bc5db13285a2669ec912fa)( &bReachedEOF );

if ( !bReachedEOF &&

uSizeTransferred != BUFFER\_SIZE )

{

// 这不可能发生。

printf( "Inconsistent transfer size.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

// 注：当前流位置应为 BUFFER\_SIZE。为了让此测试正确

// 比较数据，输入文件应足够大。如果已到达文件末尾，会立即离开。

if ( bReachedEOF )

{

printf( "Input file not big enough. Could not complete test.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

//

// 读取缓冲区中的 BUFFER\_SIZE 字节。非阻塞读取。

//

eResult = pStream->[Read](class_a_k_1_1_i_ak_std_stream_a2b12fb0cd1beb3c1d77c8206a8b5796d.html#a2b12fb0cd1beb3c1d77c8206a8b5796d)(

pBuffer,

BUFFER\_SIZE,

true, // 非阻塞

[AK\_DEFAULT\_PRIORITY](_ak_constants_8h_ab390e82d48949e194e1a1a24675b067e.html#ab390e82d48949e194e1a1a24675b067e), // 默认优先级。

0, // 截止时间为 0：现在请求数据（当然会延迟）。

uSizeTransferred );

// 检查代码。

if ( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

printf( "Read failed.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

// 轮询，直至数据准备就绪。

[AkStmStatus](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307) eStatus = pStream->[GetStatus](class_a_k_1_1_i_ak_std_stream_a165ff91b84857e73891f7943261ba275.html#a165ff91b84857e73891f7943261ba275)();

while ( eStatus != [AK\_StmStatusCompleted](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307a4ee943eb5fbd1c15c114a7db3cd9620e) && eStatus != [AK\_StmStatusError](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307acd646559057f6060264897517d7af22e) )

{

// 执行其他操作……

[AKPLATFORM::AkSleep](namespace_a_k_p_l_a_t_f_o_r_m_aacfeaa07eeeea022207bb97991cc6260.html#aacfeaa07eeeea022207bb97991cc6260)(0);

}

// 检查状态。

if ( pStream->[GetStatus](class_a_k_1_1_i_ak_std_stream_a165ff91b84857e73891f7943261ba275.html#a165ff91b84857e73891f7943261ba275)() != [AK\_StmStatusCompleted](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307a4ee943eb5fbd1c15c114a7db3cd9620e) )

{

printf( "Read failed.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

// 再次检查确保未到达 EOF，否则数据比较将失败。

pStream->[GetPosition](class_a_k_1_1_i_ak_std_stream_a7d43a89fb7bc5db13285a2669ec912fa.html#a7d43a89fb7bc5db13285a2669ec912fa)( &bReachedEOF );

if ( bReachedEOF )

{

printf( "Input file not big enough. Could not complete test.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

//

// 设置位置为 ABS\_POSITION（从文件开头起的绝对值），并读取缓冲区中的 BUFFER\_SIZE 字节。

//

[AkInt64](_ak_numeral_types_8h_a3f2533eb6fb2011f230af7474daabc6c.html#a3f2533eb6fb2011f230af7474daabc6c) ABS\_POSITION = 12000;

[AkInt64](_ak_numeral_types_8h_a3f2533eb6fb2011f230af7474daabc6c.html#a3f2533eb6fb2011f230af7474daabc6c) iRealOffset;

eResult = pStream->[SetPosition](class_a_k_1_1_i_ak_std_stream_a5d0c3c6c525a882d89558b1aae485360.html#a5d0c3c6c525a882d89558b1aae485360)(

ABS\_POSITION,

[AK\_MoveBegin](_i_ak_stream_mgr_8h_a61588d0ebdfe1148a6ee6f8304bf4865.html#a61588d0ebdfe1148a6ee6f8304bf4865aaafcaeced22c9ffabc151a3cf0585fee),

&iRealOffset );

// 检查返回代码。

if ( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

printf( "SetPosition failed.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

// 注意：使用返回的实际偏置。如果 Low-Level I/O 指定大于 1 的块大小，

// Stream Manager 将使寻址锁定到下限边界（例如，如果寻址是 9001，而块大小

// 是 2000，则位置应设为 8000，iRealOffset 同样如此）。

printf( "Set position to %u, low-level block size is %u, actual position set to %u\n",

ABS\_POSITION,

pStream->[GetBlockSize](class_a_k_1_1_i_ak_std_stream_a1121f1b371a613e020d38b99e65e7a2b.html#a1121f1b371a613e020d38b99e65e7a2b)(),

iRealOffset );

// 读取。

eResult = pStream->[Read](class_a_k_1_1_i_ak_std_stream_a2b12fb0cd1beb3c1d77c8206a8b5796d.html#a2b12fb0cd1beb3c1d77c8206a8b5796d)(

pBuffer,

BUFFER\_SIZE,

true, // 阻塞

[AK\_DEFAULT\_PRIORITY](_ak_constants_8h_ab390e82d48949e194e1a1a24675b067e.html#ab390e82d48949e194e1a1a24675b067e), // 默认优先级。

0, // 截止时间为 0：现在请求数据（当然会延迟）。

uSizeTransferred );

// 检查返回代码。

if ( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

printf( "Read failed.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

// 再次检查确保未到达 EOF，否则数据比较将失败。

pStream->[GetPosition](class_a_k_1_1_i_ak_std_stream_a7d43a89fb7bc5db13285a2669ec912fa.html#a7d43a89fb7bc5db13285a2669ec912fa)( &bReachedEOF );

if ( bReachedEOF )

{

printf( "Input file not big enough. Could not complete test.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

// 保持当前绝对位置。

iCurPosition = pStream->[GetPosition](class_a_k_1_1_i_ak_std_stream_a7d43a89fb7bc5db13285a2669ec912fa.html#a7d43a89fb7bc5db13285a2669ec912fa)( NULL );

//

// 向后设置位置，相当于当前位置设置 -REL\_POSITION //

[AkInt64](_ak_numeral_types_8h_a3f2533eb6fb2011f230af7474daabc6c.html#a3f2533eb6fb2011f230af7474daabc6c) REL\_POSITION = -8000;

eResult = pStream->[SetPosition](class_a_k_1_1_i_ak_std_stream_a5d0c3c6c525a882d89558b1aae485360.html#a5d0c3c6c525a882d89558b1aae485360)(

REL\_POSITION,

[AK\_MoveCurrent](_i_ak_stream_mgr_8h_a61588d0ebdfe1148a6ee6f8304bf4865.html#a61588d0ebdfe1148a6ee6f8304bf4865ad7036d3c0758b66299e6c1d0e60a14c5),

&iRealOffset );

// Check return code.

if ( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

printf( "SetPosition failed.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

// 注：如果块大小大于 1，则实际绝对移动偏置可以大于 REL\_POSITION

// (iRealOffset <= REL\_POSITION).

// 注：新位置相对于文件开头应大致相隔 ABS\_POSITION+BUFFER\_SIZE+REL\_POSITION

// 字节。

// iCurPosition 包含“实际”ABS\_POSITION，iRealOffset 现在包含“实际”REL\_POSITION，

// 即实际移动偏置。因此，GetPosition() 总是返回绝对位置，

// 应等于 iCurPosition+iRealOffset。

if ( pStream->[GetPosition](class_a_k_1_1_i_ak_std_stream_a7d43a89fb7bc5db13285a2669ec912fa.html#a7d43a89fb7bc5db13285a2669ec912fa)( NULL ) != iCurPosition+iRealOffset )

{

printf( "Wrong stream position." );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

iCurPosition = pStream->[GetPosition](class_a_k_1_1_i_ak_std_stream_a7d43a89fb7bc5db13285a2669ec912fa.html#a7d43a89fb7bc5db13285a2669ec912fa)( NULL );

printf( "Reading from offset %u.\n", iCurPosition );

// 从该位置开始读取。

eResult = pStream->[Read](class_a_k_1_1_i_ak_std_stream_a2b12fb0cd1beb3c1d77c8206a8b5796d.html#a2b12fb0cd1beb3c1d77c8206a8b5796d)(

pBuffer,

BUFFER\_SIZE,

true, // 阻塞

[AK\_DEFAULT\_PRIORITY](_ak_constants_8h_ab390e82d48949e194e1a1a24675b067e.html#ab390e82d48949e194e1a1a24675b067e), // 默认优先级。

0, // 截止时间为 0：现在请求数据（当然会延迟）。

uSizeTransferred );

// 检查返回代码。

if ( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

printf( "Read failed.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

//

// 取消操作

//

// 读取。

eResult = pStream->[Read](class_a_k_1_1_i_ak_std_stream_a2b12fb0cd1beb3c1d77c8206a8b5796d.html#a2b12fb0cd1beb3c1d77c8206a8b5796d)(

pBuffer,

BUFFER\_SIZE,

true, // 阻塞

[AK\_DEFAULT\_PRIORITY](_ak_constants_8h_ab390e82d48949e194e1a1a24675b067e.html#ab390e82d48949e194e1a1a24675b067e), // 默认优先级。

0, // 截止时间为 0：现在请求数据（当然会延迟）。

uSizeTransferred );

// 检查返回代码。

if ( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

printf( "Read failed.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

// 取消。

pStream->[Cancel](class_a_k_1_1_i_ak_std_stream_a12c0a90ec223f7d03d265094b0319c88.html#a12c0a90ec223f7d03d265094b0319c88)();

// 在此，Stream Manager 有时间将请求发送到底层并完成

// （状态将为 AK\_StmStatusCompleted），或者它将从尚未执行的操作队列中移除

//（状态将为 AK\_StmStatusCancelled）。

// 在任一情况下，都要确认流没有尚未执行的操作。

if ( pStream->[GetStatus](class_a_k_1_1_i_ak_std_stream_a165ff91b84857e73891f7943261ba275.html#a165ff91b84857e73891f7943261ba275)() != [AK\_StmStatusCompleted](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307a4ee943eb5fbd1c15c114a7db3cd9620e) &&

pStream->[GetStatus](class_a_k_1_1_i_ak_std_stream_a165ff91b84857e73891f7943261ba275.html#a165ff91b84857e73891f7943261ba275)() != [AK\_StmStatusCancelled](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307a8122c26f72bda0dbe4cbeaa94917f4b0) )

{

printf( "Inconsistent status after operation cancellation.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

//

// 写入。

//

// 读取。

eResult = pStream->[Read](class_a_k_1_1_i_ak_std_stream_a2b12fb0cd1beb3c1d77c8206a8b5796d.html#a2b12fb0cd1beb3c1d77c8206a8b5796d)(

pBuffer,

BUFFER\_SIZE,

true, // 阻塞

[AK\_DEFAULT\_PRIORITY](_ak_constants_8h_ab390e82d48949e194e1a1a24675b067e.html#ab390e82d48949e194e1a1a24675b067e), // 默认优先级。

0, // 截止时间为 0：现在请求数据（当然会延迟）。

uSizeTransferred );

// 检查返回代码。

if ( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

printf( "Read failed.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

// 重新写入另一文件（阻塞）。

// 创建流。

[AK::IAkStdStream](class_a_k_1_1_i_ak_std_stream.html) \* pWrStream;

eResult = [AK::IAkStreamMgr::Get](class_a_k_1_1_i_ak_stream_mgr_ac650db9915bd06d5eebc1852e0d0cd6e.html#ac650db9915bd06d5eebc1852e0d0cd6e)()->[CreateStd](class_a_k_1_1_i_ak_stream_mgr_a1de2a7935a2d3cddb71e7cc7f48effd6.html#a1de2a7935a2d3cddb71e7cc7f48effd6)(

"out.dat",

NULL, // 我们可以使用此变量来告诉 Low-Level I/O，需要在另一

// 存储设备中创建此文件（支持写入的另一个存储设备）。

[AK\_OpenModeReadWrite](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7ab17f6b95edc9ff7cd668878325ffd93a),

pWrStream,

true ); // 需要同步打开文件。

// 检查返回代码。

if ( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

printf( "Failed creating stream for writing.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

eResult = pWrStream->[Write](class_a_k_1_1_i_ak_std_stream_af983e5aec5edd20b88a6b01e466d8779.html#af983e5aec5edd20b88a6b01e466d8779)(

pBuffer,

BUFFER\_SIZE,

true, // 阻塞

[AK\_DEFAULT\_PRIORITY](_ak_constants_8h_ab390e82d48949e194e1a1a24675b067e.html#ab390e82d48949e194e1a1a24675b067e), // 默认优先级。

0, // 截止时间为 0：现在请求数据（当然会延迟）。

uSizeTransferred );

// 检查返回代码。

if ( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) ||

uSizeTransferred != BUFFER\_SIZE )

{

printf( "Write failed.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

// 将位置设置为开头，然后重新从另一个缓冲区中读取文件以对数据进行比较。

eResult = pWrStream->[SetPosition](class_a_k_1_1_i_ak_std_stream_a5d0c3c6c525a882d89558b1aae485360.html#a5d0c3c6c525a882d89558b1aae485360)(

POSITION\_BEGIN,

[AK\_MoveBegin](_i_ak_stream_mgr_8h_a61588d0ebdfe1148a6ee6f8304bf4865.html#a61588d0ebdfe1148a6ee6f8304bf4865aaafcaeced22c9ffabc151a3cf0585fee),

NULL );

if ( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

printf( "SetPosition failed.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

unsigned char pBufferCheck[BUFFER\_SIZE];

eResult = pWrStream->[Read](class_a_k_1_1_i_ak_std_stream_a2b12fb0cd1beb3c1d77c8206a8b5796d.html#a2b12fb0cd1beb3c1d77c8206a8b5796d)(

pBufferCheck,

BUFFER\_SIZE,

true, // 阻塞

[AK\_DEFAULT\_PRIORITY](_ak_constants_8h_ab390e82d48949e194e1a1a24675b067e.html#ab390e82d48949e194e1a1a24675b067e), // 默认优先级。

0, // 截止时间为 0：现在请求数据（当然会延迟）。

uSizeTransferred );

// 检查返回代码。

if ( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) ||

uSizeTransferred != BUFFER\_SIZE )

{

printf( "Read failed.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

// 比较数据。

if ( memcmp( pBuffer, pBufferCheck, uSizeTransferred ) != 0 )

{

printf( "Data read and written do not match.\n" );

bSuccess = false;

goto stdstmbasictest\_cleanup;

}

stdstmbasictest\_cleanup:

// 关闭流。

if ( pStream )

pStream->[Destroy](class_a_k_1_1_i_ak_std_stream_aaa6bca57f4a01a98dff95f68b1320403.html#aaa6bca57f4a01a98dff95f68b1320403)();

if ( pWrStream )

pWrStream->[Destroy](class_a_k_1_1_i_ak_std_stream_aaa6bca57f4a01a98dff95f68b1320403.html#aaa6bca57f4a01a98dff95f68b1320403)();

return bSuccess;

}

// 自动流使用方法和注意事项。

// 如果测试成功（如果 Stream Manager 表现正常），则此函数返回 True。

bool BasicAutoStreamTest(

const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \* in\_pszFilename

)

{

// 创建自动流。

bool bSuccess = true;

[AK::IAkAutoStream](class_a_k_1_1_i_ak_auto_stream.html) \* pStream;

// 设置启发式算法。

[AkAutoStmHeuristics](struct_ak_auto_stm_heuristics.html) heuristics;

heuristics.[fThroughput](struct_ak_auto_stm_heuristics_a4765f706b096765eb25dd6c06073d9af.html#a4765f706b096765eb25dd6c06073d9af) = 1048576; // 1 Mb/s

// 注：由于它是 Stream Manager 中创建的唯一流，因此吞吐量将没有影响。

// 调度程序将总是为 I/O 选择此流。

heuristics.[uLoopStart](struct_ak_auto_stm_heuristics_afe02155d1e487ebba5cf6b467c40f24d.html#afe02155d1e487ebba5cf6b467c40f24d) = 0;

heuristics.[uLoopEnd](struct_ak_auto_stm_heuristics_a378d13e909830ce63e57782d9389506a.html#a378d13e909830ce63e57782d9389506a) = 0; // 不循环。

// 注：循环启发式算法非常重要，即使整个应用程序中只有一条流也是如此，

// 因为它可能改变管理流内存的方式。

heuristics.[priority](struct_ak_auto_stm_heuristics_a574352be21d197e2bbca4e87177a48ab.html#a574352be21d197e2bbca4e87177a48ab) = [AK\_DEFAULT\_PRIORITY](_ak_constants_8h_ab390e82d48949e194e1a1a24675b067e.html#ab390e82d48949e194e1a1a24675b067e);

// 注：优先级也与此无关。然而，您必须指定一个介于 AK\_MIN\_PRIORITY

// 和 AK\_MAX\_PRIORITY 之间（包括两者）的值，否则 Stream Manager 会将其创建设置视为无效。

// 创建流。

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) eResult = [AK::IAkStreamMgr::Get](class_a_k_1_1_i_ak_stream_mgr_ac650db9915bd06d5eebc1852e0d0cd6e.html#ac650db9915bd06d5eebc1852e0d0cd6e)()->[CreateAuto](class_a_k_1_1_i_ak_stream_mgr_afe30a576bd859ff4e9b60a3f8e1710fb.html#afe30a576bd859ff4e9b60a3f8e1710fb)(

in\_pszFilename, // 文件名。

NULL, // 无文件系统标志：我们提供完整路径，不需要文件位置解析逻辑。

heuristics, // 我们的启发式算法。

NULL, // 缓冲限制：无。如果用户不需要，则不应指定用户限制。

pStream, // 返回的流接口。

true ); // 需要同步打开文件。

// 检查返回代码。

if ( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

printf( "Failed creating stream.\n" );

bSuccess = false;

goto autostmbasictest\_cleanup;

}

// 启动流。I/O 调度程序开始考虑此流。

pStream->[Start](class_a_k_1_1_i_ak_auto_stream_ae9d58aa42a893863f8fe85a5ee45d638.html#ae9d58aa42a893863f8fe85a5ee45d638)();

// 获取流大小（通过 GetInfo）。

[AkStreamInfo](struct_ak_stream_info.html) streamInfo;

pStream->[GetInfo](class_a_k_1_1_i_ak_auto_stream_a345fdbb2d4551f048727bc66f58eb80f.html#a345fdbb2d4551f048727bc66f58eb80f)( streamInfo );

// 获取第一个缓冲区。存取将阻塞。

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uBufferSize;

void \* pBuffer;

eResult = pStream->[GetBuffer](class_a_k_1_1_i_ak_auto_stream_aa8197d63b8e758acb075a437103e573c.html#aa8197d63b8e758acb075a437103e573c)(

pBuffer, // 用于获取数据空间的地址。

uBufferSize, // 用于获取数据空间的大小。

true // 阻塞，直至数据准备就绪。

);

// 检查返回代码。

if ( eResult != [AK\_DataReady](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63a42844243c26095d10ade29e0f020ee0f) &&

eResult != [AK\_NoMoreData](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63a94ba10d374d31161770fc490e0245802) )

{

printf( "GetBuffer failed.\n" );

bSuccess = false;

goto autostmbasictest\_cleanup;

}

// 假设我们解析了缓冲区中包含的数据，这提供了文件的相关信息。

// 比如说文件应在位置 10000 和 150000（字节）之间循环。

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uLoopStart = 10000;

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uLoopEnd = 150000;

// 注：为了让此测试正确比较数据，输入文件应大于 uLoopEnd。

if ( ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce))streamInfo.[uSize](struct_ak_stream_info_aa350fbeb216793ac822d5521df98eccf.html#aa350fbeb216793ac822d5521df98eccf) < uLoopEnd )

{

printf( "Input file not big enough. Could not complete test.\n" );

bSuccess = false;

goto autostmbasictest\_cleanup;

}

// 为了使 Stream Manager 发挥最佳性能，应相应地设置启发式算法。

pStream->[GetHeuristics](class_a_k_1_1_i_ak_auto_stream_a8017b864cb413b545e685b2fa1acfe65.html#a8017b864cb413b545e685b2fa1acfe65)( heuristics ); // 注意：在当前情况下，没必要首先获取启发式算法。

heuristics.[uLoopStart](struct_ak_auto_stm_heuristics_afe02155d1e487ebba5cf6b467c40f24d.html#afe02155d1e487ebba5cf6b467c40f24d) = uLoopStart;

heuristics.[uLoopEnd](struct_ak_auto_stm_heuristics_a378d13e909830ce63e57782d9389506a.html#a378d13e909830ce63e57782d9389506a) = uLoopEnd;

pStream->[SetHeuristics](class_a_k_1_1_i_ak_auto_stream_a0991f4a2b25e6c2fcf5fc4e04cfeaebc.html#a0991f4a2b25e6c2fcf5fc4e04cfeaebc)( heuristics );

// 注意：当前流位置是客户端见到的位置。因此它为 0，这是因为

// 尚未释放缓冲区。

if ( pStream->[GetPosition](class_a_k_1_1_i_ak_auto_stream_ae7fa6bd56c493b906e294618b47be39e.html#ae7fa6bd56c493b906e294618b47be39e)( NULL ) != 0 )

{

printf( "Invalid stream position.\n" );

bSuccess = false;

goto autostmbasictest\_cleanup;

}

// 释放缓冲区。

eResult = pStream->[ReleaseBuffer](class_a_k_1_1_i_ak_auto_stream_a4676200056afb266b730f25d5262d2c8.html#a4676200056afb266b730f25d5262d2c8)();

if ( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

printf( "ReleaseBuffer failed.\n" );

bSuccess = false;

goto autostmbasictest\_cleanup;

}

// 注：既然我们已经释放缓冲区，当前流位置应为 uBufferSize。

if ( pStream->[GetPosition](class_a_k_1_1_i_ak_auto_stream_ae7fa6bd56c493b906e294618b47be39e.html#ae7fa6bd56c493b906e294618b47be39e)( NULL ) != uBufferSize )

{

printf( "Invalid stream position.\n" );

bSuccess = false;

goto autostmbasictest\_cleanup;

}

//

// 在以下序列中，Stream Manager 用户将获取并释放缓冲区，直至过了“循环结束”位置。

// 查询位置发生在 GetBuffer() 之后，因此它们将参考缓冲区的开头。

// 用户通过累加流位置和所持缓冲区的大小来“预料”何时通过

// 循环点。。在此时，位置重新设置到循环的开头，

// 更改启发式算法，并读取文件到结束（直至 GetBuffer() 返回 AK\_NoMoreData）。

// 在释放缓冲区后更容易获取位置，但建议您

// 尽早更改位置。Stream Manager 拥有循环启发式算法，但它们的使用

// 与特定实现紧密相关。

//

bool bEOF = false;

bool bDoLoop = true;

while ( !bEOF )

{

// 轮询读取，直至经过位置 uLoopEnd。

eResult = pStream->[GetBuffer](class_a_k_1_1_i_ak_auto_stream_aa8197d63b8e758acb075a437103e573c.html#aa8197d63b8e758acb075a437103e573c)(

pBuffer,

uBufferSize,

false );

// 检查返回代码。

if ( eResult == [AK\_Fail](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63a904c9822fd2d40bb0ea6bfad9ead659b) )

{

assert( !"I/O error" );

return false;

}

else if ( eResult == [AK\_NoDataReady](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63a47f7a12fe3a41a9d52ae25543b92b4de) )

{

printf( "Starving...\n" );

}

else

{

// 文件结束条件。

bEOF = ( eResult == [AK\_NoMoreData](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63a94ba10d374d31161770fc490e0245802) ) && !bDoLoop;

// 处理循环。在第一次调用 SetPosition 后，将 bDoLoop 设为 false

// 以便我们停止循环。

if ( bDoLoop )

{

// 获取当前位置以查看是否已经穿过边界。

// 前面说过，因为 Stream Manager 用户拥有缓冲区，所以 GetPosition() 返回

// 缓冲区开头的位置。将缓冲区大小

// 加到该值上，以获得缓冲区的结束位置。

// 注意：在不调用 GetPosition() 的情况下跟踪位置

// 会更加高效。

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uCurPosition = pStream->[GetPosition](class_a_k_1_1_i_ak_auto_stream_ae7fa6bd56c493b906e294618b47be39e.html#ae7fa6bd56c493b906e294618b47be39e)( NULL );

if ( ( uCurPosition + uBufferSize ) > uLoopEnd )

{

// 已经过循环结尾。

// 将位置设置为循环开头。

[AkInt64](_ak_numeral_types_8h_a3f2533eb6fb2011f230af7474daabc6c.html#a3f2533eb6fb2011f230af7474daabc6c) iLoopStart;

iLoopStart.HighPart = 0;

iLoopStart.LowPart = uLoopStart;

[AkInt64](_ak_numeral_types_8h_a3f2533eb6fb2011f230af7474daabc6c.html#a3f2533eb6fb2011f230af7474daabc6c) iRealOffset;

eResult = pStream->[SetPosition](class_a_k_1_1_i_ak_auto_stream_a3bbe9d9fe0f933ee75da2adfbfbc9e38.html#a3bbe9d9fe0f933ee75da2adfbfbc9e38)(

iLoopStart,

[AK\_MoveBegin](_i_ak_stream_mgr_8h_a61588d0ebdfe1148a6ee6f8304bf4865.html#a61588d0ebdfe1148a6ee6f8304bf4865aaafcaeced22c9ffabc151a3cf0585fee),

&iRealOffset );

if ( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

printf( "SetPosition failed.\n" );

bSuccess = false;

goto autostmbasictest\_cleanup;

}

// 注：由于我们尚未释放缓冲区，因此 GetPosition() 仍应返回缓冲区的

// 开始位置。

// 请验证这一点。

if ( pStream->[GetPosition](class_a_k_1_1_i_ak_auto_stream_ae7fa6bd56c493b906e294618b47be39e.html#ae7fa6bd56c493b906e294618b47be39e)( NULL ) != uCurPosition )

{

printf( "Invalid position returned.\n" );

bSuccess = false;

goto autostmbasictest\_cleanup;

}

// 注意：uLoopStart 位置不会直接与该流的底层 IO

// 块大小对齐。Stream Manager 的用户负责处理此限制。

// 在此，如果 iRealOffset 不为 0，则它将小于被请求的位置。

// Stream Manager 用户可将校正值存储在本地变量中。

// 既然已经设置位置，缓冲区的下一次存取将在循环的开头

// （减去校正值）。

// 为了发挥最佳性能，可立即更改循环启发式值，因为

// 将不再出现循环。

heuristics.[uLoopStart](struct_ak_auto_stm_heuristics_afe02155d1e487ebba5cf6b467c40f24d.html#afe02155d1e487ebba5cf6b467c40f24d) = 0;

heuristics.[uLoopEnd](struct_ak_auto_stm_heuristics_a378d13e909830ce63e57782d9389506a.html#a378d13e909830ce63e57782d9389506a) = 0; // 0：不再循环。

pStream->[SetHeuristics](class_a_k_1_1_i_ak_auto_stream_a0991f4a2b25e6c2fcf5fc4e04cfeaebc.html#a0991f4a2b25e6c2fcf5fc4e04cfeaebc)( heuristics );

// 停止循环。

bDoLoop = false;

}

}

eResult = pStream->[ReleaseBuffer](class_a_k_1_1_i_ak_auto_stream_a4676200056afb266b730f25d5262d2c8.html#a4676200056afb266b730f25d5262d2c8)();

if ( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

printf( "ReleaseBuffer failed.\n" );

bSuccess = false;

goto autostmbasictest\_cleanup;

}

}

// 模拟用户吞吐量。等待时间等于缓冲区大小除以吞吐量。

//AKPLATFORM::AkSleep( DWORD( 1000\*uBufferSize / heuristics.fThroughput ) );

[AKPLATFORM::AkSleep](namespace_a_k_p_l_a_t_f_o_r_m_aacfeaa07eeeea022207bb97991cc6260.html#aacfeaa07eeeea022207bb97991cc6260)( 0 );

}

autostmbasictest\_cleanup:

if ( pStream )

pStream->[Destroy](class_a_k_1_1_i_ak_auto_stream_a7371eb45a24988fc3d5372bc15c77db7.html#a7371eb45a24988fc3d5372bc15c77db7)();

return bSuccess;

}

[AK::IAkStreamMgr::Get](class_a_k_1_1_i_ak_stream_mgr_ac650db9915bd06d5eebc1852e0d0cd6e.html#ac650db9915bd06d5eebc1852e0d0cd6e)

static IAkStreamMgr \* Get()

**Definition:** [IAkStreamMgr.h:698](_i_ak_stream_mgr_8h_source.html#l00698)

[AkAutoStmHeuristics::uLoopEnd](struct_ak_auto_stm_heuristics_a378d13e909830ce63e57782d9389506a.html#a378d13e909830ce63e57782d9389506a)

AkUInt64 uLoopEnd

Set to the end of loop (byte offset from the beginning of the stream) for streams that loop,...

**Definition:** [IAkStreamMgr.h:98](_i_ak_stream_mgr_8h_source.html#l00098)

[AK::IAkAutoStream::GetPosition](class_a_k_1_1_i_ak_auto_stream_ae7fa6bd56c493b906e294618b47be39e.html#ae7fa6bd56c493b906e294618b47be39e)

virtual AkUInt64 GetPosition(bool \*out\_pbEndOfStream)=0

[AK::IAkStreamMgr::CreateStd](class_a_k_1_1_i_ak_stream_mgr_a1de2a7935a2d3cddb71e7cc7f48effd6.html#a1de2a7935a2d3cddb71e7cc7f48effd6)

virtual AKRESULT CreateStd(const AkFileOpenData &in\_FileOpen, IAkStdStream \*&out\_pStream, bool in\_bSyncOpen)=0

[AK\_DataReady](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63a42844243c26095d10ade29e0f020ee0f)

@ AK\_DataReady

The provider has available data.

**Definition:** [AkEnums.h:60](_ak_enums_8h_source.html#l00060)

[AK::IAkAutoStream::ReleaseBuffer](class_a_k_1_1_i_ak_auto_stream_a4676200056afb266b730f25d5262d2c8.html#a4676200056afb266b730f25d5262d2c8)

virtual AKRESULT ReleaseBuffer()=0

[AK::IAkAutoStream::GetInfo](class_a_k_1_1_i_ak_auto_stream_a345fdbb2d4551f048727bc66f58eb80f.html#a345fdbb2d4551f048727bc66f58eb80f)

virtual void GetInfo(AkStreamInfo &out\_info)=0

[AK::IAkStdStream::GetBlockSize](class_a_k_1_1_i_ak_std_stream_a1121f1b371a613e020d38b99e65e7a2b.html#a1121f1b371a613e020d38b99e65e7a2b)

virtual AkUInt32 GetBlockSize()=0

[AK\_OpenModeReadWrite](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7ab17f6b95edc9ff7cd668878325ffd93a)

@ AK\_OpenModeReadWrite

Read and write access

**Definition:** [IAkStreamMgr.h:77](_i_ak_stream_mgr_8h_source.html#l00078)

[AK\_OpenModeRead](_i_ak_stream_mgr_8h_afb72442488d89ecc645c457ff48a90b7.html#afb72442488d89ecc645c457ff48a90b7ab35230305828a2d0aee87a3190ff661f)

@ AK\_OpenModeRead

Read-only access

**Definition:** [IAkStreamMgr.h:74](_i_ak_stream_mgr_8h_source.html#l00074)

[AK::IAkStdStream::GetStatus](class_a_k_1_1_i_ak_std_stream_a165ff91b84857e73891f7943261ba275.html#a165ff91b84857e73891f7943261ba275)

virtual AkStmStatus GetStatus()=0

[AK::IAkStdStream::Read](class_a_k_1_1_i_ak_std_stream_a2b12fb0cd1beb3c1d77c8206a8b5796d.html#a2b12fb0cd1beb3c1d77c8206a8b5796d)

virtual AKRESULT Read(void \*in\_pBuffer, AkUInt32 in\_uReqSize, bool in\_bWait, AkPriority in\_priority, AkReal32 in\_fDeadline, AkUInt32 &out\_uSize)=0

[AK\_MoveBegin](_i_ak_stream_mgr_8h_a61588d0ebdfe1148a6ee6f8304bf4865.html#a61588d0ebdfe1148a6ee6f8304bf4865aaafcaeced22c9ffabc151a3cf0585fee)

@ AK\_MoveBegin

Move offset from the start of the stream

**Definition:** [IAkStreamMgr.h:66](_i_ak_stream_mgr_8h_source.html#l00066)

[AK\_NoMoreData](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63a94ba10d374d31161770fc490e0245802)

@ AK\_NoMoreData

No more data is available from the source.

**Definition:** [AkEnums.h:45](_ak_enums_8h_source.html#l00045)

[AK\_DEFAULT\_PRIORITY](_ak_constants_8h_ab390e82d48949e194e1a1a24675b067e.html#ab390e82d48949e194e1a1a24675b067e)

static const AkPriority AK\_DEFAULT\_PRIORITY

Default sound / I/O priority

**Definition:** [AkConstants.h:55](_ak_constants_8h_source.html#l00055)

[AK::IAkAutoStream::SetHeuristics](class_a_k_1_1_i_ak_auto_stream_a0991f4a2b25e6c2fcf5fc4e04cfeaebc.html#a0991f4a2b25e6c2fcf5fc4e04cfeaebc)

virtual AKRESULT SetHeuristics(const AkAutoStmHeuristics &in\_heuristics)=0

[AkAutoStmHeuristics::uLoopStart](struct_ak_auto_stm_heuristics_afe02155d1e487ebba5cf6b467c40f24d.html#afe02155d1e487ebba5cf6b467c40f24d)

AkUInt64 uLoopStart

Set to the start of loop (byte offset from the beginning of the stream) for streams that loop,...

**Definition:** [IAkStreamMgr.h:97](_i_ak_stream_mgr_8h_source.html#l00097)

[AkAutoStmHeuristics::fThroughput](struct_ak_auto_stm_heuristics_a4765f706b096765eb25dd6c06073d9af.html#a4765f706b096765eb25dd6c06073d9af)

AkReal32 fThroughput

Average throughput in bytes/ms

**Definition:** [IAkStreamMgr.h:96](_i_ak_stream_mgr_8h_source.html#l00096)

[AkStreamInfo](struct_ak_stream_info.html)

**Definition:** [IAkStreamMgr.h:85](_i_ak_stream_mgr_8h_source.html#l00084)

[AK\_MoveCurrent](_i_ak_stream_mgr_8h_a61588d0ebdfe1148a6ee6f8304bf4865.html#a61588d0ebdfe1148a6ee6f8304bf4865ad7036d3c0758b66299e6c1d0e60a14c5)

@ AK\_MoveCurrent

Move offset from the current stream position

**Definition:** [IAkStreamMgr.h:67](_i_ak_stream_mgr_8h_source.html#l00067)

[AKPLATFORM::AkSleep](namespace_a_k_p_l_a_t_f_o_r_m_aacfeaa07eeeea022207bb97991cc6260.html#aacfeaa07eeeea022207bb97991cc6260)

void AkSleep(AkUInt32 in\_ulMilliseconds)

[AK\_Fail](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63a904c9822fd2d40bb0ea6bfad9ead659b)

@ AK\_Fail

The operation failed.

**Definition:** [AkEnums.h:35](_ak_enums_8h_source.html#l00035)

[AK::IAkStdStream::Destroy](class_a_k_1_1_i_ak_std_stream_aaa6bca57f4a01a98dff95f68b1320403.html#aaa6bca57f4a01a98dff95f68b1320403)

virtual void Destroy()=0

[AK::IAkAutoStream::GetBuffer](class_a_k_1_1_i_ak_auto_stream_aa8197d63b8e758acb075a437103e573c.html#aa8197d63b8e758acb075a437103e573c)

virtual AKRESULT GetBuffer(void \*&out\_pBuffer, AkUInt32 &out\_uSize, bool in\_bWait)=0

[AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664)

wchar\_t AkOSChar

Generic character string

**Definition:** [AkTypes.h:122](_platforms_2_windows_2_ak_types_8h_source.html#l00122)

[AK::IAkAutoStream::GetHeuristics](class_a_k_1_1_i_ak_auto_stream_a8017b864cb413b545e685b2fa1acfe65.html#a8017b864cb413b545e685b2fa1acfe65)

virtual void GetHeuristics(AkAutoStmHeuristics &out\_heuristics)=0

[AkInt64](_ak_numeral_types_8h_a3f2533eb6fb2011f230af7474daabc6c.html#a3f2533eb6fb2011f230af7474daabc6c)

int64\_t AkInt64

Signed 64-bit integer

**Definition:** [AkNumeralTypes.h:41](_ak_numeral_types_8h_source.html#l00041)

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63)

AKRESULT

**Definition:** [AkEnums.h:32](_ak_enums_8h_source.html#l00031)

[AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec)

uint64\_t AkUInt64

Unsigned 64-bit integer

**Definition:** [AkNumeralTypes.h:36](_ak_numeral_types_8h_source.html#l00036)

[AK\_StmStatusCompleted](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307a4ee943eb5fbd1c15c114a7db3cd9620e)

@ AK\_StmStatusCompleted

Operation completed / Automatic stream reached end

**Definition:** [IAkStreamMgr.h:54](_i_ak_stream_mgr_8h_source.html#l00054)

[AkStmStatus](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307)

AkStmStatus

Stream status.

**Definition:** [IAkStreamMgr.h:52](_i_ak_stream_mgr_8h_source.html#l00051)

[AK::IAkAutoStream](class_a_k_1_1_i_ak_auto_stream.html)

**Definition:** [IAkStreamMgr.h:522](_i_ak_stream_mgr_8h_source.html#l00521)

[AkStreamInfo::uSize](struct_ak_stream_info_aa350fbeb216793ac822d5521df98eccf.html#aa350fbeb216793ac822d5521df98eccf)

AkUInt64 uSize

Total stream/file size in bytes

**Definition:** [IAkStreamMgr.h:88](_i_ak_stream_mgr_8h_source.html#l00088)

[AK\_NoDataReady](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63a47f7a12fe3a41a9d52ae25543b92b4de)

@ AK\_NoDataReady

The provider does not have available data.

**Definition:** [AkEnums.h:61](_ak_enums_8h_source.html#l00061)

[AK::IAkAutoStream::Start](class_a_k_1_1_i_ak_auto_stream_ae9d58aa42a893863f8fe85a5ee45d638.html#ae9d58aa42a893863f8fe85a5ee45d638)

virtual AKRESULT Start()=0

[AK::IAkStdStream::SetPosition](class_a_k_1_1_i_ak_std_stream_a5d0c3c6c525a882d89558b1aae485360.html#a5d0c3c6c525a882d89558b1aae485360)

virtual AKRESULT SetPosition(AkInt64 in\_iMoveOffset, AkMoveMethod in\_eMoveMethod)=0

[AK::IAkAutoStream::SetPosition](class_a_k_1_1_i_ak_auto_stream_a3bbe9d9fe0f933ee75da2adfbfbc9e38.html#a3bbe9d9fe0f933ee75da2adfbfbc9e38)

virtual AKRESULT SetPosition(AkInt64 in\_iMoveOffset, AkMoveMethod in\_eMoveMethod)=0

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)

uint32\_t AkUInt32

Unsigned 32-bit integer

**Definition:** [AkNumeralTypes.h:35](_ak_numeral_types_8h_source.html#l00035)

[AK\_StmStatusError](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307acd646559057f6060264897517d7af22e)

@ AK\_StmStatusError

The low-level I/O reported an error

**Definition:** [IAkStreamMgr.h:57](_i_ak_stream_mgr_8h_source.html#l00058)

[AK::IAkStreamMgr::CreateAuto](class_a_k_1_1_i_ak_stream_mgr_afe30a576bd859ff4e9b60a3f8e1710fb.html#afe30a576bd859ff4e9b60a3f8e1710fb)

virtual AKRESULT CreateAuto(const AkFileOpenData &in\_FileOpen, const AkAutoStmHeuristics &in\_heuristics, AkAutoStmBufSettings \*in\_pBufferSettings, IAkAutoStream \*&out\_pStream, bool in\_bSyncOpen, bool in\_bCaching=false)=0

[AK::IAkAutoStream::Destroy](class_a_k_1_1_i_ak_auto_stream_a7371eb45a24988fc3d5372bc15c77db7.html#a7371eb45a24988fc3d5372bc15c77db7)

virtual void Destroy()=0

[AkAutoStmHeuristics::priority](struct_ak_auto_stm_heuristics_a574352be21d197e2bbca4e87177a48ab.html#a574352be21d197e2bbca4e87177a48ab)

AkPriority priority

The stream priority. it should be between AK\_MIN\_PRIORITY and AK\_MAX\_PRIORITY (included).

**Definition:** [IAkStreamMgr.h:103](_i_ak_stream_mgr_8h_source.html#l00103)

[AK::IAkStdStream](class_a_k_1_1_i_ak_std_stream.html)

**Definition:** [IAkStreamMgr.h:384](_i_ak_stream_mgr_8h_source.html#l00383)

[AK::IAkStdStream::Cancel](class_a_k_1_1_i_ak_std_stream_a12c0a90ec223f7d03d265094b0319c88.html#a12c0a90ec223f7d03d265094b0319c88)

virtual void Cancel()=0

[AK::IAkStdStream::Write](class_a_k_1_1_i_ak_std_stream_af983e5aec5edd20b88a6b01e466d8779.html#af983e5aec5edd20b88a6b01e466d8779)

virtual AKRESULT Write(void \*in\_pBuffer, AkUInt32 in\_uReqSize, bool in\_bWait, AkPriority in\_priority, AkReal32 in\_fDeadline, AkUInt32 &out\_uSize)=0

[AkAutoStmHeuristics](struct_ak_auto_stm_heuristics.html)

Automatic streams heuristics.

**Definition:** [IAkStreamMgr.h:95](_i_ak_stream_mgr_8h_source.html#l00094)

[AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e)

@ AK\_Success

The operation was successful.

**Definition:** [AkEnums.h:34](_ak_enums_8h_source.html#l00034)

[AK::IAkStdStream::GetPosition](class_a_k_1_1_i_ak_std_stream_a7d43a89fb7bc5db13285a2669ec912fa.html#a7d43a89fb7bc5db13285a2669ec912fa)

virtual AkUInt64 GetPosition(bool \*out\_pbEndOfStream)=0

[AK\_StmStatusCancelled](_i_ak_stream_mgr_8h_ae8711a0190f80248b6e59f1b17f64307.html#ae8711a0190f80248b6e59f1b17f64307a8122c26f72bda0dbe4cbeaa94917f4b0)

@ AK\_StmStatusCancelled

Operation cancelled

**Definition:** [IAkStreamMgr.h:56](_i_ak_stream_mgr_8h_source.html#l00056)