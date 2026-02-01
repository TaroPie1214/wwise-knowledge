# What&#39;s New in 2008.3

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2008.3

The following sections list and describe the changes made to the Wwise SDK between version 2008.2.1 (the most recent 2008.2.X release at the time of writing) and version 2008.3

*Changes that were also provided in patches over 2008.2.1 are shown in italics.*

# API 变化

- **WG-7665**: Fixed some functions in the SDK to add the keyword "const" when required (Multiple places).
- **WG-9014**: Sony SDK: Wwise is now using Jobs 2.0.
- **WG-11113**: SoundbanksInfo.xml now contains information about Dialogue Events.
- **WG-10363**: Source control plug-ins now need an additional parameter for the Init function of the plug-in "in\_bAutoAccept". See [AK::Wwise::ISourceControl::Init()](class_a_k_1_1_wwise_1_1_i_source_control_a965c84c993e7b9644a7d51dafcdeb113.html#a965c84c993e7b9644a7d51dafcdeb113 "This function is called when the plug-in is initialized after its creation.") for more information.
- **WG-11681**: Sony SDK: Now compiling Wwise using SDK 240.001.
- **WG-11683**: [Microsoft](namespace_microsoft.html) XDK: Now compiling Wwise using June 2008 version (7645).

# 新功能

- **WG-9280**: Optional notifications can be generated on the beat of the music. ([集成详情——音乐回调](soundengine_music_callbacks.html)).
- **WG-9372**: SB Command Line: You can now specify which bank will be generated from the command line.
- **WG-10196**: Environments can now be "positioned" using per-speaker volumes defined in the SDK. This feature is not available on Wii.
  - see AK::SoundEngine::SetEnvironmentVolumes()
- **WG-10363**: SoundBank: An "Import definition file" option is now available from the command line.
  - see [使用命令行](bankscommandline.html)
- **WG-10365**: SoundBank: A Pre-SoundBank Generation Step is now available (command line application).
  - see [使用命令行](bankscommandline.html)
- **WG-10366**: SDK: Game Objects can now have multiple positions.
  - Allows you to create area sounds, PA systems, multi-directional sounds and multi-sources.
  - see [为单个游戏对象设置多个位置](soundengine_3dpositions.html#soundengine_3dpositions_multiplepos)
- **WG-10367**: **SDK: Native Support of 64 bit processors.**
- **WG-10369**: SDK: "Attenuation Scaling Factor" is now available for game objects.
  - Allows you to modify the attenuation radius on a per object basis.
  - see AK::SoundEngine::SetAttenuationScalingFactor()
- **WG-10379**: SDK: Now possibe to query MaxDistance on Game Objects.
  - see [AK::SoundEngine::Query::GetMaxRadius()](namespace_a_k_1_1_sound_engine_1_1_query_a8cc7c4191a91375d58d6a2de118aece4.html#a8cc7c4191a91375d58d6a2de118aece4)
- **WG-10644**: Volume threshold can now be modified from the SDK.
  - Now possible to modify the volume threshold in-game. You can raise the threshold in situations where too many sounds are being played simultaneously. This value no longer has to be a fixed value for the entire project.
  - see [AK::SoundEngine::SetVolumeThreshold()](namespace_a_k_1_1_sound_engine_a4847d43893b9ec435dff3e9ac7555636.html#a4847d43893b9ec435dff3e9ac7555636)
- **WG-10645**: Instance limit on the Advanced Settings tab of the Property Editor can now be controlled using RTPCs.
- **WG-10648**: Now possible to stop pause and resume sounds using only the event containing one or many play actions. This is a workaround to avoid having to create events especially for these. It is also possible to specify fade out times programmatically.
  - see [AK::SoundEngine::ExecuteActionOnEvent()](namespace_a_k_1_1_sound_engine_ac55e3d6ac464b0579a8487c88a755d8c.html#ac55e3d6ac464b0579a8487c88a755d8c)
- **WG-10652**: Now possible to query whether Game Objects are active or not (game objects that play sounds currently) in order to limit processing on the game side. Warning: This only works for sounds that are currently playing. The initial position of the game object must be defined before this can work.
  - see [AK::SoundEngine::Query::GetActiveGameObjects()](namespace_a_k_1_1_sound_engine_1_1_query_a5e88783ff67bfcea2a765cd3adc5e3bd.html#a5e88783ff67bfcea2a765cd3adc5e3bd)
  - see [AK::SoundEngine::Query::GetIsGameObjectActive()](namespace_a_k_1_1_sound_engine_1_1_query_aa04fff7b61cd2cd4df6c0cf0af00e58d.html#aa04fff7b61cd2cd4df6c0cf0af00e58d)
- **WG-10777**: Priority option on the Advanced Settings tab of the Property Editor can now be controlled using RTPCs.
- **WG-11270**: Game sync exclusion keywords can now be used in a SoundBank definition file.
  - see [使用命令行](bankscommandline.html)
- **WG-11284**: Motion support is now available as part of the Integration Demo.
- **WG-11219**: A scaling factor can now be applied to the listener using the SDK.
  - Now possible to modify the attenuation radius per listener.
  - see AK::SoundEngine::SetListenerScalingFactor()

# Behavior and Performance Changes

- **WG-11613**: Performance enhancement: Fixed issue when opening conversion settings on very large projects.
- **WG-11246**: Enable optimizations of DSP codepaths in debug build on all platforms
- **The following were also included in patches provided after 2008.2.1**
- ***WG-11744**: Reduce memory consumption of effect slots*

# Bug Fixes and Miscellaneous Changes

- **WG-8823**: Preparing events fails if Wwise is connected before the bank structural content is loaded.
- **WG-10376**: Generating a SoundBank without "Use SoundBank names" generates a Content File with the SoundBank name instead of the SoundBank ID.
- **WG-10800**: Generating soundbanks from command line | Fix return code.
  - Now more consistent, will return non-zero when an error is encountered. Errors are logged in files.
- **WG-10876**: GetSourcePlayPosition with multiple sources not work when the longest sound is the first one.
- **WG-10921**: Fixed possible memory overwrite when monitoring game objects with very long names.
- **WG-11088**: Wii: ASSERT(AkMusicNode.cpp at line 205: Parent) on change Switch when connected to Wwise.
- **WG-11098**: Crash dump dialog should not show up in commandline scenario.
- **WG-11165**: Make the callback AK\_EndOfDynamicSequenceItem to be triggered for every item in the queue even those who will not play.
- **WG-11230**: Callbacks from Wwise were holding unnecessary lock, causing possible deadlock.
- **WG-11273**: Excluding one of duplicate media entries causes irrelevant warning to appear.
- **WG-11283**: ASSERT (objectreferencemgr.cpp) when generating SoundBanks on a drive with limited space.
- **WG-11375**: Removed some compiler warnings on PS3.
- **WG-11586**: PS3: Sound Engine SPURS instance need prefixes for identification in debugger.
- **WG-11588**: Fixed vorbis decoder stack size problem on PS3.
- **WG-11753**: Wii | ASSERT in SrcBankPCM (line 383) when sample-accurate stopping while sample-accurate starting.
- **WG-11783**: Improper handling of NULL pointer returned by GetActiveChain() in some places in the Interactive Music engine.
- **WG-11781**: Multi-channel sounds randomly glitching when used in interactive music.
- **WG-11782**: Crash in out of memory condition in Interactive Music engine.
- **The following were also included in patches provided after 2008.2.1**
- ***WG-11248**: I/O block constraint not handled in streamed Vorbis source, on the PS3. Applies whenever AK::IAkLowLevelIO::GetBlockSize() returns a value greater than 1. Results in a crash.*
- ***WG-11250**: Unsafe memory allocation in Vorbis decoder (all platforms).*
- ***WG-11251**: I/O block constraint not handled in streamed ADPCM source, on the PS3. Applies whenever AK::IAkLowLevelIO::GetBlockSize() returns a value greater than 1. Results in noise (inconsistent decoder values).*
- ***WG-11271**: Memory corruption in streamed ADPCM sources on the PS3 with multi-channel files (more than 2 channels).*
- ***WG-11275**: Possible ASSERT and file marker leak when starting playback in the middle of a Vorbis file (Windows, Xbox 360, Playstation 3). This scenario can occur with interactive music.*
- ***WG-11276**: Assert and crash in interactive music when playing a music switch container for more than 12.4 hours without changing state/switch.*
- ***WG-11280**: Zero latency streamed sources may stop before the end if they have a looping region that is entirely contained within the prefetched data (all sources).*
- ***WG-11297**: Source plugins may crash when starting virtual "FromElapsedTime" (Wii only).*
- ***WG-11298**: Assert when playing very short (<10 ms) source plugins (Wii only).*
- ***WG-11299**: Assert in CAkMusicTrack::AddPlaylistItem. This assert is related to music tracks' properties, and may occur when playing it from Wwise or loading it from a bank. The properties may become invalid due to authoring of the audio clips contained in the music track (generally when the beginning of the clip is trimmed by a large value).*
- ***WG-11309**: Assert in CAkLEngine::ProcessCommands(): WasPaused() (Wii only).*
- ***WG-11329**: Assert in AkResamplerXBox360.cpp when playing multiple 5.1 streams with pitch resampling with DVD emulation on XBox360, until there is source starvation.*
- ***WG-11330**: Crash when looping a 5.1 streamed file requiring upsample (low sample rate or low pitch) on the Xbox 360.*
- ***WG-11374**: Crash when playing streamed files and source starvation occurs in sample-accurate containers.*
- ***WG-11383**: Non-deterministic generation of .bnk files containing interactive music content. Banks were valid, but some padding was filled using random memory.*
- ***WG-11581**: (Default stream manager implementation) Situation with specific memory settings where 2 streams request each other's buffer, resulting in sub-optimal I/O bandwidth usage (and CPU usage, when I/O is fast).*
- ***WG-11582**: Possible memory corruption / crash when using Step Random or Step Sequence groups in music playlists.*
- ***WG-11587**: Sporadic out of memory error when generating soundbanks for any platform (except Windows).*
- ***WG-11622**: Some specific vorbis files stop playing and report source starvation.*
- ***WG-11633**: Possible assert in Wii Vorbis sources when started sample-accurately (inside containers with sample-accurate transitions, or interactive music). Wii only.*
- ***WG-11649**: PS3: Buffer Overrun in Vorbis codec in some cases.*
- ***WG-11677**: Crash in low memory condition when using filters.*
- ***WG-11406**: Possible bad data alignment on converted Wii ADPCM files.*
- ***WG-11227**: Non-streamed files copied in "Copy Streamed Files" post-generation step in some cases.*