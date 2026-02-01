# Query Editor

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Project Explorer](../00-Project-Explorer.md) > [Queries 选项卡](00-Queries-选项卡.md) > Query Editor

### Query Editor

在 Query Editor（查询编辑器）中，您可以创建和运行查询。查询大体上是请求显示工程中的一部分信息。当查找特定对象时，您可创建非常具体的查询；也可创建一般性查询，例如查找特定平台中的所有声音对象。另外，Query Editor 还支持 WAQL 查询。有关 WAQL 查询的详细信息，请参阅[了解 Wwise Authoring Query Language (WAQL)](https://www.audiokinetic.com/library/edge/?source=SDK&id=waql_introduction.html)。

与查询条件相匹配的所有工程元素显示在 Results 列表中。当您选择 Result 列表中的某个条目时，它会自动加载至播放控制，并准备进行播放。您可以右键点击 Result 列表中的一系列条目来访问各种命令，如 Edit、Show in Multi Editor、Show in Schematic View 和 Convert。您可以随时在 Results 列表中双击条目，以在 Property Editor 中显示该条目。您也可将属性元素从 Results 列表拖至 Project Explorer。For example, you can drag one or more sound objects from the Results list into a Property Container or containers within the Project Explorer.

**Working with search results**

- 显示搜索结果时，则选择一项可自动地将它加载到 [“Transport Control”一节](../../02-视图/10-Transport-Control.md "Transport Control") 中以便立即播放。If the corresponding view is not open, double-click the object.
- 您也可以在结果列表中选择一个或多个条目，然后右键单击以显示快捷菜单命令。Many of these, including **Show in Multi Editor** (Ctrl+M), **Show in Schematic View** (Ctl+Shift+S), and **Convert** (Shift+C), are common to a variety of objects. 但是，也有几个命令仅在搜索与查询视图中显示：

  - **Refresh All Sizes**（刷新所有对象的预计大小）：刷新结果列表中所有对象的 Preview Size。
  - **Refresh Size**（刷新对象的预计大小）：仅刷新选中对象的 Preview Size。
  - **Remove From View**：从当前搜索的结果列表中删除所选对象。

**To choose which columns (properties) are displayed:**

When different types of objects appear in the list, all of the columns possible for those
objects are shown.

Both of the following methods open the [“Object Property Settings”一节](../12-搜索和工程全局编辑/06-Object-Property-Settings.md "Object Property Settings").

- Right-click the list header and select **Configure
  Columns**.
- Click **View Settings** (Ctrl+Alt+H) in the title
  bar.

**To view and edit effects:**

1. Click  **View Settings** (Ctrl+Alt+H) in the title
   bar.
2. In the [“Object Property Settings”一节](../12-搜索和工程全局编辑/06-Object-Property-Settings.md "Object Property Settings") list, navigate to Audio > Effects, and
   choose the effect properties to view and click OK.
3. An Effects folder appears under any appropriate object. Expand it to view the effects in
   rows and their properties in columns. This displays the same properties as the [“Effects tab: Containers hierarchy objects”一节](../01-Audio-tab/05-Common-tabs-and-categories-audio-structures/08-Effects-tab-Containers-hierarchy-objects.md "Effects tab: Containers hierarchy objects").

**To edit properties of multiple items:**

- Modifying a property (slider, combo, or check box) sets the property to the same value
  for all selected objects.
- Holding the Alt key and dragging a slider offsets the selected objects' values instead
  of setting them to an absolute value.

| 界面元素 | 描述 |
| --- | --- |
|  | 点击视图右上角中的 View Settings 图标。  这时会打开 [“Object Property Settings”一节](../12-搜索和工程全局编辑/06-Object-Property-Settings.md "Object Property Settings") 对话框。选择要为适用 Wwise 对象类型显示的各项属性。 |
| Name | 查询的名称 |
|  | 打开选择器菜单，您可在此创建新查询或选择已有查询。 |
|  | 从 Query Editor 中清除所有条件和搜索结果。 |
| Notes | 备注。用于描述查询的任何额外信息。 |
| Query From | 从此处查询。所要搜索的对象类型或其他工程元素，如声音、Audio Bus（音频总线）、SoundBank（音频包）等。  除此之外，也可从列表中选择 **WAQL Query** 来启用 WAQL Query 字段。 |
| Start From | 起始位置。工程层级结构中开始查询的位置。 |
|  | 打开 Project Explorer - Browser 对话框以选择要从哪个位置开始查询。 |
|  | 重设 Start From Here 位置。 |
| WAQL Query | WAQL 查询。所要执行的 WAQL 查询。有关 WAQL 查询的详细信息，请参阅[了解 Wwise Authoring Query Language (WAQL)](https://www.audiokinetic.com/library/edge/?source=SDK&id=waql_introduction.html)。  |  |  | | --- | --- | | [备注] | 备注 | | 此字段仅在从 **Query From** 列表中选择 **WAQL Query** 时可用。 | |
| Platform | 搜索所涵盖的若干个平台。 |
|  | 搜索工程，找出满足搜索条件的对象和其它工程元素。 |
| **Criteria** | |
| Browser | 浏览器。查询所依据的条件列表，如 Name 或 Output Bus。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
| Criteria | 为查询所选择的条件列表。 |
| Operator | 当查询中包含多个条件时使用的逻辑运算符。可使用以下运算符：  **And**，匹配所有条件的项。  **Or**，匹配至少一个条件的项。 |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Name | 名称。搜索所依据的条件的名称和类别。 |
| Condition | 搜索所依据的条件的特定详情。  对于某些条件，当您试图查找包含特定字母或数字或者以它们开头或结尾的不同工程元素时，您可以使用通配符（在 Wwise 为星号 (\*)）来替换部分单词。 |
| **Results** | |
|  | 点击列标题区 **Configure Columns**（配置列）快捷方式（右键点击）选项。p  这时会打开 [“Object Property Settings”一节](../12-搜索和工程全局编辑/06-Object-Property-Settings.md "Object Property Settings") 对话框。Select the individual properties for every possible Wwise object type that you want to display as a column. |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |

|  |  |
| --- | --- |
| 普通列：如果在“对象属性设置”中选择了以下属性，则在结果区域中始终显示为列。其他列根据“结果”区域中列出的对象类型显示。 | |
| Name | 名称。与搜索条件相匹配的对象或工程元素的名称。 |
| Path | 对象或工程元素在工程层级结构中的位置。 |
| Notes | 对象或工程元素的备注或注释。 |
| Type | 结果中所包含的对象或工程元素的类型。例如：声音、总线、SoundBank、Query、效果器等。  Default value: All Objects |
| (Mute and Solo) | 控制对象的 Mute（静音）和 Solo（单独播放）状态，也会显示该对象是否处于被动静音和 Solo 状态。  将对象静音会使其在当前监听中无法听到。让对象 Solo 会使工程中的所有其它对象无声。  粗体的 **M** 或 **S** 表明已为对象主动设置了 Mute 或 Solo 状态。褪色的非粗体 **M** 或 **S** 表明对象的 Mute 或 Solo 状态是由于其它对象状态而被动设置的。  将对象静音会让其子对象被动静音。  让对象 Solo 会使同级对象被动静音，并让子对象和父对象被动 Solo。  |  |  | | --- | --- | | [技巧] | 技巧 | | 在点击 Solo 按钮的同时按住 Ctrl 键，可以强制仅 Solo 该 Solo 按钮所在的对象。 |  |  |  | | --- | --- | | [备注] | 备注 | | Mute 和 Solo 仅用于监视目的，而不会保存在工程中或存储在 SoundBank（声音包）中。 | |

|  |  |
| --- | --- |
| Platform | 对象或工程元素所在的平台。 |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Size Preview（预计大小）：打开视图时将计算其中所有对象的大小预计值。它们将在基本改变（如更换平台）发生时自动刷新。  |  |  | | --- | --- | | [备注] | 备注 | | 无法计算或不适用于对象的字段将标记为“ - ”。 | | |
| Total Size（总大小） | 该元素 Media Size 和 Structure Size 大小的总和，近似等于它们将在 SoundBank 中占用的大小。 |
| Media Size | Wwise 对象的媒体文件（包括转换的源文件，事件和效果器）将在 SoundBank 中占用的近似大小。    |  |  | | --- | --- | | [备注] | 备注 | | 对于需要授权的 Effect，除非输入相应授权码，否则其大小值将不计入。 |    如果父对象同时设置了 [media files are set to stream](../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/01-定义对象的播放行为/00-定义对象的播放行为.md#streaming_media "流播放媒体") 与 **Zero latency**，将只显示较小的音频缓冲区大小。如果父对象选择了流播放但未启用 **Zero Latency** 设置，其大小将不会显示。  |  |  | | --- | --- | | [注意] | 注意 | | 在很多情况下，对象的媒体大小已改变，但视图未更新。要确保所有的预计大小都是最新的，请使用快捷菜单中的 **Refresh All Size** 命令。要更新一个或多个特定项，请选择它们并使用 **Refresh Size** 快捷菜单选项。 | |
| Object Size | Wwise 对象将在 SoundBank 中占用的大致大小，不包括磁盘上声音文件的大小。  |  |  | | --- | --- | | [备注] | 备注 | | Action 不具有大小。只位于 Init Bank 中的对象，如 Game Sync，大小将不计入。 | |
| When limit is reachedStructure Size | 对象及其子结构将在 SoundBank 中占用的近似大小，其中对象大小即为 Object Size。 |

|  |  |
| --- | --- |
| Other Column：除了上述列，许多对象类型的特有属性也可以添加为列。在查询返回所配置的列的属性时，会根据结果予以显示。 | |
|  | 将查询结果复制到 Windows 剪贴板，这样您便可以将结果粘贴至其它应用程序中。 |

**相关主题**

- [“Creating queries”一节](../../../08-使用-Wwise/11-使用-Search、Query-和-Reference/03-Working-with-queries.md#creating_query "Creating queries")
- [“Defining and running queries”一节](../../../08-使用-Wwise/11-使用-Search、Query-和-Reference/03-Working-with-queries.md#defining_and_running_query "Defining and running queries")
- [“Creating advanced queries using criteria groups”一节](../../../08-使用-Wwise/11-使用-Search、Query-和-Reference/03-Working-with-queries.md#creating_advanced_queries_using_criteria_groups "Creating advanced queries using criteria groups")
- [“Using factory-defined queries”一节](../../../08-使用-Wwise/11-使用-Search、Query-和-Reference/03-Working-with-queries.md#using_factory_defined_queries "Using factory-defined queries")
- [“Deleting queries”一节](../../../08-使用-Wwise/11-使用-Search、Query-和-Reference/03-Working-with-queries.md#deleting_query "Deleting queries")

---