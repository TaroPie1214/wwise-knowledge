# Windows 和 Windows UWP 2021.1.3

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2021.1.3

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **Windows Software Development Kit, version 1809 (Visual Studio 2017+)**: [10.0.17763.0](https://go.microsoft.com/fwlink/p/?LinkID=2033908)
- **Windows Software Development Kit (Visual Studio 2015)**: [10.0.14393.795](https://go.microsoft.com/fwlink/p/?LinkId=838916)

# 版本说明

以下各节列举并阐述了 2021.1.2 和 2021.1.3 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2021.1.3](whatsnew_2021_1_3.html) 章节。

- [新增功能](windows_releasenotes_2021_1_3.html#windows_feature_changes_2021_1_3)
- [漏洞修复](windows_releasenotes_2021_1_3.html#windows_bugs_2021_1_3)
- [社区报告的漏洞修复](windows_releasenotes_2021_1_3.html#windows_community_bugs_2021_1_3)

# 新增功能

- **WG-55135** 非 48 kHz 声卡具有更高的输出采样率转码品质。

# 漏洞修复

- **WG-54929** 已修复：在使用 Spatial Audio 的情况下终止 System Audio Device 可能会死机。
- **WG-54931** 已修复：XboxOne vc150 和 Windows vc140 的 Mastering Suite 和 Impacter 插件缺少 DLL 文件。
- **WG-55448** 已修复：在 48 kHz 以外的采样率下运行并针对 Master Audio Bus 使用与实际 Audio Device 不匹配的总线配置时出现音频损坏问题。

# 社区报告的漏洞修复

- **WG-55065** 已修复：在 48 kHz 以外的采样率下运行时，有些 Audio Device 的重采样品质偏低。
- **WG-55131** 已修复：(wp.py) 没有打包与 DLL 文件对应的 PDB。