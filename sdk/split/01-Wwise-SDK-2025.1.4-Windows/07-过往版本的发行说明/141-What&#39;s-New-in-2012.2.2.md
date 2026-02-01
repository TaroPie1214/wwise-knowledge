# What&#39;s New in 2012.2.2

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2012.2.2

2012.2.2 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2012.2.1 and version 2012.2.2.

# Platform SDK changes

- Mac/iOS: updated to Xcode 4.5

# 漏洞修复

- **WG-21628** Fixed: XMA decoder starvation with in-memory XMA in interactive music.
- **WG-21833** Fixed: AK::SoundFrame::IGameParameter::GetGUID always returns GUID\_NULL.
- **WG-21907** Fixed: an issue where opening a Wwise project in 2012.2 that was migrated from an earlier version of Wwise on a separate computer that already had the project in the earlier version could add invalid data in the master mixer work unit. The problem shows up only in some projects. It is caused by temporary file left on the computer thet was not migrated at the same time with the project. A common case where this could happen is when using source control for the Wwise project and updating on a separate computer the migrated version while having a leftover PROJECT.USERNAME.wsettings file in the project directory that was not migrated.
- **WG-21946** Fixed: Various playback accuracy fixes on PS VitaHW. A warning is now displayed when converting files using ATRAC-9 settings which might result in playback issues.
- **WG-21957** Fixed: Any global stop action on a specific element target which is "missing" will act like a global stop all event, but only on continuous items.
- **WG-21992** Fixed: No SoundBanks generated when using ISoundFrame::GenerateSoundBanks with WwiseCLI -SoundFrameServer.
- **WG-21994** Fixed: SoundBanks containing impulse responses for Convolution Reverb on busses are always generated.
- **WG-22023** Fixed: Exiting game from WiiU HBM may hang.
- Fixed: Incorrect Voice Starvation notification on PS Vita.