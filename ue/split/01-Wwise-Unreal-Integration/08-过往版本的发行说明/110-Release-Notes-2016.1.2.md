# Release Notes 2016.1.2

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2016.1.2

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed in the 2016.1.2 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.11/4.12 - Wwise 2016.1.2

- **WG-30304** Fixed: "Unload stream level" no longer posts a global "Stop All" to the SoundEngine.
- **WG-30754** Fixed: `FAkAudioDevice::PostEvent` now always returns the playing ID.
- **WG-30804** Fixed: Removed dependencies on the Wwise SDK samples. The new IO system now uses Unreal IO utilities only.