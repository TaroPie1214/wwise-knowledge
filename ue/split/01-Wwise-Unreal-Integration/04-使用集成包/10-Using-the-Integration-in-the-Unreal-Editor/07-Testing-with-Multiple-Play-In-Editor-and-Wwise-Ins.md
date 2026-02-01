# Testing with Multiple Play In Editor and Wwise Instances

|  |
| --- |
| Wwise Unreal Integration Documentation |

Testing with Multiple Play In Editor and Wwise Instances

If you are testing multiplayer audio in Unreal, you can run separate Play in Editor (PIE) sessions with a separate Wwise instance for each session. 对此，可使用 Unreal 中的多人游戏选项来实现。If you disable **Run Under One Process** in the [Play In Editor Multiplayer Options](https://dev.epicgames.com/documentation/en-us/unreal-engine/play-in-editor-multiplayer-options-in-unreal-engine), each PIE instance uses an independent instance of Wwise. Be aware that this approach consumes more system resources and might affect performance.

You can profile the different sessions in Wwise (see [Profiling](https://www.audiokinetic.com/library/edge/?source=Help&id=profiling)). Each PIE session appears in the list of game systems to which the profiler can connect, as described in [Connecting to a Local/Remote Game System](https://www.audiokinetic.com/library/edge/?source=Help&id=connecting_to_local_remote_pc_or_game_console). However, it is not possible to know in advance which session corresponds to a specific player.