# Windows 和 Windows UWP 2021.1.13

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2021.1.13

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **在使用 Visual Studio 2015 构建时**：Windows 10 SDK (10.0.14393.0)
- **在使用 Visual Studio 2017 构建时**：Windows 10 SDK 1809 (10.0.17763.0)
- **在使用 Visual Studio 2019 构建时**：Windows 10 SDK 2104 (10.0.20348.0)
- **在使用 Visual Studio 2022 构建时**：Windows SDK for Windows 11 (10.0.22621.755)

# 版本说明

以下各节列举并阐述了 2021.1.12 和 2021.1.13 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2021.1.13](whatsnew_2021_1_13.html) 章节。

- [社区报告的漏洞修复](windows_releasenotes_2021_1_13.html#windows_community_bugs_2021_1_13)

# 社区报告的漏洞修复

- **WG-64228** 已修复：(Windows) 在音频输出连接出现问题时可能会将音频输出永久静音。
- **WG-64784** 已修复：在指定自定义线程关联掩码时发生崩溃。
- **WG-64833** 已修复：在没有有效的 Audio Device 可用时，Universal Windows Platform 发生崩溃。