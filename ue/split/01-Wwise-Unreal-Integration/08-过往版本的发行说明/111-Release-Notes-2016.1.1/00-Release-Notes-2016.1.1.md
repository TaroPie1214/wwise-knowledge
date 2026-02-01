# Release Notes 2016.1.1

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2016.1.1

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed in the 2016.1.1 release of the integration (in addition to upgrading to the new Unreal build).

[Migrating to the UE4.11/4.12 Wwise 2016.1.1 integration](migration_to_2016_1_1.html)

# Unreal Engine 4.11/4.12 - Wwise 2016.1.1

- **WG-29972** Fixed: Multiple potential threading issues with the auto-destroy behavior of the AkComponent.
- **WG-29979** Fixed: EndOfEvent callbacks are now always called.
- **WG-30004** Fixed: SetGameObjectOutputBusVolume is now exposed in Blueprints and AkAudioDevice.
- **WG-30404** Fixed: The attenuation scaling factor now properly works on `AkComponents`.
- **WG-30409** Fixed: It is now possible to decode Vorbis-encoded files.