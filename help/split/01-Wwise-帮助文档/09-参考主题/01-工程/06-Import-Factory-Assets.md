# Import Factory Assets

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [参考主题](../00-参考主题.md) > [工程](00-工程.md) > Import Factory Assets

## Import Factory Assets

使用 Import Factory Assets（导入出厂素材）对话框来导入工程素材（如声音示例、效果器预设或插件媒体文件）。

您可以在菜单栏中依次单击 **Project** > **Import Factory Assets**（工程 > 导入出厂素材）来访问此对话框。

创建工程时，系统会提示您导入出厂素材。您可以使用此对话框将工程创建期间没有导入的素材（比如安装插件后新增的可用素材）导入到工程中。

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Factory Assets（列表） | 出厂素材。列出 Wwise 安装的素材。  被禁用的素材是已导入至工程中的素材，或与工程中的文件发生冲突的素材。  使用复选框选择要安装哪个素材组。 |
| Select All（按钮） | 全选。选择列表中的所有素材组。只能选中已启用的素材。 |
| Select None（按钮） | 全部不选。取消选中列表中的所有素材组。 |
| OK（按钮） | 确认导入工程中已选择的素材组。  |  |  | | --- | --- | | [备注] | 备注 | | 该操作要求在导入前先保存工程。导入后将重新加载工程。 |  |  |  | | --- | --- | | [备注] | 备注 | | 该操作不会自动将文件添加至版本控制。完成该操作后，您需要手动将新导入的文件添加至版本控制。 | |
| Cancel（按钮） | 取消操作。 |

---