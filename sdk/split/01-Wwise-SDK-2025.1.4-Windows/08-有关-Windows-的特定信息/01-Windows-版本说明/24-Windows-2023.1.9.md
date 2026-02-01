# Windows 2023.1.9

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 2023.1.9

# 构建要求

- **在使用 Visual Studio 2017 构建时**：Windows 10 SDK 1809 (10.0.17763.0)
- **在使用 Visual Studio 2019 构建时**：Windows 10 SDK 2104 (10.0.20348.0)
- **在使用 Visual Studio 2022 构建时**：Windows SDK for Windows 11 (10.0.22621.755)

# 版本说明

以下各节列举并阐述了 2023.1.8 和 2023.1.9 版本之间针对 Wwise 所作的 Windows 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2023.1.9](whatsnew_2023_1_9.html) 章节。

- [漏洞修复](windows_releasenotes_2023_1_9.html#windows_bugs_2023_1_9)
- [文档改进](windows_releasenotes_2023_1_9.html#windows_documentation_improvements_2023_1_9)

# 漏洞修复

- **WG-48302** 已修复：在 Transport Control 中更改当前 State 时发生崩溃。
- **WG-73148** 已修复：对于不使用“米”作为距离单位的游戏引擎，在离听者很近的情况下播放 System Audio Object 时，HRTF 渲染会产生误导性的近场效应。

# 文档改进

- **WG-74817** 添加了有关“Motion 输出设备插件中不支持通过 Bluetooth 连接的 DualSense 手柄”的信息。