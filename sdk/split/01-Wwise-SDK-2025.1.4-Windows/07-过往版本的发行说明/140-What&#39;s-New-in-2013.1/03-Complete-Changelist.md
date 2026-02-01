# Complete Changelist

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Complete Changelist

The following sections list and describe the changes made to Wwise between version 2012.2.2 and version 2013.1.

# 平台 SDK 更新

- Perforce SDK was updated to version 2012.2
- Mac/iOS: Updated to Xcode 4.6 (LLVM 4.2)
- iOS: Updated to SDK 6.1 (supported architectures are now armv7 and armv7s)
- 3DS: Updated to CTR-SDK 4.2.4
- PS3: Updated to SDK 430.001
- Xbox 360: Updated to XDK November 2012 (build 21250.1)
- Wii U: Updated to Cafe SDK 2.08.13 and Multi 5.3.19
- Android: Updated to NDK r8d

# 新功能

- **WG-21536** Now possible to add randomizers on the loop count of random and sequence containers.
- **WG-21707** Added low-level I/O sample code for loading SoundBanks within Android APKs. Android IntegrationDemo now deploys SoundBanks as part of the APK.
- **WG-21723** It is now possible to add custom speaker volume gains per listener to internal spatialized volume computations.
- **WG-21995** Positioning behavior (2D/3D) can be selected with RTPC.
- **WG-22283** Attenuation based on distance can now be controlled independently when using Game defined Aux Sends and User Defined Aux Sends.
- **WG-22538** A limited version of music switch container seeking is now available.
- **WG-22657** Finer granularity now supported in music grid (1/16 and 1/32).

# API 变化

