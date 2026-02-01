# Release Notes 2017.2.2.6553.895

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2017.2.2.6553.895

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed between the 2017.2.1.6524.866 and the 2017.2.2.6553.895 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.17/4.18 - Wwise 2017.2.2.6553.895

- **WG-35044** Made the behavior of overlapping reverb volumes sharing the same Auxiliary Bus more deterministic.
- **WG-36335** Removed unnecessary logs.
- **WG-36369** Added missing include in AkAudioDevice.h.
- **WG-36429** Replaced `LoadModuleChecked` with `GetModulePtr` in `FAkAudioDevice::Init()`.
- **WG-36494** Made `FAkAudioStyle` into a singleton to avoid a non-editor crash.