# Windows 和 Windows UWP 2021.1.11

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Windows 和 Windows UWP 2021.1.11

# 构建要求

- **[Microsoft](namespace_microsoft.html) DirectX®**: [DXSDK\_Jun10 (9.29)](https://www.microsoft.com/en-ca/download/details.aspx?id=6812)

  |  |  |
  | --- | --- |
  |  | **备注:** 如果您有多个版本的 SDK，请确保 DirectX® SDK 的环境变量 DXSDK\_DIR 指向正确的目录。 |
- **Windows Software Development Kit, version 1809 (Visual Studio 2017+)**: [10.0.17763.0](https://go.microsoft.com/fwlink/p/?LinkID=2033908)
- **Windows Software Development Kit (Visual Studio 2015)**: [10.0.14393.795](https://go.microsoft.com/fwlink/p/?LinkId=838916)

# 版本说明

以下各节列举并阐述了 2021.1.10 和 2021.1.11 版本之间针对 Wwise 所作的 Windows 和 Windows UWP 特定改进。有关常规版本说明的信息，请参阅 [版本说明 2021.1.11](whatsnew_2021_1_11.html) 章节。

- [行为改进](windows_releasenotes_2021_1_11.html#windows_behavior_changes_2021_1_11)

# 行为改进

- **WG-61311** Xbox 和 Windows 平台上的 System Output Device 现在会在启用 3D Audio 时区分 Headphones 和 Home Theater 配置。这包括在适宜情况下确认使用 System Output Settings ShareSet 中的 Headphones 和 Home Theater 配置，同时避免在检测到 Home Theater 配置时生成 Passthrough Mix。注意，在 System 输出不生成 Passthrough Mix 时，所有原本要发送到 Passthrough Mix 的信号都会转而发送到 Main Mix。在实践中，可藉此实现各种应用场景。比如，将 7.1 信号发送到配置为 **Same as passthrough** 的总线，以便在检测到的配置为 Headphones 时针对直通输出实施立体声下混，或在检测到的配置为 Home Theater 时将信号直接混音为 7.1.4 扬声器 Bed。另外，还可提高耳机输出的 Passthrough Mix 的品质。因为在 Xbox 上不再进行虚拟环绕声处理，以此来提供与其他平台一致的混音效果。