# Audio Input（音频输入）

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > Audio Input（音频输入）

## Audio Input（音频输入）

Audio Input（音频输入）源插件允许游戏生成的音频内容通过 Wwise 声音引擎进行处理。为此，可以在 Wwise 层级结构中创建 Audio Input（音频输入）源插件，通过 Event 进行触发，然后添加到 SoundBank 中。

使用此源插件可以实现以下目的：

- 从连接到 PC 声卡的麦克风捕获音频。
- 允许 IP 语音通过声音引擎进行处理。
- 直接播放不在 Wwise 工程中的磁盘音频文件。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 有关 Audio Input 的详细信息，请参阅 [Wwise SDK 文档](https://www.audiokinetic.com/library/?source=SDK&id=referencematerial__audioinput.html)。 |

您可能注意到了 Source Plug-in Editor 和 Contents Editor 中的一些属性值旁边带有标志。该标志表明属性值是否通过 RTPC 与 Game Parameter 关联。

下表介绍了这两种类型的 RTPC（实时参数控制）标志：

| 标志 | 名称 | 描述 |
| --- | --- | --- |
| |  | | --- | |  | | RTPC - 开启 | 属性值已使用 RTPC 绑定到游戏中的参数值。 |
| |  | | --- | |  | | RTPC - 关闭 | 属性值未与游戏中的参数值绑定。 |

**编辑器**

- [“Source Editor：Audio Input”一节](01-Source-Editor：Audio-Input.md "Source Editor：Audio Input")
- [“内容编辑器：Audio Input ”一节](02-内容编辑器：Audio-Input.md "内容编辑器：Audio Input")

---