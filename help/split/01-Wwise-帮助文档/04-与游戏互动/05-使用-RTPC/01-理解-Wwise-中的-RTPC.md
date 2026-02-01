# 理解 Wwise 中的 RTPC

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [与游戏互动](../00-与游戏互动.md) > [使用 RTPC](00-使用-RTPC.md) > 理解 Wwise 中的 RTPC

## 理解 Wwise 中的 RTPC

在 Wwise 创建 RTPC 涉及以下操作：

- [“Creating Game Parameters”一节](02-管理-RTPC-中使用的-Game-Parameter.md#creating_game_parameter "Creating Game Parameters")、MIDI Parameter、[LFO](04-使用-LFO.md "使用 LFO")、[Envelope](05-使用包络.md "使用包络") 或 [Time](06-使用时间.md "使用时间") Modulator。
- [“将 Wwise 属性指派给游戏参数”一节](03-使用-Game-Parameter-控制属性值/01-将-Wwise-属性指派给游戏参数.md "将 Wwise 属性指派给游戏参数")
- [“映射 RTPC 坐标图中的值”一节](03-使用-Game-Parameter-控制属性值/02-映射-RTPC-坐标图中的值.md "映射 RTPC 坐标图中的值")

您可以在 Project Explorer（工程资源管理器）的 Game Syncs（游戏同步器）选项卡中或者 RTPC 选项卡内定义 Game Parameter。属性值和 Game Parameter 之间的关系可以在 Property Editor、Effect Editor 或 Attuenuation Editor 中的 RTPC 选项卡中定义。另外，还可直接在 RTPC 选项卡的侧面板内调节所选参数的属性。

|  |
| --- |
|  |

通过将 X 轴所示的 Game Parameter 映射到 Y 轴所示的 Wwise 属性值，即可让 Game Parameter 按照期望的方式影响对象属性。引擎创建完整 RTPC 曲线的方法是在您创建的控制点之间插入新的控制点。

每个对象、总线、Attenuation（衰减）或 Effect（效果器）实例都可具有多条曲线，用来表示对象属性与参数或调制器之间的不同关系。用于比较时一次可显示多条曲线，也可以一次只显示一条曲线。

### 使用 RTPC 侧面板

无论是 Game Parameter、MIDI Parameter（MIDI 参数）还是 Wwise 中的三种调制器，RTPC 的 X Axis（X 轴）对象都可设置多种属性值。而且，每个对象都可在对应的 Property Editor（属性编辑器）中单独打开，以便检查并根据需要调节各项属性。不过，一般直接在 RTPC 选项卡内调节属性值会更为便捷。侧面板会始终显示所选 RTPC X Axis 对象的属性，这些属性通常都可直接进行编辑。

若选择多个 RTPC，则侧面板将合并显示其属性及数值。若多个 RTPC 共用同一属性，但其值各不相同，则将显示破折号。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 主要可以通过两种方式直接从 RTPC 选项卡来查找引用 RTPC 的对象。  - 在 RTPC 快捷菜单中选择 **Find All References** 命令，以此打开 References 视图并查找使用该 RTPC 的对象。 - 直接单击侧面板右上角带有编号的 References 按钮。此操作同样可以打开加载有对象的 References 视图。 |

  

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| RTPC 选项卡中有两条分割线，可通过拖动来调节三个面板的大小。  - 横线：将所 RTPC 列表与坐标图隔开。 - 纵线：将所列 RTPC 与侧面板隔开（后者列有关联属性）。 |

### 在 Blend Track 内使用 RTPC

要在对象属性和游戏参数之间创建更加复杂的关系，您可在混合容器的混合轨中使用 RTPC。有关在混合容器中使用 RTPC 的详细信息，请参阅[“定义 Blend Container 的内容和行为”一节](../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/04-定义-Blend-Container-的内容和行为/00-定义-Blend-Container-的内容和行为.md "定义 Blend Container 的内容和行为")。

---