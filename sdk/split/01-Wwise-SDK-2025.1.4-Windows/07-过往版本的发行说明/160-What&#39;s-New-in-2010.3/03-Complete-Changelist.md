# Complete Changelist

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Complete Changelist

The following sections list and describe the changes made to Wwise between version 2010.2 and version 2010.3.

# 平台 SDK 更新

- PlayStation 3: updated to SDK 350.
- Xbox 360: updated to XDK 20209.1 (September 2010).

# API 变化

- **WG-18420** IAkStdStream::SetStreamName() and IAkAutoStream::SetStreamName() now accept an AkOSChar\* instead of a wchar\_t\*.
- **WG-18264** Removed AkDeviceSettings::uIdleWaitTime, which was deprecated in Wwise 2010.2.
- **WG-18267** Removed AkIOTransferInfo::uSizeTransferred. Low-level I/O hook implementations do not need to set uSizeTransferred anymore. If they return AK\_Success, it means that the size transferred was equal to the size requested (AkDeviceSettings::uRequestedSize), so this additionnal operation was useless.
- **WG-18286** Removed function [Init()](namespace_a_k_1_1_comm_a596691b552b507c26b4df958ee1c6de8.html#a596691b552b507c26b4df958ee1c6de8) of \SDK\include\[AK](namespace_a_k.html "Definition of data structures for AkAudioObject")\Tools\Common\[AkListBareLight.h](_ak_list_bare_light_8h.html).

# 新功能

Sound Engine:

- **WG-18276** Major performance optimizations in convolution reverb can be obtained by using new threshold parameter
- **WG-17245** Stream Manager devices now have the ability to cache file data in their Stream IO pool. When a cached buffer is found, no transfer to the Low-Level IO is required. This is particularly helpful with RAM/VRAM devices streaming small looping sounds.

Authoring:

- [Convolution Reverb Optimizations](whatsnew_2010_3_new_features.html#whatsnew_2010_3_convolution_reverb_optimizations)
- [Multiple State Groups Per Object](whatsnew_2010_3_new_features.html#whatsnew_2010_3_multiple_state_groups_per_object)
- [Capture Log Filter Enhancements](whatsnew_2010_3_new_features.html#whatsnew_2010_3_capture_log_filter)
- [Project Explorer Context Menu](whatsnew_2010_3_new_features.html#whatsnew_2010_3_project_explorer_menu)
- **WG-16944** [The SoundBank Manager view can now display folders and soundbanks in a hierarchical manner](whatsnew_2010_3_new_features.html#whatsnew_2010_3_soundbank_manager_tree)
- **WG-17663** [Advanced Profiler's Streams Enhancements](whatsnew_2010_3_new_features.html#whatsnew_2010_3_advanced_profiler_streams) : Multiple new columns were added to help tweak the streaming performance.
- **WG-7841** [Dialogue Event Editor Now Support Multiple Selection](whatsnew_2010_3_new_features.html#whatsnew_2010_3_dialogue_event_editor_multiple_selection) Dialogue .
- **WG-18280** [Copy Platform Settings](whatsnew_2010_3_new_features.html#whatsnew_2010_3_copy_platform_settings) : You can now copy properties from one platform to another for the whole project ("Copy Platform Settings" under the "Project" menu)
- **WG-18118** In the State Tab of the Property Editor, objects can now register to multiple state groups, instead of previously only one. For example, an object may register to a state group "In Menu" and at the same time register to state group "Power Up". Every of the registered state groups can define property variations (volume, lfe, pitch, lowpass), which will be cummulated depending on the current states driven by the game. Additionnaly, for Interactive Music and Bus Objects, every registered state group can specify a music sync point for the state changes.
- **WG-14666** It is now possible to drag and drop objects over the following elements in the Property Editor: Audio Bus, Motion Bus, Conversion Setting, Attenuation, Switch Container's Group and Default, Meter's Game Parameter.
- **WG-18195** It is now possible to specify effect sharesets in the SoundBank definition import files to have the associated Impulse Responses included in SoundBanks.

SoundFrame:

- **WG-16966** SoundFrame now expose the object path for Events, Dialogue Events and Game Syncs.

# Behavior and Performance Changes

Sound Engine:

- **WG-18136** Vorbis: looping and seeking are now sample-accurate.
- **WG-18262** Optimization: Reduced memory required in the Default Sound Engine memory pool.
- **WG-18379** Reduced CPU usage when seeking in vorbis files with large seek table block size.
- **WG-17717** Stream buffering is more efficient with small streamed sounds, and uses less IO memory.

Authoring:

- **WG-18221** General Performance was improved when converting a low number external sources at command line by minimizing the overhead of the Wwise startup.

# Miscellaneous Changes

- **WG-18126** The authoring tool executables and DLLs are now built using VS2008.
- **WG-18129** The sound engine is not built and shipped with VS2005 anymore. Win32\_vc80 and x64\_vc80 platforms have been removed.

# 漏洞修复

Sound Engine:

- **WG-18388** Fixed: Deadlock possibility when multiple thread block on a full message queue
- **WG-18220** Fixed: possible stability issue when Wwise connects to the game.
- **WG-18438** Fixed: (PS3 only) Random crash when coming back from virtual (elapsed time) when started as virtual by a sample-accurate container in vorbis.
- **WG-18344** Fixed: (Wii only) Streamed mono PCM and ADPCM files may play bad data when streaming memory is full.
- **WG-18240** Fixed: Interactive music child switch delayed transition not scheduled when parent transition ends up not being scheduled.
- **WG-18302** Fixed: Notifications randomly not working on Motion sounds.
- **WG-18292** Fixed: Possible crash when generating banks while the option "Generate max attenuation info for events" is enabled and the target of a play action is reported "Missing".
- **WG-18386** Fixed: Possible source starvation at end of stream when using Vorbis
- **WG-16800** Fixed: Stream buffering not accurate with sounds that have a looping region. Looping streams with loop regions used to consider that all data of the stream buffer crossing the loop end was valid, resulting in smaller effective buffering than expected. This could result in source starvation at each loop. It does not apply whole-file loops.
- **WG-17636** Fixed: Streamed Vorbis files may stall indefinitely if some of their packets are larger than the streaming granularity. This is more likely to occur with very high quality settings, and very small streaming granularity. They now fail on start up.
- **WG-18432** Fixed: Vorbis on Playstation 3 can sometimes hold on to more streaming buffers than necessary
- **WG-17800** Fixed: an I/O transfer may be flushed for nothing right after file header is parsed, from time to time. This results in a waste of I/O bandwidth.
- **WG-15481** Fixed: SetVolume action that is applied to a bus may be applied twice when the bus also contains an effect.
- **WG-18448** Fixed: (Wii only) Rare assert in AkVoicePlaybackCtrl.cpp that can occur if a music segment playing a Vorbis audio clip is sought and terminates in the same audio frame.
- **WG-18459** Fixed: Source starvation notifications not reported with interactive music if the audio clip starved so much that it was stopped by the music scheduler before it even started playing.
- **WG-18489** Fixed: Streamed ADPCM sources may be truncated by a few samples at the end (Windows and Xbox 360).
- **WG-18492** Fixed: Sounds playing in multiple environments does not use proper control value (PS3).
- **WG-18526** Fixed: Connecting a project on a meter effect may cause the meter effect to stop driving the associated RTPC.
- **WG-18578** Fixed: Possible crash when using MeterFX plug-in in 5.1 configuration on PS3.

Authoring:

- **WG-18435** Fixed: Context Menu can appear twice in Mixing Desk under some scenarios.
- **WG-18301** Fixed: In Advanced Profiler, Stream Tab, the sort of the column File Size is not working correctly.