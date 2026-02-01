# Windows 2024.1.0

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 2024.1.0

# 构建要求

- **在使用 Visual Studio 2017 构建时**：Windows 10 SDK 1809 (10.0.17763.0)
- **在使用 Visual Studio 2019 构建时**：Windows 10 SDK 2104 (10.0.20348.0)
- **在使用 Visual Studio 2022 构建时**：Windows SDK for Windows 11 (10.0.22621.755)

# 版本说明

The following sections list and describe the Windows specific changes to Wwise between version 2023.1.5 and version 2024.1.0. 有关常规版本说明的信息，请参阅 [版本说明 2024.1.0](whatsnew_2024_1_0.html) 章节。

- [新增功能](windows_releasenotes_2024_1_0.html#windows_feature_changes_2024_1)
- [漏洞修复](windows_releasenotes_2024_1_0.html#windows_bugs_2024_1)
- [社区报告的漏洞修复](windows_releasenotes_2024_1_0.html#windows_community_bugs_2024_1)

# 新增功能

- **WG-69324** 针对适用于 Windows 的 Motion 插件添加了对 GameInput API 的支持。藉此，可在 Wwise 设计工具中测试 Impulse Trigger 所用 Motion 插件在 Xbox 手柄上的行为，并在 Windows 上支持的游戏中使用 Impulse Trigger。在实施这一改进的过程中，我们还移除了 Motion Sink 插件对 DirectInput 的支持以及 `AkPlatformInitSettings::hWnd` 和 `AkPlatformInitSettings::bEnableDirectInputSupport` 初始化设置。有关详细信息，请参阅 [集成 Wwise Motion](integrating_elements_motion.html) 章节。
- **WG-73968** 添加了对 ARM64 目标的支持。

# 漏洞修复

- **WG-68630** 已修复：在内存不足的情况下使用流播放声音时发生死锁。

# 社区报告的漏洞修复

- **WG-74782** 已修复：在尝试为通过 Bluetooth 连接的 DualSense 手柄初始化 Motion 触觉输出设备时一再失败，并且在设备使用不兼容的连接时会发出不准确的错误消息。现在会提供更具体的错误消息。