# Setting playback properties

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > [认识 Transport Control 视图](00-认识-Transport-Control-视图.md) > Setting playback properties

## Setting playback properties

通过启用 Transport Control 中的各种控件，您可以执行以下任何操作：

- [“Using original audio files during playback”一节](01-Setting-playback-properties.md#using_original_audio_files_during_playback "Using original audio files during playback").
- [“Including or excluding audio and motion content for playback”一节](01-Setting-playback-properties.md#including_excluding_audio_and_motion_content_for_playback "Including or excluding audio and motion content for playback").
- [“重置 Transport Control”一节](01-Setting-playback-properties.md#resetting_in_transport_control "重置 Transport Control")

### Using original audio files during playback

在转码导入的音频文件时，Wwise 将保留音频文件的原始版本，需要时您可以随时试听它们。原始版本未针对平台进行转码。在默认情况下，Transport Control 播放原始声音；然而，您可以选择播放转码版本。

**播放原始声音的方法是：**

1. 在 Transport Control（走带控制）中，单击 Transport Play Options（走带播放选项）按钮 (![](../../../../images/btn_more_options_off.png))。
2. 在 Transport Play Options（走带播放选项）菜单中，选择 **Play Originals**（播放原始声音）。
3. 点击 **Play** 图标。

   Transport Control 中将播放对象的原始转码前的声音。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若要播放转码后的声音，请在 Transport Play Options 菜单中选择 **Play Converted**。这时 Transport Play Options 按钮会显示为橙色。 |

### Including or excluding audio and motion content for playback

在创建音频、音乐和振动结构时，您可以决定播放或不播放若干个平台中的特定对象。有关使用平台的详细信息，请参阅[“Excluding project elements from a platform”一节](../../07-完善工程/02-管理平台和语言版本/01-Authoring-across-platforms.md#excluding_project_elements_from_platform "Excluding project elements from a platform")。当您播放声音、音乐或振动对象时，可以选择仅播放当前平台中的内容，或者播放加载到 Transport Control 中所有平台的声音、音乐或振动对象。

**播放平台专有的内容的方法如下：**

1. 从工具栏中的 Platform Selector 列表中，为您要试听的对象选择平台。
2. 在 Transport Control（走带控制）中，单击 Transport Play Options（走带播放选项）按钮 (![](../../../../images/btn_more_options_off.png))。
3. 在 Transport Play Options（走带播放选项）菜单中，激活 **Only Play Objects Included in Platform**（仅播放平台中包含的对象）选项。

   此时 Transport Control 中只会播放当前平台中的对象和 Event（事件）。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若要播放所有对象和 Event，请停用 **Only Play Objects Included in Platform** 选项。这时 Transport Play Options 按钮会显示为橙色。 |

### 重置 Transport Control

在 Transport Control 中播放对象时，您可以访问对象的一系列属性、行为和游戏同步器，这可以帮助您模拟游戏内的体验。当您连接到游戏时，某些游戏同步器、效果器和事件也可能影响先前定义的对象属性。Transport Control 中的属性标志为您提供有关在播放期间仍然有效的行为或动作的反馈。要将对象恢复为先前的设置，可使用重置功能。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 对于每个事件播放，事件动作属性值会添加到对象的属性中去。当您使用这些事件动作时，应在重新播放对象前重置这些动作属性，以清空累加属性并恢复默认值。要了解有关事件动作如何影响对象属性的详细信息，请参阅[“处理 Event”一节](../../04-与游戏互动/01-管理-Event/03-处理-Event.md "处理 Event")。 |

**重置特定 Transport Control 属性的方法是：**

1. 在 Transport Control（走带控制）中，单击 Reset（重置）图标 (![](../../../../images/btn_reset_icon_triangle.png))。

   此时将显示 Reset 菜单。
2. 从 Reset 菜单中选择以下其中一项：

   - **Reset All** 可将所有对象恢复到原始设置。
   - **Reset All Random and Sequence Containers** 可清空已为对象触发的所有随机和序列动作。
   - **Reset All Game Parameters** 可清空已为对象触发的所有游戏参数。
   - **Reset All States** 可清空对象的所有 Set State 动作。
   - **Reset All Switches** 可清空已为对象触发的所有 Set Switch 动作。
   - **Reset All Set Mute** 可清空已为对象触发的所有静音动作。
   - **Reset All Set Voice Pitch** 可清空已为对象触发的所有声部音高设置动作。
   - **Reset All Set Voice Volume** 可清空已为对象触发的声部音量设置动作。
   - **Reset All Set Bus Volume** 可清空已为对象触发的总线音量设置动作。
   - **Reset All Set Voice Low-pass Filter** 可清空已为对象触发的所有低通滤波器动作。
   - **Reset All Bypass Effect**  可清空已为对象触发的所有旁通效果动作。
   - **Reset All Set Effect**（重置所有效果器设置）：清除所有已为对象触发的 Set Effect 动作。
   - **Reset All Music Tracks Force Usage** 不再强制播放 Soundcaster 中的特定声轨。
   - **Reset All Source Editor Play Cursors**（重置所有源编辑器播放光标）：清除 Source Editor 中手动触发的播放光标。
   - **Reset Attenuation Preview**（重置衰减预览）：将对象上设置的距离、角度、声障、声笼、衍射和透射值重置为其默认值。

---