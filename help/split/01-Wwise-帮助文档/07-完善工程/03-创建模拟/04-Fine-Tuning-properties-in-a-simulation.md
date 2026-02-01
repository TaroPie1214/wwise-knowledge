# Fine-Tuning properties in a simulation

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [完善工程](../00-完善工程.md) > [创建模拟](00-创建模拟.md) > Fine-Tuning properties in a simulation

## Fine-Tuning properties in a simulation

您可以继续选择触发器，并播放相应的插播乐句来模拟游戏中的音乐。您可以直接在 Soundcaster 中修改各个声音、音乐和振动对象。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 如果您正在使用事件，则需要打开 Event Manager 来更改属性动作。有关使用属性和事件的详细信息，请参阅[“将 Action 添加到 Event”一节](../../04-与游戏互动/01-管理-Event/02-创建-Event.md#adding_actions_to_an_event "将 Action 添加到 Event")。 |

### 属性标志

您可能注意到，模块中的某些属性值旁边有若干个标志。这些标志显示出属性值是否链接到其它平台、属性值是否使用 RTPC 与游戏参数进行相关，以及是否对属性值应用了随机化器。有关在 Wwise 中如何使用这些标志的详细信息，请参阅[“属性标志”一节](../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/00-工程层级结构中的属性介绍.md#about_properties_in_project_hierarchy_property_indicators "属性标志")。

![](../../../../images/property_indicators.png)

有关链接/取消链接属性值、使用 RTPC 和将属性值随机化的详细信息，请参阅以下各节：

- [“Customizing object properties per platform”一节](../02-管理平台和语言版本/01-Authoring-across-platforms.md#customizing_object_properties_per_platform "Customizing object properties per platform")
- [“使用 Game Parameter 控制属性值”一节](../../04-与游戏互动/05-使用-RTPC/03-使用-Game-Parameter-控制属性值/00-使用-Game-Parameter-控制属性值.md "使用 Game Parameter 控制属性值")
- [“通过随机化属性值来改善播放”一节](../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/05-通过随机化属性值来改善播放.md "通过随机化属性值来改善播放")

除了这些属性标志外，Soundcaster 还包含播放标志，在播放期间，当发生特定行为或事件时，这些标志将变为蓝色。在主控制区和单个模块中可以查看它们。下表列出了 Soundcaster 中的这些额外属性和动作参数标志。

| 图标 | 名称 | 代表 |
| --- | --- | --- |
| |  | | --- | |  | | Delay | 延迟。已对事件、随机容器或序列容器应用了延迟。 |
| |  | | --- | |  | | Fade | 淡变。已对事件、随机容器或序列容器应用了淡变。 |

有关将这些属性添加到对象的详细信息，请参阅以下各节：

- [“"Continuous" Play Mode”一节](../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/02-定义-RandomSequency-Container-的播放行为/04-定义容器内对象的播放方式.md#playing_all_objects_within_container "\"Continuous\" Play Mode")
- [“设置 Event Action 的属性”一节](../../04-与游戏互动/01-管理-Event/02-创建-Event.md#setting_properties_for_an_event_action "设置 Event Action 的属性")

### Real-time mixing and positioning

在模拟中，您可以使用属性控件在播放前和播放期间执行以下操作：

- **实时混音**，以修改音量、音高、低通属性值。有关对这些属性进行混音的详细信息，请参阅[“定义相对属性（音量、音高、LPF、HPF）”一节](../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/02-定义相对属性（音量、音高、LPF、HPF）/00-定义相对属性（音量、音高、LPF、HPF）.md "定义相对属性（音量、音高、LPF、HPF）")。
- **修改定位**，以修改 2D 或 3D 声音或振动传播属性。有关定位的详细信息，请参阅[*定义定位*](../../05-使用声音和振动来提升游戏体验/02-定义定位/00-定义定位.md "定义定位")。

![](../../../../images/module_online.png)

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 要在 Property 或 Event Editor 中直接修改这些属性，双击模块的标题栏。 |

### Using the Reset function

在 Soundcaster 中试听一个 Event 模块后，您可能想要改变与该事件相关的对象属性。事件动作可暂时更改对象的属性。在更改属性前，应将属性恢复到它们的初始值。有关使用事件和事件动作的详细信息，请参阅[“处理 Event”一节](../../04-与游戏互动/01-管理-Event/03-处理-Event.md "处理 Event")。您可以分别重置各个模块的事件动作，也可以在 Soundcaster 的主控制区中重置所有模块的事件动作。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 在主控制区，您还可以清除在 Soundcaster 中的音乐轨，以防它们被强制播放。 |

**在主控制区中重置事件动作的方法是：**

1. 在主控区中，单击 Reset（重置）图标。

   此时将打开 Reset 菜单。
2. 在 Reset 菜单中，选择以下其中一项：

   - **Reset All** 可将所有对象恢复到原始设置。
   - **Reset All Random and Sequence Containers** 可清空已为对象触发的所有随机和序列动作。
   - **Reset All Game Parameters** 可清空已为对象触发的所有游戏参数。
   - **Reset All States** 可清空对象的所有 Set State 动作。
   - **Reset All Switches** 可清空已为对象触发的所有 Set Switch 动作。
   - **Reset All Set Mute** 可清空已为对象触发的所有静音动作。
   - **Reset All Set Voice Pitch** 可清空已为对象触发的所有声部音高设置动作。
   - **Reset All Set Voice Volume** 可清空已为对象触发的声部音量设置动作。
   - **Reset All Set Bus Volume** 可清空已为对象触发的总线音量设置动作。
   - **Reset All Set Voice Low-pass Filter** 可清空已为对象触发的所有低通滤波器动作。
   - **Reset All Bypass Effect**  可清空已为对象触发的所有旁通效果动作。
   - **Reset All Set Effect**（重置所有效果器设置）：清除所有已为对象触发的 Set Effect 动作。
   - **Reset All Music Tracks Force Usage** 不再强制播放 Soundcaster 中的特定声轨。
   - **Reset All Source Editor Play Cursors**（重置所有源编辑器播放光标）：清除 Source Editor 中手动触发的播放光标。
   - **Reset Attenuation Preview**（重置衰减预览）：将对象上设置的距离、角度、声障、声笼、衍射和透射值重置为其默认值。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 主控制区中的 Reset 功能包括其它命令。有关重置 Random Container 和 Sequence Container 的信息，请参阅[“Playing back Soundcaster modules”一节](02-Managing-playback-of-your-simulation/01-在-Soundcaster-中试听.md#playing_back_soundcaster_modules "Playing back Soundcaster modules")。要重置状态、切换开关和游戏参数，请参阅[“Simulating with game syncs”一节](03-Simulating-with-game-syncs.md "Simulating with game syncs")。 |

---