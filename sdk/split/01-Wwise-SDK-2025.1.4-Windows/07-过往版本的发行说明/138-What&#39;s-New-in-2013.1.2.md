# What&#39;s New in 2013.1.2

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2013.1.2

2013.1.2 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2013.1.1 and version 2013.1.2.

# Platform SDK changes

- Xbox One: updated to May XDK
- PS4: update to SDK 0.990

# 漏洞修复

- **WG-23265** Fixed: Wwise Motion Generator Duration parameter is not using valid values with RTPC
- **WG-23271** Fixed: External sources have a potential buffer overrun
- **WG-22964** Fixed: Source Editor | Reset does not refresh curve in Sound Engine
- **WG-23264** Fixed: Motion plays at full volume when sound starts under volume threshold
- **WG-23263** Fixed: ASSERT in CAkVPLSrcCbxNodeBase::ComputeSpeakerMatrix2D when changing positioning type with a game object that has many listeners
- **WG-23261** Fixed: Motion volume not working properly in 3D User Defined mode
- **WG-23120** Fixed: Motion Voice volume not behaving as expected with 2D positioning
- **WG-23055** Fixed: Using source editor trim with HDR envelopes does not work
- **WG-23038** Fixed: Crash when connected and posting in loop the same event
- **WG-23230** Fixed: Crash when reading loudness normalization on some platforms from files that have markers with odd-length names
- **WG-23251** Fixed: Freeze in envelope analysis with very large files
- **WG-23069** Fixed: some ProTools WAV files fail to play in Wwise Authoring when original file playback is enabled.
- **WG-23045** Fixed: Memory leak situation that could happen after running out of memory.
- **WG-23235** Fixed: (WiiU) Ak::SoundEngine::Wii::SendMainToDevice crashes
- **WG-23199** Fixed: (WiiU) Memory corruption when using LPF on WiiU in certain conditions
- **WG-23059** Fixed: (PS3) Pragma push(pack) warnings on PS3 caused by SDK include AkTypes.h.
- **WG-23104** Fixed: (PS3) Meters broken on master audio bus. The displayed level is the same for all channels
- **WG-23135** Fixed: (PS3) Mix busses may be destroyed too early on the PS3, resulting in suboptimal resource allocation
- **WG-23121** Fixed: (iOS) Sound engine will switch to silent mode if iOS audio driver dies.
- **WG-23255** Fixed: (iOS) Crash when locking screen during initialization
- **WG-23247** Fixed: (Android) When app is in background, it is still taking audio CPU