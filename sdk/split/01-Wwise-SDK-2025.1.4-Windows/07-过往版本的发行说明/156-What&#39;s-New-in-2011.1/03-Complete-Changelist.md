# Complete Changelist

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Complete Changelist

The following sections list and describe the changes made to Wwise between version 2010.3.3 and version 2011.1.

# New platforms supported

- Apple iOS
- Nintendo 3DS

# 平台 SDK 更新

- Xbox 360: updated to XDK 20500 (February 2011).
- PS3: updated to SDK 360.001
- iPhone/iPad minimum Deployment version is iOS 4.0
- **WG-16940** Perforce Plugin is now using Perforce 2010.1 SDK

# API 变化

Sound Engine:

- **WG-18768** AK\_MAX\_ENVIRONMENTS\_PER\_OBJ is now 3 on the Wii to reflect the platform limit of 3 busses.
- **WG-19024** New API functions to manage a callback to be called at every audio frame: [AK::SoundEngine::RegisterGlobalCallback](namespace_a_k_1_1_sound_engine_ade293d3ed101fe494ead6dffb1c682fb.html#ade293d3ed101fe494ead6dffb1c682fb) and [AK::SoundEngine::UnregisterGlobalCallback](namespace_a_k_1_1_sound_engine_a79c4af0e9466849874ef113c9f8079d7.html#a79c4af0e9466849874ef113c9f8079d7).
- **WG-18509** New feature: Option to avoid initializing and terminating platform network library (sockets) in sound engine. Check [AK::Comm::Init](namespace_a_k_1_1_comm_a596691b552b507c26b4df958ee1c6de8.html#a596691b552b507c26b4df958ee1c6de8) function.
- **WG-18753** Removed AK\_USE\_PLUGIN\_ALLOCATOR macro, which is not necessary anymore.
- **WG-19020** Visual Studio Property Sheets are now available for building plug-ins for the Wwise Authoring application, in SDK/source/Build/PropertySheets.

Authoring:

- **WG-18704** The Plugin XML definition schema was changed to include some user interface elements that were previously defined in the User interface resources. Refer to [Wwise 插件 XML 描述文件](plugin_xml.html) for more information.

# 新功能

- **WG-16008** Mute and Solo buttons are now available for every audio object in Wwise. Refer to [Solo Mute for Monitoring](whatsnew_2011_1_new_features.html#whatsnew_2011_1_solo_mute).
- **WG-18586** Multi-edit user interface has been redesigned and has coverage been increased. Refer to [Multi-Editor improvements](whatsnew_2011_1_new_features.html#whatsnew_2011_1_multi_editor).
- **WG-18315** Notes are now shown in the Multi-Editor. Clicking the notes field everywhere in Wwise now shows a popup text editor. Refer to [Multi-Editor improvements](whatsnew_2011_1_new_features.html#whatsnew_2011_1_multi_editor).
- **WG-16407** Positioning parameters are now exposed in the multi-editor. Refer to [Multi-Editor improvements](whatsnew_2011_1_new_features.html#whatsnew_2011_1_multi_editor).
- **WG-18476** Now possible to specify the diff program to use for the Perforce Plugin. Refer to [Perforce diff tool is now configurable](whatsnew_2011_1_new_features.html#whatsnew_2011_1_perforce_diff).
- **WG-18610** Now possible to send voices to be virtual when over instance limit. Refer to [New Voice Limitation System](whatsnew_2011_1_new_features.html#whatsnew_2011_1_new_voice_limitation_system).
- **WG-18611** Now possible to set a global, per platform Maximum number of voice instances either by the SDK or the Wwise project settings. Refer to [New Voice Limitation System](whatsnew_2011_1_new_features.html#whatsnew_2011_1_new_voice_limitation_system).
- **WG-14200** Sound instance on Actor hierarchy objects can now be optionally applied globally or per game object. Refer to [New Voice Limitation System](whatsnew_2011_1_new_features.html#whatsnew_2011_1_new_voice_limitation_system).
- **WG-2700** New SetGameParameter action available. It is also capable of performing RTPC over a fixed (but randomizable) period of time using predefined curves. RTPC over a fixed period of time is also available from the SDK. Refer to [New Event Action: Set Game Parameter](whatsnew_2011_1_new_features.html#whatsnew_2011_1_event_set_game_parameter).
- **WG-17239** Now possible to set the severity of the different messages appearing during the Soundbank generation. Changing the message severity can be use to control the return code at of the command line while generating the soundbanks. Refer to [Configurable Soundbank Log Severities](whatsnew_2011_1_new_features.html#whatsnew_2011_1_soundbank_log_configurable).
- **WG-17171** Convolution Reverb now has a new tab for equalization using curve controls applied offline to the impulse response. Refer to [Convolution Reverb EQ](whatsnew_2011_1_new_features.html#whatsnew_2011_1_convolution_reverb_eq).
- **WG-18519** Convolution Reverb now has a control to allow panning the impulse response to compensate for recordings that tend to steer the image of the wet path. To create interpolation between 2 mono impulse responses to obtain a hybrid impulse response.
- **WG-18656** AAC support on Mac and iOS.
- **WG-18620** Now possible to see from the Voice tab in the advanced profiler if a voice is virtual because it is under volume threshold of if it is virtual because it is over some limit.
- **WG-18195** Now possible to specify effect shareset in the SoundBank definition import files to have the associated Impulse Response included in SoundBanks.
- **WG-18593** Sine plug-in can now route output to LFE channel, improved performance and operates on SPU on PS3 platform
- **WG-18775** The File Manager now allows move operations on a multiple selection when using Perforce or Subversion plug-ins.
- **WG-17592** New item in the Performance view to monitor the number of physical voices.
- **WG-16119** You may now edit events/actions in the authoring tool while it is connected to your game.
- **WG-16122** Advanced Settings: Now possible to edit the maximum number of voices and priority in real time.

# Behavior and Performance Changes

- **WG-18612** Now possible to playback sounds encoded with Vorbis with no seek table even if they are set to Go Virtual and "From Elapsed time", they will restart from beginning if they come back from the virtual state.
- **WG-14879** Virtual Voices do not count anymore as active voices, preventing them to be taken into account when computing voice limits.
- **WG-19033** Guitar Distortion FX: Fuzz distortion mode handles tone parameter changes more consistently across the range.
- **WG-17561** SetMultiplePositions called with no positions will virtualize all sounds on the un-positioned game object.

# Miscellaneous Changes

- **WG-17945** Mac installer is now a package file instead of a DMG.
- **WG-18547** All Wwise SDK functions are now declared using the \_\_cdecl on the Windows platform so projects using a different default calling convention can still link with the Wwise SDK.

# 漏洞修复

Sound Engine:

- **WG-18671** Fixed: Possible crash when playing interactive music when all segments are excluded from the platform.
- **WG-18631** Fixed: Possible issue with AkEvent on the Wii where a waiting thread could be released even if the event wasn't signaled.
- **WG-18616** Fixed: Crash when calling GetPoolStats with an invalid pool ID.
- **WG-18311** Fixed: Environmental effects can be lost after connecting to a game.
- **WG-18973** Fixed: Leaking file handle when converting XMA and xWMA files.
- **WG-17547** Fixed: Not possible to call SetMultiplePositions with more than 84 positions.
- **WG-18870** Fixed: Occasional crash when adding game object watches while connected to game.
- **WG-18578** Fixed: Possible crash when using MeterFX plug-in in 5.1 configuration on PS3.
- **WG-17974** Fixed: Potential deadlock when CancelCallbackCookie is called upon reception of a AK\_EndOfEvent callback.
- **WG-18625** Fixed: Stability issue with McDSP plug-ins when terminating the sound engine.
- **WG-18737** Fixed: Spread parameter ignored when sound plays at listener position.
- **WG-18930** Fixed: Total voice count in Performance Monitor also counts mixing busses.
- **WG-19019** Fixed: xWMA prefetch size (Zero-Latency mode) not computed correctly.
- **WG-18623** Fixed: Rare out of memory condition not handled properly in SoundSeed Impact plug-in.
- **WG-18847** Fixed: Rare crash with volume fades while ducking and mixing.
- **WG-18860** Fixed: (Mac Debug only) Race condition when terminating sound engine may cause an (inoffensive) assert.

Authoring:

- **WG-18922** Fixed: Potential crash in the Authoring tool when disconnecting from a game.
- **WG-18966** Fixed: Effect Rendering on the Convolution Reverb effect can sometime cause the conversion to fail.
- **WG-19109** Fixed: Advanced Profiler does not always show updated information in some tabs.
- **WG-18405** Fixed: During project migration, Wwise requires all files to be writable even if only a portion of the files need to be migrated.
- **WG-18659** Fixed: Regenerating the init bank could produce a binary different but valid bank file.
- **WG-18626** Fixed: SoundBank Editor, Edit tab: Sort is not working for first column.
- **WG-18668** Fixed: Stability issues (hangs) when the Perforce server is busy or slow.
- **WG-15557** Fixed: When using the Perforce plug-in, the message "login not necessary, no password set for this user" may be displayed unnecessarily.
- **WG-18725** Fixed: Repositioning the views in the layout can cause user interface controls to disappear.
- **WG-18364** Fixed: Presets for Effects are not loaded and saved correctly.
- **WG-18731** Fixed: Performance problem with long profiling sessions.