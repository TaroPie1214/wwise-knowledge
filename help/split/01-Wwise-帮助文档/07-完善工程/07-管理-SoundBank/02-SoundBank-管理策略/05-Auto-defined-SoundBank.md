# Auto-defined SoundBank

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理 SoundBank](../00-管理-SoundBank.md) > [SoundBank 管理策略](00-SoundBank-管理策略.md) > Auto-defined SoundBank

### Auto-defined SoundBank

此方法适用于以下情形：

- 声音设计师很难事先预测媒体需求。
- 需要将媒体设为很高的粒度级别以保持较低的内存用量。
- 最好以 SoundBank 为单位逐个打包 Event（事件）。

为此，可将 Wwise 配置为针对 Event 和 Auxiliary Bus（辅助总线）自动定义 SoundBank。

**启用 Auto-Defined SoundBank：**

1. 在 Wwise 菜单栏中，依次单击 **Project** > **Project Settings**（工程 > 工程设置）或按下 Shift+K。
2. 在 Project Settings（工程设置）对话框中，选中 SoundBanks（音频包）选项卡，然后选中 **Enable Auto-Defined SoundBanks**（启用自动定义的音频包）复选框。

在选中后，Wwise 便会针对以下各项自动定义 SoundBank：

- User-defined SoundBank（用户定义的音频包）中没有包含的 Event。
- 所有 Auxiliary Bus。

有关更多详细信息，请参阅 [“SoundBanks 选项卡”一节](../../../09-参考主题/01-工程/08-Project-Settings/03-SoundBanks-选项卡/00-SoundBanks-选项卡.md "SoundBanks 选项卡") 章节。

SoundBank Manager（音频包管理器）的 Auto-Defined SoundBanks（自动定义的音频包）列表中包含可能产生自动定义的 SoundBank 的所有 Wwise 对象。对于每个对象，列表都提供有以下各列来确定是否定义了 SoundBank：

- **Automatic**（自动）：是否定义了 SoundBank（Yes 或 No）。
- **Inc**（启用）：对象的 Inclusion 属性。
- **In User SoundBanks**（在用户音频包中）：一系列包含对象的 User-defined SoundBank。

下图显示了配置为自动定义 SoundBank 的工程的 SoundBank Manager。

![](../../../../../images/soundbank_manager_auto_defined.png)

在示例工程中，以下 Event 没有 SoundBank：

- Play\_RC3 Event 没有 SoundBank，因为未设置 Event 的 Inclusion 属性。
- Play\_Music Event 没有 SoundBank，因为该 Event 包含在 User-defined SoundBank Music 中。

|  |  |
| --- | --- |
| [备注] | 备注 |
| **Auto-Defined SoundBanks** 列的内容会在每次对工程作出更改后动态更新。其余列只会在生成 SoundBank 后更新。**Date Updated**（更新日期）列会指示上次更新的时间。 |

Auto-defined SoundBank 不包含媒体文件，只包含 Structure 和 Event。下图显示了察看 Auto-defined SoundBank Play\_RC1 时的 SoundBank Editor 的 Add（添加）和 Edit（编辑）选项卡。Auto-defined SoundBank 的内容无法手动编辑。不过，SoundBank Editor 的各个选项卡会提供有关 Auto-defined SoundBank 的内容和引用的有用信息。

![](../../../../../images/soundbank_editor_auto_defined_add.png)

![](../../../../../images/soundbank_editor_auto_defined_edit.png)

#### 集成

Auto-defined SoundBank 以显式方式排除了媒体。若要使用这种 SoundBank，需添加额外的游戏代码。See the Wwise integration documentation.

- For Unreal: [Understanding Auto-Defined and User-Defined SoundBanks](https://www.audiokinetic.com/library/edge/?source=UE4&id=unreal_using_soundbanks_concepts.html)
- For Unity: [Understanding Auto-Defined and User-Defined SoundBanks](https://www.audiokinetic.com/library/edge/?source=Unity&id=unity_use_soundbanks_concepts.html)

#### 有关此方法的补充说明

下表列出了“自动定义 SoundBank”的优点和缺点。

| 优点 | 缺点 |
| --- | --- |
| 可创建具有较高粒度级别的 SoundBank 和媒体以便游戏引擎根据需要进行管理。  SoundBank 的创建比较简单。  允许综合运用 User-defined SoundBank 和 Auto-defined SoundBank。 | Auto-defined SoundBank 的内容无法手动编辑。  当逐一加载媒体素材时，可能增加磁盘上的读取和寻址次数。  在生成 SoundBank 时，必须生成所有 SoundBank。 |

---