# 使用 RTPC

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [与游戏互动](../00-与游戏互动.md) > 使用 RTPC

## 使用 RTPC

为了在游戏中实现更多动态效果，可能需要将特定对象属性与游戏中的某些参数值绑定。在 Wwise 中，您可以使用实时参数控制（RTPC）来实现这一点。您可以使用曲线沿线上的一系列点创建 RTPC。该曲线表示了 Game Parameter （游戏参数）和 Wwise 中音频属性之间的关系。当游戏中的 Game Parameter 发生变化时，Wwise 使用 RTPC 曲线来确定相应的属性值。

## Using RTPCs - example

假设您正在创建一款第一人称射击游戏，您希望根据游戏中角色的疲惫级别来确定主人公呼吸声的音量。当角色不太疲惫时，您希望呼吸声听起来非常柔和；非常疲惫时，呼吸声听起来很沉重。这种情况下，您可以使用 RTPC 将 Game Parameter （疲惫程度）指派给 Wwise 属性（音量）。然后您可以使用坐标图视图，将呼吸声音的音量电平映射到游戏中主人公的疲惫级别。

|  |
| --- |
|  |

RTPC 还可用于获取游戏中的其它效果，例如将水深映射到低通滤波值，将爆炸力映射到低频效果值（LFE）等等。

|  |  |
| --- | --- |
| [注意] | 注意 |
| 虽然可为工程中的所有对象、总线、衰减和效果创建 RTPC，但选择性地使用它们非常重要，因为它们会消耗大量的内存和 CPU 资源。 |

**相关主题**

- [Wwise Fundamentals Module 5: Using Game Parameters](https://www.audiokinetic.com/en/courses/wwise101/?source=wwise101&id=using_game_parameters)

---