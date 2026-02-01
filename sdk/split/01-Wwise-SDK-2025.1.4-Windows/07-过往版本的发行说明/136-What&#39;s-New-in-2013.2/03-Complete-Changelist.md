# Complete Changelist

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Complete Changelist

The following sections list and describe the changes made to Wwise between version 2013.1.3 and version 2013.2.

# 平台 SDK 更新

- Xbox One: updated to XDK August 2013 QFE 3
- Xbox 360: updated to XDK 21256 September 2013
- PS4: updated SDK 1.020
- WiiU: updated to SDK 2.09.11

# 新功能

请参阅 [新功能](whatsnew_2013_2_new_features.html) f了解更多详情。

- [7.1 Channel Support](whatsnew_2013_2_new_features.html#whatsnew_2013_2_new_features_seven_dot_one).
- [Secondary Output Devices](whatsnew_2013_2_new_features.html#whatsnew_2013_2_new_features_secondary_output).
- [Improved Support For Xbox One and PS4](whatsnew_2013_2_new_features.html#whatsnew_2013_2_new_features_nextgen).
- [GenAudio AstoundSound](whatsnew_2013_2_new_features.html#whatsnew_2013_2_new_features_genaudio).
- [Crankcase Audio REV](whatsnew_2013_2_new_features.html#whatsnew_2013_2_new_features_crankcase).
- [Workgroup Enhancements](whatsnew_2013_2_new_features.html#whatsnew_2013_2_new_features_workgroup).
- **WG-17159** New shortcuts to generate soundbanks. 请参阅 [New Generate SoundBanks Shortcuts](whatsnew_2013_2_new_features.html#whatsnew_2013_2_new_features_bank_shortcuts).
- **WG-18359** New context menu on soundbanks to generate Soundbanks on all platforms or on current platform.
- **WG-18484** Added new Wave Viewer application that can show, diff and playback wav files. Refer to [Wave Viewer](whatsnew_2013_2_new_features.html#whatsnew_2013_2_new_features_waveviewer).
- **WG-19043** Duration of events is now exported in SoundbanksInfo.xml.
- **WG-19784** Project now comes back to non-dirty when undoing up to last save.
- **WG-19873** New button "Exclude All" in the Game Syncs tab of the Soundbank editor.
- **WG-19955** New option when importing new audio files and creating work units: Add to Source Control. 请参阅 [Workgroup Enhancements](whatsnew_2013_2_new_features.html#whatsnew_2013_2_new_features_workgroup) 。
- **WG-20554** Added microphone demo and SoundInput examples to Mac IntegrationDemo.
- **WG-20638** Revert is now accessible in Project Explorer for both Perforce and Subversion plug-ins.
- **WG-20810** The installer now has the possibility to download and extract the files without installing.
- **WG-21536** Now possible to add randomizers on the loop count of random and sequence containers.
- **WG-21809** (Xbox One) Hardware assisted in-memory XMA + SRC on Xbox One.
- **WG-21812** File Manager: Can now show files in flat or tree mode.
- **WG-22146** Now possible to configure the Soundbank Log to change severity on pre or post generation step messages.
- **WG-22147** Removed the -autoclose and -hideprogressui arguments from the Copy Streamed File application. Now the copy streamed file application is always command line.
- **WG-22960** Wwise now supports importing 32-bit float WAV files as exported with ProTools.
- **WG-23140** 7.1 available on PS4, Xbox One and Windows.
- **WG-23225** Perforce now show the "-" status for directories instead of "Local Only"
- **WG-23226** Perforce and Subversion: wproj status is now shown in Wwise titlebar.
- **WG-23227** User interface entries starting with protocol names (<http:,> <ftp:,> mailto:, <file:,> etc) are now clickable and executed with shell API for integration with other tools
- **WG-23275** Source Editor now scale waveforms with fade-in and fade-out curves.
- **WG-23308** Channel names are now shown in the Source Editor.
- **WG-23413** The Output Bus can be to be linked/unlinked to a Platform.

# API 变化

- **WG-23042** Added output channel configuration to [AkSpeakerVolumeMatrixCallbackInfo](struct_ak_speaker_volume_matrix_callback_info.html); also renamed input configuration to uInputConfig (formerly uChannelMask).
- **WG-23169** Added the language code (in\_szLanguageCode) to the Help function in AK::Wwise::IAudioPlugin.
- **WG-23170** Added virtual GetUndoManager() function to IPluginPropertySet. This enables plug-ins to access the undo system.
- **WG-23240** You can now specify the listener bitmask in RegisterGameObj.
- **WG-23256** Added function OnPluginMediaChanged() to AK::Wwise::IAudioPlugin.
- **WG-23422** Speaker angles can now be specified using [SetSpeakerAngles()](namespace_a_k_1_1_sound_engine_afaf319902f00bbf38fbff9129086d912.html#afaf319902f00bbf38fbff9129086d912).
- **WG-23503** (Android) expose OpenSL pointer in the SDK ([AkPlatformInitSettings](struct_ak_platform_init_settings.html))
- **WG-22480** (iOS) Added platform settings to handle audio behaviours for background-foreground switching and inter-app mixing.
- **WG-23561** (iOS) Fixed profiler reconnection failure after the suspend-wakeup UI sequence. Added new API to reinitialize communication module using current settings.

# Behavior Changes

- **WG-16917** Follow Capture Time is now automatically enabled when starting a capture.
- **WG-23144** "Default" bus channel configuration property has been replaced by "Parent". The former value used to mean "hardware device configuration", while "Parent" means "parent bus configuration". The resulting configuration of "Parent" buses may therefore be different with this new version.
- **WG-23043** Downmix equations have been made compliant with AC3 standards. This may result in slight changes in your mix when downmixing from different channel configurations.
- **WG-22922** 3D objects are panned according to the channel configuration of the bus into which they are mixed. This means that 3D objects panned into a stereo bus sound with the same volume whether they are in the front or in the back, while they previously sounded 3 dB lower due to the standard downmix recipe where surround channels are attenuated by 3 dB.

# Performance Changes

- **WG-22992** Performance improvement when updating massive number of RTPC values at every game frame.
- **WG-23404** Reduced memory usage in Default Pool.
- **WG-23423** (Unity) Performance improvement in Unity integration with game object calls.
- **WG-23648** (3DS) Volume computation now faster on the 3DS.

# Miscellaneous Changes

- **WG-20563** Perforce client SDK was updated to version 2013.1

# 漏洞修复

- **WG-19561** Fixed: Query only finds the last effect shareset placed in the four effect slots.
- **WG-20383** Fixed: when a sound is shorter that its prefetch time, it is sometime impossible to use the prepare mechanism to load the prefetch data in memory.
- **WG-22972** Fixed: Out-of-place effect bypass is incorrect when input config is mono and output is stereo: only left channel passes through.
- **WG-22999** Fixed: Music Switch Container Editor - switch/state columns are too small, can't view long switch names.
- **WG-23009** Fixed: Crash when opening a project in authoring tool.
- **WG-23031** Fixed: Source Editor constant power crossfade loop curve is not constant power.
- **WG-23110** Fixed: xWMA encoding of 5.0 file results in mixdown to stereo.
- **WG-23223** Fixed: Stereo IR not working in "filter mode" with configurations having more than 4 channels.
- **WG-23281** Fixed: Assert during interactive music context reversal.
- **WG-23294** Fixed: Unloading work units from the actor mixer hierarchy may not reload properly.
- **WG-23376** Fixed: Adding and removing out of place effects while live editing was causing random crashes or unexpected behaviors.
- **WG-23447** Fixed: Invalid bandwidth displayed in profiler when using Stream Manager for writing.
- **WG-23450** Fixed: rare crash when generating soundbanks while background analysis is in progress.
- **WG-23454** Fixed: Potential crash in Soundbank Editor's edit tab.
- **WG-23477** Fixed: iZotope Trash Multiband Distortion has printf.
- **WG-23534** Fixed: crash in AAC decoder when dummy-sink mode is on.
- **WG-23547** Fixed: init.bnk generation fails silently if existing file is read-only.
- **WG-23549** Fixed: Stop action not functioning on certain sounds, if the sound engine has been running for several days.
- **WG-23627** Fixed: Unexpected source starvation in the interactive music hierarchy with trimmed streamed sounds with zero-latency.
- **WG-23632** Fixed: Potential crash when media relocation happen on bank unload.
- **WG-23638** Fixed: Distortion 2 not processed in iZotope Trash Multi-Band Distortion.
- **WG-23517** Fixed: Source position obtained via [GetSourcePlayPosition()](namespace_a_k_1_1_sound_engine_ae0b469d9fb8a099b40f52f004882d283.html#ae0b469d9fb8a099b40f52f004882d283) is not updated properly after seeking.
- **WG-22261** Fixed: (Android) IntegrationDemo crashes on Android 4.x systems.
- **WG-23540** Fixed: (Android) Device hardware volume buttons don't work properly.
- **WG-23563** Fixed: (Android) Audio click on Nexus 7 devices.
- **WG-23125** Fixed: (iOS) Interruption handler failed to restart the AUGraph/AudioUnit on certain iOS 6 devices.
- **WG-21902** Fixed: (iOS) Updated interruption handler API for user to retry failed interruption handling on app side to get around an iOS6-specific random glitch.
- **WG-23155** Fixed: (iOS) Loss of audio when enabling mixing with built-in music app and controlling music using remote control.
- **WG-23132** Fixed: (iOS) IntegrationDemo crashes on iOS-6.x simulators and devices.
- **WG-23153** Fixed: (iOS) Fixed the bug where a sample rate specified in platformInitSettings does not work.
- **WG-23236** Fixed: (iOS) Fixed freezing in IntegrationDemo when using remote-control to pause/resume background music player app while IntegrationDemo is running under mute-other-apps platform settings.
- **WG-23351** Fixed: (iOS) Profiling crashes if the custom event memory pool is unnamed.
- **WG-23603** Fixed: (iOS) Interruption handling may fail when sound engine is not initialized.
- **WG-23508** Fixed: (iOS, Unity) Crash during start up in app interruption listener.
- **WG-23451** Fixed: (PS4) Loaded banks memory size is displayed as 0 bytes when connected in profiler.
- **WG-23497** Fixed: (Vita) volume isn't updated when changed below threshold while paused.
- **WG-23421** Fixed: (Wii U) Memory corruption with LPF in specific scenarios.