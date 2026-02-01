# Windows 2024.1.3

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 2024.1.3

# 构建要求

- **在使用 Visual Studio 2017 构建时**：Windows 10 SDK 1809 (10.0.17763.0)
- **在使用 Visual Studio 2019 构建时**：Windows 10 SDK 2104 (10.0.20348.0)
- **在使用 Visual Studio 2022 构建时**：Windows SDK for Windows 11 (10.0.22621.755)

# 版本说明

以下各节列举并阐述了 2024.1.2 和 2024.1.3 版本之间针对 Wwise 所作的 Windows 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2024.1.3](whatsnew_2024_1_3.html) 章节。

- [行为改进](windows_releasenotes_2024_1_3.html#windows_behavior_changes_2024_1_3)
- [社区报告的漏洞修复](windows_releasenotes_2024_1_3.html#windows_community_bugs_2024_1_3)

# 行为改进

- **WG-76483** Motion 音频设备初始化期间发出的所有日志的 Severity 或 `AK::Monitor::ErrorCode` 现在全部设为 Message 而不是像之前一样将部分日志标记为 Error。

# 社区报告的漏洞修复

- **WG-76553** 已修复：在对采用 HDR 分析的 External Source 实施转码时发生崩溃。