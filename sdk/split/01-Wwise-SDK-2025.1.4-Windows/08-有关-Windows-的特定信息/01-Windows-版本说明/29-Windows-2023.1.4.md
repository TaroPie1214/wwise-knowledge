# Windows 2023.1.4

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 2023.1.4

# 构建要求

- **在使用 Visual Studio 2017 构建时**：Windows 10 SDK 1809 (10.0.17763.0)
- **在使用 Visual Studio 2019 构建时**：Windows 10 SDK 2104 (10.0.20348.0)
- **在使用 Visual Studio 2022 构建时**：Windows SDK for Windows 11 (10.0.22621.755)

# 版本说明

以下各节列举并阐述了 2023.1.3 和 2023.1.4 版本之间针对 Wwise 所作的 Windows 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2023.1.4](whatsnew_2023_1_4.html) 章节。

- [社区报告的漏洞修复](windows_releasenotes_2023_1_4.html#windows_community_bugs_2023_1_4)

# 社区报告的漏洞修复

- **WG-71509** 已修复：在 Sounds 控制面板中将 Wireless Controller 音频设备标记为 Disabled 时，在 Dualsense (Haptics) 模式下使用 Motion 输出会产生过多的捕获日志消息并反复调用设备初始化回调。