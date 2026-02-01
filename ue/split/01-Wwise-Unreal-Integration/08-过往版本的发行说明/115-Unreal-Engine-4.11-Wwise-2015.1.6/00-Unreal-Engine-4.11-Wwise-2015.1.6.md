# Unreal Engine 4.11 - Wwise 2015.1.6

|  |
| --- |
| Wwise Unreal Integration Documentation |

Unreal Engine 4.11 - Wwise 2015.1.6

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed in the Unreal Engine 4.11 release of the integration (in addition to upgrading to the new Unreal build).

[迁移说明](migrationnotes_411.html)

# Unreal Engine 4.11 - Wwise 2015.1.6

- The Wwise Unreal integration is now a plug-in. Please see [从 UE4 Wwise Integration 源码迁移到插件版本](migrationnotes_411.html#migrating411_to_plugin) for migration notes.
- **UI-273** Fixed: Create a new uasset type for Auxiliary Busses. This allows one to assign an AuxBus to a SoundBank. 有关详细信息，请参阅 [UAkAuxBus](pg_features_objects_assets.html#features_objects_classes_UAkAuxBus) 章节。
- **UI-280** Fixed: Deprecated "...by name" methods, and replaced then with a string field in the relevant methods. See [Migrating "...by name" methods](migrationnotes_411.html#migrating411_byname) for more information.
- **UI-309** Fixed: Made the Wwise project path relative to the game folder, instead of relative to the UE4Editor.exe file. See [Migrating the Wwise project path](migrationnotes_411.html#migrating411_wwiseproject) for more information.