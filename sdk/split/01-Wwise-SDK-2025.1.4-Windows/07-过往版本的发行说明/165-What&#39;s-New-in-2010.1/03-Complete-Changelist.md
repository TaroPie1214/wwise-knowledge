# Complete Changelist

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Complete Changelist

The following sections list and describe the changes made to Wwise between version 2009.3 and version 2010.1

# SDK Folder Structure Changes

- **WG-16874**: XBox360 version now only supports VC9 (Visual Studio 2008), VC8 was deprecated in the last version of the [Microsoft](namespace_microsoft.html) XDK. The libraries in \SDK\XBox360\ are not distributed anymore. You must now be using \SDK\XBox360\_vc90\.

# 平台 SDK 更新

- **WG-16339**: (Wii) Sound engine now compiled using Wii Revolution SDK 3.3.
- **WG-16874**: (Xbox360) Sound engine now compiled using [Microsoft](namespace_microsoft.html) XDK February 2010 (11164).
- **WG-16878**: (PS3) Sound engine now compiled using SDK 320.( Also in 2009.3 patch 4 )

# API 变化

- **WG-11112**: Two new functions/notifications now required to be implemented in the Sound Frame IClient: AK::SoundFrame::IClient::OnDialogueEventNotif() and AK::SoundFrame::IClient::OnArgumentsNotif().
- **WG-15264**: The source control plug-in interface slightly changed in 2010.1. See changes in [AK::Wwise::ISourceControl::DoOperation](class_a_k_1_1_wwise_1_1_i_source_control_a36789a297bc4a85ba0fffb9de9bc0a6f.html#a36789a297bc4a85ba0fffb9de9bc0a6f) for latest interface.
- **WG-16163**: [AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e) now has new optional parameters to support the new "External Source" feature. See: [集成 External Source](integrating_external_sources.html)
- **WG-16671**: FNVHash::Compute now generates an incremental hash if the same instance of the class is reused across Compute calls.
- **WG-16678**: Changed Low-Level I/O structure AkTransferInfo. AkTransferInfo::uRequestedSize used to represent the buffer size and did not take the end of files into account. This was causing confusion. Henceforth, a new field, AkTransferInfo::uBufferSize, represents the buffer size, and AkTransferInfo::uRequestedSize now represents the exact amount of requested bytes for this transfer. This may have an impact on your implementation of the low-level I/O hook.
- **WG-16706**: Multiple changes regarding the Wwise plug-in interfaces. Some of these changes are for future support of large data section which are not completely exposed to the Plug-in SDK yet. Some functions will have to be added to your project with a void implementation for the moment to compile properly.
  - All existing plug-ins for Wwise should be recompiled with the latest Wwise SDK prior using them in Wwise 2010.1.
  - The new function `AK::Wwise::IAudioPlugin::SetPluginObjectMedia` (...) should be implemented to void by any plug-in that doesn't use the plug-in large media system.
  - Any plug-in implementing the `AK::Wwise::IAudioPlugin` interface must implement the function `AK::Wwise::IAudioPlugin::GetPluginMediaConverterInterface` (...). Simply return NULL, this is not accessible from plug-ins at the moments.
- **WG-16721**: API changed to allow External Sources to work with dynamic sequence objects. See: [AK::SoundEngine::DynamicSequence::PlaylistItem](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_item.html)

# 新功能

- **WG-16321**: New Mixing Desk view in Wwise authoring application (Ctrl+Shift+M in Wwise application, See help for more info.).
- **WG-16465**: Conversion Settings can be stored in ShareSet objects and re-used across the Project. Conversion Settings now also leverage the override mechanism, so Conversion Settings can be set to high-level objects in Wwise to generalize the usage. Be sure to take a look at the [video tutorial](https://www.audiokinetic.com/learn/videos/sjza1chtcek/).
- **WG-15821**: External Sources. See integration details in: [集成 External Source](integrating_external_sources.html) for integration information.
- **WG-14502**: Now allowing Sub-mixing Master-Mixer hierarchy allowing pipelining multiple layers of effects in the busses.
- **WG-11833**: New SoundBank Setting Options: List the maximum radius of any attenuation that plays on an event.
- **WG-15264**: The File Manager has now the ability to move and rename audio source files using the Source Control plug-ins. The Source Control plug-in interface has changed.
- **WG-16221**: New sample code to playback microphone output on the XBox360 in the sample "IntegrationDemo".
- **WG-14442**: Now possible to copy custom states from 1 state to another by using the "Sync Custom States" functionality.
- **WG-9505**: Wwise does now support copy/pasting RTPC curves across objects in Wwise.
- **WG-11112**: Dialogue events now supported in the Sound Frame. 2 new notifications to be implemented in the Sound Frame IClient: OnDialogueEventNotif() and OnArgumentsNotif().
- **WG-10870**: New feature: Seek actions, allow you to seek within a playing sound, or to start a sound at a specific (or random) offset. See: [AK::SoundEngine::SeekOnEvent](namespace_a_k_1_1_sound_engine_a33010f3ba82a8838bb2f4283ee2ee9d7.html#a33010f3ba82a8838bb2f4283ee2ee9d7)
- **WG-17183**: Added "Number Of Active Events" to performance counters in Wwise Profiler.
- **WG-15048**: Now possible to use user specific location for imported /.cache directory.
- **WG-2830**: New keyboard shortcut (Alt + Up Arrow) and menu item (Edit > Navigate to Parent) to edit the parent of the object that is currently being edited.

# Behavior and Performance Changes

- **WG-17071**: Streamed playback instances have smaller memory footprint, less code and are generally more efficient.
- **WG-16894**: Minor performance optimizations to resampling/pitch and low pass filtering in the pipeline on the XBox360.
- **WG-15880**: Improved performance of RTPC changes when many game parameters are present.
- **WG-17092**: Streamed XMA virtual voices FromElapsedTime now consume less CPU.
- **WG-16141**: Fixed: Streamed audio sources in music tracks require that they have streamed their first buffer in before their memory can be released after having stopped.
- **WG-16347**: I/O usage improvement: Streamed sources were tweaked so that they don't start playing immediately after reading the first streaming buffer, but instead wait until their "target buffering" is met. This allows you to use smaller IO buffering values (AkDeviceSettings::fTargetBufferLength), thus resulting in smaller IO pool usage, because you will be less likely to run the risk of provoking source starvations at the beginning of sounds. This is especially true with small streaming granularities ([AkDeviceSettings::uGranularity](struct_ak_device_settings_abd4879bfd150b9a2f898102e3815dbe2.html#abd4879bfd150b9a2f898102e3815dbe2 "I/O requests granularity (typical bytes/request).")). Before this improvement, streamed sources were more likely to starve during the first buffer.
- **WG-15951**: Insert effects in the actor-mixer hierarchy now 'stay alive' for the duration of the sample-accurate stitching. This means that the tail is not part of the sample-accurate stitch, so that it actually sounds like what you would want when you put a tail effect on it.
- **WG-16271**: "Don't play stinger again for X seconds" property of stingers is now exclusive. This means that when set to 0 (default), the same stinger will never be scheduled at exactly the same time as another stinger (from same Trigger).
- **WG-16272**: "Don't play stinger again for X seconds" property of stingers is now relative to the trigger's synchronization point, instead of the time when the Trigger is posted. The former behavior was misleading and hard to control.
- **WG-16963**: (Wii only) Changed: Vorbis voices used to fail playing when their "under volume threshold" behavior was set to "Continue To Play" and they had no seek table. Now, they are able to play. However, if their voice gets kicked by the hardware (because the maximum voice count reaches 96 or DSP usage reaches 100%), they will fail restarting when the hardware re-assigns them a voice.
- **WG-16927**: Default gain when using Audio Input plug-in with the function CreateAudioInputSource is now 0db, instead of -12 dB.
- **WG-16707**: Fixed: global RTPC values are pushed to game when connecting with Wwise.

# Bug Fixes and Miscellaneous Changes

- **WG-17410**: Fixed: Sometimes, game objects are not displayed in the Game Object column of the Capture Log of the Wwise profiler. When this happens, and if the Wwise Object Column drop menu is set to "Wwise Object Name", the Wwise object name is not displayed either.
- **WG-17140**: Fixed: Vorbis decoder state not properly reset after seeking in a Vorbis source after it had already started playing. The difference was usually inaudible.
- **WG-16998**: Fixed: Multichannel (more than 2.0) PCM and ADPCM can have their channels swapped after having been virtual FromElapsedTime.
- **WG-16765**: Fixed: Off-by-one error in sample count within loop regions. Very benign on all platforms, except on the Wii where it can have unexpected behavior when seeking (using [SeekOnEvent()](namespace_a_k_1_1_sound_engine_a33010f3ba82a8838bb2f4283ee2ee9d7.html#a33010f3ba82a8838bb2f4283ee2ee9d7)) exactly on a loop end boundary.
- **WG-16362**: Crash in multichannel PCM file sources occurring with a very specific combination of file length and streaming granularity.
- **WG-16854**: Fixed: Markers are inconsistent after streamed PCM and ADPCM sources have been virtual FromElapsedTime.
- **WG-16853**: Fixed: Streamed ADPCM push inconsistent marker notifications after being virtual (PS3 only).
- **WG-16749**: Fixed: possible glitch and false source starvation notification after seeking a streamed Vorbis sound on the Wii.
- **WG-16750**: Fixed: ASSERT in AkSrcFilePCMEx when seeking exactly on loop end boundary. Can happen in the authoring tool only.
- **WG-16753**: Fixed: (Wii only) Streamed PCM and ADPCM that have a looping region may starve immediately after seeking after the loop end.
- **WG-16500**: Actual prefetch length in zero-latency Vorbis streams is now much closer to the requested duration.
- **WG-17052**: Fixed: (Wii only) Vorbis "From Elapsed Time" virtual mode does not count time properly when virtual if the sound has a sample rate different than 32 KHz or a pitch different than 0.
- **WG-16189**: Fixed: [AKPLATFORM::SafeStrCpy](namespace_a_k_p_l_a_t_f_o_r_m_aebd4566f4b4cc51c94ab69c3272b5991.html#aebd4566f4b4cc51c94ab69c3272b5991 "Safe unicode string copy.") and SafeStrCat are not safe.
- **WG-16507**: Fixed: [AK::IAkStreamMgr::CreateStd](class_a_k_1_1_i_ak_stream_mgr_a1de2a7935a2d3cddb71e7cc7f48effd6.html#a1de2a7935a2d3cddb71e7cc7f48effd6)/CreateAuto() could set a value to the returned out\_pStream pointer if the function did not return AK\_Success (caused by insufficient memory). This resulted in an inoffensive assert in the sound engine.
- **WG-14182**: The Perforce client now supports Perforce servers in Unicode mode.
- **WG-15925**: Fixed: Attenuation curve editing while connected is not always applied in game.
- **WG-14197**: Wwise and WwiseCLI can now support relative paths to Wwise projects.
- **WG-17215**: Fixed: Conversion fails on some files when "Insert Filename Marker" is enabled.
- **WG-17162**: Fixed a rare crash that can occur when Shutting down the Communication engine at the same time Wwise application is trying to connect on the game remotely.
- **WG-17085**: Fixed playback of original WAV files created in WaveLab 6.0
- **WG-17075**: Stability issue fixed when playing Sequence Container containing 1 item.
- **WG-17068**: Fixed an issue where multi channel sounds down mixed to stereo using the Stereo\_drop conversion would possibly add a glitch at the end of the sound.
- **WG-17033**: Fixed: Bad markers notified from PCM and ADPCM streamed sources after having been virtual FromBeginning.
- **WG-17006**: Minor audio inconsistencies between XBox360 and other platforms for SoundSeed Air and McDSP FutzBox plug-ins.
- **WG-16931**: Fixed issues when launching Wwise with a project path that contains relative elements. Perforce integration was not working correctly.
- **WG-16929**: Fixed: source starvation with high-bitrate vorbis in-bank media on PS3
- **WG-16871**: Fixed: Blocking [AK::IAkAutoStream::GetBuffer()](class_a_k_1_1_i_ak_auto_stream_aa8197d63b8e758acb075a437103e573c.html#aa8197d63b8e758acb075a437103e573c) may return before I/O is actually completed. This has no incidence on the sound engine or on your title unless you explicitly use blocking [AK::IAkAutoStream::GetBuffer()](class_a_k_1_1_i_ak_auto_stream_aa8197d63b8e758acb075a437103e573c.html#aa8197d63b8e758acb075a437103e573c).
- **WG-16828**: Background Music Bus property is now correctly shown for the PS3 platform in the Master-Mixer Console and Multi Editor.
- **WG-16768**: Possible crash fixed when opening Music Segments after switching from Wwise 32bit to Wwise 64bit (or vice versa). akpk files were containing 32/64 bit dependent information.
- **WG-16719**: The switch ordering in the Music Switch Container association editor is now the same as the one found in the normal Switch Container.
- **WG-16628**: Fixed: MP3 file with multiple ID3V2 tags fails to play.
- **WG-16624**: Wwise does not allow anymore Music Segments to select themselves as stingers.
- **WG-16443**: Fixed a problem when adding watched from the Game Object Explorer's game object tab.
- **WG-16386**: Fixed: Streamed files using prefetch are not included in SoundBanksInfo.xml when the Original source file is absent.
- **WG-16104**: Fixed: live editing of bus ducking did not work in all cases.
- **WG-15813**: Fixed: SoundBank inclusion is sometimes wrongly excluding media from sounds that are duplicated then excluded in one of the path.
- **WG-17289**: Fixed: Custom multichannel (> stereo) plugins crash on the Wii. They now fail gracefully.
- **WG-17017**：以下工厂查询已从新工程中移除，且不再支持现有工程： 音频源 - 采样率 = 48000 音频源 - 转换后的声道 = 单声道 音频源 - 转换后的声道 = 立体声 音频源 - 转换后的声道 = 多于立体声 音频源 - 转换后包含 LFE
- **WG-16713**: Added a "Data Size" column in soundbanks' TXT file for the "In Memory Audio" section (size is in bytes) + Now listing every instance of source plug-ins under the "Source plug-ins" section.
- **WG-16898**: In soundbanks' TXT files, under the Source plug-ins sections, the columns are now: ID, Name, Plug-in type, [empty], Path to the Sound, Notes.
- **WG-17091**: Fixed: AkVorbisDecoder.lib symbols clash with standard vorbis distribution
- **WG-16275**: The version of subversion was updated from 1.5.2 to 1.6.6.
- **WG-16891**: (PS3)Fixed: Not all SPURS jobs are compiled with the flags -mspurs-job.
- **WG-15597**: Fixed: Can't load a project from the command line if the path is relative.
- **WG-16224**: Fixed: Possible PlayingID Conflict when calling [AK::SoundEngine::PostEvent()](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e) from two different threads.
- **WG-17351**: Fixed: Working with switch containers with large number of children can slow down the Wwise application.
- **WG-16741**: Fixed: File Manager work-unit tab shows missing wav files - Perforce.
- **WG-16737**: Fixed: Crash in Profiler statistics view in very specific situation.
- **WG-16848**: Fixed: Crash when xbox conversion plugins are not installed an editing Xbox360 conversion settings.
- **WG-16236**: Fixed: Undo is not working when deleting a column in the dynamic dialogue editor.
- **WG-16810**: Multi-edit now support setting values smaller than 0.1.
- **WG-16611**: Fixed: Wwise Crashes when browsing for a collapsing list in Event Editor
- **WG-17330**: Fixed: Stability issue fixed in Integrity Report with folders under audio objects.
- **WG-17376**: Misc change: McDSP Company ID changed from 66 to 256 to conform to existing Wwise plugin standards.

Introduced in 2009.3 Patch 4:

Platform SDK Update:

- **WG-17335**: All PS3 binaries were built with PS3 SDK 320.001 and included in this package.

Authoring:

- **WG-16939**: Fixed: False "Media not found in any SoundBank" error while generating soundbanks in some cases.
- **WG-17353**: Fixed: Generated .bnk files were not always identical even with the exact same project and authoring application (Note: Soundbanks generated with a 32-bit application may still be different from those generated with a 64-bit application - that's a different issue)

Sound Engine:

- **WG-16865**: Fixed an issue where absolute SetVolume, SetPitch, SetLFE, SetLPF actions triggered on an object while the object was already performing a similar transition while the base value was not 0 would cause the transition to be computed as relative.
- **WG-17049**: Fixed: Performance drop on 360 for voice with LPF and pitch shifting.
- **WG-17077**: Fixed: Audio source playback from music engine may not be sample-accurate if played from a music switch container in a specific situation.
- **WG-17082**: Fixed: Cone attenuation was randomly applied under special circumstances.
- **WG-17088**: Possible crash with source plug-ins when initialization failure occurs.
- **WG-17091**: Fixed: AkVorbisDecoder.lib symbols clash with standard vorbis distribution.
- **WG-17126**: Fixed: Roomverb audio output could be inconsistent on PS3 for specific presets.
- **WG-17186**: Fixed: Crash in CAkSegmentCtx::ProcessSourcesPlaybackStart() when unloading a bank while a music segment is playing, and this segment contains a track which doesn't have audio content for the whole duration of the segment. (Note that since Wwise 2009.3, unloading a bank does not stop interactive music. However, you might stop hearing it because some parts of the hierarchy are unloaded).
- **WG-17219**: Fixed: In a playlist container, audio clips of segments that are scheduled to play later may not start playing if they are supposed to start within one audio frame of the synchronization point of the current segment. This is most likely to occur with in-memory XMA.
- **WG-17220**: Fixed: (Wii only) Sporadic click at the beginning of sound playback whenever the sound has a sample rate different than 32 KHz or a pitch different than 0.
- **WG-17240**: Fixed: Crash in CAkBus::ExecuteAction() when executing a StopAll/StopAllExcept action when music is playing after the bank that references it was unloaded.

Misc:

- **WG-17151**: Updated documentation after 2009.3 patch 2 fix for WG-16576 - Error in sample code leading to incorrect registration of McDSP plug-ins.

Introduced in 2009.3 Patch 3:

Sound Engine:

- **WG-16067**: - Fixed: Unexpected result with Volume RTPC on effect busses
- **WG-16505**: - Refixed: GCC incompatibility with #pragma warning in [AkObject.h](_ak_object_8h.html)
- **WG-16659**: - Fixed: Memory leak in AkRSIterator.cpp. May happen after a Music Playlist was stopped because the bank that references it was unloaded.
- **WG-16766**: - Fixed: Rare crash in AK::CAkBusCtx::IsEnvironmental()
- **WG-16862**: - Fixed: Crash when breaking loop of an in-memory XMA sound that is virtual (using the Break action)
- **WG-16863**: - Fixed: Break actions CRASH when In-Memory ADPCM and PCM voices are virtual on the Wii

Authoring Application:

- **WG-16861**: - Fixed: Loss of parent-child relationship when there are folders under Actor-Mixers. This bug will occur if the Actor-Mixer is included in a bank that was already loaded

Introduced in 2009.3 Patch 2:

Sound Engine:

- **WG-16505**: - Fixed: GCC incompatibility with #pragma warning in [AkObject.h](_ak_object_8h.html)
- **WG-16612**: - Fixed: Rumble doesn't activate the large motor on the PS3
- **WG-16675**: - Fixed: Rare crash when using SoundSeed Air on PS3
- **WG-15539**: - Fixed: Sample accurate containers with different number of channels may pass garbage in the pipeline
- **WG-16576**: - Fixed: Link conflicts when registering McDSP effects

Introduced in 2009.3 Patch 1:

Sound Engine:

- **WG-16332**: - Fixed: Music switch transitions may not be sample-accurate when playback starts with no look-ahead (generally, using in-memory tracks with transitions without playing any pre-entry).
- **WG-16309**: - Fixed: "Continue to play" flag on switch containers can sometime cause a second playback to fail
- **WG-16402**: - Fixed: Crash while loading a bank that has a large chunk of metadata (greater than 32 KB), because the IO buffer was not aligned on 32 bytes (Wii only).
- **WG-16404**: - Fixed: handling of loss of current audio playback device on Windows
- **WG-16441**: - Fixed: Assert in AkMatrixSequencer.cpp: AKASSERT( m\_cmdPlay.uPlaybackDisableCount > 0 );. May occur when a music transition is reverted after a rapid switch change. This is a regression introduced in 2009.3.
- **WG-16448**: - Fixed: ASSERT in AkSegmentChain.cpp: ( out\_iRequiredLookAhead == pFirstBucket>EarliestActionTime() ), in some cases when using positive fade in offset values in music switch transition rules.
- **WG-16463**: - Fixed: (Wii only) Assert in AkPipelineBufferBase::SetRequestSize(), when using Vorbis sources with virtual voices, or simply if a hardware voice was kicked by the OS.
- **WG-16519**: - Fixed: Possible compiler error when building multiple .vcproj in parallel
- **WG-16538**: - Fixed: [AkFileSystemFlags::bIsAutomaticStream](struct_ak_file_system_flags_aaacd04936e1cbb575cf187470cefe0d6.html#aaacd04936e1cbb575cf187470cefe0d6) flag was missing from 2009.3 (but present in 2009.2.1)
- **WG-16542**: - Fixed: Rare memory corruption leading to a crash when using the RoomVerb plug-in on PS3
- **WG-16543**: - Fixed: The sound engine was failing to build when using the AK\_MEMDEBUG define

Authoring Application:

- **WG-15920**: - Fixed: Recurrent Object ID conflicts at project load
- **WG-16336**：- 修复：音频包编辑器中的注释无法保存 注意：如果您使用 2009.3 补丁 1 保存了带有音频包注释的工程，您将 无法在未打补丁的 2009.3 Wwise 创作应用程序中打开该工程， 因此，如果您计划在音频包上使用注释，请确保在运行 Wwise 的每台 计算机上都安装了该补丁，包括构建或测试机器。

File Packager:

- **WG-16548**: - File Packager: Stream column in Default File Assignment is not working correctly
- **WG-16315**: - File Packager: SFX & Interactive Music Streamed files located in a Mixed SoundBank are not automatically assigned to a package