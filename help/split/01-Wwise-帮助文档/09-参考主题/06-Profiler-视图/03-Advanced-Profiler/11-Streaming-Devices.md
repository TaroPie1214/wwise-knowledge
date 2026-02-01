# Streaming Devices

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > [Advanced Profiler](00-Advanced-Profiler.md) > Streaming Devices

### Streaming Devices

流播放设备。Advanced Profiler — Streaming Device 选项卡显示有关各个由 Wwise 声音引擎管理的流播放设备的信息。有关 Wwise 中 I/O 管理的详细信息，请参阅 SDK 文档的 [流播放/流管理器](https://www.audiokinetic.com/library/?source=SDK&id=streamingdevicemanager.html)章节。

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Device Name | 设备的名称。此字符串是通过您实现的 IAkLowLevelIOHook::GetDeviceDesc() 函数返回的。 |
| IO Pool Size | I/O 池大小。为此设备的流播放 I/O 内存池预留的内存量。预留大小是在创建流播放设备时设置的，设置是通过  [`AkDeviceSettings::uIOMemorySize`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_device_settings_a75893592924a59881fe2cbca4e4ddd04.html) 进行的。 |
| Ratio Used | 占用。已占用内存量与流播放 I/O 池中预留总内存相比的图形化表示。深灰条表示引用的缓存（它无法被丢弃），而浅灰条表示未引用的缓存（它可被丢弃）。 |
| Ref'd Mem. | 已引用内存。当前用在流播放 I/O 内存池中的内存量，因为它会被流播放引用或被固定到缓存中（pin-to-cache）。 |
| Peak Ref'd Mem. | 峰值引用内存。流播放 I/O 内存池中曾经使用的最大引用内存量（光标所指时间之前任意时刻）。  该值可有助于您确定内存占用量何时逼近预留的内存上限。  与其它内存池不同，不时达到流播放 I/O 池上限是可以接受的。最显著的结果是源匮乏（source starvation）。但是，如果这些播放流需要的内存量大大超过可用内存，则这些流可能会停滞非常长的时间。 |
| Cached Memory | 缓存。缓存中未引用的内存，也就是说该内存既没有用于流播放，也没有被固定到缓冲区中，该内存在流播放 I/O 内存池中。 |
| Pinned to Cache | 固定到缓存。已经固定（预留）的流播放 I/O 内存池缓存。 |
| Allocs | 分配数。自流播放 I/O 内存池创建以来执行的分配数。  此数字改变时，它表明流播放 I/O 内存池当前正在分配内存。 |
| Frees | 释放数。自流播放 I/O 内存池创建以来执行的释放数。  若此数值改变，则表示流播放 I/O 内存池当前正在释放内存。 |
| Cur. Allocs | 当前分配数。流播放 I/O 内存池中当前分配的内存块数。Current Alloc 值是通过 Alloc 的数目减去 Free 的数目得到的。  若此数值改变，则表示内存池当前正在分配或释放内存。 |
| Cache Efficiency | 缓存效率。数据缓存效率的估计值。缓存效率是从性能分析会话期间底层带宽和总带宽之间的平均差异计算得出（请参见下方的“Bandwidth (Low-Level)”和“Total Bandwidth”）。  您可以针对给定设备在流播放 I/O 内存池中启用数据缓存（参阅 SDK 文档中的 `AkDeviceSettings::bUseStreamCache`）。在准备数据传输之前，流播放设备会在池中搜索对应于此文件的数据。如果找到此数据，则会直接使用此数据并且不会将任何 I/O 传输请求发送至Low-level I/O。 |
| Granularity | 设备的 Granularity（ `AkDeviceSettings::uGranularity` ），它表示流播放 I/O 池中每个内存块的大小，也定义了向 Low-level I/O 请求的 I/O 传输大小。 |
| Active Streams | 活跃流。在任一时刻此设备中活跃播放流的数量。如果播放流尚未达到目标缓冲或正在等待至少一条 I/O 传输完成，则该流处于活跃状态。 |
| Total Bandwidth | 总带宽。此设备中的所有播放流在上一个性能分析帧中的数据传输速率。此值会考虑所有传输，包括从 Stream Manager 缓存发生的传输。 |
| Bandwidth (Low-Level) | 底层带宽。此设备中的所有播放流在上一个性能分析帧中的文件传输速率。底层流带宽。与 Total Bandwidth 字段不同，此字段值会考虑在底层设备内发生的传输。此值始终低于或等于 Total Bandwidth。 |
| Completed Req. (Low-Level) | 完成的底层 I/O 请求。在上一个性能分析帧中，Low-level I/O 中完成的 I/O 传输请求的数量。 |
| Canceled Req. (Low-Level) | 取消的底层 I/O 请求。在上一个性能分析帧中， Low-level I/O 中取消的 I/O 传输请求的数量。 |
| Pending Req. (Low-Level) | 待处理请求。在进行性能分析时，正在等待Low-level I/O 完成的 I/O 传输请求的数量。 |
| Custom Parameter | 显示您实现的 `IAkLowLevelIOHook::GetData()` 返回的值。 |

**相关主题**

- [“连接至本地/远程游戏系统”一节](../../../07-完善工程/06-性能分析/06-连接至本地远程游戏系统.md "连接至本地/远程游戏系统")
- [“从声音引擎捕获数据”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/00-从声音引擎捕获数据.md "从声音引擎捕获数据")
- [“使用 Performance Monitor 进行监控和故障排查”一节](../../../07-完善工程/06-性能分析/09-使用-Performance-Monitor-进行监控和故障排查.md "使用 Performance Monitor 进行监控和故障排查")

---