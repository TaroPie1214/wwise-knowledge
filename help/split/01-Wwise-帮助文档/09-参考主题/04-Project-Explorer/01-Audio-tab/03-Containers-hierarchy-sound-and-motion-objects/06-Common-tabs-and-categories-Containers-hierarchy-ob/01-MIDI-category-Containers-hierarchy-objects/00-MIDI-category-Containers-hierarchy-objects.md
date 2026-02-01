# MIDI category: Containers hierarchy objects

[Wwise 帮助文档](../../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../../00-参考主题.md) > [Project Explorer](../../../../00-Project-Explorer.md) > [Audio tab](../../../00-Audio-tab.md) > [Containers hierarchy: sound and motion objects](../../00-Containers-hierarchy-sound-and-motion-objects.md) > [Common tabs and categories: Containers hierarchy objects](../00-Common-tabs-and-categories-Containers-hierarchy-ob.md) > MIDI category: Containers hierarchy objects

##### MIDI category: Containers hierarchy objects

For objects located in the Containers hierarchy, there are a series of
controls that allow you to define the object's behavior as a MIDI synthesizer:

- Filters（筛选器）控件用于指定对象所要处理的 MIDI Event。
- MIDI Events（MIDI 事件）控件用于指定要针对收到的 MIDI 事件执行哪些动作。

| M ID I | |
| --- | --- |
| 界面元素 | 描述 |
| **MIDI Events** | |
| Override parent | 决定 MIDI Event 属性是从父级继承还是在当前层级定义。当没有勾选该选项时，MIDI 事件控制是不可用的。  对于顶层对象，此选项将不可用。  Default value: false |
| Play On | 确定哪些类型的 MIDI Note 事件会导致对象播放。  - Note-On - Note-Off  Default value: Note-On |
| MIDI break on note-off | 在音符关时中断。如果 **Play On** 设置为 Note-On，则该属性决定了是否在接收到音符关事件时让正在播放的对象停止循环播放。如果是这样，则被循环的声音或连续容器的播放将被停止，同时允许当前对象完成播放。  Default value: false |
| **Note Tracking** | |
| Override parent | 不沿用父项。决定是继承父对象的音符跟踪控制，还是在层级结构的当前层级中定义对音符跟踪的控制。当没有勾选该选项时，音符跟踪控制是不可用的。  对于顶层对象，此选项将不可用。  Default value: false |
| Enable MIDI note tracking | 启用。如果勾选该选项，则该节点在播放时会做移调。变调的量由接收到的 MIDI 事件音符和 Root Note 值确定。  Default value: false |
| MIDI tracking root note | 根音。该节点声音的根音。这个值与接收到的 MIDI 音符联合决定了该节点声音的移调量。  |  |  | | --- | --- | | [备注] | 备注 | | 如果音符跟踪未启用，则会忽略此值。 |  Default value: 60  Range: 0 to 127 |
| **Transformation** | |
| Transposition | 移调。作用于 MIDI 事件音符的偏置。移调是在 Key Range（音调范围）筛选器之前应用的。  Default value: 0  Range: -127 to 127 |
| Velocity Offset | 力度偏置。作用于 MIDI 事件的音符力度上的偏移量。仅适用于 MIDI 音符事件该偏置会在 Velocity（力度）筛选器之前应用。  Default value: 0  Range: -127 to 127 |
| **Filters** | |
| Key Range Min | 音调范围。对接收到的 MIDI 音符事件的音符进行筛选。如果收到的 MIDI 音符事件的力度不在最小值 - 最大值范围内，则会忽略它。  默认最小值：C-1，默认最大值：G9  |  |  | | --- | --- | | [备注] | 备注 | | 用数值表示的 MIDI 音符与各个八度之间的对应关系在用户偏好设置中指定；有关详细信息，请参阅 [用户首选项](../../../../../../02-入门/04-个性化您的工作空间/04-设置用户偏好.md "设置用户偏好") 。 |  Default value: 0  Range: 0 to 127 |
| Key Range Max | 音调范围。对接收到的 MIDI 音符事件的音符进行筛选。如果收到的 MIDI 音符事件的力度不在最小值 - 最大值范围内，则会忽略它。  默认最小值：C-1，默认最大值：G9  |  |  | | --- | --- | | [备注] | 备注 | | 用数值表示的 MIDI 音符与各个八度之间的对应关系在用户偏好设置中指定；有关详细信息，请参阅 [用户首选项](../../../../../../02-入门/04-个性化您的工作空间/04-设置用户偏好.md "设置用户偏好") 。 |  Default value: 127  Range: 0 to 127 |
| Velocity Min | 力度。对接收到的 MIDI 音符事件的力度进行过滤。如果收到的 MIDI 音符事件的力度不在最小值 - 最大值范围内，则会忽略它。  Default value: 0  Range: 0 to 127 |
| Velocity Max | 力度。对接收到的 MIDI 音符事件的力度进行过滤。如果收到的 MIDI 音符事件的力度不在最小值 - 最大值范围内，则会忽略它。  Default value: 127  Range: 0 to 127 |
| Channel Filter | 通道。对接收到的 MIDI 音符事件的通道进行过滤。如果收到的 MIDI 音符事件 Channel 与筛选条件不符，则会忽略它。  Default value: 65535  Range: 0 to 65535 |

---