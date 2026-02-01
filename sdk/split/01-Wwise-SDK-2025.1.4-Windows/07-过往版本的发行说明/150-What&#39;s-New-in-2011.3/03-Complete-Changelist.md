# Complete Changelist

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Complete Changelist

The following sections list and describe the changes made to Wwise between version 2011.2.X and version 2011.3.

# New platforms supported

- Android
- WiiU™
- PlayStation®Vita

# 平台 SDK 更新

- Xbox 360: updated to XDK 20871 (August 2011).
- PS3: updated to SDK 370
- VITA: updated to SDK 1.03
- iOS: updated to iOS 5.0 (apple llvm compiler 3.0)
- MAC: using apple llvm compiler 3.0
- 3DS: updated to CTR-SDK 2.4.0

# 新功能

- **WG-19991** Music custom cues now notified in the Wwise profiler.
- **WG-19898** Improved notifications of stingers and music transitions.
- **WG-19870** Added the Wwise Gain plug-in.
- **WG-19867** The Tone generator plug-in can now optionally output directly in the LFE channel, allowing simple LFE generation."
- **WG-19836**
- New command-line operation -SoundFrameServer starts WwiseCLI in Sound Frame server mode, so that Sound Frame clients can extract project information without requiring user intervention.
- Now possible to specify the process ID of both Sound Frame Client and Server, for scenarios where multiple instances of both can be present at once on the same PC.
- New Built-In Macro 'WwiseExeProcessID' in SoundBank generation steps enables Sound Frame use from custom steps.
- **WG-19494** Music notifications | Pass Cue name (description) in Music Cue callback.
- **WG-19245** Wwise Authoring crashes can now be reported to Audiokinetic via the Error Reporter
- **WG-19232** New fast API Query function - Retrieve PlayingID from Object. See [AK::SoundEngine::Query::GetPlayingIDsFromGameObject](namespace_a_k_1_1_sound_engine_1_1_query_a8263cb018517fadf2220ca00d88f907f.html#a8263cb018517fadf2220ca00d88f907f)
- **WG-19231** New fast API Query function - Retrieve Object from PlayingID. See [AK::SoundEngine::Query::GetGameObjectFromPlayingID](namespace_a_k_1_1_sound_engine_1_1_query_aef86db60a23116c39e1728b1e633e379.html#aef86db60a23116c39e1728b1e633e379)
- **WG-19230** New fast API Query function - Retrieve EventID from PlayingID. See [AK::SoundEngine::Query::GetEventIDFromPlayingID](namespace_a_k_1_1_sound_engine_1_1_query_a1c53c91b9b54140ac48977ee25ae6387.html#a1c53c91b9b54140ac48977ee25ae6387)
- **WG-18843** Several new interactive music features. [Music Clips - Fades and Automation](whatsnew_2011_3_new_features.html#whatsnew_2011_3_music_fade_automation)
- **WG-17792** Now possible to query from the soundframe if an Event (or a Dialogue Event) has Voice/Language specific Content. See AK::SoundFrame::ISoundFrame::EventHasVoiceContent and AK::SoundFrame::ISoundFrame::DialogueEventHasVoiceContent
- **WG-17539** Now possible to include Dialogue Events in a SoundBank Definition File using the new '-DialogueEvent' command.
- **WG-6432** Transition segments in transition rules do not force the destination to start at the entry cue. For example, it is now possible to perform a "Same Time as Playing Segment" between two music objects, and insert a transition segment in between.

# API 变化

- **WG-20192** Removed [Init()](namespace_a_k_1_1_comm_a596691b552b507c26b4df958ee1c6de8.html#a596691b552b507c26b4df958ee1c6de8) from [AkListBare](class_ak_list_bare.html "Implementation of List Bare.").
- **WG-19966** Added new overload of AK::MultiCoreServices::DspProcess::SetDspProcess supporting the jobbin2 job type.
- **WG-19836** New method ISoundFrame::Connect must be called for the Sound Frame client to attempt connection (this used to be automatically done inside AK::SoundFrame::Create).

# Behavior and Performance Changes

- **WG-20125** New option to log errors returned in custom pre/post bank building steps. When severity is set to "fatal error", the bank building process will not complete when an error is detected.
- **WG-20029** Double-clicking on target object in Event Editor now inspects it.
- **WG-19945** Music switch transition behavior more consistent with option "Continue To Play On Switch Change".
- **WG-19931** The advanced setting "On return from physical voice" default value changed from "Restart from beginning" to "Play from elapsed time".
- **WG-19890** When performing a "Same Time as Playing Segment" music switch transition, the effective position of the destination is wrapped around its duration. For example, if segment A is twice as long as segment B, and you switch from 75% of segment A, destination position will be 50% of segment B.
- **WG-19861** Remove LFE separate control from Wwise. The LFE management has been enhanced. LFE separate control was removed and is now considered as a normal channel like all others. From now on, the LFE volume is now entirely bound to the Generic Volume property. Separate control of the LFE will now be possible using the Wwise Gain Effect. All controls driving the LFE will be lost during the migration.

  That change will fix a large number of known issues and is making the volume behavior more easily predictable for all users.
- **WG-19841** Rendered effects processing is now multi-threaded. Playback of converted files in Wwise now uses the rendered effect instead of the real-time effect.
- **WG-18010** Improved music switch transition cancellation.
- **WG-18009** Improved music switch transition cutoff mechanism: when any kind of music switch transition occurs, the following segments of the exiting playlist are not heard, or are faded out right away.
- **WG-20027** Connecting to a profiling session file is now much faster.
- **WG-19619** Fixed: Switch container memory usage is not scaling well with many switch values.

# Miscellaneous Changes

- **WG-20131** StopPlayingID, StopAll and ExecuteActionOnEvent API calls are now reported in capture log.
- **WG-20066** The "char" version of [AK::Monitor::PostString()](namespace_a_k_1_1_monitor_ab6c0af10be91ee196c480081cddc38ab.html#ab6c0af10be91ee196c480081cddc38ab) now interprets it as an UTF8 string.
- **WG-19826** Added Visual Studio 2010 SoundFrame sample projects in SDK.
- **WG-18646** Migration Note: Property Value for non-unlink properties are now saved in an XML attribute instead of a XML element.

# 漏洞修复

- **WG-20265** Fixed: Meter UI refresh rate was slow in Wwise UI in low activity conditions.
- **WG-20198** Fixed: A stream may not start playing if only one stream buffer is ready even though there is enough data in that buffer for prebuffering.
- **WG-20195** Fixed: Stack overflow in music engine (CAkTimeSequencedItem::GetNextBucket()) in some circumstances.
- **WG-20189** Fixed: Package Low Level IO doesn't support external sources with file IDs
- **WG-20181** Fixed: Stream leaks when running out of Stream Manager pool memory while allocating data for low-level deferred open.
- **WG-20173** Fixed: Wwise UI sometime freezes when connected to the game and capturing in a very specific condition.
- **WG-20167** Fixed: A state change may be delayed indefinitely by a music object that is paused if this object or its ancestors or descendants listen to it with a "Sync To" that is not "Immediate". Likewise, when a state change is delayed by a music object, and this object is then paused, the state change is delayed until the object resumes or stops. The state should change as soon as the music object is paused.
- **WG-20161** Fixed: McDSP Futzbox is not applied on previous effects' tails when used in a bus on the PS3.
- **WG-20103** Fixed: A global "Resume All" action can erroneously pause a parameter transition.
- **WG-20100** Fixed: Problem when using PrepareGameSync mode and two or more events are pointing to the same switch container and are prepared at the same time.
- **WG-20093** Fixed: McDSP Futzbox clicks at the end of sounds with some settings.
- **WG-20037** Fixed: Game Parameters on the Control Busses do not appear in the Init.txt
- **WG-20034** Fixed: Crash in CAkDeviceBlocking::ExecuteTask() when running out of memory in the small object Stream Manager pool while an I/O transfer is occurring.
- **WG-20025** Fixed: Possible crash when mixing multiple layers of Continuous Random containers interleaved with blend containers with multiple children.
- **WG-20022** Fixed: Shift-click in capture log jumps to random position.
- **WG-20018** Fixed: Step Switch container under a blend container will prevent some sounds to play if no sound is assigned to the current switch at the moment of the playback.
- **WG-20002** Fixed: PrepareEvent calls the wrong Free hook in the release build when releasing prepared media.
- **WG-19974** Fixed: Transitions added or removed from a music object's transition list may be ignored at run-time.
- **WG-19965** Xbox 360: corrected buffer management in XAudio2 output voice.
- **WG-19961** Fixed: Assert if soundbank name is larger than 64 characters
- **WG-19957** PS3: Freeze when shutting down during init
- **WG-19930** Fixed: ExecuteAction on event of type "Break" were not breaking sounds.
- **WG-19929** Fixed: Dynamic dialogue callbacks have the eventID equal to the playingID
- **WG-19892** Fixed: Synchronization point music notification (AK\_MusicSyncPoint) not notified when reaching sync point of "nothing"
- **WG-19889** Fixed: Stinger pre-entry does not play.
- **WG-19871** Fixed: Sound engine init crash when failing to allocate resources.
- **WG-19866** Fixed: Unloading bank containing Convolution IR on a playing Environmental FX is not returning immediately.
- **WG-19864** Fixed: SetVolume actions on the wii/3DS on master bus may not work if no sound is playing.
- **WG-19855** Fixed: Possible crash in low memory conditions when seeking XMA Files.
- **WG-19854** Fixed: Audio is sent to wrong environment when using multiple sounds on multiple environments on PS3
- **WG-19852** Fixed: PS3: memory access out of bounds in MixN job
- **WG-19847** Fixed: Possible crash in interactive music when a transition segment was not loaded when required. Fixed: Inconsistent volume on transition segments when the segment was in a separate music hierarchy.
- **WG-19843** Fixed: Possible memory overrun when calling [QueryAudioObjectIDs()](namespace_a_k_1_1_sound_engine_1_1_query_ad760c9a7f1596231d185d8ee931231f4.html#ad760c9a7f1596231d185d8ee931231f4).
- **WG-19828** Fixed: Event Prepared messages in profiler log were set too early in the process.
- **WG-19823** Fixed: When a property fades is interrupted by a pause action, it may take a lot of time to restart after it is resumed.
- **WG-19821** Fixed: Inoffensive ASSERT in interactive music while changing state after having paused during a transition that uses a fade out in some circumstances.
- **WG-19816** Fixed: Pausing interactive music does not pause fading transitions.
- **WG-19814** Fixed: Pausing interactive music on Wii and 3DS causes loss of synchronization.
- **WG-19776** Fixed: Loss of audio when connecting headphones.
- **WG-19765** Fixed: Wwise Connect history was always displaying 3DS as not available even when it was available.
- **WG-19752** Fixed: McDSP effects can use wrong sample rate when rendering multiple effects from multiple threads.
- **WG-19734** Fixed: Streamed interactive music audio clips coming back from virtual voice may produce a click.
- **WG-19683** Fixed: Issue where random containers containing less sounds in some languages would fire blank on these non localized sounds instead of playing them.
- **WG-19425** Fixed: Abrupt LPF changes while sounds are virtual are sometimes causing small glitches when returning to physical voices.
- **WG-19346** Fixed: A situation where Wwise command line tool would still try to generate banks after an error occurred during the import definition file process.
- **WG-19333** Fixed: Matrix Reverb doesn't work on NGP (real fix)
- **WG-19332** Fixed: Occasional deadlock while loading soundbank on Xbox 360
- **WG-19114** Fixed: Default RTPC Value change were ignored when remotely connected to a game.
- **WG-19096** Fixed: Playing new sound in Wwise may reset in-progress state transition.
- **WG-18878** Fixed: The transition segment has Invalid properties when its parent is an unreferenced playlist
- **WG-18465** Fixed: 0.1 (LFE) sounds were erroneously mixed down to the Mono channel when generating banks on platforms that do not support LFE.
- **WG-17863** Fixed: Inoffensive assert and bad random behavior with "Standard" Random Step groups in interactive music playlists in some circumstances.
- **WG-16142** Fixed: Now displaying Default values of the RTPC value in the GameSync Monotor if none was set.
- **WG-15250** Fixed: On Wii, possible glitch when pausing a music segment
- **WG-9959** Fixed: A problem where when a bank passes from the localized bank folder to the SFX root folder, the obsolete bank in the localized folder was still being used by error. Now the obsolete bank is automatically deleted to avoid confusion.
- **WG-20072** Fixed: 3DS Effects not registered by AllPlugin helpers Bug Fix Added 3DS effects to [AllPluginsRegistrationHelpers.h](_all_plugins_registration_helpers_8h.html) and AllPluginFactories.h
- **WG-19858** Fixed: Possible crash with continuous switch container when game object is unregistered when playing silent switch.
- **WG-19850** Fixed: Moving the entry cue of a segment now moves the whole content of the segment. Hold the CTRL key to move freely the Entry Cue without moving the segment's content.
- **WG-19837** Fixed: "Too many segments" notification posted when there are 64 segments playing or scheduled concurrently in a playlist, instead of when there are 64 segments scheduled concurrently in the same audio frame.