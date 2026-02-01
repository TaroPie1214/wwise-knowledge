# What&#39;s New in 2013.2.9

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2013.2.9

2013.2.9 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2013.2.8 and version 2013.2.9.

# Platform SDK changes

- PS3: updated to SDK 460.001
- Vita: updated to SDK 3.150
- Xbox One: updated to July XDK
- Android: updated to NDK r9d

# 新功能

- Crankcase REV: Added Fundamental Frequency Output to Game Parameter.
- GenAudio AstoundSound plug-ins now available on Mac.
- **WG-24667** (PS4) Now using new system API to query the actual speaker configuration of the output and assign it to the master bus.
- **WG-25392** (iOS, Android) Low-Level IO sample now has a AddBasePath() function to provide additional file paths for downloaded content. Other platforms can get this behavior using the sample code in AkMultipleFileLocation.h.
- **WG-25532** [AK::SoundEngine::SetSpeakerAngles](namespace_a_k_1_1_sound_engine_afaf319902f00bbf38fbff9129086d912.html#afaf319902f00bbf38fbff9129086d912) can now be used during playback.

# 漏洞修复

- **WG-24397** (Xbox One) Fixed: Time stretch effect has phase issues in the output.
- **WG-24845** Fixed: unused variable compilation warnings in Wwise SDK header files.
- **WG-25110** Fixed: Music notifications are not posted when the event (custom cue, grid) occurs within the last audio frame of the segment's life.
- **WG-25313** (PS4) Fixed: issue with ATRAC-9 decoding.
- **WG-25383** (Windows) Fixed: DLL reference count issue in Motion.
- **WG-25395** Fixed: Full path to plug-in media is part of the conversion hash.
- **WG-25397** (Xbox One) AkSink\_BGM and AkSink\_Communication output now use new DVR exclusion flag from May XDK.
- **WG-25404** Fixed: Assert and stream starvation with sample-accurate containers with mixed virtual behavior.
- **WG-25417** Fixed: Motion LPF property causes SoundBank changes between generations.
- **WG-25419** Fixed: Android I/O cannot be reinitialized once terminated.
- **WG-25423** (Xbox One) Several fixes in XMA decoder.
- **WG-25447** Fixed: Crash when removing a listener on an object with aux sends.
- **WG-25484** Fixed: Fade-in during a transition to custom cue not working properly.
- **WG-25521** Fixed: CopyStreamedFiles.exe copies SFX streams used in language-specific banks to the wrong folder.
- **WG-25544** Fixed: Deleting a RTPC binding does not make the work unit dirty.
- **WG-25551** Fixed: Race condition in AK::MusicEngine::Init.
- **WG-25569** Fixed: variations in Vorbis encoding between PCs cause SoundBank differences.
- **WG-25577** Fixed: Occasional crash when terminating the sound engine on Windows after switching audio device.
- **WG-25587** (Xbox One) Fixed: WASAPI output does not initialize properly when console is set in 5.1.
- **WG-25618** Fixed: wrong error code returned from LoadBank when file is not found on POSIX platforms.