# Release Notes 2016.1.0 (Update to UE4.12)

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2016.1.0 (Update to UE4.12)

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed in the 2016.1.0 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.11.2 - Wwise 2016.1

- Added support for UE4.12
- **WG-29917** Fixed: Fixed a case where the attenuation radius of `AkAmbientSounds` did not show up in the Editor window.
- **WG-30000** Fixed: Changed meta properties of `StartAllAmbientSounds` and `StopAllAmbientSounds`.
- **WG-30012** Fixed: Show project supported platforms as "Available Platforms" in the "Generate Sound Banks" window.
- **WG-30014** Fixed: Fixed a crash when starting a Play in Editor session that uses a dedicated server.
- **WG-30031** Fixed: Removed usage of the `World` global pointer.
- **WG-30205** Fixed: On the Mac platform, the Wwise.app path may now contain spaces.