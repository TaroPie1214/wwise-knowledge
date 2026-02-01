# Integrity Report

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [参考主题](../00-参考主题.md) > [视图](00-视图.md) > Integrity Report

## Integrity Report

您可在 Wwise Integrity Report（完好度报告）中生成包含工程相关信息（包括错误及解决方法）的报告。Integrity Report 列出以下错误：

- 缺失的媒体文件
- 失踪的音频或振动源
- 插件问题
- SoundBanks 缺少Events

By double-clicking an error in the Error list, you can open a corresponding Wwise dialog where you can resolve the error, or receive further information about how to handle it. 要获取工程错误及相应建议的完整列表，请参阅 [“Integrity Report 问题”一节](../../03-设置工程/01-处理工程/04-排查工程的问题.md#integrity_report_issues "Integrity Report 问题")。

您也可对 Integrity Report 进行筛选，以仅显示指定的信息类型，如以下项的详细信息：

- Platforms（平台）
- Languages（语言）
- 音频文件和源
- 层级结构
- 参考源
- 优化

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Platforms（平台） | 指定所选平台的相关错误是否显示在 Integrity Report 中。 |
| Languages（语言） | 语言。启用语言列表，您可在其中选择在完好度报告中显示与单个语言相关的错误。 |
| （语言列表） | 指定在完好度报告中显示与若干种所选语言相关的错误。 |
| **Reports（报告）** | |
| Audio Files and Sources | 音频文件和源。指定在完好度报告中仅显示与媒体文件和源相关的错误。 |
| 层级结构 | Specifies that only errors related to the Busses and Containers hierarchies will be displayed in the Integrity Report. |
| 引用失效 | 引用失效。指定在完好度报告中仅显示与无效引用相关的错误。 |
| 优化 | 优化。指定在完好度报告中仅显示与优化相关的错误。 |
|  | 根据已指定的选项生成完好度报告。  点击 **Stop** 按钮，以停止生成过程。 |
| Platform | 发生错误的平台。 |
| Type | 与错误相关联的源类型。  SFX（音效）  Language |
| Object Name | 与错误相关联的 Wwise 对象的名称。 |
| Status | 状态。错误相关信息。 |
| Comments/Suggestions | 备注/建议。如何解决错误的相关信息。 |
| Hierarchy | 层级结构。与错误相关联的对象的层级中的路径或位置。 |
| Project Name | 当前工程的名称。 |
| Date Generated | 生成日期。生成报告的日期和时间。 |
|  | Opens the Save As dialog where you can browse to the location where you want to save the integrity report as a tab delimited TXT file. |

**相关主题**

- [“生成 Integrity Report”一节](../../03-设置工程/01-处理工程/04-排查工程的问题.md#generating_an_integrity_report "生成 Integrity Report")
- [“保存 Integrity Report”一节](../../03-设置工程/01-处理工程/04-排查工程的问题.md#saving_an_integrity_report "保存 Integrity Report")

---