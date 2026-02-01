# Release Notes 2017.2.1.6524.866

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2017.2.1.6524.866

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed between the 2017.2.0.6500.836 and the 2017.2.1.6524.866 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.17/4.18 - Wwise 2017.2.1.6524.866

- **WG-34960** Removed min and max properties in AkSlider widget, which are now automatically set via WAAPI.
- **WG-35238** Fixed: All open AkEvent Sequencer segments update to dirty when changes are detected in their Work Units.
- **WG-35773** Added bounds to the`UAkComponent::UseEarlyReflections` *order* parameter.
- **WG-35949** Added ability to generate a single SoundBank containing only an Auxiliary Bus.
- **WG-36083** Removed WAAPI log spam when generating SoundBanks while the Sequencer window is open.
- **WG-36200** Fixed crash when running editor with `-game` flag.
- **WG-36357** Changed Launcher to now copy Visual Studio 2017 dependencies to *ThirdParty* folder.
- **WG-36415** Fixed crash in Unreal when adding new AkSlider in UMG