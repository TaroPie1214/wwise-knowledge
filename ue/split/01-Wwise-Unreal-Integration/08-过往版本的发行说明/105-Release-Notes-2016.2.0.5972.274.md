# Release Notes 2016.2.0.5972.274

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2016.2.0.5972.274

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed in the 2016.2.0.5972.274 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.12/4.13 - Wwise 2016.2.0.5972.274

- **WG-29980** Language-specific folders are now parsed to retrieve max attenuation values for Events.
- **WG-30448** Improved logging of AkComponent when attempting to post an invalid AkEvent.
- **WG-30491** Fixed: Make sure to stop sounds when ending a PIE session.
- **WG-31030** Fixed: Optimized `FAkAudioDevice::Get()`.
- **WG-31040** Fixed: Memory leak in AkComponent when attempting to post an invalid AkEvent.
- **WG-31075** Fixed: Removed call to `FAkAudioDevice::Get()` from bank load callbacks in order to prevent crash in module manager.
- **WG-31186** Fixed: Prevent crash in `AkComponentCallback` by canceling Event callbacks when AkComponent gets destroyed.
- **WG-31204** Fixed: Memory leak when a spawned AkComponent failed to post its associated Event.
- **WG-31277** Fixed: Crash in editor when attempting to post an Event on a destroyed actor.