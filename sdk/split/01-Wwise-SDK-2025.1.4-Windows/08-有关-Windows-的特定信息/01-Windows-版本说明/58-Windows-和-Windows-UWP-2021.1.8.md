# Windows 和 Windows UWP 2021.1.8

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2021.1.8

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **Windows Software Development Kit, version 1809 (Visual Studio 2017+)**: [10.0.17763.0](https://go.microsoft.com/fwlink/p/?LinkID=2033908)
- **Windows Software Development Kit (Visual Studio 2015)**: [10.0.14393.795](https://go.microsoft.com/fwlink/p/?LinkId=838916)

# 版本说明

以下各节列举并阐述了 2021.1.7 和 2021.1.8 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2021.1.8](whatsnew_2021_1_8.html) 章节。

- [社区报告的漏洞修复](windows_releasenotes_2021_1_8.html#windows_community_bugs_2021_1_8)

# 社区报告的漏洞修复

- **WG-58680** 已修复：在重置 Sink 的情况下更改 Windows 音频设置时断言失败。
- **WG-59058** 已修复：在重新启动声音引擎时发生崩溃。
- **WG-59121** 已修复：在 [Microsoft](namespace_microsoft.html) 平台上使用 3D Audio 时发生 COM 内存泄漏。
- **WG-59146** 已修复：在通过 [Microsoft](namespace_microsoft.html) Spatial Sound 子系统以 Audio Object 形式播放新的声音时出现延迟。
- **WG-59267** 已修复：有时不会报告声部匮乏。
- **WG-59439** 已修复：在反复尝试而无法初始化设备 ID 为 0 的 Wwise Motion 输出设备时生成了过多的日志。