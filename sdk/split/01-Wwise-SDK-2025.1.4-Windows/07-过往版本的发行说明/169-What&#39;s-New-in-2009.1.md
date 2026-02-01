# What&#39;s New in 2009.1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2009.1

The following sections list and describe the changes made to the Wwise SDK between version 2008.4 and version 2009.1

*Changes that were also provided in patches over 2008.4 are shown in italics.*

# API 变化

Platform SDKs updates:

- **WG-14405**: Nintendo Wii: Now compiling Wwise using Revolution SDK 3.2.
- **WG-15036**: Nintendo Wii: Now compiling Wwise using RevoEX SDK 2.3.
- **WG-14425**: [Microsoft](namespace_microsoft.html) XDK: Now compiling Wwise using November 2008 version (7978).
- **WG-14427**: Sony SDK: Now compiling Wwise using PS3 SDK 250.001.

Common:

- **WG-7035** SoundEngine API functions that have string parameters now exist in 2 variants, Ansi and Unicode. AkChar and AkTChar were replaced by their native types char\* and wchar\_t\*. AkOSChar type was added and can be useful when working on multiple platforms.
- **WG-7319** (Change #1) [AK::Wwise::ISourceControl::GetOperationList()](class_a_k_1_1_wwise_1_1_i_source_control_ad7820c108e50155039c92223eff718f3.html#ad7820c108e50155039c92223eff718f3) now returns an error code. For more details, see: [创建版本控制插件](source_control_dll.html).
- **WG-7319** (Change #2) AK::Wwise::ISourceControl::UpdateAll() function was removed. For more details, see: [创建版本控制插件](source_control_dll.html).
- **WG-7319** (Change #3) A new function [AK::Wwise::ISourceControl::GetOperationName()](class_a_k_1_1_wwise_1_1_i_source_control_a817835af7fd2e208f9ba202d6eb5a2eb.html#a817835af7fd2e208f9ba202d6eb5a2eb "Gets the operation name to display in user interface") is now required to retrieve the name of a command based on its ID. Some other minor changes were integrated. For more details, see: [创建版本控制插件](source_control_dll.html).
- **WG-12278** [AK::IAkSourcePlugin::GetDuration()](class_a_k_1_1_i_ak_source_plugin_a4c8275d25be4ecd749f826e01eb2146d.html#a4c8275d25be4ecd749f826e01eb2146d) is now returning a AkReal32 value.
- **WG-13318** (Xbox360 only): Now using XAudio2 API. Now required to link against xaudio2.lib and Xmcore.lib.
- **WG-14285** [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13) functions will no longer return AK\_Cancelled if Unload is requested right after it.
- **WG-14299** Added GetPlayingID() to [AK::IAkEffectPluginContext](class_a_k_1_1_i_ak_effect_plugin_context.html) and [AK::IAkSourcePluginContext](class_a_k_1_1_i_ak_source_plugin_context.html).
- **WG-14309** When using Wwise in Command Line mode, users must now use WwiseCLI.exe instead of Wwise.exe. See: [使用命令行](bankscommandline.html).
- **WG-14379** Definition of [AkFileDesc](struct_ak_file_desc.html) was moved from [IAkStreamMgr.h](_i_ak_stream_mgr_8h.html) to [AkStreamMgrModule.h](_ak_stream_mgr_module_8h.html) because it is specific to the default implementation of the Stream Manager (and specific to the definition of the Low-Level IO module), and was not used in the high-level streaming API.
- **WG-14406** Removed #ifdef AK\_OPTIMIZED around the definition of IAkLowLevelIOHook::GetDeviceDesc(). The implementation in release is still expected to be void, but the interface is now consistent between versions.
- **WG-14560** New API AK::SoundEngine::Wii::ConnectCallback. Previous versions of Wwise managed automatically the reconnection of Wiimotes to re-enable the speakers. This cannot be done automatically anymore since KPADSetConnectCallback doesn't stack multiple callbacks. KPADSetConnectCallback or WPADSetConnectCallback must be called by the game and either call AK::SoundEngine::Wii::ConnectCallback in the game's callback or provide directly AK::SoundEngine::Wii::ConnectCallback if the game doesn't need to do anything on Wiimote reconnection. This is valid only if the game uses the Wiimote speakers.

# 新功能

New Features in 2009.1:

- **WG-3415** Now supporting Multi-channel sources when using Vorbis encoding.
- **WG-8545** The command-line application is now without UI, with stdout/stderr output, and with proper return code. See: [使用命令行](bankscommandline.html).
- **WG-12289** Added default value for RTPC. (Available in Wwise application).
- **WG-12996** The Integration demo is now available on PS3.
- **WG-12997** The Integration demo is now available on Wii.
- **WG-13787** New feature allowing to set a memory threshold to start kicking voices when the memory level becomes critical, using priority to kick the lowest priority voice currently playing. See: [AkInitSettings](struct_ak_init_settings.html) and [AkPlatformInitSettings](struct_ak_platform_init_settings.html).
- **WG-13966** Random Sequence containers in Step mode will now default on another element of the playlist if not all of them were loaded.

Introduced in 2008.4 Patch 1

- ***WG-13225**: Added new functionality in the SoundFrame allowing to query original files associated to an Event.*

# Behavior and Performance Changes

behavior changes:

- **WG-3690** The Stream Profiler now trims the beginning of long stream names.
- **WG-4790** FromElapsedTime virtual behavior used with objects of the Interactive Music hierarchy is now sample-accurate. When tracks are streamed, the user-defined look-ahead time is used in order to restart voices without source starvation.
- **WG-13494** Fade-out curves are not reversed anymore in the fade-out parameters of stop and pause events.
- **WG-13134** Music tracks which source clips don't require looping are not considered looping anymore. This results in a huge optimization regarding streaming (the stream manager does not cache the loop start anymore), and in improved audio quality at the end of clips when using windowing compression codecs (no more contribution from the beginning of the sound).
- **WG-13135** (Xbox360 only)XMA sources now sound well with Interactive Music. The XMA decoder introduces a latency of about 384 samples, so the actual audio was delayed compared to the boundaries of audio clips in Music Tracks. This latency is now compensated by the music engine.
- **WG-13787** Memory usage reported by the sound engine is now way more accurate.
- **WG-14609** StartOutputCapture now opens dump file synchronously.
- **WG-14845** SoundSeed Impact 插件：合成的模态数量不再映射为 4 的倍数，以允许使用少量模态进行显著的质量转换。

performance changes:

- **WG-10910** Major performance optimization when using Vorbis compression on Wii.
- **WG-13314** Enhanced Blend Container Performance when using arge number of RTPCs with multiple sounds.
- **WG-14076** Slightly improved memory usage in stream manager.
- **WG-14168** Decreased usage of PPU during low-level bus mixing. For a test case using 8 submix busses (busses with insert effects), the total time spent on the SPU for the Final Mix job, including the DMAs, went from 95us to 80us, and the time spent on the PPU to reset the busses for the next frame went from 45us to 0us.

# Bug Fixes and Miscellaneous Changes

漏洞修复：

- **WG-11747** Fixed race conditions that could cause crash or deadlocks when Loading/Unloading sound banks.
- **WG-13542** ToneGen: Each pink noise instance will have a different shape.
- **WG-13727** Fixed: very short Vorbis sounds ( < 1024 samples ) were not playing.
- **WG-13912** Fixed: Crash when double-clicking a Trigger in the Stinger list.
- **WG-14132** Fixed: Matrix Reverb Web & Dry levels assert when they have RTPC.
- **WG-14185** Fixed: Possible instability issue when the number of custom cues in Segment is larger than 12.
- **WG-14199** Fixed: during volume fades, volume was applied on groups of 2 samples, resulting in a very tiny stair-like envelope. Now volume is applied on each sample separately, resulting in a smoother (although imperceptible) envelope. This fix does not involve any loss of performance.
- **WG-14206** Fixed an issue where Priority rules were not always respected when distances between sounds are very small.
- **WG-14219** (Fix #1) Fixed: Stream manager does not clean streams when [IAkFileLocationResolver::Open()](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_ab6daddd96e109dc7669889733ce4f2cc.html#ab6daddd96e109dc7669889733ce4f2cc) fails while monitoring.
- **WG-14219** (Fix #2) Fixed: [IAkLowLevelIOHook::Close()](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_ab204d963f6b81abc102a6d6b8272b591.html#ab204d963f6b81abc102a6d6b8272b591) is called on a file handle that was never opened when stream creation fails because of insufficient memory.
- **WG-14224** Fixed: Random unused bytes in converted XMA files causing files to be sometime different at each compilation.
- **WG-14225** Fixed: Memory allocation made with AK::MemoryMgr::CreatePool won't work with some alignment settings.
- **WG-14239** Fixed a bug where the Capture log would erroneously display "Codec plug-in not registered: Vorbis " even while no vorbis sound are being processed.
- **WG-14396** Fixed: Possible crash when loading simultaneously two banks containing the same source with two different prefetch size.
- **WG-14413** Fixed: Sample implementations of IAkFileLocationResolver::Open return AK\_Fail even if AkFileHelpers::OpenFile() returns AK\_FileNotFound. Valid return values are AK\_Success, AK\_Fail, and AK\_FileNotFound. In the latter case, the default implementation of the Stream Manager posts a "File Not Found" monitoring message instead of the vague "Cannot Open File" message.
- **WG-14434** Fixed: CrossFade transitions on vorbis sounds that are looping may not occur at the right moment.
- **WG-14552** Fixed a dangerous locking issue when calling [AK::SoundEngine::CancelBankCallbackCookie](namespace_a_k_1_1_sound_engine_a544917bc88d215224272a59e70d8578c.html#a544917bc88d215224272a59e70d8578c).
- **WG-14553** Fixed a situation where a call to [ExecuteActionOnEvent( )](namespace_a_k_1_1_sound_engine_ac55e3d6ac464b0579a8487c88a755d8c.html#ac55e3d6ac464b0579a8487c88a755d8c) would be void because an invalid game object was passed in parameters and the user was not informed of the situation in the profiler.
- **WG-14613** Fixed: Possible crash when using Sequence transitions with delay of 0 seconds.
- **WG-14679** Fixed an issue where palying infinitely looping segment of size 0 would freeze the sound engine. Now printing an error message instead.
- **WG-14712** Fixed: possible noise in right channel of ADPCM stereo file on PS3.
- **WG-14716** Now possible to query GetRTPCValue to allow returning the value of global objects.
- **WG-14730** Fixed: Crash in the music engine in low-memory conditions.
- **WG-14735** Fixed: (Wii only) Sync loss between behavioral/music and lower engines when computation of an audio frame is slower than an AX frame.
- **WG-14757** Fixed: (Windows only) Fixed a situation where the sound engine would lock the entire Directsound output buffer on write.
- **WG-14808** Fixed: (PC, Xbox 360 and Playstation3): Source starvation notifications can be skipped when zero-latency streamed source start. This can happen when the prefeteched data only consists of the header (that is, using very small values of prefetching).
- **WG-14815** Fixed a bug where actions scoped with exceptions would sometime not work when sounds are overriding parents.
- **WG-14933** Fixed: Idle wait time feature of streaming devices (when AkDeviceSettings::uIdleWaitTime is not AK\_INFINITE) is broken on the PS3, and may potentially cause crashes on the Wii with AK\_SCHEDULER\_DEFERRED\_LINED\_UP devices.

Misc:

- **WG-13318** (Xbox360 only): Now using XAudio2 API.
- **WG-13345** Removed unused include of <windows.h> in AkTypes.h.
- **WG-14240** Updated Vorbis encoder to use the aoTuV-b5.61 release; noticeable audio quality gains at low bitrates.
- **WG-14340** Don't allow anymore wwise.exe to generate bank from command line. User should always be using WwiseCLI.exe. See: [使用命令行](bankscommandline.html)
- **WG-14306** Old Reverb/Lite effects need to be flagged as 'deprecated'. New projects should be using Matrix Reverb or RoomVerb instead.
- **WG-11327** Fixed: Make I/O errors in profiler more complete, including missing file path.

Introduced in 2008.4 Patch 1

- ***WG-13829**: Infinite loop in CAkEvent::QueryAudioObjectIDs if the action type is not "play".*
- ***WG-13846**: NOP asserts in sound engine/SDK samples.*
- ***WG-13979**: PS3: Fixed an issue where the soundEngine would fail to initialize if another system did initialize audio first.*

Introduced in 2008.4 Patch 2

- ***WG-14477**: (Wii only) In-memory PCM and ADPCM sounds that have a looping region which does not start at the beginning produce Voice Starvation notifications, are killed and reacquired at each frame.*
- ***WG-14478**: Vorbis from File can stop playing before the end.*
- ***WG-14494**: Assert in Stream Manager (AkDeviceBase.cpp line 1378), which can occur while streaming audio files (automatic streams)and loading soundbanks at the same time (standard streams). This assert could have been ignored safely.*
- ***WG-14495**: Crash when loading a bank while trying to play a MotionFX.*
- ***WG-14496**: Rumble keeps playing on Xbox360.*
- ***WG-14531**: (Wii only) OSReport() called from WiimoteMgr and RumbleBus in Release.*

Introduced in 2008.4 Patch 3

- ***WG-14618** Fixed: Crash when terminating the sound engine with a pending action on a seq/rnd container.*
- ***WG-14625** Fixed: Deadlock in Stream manager Standard Streams counter (Win32 + Xbox 360 only). This can result in having the IO thread constantly awaken even if there is no pending standard stream operation, thus flooding the low-level IO with automatic stream requests above their target buffer length*
- ***WG-14680** Fixed: (Wii only). Source starvation notifications can be skipped when zero-latency streamed source start. This can happen when the prefeteched data only consists of the header (that is, using very small values of prefetching).*
- ***WG-14680** Fixed: (Wii only). Possible click with zero-latency streamed PCM sources when the prefeteched data contains only the header (that is, using very small values of prefetching).*
- ***WG-14742** (Wii only) Stereo PCM and ADPCM streamed sources now become silent when source (I/O) starvation occurs (instead of looping the same buffer).*
- ***WG-14851** Fixed: Inoffensive assert in AkMusicSwitchCtx.cpp (in\_iRelativeTime==0), and possibly wrong fade-in times in music transitions that use a transition segment.*
- ***WG-14839** Fixed: Alignment error on file package header read from disk (may be problematic on the Wii). The sample samples/SoundEngine/Common/AkFilePackageLowLevelIO.inl was updated.*