# Queries tips and best practices

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > [使用 Search、Query 和 Reference](00-使用-Search、Query-和-Reference.md) > Queries tips and best practices

## Queries tips and best practices

在 Wwise 中创建查询时，有许多选项可用。在设计查询时运用特定策略，可以准确、快速、稳定地获得您需要的结果。下面是在工程中使用效果器时您可能需要考虑的一些策略。

### Object type details

Browser 列表中的许多标准都有条件，可以让您进一步缩小查询范围。不过，这些条件会随 Query From（从此处查询）列表中所选的对象类型变化。例如，对于 Property Value 标准，请考虑以下三种情形：

- 如果选择“Audio Source”作为对象类型，则有包括位深和采样率等一系列条件可供您选择。
- 如果选择“Event”作为对象类型，则无条件可用，因为它对于此对象类型不是有效的标准（在 Wwise 中，事件没有属性）。

因此，对象类型的选择非常重要，它决定了您可以用于查询的条件。

### Speeding up queries

几个简单的选择可以让您的查询运行速度变得更快。

- 在 Query From 列表中指定对象类型。
- 如果您要查找平台专有的内容，则选择平台。
- 使用 **Start From Here**（从此处开始）来选择层级结构中尽可能深的位置。

### Using wildcards in queries

通配符是一些符号，它们通过扩展搜索词的参数来提高关键词搜索的灵活性。在您试图查找包含以特定字母或数字开头或结尾的不同工程元素时，可以使用通配运算符来代替搜索词的一部分。在 Wwise 中，通配符是星号（\*）。例如，要查找名称中包含 LOOP 的所有对象，应在条件文本框中输入 **\*LOOP\***。而要查找以字母 LOOP 开头的所有对象，应在条件文本框中输入 **LOOP\***。最后，要查找以字母 LOOP 结尾的所有对象，应在条件文本框中输入 **\*LOOP**。

---