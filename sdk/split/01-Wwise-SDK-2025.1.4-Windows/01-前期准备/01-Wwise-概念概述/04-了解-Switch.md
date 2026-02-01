# 了解 Switch

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

了解 Switch

在游戏中，通常要根据游戏的当前状态在不同的游戏场景中播放不同的声音。比如，若角色在混凝土地面上奔跑，然后走到草地上，脚步声就要随着地面的转变而变化。对此，可使用 Switch 来在不同的声音之间切换。

借助 Switch 和 Switch Container，声音设计师可定义要在各种情形下播放哪些声音。您可以在 Wwise 设计工具中针对不同情形创建多个 Switch Group 以便在不同的声音之间切换。每组可以包含多个 Swtich。然后，Switch Container 便可使用这些 Switch Group 并将声音与各个 Switch 一一关联。

比如，声音设计师可在 Wwise 设计工具中为游戏创建以下 Switch Group 和 Switch：

- Ground\_Material（地表材质）
  - Concrete（混凝土）
  - Tiles（磁砖）
  - Metal（金属）
  - Sand（沙子）
  - Water（水）
- Machine\_Mode（机器模式）
  - Standby（待机）
  - Idle（闲置）
  - Medium（中）
  - High（高）

为了让这些 Switch 按照预期运作，游戏必须在必要时为各个 Switch Group 正确设置当前 Switch。

如需详细了解声音设计师如何看待 Switch 和 Switch Container，请参阅[定义 Switch Container 的内容和行为](https://www.audiokinetic.com/library/edge/?source=Help&id=defining_contents_and_behavior_of_switch_containers)。

如需简要了解 Switch 集成，请参阅 [集成详情——切换开关](soundengine_switch.html) 章节。