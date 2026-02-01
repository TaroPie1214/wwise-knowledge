# Windows 和 Windows UWP 2022.1.3

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2022.1.3

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **Windows Software Development Kit, version 1809 (Visual Studio 2017+)**: [10.0.17763.0](https://go.microsoft.com/fwlink/p/?LinkID=2033908)

# 版本说明

以下各节列举并阐述了 2022.1.2 和 2022.1.3 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2022.1.3](whatsnew_2022_1_3.html) 章节。

- [社区报告的漏洞修复](windows_releasenotes_2022_1_3.html#windows_community_bugs_2022_1_3)

# 社区报告的漏洞修复

- **WG-64228** 已修复：(Windows) 在音频输出连接出现问题时可能会将音频输出永久静音。
- **WG-64435** 已修复：在设置 `AkJobMgrSettings::fnRequestJobWorker` 的情况下运行声音引擎（即在多核模式下运行）时，无法针对 DirectInput 和 DualSense (Haptics) 输出设备初始化 Wwise Motion，且无法正确初始化 3D Audio。