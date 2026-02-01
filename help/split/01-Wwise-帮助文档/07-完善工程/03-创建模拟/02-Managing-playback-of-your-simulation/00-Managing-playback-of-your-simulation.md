# Managing playback of your simulation

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [创建模拟](../00-创建模拟.md) > Managing playback of your simulation

## Managing playback of your simulation

在将模块添加到 Soundcaster 后，便可以开始使用混音和播放选项了。

在播放模拟时，可以执行以下任何任务：

- 试听平台专有的对象和事件。
- 试听预转码的音频文件。
- 当连接到游戏时，试听与特定游戏对象相关的对象和事件。
- 按您希望的任何顺序播放模块。
- 一次管理一个或所有模块的播放。
- 应用游戏同步器。
- 修改模块的属性。
- 在播放时修改对象的 Event Action。
- 试听互动音乐。

### Specifying Wwise objects to be played

在创建模拟时，您可以根据以下条件选择要播放的声音：

- **平台**，以在模拟中将特定 Wwise 对象在不同的平台上启用或者弃用。有关使用声音和平台的详细信息，请参阅[“Excluding project elements from a platform”一节](../../02-管理平台和语言版本/01-Authoring-across-platforms.md#excluding_project_elements_from_platform "Excluding project elements from a platform")。在创建模拟时，您可以选择只播放当前平台中的声音，也可以选择播放模块中的所有声音。
- **转码后的声音** —— 将音频文件的原始版本与转码版本进行比较。在对导入的音频文件做转码时，Wwise 保留了音频文件的“原始版本”，您可以随时试听该版本。这些文件已经完成导入转码过程，但还没有针对平台进行转码。在默认情况下，Soundcaster 播放经过转码的声音；然而您可以选择播放原始导入版本。

**播放特定平台的声音和振动对象的方法是：**

1. 在工具栏中，验证一下是否已经为模拟选择了正确的平台。
2. 在 Project Explorer 的 Session 选项卡中，双击您要定义的 Soundcaster 会话。

   选定的会话于是被加载到 Soundcaster 中。
3. 在主控区中，单击 Transport Play Options（走带播放选项）图标 (![](../../../../images/btn_more_options_off.png))。
4. 在 Transport Play Options（走带播放选项）菜单中，选择 **Only Play Objects Included in Platform**（仅播放平台中包含的对象）。

   在此仅可试听当前平台中的对象和 Event（事件）。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 若要播放所有对象和 Event，请清除 **Only Play Objects Included in Platform** 选项。这时 Transport Play Options 图标会显示为橙色。 |

**播放未转码声音的方法是：**

1. 在主控区中，单击 Transport Play Options（走带播放选项）图标 (![](../../../../images/btn_more_options_off.png))。
2. 在 Transport Play Options（走带播放选项）菜单中，选择 **Play Originals**（播放原始声音）。

   这时会在 SoundCaster 内的所有模块中播放导入的未转码声音。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 若要播放转码后的声音，请在 Transport Play Options 菜单中选择 **Play Converted**。这时 Transport Play Options 图标会显示为橙色。 |

---