# WAQL 快速入门

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

WAQL 快速入门

在本教程中，建议使用 Integration Demo 工程。在通过 Audiokinetic Launcher 安装 SDK 和 Visual Studio 平台后，可在 SDK 示例中找到该工程。不过，您也可以使用自己的工程或 Wwise 示例中的其他工程（如 Wwise Audio Lab 或《Wwise Adventure Game》）。

在很多地方都可以使用 WAQL。对于本教程，我们来以 List View 为例加以阐述。

|  |  |
| --- | --- |
|  | **技巧:** 我们制作了有关如何在 List View 中使用 WAQL 的简短视频教程。详请参见 [Finding Objects using WAQL](https://www.youtube.com/watch?v=9K24tJGpoEk)。 |

# 简单的筛选查询

在 List View 的搜索字段中键入以下查询：

`$ where volume < 0`

第一个字符为 **$**，用于告知 Wwise 要写入 WAQL 查询。Wwise 可藉此区分标准文本和 WAQL 查询。**$** 之后的内容用于定义查询本身。

在本例中，使用 **where** 关键字开始查询。在使用 **where** 关键字开始时，WAQL 会自动获取工程的所有对象，并使用 **where** 之后定义的条件语句来加以筛选。作为筛选器，**where** 关键字只输出匹配的对象。

简写如下：

`$ where CONDITION`

CONDITION 是一个布尔表达式，其会返回 true 或 false。在上面的例子中，表示要将音量与数字值进行比较。若音量小于零，则查询返回 true。在此，将针对工程的所有对象验证该条件。在完成查询后，会列出所有音量小于零的对象。

补充练习：

- 尝试不同的运算符：<=、>、>=、=
- 将 **volume** 替换为 **pitch** 或 **lowpass**
- 尝试使用 **and** 和 **or**（加或不加括号）来定义更为复杂的表达式

|  |  |
| --- | --- |
|  | **技巧:** 若要了解 WAQL 属性名称，请参阅 [Wwise 对象参考](wobjects_index.html) 章节。 |

# 字符串条件

目前只使用了数字值条件。下面来试下字符串条件：

`$ where name = "hello"`

字符串条件会将两个字符串的内容进行比较。在使用等号运算符执行比较时，不区分大小写。若文本相同（不区分大小写），则认为条件成立。您可以使用该表达式来查找特定的内容。

除此之外，也可只比较字符串的部分内容：

`$ where name : "hello"`

此查询中使用了冒号而非等号作为比较运算符。冒号用于定义单词搜索运算符。若在所查看的元素内找到指定的单词，则返回 true。在此示例中，若在名称中找到 hello，则返回 true。

补充练习：

- 更改所要搜索的文本
- 尝试在搜索文本中使用星号通配符（比如 \*lo）
- 将 **name** 替换为 **notes** 或 **outputbus**

# 联用对象属性

Wwise 对象具有两种类型的属性：

- 返回数值的属性：
  - Volume、Pitch、Lowpass 等：通常与 Wwise 中的滑杆关联，用于存储数字值。这些属性因对象类型而异。比如，**Sound** 和 **Random Container** 便拥有不同的属性。
  - Name、Note、ID、Path：Wwise 对象系统的核心元素，其通常存储字符串值。所有 Wwise 对象都拥有这些属性。
- 返回另一 Wwise 对象的属性（又称引用）：
  - OutputBus, Target, UserAuxSend0: They point to another object and they vary depending on the object type. 比如，**Event** 和 **Sound** 便拥有不同的属性。
  - Parent：指向父对象 (parent)。

您可以使用**点号**运算符将两项属性结合在一起。例如：

`$ where parent.name = "Music"`

或者

`$ where parent.volume < 0`

甚至，还可将多个属性结合在一起：

`$ where outputbus.parent.name = "Main Audio Bus"`

|  |  |
| --- | --- |
|  | **备注:** 在将属性结合在一起时，确保把要返回值的属性放在最后一个点号之后。至于要返回另一对象的属性，则可放在序列中的任何位置。 |

补充练习：

- 尝试对 outputbus 的 volume 进行筛选
- Try to filter on the pluginname of the first effect

# 使用不同的源

目前，我们都是筛选整个工程中的对象。不过有时需要缩小搜索范围，将目标限定为一组特定的对象。

键入以下查询：

`$ from type sound`

此查询会列出工程中的所有 Sound 对象。**from** 关键字用于定义从哪里开始查询。这样可以有效地缩小搜索范围。藉此，WAQL 可将迭代限定为指定的源。

甚至，还可指定多种对象类型：

`$ from type randomsequencecontainer, switchcontainer, blendcontainer`

同时，还可使用 **where** 关键字为前述查询写入筛选器：

`$ where type = "randomsequencecontainer" or type = "switchcontainer" or type = "blendcontainer"`

不过，执行筛选时必须查询所有工程对象，包括 Event、Bus、Sound 等等。这样的话执行速度会比较慢。

补充练习：

- 尝试使用其他对象类型（参见 [Wwise 对象参考](wobjects_index.html) 章节）。

# 结合使用 from 和 where

键入以下查询：

`$ from type sound where volume < 0`

此查询会获取工程中的所有 Sound 对象，并在筛选之后只列出音量小于零的声音。

其中 **from** 关键字仅可用在 WAQL 查询的开头，**where** 关键字则要添加到 **from** 的后面。

补充练习：

- 尝试在 **from** 部分使用其他对象类型
- 尝试在 **where** 部分使用其他条件
- 尝试联用多个 **where** 语句

# 从特定对象查询

WAQL 可进一步限定查询源。

在 List View 中键入以下查询：

`$ from object "\Containers"`

此查询会使用对象路径来返回单个对象。

为了使语句更加紧凑，WAQL 还支持省略 from object 部分。因此，可直接键入：

`$ "\Containers"`

此查询会返回指定的对象。

当然，也可列出多个对象：

`$ "\Busses", "\Containers"`

补充练习：

- 在按住 SHIFT 的同时右键单击 Project Explorer 中的某个对象。在快捷菜单中选择 **Copy Path(s) to clipboard**。将其设为 WAQL 查询的源。
- 在按住 SHIFT 的同时右键单击 Project Explorer 中的多个对象。在快捷菜单中选择 **Copy WAQL query to clipboard**。将查询粘贴到 List View 中。
- 在按住 SHIFT 的同时右键单击 Project Explorer 中的某个对象。在快捷菜单中选择 **Copy GUID(s) to clipboard**。将 GUID 粘贴到 List View 中，并在前后添加双引号：$ "{1514A4D8-1DA6-412A-A17E-75CA0C2149F3}"。
- For Busses and Events, try using the type and the name: $ "Bus:Main Audio Bus".

# 选择对象

前面尝试了从不同的源执行 WAQL 查询，接下来我们看看如何选择对象。通过选择对象，可从初始对象序列获取其他对象。

在 List View 中键入以下查询：

`$ "\Containers\Default Work Unit" select children`

此查询会获取 Default Work Unit，并返回其所有的直接子对象 (children)。

下面来尝试获取更多对象：

`$ "\Containers\Default Work Unit" select descendants`

此查询会在结果中获取 Default Work Unit 的所有下级对象 (descendant)。这些下级对象包括所有以递归方式获取的子对象。

补充练习：

- 尝试选择父对象
- 尝试选择多个元素（元素之间使用逗号分隔）
- 尝试将 **select** 语句添加到第一部分中的 **where** 查询
- 尝试在 select 查询的末尾添加 **where** 语句
- 尝试选择 outputbus

# 通过 Event 播放声音

前面学习了 WAQL 的基本概念，下面我们来尝试构建具体的示例。在本例中，我们将尝试枚举 Event 引用的所有声音。

首先，枚举工程中的所有 Event：

`$ from type event`

然后，从 Event 对象获取 Event 动作（直接子对象）：

`$ from type event select children`

然后，获取各个动作的目标（引用命名目标）：

`$ from type event select children select target`

然后，获取目标本身（使用 **this** 关键字）及其下级对象：

`$ from type event select children select target select this, descendants`

最后，通过筛选类型来仅保留 Sound 对象：

`$ from type event select children select target select this, descendants where type = "sound"`

补充练习：

- 将查询源由工程中的所有 Event 改为特定的 Event。
- 尝试仅筛选 Play 动作（滤掉其他类型，比如 Stop）。有关动作属性的信息，请参阅 [Action](wwiseobject_action.html) 章节。

# 通过 Event 播放声音 – 反向操作

下面我们来从 Sound 对象开始查询，并列出所有可播放该对象的 Event：

`$ from type sound`

然后，获取所有声音本身及其上级对象 (ancestor)。之所以在意上级对象，是因为其同样可被 Event 引用。比如，父级 Random Container 便可作为 Event 的目标。

`$ from type sound select this, ancestors`

然后，获取所有引用目前所获元素的对象：

`$ from type sound select this, ancestors select referencesTo`

这样基本上相当于查找所有引用（类似于 Reference 视图），不过需要筛选并仅保留 Event 动作，因为其他对象（如 SoundBank 或 SoundCaster 会话）也有可能包含对它们的引用：

`$ from type sound select this, ancestors select referencesTo where type = "action"`

最后，获取各个动作的父对象（即 Event）：

`$ from type sound select this, ancestors select referencesTo where type = "action" select parent`

补充练习：

- 将查询源由工程中的所有声音改为特定的声音。
- 将查询源由工程中的所有声音改为特定 Work Unit 下的所有对象。
- 尝试仅保留 Play 动作（滤掉其他动作类型，比如 Stop）。

# 总结

下面我们来总结一下本教程中所学的内容。

关于 WAQL 查询的构成：

- 查询会返回一系列 Wwise 对象。
- 查询可拆分成多个部分（由 **from**、**where** 和 **select** 语句定义）。
- 查询的每个部分为下一部分馈送结果。
- 必须指定从哪里开始查询。查询源由 **from** 语句定义。
- 在省略 **from** 语句时，将把工程中的所有对象作为查询源。
- **where** 语句允许从馈送序列（即前一部分）中滤掉某些对象，而仅保留那些符合条件的对象。
- **select** 语句允许从馈送序列（即前一部分）中获取新的对象。
- **where** 和 **select** 语句可添加到任何序列。

关于 Wwise 对象：

- Wwise 对象拥有属性，其可用在 **where** 或 **select** 语句中。
- 属性既可以是数字值、布尔值、字符串，也可以是对工程中其他对象的引用。
- 有些属性适用于所有对象类型（称为核心属性）。
- 有些属性仅适用于一种或多种对象类型。
- 属性可与点号运算符结合使用。

下一步？您可以使用 WAQL 执行很多其他操作：

- 如需继续了解 WAQL，请参阅 [术语表](waql_glossary.html) 和 [重要的关键字和概念](waql_keywords_concepts.html) 章节。
- 如需了解都可使用 WAQL 查询哪些内容，请参阅 [Wwise Authoring Query Language (WAQL) 参考](waql_reference.html) 章节。
- 如需了解 Wwise 对象及其属性，请参阅 [Wwise 对象参考](wobjects_index.html) 章节。
- 如需了解如何在 WAAPI 中使用 WAQL，请参阅 [ak.wwise.core.object.get](ak_wwise_core_object_get.html) 章节。