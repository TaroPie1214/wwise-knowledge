# What&#39;s New in 2007.3

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2007.3

The following sections list and describe the changes made to the Wwise SDK between version 2007.2.1 and version 2007.3.

# API 变化

- **WG-8514**: Added new initialization parameter AkPlatformInitSettings::uCellSpursMaxNumSPU on the PLAYSTATION®3.

# 新功能

- **WG-7975**: Added audio output "capture to file" functionality to the Debug and Profile configurations: see [AK::SoundEngine::StartOutputCapture](namespace_a_k_1_1_sound_engine_acad2fdfa60860a790b678fa4bd078540.html#acad2fdfa60860a790b678fa4bd078540) and [AK::SoundEngine::StopOutputCapture](namespace_a_k_1_1_sound_engine_a6dd95ae4196e90674edf3a0ee21b3974.html#a6dd95ae4196e90674edf3a0ee21b3974).
- SPU-based Vorbis decoding is now available on the PLAYSTATION®3.

# Bug Fixes and Miscellaneous Changes

- **WG-6817**: Fixed asserts and crash when playing Vorbis using a seek table with granularity of 1024 sample frames.
- **WG-8220**: Fixed glitches and gaps in same-time music transition with streamed XMA files.
- **WG-8460**: Included Triggers in SoundBank content files.
- **WG-8531**: Fixed some cases of compression artifacts with Vorbis encoding.
- **WG-8544**: Stopped generation of empty enums in Wwise\_IDs.h (fixes compilation issue on the Wii).
- **WG-8559**: Used CreateFileW instead of CreateFile in AkDefaultLowLevelIO on PC (fixes compilation issue in MBCS projects).