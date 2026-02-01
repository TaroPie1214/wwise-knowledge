# Release Notes 2025.1.0 Beta 1

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2025.1.0 Beta 1

此 Integration 的各个版本分别与特定的 Unreal Engine 版本对应。此文档列出了 Integration 2025.1.0 版本中所作的改进。

**兼容性：**

- Wwise SDK：2025.1.0
- Unreal：此 Integration 支持并针对 Unreal Engine 5.4、5.5 和 5.6 编译，同时针对 Unreal Engine 5.6 进行了测试。

|  |  |
| --- | --- |
|  | **注記：** 此 Integration 版本不支持实验性的 Unreal Engine 功能。 |

有关早期版本的信息，请参阅 [过往版本的发行说明](previousreleases.html) 章节。

- [新增功能](releasenotes_2025_1_0.html#generic_feature_changes_2025_1_0)
- [API 改进](releasenotes_2025_1_0.html#generic_api_changes_2025_1_0)
- [性能改进](releasenotes_2025_1_0.html#generic_perf_changes_2025_1_0)

# 新增功能

- **WG-64937** 为很多 AkAudio 函数添加了性能分析功能。
- **WG-68203** (Spatial Audio) 向 Unreal AkRoomComponent 添加了 Auto Parent 属性。在启用时，Reverb Zone 会按照 Room Priority 自动选择父级 Room。
- **WG-75593** Auto-Defined SoundBank 现在包含预取媒体。其不再单独进行打包。

# API 改进

- **WG-74615** 添加了 Dialogue Event 和 Dynamic Sequence API 桥接。

# 性能改进

- **WG-77849** 提升了 Unreal Insights 中 SCOPED\_WWISE\_NAMED\_EVENT 的性能。