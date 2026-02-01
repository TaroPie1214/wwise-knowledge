# Windows 和 Windows UWP 2022.1.15

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2022.1.15

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **在使用 Visual Studio 2017 构建时**：Windows 10 SDK 1809 (10.0.17763.0)
- **在使用 Visual Studio 2019 构建时**：Windows 10 SDK 2104 (10.0.20348.0)
- **在使用 Visual Studio 2022 构建时**：Windows SDK for Windows 11 (10.0.22621.755)

# 版本说明

以下各节列举并阐述了 2022.1.14 和 2022.1.15 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2022.1.15](whatsnew_2022_1_15.html) 章节。

- [漏洞修复](windows_releasenotes_2022_1_15.html#windows_bugs_2022_1_15)
- [社区报告的漏洞修复](windows_releasenotes_2022_1_15.html#windows_community_bugs_2022_1_15)

# 漏洞修复

- **WG-66341** 已修复：在声音引擎渲染当中出现长时间停顿或主机应用程序被调试程序暂停后，在输出设备上激活 3D Audio 的情况下持续出现声部匮乏错误。

# 社区报告的漏洞修复

- **WG-72867** 已修复：在 Windows 上将有些音频设备（如 Xbox 360 控制器）设为主声音输出设备时，声音引擎在初始化后无法正常运行并在 Capture Log 中报告 "Hardware audio subsystem stopped responding" 错误。