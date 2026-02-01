# Release Notes 2017.2.5.6619.962

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2017.2.5.6619.962

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed between the 2017.2.4.6590.933 and the 2017.2.5.6619.962 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.17/4.18/4.19 - Wwise 2017.2.5.6619.962

- **WG-37624** Allowed to perform an asset diff on the Wwise .uasset files.
- **WG-37736** Reorganized some WAAPI Blueprint nodes under the "Audiokinetic" category.
- **WG-37790** Fixed bad listener handling that caused Spatial Audio failures in editor.
- **WG-37808** Fixed errors for WAAPI builds on Visual Studio 2017.
- **WG-37917** Ensured the plug-in compiles when the game does not use precompiled headers.
- **WG-38041** Fixed crash when performing occlusion calculations.
- **WG-38142** Fixed crash due to initialization of `AkOcclusionObstructionService` not binding `SetOcclusionObstructionFcn` when refresh interval is 0.