# Complete Changelist

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Complete Changelist

The following sections list and describe the changes made to Wwise between version 2010.1.3 and version 2010.2.

# SDK Folder Structure Changes

- **WG-18143** PS3: SPU .elf files are now included in the SDK for debugging purposes.

# 平台 SDK 更新

- Wwise Authoring: updated to DirectX February 2010.
- PlayStation 3: updated to SDK 340.
- Xbox 360: updated to XDK 11775.4 (July 2010).

# API 变化

- **WG-16578** The Reverb and Reverb Lite effects have been removed; they had been tagged as deprecated in recent versions of Wwise. Use the Matrix Reverb, RoomVerb or the Convolution Reverb instead. If you have warnings regarding these effects in your projects, make sure to replace them and re-save your project.
- **WG-16876** 8-bit data is not supported anymore as input for the Wwise sound engine.
- **WG-11166** New music callbacks are available:
  - [AK\_MusicSyncGrid](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a474f5b9582617f8a4f744e7d47dfa155) enables notifications on music grid.
  - [AK\_MusicSyncUserCue](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732ac827761a64b0d02303ea7eaa98240392) enables notifications on music user cue.
  - [AK\_MusicSyncPoint](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732afde5b3e18578530b70f6e1241a552253) enables notifications on music synchronisation point.
