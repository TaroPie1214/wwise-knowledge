# SoundBank Blueprint 函数

|  |
| --- |
| Wwise Unreal Integration Documentation |

SoundBank Blueprint 函数

2022.1 中弃用了大部分 SoundBank 处理函数。有关详细信息，请参阅 [将工程升级到 Wwise 2022.1](pg_important_migration_notes_2022_1_0.html) 章节。

# Clear Banks

针对加载的所有 Wwise 素材卸载 Wwise 资源（Bank 和媒体）。

# Init Bank 函数

您可以使用以下函数来管理 Init Bank：

- **Load Init Bank**
- **Unload Init Bank**

# 已移除和已弃用的函数

自 2022.1 起，不再提供以下 Blueprint 函数。若要针对 Wwise 素材手动加载和卸载 Bank 和媒体资源，请使用 [Wwise Unreal 素材](pg_features_objects_assets.html) 中所述的 **LoadData** 和 **UnloadData** Blueprint 函数。

- **Load Bank**
- **Load Bank Async**
- **Unload Bank**
- **Unload Bank Async**