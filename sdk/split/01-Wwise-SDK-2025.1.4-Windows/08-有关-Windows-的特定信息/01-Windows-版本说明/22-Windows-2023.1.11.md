# Windows 2023.1.11

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 2023.1.11

# 构建要求

- **在使用 Visual Studio 2017 构建时**：Windows 10 SDK 1809 (10.0.17763.0)
- **在使用 Visual Studio 2019 构建时**：Windows 10 SDK 2104 (10.0.20348.0)
- **在使用 Visual Studio 2022 构建时**：Windows SDK for Windows 11 (10.0.22621.755)

# Release Notes

The following sections list and describe the Windows specific changes to Wwise between version 2023.1.10 and version 2023.1.11. For general release notes, please refer to [Release Notes 2023.1.11](whatsnew_2023_1_11.html)

- [Behavior Changes](windows_releasenotes_2023_1_11.html#windows_behavior_changes_2023_1_11)
- [Fixes for Community-Reported Bugs](windows_releasenotes_2023_1_11.html#windows_community_bugs_2023_1_11)

# Behavior Changes

- **WG-76483** Motion 音频设备初始化期间发出的所有日志的 Severity 或 `AK::Monitor::ErrorCode` 现在全部设为 Message 而不是像之前一样将部分日志标记为 Error。

# Fixes for Community-Reported Bugs

- **WG-76553** 已修复：在对采用 HDR 分析的 External Source 实施转码时发生崩溃。