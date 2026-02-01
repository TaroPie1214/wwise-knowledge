# ReadSpeaker speechEngine

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [合作伙伴插件](../00-合作伙伴插件.md) > ReadSpeaker speechEngine

## ReadSpeaker speechEngine

ReadSpeaker speechEngine 插件可为 Wwise 工程提供文本转语音支持。该插件采用自研的文本转语音引擎，其针对性能和内存用量进行了优化，确保可无缝集成并高效地利用资源。它可以在设备端实时处理文本并生成音频，实现动态对白、旁白、GUI 元素诵读等功能。

ReadSpeaker speechEngine 插件具有以下功能和优点：

- 允许诵读屏幕 UI 元素以增强游戏的可玩性。
- 方便在开发前期对配音做原型设计。
- 支持在多人游戏中将聊天消息转化为语音。
- 可几乎零延迟地诵读 AI 生成的文本和对白。
- 可为本地化提供多种语言的母语配音素材。

语音皆由 ReadSpeaker 录制和处理，并与配音演员签订有完全披露协议。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 在 Nintendo Switch 和 PS4 上，语音听起来跟在 Wwise 设计工具中和其他平台上略有不同，原因是其使用了不同的语音模型。 |

## 安装

您可以通过 Audiokinetic Launcher 安装 speechEngine 插件。有关详细信息，请参阅[安装插件](https://www.audiokinetic.com/library/wwise_launcher/?source=InstallGuide&id=installing_plugins)。

在安装插件后，可将其作为 Containers 层级结构下的子对象添加到工程中。另外，也可将其添加为音频源或将 speechEngine 对象与 Event、Game Sync 等关联起来。

## RTPC

Speed、Pitch、Pause 和 Comma Pause 等语音相关参数都支持 RTPC。鉴于 DSP 模型方面的限制，无法实时察看所做的更改，但可在调用之间进行调整。

## 依赖项

若应用程序被静态链接到 speechEngine 插件，则须同时链接到随插件一并分发的 libvtapi 库。比如，对于 Windows 64-bit vc170 平台，该库位于 `SDK\x64_vc170\Release\lib\libvtapi.lib`。

若要在运行时加载插件，以下所列依赖 DLL 必须在系统的 DLL 加载操作能找到的路径：

- `* vt_[lang].dll`

## 在运行时发送文本

您可以使用 [AK::SoundEngine::SendPluginCustomGameData](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_aa1d99f0095ab128c8d9e8052dd2f3931.html) 函数来在运行时从游戏发送文本给插件。

使用 Company ID 和 Plug-in ID 参数在运行时查找插件：

```
in_uCompanyID = 312
in_uPluginID = 1
```

|  |  |
| --- | --- |
| [备注] | 备注 |
| 文本必须采用 UTF-8 字符编码。 |

如需查看完整的 C++ 示例，请参阅随 IntegrationDemo 工程一并提供的 `DemoSpeechEngine.cpp` 文件。

## 局限性

- 每次只能播放一个 speechEngine 声音。
- 首次请求播放特定 speechEngine 语音时延迟时间比较长。后面再播放相同语音的时候延迟时间就跟平时一样了。

---