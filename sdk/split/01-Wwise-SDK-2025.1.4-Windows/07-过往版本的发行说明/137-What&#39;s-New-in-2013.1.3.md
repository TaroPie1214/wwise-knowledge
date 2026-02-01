# What&#39;s New in 2013.1.3

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2013.1.3

2013.1.3 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2013.1.2 and version 2013.1.3.

# Platform SDK changes

- Xbox One: updated to July XDK
- PS4: updated to SDK 1.0

# 新功能

- **WG-23343** (Xbox One) Added support for WASAPI sink type, which is now the default.
- **WG-23369** Added Make Up Gain control to Mixing Desk.

# 漏洞修复

- **WG-23245** (PS4) Fixed: [CAkIOThread::Term()](namespace_a_k_1_1_comm_a94e307d2974b89cc4fbc8ab0fef20d2f.html#a94e307d2974b89cc4fbc8ab0fef20d2f) asserts when called twice.
- **WG-23293** (Windows) Fixed: Sound engine could stop functioning when unplugging headphones while using XAudio2 device type.
- **WG-23301** (iOS) Fixed: Assert in sink during sound engine termination.
- **WG-23330** (Xbox 360) Fixed: Stuttering after abruptly stopping all game audio.
- **WG-23339** Fixed: Positioning parameters bound to RTPC on Auxiliary busses are not properly updated during playback.
- **WG-23371** (3DS, Wii, Wii U) Fixed: Crash when reading loudness normalization from ADPCM files that have markers with odd-length names.
- **WG-23377** Fixed: RTPC between 2D and 3D positioning doesn't work in override hierarchy.
- **WG-23379** Fixed: various crashes when running out of memory in Lower Default Pool while creating a voice.