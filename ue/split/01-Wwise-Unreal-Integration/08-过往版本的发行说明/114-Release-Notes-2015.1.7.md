# Release Notes 2015.1.7

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2015.1.7

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed in the 2015.1.7 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.12 - Wwise 2015.1.7

- **WG-29917** Fixed: Fixed a case where the attenuation radius of `AkAmbientSounds` did not show up in the Editor window.
- **WG-29991** Added `AkEvent String Input Field` to `AkAmbientSound`.
- **WG-29997** Suppressed duplicate "LogAkAudio: StopAll API called" entries in the output log.
- **WG-30000** Fixed: Changed meta properties of `StartAllAmbientSounds` and `StopAllAmbientSounds`.
- **WG-30012** Fixed: Match the list of available platforms for SoundBank generation to the Supported Platforms under the Unreal project settings.
- **WG-30014** Fixed: Fixed a crash when starting a Play in Editor session that uses a dedicated server.
- **WG-30031** Fixed: Removed usage of the `World` global pointer.
- **WG-30218** Fixed: Crash when connecting the Wwise Profiler to the Android platform.
- **WG-30255** Fixed: UE4 crash when adding key to `Ak Event Track` in Matinee.