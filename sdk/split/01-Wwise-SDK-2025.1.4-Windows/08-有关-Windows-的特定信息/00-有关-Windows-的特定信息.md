# 有关 Windows 的特定信息

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

有关 Windows 的特定信息

本页中包含有关将 Wwise SDK 用于 Windows 平台的专用信息。

# 启用 3D Audio

现在使用 [Microsoft](namespace_microsoft.html) Spatial Sound 实现对 3D Audio 的支持。因此，只有用户在终端（即 Windows 中的音频设备）上启用 Spatial Sound 才可使用 3D Audio 功能。有关更多详细信息（包括如何在各种平台上启用 Spatial Sound），请参阅 [Microsoft Spatial Sound](https://docs.microsoft.com/en-us/windows/win32/coreaudio/spatial-sound)。

在启用 Spatial Sound 时，会将 Main Mix 发送到 [Microsoft](namespace_microsoft.html) Spatial Sound 静态对象（即声道 Bed），并采用 7.1.4 默认声道配置。同时，将 System Audio Object 映射至 [Microsoft](namespace_microsoft.html) Spatial Sound 动态对象。在初始化 System Audio Device 的过程中，Wwise 会检测终端输出配置是针对耳机还是家庭影院。Wwise 将使用终端输出配置决定将 System Audio Device ShareSet 的哪种扬声器配置指派给 Main Mix。

若终端配置为针对耳机，则还会生成 Passthrough Mix 并发送到 WASAPI 播放流。若未生成 Passthrough Mix，会将所有用于 Passthrough Mix 的信号自动发送到 Main Mix。比如，在将总线配置为 **Same as passthrough mix** 时，其会具有与设备的 Main Mix 匹配的混音行为，就像配置为 **Same as main mix** 一样。

The endpoint is configured to output for headphones if the endpoint is a 2-channel output. If the endpoint is **not** detected as a 2-channel output, then the endpoint is assumed to be a home theater setup.

因为 [Microsoft](namespace_microsoft.html) Spatial Sound 动态对象的位置以米为单位，所以 Wwise 会依靠 `AkInitSettings::fGameUnitsToMeters` 设置来实施单位换算。若工程使用的 Game Unit 不以米为单位，请确保使用正确的换算系数来恰当地初始化 `AkInitSettings::fGameUnitsToMeters` 。否则，在双耳合成过程中有些独立对象在近距离情况下听起来可能会很奇怪。

在禁用 Spatial Sound 时，会禁用 3D Audio 支持，并将 Main Mix 直接发送到 WASAPI 播放流。

|  |  |
| --- | --- |
|  | **备注:** 具体有多少可用动态对象，取决于在终端上启用了哪种 Spatial Sound 引擎。对大多数引擎来说，可用动态对象不到 30 个。然而，Wwise 中 System Audio Device 的 System Minimum Object Requirement 属性的默认值为 32。在此默认设置下，大多数引擎实际上都会禁用 Audio Object。若要启用 System Audio Object，须将 System Minimum Object Requirement 的值减到 30 以下。建议将该值设为 16。 |

如需详细了解各种平台组合的静态和动态对象限值，请参阅 [Microsoft Spatial Sound](https://docs.microsoft.com/en-us/windows/win32/coreaudio/spatial-sound) 页面的 [Microsoft](namespace_microsoft.html) Spatial Sound Runtime Resource Implications 章节。

|  |  |
| --- | --- |
|  | **备注:** 在桌面平台上，所有进程只能共用一定数量的 [Microsoft](namespace_microsoft.html) Spatial Sound 动态对象。也就是说，倘若某一进程保有全部动态对象，那么除非其被释放，否则另一进程无法使用它们。  若在终端上启用了 Spatial Sound 且 Wwise 中允许使用 System Audio Object，则 Wwise 声音引擎将尝试保有所有这些对象以供自用。为此，可使用平台设置 AkPlatformInitSettings::bEnableSystemAudioObjects，设为默认情况下禁止在桌面平台上使用 System Audio Object。 |

若要针对 Wwise 设计工具的内部声音引擎启用该选项，请在 Wwise 菜单栏中依次单击 **Audio** > **Authoring Audio Preferences**。这时将打开 Audio Preferences 对话框。在此，选中 **Allow System Audio Objects** 复选框并单击 OK。

# Arm64 support

Wwise supports the Arm64 instruction set. Binaries are compiled using the "ARM64" target in MSVC. When building a native Arm64 application, link with the binaries under `SDK\ARM64`.

Binaries for the Arm64EC ("Emulation Compatible") target are not provided. Wwise does not support dynamically loading a combination of native x86 and Arm plug-ins in the same runtime. The native Arm64 runtime only supports loading Wwise plug-ins compiled as native Arm64 shared libraries.

|  |  |
| --- | --- |
|  | **备注:** Wwise Authoring is an x86-64 application. It therefore only loads x86-64 plug-ins, even when running on an Arm64 machine. Native Arm64 plug-ins must be tested with a separate application. The [Integration Demo 示例](soundengine_integration_samplecode.html) is provided as a native Arm64 application that you can use for this purpose. |

[Windows 版本说明](windows_releasenotes.html)