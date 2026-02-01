# Release Notes 2025.1.1 Beta 2

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2025.1.1 Beta 2

此 Integration 的各个版本分别与特定的 Unreal Engine 版本对应。此文档列出了 Integration 2025.1.1 版本中所作的改进。

**兼容性：**

- Wwise SDK：2025.1.1
- Unreal：此 Integration 支持并针对 Unreal Engine 5.4、5.5 和 5.6 编译，同时针对 Unreal Engine 5.6 进行了测试。

|  |  |
| --- | --- |
|  | **注記：** 此 Integration 版本不支持实验性的 Unreal Engine 功能。 |

有关早期版本的信息，请参阅 [过往版本的发行说明](previousreleases.html) 章节。

- [新增功能](releasenotes_2025_1_1.html#generic_feature_changes_2025_1_1)
- [其他改进](releasenotes_2025_1_1.html#generic_misc_2025_1_1)
- [漏洞修复](releasenotes_2025_1_1.html#generic_bugs_2025_1_1)
- [社区报告的漏洞修复](releasenotes_2025_1_1.html#generic_community_bugs_2025_1_1)
- [文档改进](releasenotes_2025_1_1.html#generic_documentation_improvements_2025_1_1)

# 新增功能

- **WG-78502** 添加了对 Unreal Engine 5.6 的支持。

# 其他改进

- **WG-78366** 降低了 AssetLibrary 日志的严重性。

# 漏洞修复

- **WG-79093** 已修复：在退出时，AudioType Resources 有时出现卡顿或发生崩溃。

# 社区报告的漏洞修复

- **WG-76672** 已修复：在 Unreal Niagara Module 中调用 `ConditionalBeingDestroy` 时可能会发生崩溃。
- **WG-77138** 已修复：在将所有参数保留设为默认值并启用 AutoPost 时， `FAkAudioDevice::SpawnAkComponentAtLocation` 导致检查失败。
- **WG-77589** 已修复：Wwise Simple External Source Manager 因 Data Table 无效而发生崩溃。
- **WG-77912** 已修复：在卸载相应模块后才卸载 SoundEngine，导致在执行回调和流播放时发生崩溃。
- **WG-77946** 已修复：在为 `ExecutionQueue` 和 `DeferredQueue` 使用 `TQueue` 时可能会发生崩溃。
- **WG-78708** 已修复：由于 `FWwiseAssetLibraryProcessor::FilterLibraryAssets` 比较复杂，导致在 Unreal 中使用 Wwise Asset Library 时出现性能问题。

# 文档改进

- **WG-77640** 现在建议使用 AudioLink 而非 AkAudioMixer。
- **WG-79087** 在 Unreal Project Settings 页面添加了之前缺失的 Spatial Audio 设置。