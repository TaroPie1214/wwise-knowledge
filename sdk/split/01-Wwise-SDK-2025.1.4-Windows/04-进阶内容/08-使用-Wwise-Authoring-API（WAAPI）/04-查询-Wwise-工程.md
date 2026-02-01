# 查询 Wwise 工程

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

查询 Wwise 工程

Wwise Authoring API 提供了综合查询系统，可用于获取 Wwise 工程最关键方面的信息。 更具体地说，它用于获取工程中任何对象的信息。

该查询系统内置于 [ak.wwise.core.object.get](ak_wwise_core_object_get.html) 功能里。请参阅它的参考文档了解更多详情。

查询可分为 2 种不同的形式：

- **WAQL** ：在 waql 语句中使用 Wwise Authoring Query Language 定义文本查询请参阅 [使用 Wwise Authoring Query Language (WAQL)](waql_introduction.html) 和 [WAQL 快速入门](waql_getting_started.html) 。
- **JSON** ：按照 JSON 格式使用 from 和 transform 语句定义查询。

|  |  |
| --- | --- |
|  | **备注:** 建议使用 WAQL 而非 JSON 查询格式。WAQL 具有更强的功能和适用性，可更好地处理错误且更加易于使用。 |

# WAQL 查询

WAQL 查询允许在一行文本中指定整个查询。

|  |  |
| --- | --- |
|  | **技巧:** WAQL 查询还可直接用在 Wwise 设计工具内以供测试。This is especially useful to verify the query syntax and results before implementing it inside your WAAPI program or script. 比如，您可以在 Wwise 工具栏或 List View 搜索字段中键入以下 WAQL 查询： $ from type Event |

详细了解 WAQL：

- [使用 Wwise Authoring Query Language (WAQL)](waql_introduction.html)
- [Wwise Authoring Query Language (WAQL) 参考](waql_reference.html)

# JSON 查询

|  |  |
| --- | --- |
|  | **备注:** 不建议使用 JSON 查询，最好使用 WAQL 查询。请参阅 [使用 Wwise Authoring Query Language (WAQL)](waql_introduction.html) 和 [WAQL 快速入门](waql_getting_started.html) 。 |

JSON 查询包含两个部分：

- **from：** 指定查询的起点。这是获取数据的来源。
- **transform：** 指定应用于对象的一系列转换。可以按次序添加转换。

此外，查询可以用选项指定：

- **return：** 指定从对象返回的内容。如果没有指定，则默认值为 ['id', 'name']。
- **platform：** 指定使用查询的平台。如果没有指定，则默认为当前平台

## from

**from** 语句为查询开始提供了几个起点：

- **id：** 指定: 指定一列对象 ID（GUID）。当您已经有对象 ID 时，可用于查找该对象。
- **name：** 按照 type:name 形式指定一组由对象类型限定的对象名称。仅支持采用全局唯一名称的对象类型。请参阅 [Wwise 对象参考](wobjects_index.html) 了解可用类型。
- **search：** 指定在 Wwise 对象和备注中要搜索的文本。这与 Wwise 中的搜索功能所用的搜索引擎是一样的。
- **path：** 指定要查找的一系列路径。路径必须是绝对路径，并且必须以类别名称开头，就相当于物理文件夹名称。For example: \Containers\Default Work Unit\MySound.
- **ofType：** 指定一系列 Wwise 对象类型。用于获取某个对象类型的所有对象。例：获取所有 Game Parameters。请参阅 [Wwise 对象参考](wobjects_index.html) 了解可用类型。

## transform

**transform** 语句提供了几个转换功能，可以用于转换已选择的对象。第一个转换是应用于 **from** 语句所选择的对象的。另一个 transformation 应用于之前转换的结果。

可以按次序添加多个转换。

- **select** **parent：** 为每个对象选择父级对象。
- **select** **children：** 为每个对象选择子级对象列表。
- **select** **descendants：** 为每个对象递归选择所有子级对象。
- **select** **ancestors：** 为每个对象递归选择父级对象。
- **select** **referencesTo：** 为每个对象选择所有引用该对象的对象。
- **where：** 用于过滤之前迭代器的结果。可能的标准是：
  - **name:contains**： 对对象名称中文本的搜索，不区分大小写。
  - **name:matches**: 对对象名称的正则表达式搜索，不区分大小写。
  - **type:isIn**： 筛选之前迭代器的结果，仅保留特定类型的对象。如需查看对象类型列表，请参阅 [Wwise 对象参考](wobjects_index.html) 。
  - **category:isIn**： 筛选之前迭代器的结果，仅保留特定类别的对象。
- **distinct：** 筛选之前迭代器的结果，仅保留独特的对象。

# 返回选项

**return** 表达式用于指定所要返回的 Wwise 对象元素。可以返回任意数量的要素。

return 表达式可能包含：

- **核心属性**：参见 [Wwise Authoring Query Language (WAQL) 参考](waql_reference.html) 中的 **OBJECT\_EXPRESSION** 和 **VALUE\_EXPRESSION** 。
- **对象属性和引用**：参见 [Wwise 对象参考](wobjects_index.html) 。

