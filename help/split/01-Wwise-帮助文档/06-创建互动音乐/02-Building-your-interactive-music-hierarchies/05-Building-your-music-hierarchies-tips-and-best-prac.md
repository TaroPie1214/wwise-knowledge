# Building your music hierarchies tips and best practices

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [创建互动音乐](../00-创建互动音乐.md) > [Building your interactive music hierarchies](00-Building-your-interactive-music-hierarchies.md) > Building your music hierarchies tips and best practices

## Building your music hierarchies tips and best practices

互动音乐是具有多种功能的复杂工具，Adopting a coherent strategy for building your music hierarchies at the beginning of a project can save you time and effort later on. 当然，处理互动音乐工程的方法很多，您可以在 Wwise 中使用任何方法来为游戏创造最佳的结果。以下是一些建议，告诉您如何为对象分组能够充分发挥互动音乐的优势。

### Grouping music objects

Before you start building your music hierarchies you need to think about the best way to organize your objects to save authoring time, but also to manage your project's memory consumption.

To optimize memory usage, consider applying properties at a higher level in the hierarchy so that they can be shared by the entire group. 以下属性可以共享：

- Positioning（定位）
- RTPC（实时参数控制）
- State（状态）
- 随机化器

### 使用多级 Music Switch Container

最好尽量简化级联 Music Switch Container（音乐切换容器）的层级结构。在可能的情况下确保子级 Music Switch Container 相对独立，让父级 Music Switch Container 负责不同子级之间而非单个子级内部的过渡。

Music Switch Container 可绑定多个 State Group（状态组）或 Switch Group（切换开关组），因此只需一个上层 Music Switch Container 便可提供子对象之间过渡所需的全部逻辑。倘若某个 Music Switch Container 中包含多个子级 Music Switch Container，最好将各个 State Group 和 Switch Group 单独指派给对应的 Music Switch Container，而不要集中控制不同层级结构各个 State 和 Switch 的变化。

注意，在使用多级 Switch Container 时无法为所有过渡统一设定优先顺序，因为过渡是在各个不同子对象中单独设置的，它们各自内部都有普适过渡规则，而且父子音乐切换过渡规则之间并不存在优先关系。这样的话，如果过渡规则之间发生冲突，会很难追踪活跃的音乐过渡。有关过渡的详细信息，请参阅 [*使用 Transition*](../07-使用-Transition/00-使用-Transition.md "使用 Transition")。

---