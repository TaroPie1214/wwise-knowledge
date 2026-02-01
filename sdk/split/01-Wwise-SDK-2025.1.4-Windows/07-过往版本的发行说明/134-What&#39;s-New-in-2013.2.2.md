# What&#39;s New in 2013.2.2

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2013.2.2

2013.2.2 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2013.2.1 and version 2013.2.2.

# Platform SDK changes

- 3DS: updated to CTR-SDK 5.2.3 and VSI-CTR Platform based on Visual Studio 2010
- Wii U: updated Multi compiler to 5.3.22

# 新功能

- (iOS) New API function AK::SoundEngine::iOS::Suspend to notify Sound Engine that the device is suspended.
- (Wii U) Ak::SoundEngine::Wii::SendMainOutputToDevice now supports sending to both TV and DRC at the same time with AkSink\_DRC\_Slave
- (Xbox One) Trigger rumble now supported by motion generator.
- (Xbox One) Maximum XMA instance count now exposed as an initialization parameter.

# 漏洞修复

- **WG-23747** Fixed: (iOS) Various crashes due to dummy sink misbehaviour during audio session interruption and suspension.
- **WG-23839** Fixed: (Xbox One) Elapsed time calculation of "from elapsed time" XMA virtual voices is wrong.
- **WG-23868** Fixed: (Xbox One) Assert when applying a time stretch effect on a XMA voice.
- **WG-23850** Fixed: Advanced profiler erroneously displays sounds to be sent to aux busses using game-defined even when they are not enabled.
- **WG-23855** Fixed: SoundBanks show up as 'Unknown' in Advanced Profiler (SoundBanks and Loaded Media tabs).
- **WG-23857** Fixed: Possible crash when pressing directions arrows in some empty views.
- **WG-23860** Fixed: (Wii U) Compilation issues with Multi 5.3.22.
- **WG-23863** Fixed: Possible crash when adding a State Group containing lot of States in the Dynamic Dialogue view.
- **WG-23876** Fixed: Crash when connecting/disconnecting headphones in Remote Desktop.
- **WG-23880** Fixed: Possible crash when editing Game Object Watched list while the 3D filter view is displayed.
- **WG-23911** Fixed: Possible crash when using a changing set of game-defined aux sends and specifying non-existing aux bus ids.
- **WG-23935** Fixed: Rare transition leak when exceeding maximum number of transitions, or running out of memory; can cause sounds to fail to stop.
- **WG-23955** Fixed: Calling SetActiveListener always prints "Sound has no listener" warning.
- **WG-23981** Fixed: Pausing a voice sending to an Aux Bus could in some occasions loose its active send when resuming.