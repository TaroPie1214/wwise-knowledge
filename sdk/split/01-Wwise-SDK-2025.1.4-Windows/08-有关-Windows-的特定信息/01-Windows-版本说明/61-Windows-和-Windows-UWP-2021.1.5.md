# Windows 和 Windows UWP 2021.1.5

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2021.1.5

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **Windows Software Development Kit, version 1809 (Visual Studio 2017+)**: [10.0.17763.0](https://go.microsoft.com/fwlink/p/?LinkID=2033908)
- **Windows Software Development Kit (Visual Studio 2015)**: [10.0.14393.795](https://go.microsoft.com/fwlink/p/?LinkId=838916)

# 版本说明

以下各节列举并阐述了 2021.1.4 和 2021.1.5 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2021.1.5](whatsnew_2021_1_5.html) 章节。

- [其他改进](windows_releasenotes_2021_1_5.html#windows_misc_2021_1_5)
- [漏洞修复](windows_releasenotes_2021_1_5.html#windows_bugs_2021_1_5)
- [社区报告的漏洞修复](windows_releasenotes_2021_1_5.html#windows_community_bugs_2021_1_5)

# 其他改进

- **WG-57183** 当在 PC 上尝试初始化 Wwise Motion 时，在 Wwise Profiler Log 中添加了诊断信息，以便据此进行调试并解决问题。

# 漏洞修复

- **WG-56853** 已修复：在 Windows 注销过程中，Wwise 发生崩溃。

# 社区报告的漏洞修复

- **WG-53943** 已修复：在为 CrankCase 生成内容时可能会出现竞争危害，并导致在生成 SoundBank 后使用过时的信息。
- **WG-55307** 已修复：在已在线程上调用 `CoInitializeEx(NULL, COINIT_MULITHREADED)` 的情况下，`AK::SoundEngine::GetDeviceList` 返回了一组错误的设备。
- **WG-56727** 已修复：在切换到 Windows 上所用的 Bluetooth 音频设备时发生崩溃。
- **WG-56824** 已修复：在添加与映射到未连接设备的 Device ID 对应的 Wwise Motion 输出时显示 Reverting to default Built-in Audio device 警告消息，并且有些 Master Audio Bus 由预期的 Output Device 重定向到了其他设备。
- **WG-56852** 已修复：在有部分选定行不可见的情况下针对所有选定行更新 **Operation** 下拉菜单时 Import Conflict Manager 发生崩溃。