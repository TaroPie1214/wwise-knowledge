# Complete Changelist

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Complete Changelist

The following sections list and describe the changes made to Wwise between version 2012.1.1 and version 2012.2.

# 平台 SDK 更新

- PlayStation 3: updated to SDK 420.001
- Xbox 360: updated to XDK July 2012 (21173.1), and updated projects to Visual Studio 2010.
- Wii U: updated to Cafe SDK 2.07 and Multi 5.2.13
- Windows: added vc110 configuration (Visual Studio 2012 RC)
- PS Vita: updated to SDK 1.650

# 新功能

- Auxiliary Sends : Complete auxiliary send system allowing to send portion of the signal to auxiliary busses for parallel processing. Refer to [User-Defined Auxiliary Sends](whatsnew_2012_2_new_features.html#feature_2012_2_user_auxsends) and [Game-Defined Auxiliary Sends](whatsnew_2012_2_new_features.html#feature_2012_2_game_auxsends) for more information.
- Peak Meters: Peak Meters on busses, in 5.1. Refer to [Meters](whatsnew_2012_2_new_features.html#feature_2012_2_meters) for more information.
- Volume Enhancements: Volume can go over 0dB. Refer to [Volume Enhancements](whatsnew_2012_2_new_features.html#feature_2012_2_volume_enhancements) and [Volume can go over 0 dB](whatsnew_2012_2_migration.html#migration_volume_2012_2) for more information.
- Added new PS Vita platform with enhanced performances using hardware DSP decoder and effects
- **WG-16408** When selecting objects of multiple types, the Multi-Editor now displays all properties of all object types (in previous versions, only the common properties were shown).
- **WG-19391** The soundbank manager now remembers the expand collapse of the previous session.
- **WG-19391** The tree list controls now offers a expand all and collapse all via CTRL+click or by using the contextual menu over the +/-.
- **WG-20335** Custom Properties: it is now possible to add user-defined properties to Sound and Audio Source objects in a Wwise Project, and to query their value in-game. Refer to [Custom Properties](whatsnew_2012_2_new_features.html#feature_2012_2_custom_properties) for more information.
- **WG-20572** Wii U: General memory and cache optimizations (OSBlockMove, OSMemSet, DCZeroMemory, etc)
- **WG-20349** Wii U: Implemented rumble on the DRC and Wii Remotes
- **WG-20359** Wii U: Wiimote audio is now supported (CAT-DEV MP only)
- **WG-20394** Vita hardware effects are now supported on auxiliary busses.
- **WG-20963** Wii U: Can specify the number of audio buffers with [AkPlatformInitSettings.uNumRefillsInVoice](struct_ak_platform_init_settings_a953085ec90c00bf53ddafc8af700277d.html#a953085ec90c00bf53ddafc8af700277d "Number of refill buffers in voice buffer. 2 == double-buffered, defaults to 4.") for more resilience against voice starvation.
- **WG-21300** Support for Background mode (Home Button) on the Wii U. Use AK::SoundEngine::Wii::SetProcessMode to switch between the two modes. IntegrationDemo 演示了 Home 按钮支持功能（查看 Main.cpp）。

# API 变化

Environmental functions are replaced by auxiliary sends functions. The following functions are removed or replaced:

- AK::SoundEngine::SetGameObjectEnvironmentsValues()
- AK::SoundEngine::SetGameObjectDryLevelValue()
- AK::SoundEngine::SetEnvironmentVolume()
- AK::SoundEngine::SetEnvironmentVolumes()
- AK::SoundEngine::Query::GetEnvironmentVolumes()
- AK::SoundEngine::BypassEnvironment()

Refer to [Environmental system is replaced by the Auxiliary Sends](whatsnew_2012_2_migration.html#migration_environmental_2012_2) for more information.

- **WG-20357** API change: SetEffect() were replaced by SetBusEffect and [SetActorMixerEffect()](namespace_a_k_1_1_sound_engine_a00256bfd86c2bed14c626922fc4417b0.html#a00256bfd86c2bed14c626922fc4417b0), user must call the correct one.
- **WG-20874** SoundFrame: GetGUID is now a method on ISFObject base interface.

# Behavior and Performance Changes

- **WG-20928** Wii U: Optimized the PeakLimiter 4.4x. It takes 0.2% of CPU (0.06ms) for a mono sound. Between 1.1 and 2.8x for all other platforms.
- **WG-20929** Wii U: Delay effect optimized 2.3x. It takes 0.07% of CPU (0.02ms) for a mono sound.
- **WG-20986** Wii U: More optimizations for AkRoomVerb. Performance is now around 2.3x what it was with 2012.1.
- **WG-21261** When passing in\_uSize == 0 to [AK::IAkStdStream::Read()](class_a_k_1_1_i_ak_std_stream_a2b12fb0cd1beb3c1d77c8206a8b5796d.html#a2b12fb0cd1beb3c1d77c8206a8b5796d), the stream's status is now set to "AK\_StmStatusCompleted" instead of "AK\_StmStatusIdle".
- **WG-21303** Fixed: Sub-optimal cancellation of pending transfers when changing stream position, resulting in an I/O request sent twice.

# Miscellaneous Changes

- **WG-19808** Wii U: communication now goes through the USB-Ethernet adapter instead of HIO.
- **WG-20473** Upgraded TLSF allocator to version 2.0 in default memory manager.
- **WG-20811** Perforce SDK was updated to 2012.1 - fixing severe stability issues
- **WG-20148** Subversion SDK was updated to 1.7.5 and 64-bit was added
- **WG-20956** New sample project with documentation: Wwise Project Adventure.
- **WG-21448** Wii U: Communication (profiler): NC library usage was dropped in favor of AC library. Your projects should now link to nn\_ac.a.

# 漏洞修复

- **WG-18165** Fixed: Meter Effect output value is not reset to its minimum after a stop action.
- **WG-20618** Fixed: Wii U : convolution reverb is not working.
- **WG-20670** Fixed: Soundcaster and Contents Editor items have incorrect size when Windows locale is set to Japanese.
- **WG-20735** Fixed: Calling StopPlayingID with the AK\_INVALID\_PLAYING\_ID has unexpected results.
- **WG-20779** Fixed: File Packager crash in 64-bit when using external sources.
- **WG-20780** Fixed: Crash when importing a SFX audio source into a Voice object in the Audio File Importer.
- **WG-20784** Fixed: Crash when launching WwiseCli with unknown language.
- **WG-20802** Fixed: Non-alphanumerical characters are not searchable under the Edit tab of the Soundbank Editor.
- **WG-20853** Fixed: Nested work-unit can become dirty after opening a project.
- **WG-20881** Fixed: Music Track Stream/Look ahead-time/Zero Latency/Prefetch length and their Link/Unlink state are not loaded from the preset.
- **WG-20882** Fixed: SFX Stream Zero Latency Prefetch length and its Link/Unlink state are not loaded from the preset.
- **WG-20883** Fixed: Limit Sound Instance "Per game object/Globally" dropdown value is not loaded from the preset.
- **WG-20884** Fixed: Position Source User-defined "Follow Listener Orientation" value is not loaded from the preset.
- **WG-20885** Fixed: Effects tab - Bypass All, Bypass and Render checkmark state are not loaded from the preset.
- **WG-20925** Fixed: Potential hang at the end of profiling session load.
- **WG-20954** Fixed: Play button is disabled in transport when connected (should use the game assets).
- **WG-21047** Fixed: Potential crash when closing Wwise and disconnecting from the game.
- **WG-21050** Fixed: Loss of audio when unplugging and replugging headphones on a particular hardware.
- **WG-21053** Fixed: Audio clip is not played back when moved from a music track to another while the segment is playing (live authoring).
- **WG-21107** Fixed: Glitch in interactive music when loading soundbanks that contain interactive music structures.
- **WG-21135** Fixed: Crash when using a multichannel IR in convolution reverb effect.
- **WG-21169** Fixed: Persistence issue when music clips have a duration of zero.
- **WG-21176** Fixed: Copying conversion settings can crash if the codec is not installed.
- **WG-21216** Fixed: SVN: comments in non-ansi characters are lost during commit operations.
- **WG-21240** Fixed: SpeakerVolumeMatrixCallback is not working properly in 2D if user code tries to modify volumes.
- **WG-21312** Fixed: State change ignored when applied to multiple levels of switch containers in the same frame.
- **WG-21313** Fixed: Child music switch containers ignore state changes towards "None" when their parent is performing a transition.
- **WG-21333** Fixed: Wii U: crash when 5.1 voices were sent to the DRC through the "Transfer Mode" (play everything on the DRC).
- **WG-21355** Fixed: Out-of-Memory errors do not appear correctly in the Capture Log.
- **WG-21356** Fixed: PS3: Memory corruption with multiple instances of Meter Effect on busses.
- **WG-21368** Fixed: Repetitive Perforce operations required when opening iZotope Box Modeler
- **WG-21379** Fixed: User Keyboard shortcuts are not loaded when starting Wwise.
- **WG-21382** Fixed: Crash in Keyboard Shortcut Manager when removing a shortcut binding.
- **WG-21412** Fixed: Wii U:Hang or crash when closing a game from the Home Menu on Wii U.
- **WG-21466** Fixed: Sounds with bus effects sent to DRC while DRC transfer mode is active don't sound the same.
- **WG-21507** Fixed: WiiU: Use the hardware setting for the audio config of the DRC. Support Mono output for TV.
- **WG-21526** Fixed: [AK::SoundEngine::GetSourcePlayPosition](namespace_a_k_1_1_sound_engine_ae0b469d9fb8a099b40f52f004882d283.html#ae0b469d9fb8a099b40f52f004882d283) returns negative value when sound has not started yet.
- **WG-21543** Fixed: Link warnings on WiiU with ConvertInternal symbol.
- **WG-21537** Fixed: Rare memory corruption involving random/sequence containers with sample-accurate transitions and wave file markers.