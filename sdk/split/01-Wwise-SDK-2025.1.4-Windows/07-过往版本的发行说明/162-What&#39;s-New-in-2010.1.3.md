# What&#39;s New in 2010.1.3

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2010.1.3

2010.1.3 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2010.1.2 and version 2010.1.3.

# 新功能

- **WG-17920** In the Positioning tab of the Property Editor, a hierarchical menu is now used to select an Attenuation.

# Behavior and Performance Changes

- **WG-17986** Added separate source starvation notification for XMA decoder.

# 漏洞修复

- **WG-17610** Fixed: Errors about invalid events were displayed when generating banks in cases where there was actually no error.
- **WG-17913** Fixed: PS3 Vorbis decoder crashes on packet header corruption.
- **WG-17952** Fixed: Inoffensive assert "in\_pBranchItem->CanRestoreChainPlayback()".
- **WG-17972** Fixed: Possible memory leak on the Wii when spawning multiple Environmental effects.
- **WG-18069** Fixed: Very rare crash or assert (First() && First()>IsSegment() && First()>SyncTime() == 0) while performing a music transition in a particular scenario.
- **WG-18087** Fixed: Crash when adding a player motion device while playing a 3d Game Defined motion object.
- **WG-18098** Fixed: Rare crash in CAkMusicCtx::OnStopped().
- **WG-18139** Fixed: DirectInput controller that doesn't support rumble could lead to a crash.