- **WG-14789** Grid and Grid Offset are now returned with every music callback notification.
- **WG-16870** LockParams() and UnlockParams() have been removed from [AK::IAkPluginParam](class_a_k_1_1_i_ak_plugin_param.html). Locking of the parameters is not necessary anymore as they are always accessed from the same thread.
- **WG-17060, WG-17080** The following functions now take an optional transition time (fade-in/fade-out) and fade curve type:
  - [AK::SoundEngine::DynamicSequence::Play](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_ae2ac4c400d0145c6c25e050d752064bd.html#ae2ac4c400d0145c6c25e050d752064bd)
  - [AK::SoundEngine::DynamicSequence::Stop](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_a3153fbaab7c917914f2a60183523b1cc.html#a3153fbaab7c917914f2a60183523b1cc)
  - [AK::SoundEngine::DynamicSequence::Pause](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_afd87604f8cea6b836be5b657f74723f3.html#afd87604f8cea6b836be5b657f74723f3)
  - [AK::SoundEngine::DynamicSequence::Resume](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_aa34180ccd604c29cd9222de08a449b4a.html#aa34180ccd604c29cd9222de08a449b4a)
  - [AK::SoundEngine::StopPlayingID](namespace_a_k_1_1_sound_engine_a362a652b7fb7881e3d036facc173dfa1.html#a362a652b7fb7881e3d036facc173dfa1)
- **WG-17087** Added an optional [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) argument to [AK::SoundEngine::DynamicDialogue::ResolveDialogueEvent](namespace_a_k_1_1_sound_engine_1_1_dynamic_dialogue_a18385d0523eb14ff57bd4ea9f18c08f6.html#a18385d0523eb14ff57bd4ea9f18c08f6); when passing the AkPlayingID, the Capture Log will associate the resolved notifications with the dynamic sequence actions.
- **WG-17235** SoundFrame: Added a function "GetDialogueEventOriginalFileList" to obtain the list of Original source files for Dialogue Events into SoundFrame API. Also renamed GetOriginalFileList to AK::SoundFrame::ISoundFrame::GetEventOriginalFileList "GetEventOriginalFileList".
- **WG-17325** Added a function AK::SoundEngine::SetEffect to add or remove effect ShareSets on audio nodes at runtime.
- **WG-17481** The instance of XAudio2 used by the Sound Engine on the Xbox 360 can now be managed by the game by passing AkPlatformInitSettings::pXAudio2 at initialization time.
- **WG-17484** [AK::SoundEngine::Query::GetRTPCValue](namespace_a_k_1_1_sound_engine_1_1_query_a1149dfe866412f53644e3236639ba951.html#a1149dfe866412f53644e3236639ba951) has a modified signature, making it more flexible.
- **WG-17501** Specialization of effect processing interfaces to support out-of-place processing (see [AK::IAkOutOfPlaceEffectPlugin](class_a_k_1_1_i_ak_out_of_place_effect_plugin.html)) additionally to in-place processing (see [AK::IAkInPlaceEffectPlugin](class_a_k_1_1_i_ak_in_place_effect_plugin.html)). Out-of-place effects can be used (outside of Master-Mixer hierarchy) to implement effects that need to produce and consume data at different rates.
- **WG-17596** Effect plug-ins can update their internal state when processing virtual voices 'from elapsed time' (see [AK::IAkInPlaceEffectPlugin](class_a_k_1_1_i_ak_in_place_effect_plugin.html) and [AK::IAkOutOfPlaceEffectPlugin](class_a_k_1_1_i_ak_out_of_place_effect_plugin.html)).
- **WG-17741** Added new AkCommSettings::threadProperties initialization parameter to change the default priority of the communication thread.
- **WG-17788** Stream manager interface now available for use within effect plug-ins. This provides the ability to stream data to or from an effect plug-in by reading or writing data on a specific device (see [AK::IAkEffectPluginContext](class_a_k_1_1_i_ak_effect_plugin_context.html)).
- **WG-17850** [AK::SoundEngine::StartOutputCapture()](namespace_a_k_1_1_sound_engine_acad2fdfa60860a790b678fa4bd078540.html#acad2fdfa60860a790b678fa4bd078540), which opens wave files for writing, now passes [AkFileSystemFlags::uCodecID](struct_ak_file_system_flags_a10e070636834a71e86006eb966ecc77d.html#a10e070636834a71e86006eb966ecc77d "File/codec type ID (defined in AkTypes.h)") = AKCODECID\_PCM to the Low-Level IO ([AK::StreamMgr::IAkFileLocationResolver::Open()](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_ab6daddd96e109dc7669889733ce4f2cc.html#ab6daddd96e109dc7669889733ce4f2cc)) instead of the former value AKCODECID\_BANK. In order to save this file into the "base path" instead of into the streamed files path, the CAkFileLocationBase SDK sample now accepts the file open mode (AkOpenMode) (see functions GetFullFilePath() in file SDK/samples/SoundEngine/Common/AkFileLocationBase.h). Platform-specific default Low-Level I/O implementations were modified accordingly.
- **WG-17868** Extrapolation of position returned by [AK::SoundEngine::GetSourcePlayPosition](namespace_a_k_1_1_sound_engine_ae0b469d9fb8a099b40f52f004882d283.html#ae0b469d9fb8a099b40f52f004882d283) and AK::MusicEngine::GetPlayingSegmentInfo based on elapsed time since last update by sound engine is now optional.
- **WG-17887** Removed the AkEnvironmentValue::fUserData structure member.
- **WG-17888** Reduced usage of AK\_OPTIMIZED define in SDK headers.
- **WG-17946** Mac: added new parameter [AkPlatformInitSettings::uSampleRate](struct_ak_platform_init_settings_a2bf6f000f256b146d6cd36401a234b85.html#a2bf6f000f256b146d6cd36401a234b85 "Sampling Rate. Default is 48000 Hz. Use 24000hz for low quality. Any positive reasonable sample rate ...") to specify the sound engine sample rate.

# 新功能

- New effect plug-ins:
  - Convolution Reverb.
  - Guitar Distortion.
  - Flanger.
  - Tremolo.
  - Meter.
- New codec plug-in:
  - xWMA (only on Xbox 360).
- Source control integration improvements:
  - **WG-16936** Tree conflicts are now shown in the status column when using the Subversion plug-in.
  - **WG-17506** The source control (Perforce and subversion) overlay icons of workunits are now shown in the title bar of the views. The standard context menu is also now available in the title bar area of the views.
  - **WG-17508** Perforce integration now shows outdated files with a yellow triangle.
  - **WG-17509** Workgroup operations (source control) are now accessible from the standard context menu in Wwise.
- **WG-3254, WG-17152** Advanced Profiler: Voice Tab now displays Base Volume, Final Volume, Base LPF and Final LPF for each voice.
- **WG-12128** Wwise custom pre and post soundbank generation steps now have 2 new macros: $SoundBankList and $LanguageList. The value of those macro contains the SoundBanks and Languages passed at the Wwise command line OR the selected banks and languages in the SoundBank Manager.
- **WG-16762** File Packager and CopyStreamedFiles now accept lists of SoundBanks and Languages: use -banks and -languages with a quoted-space-separated list.
- **WG-16208** Capture Log: shift-clicking on an item in the Capture Log now moves the game profiler time cursor to the item's time so that other views (such as Performance Monitor and Advanced Profiler) are synced to the same time.
- **WG-16361** The source control Commit/Submit dialog now show the status of the files. Also, when saving non-checked-out files under Perforce, the list of the files to check-out is now shown with the associated status of the files.
- **WG-16449** Wwise now lists the files to be migrated when loading a project created in an earlier version.
- **WG-16679** The Integration Demo has been completely rewritten; it now contains new and better examples of sound engine usage, and is better organized.
- **WG-16718** New "Plug-in Media" section in SoundBank Content Files listing plug-in media included in the bank. Convolution Reverb is currently the only plug-in with associated media.
- **WG-17525** Ports used for Wwise communication are now configurable. Dynamic/ephemeral ports are used by default where applicable. For more information refer to [通信端口](workingwithsdks_initialization.html#initialization_comm_ports) in the Wwise SDK documentation and "Specifying Network Ports" in the Wwise Help.
- **WG-17674** Command-line support for External Sources has been modified and extended. For more information refer to [Integrating External Sources](integrating_external_sources.html) in the Wwise SDK documentation.

# Behavior and Performance Changes

- **WG-17341, WG-17377** General performance improvements to the Wwise Authoring user interface.
- **WG-17394, WG-17910** Optimized memory usage of Events and Structures in the Default memory pool of the Sound Engine.
- **WG-17939** Major performance improvements when inspecting and playing large sound structures from the Wwise Transport.
- **WG-18138** Improved performance when modifying RTPC values affecting large hierarchies of structures.

# Miscellaneous Changes

- **WG-16832** The Soundbank Manager now support multiple selection.
- **WG-16872** Object context menu is now available by right-clicking in the background of most views.
- **WG-17386** New option "Edit source of override" in areas of the Property Editor where the object inherits from a parent.
- **WG-17617** Effect ShareSets and custom effects now appear in the Edit tab of the SoundBank Editor.
- **WG-17414** Audio Input plug-in now plays back input from microphone inside of Wwise Authoring.
- **WG-17430** External Sources are now allowed to have identical names in the same Wwise project.
- **WG-17457** Effect assignment and ShareSet selection can now be modified during playback or while connected to the game.
- **WG-17465** It is now possible to enter up to 6 decimals in the Game Parameter minimum, maximum and default values.
- **WG-17530** "Volume below minimum threshold" notification now specifies which sound was killed.
- **WG-17556** Now possible to copy and paste RTPC curves on Positioning objects (2D Panner, 3D User-Defined).

# 漏洞修复

- **WG-16764** Inactive references are no longer shown in the Reference view. Inactive references can be references to Conversion Settings or Attenuations for which the owner is not the source of override.
- **WG-16875** Fixed a situation where playing blend containers using the dynamic sequence mechanism would play sounds that are meant to play simultaneously one after the other.
- **WG-17056** Fixed a situation where an assert could pop when shutting down the Sound engine while using dialogue system.
- **WG-17424** Missing Events from the SoundBank Defintion importation now cause the WwiseCLI.exe to return the proper return code.
- **WG-17446** Fixed: Crash after creating 2 streaming devices, destroying the first one, and then profiling.
- **WG-17449** Unused Transition Segments are not packaged in SoundBanks anymore.
- **WG-17474** Fixed: Soundbank generation took a long time to finish after clicking Stop while generating a bank with lots of rendered effects.
- **WG-17477** Fixed: QueryAudioObjectIDs asserts uselessly in case where an audio node is not found.
- **WG-17528** Fixed: Setting environment values with multiple environment values, some of them invalid, was causing the subsequent valid environments settings to be ignored.
- **WG-17558** Fixed a situation where editing the Random Container weight in the Wwise application was not applying it right away.
- **WG-17562** Fixed: Possible lost of profiling data when connecting to a game.
- **WG-17659** Fixed a situation where the sound engine initialization on PC could cause a crash if DirectSound is not supported.
- **WG-17687** Fixed: [AkFNVHash.h](_ak_f_n_v_hash_8h.html) was resetting compiler warning 4127 to default (now using pragma warning push/pop).
- **WG-17734** Fixed: Music Switch Container editor sort is lost during drag & drop operation.
- **WG-17799** Fixed: Crash when multi-editing an audio object that doesn't have a BusRouting element, or a GUID\_NULL BusRouting element.
- **WG-17827** Fixed: "IO error" notification not reported when an error is reported by the low-level IO (deferred device only).
- **WG-17844** Fixed: Profiler stays empty after connection to a game in low memory scenario.
- **WG-17877** Fixed: On Windows XP (Japanese), UI doesn't display properly in some areas such as the lower part of Property Editor's Effects tab.
- **WG-17926** Fixed: Some sounds fail to play when audio clips have been resized in the segment editor.
- **WG-17984** Fixed: External sources specified by "file name" ([AkExternalSourceInfo::szFile](struct_ak_external_source_info_af29151c09e6b12f9b4f5b4c9a9389ba1.html#af29151c09e6b12f9b4f5b4c9a9389ba1 "UTF-8 File path for the source. If not NULL, the source will be streaming from disk....")) pass [AKCOMPANYID\_AUDIOKINETIC](_ak_constants_8h_a807adbb4abc6856ff54fa2010e7f6a0f.html#a807adbb4abc6856ff54fa2010e7f6a0f) to file system instead of [AKCOMPANYID\_AUDIOKINETIC\_EXTERNAL](_ak_constants_8h_a3c5b5200bb04692b832a756b9a71a8b9.html#a3c5b5200bb04692b832a756b9a71a8b9).
- **WG-18019** Fixed: Marker cues not notified in the capture log with converted XMA files played from within the authoring tool.
- **WG-18062** Fixed: Vorbis decoder does not emit an error notification when processing corrupted packet headers.
- **WG-18076** Fixed: Possible crash when undoing creation of groups inside the Music Playlist Editor.
- **WG-18088** Fixed: game object ID '0' was behaving differently in Release config. Note that this game object is reserved for the Wwise Transport and should not be used by the game.
- **WG-18093** Fixed: Possible crash when running Integrity Report on Interactive Music.
- **WG-18148** Fixed: import of multi-channel WAV files generated with Pro-Tools.
- **WG-18159** Fixed: Performance Monitor: "Save All Counters to File" does not saves all counters/columns.