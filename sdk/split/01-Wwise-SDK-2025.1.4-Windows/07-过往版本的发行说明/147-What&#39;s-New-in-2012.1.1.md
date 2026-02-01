# What&#39;s New in 2012.1.1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2012.1.1

2012.1.1 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2012.1 and version 2012.1.1.

# 平台 SDK 更新

- Vita: updated to SDK 1.6
- Android: updated NDK to r7c
- Wii U: updated to Cafe SDK 2.03 and Cafe VSI 1.4.4

# 漏洞修复

- **WG-20790** Fixed: ASSERT in AkMusicSwitchCtx.cpp in a specific scenario when changing switch rapidly.
- **WG-20707** Fixed: Potential crash when moving objects in Project Explorer.
- **WG-20714** Fixed: Assert with SeekOnEvent if called in same audio frame as StopPlayingID.
- **WG-20743** Fixed: (Xbox 360 only) Unhandled denormals in ParametricEQ cause CPU spike when input is silent.
- **WG-20746** Fixed: Unhandled overflow in Vorbis Conversion Plugin corrupts seek table (most likely to occur with 32KB).
- **WG-20782** Fixed: (Wii only) Rare occurrence of interactive music clip not stopping and indefinitely looping over a few buffers.
- **WG-20776** Fixed: Improved accuracy of GetSourcePlayPosition on 3DS with streamed audio files.
- **WG-20731** Fixed: Possible leak when breaking a playback located under a combinaison of Blend containers and continuous containers.
- **WG-20704** Fixed: Disabling the "follow listener orientation" in 3D User Defined positioning does not start the sound at the right position
- **WG-20729** Fixed: Wrong message in Authoring tool effect tab when an environmental bus has effects.
- **WG-20721** Fixed: Can not delete Switch Container's switch associations in Contents Editor.
- **WG-20733** Fixed: (Wii U) Device callbacks are now properly called in chain (Bink support)

# 新功能

- **WG-20715** Query "Music / Segment to play" can now search for Stingers set to 'nothing' as the segment to play.
- **WG-19825** Wii U: support for 5.1 sources, mixing and output was added.
- **WG-20134** Wii U: Profiler communication is now done through the USB-Ethernet adapter only. This is the same adapter that the original Wii was using.

# iZotope Effects

- Added PDF help documentation for all plugins
- Top 3 most expensive distortions optimized for Xbox360