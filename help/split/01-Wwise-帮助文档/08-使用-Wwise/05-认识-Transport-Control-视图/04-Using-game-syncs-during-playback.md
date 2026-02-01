# Using game syncs during playback

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > [认识 Transport Control 视图](00-认识-Transport-Control-视图.md) > Using game syncs during playback

## Using game syncs during playback

在 Transport Control 中，您可以访问为工程创建的 Game Sync。To audition the States, Switches, and RTPCs as they are applied to your sounds, music, and motion objects, you can do any of the following.

### Enabling States during playback

在将对象加载到 Transport Control 中时，可从列表中选择对象采用的 State Group 和 State，来模拟播放期间游戏中发生的 State 和 State 变化。这意味着，在播放对象时，您可以试听 State 属性，还可以切换 State 来试听 State 更改。要了解有关创建 State、您将在 Transport Control 中试听的 State 属性和过渡，以及将对象指派到 State 的详细信息，请参阅以下各节：

- [“使用 State”一节](../../04-与游戏互动/03-使用-State/01-使用-State.md "使用 State")
- [“将 State 指派给对象和总线”一节](../../04-与游戏互动/03-使用-State/03-将-State-指派给对象和总线/00-将-State-指派给对象和总线.md "将 State 指派给对象和总线")

![](../../../../images/states_list_TConline.png)

**在播放期间启用状态的方法是：**

1. 将对象加载到 Transport Control 中。
2. 在 Game Syncs（游戏同步器）分区中，单击 State（状态）图标 (![](../../../../images/btn_states.png))。
3. 在 States 列表中，选择您要应用的 State。

   在播放期间，State 将作用于 Transport Control 内采用该 State 的所有声音。
4. 点击 **Play** 图标。

   播放期间将应用您选择的 State。在对象播放时，您可以继续切换 State 来模拟游戏。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若要切换回默认 State，请单击 Reset 图标并选择 **Reset All States**。 |

### Assigning Switches during playback

当对象加载到 Transport Control 时，您可以从 Switch Group 和 Switch 的列表中选择对象已指定的 Switch 和 Switch Group，以模拟播放期间游戏中将发生的 Switch 切换。这意味着在播放对象时，您可以切换 Switch，并试听切换。要了解有关创建 Switch 以及如何使用 Switch 的详细信息，请参阅以下章节：

- [“使用 Switch”一节](../../04-与游戏互动/04-使用-Switch/01-使用-Switch.md "使用 Switch")
- [“定义 Switch Container 的类型”一节](../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/03-定义-Switch-Container-的内容和行为.md#defining_type_of_switch_container "定义 Switch Container 的类型")

![](../../../../images/switches_TConline.png)

**在播放期间指定 Switch 的方法是：**

1. 将对象加载到 Transport Control 中。
2. 在 Game Syncs（游戏同步器）分区中，单击 Switch（切换开关）图标 (![](../../../../images/btn_switches.png))。
3. 从 Switch 列表中选择要应用的 Switch。

   状态于是应用到 Soundcaster 中采用该状态的所有对象上去了。
4. 点击 **Play** 图标。

   播放期间将应用您选择的 Switch。当播放对象时，您可以继续切换 Switch 来模拟游戏。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若要切换回在 Property Editor 中为 Switch Container 指定的默认 Switch，请单击 Reset 图标并选择 **Reset All Switches**。 |

### Changing game parameter values during playback

当对象加载到 Transport Control 时，相关的 RTPC 将显示在 Games Syncs 区。该区域提供一个滑块，您可以在播放对象时更改游戏参数。由于您已经将这些值映射至 Wwise 属性值，因此更改游戏参数值时，会自动改变对象属性值。这样就会模拟当游戏参数改变时发生了什么，从而确认属性映射在游戏中的效果。在将模块添加到 Soundcaster 并确定要试听的 Wwise 对象后，便可以测试映射到游戏参数（Game Parameter）的属性值。

- [“管理 RTPC 中使用的 Game Parameter”一节](../../04-与游戏互动/05-使用-RTPC/02-管理-RTPC-中使用的-Game-Parameter.md "管理 RTPC 中使用的 Game Parameter")
- [“将 Wwise 属性指派给游戏参数”一节](../../04-与游戏互动/05-使用-RTPC/03-使用-Game-Parameter-控制属性值/01-将-Wwise-属性指派给游戏参数.md "将 Wwise 属性指派给游戏参数")

![](../../../../images/PTC_Game_Params_online.png)

在模拟中，您可以试听这些属性在播放期间的变化。

**在播放期间修改游戏参数值的方法是：**

1. 将对象加载到 Transport Control 中。
2. 在 Game Syncs（游戏同步器）分区中，单击 Game Parameter（游戏参数）图标 (![](../../../../images/btn_RTPCs.png))。

   此时将显示已映射到对象的游戏参数。
3. 点击 **Play** 图标。

   当对象播放时，您可以使用 RTPC 滑块更改游戏参数值，以了解声音如何对更改做出反应。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若要将 Game Parameter 切换回其默认设置，请单击 Reset 图标并选择 **Reset All Game Parameters**。 |

|  |  |
| --- | --- |
| [备注] | 备注 |
| To bypass Game Parameter interpolation, hold Ctrl while using the RTPC slider in **Transport Control**, or the Game Parameter cursor in the RTPC tab of the Primary Editor. |

### Calling Triggers during playback

除了试听此对象外，您还可以从触发器列表中选择 Trigger 来试听 Stinger。插播乐句是简短的乐句，与当前播放的音乐进行叠加，混合播放。通过这种方式，您可以模拟游戏在关键时刻通过 Trigger 调用 Stinger 后，插播乐句与当前音乐叠加播放的情况。要了解有关创建触发器以及为它们创建您要在 Transport Control （播放控制）中试听的插播乐句的详细信息，请参阅以下各节：

- [*使用 Trigger*](../../04-与游戏互动/06-使用-Trigger.md "使用 Trigger")
- [*使用 Stinger*](../../06-创建互动音乐/08-使用-Stinger.md "使用 Stinger")

|  |
| --- |
|  |

**在播放期间调用触发器的方法是：**

1. 将音乐对象加载至 Transport Control 中。
2. 点击 **Play** 图标。

   随即播放加载至 Transport Control 中的音乐对象。
3. 在 Game Syncs（游戏同步器）分区中，单击 Trigger（触发器）图标来显示 Trigger 列表 (![](../../../../images/btn_triggers.png))。
4. 单击 **Call Trigger**（调用触发器）图标 (![](../../../../images/btn_play_arrow.png))。

   相应的插播乐句将在当前所播放的音乐对象之上播放。You can select other Triggers and play back the corresponding Stingers to simulate the music in the game.

---