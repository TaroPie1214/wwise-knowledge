# 了解 Event

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

了解 Event

Event 由声音设计师在 Wwise 设计工具中创建，并可指定要针对 Wwise 对象执行哪些操作。比如，某个 Event 可能包含针对 *Bird1* 声音的 Play 动作和针对 *Bird2* 声音的 Stop 动作。另一 Event 可能包含将 *CarEngine* 声音的相对音量偏置设为 -2 的 Set Volume 动作和将 *Ground\_Material* Switch Group 切换为 *Tiles* 的 Set State 动作。

Event 会被打包到 SoundBank 中以便在游戏中加载。然后，游戏的代码便可触发 Event。比如，在玩家进入厨房时，代码可触发将 *Ground\_Material* Switch Group 设为 *Tiles* 的 Event。

在将 Event 集成到游戏中后，声音设计师可继续更改或调节其所含的动作或指向的对象。因为游戏触发的仍是同一 Event，所以无需另外编程或重新编译代码，所做的更改就会在游戏中生效。

如需详细了解声音设计师如何看待 Event，请参阅[管理 Event](https://www.audiokinetic.com/library/edge/?source=Help&id=managing_events) 章节。

如需简要了解 Event 集成，请参阅 [集成详情——事件](soundengine_events.html) 章节。