# Release Notes 2017.1.2.6361.696

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2017.1.2.6361.696

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed between the 2017.1.1.6340.673 and the 2017.1.2.6361.696 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.15/4.16/4.17 - Wwise 2017.1.2.6361.696

- **WG-32413** Fixed: Cannot hear sounds in the Content Browser and the Animation Editor.
- **WG-33970** Fixed: (Mac) Crash when running game with PAK files.
- **WG-34030** Fixed: Properly update the details panel when a surface is removed from an AkSpatialAudioVolume.
- **WG-34083** Fixed: Refresh issue when changing a Spatial Audio Volume's geometry properties.
- **WG-34213** Fixed: Sounds can now be heard from the Content Browser and the Animation Editor.
- **WG-34222** Virtual Acoustics factory ShareSets now appear in the Wwise Picker.
- **WG-34276** Added ability to allow posted Events to continue playing past their associated sections within Level Sequences.
- **WG-34605** Fixed: Portals are not pushed to Wwise Spatial Audio when starting a game, in some circumstances.
- **WG-34630** Fixed: Crash when `-nosound` option is enabled.
- **WG-34703** Fixed: Prevent crash when modifying multiple SpatialAudioVolumes at the same time.
- **WG-34704** Fixed: Prevent crash when unregistering an AkComponent that is a default listener.
- **WG-34745** Fixed: Reduced lower engine memory pool size.