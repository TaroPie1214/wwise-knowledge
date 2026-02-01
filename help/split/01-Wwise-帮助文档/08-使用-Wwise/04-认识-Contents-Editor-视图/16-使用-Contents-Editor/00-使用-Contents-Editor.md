# 使用 Contents Editor

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [使用 Wwise](../../00-使用-Wwise.md) > [认识 Contents Editor 视图](../00-认识-Contents-Editor-视图.md) > 使用 Contents Editor

## 使用 Contents Editor

Contents Editor（内容编辑器）中显示了一系列字段、列表、选项和滑杆，可以用它们设置对象、State 和 Switch 的属性和行为。如果需要这些工具的使用帮助，请参阅以下各节：

- [“使用文本框和滑杆”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_text_boxes "使用文本框和滑杆")
- [“使用列表”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_lists "使用列表")

在 Contents Editor 中，您可以播放每个对象，也可以重新排序、复制、粘贴和删除视图中的对象。根据当前加载的对象类型，视图中显示的选项或属性将有所不同。多数视图中，一些属性滑杆旁边会显示特定图标，来表示它们具有特定属性。下表介绍了这些图标。

| 图标 | 名称 | 描述 |
| --- | --- | --- |
|  | | |

|  |  |  |
| --- | --- | --- |
|  | Link | 链接。属性值已链接到其它有效游戏平台的值。 |
|  | Unlink | 取消链接。属性值没有链接到其它有效游戏平台的值。 |
|  | Partial Unlink | 部分取消链接。当前平台的属性值已链接到其它有效平台，但其它平台的若干个相应值已取消链接。 |
|  | Link Mixed | 有些选定的对象具有不同的链接状态。有些可能是链接的，而另一些则是取消链接或部分取消链接的。 |

|  |  |  |
| --- | --- | --- |
|  | RTPC 已禁用 | 该属性值未绑定至游戏内参数值。 |
|  | RTPC 已启用 | 游戏内参数值已绑定至该属性值。这意味着，例如游戏赛车的速度可直接绑定至 Wwise 中的音调属性。当游戏中的赛车速度提高时，Wwise 中的音调也将实时提高。 |
|  | RTPC 部分启用 | Multi Editor 中只有部分对象为该属性绑定了游戏参数值。Property Editor 或 Contents Editor 中不会看到这个标识。 |

|  |  |  |
| --- | --- | --- |
|  | State 已禁用 | 此属性值未与 State 绑定。 |
|  | State 已启用 | State Group 已与此属性值绑定。也就是说，所述属性（如 Volume）可能会随应用的 State 变化。 |
|  | State 混合情形 | State Group 绑定到了 Multi Editor 中加载的一个或多个对象（并非全部）的属性值。Property Editor 或 Contents Editor 中不会看到这个标识。 |

|  |  |  |
| --- | --- | --- |
|  | Randomizer 已启用 | 随机化器效果已应用到的属性值。 |
|  | Randomizer 已禁用 | 尚未应用随机化器效果的属性值。 |
|  | 随机化器 Mixed | Multi Editor 中只有部分对象为该属性值启用了 Randomizer 效果。Property Editor 或 Contents Editor 中不会看到这个标识。 |

---