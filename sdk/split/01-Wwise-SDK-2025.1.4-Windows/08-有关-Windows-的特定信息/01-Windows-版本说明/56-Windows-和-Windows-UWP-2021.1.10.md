# Windows 和 Windows UWP 2021.1.10

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2021.1.10

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **Windows Software Development Kit, version 1809 (Visual Studio 2017+)**: [10.0.17763.0](https://go.microsoft.com/fwlink/p/?LinkID=2033908)
- **Windows Software Development Kit (Visual Studio 2015)**: [10.0.14393.795](https://go.microsoft.com/fwlink/p/?LinkId=838916)

# 版本说明

以下各节列举并阐述了 2021.1.9 和 2021.1.10 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2021.1.10](whatsnew_2021_1_10.html) 章节。

- [新增功能](windows_releasenotes_2021_1_10.html#windows_feature_changes_2021_1_10)
- [社区报告的漏洞修复](windows_releasenotes_2021_1_10.html#windows_community_bugs_2021_1_10)

# 新增功能

- **WG-58768**添加了对 Visual Studio 2022 的支持。

# 社区报告的漏洞修复

- **WG-59862** 已修复：由于在未启用 3D Audio 时没有在 System 输出设备上准确报告声部匮乏导致出现毛刺噪声。
- **WG-60283** 已修复：在反复尝试而无法初始化设备 ID 为 0 的 Wwise Motion 输出设备时生成了过多的日志。