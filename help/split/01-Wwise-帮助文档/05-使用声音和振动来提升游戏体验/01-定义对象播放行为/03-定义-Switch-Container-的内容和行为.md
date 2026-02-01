# 定义 Switch Container 的内容和行为

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../00-使用声音和振动来提升游戏体验.md) > [定义对象播放行为](00-定义对象播放行为.md) > 定义 Switch Container 的内容和行为

## 定义 Switch Container 的内容和行为

通过使用 Switch Container（切换容器），您可以根据游戏内的不同条件变化来为对象编组。在 Switch Container（切换容器）中，Swtich（切换开关）或State（状态）被用来代表各个不同条件。例如，可以为角色行走时的所有不同表面材质创建一个切换容器。容器中可能包含与水泥、木材、草地、雪地及游戏中角色可能踩到的其他表面材质对应的 Switch。

|  |
| --- |
|  |

每个切换开关/状态对应于与该条件有关的声音对象。例如，所有混凝土上的脚步声可编组至“Concrete”切换开关，所有木头上的脚步声可编组至“Wood”切换开关，以此类推。当游戏调用切换容器时，Wwise 会验证当前哪个 Switch/State 处于激活状态，以决定播放哪个容器或声音。

下图说明当事件调用“Footsteps”切换容器时发生的情况。该容器根据游戏中角色可行走的不同表面材质将声音编组。在本例中有两个切换开关：Grass 和 Concrete。当该事件调用切换容器时，角色走在草地上（切换开关 = Grass），因此会播放草地上的脚步声。随机容器用于将切换开关内的脚步声编组，因此当角色每次踏到同一表面时，都会播放不同的声音。

|  |
| --- |
|  |

### 定义 Switch Container 的类型

创建切换容器时，您必须定义该容器应该是基于状态、切换开关，还是 RTPC。一方面，您可以在切换容器的属性编辑器中选择切换开关或状态；另一方面，RTPC 可以关联至 Switch Group Property Editor 中的切换开关组。有关 RTPC（实时参数控制）如何与切换开关进行关联的详细信息，请参阅[“将 Game Parameter 值映射到 Switch”一节](../../04-与游戏互动/04-使用-Switch/02-将-Game-Parameter-值映射到-Switch.md "将 Game Parameter 值映射到 Switch")。

决定切换开关容器类型后，您还必须为该容器指派切换开关或状态组。这定义了可供指派对象所用的 Switch/State/RTPC。

在为容器指派状态或切换开关组，或将 RTPC 关联至切换开关之前，您必须先创建它们。有关创建切换开关组、状态组和 RTPC 的信息，请参阅：

