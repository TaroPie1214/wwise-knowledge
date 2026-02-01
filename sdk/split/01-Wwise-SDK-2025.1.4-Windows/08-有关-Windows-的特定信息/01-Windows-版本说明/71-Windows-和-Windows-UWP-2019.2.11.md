# Windows 和 Windows UWP 2019.2.11

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2019.2.11

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **Windows Software Development Kit, version 1809 (Visual Studio 2017+)**: [10.0.17763.0](https://go.microsoft.com/fwlink/p/?LinkID=2033908)
- **Windows Software Development Kit (Visual Studio 2015)**: [10.0.14393.795](https://go.microsoft.com/fwlink/p/?LinkId=838916)

# 版本说明

以下各节列举并阐述了 2019.2.10 和 2019.2.11 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2019.2.11](whatsnew_2019_2_11.html) 章节。

- [漏洞修复](windows_releasenotes_2019_2_11.html#windows_bugs_2019_2_11)
- [社区报告的漏洞修复](windows_releasenotes_2019_2_11.html#windows_community_bugs_2019_2_11)

# 漏洞修复

- **WG-54463** 已修复：在设计工具中选择将 Quadraphonic Haptics 或 DirectInput 设备用于 Wwise Motion 输出时无法保证 Wwise Motion 正常运行。

# 社区报告的漏洞修复

- **WG-54148** 已修复：为某些使用 Steam XInput 手柄模拟的控制器应用 Motion 效果会引发崩溃。