# Windows 2024.1.5

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 2024.1.5

# 构建要求

- **在使用 Visual Studio 2017 构建时**：Windows 10 SDK 1809 (10.0.17763.0)
- **在使用 Visual Studio 2019 构建时**：Windows 10 SDK 2104 (10.0.20348.0)
- **在使用 Visual Studio 2022 构建时**：Windows SDK for Windows 11 (10.0.22621.755)

# 版本说明

以下各节列举并阐述了 2024.1.4 和 2024.1.5 版本之间针对 Wwise 所作的 Windows 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2025.1](releasenotes.html) 章节。

- [社区报告的漏洞修复](windows_releasenotes_2024_1_5.html#windows_community_bugs_2024_1_5)

# 社区报告的漏洞修复

- **WG-77444** 已修复：(Spatial Audio) 倘若发声体和听者之间存在直接视线，而发声体或听者和 Portal 的中心之间不存在视线，为 Portal 应用的 Obstruction 和 Occlusion 在直达路径上会不起作用。