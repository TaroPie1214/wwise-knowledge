# Windows 和 Windows UWP 2019.2.15

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2019.2.15

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **Windows Software Development Kit, version 1809 (Visual Studio 2017+)**: [10.0.17763.0](https://go.microsoft.com/fwlink/p/?LinkID=2033908)
- **Windows Software Development Kit (Visual Studio 2015)**: [10.0.14393.795](https://go.microsoft.com/fwlink/p/?LinkId=838916)

# 版本说明

以下各节列举并阐述了 2019.2.14 和 2019.2.15 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2019.2.15](whatsnew_2019_2_15.html) 章节。

- [漏洞修复](windows_releasenotes_2019_2_15.html#windows_bugs_2019_2_15)

# 漏洞修复

- **WG-58545** 已修复：在打开 REV2 Source Editor 视图的情况下生成 SoundBank 时，有时会出现数据丢失。