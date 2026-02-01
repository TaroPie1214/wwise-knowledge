# What&#39;s New in 2009.3

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2009.3

The following sections list and describe the changes made to Wwise between version 2009.2.1 and version 2009.3

*Changes that were provided in patches over 2009.2.1 are shown in italics.*

# SDK Folder Structure Changes

- **WG-15799**: Windows libraries (32-bit and 64-bit) are now available for both Visual C++ 2005 and Visual C++ 2008. To differentiate them, the Visual C++ short version was appended to the platform folder name:
  - **Win32\_vc80**: 32-bit binaries built with Visual Studio 2005
  - **Win32\_vc90**: 32-bit binaries built with Visual Studio 2008
  - **x64\_vc80**: 64-bit binaries built with Visual Studio 2005
  - **x64\_vc90**: 64-bit binaries built with Visual Studio 2008

# 平台 SDK 更新

- **WG-15979**: Updated Visual Studio 2005 to version 8.0.50727.867. Note that this Visual Studio update introduced a new version of the CRT libraries and DLLs. Please refer to [通用工具](reference_platform.html#reference_platform_common) for details on what this means in terms of DLL dependencies in your game, and how to work around potential problems by using the StaticCRT version of our libraries.
- **WG-16014**: Update to PS3 SDK 300.001.

# API 变化

- **WG-14515**: New methods in the AudioPlugin interface (NotifyMonitorData()) and in the run-time IAkPluginContext interface (PostMonitorData(), CanPostMonitorData()).
- **WG-15955**: Removed uNumRefillsInVoice from [AkPlatformInitSettings](struct_ak_platform_init_settings.html) structure on the Xbox 360.
- **WG-15533**: Added method [AK::SoundEngine::SeekOnEvent()](namespace_a_k_1_1_sound_engine_a33010f3ba82a8838bb2f4283ee2ee9d7.html#a33010f3ba82a8838bb2f4283ee2ee9d7) to the main API.

# 新功能

- **WG-14515**: Run-time components of plug-ins are now able to send custom data to their UI counterpart (in the authoring tool) to display some feedback to users. This only applies to effects that are placed on busses.
- **WG-15533**: Ability to seek in a playing SFX from the SDK, using the method [SeekOnEvent()](namespace_a_k_1_1_sound_engine_a33010f3ba82a8838bb2f4283ee2ee9d7.html#a33010f3ba82a8838bb2f4283ee2ee9d7). This works for all source formats, on all platforms. It also works (but behaves differently) with music segments. Refer to [AK::SoundEngine::SeekOnEvent()](namespace_a_k_1_1_sound_engine_a33010f3ba82a8838bb2f4283ee2ee9d7.html#a33010f3ba82a8838bb2f4283ee2ee9d7) for more details.
- **WG-15732**: Ability to seek at an arbitrary position in a music segment from the SDK.
- **WG-15733**: Query music segment position through GetSegmentPosition()
- **WG-15799**: Windows libraries (32-bit and 64-bit) are now available for both Visual C++ 2005 and Visual C++ 2008.
- **WG-15963**: Improved error monitoring messages. For example, "Source starvation" messages indicate which source is actually starving. The "Wwise Object" column now displays the appropriate, inspectable object (if applicable). Overall, this helps troubleshooting errors in the sound engine.
- **WG-16066**: Added projects/makefiles to build AkAudioInput sample plugin on PS3, Xbox 360 and Wii (previously Windows only).

# Behavior and Performance Changes

- **WG-15340, WG-15817**: Optimized Vorbis codebook packing resulting in sizeable memory savings.

# Bug Fixes and Miscellaneous Changes

- **WG-15424**: Fixed: Empty random partitions that are created when the partition count is higher than the amount of files in the container don't behave as expected within dialogue events.
- **WG-15478**: Fixed: Ordering of channels is incorrect when using Spread curve on multi-channel audio sources.
- **WG-15621**: Fixed: Music tracks may take longer than expected to update due to WAL Track::AddChild invalidating the clips on the track resulting in an excessive number of calls being made to WAudioSource::GetAudioFormat.
- **WG-15736**: Fixed: Wwise may assert during the playback of looping Vorbis streamed files when the low-level i/o block size is larger than 1.
- **WG-15742**: Fixed (PS3 only): In-memory ADPCM sources crash when becoming physical after loop end when the loop region doesn't cover the whole file.
- **WG-15809**: Fixed: Stopping a continuously playing container in cross-fade mode when using a fade out transition may fail.
- **WG-15825**: Fixed: Situation where a game may crash when the profiler is connected to the game while interactive music is playing.
- **WG-15837**: Fixed: Wwise may crash in certain circumstances when using continuous sequence containers.
- **WG-15866**: Fixed (Xbox 360 only): The 2kB alignment for non-XMA audio in SoundBanks on the Xbox 360 was unnecessary and has been removed.
- **WG-15888**: Fixed (PS3 only): Effect tail never ends when effect is applied to the master bus.
- **WG-15889**: Fixed: Wwise may crash in AkContinuousPBI::PrepareNextToPlay when SoundBanks are unloaded and reloaded at the same time.
- **WG-15893**: Fixed (PS3 only): Occasional loud noise may be heard when using silence plug-in.
- **WG-15898**: Fixed: Some WAV files coming from Pro Tools may fail to play as Original in Wwise application.
- **WG-15902**: Fixed: Wwise may crash when a sound is playing and the SoundBank containing the sound is unloaded, reloaded, and unloaded again in rapid succession.
- **WG-15972**: Fixed (PS3 only): In cases where the size of the Vorbis file is larger than the granularity of the streaming device, the Vorbis voice stops playing but remains alive.
- **WG-15973**: Fixed (PS3 only): CAkDeviceBase::ClearStreams() is executing an inaccurate instruction generated by the compiler.
- **WG-16011**: Fixed: Fast disposal of internal interactive music structures which, in some extreme cases involving a great amount of state changes in small period of time, may provoke stack overflows. Additionnally, this fixed a rare memory leak.
- **WG-16032**: Fixed (PS3 only): Looped ADPCM files within a SoundBank do not play to the end after Break action.
- **WG-16054**: Fixed: Bypass effect setting may be ignored for effects placed within the second, third, and fourth effect slots.
- **WG-16089**: Fixed: RTPCs are erroneously reset globally if [ResetRTPCValue()](namespace_a_k_1_1_sound_engine_ae60a85c95e6a263c2bf1155f6d3887d1.html#ae60a85c95e6a263c2bf1155f6d3887d1) is called with a game object that does not exist.
- **WG-16127**: Fixed: The next music segment within a playlist may play for a short time and then cut-off unexpectedly after transitioning. This may occur if "Exit Cue" and "Play post-exit" are selected, and a transition has just been reverted.
- **WG-16202**: Fixed: Music sync callbacks (AK\_MusicSyncBeat, AK\_MusicSyncBar, AK\_MusicSyncExit) are invalid when posted from segments that do not start at the Entry Cue or at the beginning of the Pre-Entry (for e.g., after a "Same Time As Playing Segment" transition).
- **WG-16244**: Fixed: Wwise may crash when terminating the sound engine if a bank load/unload call occurs between the [Term()](namespace_a_k_1_1_comm_a94e307d2974b89cc4fbc8ab0fef20d2f.html#a94e307d2974b89cc4fbc8ab0fef20d2f) of the audio manager and the bank manager.
- **WG-16267**: Fixed: Race condition exists between the execution of a Stop\_all command that is issued from calls to [AK::SoundEngine::ClearBanks()](namespace_a_k_1_1_sound_engine_ab934f98a6622976d24e0a096911eb0c8.html#ab934f98a6622976d24e0a096911eb0c8), [StopAll()](namespace_a_k_1_1_sound_engine_a0439f61753f31e6b5bb0b42a140ad598.html#a0439f61753f31e6b5bb0b42a140ad598) or a Stop "all" action, and [AK::MusicEngine::Term()](namespace_a_k_1_1_comm_a94e307d2974b89cc4fbc8ab0fef20d2f.html#a94e307d2974b89cc4fbc8ab0fef20d2f).
- **WG-16306**: Fixed: Using specific property configurations of the RoomVerb effect plug-in may cause a DC offset to slowly build up over time.

Introduced in 2009.2.1 Patch 1:

- **WG-15770**: *Fixed: Set Volume events applied to a bus that is the parent of a bus with an environmental effect are incorrectly applied.*
- **WG-15786**: *Fixed: Audio-to-motion continues indefinitely when Motion Offset is more than 0.*
- **WG-15954**: *Fixed: Crash in low memory conditions when using the Audio-To-Motion LPF.*
- **WG-15962**: *Fixed: Memory may become corrupted and Wwise may crash when source starvation occurs with continuous random-sequence containers with sample-accurate transitions.*
- **WG-16040**: *Fixed: Crash in the interactive music engine when using Shuffle and JumpTo transitions.*