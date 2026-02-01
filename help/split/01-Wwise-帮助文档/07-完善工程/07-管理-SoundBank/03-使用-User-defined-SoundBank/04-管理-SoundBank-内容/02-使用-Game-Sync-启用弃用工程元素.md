# 使用 Game Sync 启用/弃用工程元素

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [完善工程](../../../00-完善工程.md) > [管理 SoundBank](../../00-管理-SoundBank.md) > [使用 User-defined SoundBank](../00-使用-User-defined-SoundBank.md) > [管理 SoundBank 内容](00-管理-SoundBank-内容.md) > 使用 Game Sync 启用/弃用工程元素

#### 使用 Game Sync 启用/弃用工程元素

在 SoundBank 中启用或弃用声音的另一种快速、便捷的方法是使用 Game Sync。在将 Event 或声音结构添加到 SoundBank 时，SoundBank Editor 的 Game Sync 选项卡上会自动创建相关 Game Sync 的列表。您可以通过弃用特定 Grame Sync 将特定元素从 SoundBank 中弃用。在将 Game Sync 从 SoundBank 弃用时，引用该 Game Sync 的所有对象结构和媒体文件也会被弃用。

通过根据游戏同步器来启用／弃用声音，可以更好地控制在游戏特定时刻加载的声音。这意味着您可以更好地管理游戏平台的内存限制。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 游戏参数不可用于从 SoundBank 中弃用工程元素，因此不会在 SoundBank Editor 的 Game Sync 选项卡上列出。 |

##### 示例 – 使用 Game Sync 启用/弃用工程元素

假设您的一个小游戏由三个不同的区域构成。要完成游戏通关，主人公必须穿过区域 1、2 和 3。在 Wwise 中，您使用切换容器处理主人公的脚步声。您为主人公可能行走的不同地面材质创建了以下四个切换开关：

- Carpet
- Tile
- Wood
- Water

在游戏中，“Water”切换开关只用于区域 2 和 3，而其它三个切换开关用于所有三个区域。您决定定义三个 SoundBank；每个 SoundBank 对应于一个区域。由于各个 SoundBank 中必须包含 Switch Container，因此您需要从区域 1 的 SoundBank 中移除“与水相关”的Event、声音结构和媒体文件。为此，您可以加载区域 1 的 SoundBank，然后切换到 Game Sync 选项卡，并取消选择"Water"切换开关。

![](../../../../../../images/SB_GS_Exclude1.png)

此操作将从 SoundBank “Zone1”中弃用“水”相关声音结构和媒体文件。如果您切换到 Edit 选项卡，则会发现 SoundBank 中不再包含引用此切换开关的声音结构、Event 和媒体文件。

![](../../../../../../images/SB_GS_Exclude2.png)

通过导入包含 Game Sync 弃用项的定义文件也可自动将 Game Sync 从 SoundBank 弃用。有关使用定义文件的详细信息，请参阅[“通过导入定义文件创建并填充 SoundBank”一节](../02-通过导入定义文件创建并填充-SoundBank.md "通过导入定义文件创建并填充 SoundBank")。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 您可能会发现 Edit 选项卡中的有些工程元素和媒体文件甚至在手动弃用之前就已变为灰色。当 Switch Container 中包含尚未指定到 Switch 的对象，在添加到 SoundBank 时就会发生这种情况。由于游戏中永远不会播放这些对象，因此它们将自动从 SoundBank 中弃用。 |

**使用 Game Sync 将工程元素从 SoundBank 中弃用的方法是：**

1. 将 SoundBank 加载到 SoundBank Editor。
2. 切换到 **Game Syncs** 选项卡。

   此时将显示与 Add 选项卡上的 Event 或对象相关的 Game Sync 的完整列表。
3. 定位您要从 SoundBank 中弃用的 Game Sync，并取消选择相应的复选框。

   此时 Game Sync 及其所有相关对象和媒体文件就从 SoundBank 中弃用掉了。
4. 重复步骤 3，直至从 SoundBank 中弃用掉您想移除的所有 Game Sync。

---