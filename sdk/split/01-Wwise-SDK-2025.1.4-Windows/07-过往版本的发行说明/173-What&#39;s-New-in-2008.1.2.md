# What&#39;s New in 2008.1.2

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2008.1.2

The following sections list and describe the changes made to the Wwise SDK between version 2007.4 and version 2008.1.2.  *Changes between 2008.1.1 and 2008.1.2 are shown in italic.*

# API 变化

- **WG-9320**: Several changes made to the plug-in API: AK::IAkEffectPluginContext::GetBypass() method removed. AK::IAkEffectPluginContext::GetProcessLFE() method removed. AK::IAkPlugin::Execute() method changed signature. AK::IAkPlugin::ProcessDone() method removed (was present for PS3 platform only)
- **WG-8202**: AK::SoundEngine::Wii::ActivateRemoteSpeakers function prototype changed. AK::SoundEngine::Wii::ActivateRemoteSpeakers now returns an error code and this error code must be checked by the game.
- **WG-9885**: Functions have been added/modified in the SDK API. [AK::SoundEngine::StopAll()](namespace_a_k_1_1_sound_engine_a0439f61753f31e6b5bb0b42a140ad598.html#a0439f61753f31e6b5bb0b42a140ad598) now takes an optional parameter allowing you to stop only the specified game object. [AK::SoundEngine::StopPlayingID()](namespace_a_k_1_1_sound_engine_a362a652b7fb7881e3d036facc173dfa1.html#a362a652b7fb7881e3d036facc173dfa1) was added to the SDK. This function allows you to stop the playback that was initiated by a specific call to post event.
- ***WG-10578**: Added [AkPlatformInitSettings::threadMonitor](struct_ak_platform_init_settings_aceb6ec44ce21cff07374779bedacda14.html#aceb6ec44ce21cff07374779bedacda14 "Monitor threading properties (its default priority is AK_THREAD_PRIORITY_ABOVENORMAL)....") to allow user changes to monitoring thread properties.*

# 新功能

- Number of effect slots on a voice, mix bus and master control bus has been increased from 1 to 4.
- Switch and Random-Sequence containers are now supported as parents of the Blend container.

# Behavior and Performance Changes

- **WG-8774**: Fixed notifications when loading a bank while simultaneously doing an async unload of the same bank.
- Matrix Reverb processing optimized on the PC and XBox360 platforms.
- Switched to the Tremor codebase for Vorbis decoding on PC, which uses less memory.

# Bug Fixes and Miscellaneous Changes

- **WG-9471**: Fixed crash on [AK::SoundEngine::Term()](namespace_a_k_1_1_sound_engine_a90f8c91937038615480db2b57ce2279e.html#a90f8c91937038615480db2b57ce2279e) while state transitions are still occuring.
- **WG-9459**: Fixed C90 compiler warning on PS3 in Wwise\_IDs.h
- **WG-9423**: Wwise now reports an error when a file is not written on disk due to read-only access during SoundBank generation.
- **WG-9304**: Improved responsiveness of the Game Object Explorer window when connecting to a game.
- **WG-9007**: Better sorting of the information in the profiler tabs.
- **WG-8475**: Limit on the number of children of a Random-Sequence container has increased from 128 to 65535.
- **WG-8297**: Fixed: Unused Wii-motes speaker emits a hiss sound when a sound is played on another Wii-mote speaker.
- **WG-9387**: Add include <malloc.h> to AkFilePackagerLUT.cpp
- **WG-9342**: Add Wwise Object Path for Events and Dialogue Events in SoundBank Contents File
- **WG-8298**: Fixed: BIQUAD and LPF effects cannot be applied on sound already playing on the Wii-mote speaker.
- **WG-9466**: Fixed: Wii build: warning identifier expected in AkTypes.h (2 places)
- **WG-9394**: Fixed: missing exports for [AK::SoundEngine::Query](namespace_a_k_1_1_sound_engine_1_1_query.html) methods in AkAudioEngineDLL.dll
- Fixed: AK\_PS3 define used without being defined in AkPlatformFuncs.h
- **WG-9891**: Fixed: Wwise crashes when saving the project after deleting an effect.
- **WG-9892**: Fixed: A Soundbank that contains no voices may be tagged as "Mixed" and be generated in the language-specific folder.
- **WG-9893**: Fixed: Blend container with multiple children within a sequence or random container may ignore trigger rate.
- **WG-9896**: Fixed: Sound engine crashes when trying to log an Insufficient Memory error after Monitor was term()ed.
- **WG-9897**: Fixed: Interactive music crash when deleting any to any transition.
- **WG-9899**: Fixed: Random-sequence container with trigger transitions : Invalid rate.
- **WG-9901**: Fixed: SDK Doumentation :The initialization snippet of the default Stream Mgr should include [AkStreamMgrModule.h](_ak_stream_mgr_module_8h.html).
- **WG-9902**: Fixed: Random source starvation on Wii when playing ADPCM looping sounds.
- **WG-9904**: Fixed: Sporadic crash in music engine, generally when a State change is pending.
- **WG-9905**: Fixed: Music engine : Fade offset not set in MusicSwitchCntr when using a play action with a fade, and starting state points to nothing.
- **WG-9906**: Fixed: InteractiveMusic Content Still present after terming the music engine (assert + crash on exit).
- ***WG-9529**: Fixed: Crash when converting an XMA file.*
- ***WG-10299**: Extensive rework of Wii playback system – lots of fixes.*
- ***WG-10573**: Fixed: Source Starvation when using Vorbis with certain settings.*
- ***WG-10578**: Fixed: Monitoring freezes Wii game when Sound Engine is under stress.*
- ***WG-10795**: Fixed: Sounds may not play, with the reason specified: Priority was too low, in situations where the maximum number of instances was not yet reached.*
- ***WG-10796**: Fixed: Assert and crash when playing back interactive music on the Wii.*