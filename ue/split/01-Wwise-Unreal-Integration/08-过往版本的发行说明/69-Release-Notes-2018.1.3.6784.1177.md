# Release Notes 2018.1.3.6784.1177

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2018.1.3.6784.1177

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed between the 2018.1.3.6784.1153 and the 2018.1.3.6784.1177 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.19/4.20/4.21 - Wwise 2018.1.3.6784.1177

- Added support for Unreal 4.21
- **WG-38379**: Added a new Wwise setting for the default Occlusion Collision Channel value used by Ak Component.
- **WG-38497**: Improved stability of the Sequencer while playing and moving around AkAudioEvent.
- **WG-38746**: Added setting to allow using Multi-core rendering.
- **WG-39181**: Fixed: Crash when resizing an AkAudioEvent section in the sequencer to its minimum width.
- **WG-39408**: Wwise Installation Path can now be configured per user. Use Wwise User Settings in the Project Settings to edit the Wwise installation path.
- **WG-39669**: Added parameter restrictions to Wall Occlusion in Ak Room component and Send Level in Ak Late Reverb Component.
- **WG-39713**: UAkAuxBus no longer causes premature initialization of FAkAudioDevice.
- **WG-40128**: Fixed: File handle leak in the IO hook.