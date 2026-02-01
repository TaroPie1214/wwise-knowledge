# Release Notes 2018.1.1.6727.1082

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2018.1.1.6727.1082

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed between the 2018.1.0.6714.1065 and the 2018.1.1.6727.1082 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.19/4.20 - Wwise 2018.1.1.6727.1082

- **WG-32970** (Xbox One) Removed warnings when building.
- **WG-38486** Fixed: Crash when removing an always-loaded level that uses `AkRoomComponents` and/or `AkLateReverbComponents`.
- **WG-38741** Fixed: Hang on initialization due to some critical sections being initialized before `AK::SoundEngine::Init`.
- **WG-38805** Corrected Integration to unregister all global callbacks after terminating sound engine.
- **WG-39228** Fixed: WAAPI crash when closing Wwise Authoring and Unreal editor simultaneously.