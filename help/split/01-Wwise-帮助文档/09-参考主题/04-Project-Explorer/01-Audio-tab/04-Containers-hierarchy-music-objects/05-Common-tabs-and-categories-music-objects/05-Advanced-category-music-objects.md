# Advanced category: music objects

[Wwise 帮助文档](../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../00-参考主题.md) > [Project Explorer](../../../00-Project-Explorer.md) > [Audio tab](../../00-Audio-tab.md) > [Containers hierarchy: music objects](../00-Containers-hierarchy-music-objects.md) > [Common tabs and categories: music objects](00-Common-tabs-and-categories-music-objects.md) > Advanced category: music objects

##### Advanced category: music objects

The properties in the Advanced category for music objects, which are located in the Containers Hierarchy, include a series of controls that allow you to define the advanced playback behaviors of your music objects. 您可以定义各个游戏对象可同时播放的实例数，指定各个声音对象的播放优先级，确定当音量低于音量阈值时音乐是继续播放、终止，还是移到虚声部列表。

| Advanced | |
| --- | --- |
| 界面元素 | 描述 |
| **Playback Limit** | |
| Ignore Parent Playback Limit | 忽略父项。决定当前对象及子对象是受父级 Playback Limit 的制约（勾选），还是在当前级别进行定义（不勾选）。对于顶层对象，此选项将不可用。  Default value: false |
| Limit Sound Instances | 发声数限制。同一层级结构中可同时播放的声音或振动的数量。  Default value: false |
| Sound Instance Limit | Default value: 50  Range: 1 to 1000 |
| Limitation sound instances to: | 发声数限制。同一层级结构中可同时播放的声音或振动的数量。此限制数将应用到所选范围：  - **Per game object：** 每个游戏对象。分别为此层级中的每个游戏对象应用发声限制。 - **Globally：** 全局。为此层级中所有游戏对象的发声总数应用限制。  Default value: Game object |
| When limit is reached: | 当达到上限时。决定在达到播放数上限时将会发生什么。您可以选择以下选项之一：  - **Kill voice for lowest priority：** 停止播放具有最低优先级的实例。在某个对象被终止后，会执行几毫秒的小淡出。 - **Use virtual voice settings for lowest priority：** 为优先级最低的声部应用其Virtual voice behavior。Refer to the **Virtual 声部 behavior** row in this table.  请记住，各个实体都可不沿用其自己的行为，因此声音的虚声部行为可能仍是丢弃声音或继续播放。  Default value: Kill voice |
| When priority is equal: | 当达到上限且优先级相等时。决定在达到播放数上限并且不只一个对象具有最低优先级时将会发生什么。您可以选择以下选项之一：  - **Discard oldest instance** —— 丢弃最早播放的优先级最低的实例。 - **Discard newest instance** —— 丢弃最新播放的优先级最低的实例。  Default value: Discard oldest |
| **Virtual Voice** | |
| Override parent | 不沿用父对象。决定是继承父对象的虚声部设置，还是在层级结构的当前层级中进行定义。当没有勾选该选项时，虚声部控件将不可用。  对于顶层对象，此选项将不可用。  Default value: false |
| Virtual voice behavior | 当对象音量低于音量阈值或播放数量超出限制时，对象的行为。您可以选择以下选项之一：  - **Continue to play**，即使无法听到或感受到对象，但仍继续播放对象。 - **Kill voice**，停止播放对象。此选项不会施加任何淡出处理。 - **Send to virtual voice**，将对象发送到虚声部列表。当某个对象被发送到虚声部列表时，该对象的某些参数将由声音引擎监视，但不会对音频或振动进行任何处理。 - **Kill if finite else virtual**，如果对象不是无限循环，则停止播放；如果对象无限循环，则将发送到虚声部列表。  对于音乐对象，若选择 **Send to virtual voice** 或 **Kill if finite else virtual**，则在恢复为实声部时继续播放对象，如同从未停止播放一样。  Default value: Continue to play |
| **Playback Priority** | |
| Override parent | 对于顶层对象，此选项将不可用。  不沿用父对象。决定播放优先级是从父对象继承还是在层级结构当前层级进行定义。当没有勾选该选项时，Playback Priority 控件将不可用。  Default value: false |
| Priority | 优先级。优先级为 1 的对象具有最低的优先级，而优先级为 100 的对象具有最高的优先级。  此值决定在达到播放数上限时会播放哪些对象。  该属性用于定义同一结构下各个对象的相对重要性。  Default value: 50  Range: 0 to 100 |
| Use Priority Distance Factor | Default value: false |
| Offset priority by x at max distance | 在最大距离时对优先级做量为 x 的偏置。指定一个值，当对象达到 Attenuation Editor 中指定的最大距离值时，可以用此值来升高或降低该对象的优先级。  在选择此选项时，如果对象落入衰减最大距离值内的任何位置，则会对对象的优先级做一个偏置。应用的偏置量将取决于对象与听者之间的相对位置。  当没有勾选该选项时，距离听者的距离不会影响对象的优先级。  Default value: -10  Range: -100 to 100 |

**相关主题**

- [“限制对象播放实例”一节](../../../../../05-使用声音和振动来提升游戏体验/03-管理优先级/02-限制对象播放实例.md "限制对象播放实例")
- [“定义 Playback Priority”一节](../../../../../05-使用声音和振动来提升游戏体验/03-管理优先级/03-定义-Playback-Priority.md "定义 Playback Priority")
- [“管理音量较低的对象”一节](../../../../../05-使用声音和振动来提升游戏体验/03-管理优先级/04-管理音量较低的对象.md "管理音量较低的对象")

---