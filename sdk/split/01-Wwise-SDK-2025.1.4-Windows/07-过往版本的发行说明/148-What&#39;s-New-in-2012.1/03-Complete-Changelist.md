# Complete Changelist

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Complete Changelist

The following sections list and describe the changes made to Wwise between version 2011.3.1 and version 2012.1.

# 平台 SDK 更新

- PS3: updated to SDK 410.
- Wii U: updated to CAFE 2.02.

# 新功能

- iZotope Effects now available for Wwise on Windows and Xbox 360. Including Hybrid Reverb, Trash Filters, Trash Distortion, Trash Multiband Distortion, Trash Box Modeler, Trash Dynamics, Trash Delay.
- Nested Work Units. Hierarchies of nested work units can now be created in Wwise and organized in physical folders.
- Unity Pro Integration support new platforms: iOS, Mac, Xbox 360 and Windows.
- Software rendering pipeline on Wii U which leverages all features available on the other software platforms like the Xbox360 and PS3.
- Recording profiling data without using the authoring tool, using the new [AK::SoundEngine::StartProfilerCapture](namespace_a_k_1_1_sound_engine_a55e99fc6cc6be2f93c4599e6e1bd1c0d.html#a55e99fc6cc6be2f93c4599e6e1bd1c0d) API.
- Limited Wii U DRC audio support.

# API 变化

- **WG-13738** Source Control Plugin (Perforce, SVN) API change. See [Source Control API change](whatsnew_2012_1_migration.html#migration_source_control_2012_1) for details.
- **WG-20468** Source Plug-Ins: added support for plug-in media. A Plug-In can now hold more than one item of Plug-In Media (media index > 0 are now supported).

# Behavior and Performance Changes

- Wii U basic software pipeline is now optimized (decoders, resampler, mix). About 3x to 4x performance improvement, comparable to XBox performances (sometimes better!).
- **WG-20421** Fixed: Wwise was possibly taking very long time to close a Wwise project if the project contained a lot of audio input sources.

# Miscellaneous Changes

- **WG-20449** Fixed SN Compiler warnings in low-level IO PS3.
- **WG-20555** iOS | Missing files in level 2 source code.

# 漏洞修复

- **WG-20221** Fixed: Rare crash in CAkMusicSwitchCtx when running out of memory in the default pool.
- **WG-20346** Fixed: Unable to load short RSX package names (smaller than 4 characters, without extension) with sample implementation of RSX device (PS3).
- **WG-20351** Fixed: Crash in Installer while trying to install or modify.
- **WG-20415** Fixed: Compiler warnings in [IBytes.h](_i_bytes_8h.html) and POSIX/AkPlatformFuncs.h.
- **WG-20428** Fixed: Crash in Event Manager Page.
- **WG-20445** Fixed: Crash (division by zero) in some circumstances when playing a music object from the authoring tool.
- **WG-20479** Fixed: [AK::MusicEngine::Term()](namespace_a_k_1_1_comm_a94e307d2974b89cc4fbc8ab0fef20d2f.html#a94e307d2974b89cc4fbc8ab0fef20d2f) does not return if music is still playing.
- **WG-20480** Fixed: Continuous mode may cause Wwise authoring to crash when some node has nothing to play.
- **WG-20487** Fixed: Out-of-memory error when loading bank containing music structures, after loading a mismatching init bank.
- **WG-20510** Fixed: Possible Crash when having multiple nodes in continuous mode in the same hierarchy splitted by switch containers in continuous mode.
- **WG-20511** Fixed: Interactive music does not stop after pausing an ongoing stop action with fade out.
- **WG-20535** Fixed: Possible crash when editing name in project explorer.
- **WG-20537** Fixed: Crash in the source control plug-in manager.
- **WG-20538** Fixed: Crash in Perforce source control at Wwise shutdown.
- **WG-20543** Fixed: Possible memory leak on 3DS in the Release build only when using the Prepare Event mechanism.
- **WG-20571** Fixed: Wwise is unable to play files converted to PCM if they were produced by tools that use a WAVE\_FORMAT\_EXTENSIBLE chunk with a FormatTag equal to WAVE\_FORMAT\_PCM.
- **WG-20577** Fixed: Crash in [AkExternalSourceArray::Create()](namespace_a_k_1_1_stream_mgr_af9d67dd0e502e5603a2921099916e2ab.html#af9d67dd0e502e5603a2921099916e2ab) when out of memory.
- **WG-20616** Fixed: Sound routed to environmental bus does not play if its wet volume is initially under threshold but the dry volume is over the same threshold.
- **WG-20648** Fixed: Occasional crash when connecting or disconnecting to UnrealEd running on same PC as Wwise Authoring.
- **WG-20665** Fixed: Deadlock possible when executing bank callbacks from game thread
- **WG-20643** Fixed: Crash when disconnecting SoundFrame client
- **WG-20596** Fixed: Gain plugin is not part of RegisterAllEffectPlugins

# Bugs fixes for Wii U

The Wii U is still in development. Please check Wii U Known Issues in the Wii U specific section for more information about the state of things on this platform.

- **WG-20484** Fixed: Wii U limited to 1 effect per object (should be 4).
- **WG-20448** Fixed: Memory leak when terminating the sound engine on Wii U.
- **WG-20499** Fixed: Wii U | Convolution reverb fails to initialize.
- **WG-20503** Fixed: Wii U | Sample source plugins are silent in software pipeline configs.
- **WG-20514** Fixed: Wii U Audio glitches alot.
- **WG-20530** Fixed: Crash when running Integrity Report on Integration Demo with the Wii U enabled.
- **WG-20548** Fixed: Crash when connecting to Wii U game, if the music hierarchy needs to be synchronized.
- **WG-20592** Fixed: Wii U profiling | Invalid value for output DC offset whenever a sound plays.
- Fixed: Wii U Positioning Demo CRASH in DEBUG and is silent in PROFILE.
- Fixed: Voice graph profiler exhibits some strange behavior in the Sound "Blue/Turquoise" effect box when profiling Wii U.
- Fixed: Wii U 5.1 source fold-down to stereo is not done correctly.