# Nuendo Connection Settings

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [参考主题](../00-参考主题.md) > [工程](00-工程.md) > Nuendo Connection Settings

## Nuendo Connection Settings

**Nuendo Connection Settings**（Nuendo 连接设置）对话框允许配置 Wwise 和 Steinberg® Nuendo® 数字音频工作站软件之间的链接。但要启用该功能，还需要对 Nuendo 进行一些配置。请参阅 Nuendo 手册了解详情。

|  |  |
| --- | --- |
| [备注] | 备注 |
| Access to the **Nuendo Connection Settings** dialog is only possible if you installed the Nuendo Game Audio Connect plug-in. See [Adding Platform Components to Your Current Installation](https://www.audiokinetic.com/en/library/edge/?source=InstallGuide&id=modyfing_wwise#adding_platform_components_to_your_current_installation) in the Audiokinetic Launcher documentation for details on how to add plug-ins to your Wwise installation via the Audiokinetic Launcher. |

**与 Nuendo 连接后可实现各种交互：**

- 将导出区域拖至 Nuendo 的 Game Audio Connect（游戏音频连接）窗口：通过 [“Audio File Importer 对话框”一节](05-Importing/01-Audio-File-Importer-对话框.md "Audio File Importer 对话框") 将文件直接发送至 Wwise。可对网络中的多台设备执行该操作。
- 在 Nuendo 中导出音频缩混：通知 Wwise 执行音频导入，如果导出目录是两台设备上均可使用的共享路径，则可跨设备执行，并可在 Wwise **Nuendo Connection Settings** 中进行配置。
- 使用 Wwise 对象快捷菜单选项 **Edit in Nuendo**（在 Nuendo 中编辑）：Nuendo 会查找源工程并高亮显示导出的区域。
- **Create in Nuendo**（在 Nuendo 中创建）快捷选项仅适用于 Music Segment（音乐段落）对象。选中后会弹出 Steinberg Hub 窗口，可以在 Nuendo 中创建新的工程。Nuendo 将弹出窗口，询问您 **Do you want to import the transferred Segment into this Project**（是否要将转换的片段导入此工程？）点击 **Yes** 将音乐片段添加到 Project Zone。

| 界面元素 | 描述 |
| --- | --- |
| Server Address | 服务器地址。运行 Nuendo 的设备的网络地址，可以是 IP 地址（如“127.0.0.1”），也可以是主机名（如“localhost”）。将该字段留空，并应用默认值“127.0.0.1”。 |
| Port | Nuendo 连接使用的网络端口，该端口应与在 Nuendo 的 Game Audio Connect 设置的“Local Game Audio Connect TCP Port（本地游戏音频连接 TCP 端口）”字段中选择的值相匹配。将该字段留空，使用默认值“4444”。 |
| Exported asset share path | 导出的素材共享路径。用于通过网络使用 Nuendo 交换素材的文件系统路径，该路径必须针对 Wwise 设置，让 Wwise 能在运行于另外一台设备上时，可找到从 Nuendo 导出的素材。 |

  

|  |  |
| --- | --- |
| [备注] | 备注 |
| For more info on using Wwise with Nuendo, consult the Nuendo documentation on [Exporting Audio Assets to a Game Audio Engine](https://steinberg.help/nuendo/v8/en/cubase_nuendo/topics/game_audio_connect/game_audio_connect_exporting_audio_assets_to_a_game_audio_engine_c.html) and [Game Audio Connect](https://steinberg.help/nuendo/v8/en/cubase_nuendo/topics/game_audio_connect/game_audio_connect_c.html). |

---