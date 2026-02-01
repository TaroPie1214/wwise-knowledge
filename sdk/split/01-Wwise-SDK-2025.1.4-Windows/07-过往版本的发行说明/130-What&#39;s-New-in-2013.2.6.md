# What&#39;s New in 2013.2.6

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2013.2.6

2013.2.6 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2013.2.5 and version 2013.2.6.

# Platform SDK changes

- PS4: updated to SDK 1.600
- Xbox One: updated to XDK March 2014

# 新功能

- **WG-22305** (Android) Allow deploying and accessing SoundBanks in both APK and Android file system. Call low-level IO function AddBasePath() to point to an alternate location.
- **WG-24271** AstoundSound plug-ins now available on Android and iOS.
- **WG-24699** (PS4) Support for ATRAC-9 Streaming.

# 漏洞修复

- **WG-24660** Fixed: Possible stack overflow when playing a continuous infinitely looping container with a transition time set to delay of 0 s when nothing is playable
- **WG-24691** Fixed: Invalid display of secondary output voices in Advanced Profiler
- **WG-24692** (WiiU) Fixed: Remote Connection not functioning properly (regression introduced in 2013.2.5)
- **WG-24699** (PS4) Fixed: ATRAC-9 crashes in various scenarios
- **WG-24704** (Xbox 360) Fixed: Peak Limiter meters not displayed correctly when monitoring
- **WG-24709** Possible crash in Advanced Profiler Voices Graph tab when connecting to a game