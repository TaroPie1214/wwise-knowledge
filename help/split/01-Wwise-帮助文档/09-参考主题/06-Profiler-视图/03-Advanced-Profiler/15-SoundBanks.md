# SoundBanks

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > [Advanced Profiler](00-Advanced-Profiler.md) > SoundBanks

### SoundBanks

Advanced Profiler — SoundBank 选项卡显示有关已隐式或显式加载到内存的 SoundBank 信息，包括 SoundBank 大小、它包含的媒体文件数量以及媒体已加载到内存中的位置。使用 LoadBank() 时，SoundBank 会显式加载到内存中。

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Name | 名称。加载到内存中的 SoundBank 的名称。 |
| Media Memory | 媒体内存。SoundBank 及其对应的媒体文件占用的内存量。  对于流播放媒体和[自动定义的 SoundBank](../../../07-完善工程/07-管理-SoundBank/02-SoundBank-管理策略/05-Auto-defined-SoundBank.md "Auto-defined SoundBank")，Media Memory 为 0 字节。对于后者，Wwise 为 Event 自动定义的 SoundBank 仅包含 Event 和引用的 Structure，其会以显式方式排除媒体。  根据 SoundBank 的大小，将会显示内存值，单位为字节、千字节 （KB）或兆字节 (MB)。 |
| Object Memory | 默认内存池。从 SoundBank 加载的声音结构已占用的内存量。 |
| Wwise Objects | The number of Wwise objects, such as sound and motion objects, and busses, that are currently loaded into memory. |
| Media Files | 媒体文件。当前加载到内存中的媒体文件的数量。 |
| Memory Category | 内存类别。指示将 SoundBank 媒体加载到了哪个内存类别。 |
| Explicit Load | 显式加载。是使用 LoadBank() 函数显式加载 SoundBank，还是使用  [`PrepareEvent()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a98b617d05618e6d18680d198845ff3d7.html)函数隐式加载。 |

**相关主题**

- [“连接至本地/远程游戏系统”一节](../../../07-完善工程/06-性能分析/06-连接至本地远程游戏系统.md "连接至本地/远程游戏系统")
- [“从声音引擎捕获数据”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/00-从声音引擎捕获数据.md "从声音引擎捕获数据")
- [“使用 Performance Monitor 进行监控和故障排查”一节](../../../07-完善工程/06-性能分析/09-使用-Performance-Monitor-进行监控和故障排查.md "使用 Performance Monitor 进行监控和故障排查")

---