属性和引用名称可选用以下两种前缀：

- **'@PROPERTYNAME'**：返回直接在对象上设置的值。这种情况下会忽略重写系统，并且可能会返回未使用和隐藏的值。
- **'@@PROPERTYNAME'**：返回重写系统所解析的值。这种情况下可能会返回从父对象继承的值或直接返回对象的值（如对象不沿用属性）。

若未使用任何前缀，则返回重写系统所解析的值。其效果跟使用 @@ 前缀相同。此时建议不使用前缀。

示例：

- **'volume'**、**'Volume'**、**'@Volume'**、**'@@Volume'**：返回对象的音量。因为音量不可重写，所以这些前缀的效果都是一样的。注意，属性名称不区分大小写。
- **'OutputBus'**、**'outputbus'**、**'@@OutputBus'**：返回重写系统所解析的 Output Bus（使用 Override Parent）。该值在播放时使用。注意，引用名称不区分大小写。
- **'@OutputBus'**：返回直接在对象上设置的 Output Bus。该值同时保留用于与此对象关联的 Work Unit。若对象未选中 Override Parent 选项，则可能会不使用并隐藏该值。

在表达式解析为有效引用时，可进一步查询被引用对象的属性。 For example, if the reference 'UserAuxSend0' on a Sound object references an existing Auxiliary Bus, it is possible to query a property of this Auxiliary Bus by appending a dot ('.'), followed by the property descriptor. Querying for the Attenuation of the referenced Auxiliary Bus would therefore simply be 'UserAuxSend0.Attenuation'.

示例：

- **OutputBus.name**：返回输出总线的名称。
- **parent.name**：返回父对象的名称。
- **parent.parent.type**：返回祖对象的类型。
- **OutputBus.Volume**：返回输出总线的音量。
- **OutputBus.Attenuation.name**：返回输出总线的名称。
- **Attenuation.path**：返回输出总线的路径。
- **Effects.first.effect.id**: returns the ID of the first Effect.

有些对象包含带有特定功能（如随机化）的属性。为了检索与这些功能相关的值，可通过类似函数的访问器来查询与属性绑定的特殊对象。比如，随机化器功能由绑定到对象特定属性的 Modifier 对象描述。此对象可作为 'randomizer("PropertyName")' 来查询，其中 PropertyName 为属性（如 'Volume'）的名称。 在访问器提供有效引用时，可按照前文所述方式进一步查询返回的对象。比如，可按照以下方式获取 Volume 随机化器的 'Max' 属性：'randomizer("Volume").@Max'。

可用的访问器包括：

- randomizer

如果返回表达式中的一个条目不兼容或不在返回对象中，则结果将不含该条目。

- 请参阅 [ak.wwise.core.object.get](ak_wwise_core_object_get.html) 查看可用访问器的完整清单。
- 请参见 [Wwise 对象参考](wobjects_index.html) 了解属性和引用的更多可用信息。

# 其他选项

[ak.wwise.core.object.get](ak_wwise_core_object_get.html) 函数及其他函数允许使用选项对象来定义：

- return 语句（参见上文）
- platform：平台的 ID (guid) 或名称。
- language：语言的 ID (guid) 或名称。

有些访问器会区分选项。For example, when retrieving a property or reference value, you can specify the platform to get the unlinked values. 若未指定平台，则使用当前平台。 另外，还可通过指定语言来检索针对语言的信息，如 Sound SFX（音效）对象的音频源数据。 若未指定语言，则使用当前语言。

# 示例

请参照 to [工程代码](wamp_js_node.html#wamp_js_node_code) 了解初始化。

如需查看更多示例，请参阅 [ak.wwise.core.object.get](ak_wwise_core_object_get.html) 。

返回一列对象的 ID、名称和音量：

from waapi import WaapiClient

import pprint

# Connect (default URL)

client = WaapiClient()

# Return two objects

args = {

'waql': '$ "\\Devices\\Default Work Unit\\System", "{1514A4D8-1DA6-412A-A17E-75CA0C2149F3}"'

}

options = {

'return': ['id', 'name', 'Volume']

}

result = client.call("ak.wwise.core.object.get", args, options=options)

pprint.pprint(result)

# Disconnect

client.disconnect()

Return the ID and name of every object in the Containers starting with 'My', using a regular expression:

from waapi import WaapiClient

import pprint

# Connect (default URL)

client = WaapiClient()

# Return all objects under the Containers hierarchy with a name that starts with "My"

args = {

'waql': '$ "\Containers" select descendants where name = /^My/'

}

options = {

'return': ['name', 'id']

}

result = client.call("ak.wwise.core.object.get", args, options=options)

pprint.pprint(result)

# Disconnect

client.disconnect()

如需进一步了解 WAQL，请参阅 [使用 Wwise Authoring Query Language (WAQL)](waql_introduction.html) 章节。