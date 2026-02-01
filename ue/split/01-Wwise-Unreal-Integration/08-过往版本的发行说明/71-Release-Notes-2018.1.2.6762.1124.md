# Release Notes 2018.1.2.6762.1124

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2018.1.2.6762.1124

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed between the 2018.1.1.6727.1082 and the 2018.1.2.6762.1124 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.19/4.20 - Wwise 2018.1.2.6762.1124

- **WG-37990** Fixed: (Xbox One) Crash when loading large SoundBank in a packaged game not using PAK files.
- **WG-38420** Fixed: Crash when Sequencer AkAudioEvent section is garbage collected while playing.
- **WG-38693** 已修复：(WAAPI) 在将 AkAutobahn 用于多个集成包和示例时出现争用问题。
- **WG-39055** Fixed: Display issue where waveform in Sequencer sections would render over text.
- **WG-39091** Fixed: Made `RoomComponent` and `LateReverbComponent` compatible with level streaming.
- **WG-39097** Fixed: Removed build warnings about missing samples folder.
- **WG-39115** Fixed: Obstruction refresh issue on Portals.
- **WG-39170** Fixed: Invalid argument passed to `UnloadBank`.
- **WG-39219** Fixed: WAAPI reconnection issue when Wwise Authoring is quickly restarted.
- **WG-39301** Fixed: `CancelEventCallbackCookie` does not properly use user-supplied cookies to cancel.
- **WG-39334** Re-enabled Opus codec on Android and Mac.
- **WG-39393** Fixed: (Switch) Invalid State Group ID.
- **WG-39604** Fixed: Added description to `PostAndWaitForEndOfEvent`.