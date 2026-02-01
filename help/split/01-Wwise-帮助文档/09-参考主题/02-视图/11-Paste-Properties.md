# Paste Properties

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [参考主题](../00-参考主题.md) > [视图](00-视图.md) > Paste Properties

## Paste Properties

您可以通过 Paste Properties（粘贴属性）视图将各种属性从某个对象复制到一个或多个其他对象。比如，您可能需要管理一系列相同类型的对象，并想为多个或所有对象设定相同的设置，或者希望其使用一系列相同的 RTPC。Paste Properties 视图方便高效地管理各个对象的此类数据。

有关 Paste Properties 视图和如何使用它的详细信息，请参阅“[*复制和粘贴对象属性*](../../08-使用-Wwise/13-复制和粘贴对象属性.md "复制和粘贴对象属性")”章节。

| 界面元素 | 描述 |
| --- | --- |
| Copy from Object | 从对象复制。包含要将其属性复制粘贴到一个或多个目标对象的源对象。要选择源对象，可将对象从 Project Explorer（工程资源管理器）复制到此选择框，或者使用右侧的按钮（Follow Clipboard、Browse for Source Objects 和 Select a Recent Paste）。 |
| Paste to Object(s) | 粘贴到对象。包含一个或多个目标对象。您可以将对象从 Project Explorer 拖到此处，或者使用右侧的 Follow Selection 按钮。 |
|  | 跟随剪贴板。在选中时，会将复制到剪贴板的对象设为源对象。 |
|  | 跟随选择。在选中时，会将 Project Explorer 中单击的对象设为目标对象。 |
|  | 打开 Project Explorer - Browser（工程资源管理器 - 浏览器），以便从中选择源对象。 |
|  | 列出最近的 15 项粘贴操作。您可以选择其中一项来查看源对象和目标对象、Property Filter（属性筛选器）按钮状态、所用 Paste Mode 以及选中或清除的复选框。 |
|  | 开启或关闭 Property Filter。在选中时，两个对象对比窗格仅显示在单击 **Paste** 时更改的对象。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
| Properties | 属性。显示对应层级结构内的对象属性。跟其他层级结构视图一样，您可以展开和折叠父对象来显示或隐藏子元素。若启用了 Property Filter，则仅显示其值与目标对象中的对应值不同的属性。不显示 RTPC 和 State（状态）图标。 |
| Source Value | 源值。显示源对象中的属性的值。所有值都是只读的。 |
| Target Value(s) | 目标值。显示目标对象中的属性的值。若有多个具有不同值的目标对象，则显示短横线。若没有目标支持属性且禁用了 Property Filter，则值为空。所有值都是只读的。 |
| Objs Changed on Paste | 对象在粘贴时被更改。显示在单击 **Paste** 时更改的目标对象数。若有多个目标对象，则可右键单击数值，然后单击 **Show Changed in List View**（在列表视图中显示更改的对象），来列出受影响的对象。若没有目标支持属性且禁用了 Property Filter，则不显示任何内容。 |
|  | 指示属性列表仅部分可见，且仅显示源对象中与目标对象中属性的值不同的属性。只有开启了 Property Filter 才会显示这些箭头。要查看整个属性列表，可单击相应箭头来显示该分区的整个属性列表。此时，图标会变为常规的灰色展开箭头。除此之外，还可关闭 Property Filter 来查看所有分区的全部属性。 |
| Paste Mode | 粘贴模式。决定在将 List Element 粘贴到目标对象时其会受怎样的影响。其设有三个选项：  - **Replace Entire List**（替换整个列表）。完全移除目标对象列表元素，并将所选列表元素从源对象复制到目标对象。 - **Add New, Replace Existing**（添加新的，替换现有）。将所有列表元素从源对象复制到目标对象，同时替换目标对象中已经存在的列表元素，但不从目标对象移除任何多出的列表元素。 - **Add New, Keep Existing**（添加新的，保留现有）。粘贴源对象中存在而目标对象中不存在的列表元素，但是不替换或移除目标对象中已经存在的列表元素。 |
| List Element | 列表元素。显示要从源对象复制到目标对象的 List Element。共有四个列表：  - Metadata - RTPC - Stingers - Music Cue |
| Objs with Added | 对象包含添加的条目。显示在单击 **Paste** 时接收新的 List Element 的目标对象数。若有多个目标对象，则可右键单击数值，然后单击 **Show Changed in List View**（在列表视图中显示更改的对象），来列出受影响的对象。 |
| Objs with Replaced | 对象包含替换的条目。显示在单击 **Paste** 时包含要替换的 List Element 的目标对象数。若有多个目标对象，则可右键单击数值，然后单击 **Show Changed in List View**（在列表视图中显示更改的对象），来列出受影响的对象。 |
| Objs with Removed | 对象包含移除的条目。显示在单击 **Paste** 时包含要移除的 List Element 的目标对象数。若有多个目标对象，则可右键单击数值，然后单击 **Show Changed in List View**（在列表视图中显示更改的对象），来列出受影响的对象。 |
|  | 全部选择。选中 Properties 和 List Elements 分区中的所有复选框。 |
|  | 全部不选。清除 Properties 和 List Elements 分区中的所有复选框。 |
|  | 粘贴。将属性和 List Element 从源对象复制到目标对象。 |

**相关主题**

- [*复制和粘贴对象属性*](../../08-使用-Wwise/13-复制和粘贴对象属性.md "复制和粘贴对象属性")
- [“Pasting object properties”一节](../../08-使用-Wwise/13-复制和粘贴对象属性.md#paste_properties_paste "Pasting object properties")

---