# MIDI Keymap Editor 视图

[Wwise 帮助文档](../../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../../00-参考主题.md) > [Project Explorer](../../../../00-Project-Explorer.md) > [Audio tab](../../../00-Audio-tab.md) > [Containers hierarchy: sound and motion objects](../../00-Containers-hierarchy-sound-and-motion-objects.md) > [Common tabs and categories: Containers hierarchy objects](../00-Common-tabs-and-categories-Containers-hierarchy-ob.md) > [MIDI category: Containers hierarchy objects](00-MIDI-category-Containers-hierarchy-objects.md) > MIDI Keymap Editor 视图

###### MIDI Keymap Editor 视图

The MIDI Keymap Editor is where you can define and modify the MIDI properties of an object in the Containers hierarchy and all its descendants. 这对例如编辑 MIDI 合成器所有节点的 MIDI 滤波器可能非常有用。

The MIDI Keymap Editor is available from the Views menu.

With the MIDI Keymap Editor you can choose which object properties to display, and
edit them.

**Working with search results**

- 显示搜索结果时，则选择一项可自动地将它加载到 [“Transport Control”一节](../../../../../02-视图/10-Transport-Control.md "Transport Control") 中以便立即播放。If the corresponding view is not open, double-click the object.
- 您也可以在结果列表中选择一个或多个条目，然后右键单击以显示快捷菜单命令。Many of these, including **Show in Multi Editor** (Ctrl+M), **Show in Schematic View** (Ctl+Shift+S), and **Convert** (Shift+C), are common to a variety of objects. 但是，也有几个命令仅在搜索与查询视图中显示：

  - **Refresh All Sizes**（刷新所有对象的预计大小）：刷新结果列表中所有对象的 Preview Size。
  - **Refresh Size**（刷新对象的预计大小）：仅刷新选中对象的 Preview Size。
  - **Remove From View**：从当前搜索的结果列表中删除所选对象。

**To choose which columns (properties) are displayed:**

When different types of objects appear in the list, all of the columns possible for those
objects are shown.

Both of the following methods open the [“Object Property Settings”一节](../../../../12-搜索和工程全局编辑/06-Object-Property-Settings.md "Object Property Settings").

- Right-click the list header and select **Configure
  Columns**.
- Click **View Settings** (Ctrl+Alt+H) in the title
  bar.

**To view and edit effects:**

1. Click  **View Settings** (Ctrl+Alt+H) in the title
   bar.
2. In the [“Object Property Settings”一节](../../../../12-搜索和工程全局编辑/06-Object-Property-Settings.md "Object Property Settings") list, navigate to Audio > Effects, and
   choose the effect properties to view and click OK.
3. An Effects folder appears under any appropriate object. Expand it to view the effects in
   rows and their properties in columns. This displays the same properties as the [“Effects tab: Containers hierarchy objects”一节](../../../05-Common-tabs-and-categories-audio-structures/08-Effects-tab-Containers-hierarchy-objects.md "Effects tab: Containers hierarchy objects").

**To edit properties of multiple items:**

- Modifying a property (slider, combo, or check box) sets the property to the same value
  for all selected objects.
- Holding the Alt key and dragging a slider offsets the selected objects' values instead
  of setting them to an absolute value.

| 界面元素 | 描述 |
| --- | --- |
|  | 点击视图右上角中的 View Settings 图标。  这时会打开 [“Object Property Settings”一节](../../../../12-搜索和工程全局编辑/06-Object-Property-Settings.md "Object Property Settings") 对话框。选择要为适用 Wwise 对象类型显示的各项属性。 |
|  | 点击列标题区 **Configure Columns**（配置列）快捷方式（右键点击）选项。p  这时会打开 [“Object Property Settings”一节](../../../../12-搜索和工程全局编辑/06-Object-Property-Settings.md "Object Property Settings") 对话框。Select the individual properties for every possible Wwise object type that you want to display as a column. |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../../../12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../../../07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |

|  |  |
| --- | --- |
| 普通列：如果在“对象属性设置”中选择了以下属性，则在结果区域中始终显示为列。其他列根据“结果”区域中列出的对象类型显示。 | |
| Name | 名称。与搜索条件相匹配的对象或工程元素的名称。 |
| Path | 对象或工程元素在工程层级结构中的位置。 |
| Notes | 对象或工程元素的备注或注释。 |
| Type | 结果中所包含的对象或工程元素的类型。例如：声音、总线、SoundBank、Query、效果器等。  Default value: All Objects |
| (Mute and Solo) | 控制对象的 Mute（静音）和 Solo（单独播放）状态，也会显示该对象是否处于被动静音和 Solo 状态。  将对象静音会使其在当前监听中无法听到。让对象 Solo 会使工程中的所有其它对象无声。  粗体的 **M** 或 **S** 表明已为对象主动设置了 Mute 或 Solo 状态。褪色的非粗体 **M** 或 **S** 表明对象的 Mute 或 Solo 状态是由于其它对象状态而被动设置的。  将对象静音会让其子对象被动静音。  让对象 Solo 会使同级对象被动静音，并让子对象和父对象被动 Solo。  |  |  | | --- | --- | | [技巧] | 技巧 | | 在点击 Solo 按钮的同时按住 Ctrl 键，可以强制仅 Solo 该 Solo 按钮所在的对象。 |  |  |  | | --- | --- | | [备注] | 备注 | | Mute 和 Solo 仅用于监视目的，而不会保存在工程中或存储在 SoundBank（声音包）中。 | |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Size Preview（预计大小）：打开视图时将计算其中所有对象的大小预计值。它们将在基本改变（如更换平台）发生时自动刷新。  |  |  | | --- | --- | | [备注] | 备注 | | 无法计算或不适用于对象的字段将标记为“ - ”。 | | |
| Total Size（总大小） | 该元素 Media Size 和 Structure Size 大小的总和，近似等于它们将在 SoundBank 中占用的大小。 |
| Media Size | Wwise 对象的媒体文件（包括转换的源文件，事件和效果器）将在 SoundBank 中占用的近似大小。    |  |  | | --- | --- | | [备注] | 备注 | | 对于需要授权的 Effect，除非输入相应授权码，否则其大小值将不计入。 |    如果父对象同时设置了 [media files are set to stream](../../../../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/01-定义对象的播放行为/00-定义对象的播放行为.md#streaming_media "流播放媒体") 与 **Zero latency**，将只显示较小的音频缓冲区大小。如果父对象选择了流播放但未启用 **Zero Latency** 设置，其大小将不会显示。  |  |  | | --- | --- | | [注意] | 注意 | | 在很多情况下，对象的媒体大小已改变，但视图未更新。要确保所有的预计大小都是最新的，请使用快捷菜单中的 **Refresh All Size** 命令。要更新一个或多个特定项，请选择它们并使用 **Refresh Size** 快捷菜单选项。 | |
| Object Size | Wwise 对象将在 SoundBank 中占用的大致大小，不包括磁盘上声音文件的大小。  |  |  | | --- | --- | | [备注] | 备注 | | Action 不具有大小。只位于 Init Bank 中的对象，如 Game Sync，大小将不计入。 | |
| When limit is reachedStructure Size | 对象及其子结构将在 SoundBank 中占用的近似大小，其中对象大小即为 Object Size。 |

|  |  |
| --- | --- |
| Other Column：除了上述列，许多对象类型的特有属性也可以添加为列。在查询返回所配置的列的属性时，会根据结果予以显示。 | |

---