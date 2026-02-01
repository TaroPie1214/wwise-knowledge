# What&#39;s New in 2010.1.1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2010.1.1

2010.1.1 属于补丁发布. Audiokinetic decided to go with full installers instead of zip files to reduce frequent manipulation errors. The following sections list and describe the changes made to Wwise between version 2010.1 and version 2010.1.1.

# 平台 SDK 更新

- **WG-17601** Upgrade to PS3 SDK 330.001

# 漏洞修复

- **WG-17451** Fixed: Generated soundbanks can be different every time when objects have multiple RTPCs
- **WG-17464** Fixed: Generated soundbanks can be different every time when using Interactive Music playlists
- **WG-17483** Fixed: UnloadBank Async would sometimes not call the completion callback.
- **WG-17487** Fixed: Attenuation of children not working when parent actor-mixer is not included in soundbank
- **WG-17516** Fixed: Stream profile data not displayed properly in the Streaming tab of the Wwise profiler when using more than one I/O device.
- **WG-17523** Fixed: Seek on segment commands are not properly released when terminating the sound engine.
- **WG-17527** Fixed: ASSERT and crash when posting an event with two separate play actions on music object, with the AK\_EnableGetMusicPlayPosition flag.
- **WG-17583** Fixed: Fixed a possible glitch that can occur at the end of the lifespan of a RoomVerb effect (environmental or else)
- **WG-17584** Fixed: Fixed a possible glitch that can occur notably when a RoomVerb effect on an effect chain on a mix bus (or master mix bus) where there is an effect with a tail following. Most often encountered when pausing some sounds making effects enter their FX tail state on mixing busses.
- **WG-17585** Fixed: Performance drop using RoomVerb on PS3 and XBox360
- **WG-17590** Fixed: All mixing session objects (including Actor-Mixer and Busses) are now loaded correctly and send modifications to remote games.
- **WG-17612** Fixed: Wave file with unknown meta data chunk greater than 64 KB fails to play as "original" in the authoring tool.