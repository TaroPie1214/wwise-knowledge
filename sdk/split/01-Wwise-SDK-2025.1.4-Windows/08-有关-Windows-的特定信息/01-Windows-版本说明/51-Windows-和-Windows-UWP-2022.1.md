# Windows 和 Windows UWP 2022.1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2022.1

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **Windows Software Development Kit, version 1809 (Visual Studio 2017+)**: [10.0.17763.0](https://go.microsoft.com/fwlink/p/?LinkID=2033908)

# 版本说明

以下各节列举并阐述了 2021.1.9 和 2022.1 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2022.1](whatsnew_2022_1.html) 章节。

- [行为改进](windows_releasenotes_2022_1.html#windows_behavior_changes_2022_1)
- [漏洞修复](windows_releasenotes_2022_1.html#windows_bugs_2022_1)

# 行为改进

- **WG-61205** 通过 Windows 上 Motion 插件输出设备控制的 XInput 手柄现在在所有振幅下都具有更加一致的响应（尤其包括在低输入振幅下增强振动的情况）。这使得 Windows 上 Motion 插件输出设备的行为与其在 UWP、Xbox One 和 Xbox Series X 上的行为一致。

# 漏洞修复

- **WG-54716** 已修复：在调整 Platform Manager 对话框的大小时，按钮可能会被裁剪。
- **WG-54809** 已修复：Wwise Wave Viewer 中缺少包含提示的开始页面。
- **WG-58035** 已修复：驱动器相关路径无法用作 Wwise Console 参数。
- **WG-60189** 已修复：在文件系统中隐藏了控制器设置文件时发生崩溃。