# Release Notes 2023.1.11

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2023.1.11

此 Integration 的各个版本分别与特定的 Unreal Engine 版本对应。Here is what has changed in the 2023.1.11 release of the integration (in addition to upgrading to the new Unreal build).

|  |  |
| --- | --- |
|  | **注記：**  - 此 Integration 针对 Unreal Engine 5.3、5.4 和 5.5 编译，同时针对 Unreal Engine 5.5 进行了测试。 - 此 Integration 版本不支持实验性的 Unreal Engine 功能。 |

有关早期版本的信息，请参阅 [过往版本的发行说明](previousreleases.html) 章节。

- [New Features](releasenotes_2023_1_11.html#generic_feature_changes_2023_1_11)
- [Bug Fixes](releasenotes_2023_1_11.html#generic_bugs_2023_1_11)
- [Fixes for Community-Reported Bugs](releasenotes_2023_1_11.html#generic_community_bugs_2023_1_11)

# New Features

- **WG-75949** 在 User Settings 中添加了 WAAPI Call Timeout 设置。

# Bug Fixes

- **WG-76353** 已修复：在 Editor 中播放时无法启用 **Visualize Rooms and Portals** 和 **Show Reverb Info** User Settings。
- **WG-76417** 已修复：只要不将 **Unreal Audio Routing** 设为 **Default** 或 **Route through AudioLink**，Unreal Editor 就会在重新启动时发生崩溃。

# Fixes for Community-Reported Bugs

- **WG-76419** 已修复：对于使用 "Wwise Persistent Events" 的 Niagara 系统，在负荷过重的情况下可能会发生崩溃。
- **WG-76500** 已修复：在采用 Debug 配置时，服务器构建失败。
- **WG-76666** 已修复：无法覆盖 Reconcile 的 Move 操作。