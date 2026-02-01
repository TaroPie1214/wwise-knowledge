# Using containers and Property Containers in the Containers hierarchy

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [设置工程](../../00-设置工程.md) > [Building your sound and motion hierarchies](../00-Building-your-sound-and-motion-hierarchies.md) > [Grouping objects to create your Containers hierarchy](00-Grouping-objects-to-create-your-Containers-hierarc.md) > 
Using containers and Property Containers in the Containers hierarchy

### Using containers and Property Containers in the Containers hierarchy

Containers and Property Containers can both be used to group the assets within your project hierarchy, but they are applied at different levels and serve different purposes.

Containers are at the second level in the Containers hierarchy, which means they can be both parent and child objects. You can use containers to group sounds as well as other containers. 通过在容器内 "嵌套" 其他容器 ，可以得到多样化的结果，模拟真实声音表现。

Property Containers also group objects within the project hierarchy, but they sit one level above containers. This means that a Property Container can be the parent of a container, but not vice versa. Property Containers can be the parent of any number of sounds, containers, and other Property Containers. 可以使用 Actor-mixer 将大量的 Wwise 对象分组到一起，从而统一设置整个组的属性。

The following illustration demonstrates how you can use containers and Property Containers to group the sound assets related to one of the characters in your project.

|  |
| --- |
|  |

|  |  |
| --- | --- |
| [备注] | 备注 |
| A similar hierarchy of containers and Property Containers can be created at the same level to group the motion assets in your project. |

#### 组织素材 —— 示例

假设您正在研发一款第一人称射击游戏，里面使用了七种不同武器，您希望每种武器的声音具有类似的属性。You can group all the sounds related to a weapon into a Sequence or Random Container. Then you can group all the weapon containers in one Switch Container so that you can control properties such as volume and pitch for all the weapons as one unit.

|  |
| --- |
|  |

You can build your asset structures in the early phases of your project based on the game design. 同时也需要考虑工程中的其它元素，例如 Work Unit（工作单元）、Routing（信号通路）以及 Game Syncs（游戏同步器）等。从工程整体来考虑问题有助于有效地为对象分组。For some ideas about how to group objects, refer to [“Grouping objects in the Containers hierarchy”一节](../06-Building-Containers-hierarchy-tips-and-best-practi.md#grouping_objects_in_actor_mixer_hierarchy "Grouping objects in the Containers hierarchy") in the Building Containers hierarchy Tips and Best Practices section.

关于如何建立通路结构、Work Unit 以及新建 Game Sync，请参阅以下几节：

- [*Working with a team*](../../04-Working-with-a-team/00-Working-with-a-team.md "Working with a team")
- [*建立输出总线的结构*](../../07-建立输出总线的结构/00-建立输出总线的结构.md "建立输出总线的结构")
- [*使用 State*](../../../04-与游戏互动/03-使用-State/00-使用-State.md "使用 State")
- [*使用 Switch*](../../../04-与游戏互动/04-使用-Switch/00-使用-Switch.md "使用 Switch")
- [*使用 RTPC*](../../../04-与游戏互动/05-使用-RTPC/00-使用-RTPC.md "使用 RTPC")
- [*使用 Trigger*](../../../04-与游戏互动/06-使用-Trigger.md "使用 Trigger")
- [*将 State 和 State Group 用于动态对话*](../../../04-与游戏互动/07-将-State-和-State-Group-用于动态对话.md "将 State 和 State Group 用于动态对话")

---