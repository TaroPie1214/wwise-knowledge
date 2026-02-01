# 定义 Music Switch Container 的内容和行为

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [创建互动音乐](../00-创建互动音乐.md) > [定义音乐对象播放行为](00-定义音乐对象播放行为.md) > 定义 Music Switch Container 的内容和行为

## 定义 Music Switch Container 的内容和行为

Music Switch Container 允许根据游戏内特定元素的不同备选方案来对乐曲进行分组。在 Switch Container（切换容器）中，Swtich（切换开关）或 State（状态）代表着各种不同条件。例如，游戏中主角采用不同的行动模式时，可以针对性地创建 Music Switch Container，其中包含战斗场景、紧张情况以及潜行模式的 Switch。

|  |
| --- |
|  |

各 Switch/State 对应着特定条件选项下的音乐对象。本例中，所有游戏战斗相关的 Music Segment 将对应 Switch Fight，与紧张情况相关的 Music Segment 将对应 Switch Stress，以此类推。游戏调用切换容器时，Wwise 会验证哪个 Switch/State 处于激活状态，进而确定播放哪个 Container 或 Music Segment。

下图表示当事件调用了 “Character Action”（角色行动模式）这个 Music Switch Container 时，会发生什么。该容器中，已根据游戏中可能的角色动作类型将音乐分成了几组，有两种状态：潜行（Stealth）和战斗（Fight）。事件调用 Music Switch Container 时，角色正处于潜行模式（State=Stealth），因此会播放潜行模式音乐。您可以使用 Music Playlist Container 对潜行状态下的乐曲进行分组，以确保在角色每次进入潜行模式时都会播放不同变化版本的音乐。

|  |
| --- |
|  |

### 将 Music Switch Container 与 Game Sync 关联

Music Switch Container（音乐切换容器）可以基于 State（状态）、Switch（切换开关）或 Game Parameter（游戏参数）。要将 Music Switch Container 关联到 Game Parameter，需要先在 Switch Group Property Editor（切换开关组属性编辑器）中将 Switch Group（切换开关组）关联到所需的 Game Parameter。关于 RTPC（实时参数控制）如何与 Switch 进行关联的详细信息，请参阅[“将 Game Parameter 值映射到 Switch”一节](../../04-与游戏互动/04-使用-Switch/02-将-Game-Parameter-值映射到-Switch.md "将 Game Parameter 值映射到 Switch")。

设置 Music Switch Container 时，首先需要将 Switch Group 或 State Group（状态组）指派给容器，这决定了音乐将对哪些 Switch、State 或 RTPC 做出反应。

为容器指派 Switch\State Group，或将 RTPC 关联至 Switch之前，必须先创建它们。有关创建切换开关组、状态组和 RTPC 的信息，请参阅：

- [*使用 State*](../../04-与游戏互动/03-使用-State/00-使用-State.md "使用 State")
- [*使用 Switch*](../../04-与游戏互动/04-使用-Switch/00-使用-Switch.md "使用 Switch")
- [“Creating Game Parameters”一节](../../04-与游戏互动/05-使用-RTPC/02-管理-RTPC-中使用的-Game-Parameter.md#creating_game_parameter "Creating Game Parameters")

**将 Music Switch Container 与 Game Sync 关联：**

1. 将音乐切换容器加载到音乐编辑器。
2. 执行以下操作之一：

   - 点击编辑器顶部的 [>>] 按钮，并选择 Game Sync（游戏同步器）。
   - 将 Switch Group（切换开关组）或 State Group（状态组）对象从 Project Explorer（工程资源管理器）拖放到编辑器的顶部。

### 定义 Music Switch Container 内各个音乐对象的行为

在重复使用不同乐段的情况下，Switch 或 State 可能会包含多个相同的音乐对象。这种情况下，需要确定 State 改变时这些共用音乐对象如何播放。视具体情况而异，可能需要音乐对象继续播放，或在下一个同步点停止并从头播放。

下图中， Stealth（潜行）和 Stress（紧张）两个 Switch 关联了同一播放列表编组（S2\_Playlist） 。游戏从潜行切换至紧张模式时（反之亦可），可以选择在下一同步点继续播放 S2\_Playlist，或停止当前音乐段落并从播放列表开头播放。

|  |
| --- |
|  |

**定义 Music Switch Container 内音乐对象播放行为的方法如下：**

1. 将 Music Switch Container（音乐切换容器）加载到 Property Editor（属性编辑器）中。
2. 在 **Play Options** 分组中，根据需要执行以下操作：

   若希望在 Switch/State（切换开关/状态）改变时继续播放源和目标共用的音乐对象，请选中 **Continue to play on Switch change**（在切换开关变化时继续播放）选项。

   如果希望 Switch/State 改变时，源和目标共用的音乐对象在下一个同步点停止并从头播放，则不应勾选 **Continue to play on Switch change** 选项。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 您可以精准地定义同步点并使用淡变来确保无缝过渡。 |

### 将音乐对象与 State 和 Switch 关联

在将一个或多个 State Group（状态组）或 Switch Group（切换开关组）指派给 Music Switch Container（音乐切换容器）后，可将不同的音乐对象与相应的 State 或 Switch 组合关联。

每个特定的 State 或 Switch 组合称为一个 Path（路径）， Path 中还可能包括通配符。Paths are then associated with music objects that are children of the Music Switch Container.

**To assign music objects:**

1. 将音乐切换容器加载到音乐编辑器。

   此容器的状态组和切换开关组会显示在音乐切换容器的顶部区域中。
2. 在顶部每个 State Group 或 Switch Group 中选择一个状态。
3. 点击 **Add Path**（添加路径）按钮，在列表中创建条目。

   条目将显示在列表中，但尚未指派对象。
4. 点击条目上的 [...] 按钮，为条目指派音乐对象。

   对象浏览器将弹出，并显示 Music Switch Container 的子对象。
5. Select an object, and click OK.

**To assign music objects using drag and drop:**

1. 将音乐切换容器加载到音乐编辑器。

   此容器内的 State Group 和 Switch Group 会显示在 Music Switch Container 的顶部。
2. 将 Music Switch Container（音乐切换容器）的子对象拖到顶部的 Switch（切换开关）或 State（状态）上以与该子对象建立关联。

---