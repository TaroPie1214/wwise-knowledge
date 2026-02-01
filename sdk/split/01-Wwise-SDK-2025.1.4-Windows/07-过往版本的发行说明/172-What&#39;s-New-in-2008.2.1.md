# What&#39;s New in 2008.2.1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2008.2.1

The following sections list and describe the changes made to the Wwise SDK between version 2008.1.2 (the most recent 2008.1.x release at the time of writing) and version 2008.2.1.

*Changes between 2008.2 and 2008.2.1 are shown in italics.*

# API 变化

- **WG-5054**: Changes to plug-in API for multi-channel support
  - Structure AkPluginAudioBuffer does not exist anymore
  - New class [AkAudioBuffer](class_ak_audio_buffer.html) is defined in [AK\SoundEngine\Common\AkCommonDefs.h](_ak_common_defs_8h.html)
  - The first parameter to IAkPlugin::Execute() is now a pointer to a [AkAudioBuffer](class_ak_audio_buffer.html) instead of a pointer to a AkPluginAudioBuffer
  - See [访问使用 AkAudioBuffer 结构的数据](soundengine_plugins.html#fx_audiobuffer_struct) for more information.
- **WG-10070**: Added StopLooping() on source plug-ins to support Break action.
  - See [AK::IAkSourcePlugin::StopLooping()](soundengine_plugins_source.html#iaksourceeffect_stoplooping) for more information.
- **WG-9354**: Wwise sound engine messages and errors are now displayed to debug output
  - Profiling error messages can be seen/intercepted without having to be connected to Wwise.
  - [AK::Monitor::SetLocalOutput()](namespace_a_k_1_1_monitor_a08ad42ff638aecd238566366598970dc.html#a08ad42ff638aecd238566366598970dc) can be used to select exactly which type of message ('message' and/or 'error') is shown, and also to specify a callback method for alternative processing of messages (logging, etc).
  - See [监控错误](errormonitoring.html) for more information.
- **WG-10780**: Added [AK::Monitor::GetTimeStamp()](namespace_a_k_1_1_monitor_a3f6c8bb7d343e3c92c85be7fd615a3e8.html#a3f6c8bb7d343e3c92c85be7fd615a3e8) method to retrieve the current sound engine timestamp
- **WG-10265**: Removed obsolete velocity member in AkSoundPosition and AkListenerPosition structures.

# 新功能

- *Vorbis format now available on the Wii.*
  - *New library: AkVorbisDecoder.a.*
  - *See [在游戏中集成插件](integrating_elements_codecs.html#soundengine_integration_codec_integrating) for information on registering the Vorbis codec in your game.*
- Added motion feature set.
  - See [集成 Wwise Motion](integrating_elements_motion.html).
- Added multi-channel support.
  - Audio sources, which previously could only be mono or stereo, can now have up to 5.1 channels. For information on how this affects source and effect plug-ins, see [创建声音引擎源插件](soundengine_plugins_source.html) and [创建声音引擎效果器插件](soundengine_plugins_effects.html).
- **WG-9958**: Added sample Subversion source control plug-in with full sources.
  - See [Subversion 版本控制插件示例](referencematerial_samplecode_source_control.html#referencematerial_samplecode_source_control_subversion) for more information.
- **WG-10185**: Added sample Perforce source control plug-in with full sources.
  - See [Perforce 版本控制插件示例](referencematerial_samplecode_source_control.html#referencematerial_samplecode_source_control_perforce) for more information.

# Behavior and Performance Changes

- ***WG-10939**: Fixed: Asserts then crash while changing state during interactive music playback.*
  - Behavior change: SameTime transitions are ignored when there is a transition segment (they used to apply between the transition segment's Exit Cue and the destination segment, which did not really made sense and was useless).
- **WG-9604**: Changes to positioning
  - Stereo sounds will sound louder in stereo setups when 2dPanner is OFF: this is as a result of changing to a direct channel assignment (1-1) from constant power (0.7-0.7).
  - Center% no longer affects stereo sources: this means nothing will come out of the center speaker for stereo sources.
  - 3D positioning with Spatialization checked OFF: now uses default spatialization (center in X and Y) with constant power. It used to be center in X but FRONT in Y. This means that 3D stereo sources with no spatialization used to be heard only in front channels. Now they will be heard in both the front and rear channels, with constant power. As mentioned previously, nothing is played in the Center speaker for stereo sources.
  - 3D positioned stereo sources with a spread=0 or that are perfectly in the middle of the positioning plane, now have a constant power, which means that both channels will lose 3dB.
- **WG-9279**: Xbox 360 Vorbis now using Tremor implementation.
  - Smaller memory footprint than previous implementation

# Bug Fixes and Miscellaneous Changes

- ***WG-10939**: Fixed: Asserts then crash while changing state during interactive music playback.*
  - Behavior change: SameTime transitions are ignored when there is a transition segment (they used to apply between the transition segment's Exit Cue and the destination segment, which did not really made sense and was useless).
- ***WG-11146**: Fixed: Unwanted assertions in Vorbis codec on out-of-memory conditions (all platforms).*
- ***WG-11136**: Fixed: (Interactive music) Problem with "Same Time" transition: A portion of the 1st segment's post-exit is heard during 2nd segment of destination playlist, even if the playlist's transition rules require that it should not play.*
- ***WG-11103**: Fixed: Possible crash when source instantiation fails (because of file not found, not enough memory, or playing a file in Wwise whose format is not natively supported by the Win32 version of the sound engine). Applies to all software pipeline-based platforms (Win32, Xbox 360, PS3).*
- ***WG-11123**: Fixed: Possible infinite loop while converting file.*
- ***WG-11089**: Fixed: Streamed Vorbis sources can get into a state where source starvation will occur indefinitely.*
- ***WG-11083**: Fixed: Possible source starvation with streaming devices that use a block size > 1.*
- ***WG-11062**: Fixed: Streaming | Possible unwanted read request at the end of file.*
- ***WG-11035**: Fixed: Multiple banks referencing the same streaming file aren't all tracked it in the SoundBanksInfo.xml.*
- ***WG-11019**: Fixed: Race condition with blocking (Soundbank) I/O. This could have affected custom implementations of Low-Level I/O.*
- ***WG-11016**: Fixed: Possible memory leak when stopping a sound that notifies markers.*
- ***WG-11006**: Fixed: Divide by zero crashes in AkRSIterator::SelectRandomly. Bug with Random Step groups in Music Playlists used with transition rules that force-specify a segment in the destination playlist.*
- ***WG-10994**: Fixed: Random crashes caused by memory corruption in the Silence source plug-in.*
- ***WG-10944**: Fixed: Sporadic voice starvation on Wii with sample-accurate playback (random-sequence containers with sample-accurate transitions, interactive music). Voice starvations occur on the Wii when hardware voices begin reading out of bounds (they automatically become virtual). The sample-accurate stop could fail in a very specific situation, so a voice starvation would be detected (and handled) at the next update. Sample-accurate stopping now works correctly.*
- ***WG-10889**: Fixed: Motion on Wii crashes when sound is routed to a Wii-remote.*
- *Xbox 360 libraries now built against [Microsoft](namespace_microsoft.html) XDK build 6995.1 (March 2008 SP1).*
- *Temporarily Removed IXmlTextReader.h and IXmlTextWriter.h from the SDK*
  - *These files were added in 2008.2 but have now been temporarily removed because they depend on MFC. They will be re-included in the SDK later when this is fixed.*
- Wii libraries now built against Revolution SDK Version 3.1 patch 4
- PS3 libraries now built against PS3 SDK version 220.002, Toolchain (Win) version 220.002 (based on GCC 4.1.1) and ProDG version 220.1.0
- **WG-7756**: Fixed : Improve memory error reporting.
- **WG-8204**: Fixed : Interactive Music / Soundcaster | empty segment prevents Unpause of other play events.
- **WG-9147**: Fixed : Integrity Report incorrectly displays Vorbis seek table error.
- **WG-9151**: Fixed : PS3: Complete noise at playback with ADPCM zero latency.
- **WG-9325**: Fixed : Positioning reported to (0,0,1) when GameObject set to "FollowListener".
- **WG-9529**: Fixed : Wwise CRASHED when converting an XMA file.
- **WG-9725**: Fixed : Race condition in CancelCallbackCookie when using Marker, EndOfDynamicSequence callbacks.
- **WG-9844**: Fixed : Wwise profiler should show dialog event.
- **WG-9854**: Fixed : Sound engine crashes when trying to log an Insufficient Memory error after Monitor was term()ed.
- **WG-9862**: Fixed : Blend container with multiple children within sequence container breaks trigger rate.
- **WG-9871**: Fixed : Source Starvation when using Vorbis with certain settings.
- **WG-9872**: Fixed : Race condition in [AK::SoundEngine::ClearBanks](namespace_a_k_1_1_sound_engine_ab934f98a6622976d24e0a096911eb0c8.html#ab934f98a6622976d24e0a096911eb0c8).
- **WG-9911**: Fixed : Make the new StopPlayingID and StopAll functionality available through the game simulator.
- **WG-10064**: Fixed : Wwise reverb plug-in – Center channel not reverberated at all.
- **WG-10049**: Fixed : Wii: AcquireVoice called when ResetPlayback was not called previously (Rewrite voice acquisition/kick logic).
- **WG-10114**: Fixed : Sound bank definition files are sometimes incomplete (Switch/states missing).
- **WG-10143**: Fixed : Wii: Do not use frame offset if re-acquiring a voice.
- **WG-10147**: Fixed : Reverb Lite – No tail when used as environemental effect.
- **WG-10201**: Fixed : Actor-Mixer volume changes not propagated to connected Sound Engine.
- **WG-10229**: Fixed : SoundFrame | Remove dependency with ATL.
- **WG-10212**: Fixed : Wii: Paused sounds become virtual.
- **WG-10215**: Fixed : Wii: Stop/Pause/Resume on sample-accurate containers not working properly.
- **WG-10269**: Fixed : File packager | No error message when error is related to info file loading.
- **WG-10387**: Fixed : AkFXMemAlloc dependancy should be removed from AkMemoryMgr.lib.
- **WG-10411**: Fixed : Port XDK to march 2008.
- **WG-10426**: Fixed : Revise CAkVPLSrcCbxNode::IsInitiallyUnderThreshold() to make sure sounds will not get killed when they shouldn't.
- **WG-10523**: Fixed : CRASH when you Generate a SoundBank with a Switch Container missing its Switch or State Group assignment.
- **WG-10585**: Fixed : Command Queue Used in the Performance Monitor might be displaying incorrectly - it reads as 0.12% instead of 12%.
- **WG-10631**: Fixed : Interactive Music: Music & Stinger don't play if loaded in Transport and you're connected to Wwise.
- **WG-10657**: Fixed : Use files instead of registry to identify installed platforms (in Wwise).
- **WG-10765**: Fixed : LEAK: random container with local scope when unregistering game objects.
- **WG-10842**: Fixed : Possible assert in music engine when using more than 2 levels of switch containers.
- **WG-10848**: Fixed : Soundbank content file not printing media data.
- **WG-10863**: Fixed : Possible crash when out of memory and triggering a Reset Action.