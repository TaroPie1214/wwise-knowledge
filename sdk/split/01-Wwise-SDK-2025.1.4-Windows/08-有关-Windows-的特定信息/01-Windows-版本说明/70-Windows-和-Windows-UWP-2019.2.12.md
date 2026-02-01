# Windows 和 Windows UWP 2019.2.12

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2019.2.12

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **Windows Software Development Kit, version 1809 (Visual Studio 2017+)**: [10.0.17763.0](https://go.microsoft.com/fwlink/p/?LinkID=2033908)
- **Windows Software Development Kit (Visual Studio 2015)**: [10.0.14393.795](https://go.microsoft.com/fwlink/p/?LinkId=838916)

# 版本说明

以下各节列举并阐述了 2019.2.11 和 2019.2.12 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2019.2.12](whatsnew_2019_2_12.html) 章节。

- [漏洞修复](windows_releasenotes_2019_2_12.html#windows_bugs_2019_2_12)
- [社区报告的漏洞修复](windows_releasenotes_2019_2_12.html#windows_community_bugs_2019_2_12)

# 漏洞修复

- **WG-53450** 已修复：架构参数格式有误会导致 wp.py 无法运行。
- **WG-54931** 已修复：XboxOne vc150 和 Windows vc140 的 Mastering Suite 和 Impacter 插件缺少 DLL 文件。

# 社区报告的漏洞修复

- **WG-55131** 已修复：(wp.py) 没有打包与 DLL 文件对应的 PDB。