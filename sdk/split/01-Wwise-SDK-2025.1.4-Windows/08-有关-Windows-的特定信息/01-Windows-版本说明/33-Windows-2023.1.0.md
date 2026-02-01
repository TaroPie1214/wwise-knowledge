# Windows 2023.1.0

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 2023.1.0

# 构建要求

- **在使用 Visual Studio 2019 构建时**：Windows 10 SDK 2104 (10.0.20348.0)
- **在使用 Visual Studio 2022 构建时**：Windows SDK for Windows 11 (10.0.22621.755)

# 版本说明

The following sections list and describe the Windows specific changes to Wwise between version 2022.1.8 and version 2023.1.0. For general release notes, please refer to [Release Notes 2023.1.0](whatsnew_2023_1_0.html)

- [API 改进](windows_releasenotes_2023_1_0.html#windows_api_changes_2023_1)
- [其他改进](windows_releasenotes_2023_1_0.html#windows_misc_2023_1)
- [文档改进](windows_releasenotes_2023_1_0.html#windows_documentation_improvements_2023_1)

# API 改进

- **WG-61932** 移除了已经不再需要的 `GetWwiseXAudio2Interface` 和 `GetDirectSoundInstance`。
- **WG-62156** 移除了 UWP 平台。

# 其他改进

- **WG-62824** 取消了对 [Microsoft](namespace_microsoft.html) Spatial Sound 插件的支持。
- **WG-64519** 取消了对 Visual Studio 2017 的支持。

# 文档改进

- **WG-67002** 更正了对 `AK::GetWindowsDeviceName` 和 `AK::GetWindowsDevice` 的描述，表明在完成设备枚举后会返回 AK\_INVALID\_DEVICE\_ID (-1)。