# Windows 和 Windows UWP 2022.1.9

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2022.1.9

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **在使用 Visual Studio 2017 构建时**：Windows 10 SDK 1809 (10.0.17763.0)
- **在使用 Visual Studio 2019 构建时**：Windows 10 SDK 2104 (10.0.20348.0)
- **在使用 Visual Studio 2022 构建时**：Windows SDK for Windows 11 (10.0.22621.755)

# 版本说明

以下各节列举并阐述了 2022.1.8 和 2022.1.9 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2022.1.9](whatsnew_2022_1_9.html) 章节。

- [文档改进](windows_releasenotes_2022_1_9.html#windows_documentation_improvements_2022_1_9)

# 文档改进

- **WG-67002** 更正了对 `AK::GetWindowsDeviceName` 和 `AK::GetWindowsDevice` 的描述，表明在完成设备枚举后会返回 AK\_INVALID\_DEVICE\_ID (-1)。