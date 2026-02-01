# What&#39;s New in 2013.1.1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2013.1.1

2013.1.1 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2013.1 and version 2013.1.1.

# Platform SDK changes

- DirectX: updated version used by Wwise Authoring to June 2010
- PS3: updated to SDK 440.001
- Xbox One: updated to April XDK QFE 4

# 漏洞修复

- **WG-22987** Fixed: Wwise freezes when viewing the Edit tab of the SoundBank Editor for a SoundBank which has a Music Switch Track.
- **WG-22994** Use safe sprintf variants on Windows and Xbox360 in AK\_OSPRINTF macro.
- **WG-22995** Fixed: crash when importing or opening a project that has a WAV file with 0 samples.
- **WG-22996** Fixed: crash in low-pass filter with a virtual voice in low-memory situation.
- **WG-23007** Fixed: wrong type for [AkThreadProperties](struct_ak_thread_properties.html) members on PS4.
- **WG-23008** Fixed: thread affinity ignored on Xbox One.
- **WG-23011** Corrected PS4-specific documentation in Japanese help file.
- **WG-23015** Fixed: crash in WObjectGroupList<T>::UpdateCombo when state/switch group is deleted.
- **WG-23019** Fixed: Wwise freezes when converting WAV file with extra data past end.
- **WG-23021** Fixed: unnecessary dependency on .NET 4.0 full framework in installer.
- **WG-23029** Fixed: memory leak in default pool when using sample-accurate containers in combination with the 'from elapsed time' virtual voice behavior.
- **WG-23031** Fixed: source editor: discrepancy between the displayed crossfade region and what is heard.