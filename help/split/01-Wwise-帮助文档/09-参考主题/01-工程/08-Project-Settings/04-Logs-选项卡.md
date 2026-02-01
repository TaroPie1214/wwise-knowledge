# Logs 选项卡

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [工程](../00-工程.md) > [Project Settings](00-Project-Settings.md) > Logs 选项卡

### Logs 选项卡

有时不希望或不需要在生成过程中在 SoundBank Log（音频包日志）中或在转码过程中在 Conversion Log（转码日志）中显示特定警告和/或消息。有时还会想根据自己的策略来更改特定消息的严重性。您也可限制日志中显示的消息的数量（按类型）。

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Ignore | 忽略。决定是否在日志中显示该消息类型。默认情况下将显示所有消息类型。选中该复选框后，Wwise 将忽略相应的消息类型，日志中将不会显示此类消息。 |
| ID | 指派给特定错误、警告或消息的 ID。 |
| Message | 消息。转码或生成 SoundBank 过程中遇到的问题描述。 |
| Severity | 严重性。转码或生成 SoundBank 过程中遇到问题时应用的严重性。  |  |  | | --- | --- | | [备注] | 备注 | | 使用命令行生成 SoundBank 时，WwiseConsole.exe 进程会返回一个代码，表示 SoundBank 生成过程中找到的最大严重性值。0：仅消息或没有任何消息，1：重大错误或错误，2：警告。您可使用该列以控制返回值。 | |
| Max Messages Per Message Id | 决定 Wwise 是否限制日志中显示的消息的数量（按类型）。您可指定显示的消息数量上限。  同一数字将作用于所有消息类型。  Default value: 100 |
| Warn, while profiling, when number of Resume/Play-From-Beginning virtual voices exceeds: | 若在执行性能分析时 Resume/Play-From-Beginning（继续/从头播放）的虚声部数超出该值，则发出警告。确定 Wwise 是否在 Resume/Play-From-Beginning 类型的虚声部数超出指定数值时向 Capture Log（捕获日志）输出错误消息。 |
|  | 保存您对列表所做的任何更改，然后关闭 Log Ignore List。 |
|  | 关闭 Log Ignore List，不保存更改。 |

**相关主题**

- [“管理在日志中出现的消息”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/04-管理在日志中出现的消息.md "管理在日志中出现的消息")

---