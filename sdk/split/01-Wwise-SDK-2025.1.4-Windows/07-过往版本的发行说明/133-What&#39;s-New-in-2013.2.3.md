# What&#39;s New in 2013.2.3

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2013.2.3

2013.2.3 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2013.2.2 and version 2013.2.3.

# Platform SDK changes

- Android: updated to NDK r9b, added x86 and armeabi-v7a-hf (hard float) configurations
- PS3: updated to SDK 450.001
- Xbox One: updated to XDK August 2013 QFE 8

# Behavior changes

- **WG-24003** (Xbox One) AkSink\_BGM output now tagged as communication stream to avoid it being recorded by DVR.

# 漏洞修复

- **WG-23912** Fixed: crash when limiting voices using game aux sends, combined with some virtual voice behaviors.
- **WG-24073** Fixed: crash after calling RegisterBusVolumeCallback with NULL callback.
- **WG-24076** Fixed: assert in IsActivityChunkEnabled.
- **WG-24086** Fixed: leftover dynamic sequences not cleanly released when terminating sound engine.
- **WG-24103** Fixed: crash when hitting an out-of-memory condition when initializing iZotope Hybrid Reverb.
- **WG-24104** (PS4) Fixed: assert when playing a 7.1 ATRAC9 sound.
- **WG-24148** Fixed: crash when changing game parameter affecting the voice volume of a Blend Container using motion.
- **WG-24152** Fixed: multiple listeners pick the strongest LPF value instead of weakest.
- **WG-24199** (Android) Fixed: SL\_RESULT\_BUFFER\_INSUFFICIENT is printed very often in Android logs.
- **WG-24203** Fixed: rare Wwise application crash when receiving voice profiling information.