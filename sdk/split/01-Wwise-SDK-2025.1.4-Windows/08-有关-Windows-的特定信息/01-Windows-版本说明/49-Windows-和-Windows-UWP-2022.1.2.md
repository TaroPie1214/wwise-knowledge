# Windows 和 Windows UWP 2022.1.2

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2022.1.2

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **Windows Software Development Kit, version 1809 (Visual Studio 2017+)**: [10.0.17763.0](https://go.microsoft.com/fwlink/p/?LinkID=2033908)

# 版本说明

以下各节列举并阐述了 2022.1.1 和 2022.1.2 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2022.1.2](whatsnew_2022_1_2.html) 章节。

- [漏洞修复](windows_releasenotes_2022_1_2.html#windows_bugs_2022_1_2)

# 漏洞修复

- **WG-61464** 已修复：在将 System Audio Object 位置发送到终端的 3D Audio 系统时，没有将 `AkInitSettings::fGameUnitsToMeters` 考虑在内。