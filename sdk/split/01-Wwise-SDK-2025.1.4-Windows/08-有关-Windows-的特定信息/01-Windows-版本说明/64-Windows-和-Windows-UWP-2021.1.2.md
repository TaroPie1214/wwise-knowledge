# Windows 和 Windows UWP 2021.1.2

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2021.1.2

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **Windows Software Development Kit, version 1809 (Visual Studio 2017+)**: [10.0.17763.0](https://go.microsoft.com/fwlink/p/?LinkID=2033908)
- **Windows Software Development Kit (Visual Studio 2015)**: [10.0.14393.795](https://go.microsoft.com/fwlink/p/?LinkId=838916)

# 版本说明

以下各节列举并阐述了 2021.1.1 和 2021.1.2 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2021.1.2](whatsnew_2021_1_2.html) 章节。

- [漏洞修复](windows_releasenotes_2021_1_2.html#windows_bugs_2021_1_2)
- [社区报告的漏洞修复](windows_releasenotes_2021_1_2.html#windows_community_bugs_2021_1_2)

# 漏洞修复

- **WG-52690** 已修复：在特定字体大小下，Krotos Igniter Live 文本被裁剪。
- **WG-54463** 已修复：在设计工具中选择将 Quadraphonic Haptics 或 DirectInput 设备用于 Wwise Motion 输出时无法保证 Wwise Motion 正常运行。
- **WG-54830** 已修复：在顶层总线上的效果器具有与 Audio Device 不同的声道配置时混音不当。

# 社区报告的漏洞修复

- **WG-54148** 已修复：为某些使用 Steam XInput 手柄模拟的控制器应用 Motion 效果会引发崩溃。