# Windows 和 Windows UWP 2022.1.10

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2022.1.10

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **在使用 Visual Studio 2017 构建时**：Windows 10 SDK 1809 (10.0.17763.0)
- **在使用 Visual Studio 2019 构建时**：Windows 10 SDK 2104 (10.0.20348.0)
- **在使用 Visual Studio 2022 构建时**：Windows SDK for Windows 11 (10.0.22621.755)

# 版本说明

以下各节列举并阐述了 2022.1.9 和 2022.1.10 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2022.1.10](whatsnew_2022_1_10.html) 章节。

- [社区报告的漏洞修复](windows_releasenotes_2022_1_10.html#windows_community_bugs_2022_1_10)

# 社区报告的漏洞修复

- **WG-69122** 已修复：在使用系统空间音频对象时，`CAkSinkCoreAudio::SpatialSinkWorkCallback` 引发崩溃。
- **WG-69526** 已修复：在移除设备后，`CAkMotionDeviceMgr::EnumerateXInputDevices` 可能会引发崩溃。