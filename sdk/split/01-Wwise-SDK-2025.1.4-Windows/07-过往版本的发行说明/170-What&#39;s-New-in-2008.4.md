# What&#39;s New in 2008.4

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2008.4

The following sections list and describe the changes made to the Wwise SDK between version 2008.3 and version 2008.4

*Changes that were also provided in patches over 2008.3 are shown in italics.*

# API 变化

- **WG-6970**: Reworked the Low-Level I/O API, specific to the default implementation of the Stream Manager. It is now cross-platform, and some heuristics are passed down to the Low-Level I/O system. Coupled with asynchronous low-level I/O handshaking, it allows for tighter integration with the game regarding I/O. ([Low-Level I/O](streamingmanager_lowlevel.html)). **Note that you may keep your current streaming integration with little effort. See the note in [流播放/流管理器](streamingdevicemanager.html).**
- **WG-12375**: I/O pool attributes were added to the user-defined device settings ([AkDeviceSettings](struct_ak_device_settings.html), in [AkStreamMgrModule.h](_ak_stream_mgr_module_8h.html)).
- **WG-8476**: Added [GetDefaultSettings()](namespace_a_k_1_1_memory_mgr_ada3c244e4c16e6863cec97eef039319b.html#ada3c244e4c16e6863cec97eef039319b "Obtain the default initialization settings for the default implementation of the Memory Manager.") and [GetDefaultDeviceSettings()](namespace_a_k_1_1_stream_mgr_a7d01e09a9bb6b6d34c2bb8f4c8995214.html#a7d01e09a9bb6b6d34c2bb8f4c8995214) to the default Stream Manager's specific definitions. Simplifies initialization of the Stream Manager and I/O system. ([初始化 Streaming Manager](workingwithsdks_initialization.html#initialization_streamingmgr)).
- **WG-8656**: Added one argument to AK::IAkStreamMgr::Create[Std|Auto]: in\_bSyncOpen. When it is false, the Low-Level I/O is allowed to perform an asynchronous file open. This argument is passed (and was added) to [Open()](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_ab6daddd96e109dc7669889733ce4f2cc.html#ab6daddd96e109dc7669889733ce4f2cc) in the Low-Level I/O. ([IAkStreamMgr.h](_i_ak_stream_mgr_8h.html)).
- **WG-8656**: Added error code to the prototype of LocalOutputFunc. LocalOutputFunc is the handler for local ouput. ([AkMonitorError.h](_ak_monitor_error_8h.html)).
- **WG-12103**: Added method [PrepareBank()](namespace_a_k_1_1_sound_engine_a7d92b3c386cd60e76be54ca69f051c09.html#a7d92b3c386cd60e76be54ca69f051c09) on the main API. ([对 SoundBank 做 Prepare 操作](soundengine_banks_loading.html#soundengine_banks_preparingbanks)).
- **WG-10441**: Added argument to AK::MotionEngine::AddPlayerMotionDevice() to support DirectInput-compatible controllers.
- **WG-11949**: Exposed object GUIDs in the SoundFrame.

# 新功能

- **WG-13541**: New Wwise effect plug-in: SoundSeed Impact.
- **WG-12103**: New bank loading scheme: [PrepareBank()](namespace_a_k_1_1_sound_engine_a7d92b3c386cd60e76be54ca69f051c09.html#a7d92b3c386cd60e76be54ca69f051c09). The events/data structures and media of a single soundbank may be loaded separately using this method. ([对 SoundBank 做 Prepare 操作](soundengine_banks_loading.html#soundengine_banks_preparingbanks)).
- **WG-6970**: Reworked the Low-Level I/O API, specific to the default implementation of the Stream Manager. It is now cross-platform, and some heuristics are passed down to the Low-Level I/O system. Coupled with asynchronous low-level I/O handshaking, it allows for tighter integration with the game regarding I/O. ([Low-Level I/O](streamingmanager_lowlevel.html)). The default Stream Manager was reimplemented accordingly.
- **WG-6885**: Streaming: AK\_DEFERRED\_LINED\_UP streaming device now posts many concurrent requests to the Low-Level I/O. ([AkStreamMgrModule.h](_ak_stream_mgr_module_8h.html) and [Low-Level I/O](streamingmanager_lowlevel.html)).
- **WG-8656**: Streaming: Possibility to defer file opening in the Low-Level I/O so that it is executed in the I/O thread. ([Low-Level I/O](streamingmanager_lowlevel.html))
- **WG-12409**: Streaming: New Low-Level I/O implementations for the new Low-Level I/O API. Cleaner, better organization. ([默认底层 I/O 实现](samplecode.html#samplecode_integration_defaultlowlevelio))
- **WG-10996**: New Low-Level I/O sample prototype for streaming from the video RAM on the PS3.
- **WG-13062**: File Packager utility may now generate separate package files for soundbanks and streamed sounds. The File Package Low-Level I/O can now load more than one file package at a time.
- **WG-10441**: Motion: Rumble now works with DirectInput-compatible controllers.

# Behavior and Performance Changes

- **WG-6885**: Streaming optimization: Re-organized and improved default Stream Manager implementation. Most importantly, memory management was improved.
- **WG-6885**: Streaming behavior: AK\_DEFERRED\_LINED\_UP streaming device now posts many concurrent requests to the Low-Level I/O.
- **WG-6764**: Streaming optimization: Loop prefetching, computations for tasks deadline and buffering strategy were improved.
- **WG-11943**: Memory usage optimization: Structural information concerning states in all AudioNodes now use dynamic allocation, saving ~7% total default memory pool size.
- **WG-11954**: Memory usage optimization: Multiple memory saver alignments, saving significant memory in the sound engine.
- **WG-12162**: CPU optimization: Increase number of buckets for lists of CAkIndexable.
- **WG-12262**: Vorbis optimization: share decoded codebooks at run-time.
- **WG-11705**：底层引擎声部管理优化：刚开始播放但尚未从磁盘读取数据的流式声音，在收到停止事件时会立即停止，而不是等待解析头部信息。

# Bug Fixes and Miscellaneous Changes

- **WG-8879**: Installer now adds shortcut to some soundframe samples.
- **WG-13186**: Fixed: PS3: Volume RTPC on output bus doesn't affect center channel.
- **WG-13186**：修复：PS3：仅分配到 LFE 声道（0.1）播放的声音，如果使用 3D 用户定义或 3D 游戏定义的定位，则不会播放。
- **WG-13067**: Fixed: PS3: unsafe DMA transfer in Pitch.
- **WG-13039**: Fixed: Crash in CAkRanSeqCntr::ResetSpecificInfo() when using Game Object scope on a Random or Sequence Container.
- **WG-12953**: Fixed: Custom pre- and post-generation steps are asynchronous.
- **WG-12857**: Fixed: Wii: Noise from Wii remote speaker after returning from Home Menu.
- **WG-12816**: Fixed: PS3: Audio artefacts playing a certain looping sound.
- **WG-12343**: Fixed: Switch container in step mode doesn't use global value when driven by an RTPC through a game parameter.
- **WG-12308**: Fixed: Advanced profiler (Streaming tab) not working properly when 2 or more streaming devices are instantiated.
- **WG-12304**: Fixed: Crash in CAkPath::NextVertex in very specific conditions.
- **WG-12249**: Fixed: Wii: CRASH: OSLockMutex called in DSP voice kicking interrupt handler.
- **WG-12146**: Fixed: Some streamed sounds fail to load with [PrepareEvent()](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238).
- **WG-12224**: Fixed: Low memory: AKASSERT(io\_pContainerInfo != NULL); should be removed and the error should be correctly handled.
- **WG-12222**: Fixed: Low memory: Initialisation error on monitoring is not handled properly.
- **WG-12211**: Fixed: Low memory: Wrong size being read without error when loading busses.
- **WG-11760**: Fixed: Low memory: Crash when decoding XMA, and when initializing the sound engine.
- **WG-12058**: Fixed: Low memory: [LoadBank()](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13) may fail silently.
- **WG-12875**: Fixed: Wii: remote speaker whines for a while if the remote is activated in game.
- **WG-11081**：已修复：即使在"效果器"选项卡中未勾选"覆盖父级"而导致效果器被禁用，效果器上的 RTPC 曲线仍会被推送到音频引擎，并且节点会被放入传输中。
- **WG-13400**: Fixed: Streamed files used multiple times are copied multiple times (Copy Streamed Files).
- **WG-12201**: Fixed: CRASH when updating a project (through perforce) while soundbanks are being generated.
- **WG-12277**: Fixed: Assertion failure (AkMemoryMgrBase.cpp) when connecting to game with empty user-defined positioning.
- **WG-13045**: Fixed: Max block size in the memory profiler is wrong most of the time.
- **WG-12856**: Removed "#include <new>" from public headers.
- **WG-12226**: ASSERT: (m\_ulSizeLeft ==0) when playing streamed vorbis file with 4k granularity.
- **WG-12197**: Fixed: Playback Position returned for streaming files is wrong after loop end.
- **WG-12183**: Fixed: Streaming Profiler does not work properly with 2 devices.
- **WG-11704**：已修复：当存在过渡段落且目标上下文的前导段长度大于该过渡段落的长度时，音乐过渡会从下一个段落而非下一个节拍/小节/网格/提示处开始调度。
- **WG-13479**: Fixed: Ill-behaved fade-in offset in interactive music Playlist transitions.
- **WG-13479**: Fixed: Ill-behaved fade-out offset in interactive music Playlist transitions when fade offset equals fade out duration.
- **WG-13114**: Fixed: When changing state while interactive music is playing and the segment that is currently playing is the last one of a playlist (or if a single segment is playing), state change in actor-mixer is delayed to the end of the segment.
- **WG-12374**: Fixed: Bug in sample-accurate stopping. May cause glitches while playing back interactive music. Platforms: PC, Xbox360, PS3.
- **WG-8218**: Fixed: Glitch at the end of a music segment when it is paused without a fade out, then resumed. The first few frames of the audio clips may be played back again.
- **WG-12205**: Fixed: Inoffensive assert in CAkPendingSwitchTransition::AttachPlayCmd() (in\_iRelativeTime >= -SwitchSyncTime()) while switching interactive music, possible in some scenarios involving many levels of switch containers. The fix results in an optimization of transition scheduling.
- **WG-13501**: Fixed: Wii: Streamed sources not sample-accurate when pitch != 0 or SR != 32 KHz (applies to random-sequence containers only, not music).
- **WG-10924**: Motion: Vibration of Motion FX shouldn't be influenced by Master Audio Bus volume.
- **WG-12346**: Fixed: Potential deadlock when memory pool posts a monitoring notification to signal that there is no memory.
- ***WG-13099**: Fixed: LPF is not computed properly when multiple listeners are used.*
- ***WG-12146**: Fixed: Some streamed sounds fail to load with [PrepareEvent()](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238).*
- ***WG-12134**: Fixed: PS3: Codebook not being decoded properly when an in-memory Vorbis sound does not start at the beginning of the file. This can occur in some scenarios of virtual voices or interactive music. The sound silently fails to play, and random (but aligned) data is sent to the SPU.*
- ***WG-12056**: Fixed: ASSERT (AkList2.h) when loading SoundBanks.*
- ***WG-12050**: Fixed: Wii: Cannot pause vorbis on Wii.*
- ***WG-12010**: Fixed: Assert in AkSegmentChain.cp line 172.*
- ***WG-12011**: Fixed: Assert in CAkMusicSwitchCtx::TryPropagateDelayedSwitchChange.*
- ***WG-12003**: Fixed: Wwise profiler crashes on connect.*
- ***WG-11984**: Fixed: Assert and crash in low memory situations in void \* CAkBankReader::GetData.*
- ***WG-12008**: Fixed: Pause/resume actions with no fade triggered during a fading resume/pause have no effect in interactive music.*
- ***WG-11862**: Fixed: [StopPlayingID()](namespace_a_k_1_1_sound_engine_a362a652b7fb7881e3d036facc173dfa1.html#a362a652b7fb7881e3d036facc173dfa1) takes too much CPU.*
- ***WG-12130**: Fixed: Resume with fade in only works if a Pause with a Fade Out was previously performed.*
- ***WG-12160**: Fixed: RTPC on source plug-ins are broken in Wwise and in game.*
- ***WG-12031**: Fixed: Unhandled low memory situation in [CAkVPLFilterNode::Init()](namespace_a_k_1_1_comm_a596691b552b507c26b4df958ee1c6de8.html#a596691b552b507c26b4df958ee1c6de8).*
- ***WG-12007**: Removed unwanted assert (m\_PBTrans.pvPSTrans) in AkMusicCtx.cpp, line 142.*
- ***WG-11991**: Fixed: Unhandled low-memory situation in CAkAudioMgr::InsertAsPaused and in CAkAudioMgr::TransferToPending.*