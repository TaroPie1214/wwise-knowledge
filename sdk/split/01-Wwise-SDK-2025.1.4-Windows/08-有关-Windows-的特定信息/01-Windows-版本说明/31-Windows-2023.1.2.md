# Windows 2023.1.2

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 2023.1.2

# 构建要求

- **在使用 Visual Studio 2019 构建时**：Windows 10 SDK 2104 (10.0.20348.0)
- **在使用 Visual Studio 2022 构建时**：Windows SDK for Windows 11 (10.0.22621.755)

# 版本说明

以下各节列举并阐述了 2023.1.1 和 2023.1.2 版本之间针对 Wwise 所作的 Windows 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2023.1.2](whatsnew_2023_1_2.html) 章节。

- [漏洞修复](windows_releasenotes_2023_1_2.html#windows_bugs_2023_1_2)
- [社区报告的漏洞修复](windows_releasenotes_2023_1_2.html#windows_community_bugs_2023_1_2)
- [文档改进](windows_releasenotes_2023_1_2.html#windows_documentation_improvements_2023_1_2)

# 漏洞修复

- **WG-69710** 已修复：在编辑 Music Track 的 Switch 关联时没有更新所要播放的内容，直到关闭并重新打开工程才予以更新。

# 社区报告的漏洞修复

- **WG-69962** 已修复：在游戏暂停/继续情形下尝试访问空间音频扬声器 Bed 时，`CAkSinkCoreAudio::SpatialSinkWorkCallback` 引发崩溃。
- **WG-70061** 已修复：在打开 Wwise 工程时不再要求输入 Perforce 密码。在 Perforce 密码过期时，Wwise 有时会出现卡顿。

# 文档改进

- **WG-69092** 在 [已知问题和限制](whatsnew_known_issues.html) 中添加了已知问题来详细说明在通过 Bluetooth 连接的 XInput 控制器上使用 Motion 时可能出现的性能问题。