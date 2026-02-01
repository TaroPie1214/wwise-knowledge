# 了解 State

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

了解 State

在游戏的状态发生变化时，我们一般希望声音能对此予以反映。比方说，当玩家角色浸没在水中时，枪声、背景音乐和身体移动的声音听起来要像在水下发出的一样。对此，可使用 State 来让音频与当前游戏情境协调一致。

With States, sound designers can create different sets of properties for Busses, Containers, and Sounds to use depending on the current game state. State 可能会影响到的属性包括 Volume、Pitch 和 Low-Pass Filter。

您可以在 Wwise 设计工具中创建 State Group 来表示不同类型的游戏状态。这些 State Group 可包含多个 State。比如，声音设计师可在 Wwise 设计工具中为游戏创建以下 State Group 和 State：

- Player\_Environment（玩家环境）
  - Ground（地面）
  - Underwater（水下）
  - Car（汽车）
- Slow\_Time（时间减速）
  - On（开）
  - Off（关）

为了让这些 State 按照预期运作，游戏必须在必要时为各个 State Group 正确设置当前 State。

如需详细了解声音设计师如何看待 State，请参阅[使用 State](https://www.audiokinetic.com/library/edge/?source=Help&id=working_with_states)。

如需简要了解如何将 State 集成到游戏中，请参阅 [集成详情—— State（状态）](soundengine_states.html) 章节。