- **WG-14431** On Windows, XAudio2 is now the default audio API used for audio output, with a fallback to DirectSound when not available. The new AkPlatformInitSettings::eSinkType parameter can be used to modify this behavior.
- **WG-21251** It is now required to specify a valid memory pool ID to the initialization of the sound engine to use the prepare media mechanism. We removed the default behavior (allocation in the Default memory pool when not specified) as it was only causing confusion.
- **WG-21251** (Xbox360 Only) The Default memory pool memory is now allocated using malloc instead of PhysicalAlloc.
- **WG-21615** Removed in\_ulListenerIndex from [SetPosition()](namespace_a_k_1_1_sound_engine_a789e25bda32d1e11849afb6584942455.html#a789e25bda32d1e11849afb6584942455). Workaround is to set the position of the game object directly to that of the corresponding listener.
- **WG-21635** Migration iOS:
  - Migration: iOS SDK now uses a new header AkiOSSoundEngine.h. You need to include this new header instead of AkMacSoundEngine.h.
  - API Change:
    - Added a new API to handle audio session interruption at the app level.
    - Updated [AkPlatformInitSettings](struct_ak_platform_init_settings.html) for iOS to allow users to select whether to handle audio session interruptions at the app level or not.
- **WG-21759** Added methods to the SoundFrame API:
  - AK::SoundFrame::IGameParameter::Default returns the default value of the game parameter
  - AK::SoundFrame::ISoundFrame::GetConversionSettingsList lists all available conversion settings
  - AK::SoundFrame::ISoundFrame::ConvertExternalSources performs conversion of specified input source files
  - AK::SoundFrame::ISoundFrame::ResetRTPCValue provides functionality matching [AK::SoundEngine::ResetRTPCValue](namespace_a_k_1_1_sound_engine_ae60a85c95e6a263c2bf1155f6d3887d1.html#ae60a85c95e6a263c2bf1155f6d3887d1)
- **WG-21803** AK::SoundEngine::Unloadbank prototype changed:
  - When loading banks using an in-memory location, it is now allowed to load the same bank from two different memory locations simultaneously. Also, when loading banks from in-memory locations, it is now required to unload the bank using the same in-memory pointer that was used at the load call. This new requirement allows selecting which of the in-memory banks must be unloaded. To avoid confusion upon migration, the new parameter is now mandatory and NULL should be specified if the bank was not loaded from an in-memory location.
  - When multiple banks are sharing the same media and media is duplicated in memory, priority is given to the media from the latest loaded bank.
- **WG-22001** Source and insert effect plugins are now able to access the Playing ID and Game Object ID associated to the sound structure on which they are playing, as well as the game object and listener positions in cartesian and spherical coordinates.
- **WG-22259** New API: AK::SoundEngine::Wii::SetDRCVolume() can be used to set the volume of the DRC audio mix.
- **WG-22527** Calling [AK::SoundEngine::UnloadBank](namespace_a_k_1_1_sound_engine_ac91406bc2fe061e4248cb448207b5a64.html#ac91406bc2fe061e4248cb448207b5a64) with a specified bank not previously loaded now returns AK\_UnknownBankID instead of AK\_Success.

# Behavior Changes

- **WG-21393** Volume threshold evaluation now takes bus gains of all signal paths into account and takes the maximum. This means that a voice will become virtual if both its dry and wet paths are below threshold. Also, voices routed to a mixing bus will become virtual when the output bus volume is brought down.
- **WG-21803**
  - When loading banks using an in-memory location, it is now allowed to load the same bank from two different memory locations simultaneously. Also, when loading banks from in-memory locations, it is now required to unload the bank using the same in-memory pointer that was used at the load call. This new requirement allows selecting which of the in memory banks must be unloaded.
  - When multiple banks are sharing the same media and media is duplicated in memory, the media from the latest loaded bank has priority.
- **WG-22164** Sources now restart with perfect synchronization after source starvation has occurred under the interactive music hierarchy. The counterpart is that the starving source remains silent for some time (the track's look-ahead time) before restarting.

# Performance Changes

Android now runs 10% faster. Vorbis and many effects have been optimized on several platforms. Here's an overview of the performance factors (as a reference, 1x represents status quo while 2x means that an effect runs twice as fast as before):

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Xbox 360** | **PS3** | **Wii U** |
| Matrix Reverb | **-** | **-** | 4.6x |
| Flanger | 1.1x to 1.8x | 1.3x | 1.5x to 2.4x |
| LPF | 1.2x | 1.8x | 1.1x |
| Time Stretch | 1.1x to 2.4x | 1.3x to 1.6x | 2.5x to 3x |
| Convolution Reverb | 1.3x to 1.7x | 1.1x to 1.3x | 8x to 10x |
| Guitar Distortion | 1.4x to 1.7x | 1.1x to 1.5x | 1.4x to 2x |
| Tremolo | 5.5x | 1.25x | 4.4x |
| Harmonizer | 1.1x to 1.2x | 1.3x | 1.5x to 2.2x |
| Vorbis | Up to 2% | Up to 4.5% | 10 to 15% |

# Miscellaneous Changes

- **WG-21619** Migration support for Wwise projects saved with Wwise prior to version 2007.2 has been removed.
- **WG-21728** Removed useless Windows files from Mac/iOS installers.
- **WG-21878** WwiseCLI can now perform project migration when -Save option is specified.

# 漏洞修复

- **WG-14797** Fixed: Occasional assertion in AkContextualSequencer.cpp when playing XMA in interactive music.
- **WG-15390** Fixed a situation where playing a blend container with multiple children will stop playing if one of its children fails to play.
- **WG-21299** Mac/iOS: GameSimulator docsets are now copied to Xcode documentation folders during installation.
- **WG-21573** Fixed: Stereo delay channel crossfeed results in unstable feedback.
- **WG-21596** Fixed: DRC Surround mode always processes 6 channels, even when the game doesn't support it. Stereo is now used in this case.
- **WG-21599** Fixed: Spread curve is evaluated against total distance instead of distance that is projected on the listener's plane.
- **WG-21603** Fixed: Music context leaks in a very rare scenario.
- **WG-21628** Fixed: XMA decoder starvation with in-memory XMA in interactive music.
- **WG-21638** Fixed: Possible crash when using Mbox/M-Audio when sound card is set with multichannel.
- **WG-21700** Fixed misplaced HUD of IntegrationDemo on iOS6 (armv7s).
- **WG-21709** Fixed: SoundEngine API symbols DLL-exported in StaticCRT configurations.
- **WG-21716** Race condition between AX and audio thread when initializing, possible crash.
- **WG-21736** Fixed: Silent output (NaN) on 32 bit Windows and Mac in rare cases.
- **WG-21741** NaN created in 3D User Defined positioning code, when multiple listeners used, with No Follow Listener. Output is silent.
- **WG-21772** Fixed: crash when trying to resolve Dialogue Event containing no arguments.
- **WG-21786** Fixed an assert when resizing [AkArray](class_ak_array.html "Specific implementation of array") instance to zero.
- **WG-21798** Fixed: Muting of Aux busses using the authoring tool's monitoring features is inconsistent on PS3.
- **WG-21804** Fixed: Custom listener spatialization ignores sources channel count.
- **WG-21816** Fixed a warning in SWIG-generated API: WwiseObjectIDext.cs.
- **WG-21833** Fixed a situation where Soundframe::IGameParameter getGUID returns invalid GUID.
- **WG-21838** Fixed: Fade out is abruptly cut off during music transition while it should continue across next segment inside fading playlist. This is a regression since Wwise 2011.2.
- **WG-21877** iZotope Fixes:
  - 4.0 support added to all plugins on all platforms.
  - Buffering bug fix to the Box Modeler allowing it to be used with the low latency builds of Wwise.
  - Fixing the phase inversion of several distortions: Clip Control, Delicate Harmonics and Smooth Fuzz.
- **WG-21907** Bug Fix: Fixed an issue where opening a Wwise project in 2012.2 results in project migration. The bug occurs if the project is migrated on computer A, then opened on computer B. The problem shows up only in some projects. It is caused by a temporary file left on computer A that was not migrated with the project. A common case where this could happen is when using source control for the Wwise project and updating on a separate computer while having a leftover, non-migrated PROJECT.USERNAME.wsettings file in the project directory.
- **WG-21957** Fixed: Any global stop action on a specific element target which is "missing" will act like a global stop all event, but only on continuous items.
- **WG-21994** Fixed: SoundBanks containing impulse responses for Convolution Reverb on busses are always generated.
- **WG-22240** Fixed crash with rumble on WiiU Controller Pro.
- **WG-22254** Fixed: Android IntegrationDemo resets to main menu and loses all audio when switching the app between foreground and background.
- **WG-22266** In Android IntegrationDemo, sounds are now paused and resumed when user switches the demo between foreground and background.
- **WG-22268** Fixed: Meters on PS3 are insensitive to bus gains.
- **WG-22313** Fixed: Crash while playing sound with corrupt State Groups.
- **WG-22331** Fixed: crash when playing back a specific WAV file in Wwise.
- **WG-22501** Fixed: Positioning-related RTPC may be erroneously applied on nodes that do not define positioning.
- **WG-22505** Fixed: Capture log indicates "Filter" instead of "segment" when a transition is scheduled from anywhere but a music cue.
- **WG-22506** Fixed: Expander initial state behaves as if the input was above threshold instead of below threshold (as silence should be).
- **WG-22726** Fixed: Situation where instance limiters were over limiting when launching multiple times the same sound in the same frame.
- **WG-22793** Fixed: 3D User-Defined sounds with "follow listener" option are not silent when active listener mask on game object is 0.
- **WG-22794** Fixed: Listener scaling factor not taken into account for sounds in 3D User Defined positioning mode.
- **WG-22795** Fixed: Listener spatialization not taken into account for sounds in 3D User Defined positioning mode.
- **WG-22833** Fixed: [CAkDeviceDeferredLinedUp::Init()](namespace_a_k_1_1_comm_a596691b552b507c26b4df958ee1c6de8.html#a596691b552b507c26b4df958ee1c6de8) returns AK\_Success even if IO thread creation fails.
- **WG-22890** Fixed: 3D User-Defined positioning in "no follow" mode is invalid when used with multiple listeners.
- **WG-22939** Fixed: [GetSourcePlayPosition()](namespace_a_k_1_1_sound_engine_ae0b469d9fb8a099b40f52f004882d283.html#ae0b469d9fb8a099b40f52f004882d283) is broken with time stretch effect.