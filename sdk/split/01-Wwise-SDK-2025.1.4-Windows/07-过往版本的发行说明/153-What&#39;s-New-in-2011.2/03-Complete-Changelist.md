# Complete Changelist

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Complete Changelist

The following sections list and describe the changes made to Wwise between version 2011.1.2 and version 2011.2.

# New platforms supported

- **WG-18128** Added Visual Studio 2010 Sound Engine configuration for Windows.

# 平台 SDK 更新

- Xbox 360: updated to XDK 20764 (June 2011).

# API 变化

- **WG-19397** When using the default Stream Manager, the language name used for localized sounds is now set using [AK::StreamMgr::SetCurrentLanguage()](namespace_a_k_1_1_stream_mgr_ae4820886baae734dd90177a49a2be1eb.html#ae4820886baae734dd90177a49a2be1eb), instead of setting a directory name on all low-level I/O devices. Note that the directory separator ("/" or "\") must not be appended to the language name anymore. See [AK::StreamMgr::SetCurrentLanguage()](namespace_a_k_1_1_stream_mgr_ae4820886baae734dd90177a49a2be1eb.html#ae4820886baae734dd90177a49a2be1eb) for more details.
- **WG-18044** Now possible to specify a target playing ID to [PostEvent()](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e) and [ExecuteActionOnEvent()](namespace_a_k_1_1_sound_engine_ac55e3d6ac464b0579a8487c88a755d8c.html#ac55e3d6ac464b0579a8487c88a755d8c), allowing to stop a specific instance using a stop event parametrized in Wwise authoring tool.
- **WG-18044** Now possible to specify the parameter AkActionOnEventType\_Break to the function [ExecuteActionOnEvent()](namespace_a_k_1_1_sound_engine_ac55e3d6ac464b0579a8487c88a755d8c.html#ac55e3d6ac464b0579a8487c88a755d8c).

# 新功能

- **WG-19208** Audio File Importer Enhancements: Now can import folders, and use templates for importation.
- **WG-14665** Different lists in Wwise now remember the column sizes between user sessions.
- **WG-17600** Binary data is now supported in WAV marker labels (i.e. including NULL characters).
- **WG-17676** Wwise Motion now supports rumble on the PS3 Move.
- **WG-17721** New Effect: Harmonizer. Supports pitch shift of multiple voiced without affecting the signal duration.
- **WG-18629** New Effect: Stereo Delay.
- **WG-18633** New Effect: Pitch Shifter plug-in to create a mix of multiple pitched voices without time scaling.
- **WG-17713** New Effect: Time Stretch.
- **WG-18761** States groups inside the Mixing Desk remain sorted and aligned. State groups are now sorted in State tab of Property Editor.
- **WG-18788** Integration Demo for Mac is now available.
- **WG-18909** Multi-editor now remembers the expanded section across sessions.
- **WG-18985** New shortcut key to Edit in an External Editor available from all views (Ctrl+E).
- **WG-19083** Holding the Ctrl key while clicking Solo will remove all other solo currently in place and will solo the currently selected objects.
- **WG-19105** Originals and cache folders can now be relative to Project folder.
- **WG-19208** Now possible to import folders in Wwise and automatically create Containers for every folder.
- **WG-19225** Now possible to specify a list of soundbanks when generating packages with the File Packager to only generate the package associated with the specified soundbanks.
- **WG-19237** Wwise to 3DS Profiler connection is now performed using 3DS Serial IO system instead of the WiFi system.
- **WG-19326** The Content Editor now shows the number of children for the current object.
- **WG-19330** New shortcuts are now enumerated inside context menu. For example, press Ctrl+Shift+1 to do find in project explorer.
- **WG-19344** Content Editor remembers splitter position in for Blend Container, Switch Container and Playlist Containers.
- **WG-19066** Improved streaming latency as well as workflow for sounds that are streamed from RSX (PS3).
- **WG-19457** The File Packager now shows the package header and content size.
- **WG-19040** The File Packager now supports external sources. External Sources can be manually or automatically assigned to packages.

# Behavior and Performance Changes

- **WG-19393** CAkFilePackageLowLevelIO now uses the Wwise Stream Manager API to read file packages instead of reading from disk directly.
- **WG-19404** PS3 controller rumble is slightly stronger to match the XBox controller results.
- **WG-18924** Fixed: FutzBox potential denormal performance problem (drastic CPU increase when effect runs with silenced input).
- **WG-19077** Optimization: Calling PrepareEvent and PrepareGameSync functions will now be causing less seeking on disk as they now order all the media to be loaded by file ID and file offset before proceeding to the I/O. There is now a real advantage to pack all the events to prepare in a single PrepareEvent or PrepareGameSync instead of calling it for each event or gamesync independently.
- **WG-19423** Improved performance of virtual voices on 3DS and Wii.

# Miscellaneous Changes

- **WG-19004** Updated Vorbis encoder to aoTuV beta 6.03.
- **WG-19200** Removed the WwiseMax 3ds Max / SoundFrame sample plug-in.

# 漏洞修复

Sound Engine:

- **WG-19360** Fixed: Loading banks containing very large amount of children under a single container could hang the AudioThread for some time, causing voice starvation.
- **WG-19400** Fixed: Argument [AkFileDesc](struct_ak_file_desc.html) & out\_fileDesc of [AK::StreamMgr::IAkFileLocationResolver::Open()](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_ab6daddd96e109dc7669889733ce4f2cc.html#ab6daddd96e109dc7669889733ce4f2cc) does not have the same address as when it is passed to other functions of the Low-Level I/O interfaces.
- **WG-19429** Fixed: Crash when changing the delay time of a Flanger plug-in while connected to a game (PS3 only).
- **WG-19449** Fixed: LPF and LFE curves set in attenuation editor do not work if spatialization is disabled.
- **WG-19455** Fixed: Memory corruption when a soundbank, loaded into an user-supplied memory pool created with the AkFixedBlockSize attribute, has a media section that is larger than the pool's block size. They should fail gracefully.
- **WG-19460** Fixed: Crash in CAkDeviceBase when terminating a "blocking" streaming device while there are still streams open.
- **WG-19464** Fixed: small audio glitch when LPF parameter changes to and from 0.
- **WG-19483** Fixed: (Xbox 360) Bad throughput heuristic set on xWMA streams. Results in inconsistent xWMA stream profiling data, and suboptimal I/O scheduling when there are xWMA files playing.
- **WG-19503** Fixed: Possible click while stopping continuous containers with sample-accurate transitions on the Wii.
- **WG-19505** Fixed: A maximum of 256 non-virtual voices can be playing at the same time.
- **WG-19515** Fixed: Crash in game when connecting with Wwise and syncing interactive music hierarchy with specific memory conditions.
- **WG-19580** Fixed: Source starvation with streamed XMA in interactive music, if seeking is required when a segment starts.
- **WG-19597** Fixed: (3DS only) Possible crash when Source plug-in are going virtual from elapsed time.
- **WG-19626** Fixed: Possible crash when connecting to the game in low memory situations.
- **WG-19700** Fixed: AKASSERT( !IsActivityChunkEnabled() ); when unloading a bank with a Switch Container in Continuous Mode.
- **WG-19701** Fixed: Streamed sounds within same event are not guaranteed to be synchronized.
- **WG-19721** Fixed: [GetSourcePlayPosition()](namespace_a_k_1_1_sound_engine_ae0b469d9fb8a099b40f52f004882d283.html#ae0b469d9fb8a099b40f52f004882d283) returns undertermined values when more than one sound is played from within the same event.
- **WG-19724** Fixed: [GetSourcePlayPosition()](namespace_a_k_1_1_sound_engine_ae0b469d9fb8a099b40f52f004882d283.html#ae0b469d9fb8a099b40f52f004882d283) returns invalid values after going virtual if started physical, or going physical if started virtual.

Authoring:

- **WG-18570** Fixed: Blend containers using RTPC on layers were not using the common global default RTPC value if the RTPC was not explicitely given to the engine.
- **WG-18748** Fixed: Files may not be re-converted when "Insert filename marker" changes on the conversion settings and working on several platforms.
- **WG-18868** Fixed: Wwise at command line does not handle correctly project paths beginning with a backslash.
- **WG-18914** Fixed: Folder and Work Unit are missing from the object types in the Query editor.
- **WG-19039** Fixed: Now possible to restore None as the Default Switch of a Switch Container.
- **WG-19065** Fixed: GameObject View was not displaying unnamed registered objects registered before the connection.
- **WG-19112** Fixed: Advanced profiler sometimes shows prepared soundbank as loaded in wrong memory pool.
- **WG-19220** Fixed: Wwise memory consumption increases over time when profiler capture stops at maximum memory usage.
- **WG-19256** Fixed: Invalid soundbank names in Soundbank Definition Files now generates an error or warning based on project preference.
- **WG-19294** Fixed: Wav file containing bad RIFF data size in header could hang Wwise in certain situations.
- **WG-19394** Fixed: Wwise Authoring can crash if an event requires more than 16MB.
- **WG-19395** Fixed: Custom instance of Copied sharesets of Meter plug-in do not get their Game Parameter reference copied.
- **WG-19452** Fixed: Some wav files can't load in the waveform view and fail to use the Automatic Sample Detection.
- **WG-19521** Fixed: Possible crash in the Profiler Stat View with empty events.
- **WG-19703** Fixed: The Query Criteria "Platform inclusion" does not consider the ancestor inclusions.