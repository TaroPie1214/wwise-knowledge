# Wwise 系统要求

[Wwise 帮助文档](../00-Wwise-帮助文档.md) > [入门](00-入门.md) > Wwise 系统要求

## Wwise 系统要求

在安装 Wwise 之前，确保系统满足最低配置要求。下表列出了安装和运行 Wwise 设计工具所需的硬件和软件。

| 系统组件 | 要求 |
| --- | --- |
| 操作系统 | This version of Wwise was tested on the following operating systems:  - Windows 11 64-bit - macOS Sequoia  If you are using a more recent operating system and you experience issues with Wwise, we recommend that you upgrade to the latest available version of Wwise.  Wwise 设计工具现在仅提供 64 位版本。 |
| Memory | 4 GB 内存 |
| 分辨率 | 出厂布局针对 1920 x 1080 分辨率的显示器进行了优化，不过也可通过调整来适配其他分辨率。如需支持 4K 或 5K 显示器，请在 Wwise 的 User Preferences（用户首选项）窗口中选中 **Enable High DPI**（启用高分辨率）复选框。 |
| PDF 阅读器 | 为了能够打开 Wwise 分发的 PDF 文件，需要安装 Adobe Reader 或其他 PDF 阅读器。 |
| **必需代码依赖项** | |
| Microsoft .NET Framework | Microsoft .NET Framework 4.8  Audiokinetic Launcher 会在安装 Wwise 之前自动安装此组件。不过，倘若使用 Launcher 以外的途径部署 Wwise（比如通过 Perforce 或其他版本控制系统），则须手动安装 .NET Framework 以便运行 File Packager。Refer to the [Microsoft .NET Framework download page](https://dotnet.microsoft.com/en-us/download/dotnet-framework). |

|  |  |
| --- | --- |
| [备注] | 备注 |
| 在不使用 Launcher 安装 Wwise 时，假如缺少一个或多个依赖项，很有可能会发生崩溃。The required dependencies are detailed in the following rows of the Wwise System Requirements table: [Microsoft .NET Framework](01-Wwise-系统要求.md#microsoft_net_framework). 建议使用 Launcher 安装设计工具，以此确保同时安装相应的依赖项。 |

---