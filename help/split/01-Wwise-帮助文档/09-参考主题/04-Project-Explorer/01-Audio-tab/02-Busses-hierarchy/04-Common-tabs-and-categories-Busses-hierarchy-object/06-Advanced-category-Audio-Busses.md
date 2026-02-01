# Advanced category: Audio Busses

[Wwise 帮助文档](../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../00-参考主题.md) > [Project Explorer](../../../00-Project-Explorer.md) > [Audio tab](../../00-Audio-tab.md) > [Busses hierarchy](../00-Busses-hierarchy.md) > [Common tabs and categories: Busses hierarchy objects](00-Common-tabs-and-categories-Busses-hierarchy-object.md) > Advanced category: Audio Busses

##### Advanced category: Audio Busses

The properties in the Advanced category for all Busses hierarchy objects, except [Auxiliary Busses](../03-Property-Editor-Auxiliary-Busses.md "Property Editor: Auxiliary Busses"), allow you to specify the overall number of sound, music, and/or motion instances that can be passed through a bus simultaneously.

| Advanced | |
| --- | --- |
| 界面元素 | 描述 |
| **Playback Limit** | |
| Ignore Parent Playback Limit | 忽略父项。决定当前对象及子对象是受父级 Playback Limit 的制约（勾选），还是在当前级别进行定义（不勾选）。对于顶层对象，此选项将不可用。  Default value: false |
| Limit Sound Instances | 发声数限制。同一层级结构中可同时播放的声音或振动的数量。  Default value: false |
| Sound Instance Limit | Default value: 50  Range: 1 to 1000 |
| When limit is reached: | 当达到上限时。决定在达到播放数上限时将会发生什么。您可以选择以下选项之一：  - **Kill voice for lowest priority：** 停止播放具有最低优先级的实例。在某个对象被终止后，会执行几毫秒的小淡出。 - **Use virtual voice settings for lowest priority：** 为优先级最低的声部应用其Virtual voice behavior。Refer to the **Virtual 声部 behavior** row in this table.  请记住，各个实体都可不沿用其自己的行为，因此声音的虚声部行为可能仍是丢弃声音或继续播放。  Default value: Kill voice |
| When priority is equal: | 当达到上限且优先级相等时。决定在达到播放数上限并且不只一个对象具有最低优先级时将会发生什么。您可以选择以下选项之一：  - **Discard oldest instance** —— 丢弃最早播放的优先级最低的实例。 - **Discard newest instance** —— 丢弃最新播放的优先级最低的实例。  Default value: Discard oldest |

**相关主题**

- [“限制对象播放实例”一节](../../../../../05-使用声音和振动来提升游戏体验/03-管理优先级/02-限制对象播放实例.md "限制对象播放实例")

---