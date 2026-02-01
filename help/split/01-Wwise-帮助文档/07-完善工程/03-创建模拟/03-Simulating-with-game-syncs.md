# Simulating with game syncs

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [完善工程](../00-完善工程.md) > [创建模拟](00-创建模拟.md) > Simulating with game syncs

## Simulating with game syncs

在 Soundcaster 中，您为工程创建的游戏同步器（Game Sync）应有尽有，都可供试用。在游戏和 Wwise 中，您都可以试听状态、切换开关、RTPC 和触发器施加在声音上的效果。通过连接到游戏并将相应模块添加到 Soundcaster，您可以使用游戏同步器随着游戏动作实时对它们进行试听、测试和混音。

选中 Show All 按钮时，创建的所有游戏同步器都将显示在 Soundcaster 的 Game Syncs 区域。否则将只显示与 Soundcaster 中加载的 Wwise 对象相关联的游戏同步器。

![](../../../../images/Soundcaster_game_syncs.png)

### Enabling States during playback

在将模块添加到 Soundcaster 会话中并确定要播放的 Wwise 对象后，您可以在播放期间启用状态（State）。在将对象拖到 Soundcaster 中时，为模块中的 Wwise 对象所启用的状态组和状态会添加到 State 列表。如果未显示状态，点击 **Show All**。然后，所有状态组和状态都会显示在 States 区域。要了解有关创建状态和指定对象到状态的详细信息，请参阅以下章节：

- [“使用 State”一节](../../04-与游戏互动/03-使用-State/01-使用-State.md "使用 State")
- [“将 State 指派给对象和总线”一节](../../04-与游戏互动/03-使用-State/03-将-State-指派给对象和总线/00-将-State-指派给对象和总线.md "将 State 指派给对象和总线")

**在播放期间启用状态的方法是：**

1. 在 States 列表中，选择您要应用的 State。

   该状态将应用于 Soundcaster 中的所有采用了该状态的 Wwise 对象。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若要切换回为 Switch Container 指定的默认 State，请在主控区中单击 Reset 图标并从菜单中选择 **Reset All States**。 |

### Assigning Switches during playback

在将模块添加到 Soundcaster 会话中并确定您要试听的 Wwise 对象后，您可以启用在播放期间要应用的切换开关。在将对象拖到 Soundcaster 中时，应用到 Wwise 对象的切换开关组和切换开关会添加到 Switches 区域。如果未显示切换开关，则点击 **Show All**。于是所有切换开关组和切换开关都将显示在 Switches 区域。要了解有关创建 Switch 以及如何使用 Switch 的详细信息，请参阅以下章节：

- [“使用 Switch”一节](../../04-与游戏互动/04-使用-Switch/01-使用-Switch.md "使用 Switch")
- [“定义 Switch Container 的类型”一节](../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/03-定义-Switch-Container-的内容和行为.md#defining_type_of_switch_container "定义 Switch Container 的类型")

**将切换开关指定到模块的方法是：**

1. 从 Switch 列表中选择要应用的 Switch。

   状态于是应用到 Soundcaster 中采用该状态的所有 Wwise 对象上去了。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若要切换回为 Switch Container 指定的默认 Switch，请在主控区中单击 Reset 图标并从菜单中选择 **Reset All Switches**。 |

### Simulating changes in Game Parameters

采用所选切换开关组的切换容器将播放对应于所选切换开关的 Wwise 对象。在将模块添加到 Soundcaster 并确定要试听的 Wwise 对象后，便可以测试映射到游戏参数（Game Parameter）的属性值。

- [“管理 RTPC 中使用的 Game Parameter”一节](../../04-与游戏互动/05-使用-RTPC/02-管理-RTPC-中使用的-Game-Parameter.md "管理 RTPC 中使用的 Game Parameter")
- [“将 Wwise 属性指派给游戏参数”一节](../../04-与游戏互动/05-使用-RTPC/03-使用-Game-Parameter-控制属性值/01-将-Wwise-属性指派给游戏参数.md "将 Wwise 属性指派给游戏参数")

要了解有关创建游戏参数和将属性值映射到它们的详细信息，请参阅以下各节：如果没有显示游戏参数，请点击 **Show All**。您创建的所有游戏参数都将显示在 RTPCs 区域。滑杆代表游戏参数值的值域。在将这些值映射到 Wwise 属性值后，在更改这些参数值时将自动更改属性值。

在模拟中，您可以试听这些属性在播放期间的变化。

**在播放期间修改游戏参数值的方法是：**

1. 在播放期间，使用 RTPC 滑杆更改游戏参数值。

   相关的对象属性将根据您在游戏参数和对象属性之间创建的映射而改变。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 若要将 Game Parameter 切换回其原始设置，请在主控区中单击 Reset 图标并从菜单中选择 **Reset All Game Parameters**。 |

### Calling Triggers during a simulation

将模块添加到 Soundcaster 并确定要试听的 Wwise 对象后，您还可以测试为音乐触发 Stinger（插播乐句）的 Trigger（触发器）。通过这种方式，您可以模拟游戏在关键时刻通过 Trigger 调用 Stinger 后，插播乐句与当前音乐叠加播放的情况。要了解有关创建触发器以及为它们创建您要在 Soundcaster 中试听的插播乐句的详细信息，请参阅以下各节：

- [*使用 Trigger*](../../04-与游戏互动/06-使用-Trigger.md "使用 Trigger")
- [*使用 Stinger*](../../06-创建互动音乐/08-使用-Stinger.md "使用 Stinger")

在将对象拖到 Soundcaster 中时，相关触发器会添加到 Triggers 区域。如果未显示触发器，则点击 **Show All**。您创建的所有触发器将显示在 Triggers 区域。

**在播放期间调用触发器的方法是：**

1. 在模块中的音乐对象播放时，从 Triggers 列表中选择您要试听的触发器。

   |  |
   | --- |
   |  |
2. 点击 **Call Trigger** 图标。

   相应的插播乐句将在当前所播放的音乐对象之上播放。您可继续选择其它触发器，播放其相应的插播乐句，以模仿游戏中插播乐句的播放。

---