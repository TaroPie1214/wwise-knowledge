# Release Notes 2018.1.5.6835.1218

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2018.1.5.6835.1218

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed between the 2018.1.4.6807.1189 and the 2018.1.5.6835.1218 release of the integration (in addition to upgrading to the new Unreal build).

|  |  |
| --- | --- |
|  | **注記：** 此 Integration 版本不支持实验性的 Unreal Engine 4 功能。 |

# Unreal Engine 4.19/4.20/4.21 - Wwise 2018.1.5.6835.1218

- **WG-38420** Fixed: Crash when Sequencer AkAudioEvent section is garbage collected while playing.
- **WG-39056** Lists of available properties in the WAAPI widgets have been updated.
- **WG-40197** Ensured the occlusion or obstruction values are properly being set depending on the use of SpatialAudio rooms.
- **WG-40318** Fixed: WAAPI Picker does not refresh.
- **WG-40420** Fixed: Crash when creating a new actor with AkRoom and AkLateReveb components.
- **WG-40542** Added a nice error when you try to generate your first SoundBank with no Event referenced in it.