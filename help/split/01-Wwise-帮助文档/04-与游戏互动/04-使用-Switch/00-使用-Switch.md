# 使用 Switch

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [与游戏互动](../00-与游戏互动.md) > 使用 Switch

## 使用 Switch

在使用层级结构组织对象之外，Wwise 中的 Switch（切换开关）也能帮您简化声音、音乐和振动对象的组织。Switch 代表游戏中特定元素的不同条件，可以用来管理这些条件下的相应对象。这些元素的条件种类非常丰富，可以是天气状况，游戏主角使用的武器等。您可以将特定条件下的对象指派到特定 Switch，这样播放该游戏元素时，将播放当前 Switch 对应的对象。

Switch 可以在运行时简化各种条件的管理，对于众多游戏场景或元素都适用，下面列出少数几个：

- 房间、地面、室内/室外的游戏设置 —— 可以为不同的地面材质（例如木板、草地、碎石等）创建 Switch。
- 游戏角色 —— 可以在男性或女性角色讲话时，为对白创建 Switch。
- 天气状态 —— 可以为暴风雨、暴风雪、小雨或晴天创建 Switch。
- 魔界或仙界的游戏氛围 —— 可以为不同世界的特有声音创建 Switch。
- 武器 —— 可以为游戏中火器的不同发射方式、激光和剑创建 Switch。

上述各例中，您都可以先创建 Switch，然后指派相应的对象。指派到 Switch 的对象需要用 Switch Container（切换开关容器）进行编组。When an Event or a Game Parameter value signals a change, the Switch Container verifies the Switch and the correct object is played.

## Using Switches - example

假设您正在研发一款第一人称射击游戏，其中角色可以在各种环境中走动。每种物理环境中都有不同的地面材质，例如混凝土、草地和泥地，每种表面都需要不同的脚步声。这种情况下，您可以为各地面材质创建 Switch，然后将不同脚步声指派到相应的 Switch。当角色行走在混凝土地面上，“Concrete” Switch 将激活，并播放相应声音。从混凝土走到到草地上时，“Grass” Switch 将激活，并播放相应声音。

下图演示了激活的 Switch 如何影响播脚步声的播放。

![](../../../images/000040_02e_online.png)

**相关主题**

- [Wwise Fundamentals Module 4: Using Switches](https://www.audiokinetic.com/en/courses/wwise101/?source=wwise101&id=using_switches)

---