# Release Notes 2018.1.3.6784.1153

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2018.1.3.6784.1153

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed between the 2018.1.2.6762.1124 and the 2018.1.3.6784.1153 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.19/4.20 - Wwise 2018.1.3.6784.6784.1153

- **WG-36728** Added a Commandlet allowing to generate SoundBanks from the command line.
- **WG-39113** Fixed: (iOS, Linux, macOS) No audio for Shipping configuration.
- **WG-39715** Added a checkbox allowing to disable Spatial Audio on an AkComponent. This allows the use of `SetMultiplePositions` on such a component.
- **WG-39833** Fixed: Reduced the number of calls to `SetAuxSends` when unnecessary.