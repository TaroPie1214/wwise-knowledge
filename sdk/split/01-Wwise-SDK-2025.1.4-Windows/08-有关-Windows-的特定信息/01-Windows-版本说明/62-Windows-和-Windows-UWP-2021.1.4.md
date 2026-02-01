# Windows 和 Windows UWP 2021.1.4

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2021.1.4

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **Windows Software Development Kit, version 1809 (Visual Studio 2017+)**: [10.0.17763.0](https://go.microsoft.com/fwlink/p/?LinkID=2033908)
- **Windows Software Development Kit (Visual Studio 2015)**: [10.0.14393.795](https://go.microsoft.com/fwlink/p/?LinkId=838916)

# 版本说明

以下各节列举并阐述了 2021.1.3 和 2021.1.4 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2021.1.4](whatsnew_2021_1_4.html) 章节。

- [漏洞修复](windows_releasenotes_2021_1_4.html#windows_bugs_2021_1_4)

# 漏洞修复

- **WG-55645** 已修复：无法通过 Property Editor 选择混音器插件。
- **WG-55897** 已修复：在没有音频设备与系统相连的情况下启动声音引擎时，Wwise 无法检测并确认是否连接了新的音频设备。