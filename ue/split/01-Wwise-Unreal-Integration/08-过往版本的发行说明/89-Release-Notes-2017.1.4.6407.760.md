# Release Notes 2017.1.4.6407.760

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2017.1.4.6407.760

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed between the 2017.1.3.6377.732 and the 2017.1.4.6407.760 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.15/4.16/4.17/4.18 - Wwise 2017.1.4.6407.760

- **WG-33333** Removed obsolete code that tried to handle global focus.
- **WG-34745** Reduced Lower Engine memory pool size on mobile platforms.
- **WG-34879** Exposed the collision channel used for occlusion line trace in AkComponent's properties.
- **WG-35035** Ensured setting the occlusion refresh interval to 0 from Blueprint correctly disables the feature.
- **WG-35104** In a multiplayer scenario, listeners are now properly handled.
- **WG-35463** Fixed: Portals not working on 32-bit platforms.
- **WG-35473** Now register game objects only when the world is valid.
- **WG-35614** Removed coordinates conversion. 有关详细信息，请参阅 [迁移到新的坐标系](migrationnotes_2017_2_0.html#migration_to_new_coord_system) 章节。