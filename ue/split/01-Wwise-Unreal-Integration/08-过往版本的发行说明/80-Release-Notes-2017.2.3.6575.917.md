# Release Notes 2017.2.3.6575.917

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2017.2.3.6575.917

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed between the 2017.2.2.6553.895 and the 2017.2.3.6575.917 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.17/4.18/4.19 - Wwise 2017.2.3.6575.917

- Added support for Unreal Engine 4.19.
- **WG-36727** Excluded WAAPI from Visual Studio 2017 builds.
- **WG-36883** Moved occlusion raycasts into an async task.
- **WG-37088** Changed to use `GEngine->GetFirstLocalPlayerController()` instead of `UWorld->GetFirstPlayerController()`.
- **WG-37246** Fixed editor crash when starting with -nosound flag.