# Windows 和 Windows UWP 2019.2.8

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2019.2.8

# 要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **Windows Software Development Kit, version 1809 (Visual Studio 2017+)**: [10.0.17763.0](https://go.microsoft.com/fwlink/p/?LinkID=2033908)
- **Windows Software Development Kit (Visual Studio 2015)**: [10.0.14393.795](https://go.microsoft.com/fwlink/p/?LinkId=838916)

# 版本说明

以下各节列举并阐述了 2019.2.7 和 2019.2.8 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2019.2.8](whatsnew_2019_2_8.html) 章节。

- [新增功能](windows_releasenotes_2019_2_8.html#windows_feature_changes_2019_2_8)
- [漏洞修复](windows_releasenotes_2019_2_8.html#windows_bugs_2019_2_8)

# 新增功能

- **WG-49854** Mastering Suite：现在拖动 Multiband Compressor 中的分频滑杆会显示其当前频率。

# 漏洞修复

- **WG-51288** 已修复：随机射线投射引擎中出现除数为零的情况，导致 akmath.h:400 触发断言：(in\_fAngle <= 1.0f) && (in\_fAngle >= -1.0f)。
- **WG-51504** 已修复：驱动程序故障导致 Audio Device 初始化中的 `AK::GetDeviceList` 发生崩溃。
- **WG-51549** 已修复：在 Convolution Reverb 中设置 Impulse Response 文件后撤消操作会引发崩溃。