- [“使用 State”一节](../../04-与游戏互动/03-使用-State/01-使用-State.md "使用 State")
- [“使用 Switch”一节](../../04-与游戏互动/04-使用-Switch/01-使用-Switch.md "使用 Switch")
- [“Creating Game Parameters”一节](../../04-与游戏互动/05-使用-RTPC/02-管理-RTPC-中使用的-Game-Parameter.md#creating_game_parameter "Creating Game Parameters")

**定义 Switch Container 的类型：**

1. 将 Switch Container 容器加载至 Property Editor 中。
2. In the **Switch Group or State Group**, click **Set SwitchGroup/StateGroup**, and select the Switch
   or State Group to assign to the container.

   In the Primary Editor, the Assigned Objects column is populated with the
   Switches/States of that group.
3. In the Property Editor, click **Set Default Switch/State**,
   and select the Switch/State to be played when the game cannot identify a
   specific Switch or State.

### 定义 Switch Container 的播放行为

由于切换开关或状态可在游戏中随时更改，因此您需要决定对象是立即应用更改，还是下次播放切换容器时再应用更改。Wwise 提供以下播放模式：

- Step
- Continuous

您可针对 one-shot 声音（一次播放一个的声音，如脚步声）使用 **Step** 选项。而 **Continuous** 选项对于持续循环的对象（如单板滑雪声）则更为实用。

**定义切换容器播放模式的方法如下：**

1. 将 Switch Container 容器加载至 Property Editor 中。
2. For the **Play Mode** property, select one of the following
   options:

   - **Step**，不论播放过程中切换开关是否更改，仅在触发新的播放事件后播放不同的对象。
   - **Continuous**，只要检测到新的 Switch/State，就播放新对象。当选择 Continuous 时，切换播放对象不需要新的播放事件。

### 为 Switch 和 State 添加和移除对象

您必须将 Switch Container（切换开关容器）内的对象指派给特定的 Switch 或 State（状态）。

You can assign objects to switches by adding objects and other containers to the **Assigned Objects** column of the Primary Editor. 您可以按住 Ctrl 或 Shift 键同时点击多个对象，然后同时添加或移除它们，来更快地指派对象。若将多个对象指派给某个 Switch，则会在 Wwise 内和游戏中运行时同时予以播放。

在大多数情况下，会指派 Switch Container（切换开关容器）中已有的对象。不过，也可能需要将对象直接从 Project Explorer（工程资源管理器）的 Audio（音频）选项卡拖到 Switch/State（切换开关/状态）上。这些对象将被从当前位置移动到切换容器中。如果您要创建对象的副本，而不是移动它，则可按住 Ctrl 键，同时将该对象从 Project Explorer 的 Audio 选项卡中拖拽至 Assigned Objects 面板中的 Switch/State 上。

**为 Switch/State 指派/移除对象的方法如下：**

1. 将 Switch Container 容器加载至 Property Editor 中。

   容器内的对象将显示在 Contents Editor 中。
2. To assign an object to a Switch/State, drag an object from the **Contents** pane to a Switch/State in the **Assigned Objects** column of the Primary Editor.

   对象将被添加至 Switch/State。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 必须将对象直接拖拽至切换开关或状态的名字上。 |
3. To remove an object from a Switch/State, click the object you want to remove in the
   **Assigned Objects** column.
4. 按 **Delete** 键。

   该对象将从 Switch/State 中移除，但仍保留在 Contents 面板中。

### 在 Switch 或 State 之间移动对象

如果首次将对象指派至 Switch/State 时出现错误，或是要移动对象，您则可以随时将它们移动至新位置。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 要同时移动多个对象，则请按住 Ctrl 键并点击各个对象，然后将它们拖至新位置。 |

**在 Switch 或 State 之间移动对象：**

1. 在 Contents Editor 的 Assigned Objects 面板中，选择要移动的若干个对象。
2. 将对象拖拽至新的 Switch/State。

   对象将被指派至新的 Switch/State。

### 定义 Switch Container 所含对象的播放行为

由于在游戏内，切换开关和状态会经常变化，因此您需要决定在发生变化时，切换容器内的各个对象将如何反应。可以选择以下播放行为：

- **Play** —— 决定是每次切换被触发时都重新播放对象，还是仅当触发的 Switch/State 发生变化时才重新播放对象。
- **Across Switches**（多个切换开关）：决定在触发新的 Switch/State 时是否继续播放指派给多个 Switch 的同一对象。
- **Fade In**（淡入）：决定在触发新的 Switch/State 时是否要淡入到新的对象。
- **Fade Out**（淡出）：决定在触发新的 Switch/State 时是否要从现有对象淡出。

**定义切换容器内对象播放行为的方法如下：**

1. 将 Switch Container 容器加载至 Property Editor 中。

   容器内的对象将显示在 Contents Editor 中。
2. 在 Play 列中选择 **1st only** 选项，那么将仅当 Switch/State 有变化时才播放该对象。如果您不勾选 1st only 选项，那么游戏每次触发切换容器时，无论 Switch/State 是否有变化，都将播放该对象。
3. 在 Across Switches 列中选择 **Continue to play** 选项，那么如果音频对象同时指派至源和目标 Switches/States ，则在 Switch/State 变化期间对象将继续播放。如果您不勾选 Continue to play 选项，那么对象将停止并从开头重新播放。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | Across Switches 选项仅适用于 Continuous 播放模式。 |
4. 如果您希望在 Switch/State 发生变化时让新对象淡入，则请在 Fade-In 文本框中输入时间长度。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | Fade-In 选项仅在 Continuous 播放模式下可用。 |
5. 如果您希望在 Switch/State 发生变化时让现有对象淡出，则请在 **Fade Out** 文本框中输入时间长度。

---