# Windows 和 Windows UWP 2021.1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2021.1

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **Windows Software Development Kit, version 1809 (Visual Studio 2017+)**: [10.0.17763.0](https://go.microsoft.com/fwlink/p/?LinkID=2033908)
- **Windows Software Development Kit (Visual Studio 2015)**: [10.0.14393.795](https://go.microsoft.com/fwlink/p/?LinkId=838916)

# 版本说明

以下各节列举并阐述了 2019.2.8 和 2021.1 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2021.1](whatsnew_2021_1.html) 章节。

- [其他改进](windows_releasenotes_2021_1.html#windows_misc_2021_1)
- [漏洞修复](windows_releasenotes_2021_1.html#windows_bugs_2021_1)

# 其他改进

- **WG-50478** 弃用了 [Microsoft](namespace_microsoft.html) Spatial Sound 插件。
- **WG-50970** (新的 Wwise 设计工具插件 API) 添加了对 GetResourceHandle 的默认实现。

# 漏洞修复

- **WG-47662** 已修复：Windows 版本的 `AkAtomic.h` 中存在错误的 ARM 专用声明。
- **WG-50071** 已修复：在播放期间更改 Wwise Compressor 效果器的 Channel Link 属性值可能会引发崩溃。
- **WG-50600** 已修复：在有些演示页面中，Integration Demo 无法找到 "Pause\_All\_Global" 和 "Resume\_All\_Global" Event。
- **WG-51099** 已修复：在连接 USB 设备时，音频出现卡顿。
- **WG-52944** 已修复：将未知听者传给 SetGameObjectAuxSendValues 可能会导致不符合预期的行为并引发崩溃。