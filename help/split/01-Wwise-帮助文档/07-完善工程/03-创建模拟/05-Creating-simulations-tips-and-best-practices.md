# Creating simulations tips and best practices

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [完善工程](../00-完善工程.md) > [创建模拟](00-创建模拟.md) > Creating simulations tips and best practices

## Creating simulations tips and best practices

在 Wwise 中创建模拟非常灵活，您可以使用它们高效地执行性能分析、创建概念验证以及在 Wwise 或游戏中测试当前的作品。以下是帮助您取得游戏最佳效果而需要考虑的一些概念。

### 实时混音和对象属性

当您连接到游戏或游戏模拟器时，可以在 Wwise 中实时修改以下相对属性的值：

- Volume（音量）
- Pitch（音高）
- Low-Pass Filter（低通滤波器）

为了能够做到这一点，您需要加载您想在 **Transport Control** 或 **Soundcaster** 中修改其属性的对象。如果未加载对象，则更改将不会生效，因为声音引擎中未注册该对象。For the Transport Control, certain objects such as Property Containers cannot be loaded, but you can load a child object of the Property Container and this will register its parent objects in the sound engine. Since you can load a Property Container in the Soundcaster, this is not a problem. 在注册对象后，对象将在您连接到游戏时保持注册状态。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 记住，如果您将对象固定在 Transport Control 中，则其它对象要到您取消固定第一个对象后才可加载。然而，如果您已将对象加载到 Soundcaster 中，则此对象将在声音引擎中注册。 |

对于某些属性，包括 Randomizer、Effect、Attenuation 和 Source 插件属性，只有在游戏下次播放该对象时，您所做的更改才会生效。

---