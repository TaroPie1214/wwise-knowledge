# Building Containers hierarchy tips and best practices

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [设置工程](../00-设置工程.md) > [Building your sound and motion hierarchies](00-Building-your-sound-and-motion-hierarchies.md) > Building Containers hierarchy tips and best practices

## Building Containers hierarchy tips and best practices

在 Wwise 中创建层级结构的方式非常灵活，在项目伊始就制定统一的策略可以节省后期的时间和精力。当然，处理音频工程的方法多种多样；了解相关概念可让游戏获得最佳效果。

### Grouping objects in the Containers hierarchy

在构建层级结构之前，要构思组织对象的最佳方式。既要节省创作时间，又要更好地管理工程内存占用。关于如何对工程中的不同对象进行有效分组，以下是一些建议，请您根据实际需求选用。

The Property Container is the ultimate memory and CPU saver because some of the Property Container's properties, such as positioning and RTPCs, are shared by all of its child objects. So when you are considering how to organize your objects, think about grouping objects under Property Containers to:

- 共享属性设置，方便统一处理。
- 共享 Overrides （不沿用）属性，避免为多个子对象单独勾选 Override 和指定新值。

|  |  |
| --- | --- |
| [注意] | 注意 |
| Effects applied at the Property Container level is an efficient way to apply the Effect but will not save CPU usage. When you apply an Effect at the Property Container level, an instance of the Effect is applied to all child objects. 实时为各个对象处理效果可能会占用大量 CPU。 |

To optimize memory usage, consider grouping objects into Property Containers to share the following properties:

- 定位
- RTPC（实时参数控制）
- States（状态）
- 随机化器

Let's say you have a Property Container containing 10 sounds and you want to set the sound positioning to 3D. 可以为这些声音逐个勾选 Override Parent（不沿用父选项），并设置为 3D。However, doing it this way uses 10 times more memory at runtime than if you had set the Property Container positioning properties to 3D. Now if you wanted some of the sounds to be panned, you would still be optimizing memory if you set the Property Container's positioning to 3D Emitter. In this case you would override the Property Container and apply panning to the specific sounds because panned sounds do not require additional memory.

While the Property Container is usually your best choice, in certain situations, you can decide to apply properties in containers to optimize memory consumption. If, for example, you are only applying positioning to specific objects within a container, for example footstep sounds in a Random Container, you could save memory by applying the positioning properties to the container and not to the parent Property Container. If, however, you want all the objects in the structure to share the positioning properties, you would apply these at the Property Container level.

### 为对象分组 – 示例

Let's have a look at how you can group objects in a Property Container effectively using some of the concepts we have just discussed. 本例中，您会处理游戏的对话素材，其中一些是角色语音，另一些是对讲机语音。You could group these under a Dialogue Property Container because you know that you want your dialogue to share properties such as volume, for example.

The following image shows that if you apply a volume setting once to the Dialogue
container, all the objects share the volume.

|  |
| --- |
|  |

Now that you have set your volume for the Property Container, you have decided to add a Parametric EQ effect on the radio dialogue only. You could edit each radio voice and override the Property Container settings for each and apply this effect. But you could also work more efficiently by grouping all the radio voice files together in a container and then override the Property Container settings and add the Effect on the container.

The following image displays using Override parent to add effects to a Dialogue
container.

![](../../../../images/override_effect_parent_online.png)

### 实时混音和对象属性

当您连接到游戏或游戏模拟器时，可以在 Wwise 中实时修改以下相对属性的值：

- Volume
- Pitch（音高）
- Low-Pass Filter（低通滤波器）
- Center %
- RTPC 值
- State 和 Switch 变换
- Triggers
- Attenuation 控件
- 部分音频和源效果器插件属性

|  |  |
| --- | --- |
| [备注] | 备注 |
| 一般情况下，任何可映射至 Game Parameter 的属性都可在游戏中实时修改。 |

为了能够做到这一点，您需要加载您想在 Transport Control 或 Soundcaster 中修改其属性的对象。如果未加载对象，则更改将不会生效，因为声音引擎中未注册该对象。For Property Containers, which cannot be loaded into the Transport Control, you can load a child object of the Property Container and this will register its parent objects in the sound engine. 在注册对象后，对象将在您连接到游戏时保持注册状态。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 记住，如果您将对象固定在 Transport Control 中，则其它对象要到您取消固定第一个对象后才可加载。然而，如果您已将对象加载到 Soundcaster 中，则此对象将在声音引擎中注册。 |

### 相对属性和性能

在不同平台上，Wwise 中的有些相对属性（如音高）可能会对性能造成影响。Wwise 中管理音高的机制是基于采样率的，改变声音的音高会增加 CPU 占用，因为必须对文件进行重新采样。

---