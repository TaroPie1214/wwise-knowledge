# Control Surface Binding 视图和 Control Surface 会话

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Project Explorer](../00-Project-Explorer.md) > [Sessions 选项卡](00-Sessions-选项卡.md) > Control Surface Binding 视图和 Control Surface 会话

### Control Surface Binding 视图和 Control Surface 会话

在 Control Surface Bindings（控制器绑定）视图中，可定义 Control Surface 设备在 Wwise 中的行为。您可以使用 Control Surface 设备来控制 Wwise 功能或工程属性。有关详细信息，请参阅[*使用控制设备*](../../../08-使用-Wwise/14-使用控制设备/00-使用控制设备.md "使用控制设备")。

Control Surface Bindings 视图会显示当前活跃的 Control Surface Session。

| 界面元素 | 描述 |
| --- | --- |
|  | 当前工程内的 Control Surface Session 列表。  所选 Control Surface Session 的名称会显示在名称字段内。  选择 Control Surface Session 会将其相关的绑定加载到 Wwise 中。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
|  | 激活或停用 Control Surface Session 并打开或关闭 Control Surface Toolbar。 |
| **组** | |
| Global | Global 组中是与特定对象有关的绑定。  目标对象可以直接在绑定中指定。  有关详细信息，请参阅：  - [“为键盘快捷方式创建绑定”一节](../../../08-使用-Wwise/14-使用控制设备/04-创建-Control-Surface-Binding.md#creating_binding_for_keyboard_shortcut "为键盘快捷方式创建绑定") - [“创建绑定以修改特定对象属性值”一节](../../../08-使用-Wwise/14-使用控制设备/04-创建-Control-Surface-Binding.md#creating_binding_to_modify_specific_object_property_value "创建绑定以修改特定对象属性值") |
| Current Selection | 当前选中项。Current Selection 组中是与当前选中的对象有关的绑定。  此组中绑定以 Wwise 中当前所选对象为目标对象。  有关详细信息，请参阅[“创建绑定以修改当前选中项”一节](../../../08-使用-Wwise/14-使用控制设备/04-创建-Control-Surface-Binding.md#creating_binding_to_modify_current_selection "创建绑定以修改当前选中项")。 |
| View Groups | 视图组。View Group 组中是将视图中的对象与绑定动态关联的 View Group 列表，View Group 可以被加载到视图中。  View Group 绑定的目标对象由加载了绑定组的视图来定义。视图中加载的每个对象都有一个索引。  您可以通过单击 **Add Group** 按钮来创建 View Group。  有关 View Group 的详细信息，请参阅 [“理解 Control Surface 的 View Group”一节](../../../08-使用-Wwise/14-使用控制设备/05-理解-Control-Surface-的-View-Group.md "理解 Control Surface 的 View Group")。 |
| **属性列** | |
| Group/Binding | 组/绑定。显示绑定或组的名称。  您可以使用 Binding 上的快捷菜单来重命名 Binding。 |
| Learn | 学习。为绑定激活/停用学习模式。  在激活以后，绑定将一直保持学习模式，直到学习模式被停用，或关联了有效属性/命令和硬件控件为止。 |
| [>>] （选择器） | 打开菜单以便选择用于 Binding 的命令或属性。 |
| Property/Command name | 属性/命令名称。定义绑定的行为。  点击 [>>] 选择器以选择属性或命令。  有关详细信息，请参阅[“创建 Control Surface Binding”一节](../../../08-使用-Wwise/14-使用控制设备/04-创建-Control-Surface-Binding.md "创建 Control Surface Binding")。 |
| Object/Index | 对象/索引。为绑定的属性或命令定义目标对象。  点击 [...] 按钮，在 Global 组中浏览要绑定的对象。 |
| [...]  （按钮） | 浏览要设置为绑定目标的对象。  此按钮仅适用于 Global 组内的绑定。 |
| Controller Assignment | 控制器指派。定义要将 Control Surface 设备上的哪个硬件控件用于 Binding。 |
| Status | 状态。指明未加载绑定的原因。  可能的状态举例：  - 控制器指派冲突 - 目标对象无法解析（目前没有选择，或视图不包含此类对象） - 绑定不完整  有关冲突的详细信息，请参阅 [“处理 Control Surface Session 中的冲突”一节](../../../08-使用-Wwise/14-使用控制设备/06-处理-Control-Surface-Session-中的冲突.md "处理 Control Surface Session 中的冲突")。 |
| **按钮** | |
| Add & Learn Binding | 添加和学习绑定。在选组中添加新的绑定并激活学习模式。  除非学习模式处于停用状态，或已经关联了有效属性/命令和硬件控件，否则绑定将一直保持学习模式，。 |
| Add Group | 添加组。在 **View Group** 文件夹中创建新的 View Group。View Group 可加载到视图中，从而将视图中的对象与绑定进行动态关联。 |
| Remove | 删除。删除 Control Surface Binding 中所选的绑定或 View Group。  Global、Current Selection 和 View Group 三个组无法删除。 |

**相关主题**

- [“使用 Control Surface 工具栏”一节](../../../08-使用-Wwise/14-使用控制设备/07-使用-Control-Surface-工具栏.md "使用 Control Surface 工具栏")

---