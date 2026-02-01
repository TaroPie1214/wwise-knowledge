# System Audio Device 的作用

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [设置工程](../../00-设置工程.md) > [建立输出总线的结构](../00-建立输出总线的结构.md) > [了解基于对象的音频](00-了解基于对象的音频.md) > System Audio Device 的作用

### System Audio Device 的作用

System Audio Device（系统音频设备）是唯一一种支持 Audio Object（音频对象）的内置 Wwise Audio Device。System Audio Device 会根据终端的性能和 System Audio Device 设置决定要将哪些输出发送到终端。

System Audio Device 将按照以下规则选择是将 Audio Object 输出到 Main Mix、Passthrough Mix 还是 System Audio Object：

- 只有满足以下所有要求才会将 Audio Object 作为 System Audio Object 输出到终端：

  - 其设有 **3D Spatialization**。
  - 其 **Speaker Panning / 3D Spatialization Mix**（扬声器声像摆位/3D 空间化混音）被设为了 100%。
  - 其具有不带任何高度声道的标准声道配置。
  - 有足够的 System Audio Object 可供容纳其所有声道。换句话说，在实施性能分析时，Audio Device Editor（音频设备编辑器）中显示的 **System Audio Objects Used**（所用系统音频对象数）不得超过 **Available System Audio Objects**。

    ![](../../../../../images/system_audio_device_audio_objects.png)

    |  |  |
    | --- | --- |
    | [备注] | 备注 |
    | 最好不要超出 Available System Audio Objects 的最大限值。对于输出到 Main Mix 的其余 Audio Object，可能会进行不同的处理，最终产生明显的变化。System Audio Object 采用先进先出的优先次序进行分配。 |
- 只有满足以下所有要求才会将不符合上述要求的 Audio Object 输出到 Passthrough Mix：

  - 其采用单声道或立体声声道配置。
  - 其没有 3D 位置。
- 不符合上述全部要求的 Audio Object 将被输出到 Main Mix。对于输出到 Main Mix 的音频，会渲染为 System Audio Device 的 Main Mix 的输出配置。此配置可使用 Audio Device Editor 中的 **Main Mix for Binauralization** 或 **Main Mix for Home Theater** 设置来定义；若两者均被设为 **Use Game-Defined Settings**，则由终端对 Main Mix 配置进行初始化。在这种情况下，Main Mix 配置可满足不同听觉环境的需要。

|  |  |
| --- | --- |
| [备注] | 备注 |
| Audio Object 的插件元数据中定义的 **Mix Behavior**（混音行为）可改写上述默认行为。有关详细信息，请参阅 [“Metadata”一节](03-Metadata.md "Metadata") 章节。 |

|  |  |
| --- | --- |
| [备注] | 备注 |
| 在 System Audio Device 收到具有 3D 位置和多个声道的 Audio Object 时，会先将其拆分为多个单声道 System Audio Object（每个声道对应一个），然后再发送到终端。比如，对于采用立体声配置的 Audio Object，将拆分为两个 System Audio Object。注意，LFE 声道将被弃用。比如，对于采用 5.1 声道配置的 Audio Object，将拆分为五个 System Audio Object（弃用 LFE 声道）。 |

有关更多详细信息，请参阅 [“了解声部管线”一节](../../../07-完善工程/01-管理输出/05-了解声部管线.md "了解声部管线") 章节。

---