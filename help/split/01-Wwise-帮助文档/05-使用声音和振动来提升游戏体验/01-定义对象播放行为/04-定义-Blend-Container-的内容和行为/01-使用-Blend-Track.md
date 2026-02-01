# 使用 Blend Track

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../../00-使用声音和振动来提升游戏体验.md) > [定义对象播放行为](../00-定义对象播放行为.md) > [定义 Blend Container 的内容和行为](00-定义-Blend-Container-的内容和行为.md) > 使用 Blend Track

### 使用 Blend Track

Blend Track 用于将混合容器内的对象及其属性值进行编组。每个 Blend Track 可以包含多个对象，它们可以同时被听到，也可以使用 RTPC 由游戏参数决定何时听到它们。

#### 创建 Blend Track

在混合容器内组织对象的第一个步骤是创建并命名 Blend Track。

**创建新 Blend Track 的方法如下：**

1. 将混合容器加载至属性编辑器。
2. In the Blend Track tab of the Secondary Editor, click **New Blend Track**.
3. 输入 Blend Track 的名称，然后按下 **Enter**。

   此时新的 Blend Track 将显示在 Blend Track Editor 中。
4. 重复该步骤，来创建所需的新 Blend Track。

   您创建的 Blend Track 将显示在 Blend Track Editor，以及 Contents Editor 的 **>Blend Tracks**> 部分中。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 要删除 Blend Track，请选择 Blend Track，并按下 **Delete**。 |

#### 为 Blend Track 添加和移除对象

如果不为创建的 Blend Track 添加对象的话，Blend Track 则将是空白的。混合容器内的每个 Blend Track 最多可以包含 128 个对象。一个对象可以同时存在于多个 Blend Track 中，一个 Blend Track 也可以多次包含同一对象。您可以在 Content Editor 中为 Blend Track 添加或移除对象。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| Blend Track 内的对象顺序十分重要，因为顺序决定了这些对象如何行排列和交叉淡变。有关交叉淡变的详细信息，请参阅 [“管理交叉淡变”一节](02-管理交叉淡变.md "管理交叉淡变")。 |

**将对象添加至混合容器中的 Blend Track 的方法如下：**

1. 将混合容器加载至属性编辑器。
2. 将对象从 Contents Editor 或 Project Explorer 中拖至 Blend Tracks 列表中的各个 **Blend Track**，为其添加对象。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 从 Blend Track 中移除对象，选择对象并按下 **Delete**。该操作会从 **Blend Track** 列表中移除对象，但不会从 Contents Editor 中移除对象。 |

#### 将 RTPC 曲线添加到 Blend Track

可以通过两种方式将 RTPC（实时参数控制）曲线添加至 Blend Track：

- 将曲线添加至混合容器本身。
- 将曲线添加至混合容器内的各个 Blend Track。

如果您选择将 RTPC 添加至混合容器本身，该 RTPC 则将同时作用于容器内的所有对象。有关创建和使用 RTPC 的详情，请参阅 [使用 RTPC](../../../04-与游戏互动/05-使用-RTPC/00-使用-RTPC.md "使用 RTPC")。

但您也可以将 RTPC 添加至容器内的各个 Blend Track。通过这种方式，您可以仅针对所选对象应用 RTPC。例如，您可以将赛车游戏中的所有碰撞声添加至一个 Blend Track 中。如果您使用冲击力 RTPC 来改变 Blend Track 的音量，则该 RTPC 会影响各个撞击声的音量。

**将 RTPC 曲线添加至 Blend Track 的方法如下：**

1. In the Blend Tracks tab of the Secondary Editor, select the blend
   track to which you want to add RTPC curves, and click the **Property Selector** button.

   可用声音属性列表将被显示。
2. 点击您想用 RTPC 影响的声音属性。

   RTPC 曲线将被显示在图形视图中。
3. 在 X 轴列表中，点击要指派给 Wwise 属性的游戏参数。

   游戏参数被指派给图形视图中的 X 轴。
4. 重复这些步骤，为图形添加更多的 RTPC 曲线。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 由于您添加了多条使用不同单位的游戏参数曲线，因此单位将不再显示。但您选中控制点时，仍可看到图形下方 X 轴和 Y 轴框中所显示的单位。 |

#### 在 Blend Track 中编辑 RTPC 曲线

将若干条 RTPC 曲线添加至 Blend Track 后，您可以像定义其它 RTPC 曲线那样定义这些曲线。例如，可以添加点、移动它们，也可以定义曲线段形状。有关这些操作的详细信息，请参阅 [“使用 Game Parameter 控制属性值”一节](../../../04-与游戏互动/05-使用-RTPC/03-使用-Game-Parameter-控制属性值/00-使用-Game-Parameter-控制属性值.md "使用 Game Parameter 控制属性值")。

#### 在 Blend Track 中显示 RTPC 曲线

Blend Container（混合容器）中的每条 Blend Track（混合音轨）都可包含多条 RTPC 曲线。使用 Blend Track Editor，您可以同时处理多条 RTPC 曲线。

|  |
| --- |
|  |

当在 RTPC 列表中选择某条 RTPC 曲线时，它会在图形视图中高亮显示，并可以进行编辑。有关使用 RTPC 曲线的详情，请参阅 [“使用 Game Parameter 控制属性值”一节](../../../04-与游戏互动/05-使用-RTPC/03-使用-Game-Parameter-控制属性值/00-使用-Game-Parameter-控制属性值.md "使用 Game Parameter 控制属性值")。

---