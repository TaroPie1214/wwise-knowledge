# 了解环境和 Game-defined Auxiliary Sends

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

了解环境和 Game-defined Auxiliary Sends

您可以使用 Game-defined Auxiliary Sends 来根据游戏中声音所在的位置为其应用效果器。 为此，须在对象属性或其沿用属性的父对象中设置 **Use game-defined aux sends** 选项。

在 Wwise 设计工具中，声音设计师可定义多个要在游戏中使用的 Game-defined Auxiliary Sends（如 Hangar、Tunnel 等）。

比如，各个 Game-defined Auxiliary Sends 可代表具有不同参数集的环境混响效果器。然后，便可由 Auxiliary Bus 来表示 Wwise 工程中的各种环境。

同一 Auxiliary Bus 总线下的所有声音会先混合在一起再应用效果器。您可以为各个游戏对象设置不同的音量。

另外，还可使用声障和声笼来修改声音及其 Game-defined Auxiliary Sends 效果器传播至听者的方式（详见 [声障、声笼及 Game-defined Auxiliary Sends](soundengine_obsocc.html) 章节）。

如需详细了解 Wwise 设计工具中的 Auxiliary Bus，请参阅以下主题：

- "The Main Audio Bus hierarchy" under [Building the structure of output busses](https://www.audiokinetic.com/library/edge/?source=Help&id=building_structure_of_output_busses)
- [利用效果器重构声学环境](https://www.audiokinetic.com/library/edge/?source=Help&id=using_effects_to_implement_environment_acoustics)下的“理解发送”

如需简要了解如何结合 SDK 使用 Game-defined Auxiliary Sends，请参阅 [集成详情——环境和游戏定义的辅助发送](soundengine_environments.html) 章节。