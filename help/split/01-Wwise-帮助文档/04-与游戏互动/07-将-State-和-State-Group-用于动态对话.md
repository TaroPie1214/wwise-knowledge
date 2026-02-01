# 将 State 和 State Group 用于动态对话

[Wwise 帮助文档](../00-Wwise-帮助文档.md) > [与游戏互动](00-与游戏互动.md) > 将 State 和 State Group 用于动态对话

## 将 State 和 State Group 用于动态对话

如今的很多游戏（尤其是体育游戏）都包含 Dynamic Dialogue（动态对白）或由游戏情节驱动的音频内容。如果用传统方法模拟真实对白，可能要创建成千上万的素材，再构建复杂的 Switch Container（切换容器）层级结构，才能满足所有可能的方案。由于内存成本昂贵，所以您需要通过有效的方式来管理工程中的素材。

为了应对这些挑战，Wwise 引入了一种独特的动态对白管理方式，即采用 State 和 State Group（状态组）来预先定义游戏中可能出现各种的情况或结果。State Group 可以表示游戏中的各种元素类别。比如，在足球游戏中，State Group 可能是 Teams（球队）、Players（球员）和 Actions（动作）等。每个 State Group 类别都需要一组对应的 State 值。在足球游戏的例子中，"Teams" State Group 可能包括多个 State 值（如 Dallas、Pittsburgh、New England 等）。

在 Dialogue Event（对白事件）中，State Group 和 State 将被排列组合，以涵盖游戏中所有可能的情况。这些情况称为 Path（路径）。它们会被指派给特定的 Voice（语音）对象。游戏过程中的实时状态会与 Wwise 内 Dialogue Event 中的 State 进行匹配以决定要播放哪段对白。

State Group（状态组）代表游戏中的各种元素类别。比如，体育游戏中的 Teams（球队）和 Players（球员）或动作冒险游戏中的 Friends（队友）、Enemies（敌人）和 Weapons（武器）。在 Project Explorer（工程浏览器）的 Game Syncs（游戏同步器）选项卡中，可以管理 State Group 列表。

为了让您在界面中轻松识别 State Group 和 State，Wwise 将它们用特定图标表示。

| 图标 | 代表 |
| --- | --- |
| |  | | --- | |  | | State Group |
| |  | | --- | |  | | State Group 值 |

## 将 State 用于 Dynamic Dialogue – 示例

假设您正在开发一款带有现场解说的高尔夫游戏，需要先为其中各个不同类别分别创建 State Group，每个 State Group 要包含该类别对应的所有 State。高尔夫游戏需要多种 State Group，包括 Players（选手）、Clubs（俱乐部）、Courses（球场）、Shots（击球）、Locations（位置）、Reactions（反应）等。

下图展示了在高尔夫游戏中如何将部分类别与 State Group 和其中的 State 进行对应。

|  |
| --- |
|  |

在定义 State Group 和 State 之后，即可将其添加到游戏所需的 Dialogue Event 中。有关如何创建 Dialogue Event 的详细信息，请参阅[“创建 Dialogue Event”一节](02-管理动态对话/01-创建-Dialogue-Event/00-创建-Dialogue-Event.md "创建 Dialogue Event")。

## 创建 State Group

您可以在 Project Explorer 的 Game Syncs 选项卡中创建工程所需的所有 State Group。

**在 Project Explorer 中新建 State Group 的方法如下：**

1. 在 Project Explorer 中，切换至 Game Syncs（游戏同步器）选项卡。
2. 在 State（状态）层级中，执行以下操作之一：

   选中 Virtual Folder（虚拟文件夹）或 Work Unit（工作单元），并点击 Project Explorer 工具栏上的 **State Group** 图标。

   右键点击 Virtual Folder 或 Work Unit ，从快捷菜单中选择 **New Child > State Group**（新建子项 > 状态组）。

   新 State Group 将被添加至 State Group 列表。
3. 将默认名称替换为更合适的命名。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 各 State Group 不得重名，而且名称只能包含字母、数字和下划线。 |
4. 根据需要，继续添加 State Group。

   |  |  |
   | --- | --- |
   | [技巧] | 技巧 |
   | 双击 State Group 可将其加载到 Property Editor 中。在 **Notes** 字段，还可注明该 State Group 的相关信息。 |

## 创建 State

您创建的各个 State Group（状态组）可以具有多个不同的值，分别代表每个类别内的不同选项。例如，**Player Name**（玩家名字）这个 State Group 中，各 State（状态）就是游戏中各个玩家的名字。可以在 Project Explorer （工程浏览器）的 Game Syncs（游戏同步器）选项卡中创建工程所需的所有状态。

**在 Project Explorer 中新建 State 的方法如下：**

1. 在 Project Explorer 中，切换至 Game Syncs 选项卡。
2. 在 State（状态）层级中，执行以下操作之一：

   选中 State Group，并点击 Project Explorer 工具栏中的 **State** 图标。

   右键单击 State Group（状态组）并在快捷菜单中依次选择 **New Child** > **State**（新建子对象 > 状态）。

   这时会将新建的 State 添加到 State Group 列表。
3. 将默认名称替换为最能代表 State Group 值的名称。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 同一 State Group 内的各个 State 不得重名。 |
4. 根据需要继续添加 State。

   |  |  |
   | --- | --- |
   | [技巧] | 技巧 |
   | 双击 State 可将其加载到 Property Editor 中。在 **Notes** 字段，还可注明该 State 的相关信息。 |

## 删除 State 或 State Group

您可能想要删除不再需要的 State Group（状态组）或 State。在删除 State Group 时，其中的所有 State 也将被删除。记住，若删除 State Group，则会从所有用到它的 Dialogue Event 移除该 State Group。

**删除 State Group 的方法如下：**

1. 在 Project Explorer 中，切换至 Game Syncs 选项卡。
2. 在 **State Groups**（状态组）分区中，右键单击要删除的 State Group 或 State 并选择 **Delete Selection**（删除选中项）。

   这时会删除选中的 State Group 或 State。

   |  |  |
   | --- | --- |
   | [技巧] | 技巧 |
   | 除此之外，也可选中 State Group 或 State 并按下 Delete 键。 |

---