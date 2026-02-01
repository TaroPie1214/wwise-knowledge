# Windows 2023.1.3

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 2023.1.3

# 构建要求

- **在使用 Visual Studio 2017 构建时**：Windows 10 SDK 1809 (10.0.17763.0)
- **在使用 Visual Studio 2019 构建时**：Windows 10 SDK 2104 (10.0.20348.0)
- **在使用 Visual Studio 2022 构建时**：Windows SDK for Windows 11 (10.0.22621.755)

# 版本说明

以下各节列举并阐述了 2023.1.2 和 2023.1.3 版本之间针对 Wwise 所作的 Windows 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2023.1.3](whatsnew_2023_1_3.html) 章节。

- [社区报告的漏洞修复](windows_releasenotes_2023_1_3.html#windows_community_bugs_2023_1_3)

# 社区报告的漏洞修复

- **WG-70639** 已修复：在终止前取消流播放时，`CAkIOThread::Term` 挂起。