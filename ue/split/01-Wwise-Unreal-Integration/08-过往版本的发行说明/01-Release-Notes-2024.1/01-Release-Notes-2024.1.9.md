# Release Notes 2024.1.9

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2024.1.9

此 Integration 的各个版本分别与特定的 Unreal Engine 版本对应。This document lists the changes in the 2024.1.9 release of the integration.

**兼容性：**

- Wwise SDK: 2024.1.9
- Unreal：此 Integration 支持并针对 Unreal Engine 5.5、5.6 和 5.7 编译，并且针对 Unreal Engine 5.7 进行了测试。

|  |  |
| --- | --- |
|  | **注記：** 此 Integration 版本不支持实验性的 Unreal Engine 功能。 |

有关早期版本的信息，请参阅 [过往版本的发行说明](previousreleases.html) 章节。

- [新增功能](releasenotes_2024_1_9.html#generic_feature_changes_2024_1_9)
- [行为改进](releasenotes_2024_1_9.html#generic_behavior_changes_2024_1_9)
- [漏洞修复](releasenotes_2024_1_9.html#generic_bugs_2024_1_9)
- [社区报告的漏洞修复](releasenotes_2024_1_9.html#generic_community_bugs_2024_1_9)

# 新增功能

- **WG-70600** 现在会在将鼠标悬停在 Wwise Browser 中的“设置”图标之上时显示 Wwise SoundEngine 和 Wwise Unreal Integration 版本。
- **WG-72432** 现在可在 Reconcile 窗口中双击对象来打开 Unreal Content Browser 并转到对应 UAsset 所在位置。在需要手动删除 UAsset 时，若无其他调和操作可用，则 **Reconcile** 按钮不可用。
- **WG-79876** 添加了对 Unreal Engine 5.7 的支持。

# 行为改进

- **WG-65680** 在 Wwise Browser 的 Event 快捷菜单中将 "WwiseBrowser" 重命名为了 "Playback"。
- **WG-66190** 在 Wwise Browser 中将 "AcousticTextures" 文件夹重命名为了 "Virtual Acoustics"。
- **WG-75940** Wwise Browser 快捷菜单中不再显示不适用于选定条目的选项。
- **WG-76812** 对所有提到 WAAPI Picker 的地方进行了修改，统一了 Wwise Unreal 用户设置中的名称和描述。
- **WG-77437** 在 Wwise Browser 中将 "Orphaned" 文件夹重命名为了 "Found only in Unreal"。
- **WG-79477** 在 Post Event 节点的 Callback Mask 部分将 "MIDIEvent" 重命名为了 "MIDI Event"。
- **WG-79492** 不再默认创建 WwiseMultiReferenceAssetLibrary。

# 漏洞修复

- **WG-74363** 已修复：当 Audiolink 设置中的开始事件无效时会导致崩溃
- **WG-74815** 已修复：在放大时无法正确调整 AkSpotReflector 图标的大小。
- **WG-75194** 已修复：在 Wwise Browser 中双击 Audio\_Device 时不会跳转到对应的 UAsset。
- **WG-76407** 已修复：(WAAPI) 在通过 WAAPI 取消订阅时无法正确停止正在播放的 Event。
- **WG-79760** 已修复：Unreal 5.6 中找不到 **Visualize Rooms And Portals** 和 **Show Reverb Info** 复选框。
- **WG-79975** 已修复：StopWhenOwnerDestroyed 无法停止已卸载的 Sub Level 中的 Event。
- **WG-79976** 已修复：在预览无效的 Wwise Event Asset 时发生崩溃。
- **WG-80214** 已修复：禁用 WAAPI 可能会引发崩溃。
- **WG-80287** 已修复：在启用 **Auto Connect To WAAPI** 设置时 Editor 时不时发生崩溃。

# 社区报告的漏洞修复

- **WG-77531** 已修复：(WAAPI) 在启动 Unreal Editor 时，即便取消选中 **Auto Connect to WAAPI**，WAAPI 客户端也会发生崩溃。
- **WG-79498** 已修复：Unreal Engine 5.6 及更高版本将素材库标记为隐藏的依赖项。