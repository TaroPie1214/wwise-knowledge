# What&#39;s New in 2013.2.5

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2013.2.5

2013.2.5 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2013.2.4 and version 2013.2.5.

# Platform SDK changes

- Mac OS X: updated to SDK 10.8 (Mountain Lion)
- iOS: updated to SDK 7.0
- Xbox One: updated to XDK August 2013 QFE 12
- WiiU: updated to SDK 2.10.03

# API 变化

- (Xbox One) AddPlayerMotionDevice: in\_pDeviceId should now be a straight cast of IGamepad::Id to (void \*). Motion will not work if not done.
- (iOS) New platform initialization settings: interruptionCallback and interruptionCallbackCookie for setting the user callback for handling audio session interruptions.
- (iOS) New platform initialization settings: inputCallback and inputCallbackCookie for setting the user callback for handling audio input.
- (iOS) Removed platform initialization setting: ibAppListensToInterruption to allow apps to handle audio session interruption at all times.
- (iOS) New API: AudioInterruptionCallbackFunc as a user callback to handle audio session interruptions according to the app's need.
- (iOS) API change: ListenToAudioSessionInterruption has a new argument to bypass the user callback.
- (iOS) Removed API: SetAudioInputCallback.

# Performance Improvements

- **WG-24373** Improved performance of File Manager source control operations
- **WG-24419** Improved performance of multi-position game objects

# 漏洞修复

- **WG-20240** Fixed: Unnecessary file conversion when rendered effects are applied, due to random changes in the converted file name
- **WG-23712** (iOS) Fixed: Remote-control-related freezes, crashes, or loss of audio. iOS audio session interruption handling is much improved.
- **WG-23856** (Android) Fixed: Missing memory pool names in the profiler.
- **WG-24030** (Xbox One) Fixed: Possible crash when setting gamepad vibration
- **WG-24389** (Xbox One) Fixed: XMA hang or memory corruption when seeking or using virtual voices in 'play from elapsed time' mode
- **WG-24309** (PS4) Fixed: AkSinkType non-recordable flag handling is inversed
- **WG-24318** Improved documentation and invalid parameter handling of AddSecondaryOutput()
- **WG-24413** Fixed: Invalid Secondary Bus display in the Advanced Profiler
- **WG-24469** Fixed: SoundFrame: GenerateSoundBanks and ConvertExternalSources always return true (success)
- **WG-24490** Fixed: Visual Studio x64 redistributables are not installed on Windows 8
- **WG-24491** Fixed: Bug in streaming manager cache search (valid buffers were not always reused)
- **WG-24520** Fixed: crash in some out-of-memory scenarios in iZotope Hybrid Reverb
- **WG-24541** Fixed: Voice Monitor HDR window not updated in Bus Input mode
- **WG-24546** Fixed: Crash when using an effect on a bus that was not registered via RegisterPlugin
- **WG-24559** Fixed: SoundBank fails to unload due to paused sounds not stopping in rare case
- **WG-24573** Fixed: Rare assert in CAkURenderer::Kick()
- **WG-24578** Fixed: Incorrect HDR behavior when using secondary outputs
- **WG-24615** (Xbox One) Fixed: Crash in [ACPMgr::Init()](namespace_a_k_1_1_comm_a596691b552b507c26b4df958ee1c6de8.html#a596691b552b507c26b4df958ee1c6de8) when initializing and terminating sound engine multiple times
- **WG-24617** Fixed: wrong error handling in RTPC Manager that could lead to corruption in rare low memory conditions.
- **WG-24620** Fixed: Rare crash when terminating the sound engine.