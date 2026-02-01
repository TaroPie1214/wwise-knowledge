# Metadata tab

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Audio tab](../00-Audio-tab.md) > [Common tabs and categories: audio structures](00-Common-tabs-and-categories-audio-structures.md) > Metadata tab

#### Metadata tab

  

|  |  |
| --- | --- |
| [备注] | 备注 |
| The Metadata tab for busses is exactly the same as the Metadata tab for objects in the Containers hierarchy except that the **Override parent** check box does not apply. |

Metadata（元数据）选项卡允许将任意数量的元数据插件关联到对象。在将元数据插件与对象关联时，必须指定其 Type 和 Mode（Use ShareSets 或 Define custom）。通过单击 Edit 按钮 [...] 可打开 Metadata Editor，并编辑元数据插件的各项属性。

Metadata 选项卡分为两个面板。在左侧面板中，可添加或移除元数据插件、指派名称和模式或在 Metadata Editor 中将其打开。在右侧面板（看起来像是一个简化版的 [“Multi Editor”一节](../../12-搜索和工程全局编辑/03-Multi-Editor.md "Multi Editor")）中，可统一编辑多个选定插件的属性。

| General | |
| --- | --- |
| 界面元素 | 描述 |
| [name] | 对象的名称。 |
| (Object Color) | 显示对象的颜色。单击图标可打开颜色选择器。    选择一种颜色并将其应用于对象。在为对象选择某种颜色时，会在选定方块上显示调色板图标，并在右下角标注黄色三角（如图所示）。  若要沿用父对象的颜色，请选中颜色选择器最左侧的方块。 |
| (Mute and Solo) | 控制对象的 Mute（静音）和 Solo（单独播放）状态，也会显示该对象是否处于被动静音和 Solo 状态。  将对象静音会使其在当前监听中无法听到。让对象 Solo 会使工程中的所有其它对象无声。  粗体的 **M** 或 **S** 表明已为对象主动设置了 Mute 或 Solo 状态。褪色的非粗体 **M** 或 **S** 表明对象的 Mute 或 Solo 状态是由于其它对象状态而被动设置的。  将对象静音会让其子对象被动静音。  让对象 Solo 会使同级对象被动静音，并让子对象和父对象被动 Solo。  |  |  | | --- | --- | | [技巧] | 技巧 | | 在点击 Solo 按钮的同时按住 Ctrl 键，可以强制仅 Solo 该 Solo 按钮所在的对象。 |  |  |  | | --- | --- | | [备注] | 备注 | | Mute 和 Solo 仅用于监视目的，而不会保存在工程中或存储在 SoundBank（声音包）中。 | |
| (Show references) | 指示工程中有多少元素包含对对象的直接引用。若存在对对象的引用，则图标显示为橙色；若不存在此类引用，则图标显示为灰色。  通过单击该按钮，可打开 [“Reference View 视图”一节](../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")，并在 **References to:**（引用:）字段中查看对象的名称。 |

| Metadata | |
| --- | --- |
| 界面元素 | 描述 |
| Override parent | 不沿用父级。决定是从父对象沿用元数据插件，还是在层级结构的当前层级另行定义。在没有选中此项时，元数据选项不可用。  若对象为总线或顶层对象，则 Override parent 选项不可用。  默认值：False（否） |
| Link 标志 | 您可以使用 [Link 标志](../../../../08-使用-Wwise/03-了解-Property-Editor/11-使用-Property-Editor.md#linking_unlinking_property_values "Linking or unlinking property values")（**Metadata** 标题栏左侧）来查看或设置平台专有属性。  此项用于链接或取消链接整列元数据插件而非列表中的个别条目。 |
| **Metadata** | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Type | 类型。元数据插件的类型。 |
| Name | 名称。元数据实例的名称。元数据实例既可为 ShareSet，也可为 ShareSet 的自定义实例。对应列表中会显示选定元数据类型的所有元数据实例。 |
| Mode | 模式。决定是否共享元数据实例。模式可以是：  - **Define custom**（定义自定义）：创建自定义元数据插件实例，不在对象之间共享其属性。 - **Use ShareSets**（使用共享集）：使用元数据插件的 ShareSet，可在对象之间共享元数据属性。 |
| Edit | 编辑。打开 Metadata Editor（元数据编辑器），并实时编辑选定元数据实例的属性。 |
|  | **Add**（添加）按钮方便将元数据插件添加到列表中。The list of Metadata plug-ins and corresponding instances that can be selected are presented in a list. |
|  | **Delete**（删除）按钮方便从列表中移除所选元数据插件。 |
| (Name 字段) | 名称。可编辑文本字段，用于显示所选元数据插件的名称。若选中多个插件，则此字段为空。 |
|  | References（引用）按钮用于显示工程中引用了多少个当前所选元数据插件。  在单击该按钮后，将打开 [“Reference View 视图”一节](../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图") 并显示直接引用所选元数据插件的所有工程对象/元素。  |  |  | | --- | --- | | [备注] | 备注 | | 在选择多个元数据插件时，该按钮将变为灰色并显示 0。  显示的最大值为 999。在个别情况下有 1,000 个或更多引用时，该数值不会继续增大，但 Reference 视图中会显示所有对象/元素。 | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Name | 名称。当前所选元数据插件的属性名称。  |  |  | | --- | --- | | [备注] | 备注 | | ShareSet 包含 Color 和 Inclusion 属性，而自定义实例则不包含。 | |
| Value | 值。当前所选元数据插件的属性值。此面板中执行的修改将应用于左侧面板中具有对应属性的所有选定插件。  若多个选定插件具有同一属性但属性值不同，则 Value 列中将显示短横线（如下图所示）。在这种情况下，仍可照常编辑属性并将更改应用于具有对应属性的所有选定插件。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |

---