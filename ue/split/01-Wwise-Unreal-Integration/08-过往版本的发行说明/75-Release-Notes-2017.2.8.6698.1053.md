# Release Notes 2017.2.8.6698.1053

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2017.2.8.6698.1053

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed between the 2017.2.7.6667.1010 and the 2017.2.8.6698.1053 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.17/4.18/4.19/4.20 - Wwise 2017.2.8.6698.1053

- **WG-36728** Added a Commandlet allowing to generate SoundBanks from the command line.
- **WG-37990** Fixed: (Xbox One) Crash when loading large SoundBank in a packaged game not using PAK files.
- **WG-38420** Fixed: Crash when Sequencer AkAudioEvent section is garbage collected while playing.
- **WG-39091** Made `RoomComponent` and `LateReverbComponent` compatible with level streaming.
- **WG-39097** Removed build warnings about missing samples folder.
- **WG-39113** Fixed: (iOS, Linux, macOS) No audio for Shipping configuration.
- **WG-39115** Fixed: Obstruction refresh issue on Portals.
- **WG-39170** Fixed: Invalid argument passed to `UnloadBank`.
- **WG-39301** Fixed: `CancelEventCallbackCookie` does not properly use user-supplied cookies to cancel.
- **WG-39393** Fixed: (Switch) Invalid State Group ID.
- **WG-39833** Fixed: Reduced the number of calls to SetAuxSends when unnecessary.