# Object Property Settings

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Project Explorer](../00-Project-Explorer.md) > [搜索和工程全局编辑](00-搜索和工程全局编辑.md) > Object Property Settings

### Object Property Settings

The Object Property Settings dialog allows you to configure which columns to show in a number of views. 可用的列将按组排序，用于显示 Wwise 中所有对象类型的所有属性，包括一些所有对象都适用的属性。

The Object Property Settings can be opened when clicking on the View Settings icon of
different views or by selecting **Configure Columns** when
right-clicking the header band of the columns. It is also possible to open the Object
Property Settings from the **Hide or Show Properties**
shortcut menu option available in the [“Multi Editor”一节](03-Multi-Editor.md "Multi Editor").

**以下视图是互连的，因此某个视图中执行的列更改会应用于其他视图：**

- [“List View（列表视图）”一节](02-List-View（列表视图）.md "List View（列表视图）")
- [“Query Editor”一节](../07-Queries-选项卡/01-Query-Editor.md "Query Editor")
- [“Reference View 视图”一节](05-Reference-View-视图.md "Reference View 视图")
- [“Event Editor”一节](../02-Events-选项卡/01-Event-Editor/00-Event-Editor.md "Event Editor")

|  |  |
| --- | --- |
| [备注] | 备注 |
| [“MIDI Keymap Editor 视图”一节](../01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图") 视图虽然也带有列显示设置和 Object Property Settings 对话框，但其并不与其他视图互连。 |

如上述视图一样，大部分 Wwise 对象的 Contents Editor（内容编辑器）的列配置也是互连的。不过，对于 Wwise 对象的 Contents Editor，仅可通过右键单击列标题区并选择 **Configure Columns…** 来打开 Object Property Settings。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 此外，[“Contents Editor 视图：Random Container”一节](../01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/08-Contents-Editor-视图：Random-Container.md "Contents Editor 视图：Random Container") 和 [“Contents Editor 视图：Switch Container”一节](../01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/10-Contents-Editor-视图：Switch-Container.md "Contents Editor 视图：Switch Container") 也带有列显示设置和 Object Property Settings 对话框；不过，它们并不与其他对象的 Contents Editor 互连。 |

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| 属性 | 按照树形组织的一系列对象属性，可通过复选框在视图中添加或删除它们。 |
| Affected Object Type | 可能受所选属性影响的所有 Wwise 对象列表，包括音频总线、容器和声音等若干对象类型。 |
|  | 全部不选。取消选择所有属性。 |
|  | 重置为默认设置。在单击此按钮后，将把属性选择恢复为默认设置。 |

---