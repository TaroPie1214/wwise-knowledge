# 通过导入定义文件创建并填充 SoundBank

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理 SoundBank](../00-管理-SoundBank.md) > [使用 User-defined SoundBank](00-使用-User-defined-SoundBank.md) > 通过导入定义文件创建并填充 SoundBank

### 通过导入定义文件创建并填充 SoundBank

其中一种创建并填充 SoundBank（音频包）的方法是导入制表符分隔的文本文件。该文件会按 SoundBank 分类列出游戏中的所有 Event（事件）。通常，这种文件由用于将 Event 集成到游戏中的 3D 应用程序或关卡编辑器生成。在导入定义文件之前，必须在 Wwise 中创建 Event。若 Event 缺失，Import Definition Log 中会对应显示 Event Missing。

定义文件必须包括 SoundBank 的名称和相应的 Event 名称，它们之间通过制表符隔开。下面举例展示了有效的定义文件。其中，→ 表示制表符。

```
          SB1→"Event_01"
          SB2→"Event_02"
          SB2→"Event_03"
          SB3→"Event_04"
```

#### 使用关键字在 SoundBank 中启用/弃用元素

定义文件还可包括特殊关键字，用于定义将在 SoundBank 中启用或弃用的工程元素类型。有以下关键字可供使用：

- **Event**：指定 SoundBank 将包含 Event 信息。
- **Structure**：指定 SoundBank 中将包含声音、音乐或振动结构信息。
- **Media**：指定 SoundBank 中将包含媒体文件。
- **-GameSyncExclusion**：指定特定 Game Sync 将从 SoundBank 中弃用。弃用 Game Sync 时，所有相关声音结构和媒体文件也会被弃用。关键字 -GameSyncExclusion 必须结合以下其中一个关键字使用：

  - **State**：指定特定状态及其所有相关对象和媒体文件都将从 SoundBank 中弃用。此关键字后面必须写上 State Group 名称和 State 名称，名称之间通过制表符隔开。
  - **Switch**：指定特定切换开关及其所有相关对象和媒体文件都将从 SoundBank 中弃用。此关键字后面必须写上切换开关组名称和切换开关名称，名称之间通过制表符隔开。
  - **Trigger**：指定特定触发器及其所有相关对象和媒体文件都将从 SoundBank 中弃用。该关键字后面必须写上 Trigger 名称。
- **-DialogueEvent**：将在 SoundBank 中启用指定特定对白事件。此关键字后面必须写上对白事件的名称、GUID 或short ID（短 ID）。它后面还可以写上 **Event**、**Structure** 或 **Media** 关键字作为包含选项。
- **-EffectShareset**：将在 SoundBank 中启用指定特定效果器 ShareSet。此关键字之后必须附加 Effect ShareSet 的名称、GUID 或 Short ID。它后面还可以写上 **Structure** 或 **Media** 关键字作为包含选项。
- **-AuxBus**：指定将特定辅助总线加入 SoundBank。此关键字后面必须写上总线的名称、GUID 或short ID。它后面还可以写上 **Structure** 或 **Media** 关键字作为包含选项。

```
            My_SoundBank_Normal→"Event_01"
            My_SoundBank_EventandStructure→"Event_02"→Event→Structure
            My_SoundBank_Media→"Event_03"→Media
```

在上图中，被称为"My\_SoundBank\_Normal"的第一个 SoundBank 将包含与 Event\_01 相关的所有 Event 数据、结构数据和媒体文件。被称为"My\_SoundBank\_EventandStructure"的第二个 SoundBank 将只包含与 Event\_02 相关的 Event 和结构数据。被称为"My\_SoundBank\_Media"的第三个同时也是最后一个 SoundBank 将只包含与 Event\_03 相关的媒体文件。

在使用 -GameSyncExclusion 关键字时，必须另起一行为弃用的各个关键字创建单独的条目。弃用 Game Sync 还会弃用所有对应的对象结构和媒体文件。下图展示了 -GameSyncExclusion 关键字在定义文件中的正确用法。其中，→ 表示制表符。

```
            SB1→-GameSyncExclusion→State→StateGroupName→StateName
            SB1→-GameSyncExclusion→Switch→SwitchGroupName→StateName
            SB1→-GameSyncExclusion→Trigger→Trigger
```

|  |  |
| --- | --- |
| [备注] | 备注 |
| Game Sync（State Group、State、Switch Group、Switch 和 Trigger）的名称不需要使用引号（"）。 |

```
            SB1→-EffectShareset→"effect1"→Media
            SB1→-EffectShareset→"effect2"→Structure
            SB1→-EffectShareset→"effect3"→Media→Structure
```

#### 使用 ID 而非字符串来识别 Event 和效果器

如果游戏未对 Event 名称使用字符串，则可以在定义文件中使用以下任一进制系统定义 Event：

- 十六进制
- 小数值

|  |  |
| --- | --- |
| [备注] | 备注 |
| 十六进制和十进制系统可用于标识定义文件中的 Event，但不可用于标识 Game Sync 弃用项中的 State、 Switch 和 Trigger。 |

下图展示如何在定义文件中使用三种不同的进制系统定义 Event。其中，→ 表示制表符。

```
            SB1→"Event_01"
            SB1→26507443
            SB1→0x19478B3
```

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| SoundBank 定义文件还可用于跟踪已经集成到游戏中的、缺失的以及仍需在 Wwise 中创建的 Event。某个程序员可以从游戏中生成 Event 列表，然后您可以将定义文件导入 Wwise。您可以使用日志文件中的信息将游戏中的 Event 与在 Wwise 中创建的 Event 匹配起来。 |

**通过导入定义文件创建 SoundBank 的方法是：**

1. 在 Project Explorer 中，切换到 SoundBank 选项卡。
2. 右键点击您要在其中创建 SoundBank 的工作单元。
3. 从快捷菜单中选择 **Import SoundBank Definition**。

   这时会打开 Open（打开）对话框。
4. 前往保存定义文件的位置。
5. 点击 **Open**。

   这时会打开 Import Definition Log（导入定义日志）对话框。
6. 仔细查看日志中的导入活动。导入活动可以为以下任意一项：

   - **Inclusion Added** —— 新的事件或效果已添加到现有 SoundBank。
   - **SoundBank Created** —— 创建了新的 SoundBank。
   - **Inclusion Removed** —— 某Event 或效果器已从现有 SoundBank 中移除。
   - **Event Missing** —— 工程中不再存在某 Event 或者某 Event 尚未创建。
   - **Effect Missing** —— 工程中不再存在某效果器或者某效果器尚未创建。
   - **Exclusion Added** —— 某 Game Sync 已从现有 SoundBank 中弃用。
   - **Exclusion Deleted** —— 某 Game Sync 已在现有 SoundBank 中被重新启用。
   - **Exclusion Missing** —— 工程中不再存在某 Game Sync 或者 Game Sync 尚未创建，因此不能添加弃用项或者从弃用列表中删除。
   - **No Change Detected** —— 导入的 SoundBank 与 Wwise 中已存在的 SoundBank 相同。
7. 点击 **Close**。

   Wwise 于是会创建 definition file（定义文件）中定义的 SoundBank，并将指定的 Event、对象结构和媒体添加到 SoundBank 中去。

---