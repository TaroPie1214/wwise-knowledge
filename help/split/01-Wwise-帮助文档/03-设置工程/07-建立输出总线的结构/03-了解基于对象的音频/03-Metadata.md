# Metadata

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [设置工程](../../00-设置工程.md) > [建立输出总线的结构](../00-建立输出总线的结构.md) > [了解基于对象的音频](00-了解基于对象的音频.md) > Metadata

### Metadata

元数据是一组与 Audio Object（音频对象）关联的属性，专门供终端或对象处理器使用。元数据允许终端或对象处理器执行各种涉及 Audio Object 的计算，以此生成相应的空间化效果。

A Metadata tab is available in the Primary Editor of all objects and busses in Wwise.

元数据插件仅适用于某些终端或对象处理器。不同的元数据插件所含的各种属性不尽相同。这些属性包括 3D Position（3D 位置）、Azimuth（方位角）、Elevation（高度角）、Focus（聚焦）、Spread（散布）等等。在将元数据插件添加到 Metadata 选项卡时，会将一组属性与 Wwise 对象或总线关联。对于总线，会将元数据填写到所有输出到总线和子总线的对象。

|  |  |
| --- | --- |
| [注意] | 注意 |
| 若将 Audio Object 输出到处于 Mixing（正在混音）状态的总线，则所有与 Audio Object 关联的元数据都会被销毁。有关详细信息，请参阅 [“了解总线图标和处理状态”一节](../../../07-完善工程/01-管理输出/11-完成终混/01-了解总线图标和处理状态.md "了解总线图标和处理状态") 章节。 |

在默认情况下，Wwise 中提供 Wwise System Output Settings 元数据插件。对于其他元数据插件，可通过 Audiokinetic Launcher 加以安装。

#### Mix Behavior

Audio Object 的 Metadata 选项卡中所选 Mix Behavior（混音行为）会改写 System Audio Device（系统音频设备）原本要执行的默认混音行为。

可能的 Mix Behavior 包括：

- **Use Default**（使用默认设置）：允许 System Audio Device 选择最适合此 Audio Object 的目标。有关详细信息，请参阅 [“System Audio Device 的作用”一节](02-System-Audio-Device-的作用.md "System Audio Device 的作用") 章节。
- **Mix to Main**（混音到主混音）：强制将 Audio Object 输出到 Audio Device 的 Main Mix。
- **Mix to Passthrough**（混音到直通混音）：强制将 Audio Object 输出到 Audio Device 的 Passthrough Mix。若 Audio Device 不支持 Passthrough Mix，则将 Audio Object 输出到 Main Mix。

---