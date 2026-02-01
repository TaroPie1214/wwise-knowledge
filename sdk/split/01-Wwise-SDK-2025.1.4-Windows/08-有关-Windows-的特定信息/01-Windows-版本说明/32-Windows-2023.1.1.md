# Windows 2023.1.1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 2023.1.1

# 构建要求

- **在使用 Visual Studio 2019 构建时**：Windows 10 SDK 2104 (10.0.20348.0)
- **在使用 Visual Studio 2022 构建时**：Windows SDK for Windows 11 (10.0.22621.755)

# 版本说明

以下各节列举并阐述了 2023.1 和 2023.1.1 版本之间针对 Wwise 所作的 Windows 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2023.1.1](whatsnew_2023_1_1.html) 章节。

- [行为改进](windows_releasenotes_2023_1_1.html#windows_behavior_changes_2023_1_1)
- [漏洞修复](windows_releasenotes_2023_1_1.html#windows_bugs_2023_1_1)
- [社区报告的漏洞修复](windows_releasenotes_2023_1_1.html#windows_community_bugs_2023_1_1)

# 行为改进

- **WG-68283** 弃用了 Motion 插件对 DirectInput 的支持。未来的 Wwise 大版本将取消对 DirectInput 的支持。不过，在此之前会提供对 [Microsoft](namespace_microsoft.html) GDK 新增 GameInput API 的支持。在弃用的同时，为 Windows 添加了新的平台初始化设置：AkPlatformInitSettings::bEnableDirectInputSupport。Motion 插件可利用其来控制是否初始化 DirectInput 并将其用于设备枚举。此选项默认设为 false，即禁用 DirectInput。插件中的 XInput 和 libScePad 功能还在且未做修改。

# 漏洞修复

- **WG-68497** 已修复：SoundBank 生成包含非活跃 Audio Device。

# 社区报告的漏洞修复

- **WG-69122** 已修复：在使用系统空间音频对象时，`CAkSinkCoreAudio::SpatialSinkWorkCallback` 引发崩溃。
- **WG-69526** 已修复：在移除设备后，`CAkMotionDeviceMgr::EnumerateXInputDevices` 可能会引发崩溃。