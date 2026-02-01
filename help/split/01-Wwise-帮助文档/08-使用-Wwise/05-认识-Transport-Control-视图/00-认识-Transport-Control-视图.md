# 认识 Transport Control 视图

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > 认识 Transport Control 视图

## 认识 Transport Control 视图

在编辑声音、音乐或振动属性时，您需要能够试听您的作品。在 Wwise 中，当您选择一个声音、容器或事件时，它会自动加载到 Transport Control（播放控制）中，您可以在其中试听它。对象的名称将与它的关联图标一起显示在标题栏。

Transport Control 包括两个不同区域：

![](../../../images/TC_Sections.png)

|  |  |
| --- | --- |
|  | [“Playback Control area”一节](00-认识-Transport-Control-视图.md#playback_control_area "Playback Control area") |
|  | [“Game Syncs area”一节](00-认识-Transport-Control-视图.md#game_syncs_area "Game Syncs area") |

|  |  |
| --- | --- |
| [备注] | 备注 |
| Dialogue Events are not loaded into the Transport Control; however, the objects assigned to a path can be loaded. |

## Playback Control area

Transport Control 包含与播放音频相关的传统控件，例如播放、停止和暂停按钮。您还可以使用 Transport Control 设置确定播放对象的方式。通过选择或取消选择这些设置，您可以指定是播放原始对象还是经过转码的对象，以及是否播放已从当前平台弃用的对象。

![](../../../images/PTC_play_controls_online.png)

|  |  |
| --- | --- |
| [备注] | 备注 |
| You cannot play back a Property Container or bus, so they are not loaded into the Transport Control when selected. |

Playback Control 区域还包含一系列标志，当特定属性或行为先前已作用于正在播放的对象时，它们会改变颜色。下表列出了 Transport Control 中的属性和动作参数指示器。

| 图标 | 名称 | 代表 |
| --- | --- | --- |
| |  | | --- | |  | | Delay | 已对事件、随机容器和序列容器中的对象应用延迟。 |
| |  | | --- | |  | | Fade | 已对事件、随机容器或序列容器中的对象应用渐变。 |

有关编辑对象的这些属性的详细信息，请参阅以下各节：

- [“"Continuous" Play Mode”一节](../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/02-定义-RandomSequency-Container-的播放行为/04-定义容器内对象的播放方式.md#playing_all_objects_within_container "\"Continuous\" Play Mode")
- [“设置 Event Action 的属性”一节](../../04-与游戏互动/01-管理-Event/02-创建-Event.md#setting_properties_for_an_event_action "设置 Event Action 的属性")

另外，请记得进行声音设计时可以使用 Play-Bypass Properties 快捷方式。

Hold Shift while clicking Play to have Wwise play the loaded sound while bypassing its properties. That is, somewhat like a PFL (Pre-Fader Listen) found in some DAWs, Wwise will play the object without its hierarchical properties (including such things as volume, pitch, filters, delays, Effects, Auxiliary Sends, Attenuation Curves, RTPC curves, States, positioning, and bus routing), but with its source edits (such as fades, trims, and loop points) still intact.

|  |  |
| --- | --- |
| [警告] | 警告 |
| If you use the Play - Bypass properties shortcut, the resulting sound might be uncomfortably loud or off-pitch. |

单击 Transport 的 Play 按钮会从播放光标的位置播放片段。当播放光标前进时单击 Play 按钮将添加新的播放光标，并从第一个播放光标的起始位置同时播放。

## Game Syncs area

除传统播放控件外，Transport Control 还有一个 Game Sync 区，其中包含与当前选定对象相关的所有 State、Switch、Trigger 和 RTPC。您可以使用 Transport Control 作为微型模拟器，来测试您的声音、音乐和振动，以及模拟在游戏中的变化。在播放期间，您可以在 State 和 Switch 之间切换，并试听游戏参数及其映射值。

![](../../../images/PTC_multi_purpose_area_online.png)

有关使用 Game Sync 的详细信息，请参阅以下各节：

- [*使用 State*](../../04-与游戏互动/03-使用-State/00-使用-State.md "使用 State")
- [“为 Switch 和 State 添加和移除对象”一节](../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/03-定义-Switch-Container-的内容和行为.md#adding_and_removing_objects_from_switch_state "为 Switch 和 State 添加和移除对象")
- [“在 Switch 或 State 之间移动对象”一节](../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/03-定义-Switch-Container-的内容和行为.md#moving_objects_between_switches_states "在 Switch 或 State 之间移动对象")
- [“管理 RTPC 中使用的 Game Parameter”一节](../../04-与游戏互动/05-使用-RTPC/02-管理-RTPC-中使用的-Game-Parameter.md "管理 RTPC 中使用的 Game Parameter")
- [*使用 Trigger*](../../04-与游戏互动/06-使用-Trigger.md "使用 Trigger")

---