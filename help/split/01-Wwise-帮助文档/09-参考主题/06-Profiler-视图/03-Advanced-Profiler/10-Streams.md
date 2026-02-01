# Streams

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > [Advanced Profiler](00-Advanced-Profiler.md) > Streams

### Streams

Advanced Profiler — Stream 选项卡显示有关 Wwise 声音引擎如何管理各路流播放的信息。有关 Wwise 中 I/O 管理的详细信息，请参阅 SDK 文档的“流播放/流管理器”章节。

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Device Name | 设备名称。流播放所在的设备名称。从您实现的  [`IAkLowLevelIOHook::GetDeviceDesc()`](https://www.audiokinetic.com/library/?source=SDK&id=class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a06860cb1211c2ebd5c49f4429cc66a0b.html)中返回的字符串。 |
| Stream Name | 播放流的名称。通过设计工具播放时，流名称是流播放音频文件的完整文件路径。在游戏中播放时，它是音频源的名称。 |
| Priority | 播放流的优先级。在不只一条播放流等待响应时，优先级能够影响计划程序服务流播放的顺序。 |
| Tgt. Buffer Size | 目标缓冲区长度。是由代码中指定的流播放设备的目标缓冲区长度（ [AkDeviceSettings::fTargetAutoStmBufferLength](https://www.audiokinetic.com/library/?source=SDK&id=struct_ak_device_settings_af396c1626da7df1bbb6d9129e132b02f.html) ，以毫秒为单位）乘以流播放的预期吞吐量（以每秒字节数为单位）来计算得到的。在流播放声音的缓冲区低于目标缓冲区长度时，这向流播放设备表明需要更多的 I/O 数据。在流播放声音超过目标缓冲区长度时，该流会空闲。 |
| Ref. Memory | 流播放引用的内存量。它不包含用于 I/O 传输的内存。它可视为衡量在任一时刻流播放送到声音引擎的数据量。例如，如果某播放流整个展现出 “Buffering Status”（缓冲状态）却只引用了 0 字节内存，则这也就是说，它的所有 I/O 传输已被调度，但一条也没有完成，进而导致流的匮乏。由于 I/O 内存池被拆分为大小相等的块 （在 [AkDeviceSettings::uGranularity](https://www.audiokinetic.com/library/?source=SDK&id=struct_ak_device_data_a73ceca6480ceffa50466df30b5d2120f.html) 中指定），因此引用的内存量可能会大于实际的有效数据量。例如，这些块之一包含文件的最后几个字节。当为某个指定设备启用数据缓存时，其所有播放流引用的内存总和可能超过其流播放 I/O 池大小，因为这些播放流中的某些流引用了相同的内存。 |
| Buffering Status | 缓冲状态。流播放逼近其目标缓冲区程度的图形化表示。  状态栏有可能显示为两种颜色：  - **灰色**：表示已经缓冲的请求的数据部分。 - **橙色（Classic 主题下为蓝色）**：表示尚未缓冲的请求的数据部分。其中包括 I/O 传输已经安排但尚未完成处理的数据。  在没有请求任何数据时，状态栏显示空白。  若整个状态栏显示为灰色，则表示播放流的缓冲达到目标，播放流变为空闲状态。随着声音引擎不断使用来自播放流的数据，缓冲区长度逐渐缩短，使其降到目标以下。此时，播放流会请求获取更多数据。若缓冲区没有恢复到目标长度，则状态栏变为橙色（Classic 主题下为蓝色）。  状态栏的颜色取决于性能分析器最后采样时播放流的瞬时状态。下图举例展示了部分为灰色、部分为橙色的状态栏。不过，对于大多数现代数据存储设备，状态栏在全灰色和全橙色（或全蓝色）之间的过渡非常快，前后往往只有一帧的时间。因此，大部分情况下看到的状态栏都只是其中一种颜色。 |
| File Size | 文件大小。采用流播放的文件大小。 |
| File Position | 文件位置。表明文件内流播放位置的图形化表示。 |
| Total Bandwidth | 总带宽。文件在上一个性能分析帧中的流播放速率。此值会考虑所有传输，包括从 Stream Manager 缓存发生的传输。 |
| Bandwidth (Low-Level) | 总带宽。文件在上一个性能分析帧中的流播放速率。底层流带宽。与 Total Bandwidth 字段不同，此字段值会考虑在底层设备内发生的传输。此值始终低于或等于 Total Bandwidth。 |
| Est. Throughput | 估计吞吐量。播放流的估计吞吐量。声音引擎根据流播放的编码格式和声道数来估计引擎处理来自该流的数据的速度。它会将此值作为启发值向播放流推送，流播放将使用该值来确定其目标缓冲长度（缓冲区大小）。 |
| Active | 活跃。如果流播放在上一个性能分析帧中至少处于活跃状态一次，则指示 **True**。如果播放流尚未达到目标缓冲或正在等待至少一条 I/O 传输完成，则该流处于活跃状态。 |

**相关主题**

- [“连接至本地/远程游戏系统”一节](../../../07-完善工程/06-性能分析/06-连接至本地远程游戏系统.md "连接至本地/远程游戏系统")
- [“从声音引擎捕获数据”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/00-从声音引擎捕获数据.md "从声音引擎捕获数据")
- [“使用 Performance Monitor 进行监控和故障排查”一节](../../../07-完善工程/06-性能分析/09-使用-Performance-Monitor-进行监控和故障排查.md "使用 Performance Monitor 进行监控和故障排查")

---