# What&#39;s New in 2013.2.8

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2013.2.8

2013.2.8 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2013.2.7 and version 2013.2.8.

# Platform SDK changes

- Updated PS4 to SDK 1.700
- Updated Xbox One to May XDK
- Updated Xcode to 5.1.1

# 新功能

- **WG-24746** Support for tab-delimited files in Audio Files Importer. 现在可从用制表符分隔的文本文件（又称为用制表符分隔的文件）中导入媒体文件。This file can define the following elements:
  - WAV file to import.
  - Object structure to contain the object which uses the WAV file.
  - 任何属性值或引用，例如声部音量或输出总线。
  - Event's Action using the object.
- **WG-25079** Added support for AkSink\_MergeToMain on Windows.
- **WG-25276** Integrity Report for Trigger rate virtual behaviors.

# 漏洞修复

- **WG-24588** Fixed: Rare assert on line 246 in AkLEngineCmds.cpp when stopping a streamed file before its initial buffer has been read from disk.
- **WG-24703** Fixed: Crash or assert when using SoundSeed Air in a low-latency build of the sound engine.
- **WG-24860** Fixed: Occasional nullpointer crash in CAkMixer when using out-of-place effects (corrected fix made in 2013.2.7).
- **WG-25097** (Xbox One) Fixed: Unhandled exception when playing XMA with in\_platformInitSettings.uMaxXMAVoices = 0.
- **WG-25111** Fixed: Dependency on specific version of XInput DLL on Windows in AkRumble plug-in.
- **WG-25114** Fixed: Wrong cue (name) notified when user cue and exit cue overlap.
- **WG-25125** All members of [AkFileDesc](struct_ak_file_desc.html) are now cleared the first time it is passed to [IAkFileLocationResolver::Open()](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_ab6daddd96e109dc7669889733ce4f2cc.html#ab6daddd96e109dc7669889733ce4f2cc).
- **WG-25186** Fixed: AkMp3Source.lib missing from Visual Studio 2013 installer package.
- **WG-25187** (PS4) Fixed: Occasional crash in [AK::SoundEngine::Term](namespace_a_k_1_1_sound_engine_a90f8c91937038615480db2b57ce2279e.html#a90f8c91937038615480db2b57ce2279e).
- **WG-25199** (PS4) Fixed: Several issues in ATRAC-9 decoder with specific files.
- **WG-25203** Fixed: Harmonizer effect crash in out-of-memory conditions.
- **WG-25244** Fixed: Possible assert and crash when running out of memory when starting a state transition.
- **WG-25256** Fixed: Rare crash in [AK::Comm::Term](namespace_a_k_1_1_comm_a94e307d2974b89cc4fbc8ab0fef20d2f.html#a94e307d2974b89cc4fbc8ab0fef20d2f).
- **WG-25276** Fixed: Obsolete warning in Integrity Report when a switch container is child of a sample-accurate container.
- **WG-25286** Fixed: Memory corruption when out-of-bounds listener ID is passed to AddSecondaryOutput.
- **WG-25289** (Xbox One) Fixed: Flush-To-Zero mode not set.
- **WG-25301** Fixed: Music clips lose sync when paused during look-ahead time period.
- **WG-25309** Fixed: Exception handling and RTTI are enabled on Android.