# 创建 Event

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [与游戏互动](../00-与游戏互动.md) > [管理 Event](00-管理-Event.md) > 创建 Event

## 创建 Event

游戏中的所有对象都是由 Event 驱动的。事件创建过程涉及以下步骤：

- [“创建新的 Event”一节](02-创建-Event.md#creating_new_event "创建新的 Event")
- [“将 Action 添加到 Event”一节](02-创建-Event.md#adding_actions_to_an_event "将 Action 添加到 Event")
- [“将目标指派给 Event Action”一节](02-创建-Event.md#assigning_objects_to_event_actions "将目标指派给 Event Action")
- [“定义 Event Action 的作用域”一节](02-创建-Event.md#defining_scope_of_an_event_action "定义 Event Action 的作用域")
- [“设置 Event Action 的属性”一节](02-创建-Event.md#setting_properties_for_an_event_action "设置 Event Action 的属性")

为了给您提供额外的可控性和灵活性，事件可执行一个动作或一系列动作。事件的管理可使用事件编辑器来完成。

在跨平台创作时，您可能会需要从特定平台弃用某些动作。在默认情况下，所有 Action 都包含在 Event 中，但是您可以根据平台进行自定义。有关跨平台创作的详细信息，请参阅[“Excluding project elements from a platform”一节](../../07-完善工程/02-管理平台和语言版本/01-Authoring-across-platforms.md#excluding_project_elements_from_platform "Excluding project elements from a platform")。

如果您作为团队的一份子参与同一工程，则可以将事件指派给不同的工作单元，以便各个团队成员都可同时处理不同事件。有关处理工作单元的详细信息，请参阅[“将工程分成 Work Units”一节](../../03-设置工程/04-Working-with-a-team/01-将工程分成-Work-Units.md "将工程分成 Work Units")。

### 创建新的 Event

创建新 Event 时，可以执行以下操作之一：

- 创建不包含动作或目标的空 Event。
- 创建包含特定动作的事件。
- 创建不包含动作或目标的空 Event。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 您还可以在 Event Viewer（事件查看器）中通过右键点击来创建事件。在通过 Event Viewer 添加事件时，您还必须将事件指派给特定工作单元。 |

**创建空 Event 的方法如下：**

1. 在 Project Explorer 中，切换至 Events 选项卡。
2. 执行以下操作之一：

   - 选择工作单元或虚拟文件夹，然后点击 Project Explorer 工具栏中的 **Event** 图标。
   - 右键点击工作单元或虚拟文件夹，然后从快捷菜单中选择 **New Child** > **Empty Event**（空事件）。

   新事件已在您在 Project Explorer 中选择的工作单元或虚拟文件夹内创建成功。
3. 将默认名称替换为最适合事件的名称。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 事件名称中只能包含不带变音符号的的罗马字母、数字和下划线。名称还必须以字母或下划线开头。 |

**创建包含动作的事件的方法如下：**

1. 在 Project Explorer 中，切换至 Events 选项卡。
2. 右键点击要添加事件的工作单元或虚拟文件夹。
3. 从快捷菜单中，选择 **New Child** 以显示事件动作列表。
4. 在 Action 列表中选择 Action 类别或 Action。（选择前者时，将显示包含一系列 Action 的子菜单；请从中选择一个 Action。）

   包含所需动作的新事件已在您在 Project Explorer 中选择的工作单元内创建成功。
5. 将默认名称替换为最适合事件的名称。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 事件名称中只能包含不带变音符号的的罗马字母、数字和下划线。名称还必须以字母或下划线开头。 |

**创建包含 Action 和目标的事件方法如下：**

1. 在 Project Explorer 的 Audio 选项卡中，选择事件中要包含的一个或多个目标，然后右键单击选项。

   此时将会显示快捷菜单。
2. 选择以下选项之一：

   - **New Event**（新建事件），创建包含所需对象的事件。
   - **New Events (One event per object)**（新建事件（每个对象一个事件）），为每个所选对象创建一个事件。
   - **New Event (Single event for all objects)**（新建事件（所有对象一个事件）），创建一个包含所有所选对象的事件。
3. 在 Action 列表中选择 Action 类别或 Action。（选择前者时，将显示包含一系列 Action 的子菜单；请从中选择一个 Action。）

   于是我们在事件编辑器中创建成功了若干个事件，里面包含所选的动作和对象。
4. 在 **Name**（名称）字段中，将默认名称替换为最适合事件的名称。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 事件名称中只能包含不带变音符号的的罗马字母、数字和下划线。名称还必须以字母或下划线开头。 |

### 将 Action 添加到 Event

必须定义事件中要包含的 Action。每个事件都可包含若干个动作。

**将动作添加到事件的方法如下：**

1. 在 Event Editor 中，单击 **Add >>** 按钮。

   此时将会显示动作列表。
2. 从 Action 列表中选择 Action 或 Action 类别。（选择前者时，将显示包含一系列 Action 的子菜单；请从中选择一个 Action。）

   所选的 Action 将被添加到事件。

   现在，可以给事件中的 Action [指派目标](02-创建-Event.md#assigning_objects_to_event_actions "将目标指派给 Event Action")或者继续为事件添加 Action。

可通过几种其它方式将 Action 添加到事件，如：

- 将 Project Explorer 中的一个或多个元素拖动到 Event Editor 的 Event Action 窗格空白处。随即将生成适用于元素的 Action，但是可以自由更改它。
- 在 Event Editor 的 Event Action 窗格空白处打开快捷菜单后，从其中选择 **New Action**选项。显示的选项与单击 **Add >>** 按钮相同，后者请参阅上面的“将 Action 添加到 Event”列表。
- 可以使用标准 Copy 和 Paste 快捷方式或快捷菜单选项，同时复制和粘贴若干个 Action。

### 将目标指派给 Event Action

大多数事件动作必须指派给特定对象、结构或游戏同步器。包含一个或多个 Action 但未关联目标的事件称为 Orphaned Event（落单事件）。这些落单事件将显示在 Event Viewer 的 Orphans（落单）选项卡中。这些落单事件也会在您为工程生成完好度报告（Integrity Report）时显示。

为了帮助您识别 Event 中对象的状态，对象名称将以以下一种颜色显示：

- **白色** —— 表示包含的对象。（在当前平台中。）
- **灰色** —— 表示未包含的对象。（在当前平台中。）
- **红色** —— 表示缺失关联对象的事件动作或当前工程缺失的对象。
- **黄色** —— 表示目前从当前工程中卸载的对象。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 将音乐对象指派给特定 Action（例如 Trigger、Set Switch 以及 Set State）时，请注意这些 Action 可能会延迟，这是因为在音乐对象中可能已经预先定义了这些特定 Action 发生的时刻。 |

**将目标指派给 Event Action 的方法如下：**

1. 在 Event Editor 中，选择要为其指派目标的 Action。
2. 点击 **Browse**（浏览）。

   此时将会显示 Project Explorer - Browser。
3. 浏览层级结构并选择要指派给动作的对象。
4. 单击 **OK**（确定）。

   对象于是指派给 Action 了。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 您还可以通过将某对象从 Project Explorer 拖至 Event Action 列表中的动作，来将该对象指派给相应事件动作。 |

### 定义 Event Action 的作用域

创建事件时必须定义每个 Action 的 Scope。Scope 会指定 Action 在游戏对象中作用的范围。Scope 会指定 Action 在游戏对象中作用的范围。对于某些 Action，您可以选择 Scope；对于其它 Action，Scope 是预先定义好的。

例如，假定您为玩家离开游戏进入菜单这种情况创建了一个事件。This Event will play the “Enter\_Menu” sound, pause all the sounds related to the player, and set the State to “Menu.” In turn, the "Menu" State is set to decrease the volume of the Main Audio Bus by 20 dB, but to increase the volume of the "Music" Audio Bus by 20 dB.

这些事件中各个事件的范围如下所示：

| 事件动作类型 | Scope（作用域） | 备注 |
| --- | --- | --- |
| Play > Menu\_Enter | Game Object | 由于 Play Event 总是由一个游戏对象触发，作用域会设置为 Game Object。 |
| Pause All | Global 或 Game Object | 在该场景中，玩家角色即为调用 Event 的 Game Object。暂停玩家相关的声音，可以让您在阅读菜单时不受干扰。因此，虽然可以将 Scope 设置为 Global，但在这种情况下，使用 Game Object 范畴将允许玩家仍然听到游戏中的其它声音。 |
| Set State > Menu | Global | Set State 的作用域始终为 Global，原因是工程中所有使用该 State 的地方都会响应状态变化。In our scenario, we have a "Menu" State set up on the Main Audio Bus and our "Music" Audio Bus. 让前者音量降低，后者音量增加。  |  |  | | --- | --- | | [备注] | 备注 | | 本示例旨在对 Scope 进行说明，并非最佳音频设计选择。实际上，如果两条总线都是 [Mixing](../../07-完善工程/01-管理输出/11-完成终混/01-了解总线图标和处理状态.md "了解总线图标和处理状态") Bus，在音量更改时会出现非常短的延时，可能会发出类似 click 或 buzz 的噪声。此外，如果“Music”Audio Bus 上存在线性效果器，则不一定能够保持该总线的音量恒定。不过，在该情况下，我们还可以使用 Bypass Effect Action。 | |

  

**定义 Event 的作用域：**

1. 从 **Scope** 列表中，选择以下选项之一：

   - **Game object**，将事件动作作用于触发事件的游戏对象。
   - **Global**，将事件动作作用于所有游戏对象。

### 设置 Event Action 的属性

各个事件动作都有一组可用于进一步美化游戏声音、音乐和振动的相关属性。

各个动作都包含不同的属性，但这些属性分别属于以下类别之一：

- 延迟
- Transitions（过渡）
- 旁通效果器属性
- 音量、音高、LPF、游戏参数、跳转、状态或切换开关设置。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 在设置包含音乐对象的某些事件动作的延迟属性（例如触发、设置状态以及设置切换开关）时，请注意实际延迟可能会比指定值要长，这是因为在音乐对象中可能已经预先定义了这些动作发生的时刻。 |

**设置事件动作属性的方法如下：**

1. 在 Event Editor 中，从 Event Action 窗格中选择 Action。

   与所选 Action 关联的属性将显示在 Action Property 窗格中（右侧）。
2. 根据需要为关联的属性指定值。

### 播放 Event

在创建过程中，您随时都可以试听事件。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 为了试听振动，相应振动设备必须连接到您的电脑。 |

**播放事件的方法如下：**

1. 执行以下操作之一：

   - 在 Event Viewer 中选择一个事件。
   - 将事件加载到 Event Editor（事件编辑器）中。

   事件于是加载到 Transport Control 中来了。
2. 点击 Transport Control 中的 **Play**（播放）图标。

   事件已播放。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 您还可以使用 Soundcaster（声音选角器）播放事件。有关使用 Soundcaster 的详细信息，请参阅[“在 Soundcaster 中试听”一节](../../07-完善工程/03-创建模拟/02-Managing-playback-of-your-simulation/01-在-Soundcaster-中试听.md "在 Soundcaster 中试听")。 |

---