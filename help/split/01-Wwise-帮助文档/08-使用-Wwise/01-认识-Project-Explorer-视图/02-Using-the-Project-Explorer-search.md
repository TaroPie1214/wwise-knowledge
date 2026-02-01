# Using the Project Explorer search

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > [认识 Project Explorer 视图](00-认识-Project-Explorer-视图.md) > Using the Project Explorer search

## Using the Project Explorer search

Project Explorer Search 设在 Project Explorer 视图的最上面。您可以使用其来查找并聚焦于 Project Explorer 的任一选项卡内的特定对象。该功能对包含大量对象的大型工程特别有用。

**使用搜索功能：**

- 通过以下任一方式来在“搜索”字段中输入内容：

  - 在“搜索”字段中键入所需文本。
  - 将一个或多个对象从任意视图拖到“搜索”字段中。

这时会显示搜索结果。系统会根据 [Search 工具](../11-使用-Search、Query-和-Reference/01-搜索工程中的元素.md "搜索工程中的元素")中应用的相同规则来评估搜索匹配项。

下图举例展示了在“搜索”字段中键入单词 foot 后的结果：

![](../../../../images/pe_filter_example.png)

|  |  |
| --- | --- |
|  | 系统会指示每个选项卡中的匹配结果总数。在总数大于零时，会高亮显示为黄色。 |
|  | 在各个选项卡内，除非包含与搜索匹配的对象，否则所有层级结构都会收起。朝下的黄色箭头表示分支被部分展开了（只显示匹配的下级对象，隐藏不匹配的下级对象）。单击箭头可显示所有下级对象。  After a search:  - Collapsed hierarchies: No matching objects are   found. - Partially expanded hierarchies (yellow): Some matching objects are found, but not   all children match. - Fully expanded hierarchies: Matching objects are found, and all children   match. |
|  | 对于包含至少一个与搜索匹配的对象的层级结构，只会展开到第一个匹配对象所在的层级。朝右的黄色箭头表示其内隐藏了匹配的下级对象。单击箭头可显示分支中的所有匹配下级对象。不匹配的下级对象会保持隐藏状态。  除此之外，也可单击“搜索”字段右侧的 Show All Search Results 按钮  来显示所有分支中的全部匹配下级对象。 |
|  | 背景底纹会高亮显示所有与搜索匹配的对象。 |
|  | 其内隐藏的附加匹配项数会标明并高亮显示为黄色。 |

|  |  |
| --- | --- |
| [备注] | 备注 |
| Project Explorer Search 支持 [WAQL](https://www.audiokinetic.com/library/edge/?source=SDK&id=waql_introduction.html) 查询；不过，有些 WAQL 功能并不适用于这种搜索。比如，关键词 **orderby**、**reverse** 和 **distinct** 对如何呈现结果不起任何作用。Project Explorer 始终按照名称排列并显示结果且不会显示重复结果。另外，Project Explorer 只会显示所支持类型的对象；有些对象类型从不显示在 Project Explorer 中。比如，不会显示 **Event Action**，而只会显示 **Event** 本身。 |

### Refreshing the search

按下 Refresh 按钮 ![](../../../../images/btn_refresh_circle.png) 可基于 Wwise 中所有参数的当前状态再次执行搜索。上次执行搜索后展开或收起的所有分支将恢复为执行搜索操作后的原始展开状态。注意，在更改对象的父对象或创建、重命名或删除对象时会自动刷新搜索结果，但不会对其他参数更改（比如可能对评估音量的 WAQL 查询产生影响的音量更改）做出反应。Refresh 按钮在这些情况下特别有用。

### Resetting the search

若要重置搜索，可单击“搜索”字段最右侧的 **x**。这样会清除“搜索”字段中的所有内容和 Project Explorer 中的所有结果。总的来说，在重置搜索时，Project Explorer 中的各个层级结构会恢复为其之前的展开状态。不过，所有在关闭时选中的对象仍然是可见的（即其层级结构会保持展开状态）。

### 搜索操作和 Selection Channel

搜索操作会与当前 [Selection Channel](../../02-入门/04-个性化您的工作空间/01-处理视图/01-了解-Selection-Channel-和-Meter-Instance.md "了解 Selection Channel 和 Meter Instance") 关联。也就是说，您可以同时在各个 Selection Channel 中执行不同的搜索。在关闭工程时，会保存所有的活跃搜索；在重新打开时，会自动启动这些搜索。

### Keyboard shortcuts

在 Wwise 中的任意位置按下 **Ctrl+F** 即可将键盘焦点移到 Project Explorer Search 字段。若 Project Explorer 视图未打开，会在新的窗口中将其打开。

利用 [“键盘快捷方式和自定义命令”一节](../../09-参考主题/01-工程/12-键盘快捷方式和自定义命令.md "键盘快捷方式和自定义命令") 对话框，可将 **View** > **Project Explorer** > **Reset Search** 命令映射到键盘快捷方式。此命令的效果跟单击“搜索”字段中的 **x** 一样。

**相关主题**

- [“Project Explorer Search”一节](../../09-参考主题/04-Project-Explorer/00-Project-Explorer.md#project_explorer_filter_ref "Project Explorer Search")

---