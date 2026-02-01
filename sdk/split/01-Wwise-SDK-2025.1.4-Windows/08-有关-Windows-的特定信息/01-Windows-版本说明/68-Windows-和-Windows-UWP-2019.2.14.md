# Windows 和 Windows UWP 2019.2.14

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2019.2.14

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **Windows Software Development Kit, version 1809 (Visual Studio 2017+)**: [10.0.17763.0](https://go.microsoft.com/fwlink/p/?LinkID=2033908)
- **Windows Software Development Kit (Visual Studio 2015)**: [10.0.14393.795](https://go.microsoft.com/fwlink/p/?LinkId=838916)

# 版本说明

以下各节列举并阐述了 2019.2.13 和 2019.2.14 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2019.2.14](whatsnew_2019_2_14.html) 章节。

- [社区报告的漏洞修复](windows_releasenotes_2019_2_14.html#windows_community_bugs_2019_2_14)

# 社区报告的漏洞修复

- **WG-56620** 已修复：在执行有些自定义内存分配改写操作时，试图在 `AkPipelineBufferBase::ReleaseCachedBuffer` 中释放无效指针。
- **WG-56727** 已修复：在切换到 Windows 上所用的 Bluetooth 音频设备时发生崩溃。
- **WG-56852** 已修复：在有部分选定行不可见的情况下针对所有选定行更新 **Operation** 下拉菜单时 Import Conflict Manager 发生崩溃。