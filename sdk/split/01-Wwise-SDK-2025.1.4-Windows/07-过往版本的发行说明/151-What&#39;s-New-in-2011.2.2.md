# What&#39;s New in 2011.2.2

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2011.2.2

2011.2.2 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2011.2.1 and version 2011.2.2.

# 平台 SDK 更新

- PS3: updated to SDK 370.001
- Xbox 360: updated to XDK 20871.2 (August 2011)

# 漏洞修复

- **WG-19776** Fixed: loss of audio on Windows when current audio device becomes inactive or default audio device changes.
- **WG-19930** Fixed: ExecuteActionOnEvent with AkActionOnEventType\_Break does not work.
- **WG-19957** PS3: Freeze when shutting down console during [AK::SoundEngine::Init](namespace_a_k_1_1_sound_engine_a9a26da64092b97243844df77cbcdbf5f.html#a9a26da64092b97243844df77cbcdbf5f).
- **WG-19965** Xbox 360: corrected buffer management in XAudio2 output voice.
- **WG-20002** Fixed: PrepareEvent calls the wrong Free hook in the release build when releasing prepared media.