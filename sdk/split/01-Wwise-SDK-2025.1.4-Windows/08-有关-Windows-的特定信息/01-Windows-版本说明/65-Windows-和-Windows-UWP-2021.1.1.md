# Windows 和 Windows UWP 2021.1.1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2021.1.1

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **Windows Software Development Kit, version 1809 (Visual Studio 2017+)**: [10.0.17763.0](https://go.microsoft.com/fwlink/p/?LinkID=2033908)
- **Windows Software Development Kit (Visual Studio 2015)**: [10.0.14393.795](https://go.microsoft.com/fwlink/p/?LinkId=838916)

# 版本说明

以下各节列举并阐述了 2021.1 和 2021.1.1 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2021.1](whatsnew_2021_1.html) 章节。

- [漏洞修复](windows_releasenotes_2021_1_1.html#windows_bugs_2021_1_1)
- [社区报告的漏洞修复](windows_releasenotes_2021_1_1.html#windows_community_bugs_2021_1_1)

# 漏洞修复

- **WG-50130** 已修复：在顶层总线上的效果器具有与 Audio Device 不同的声道配置时混音不当。

# 社区报告的漏洞修复

- **WG-53220** 已修复：在使用 MIDI Keymap Editor 和滑杆时可能会发生崩溃。