# What&#39;s New in 2011.2.1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2011.2.1

2011.2.1 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2011.2 and version 2011.2.1.

# 平台 SDK 更新

- 3DS: updated to CTR-SDK 2.4.0
- Vita: updated to SDK 1.0

# 漏洞修复

- **WG-19804** Fixed: Crash in Vorbis decoder when using very high quality settings on PS3.
- **WG-19823** Fixed: When a property fades is interrupted by a pause action, it may take a lot of time to restart after it is resumed.
- **WG-19843** Fixed: Possible memory overrun when calling [QueryAudioObjectIDs()](namespace_a_k_1_1_sound_engine_1_1_query_ad760c9a7f1596231d185d8ee931231f4.html#ad760c9a7f1596231d185d8ee931231f4).
- **WG-19844** Fixed: Incorrect initial volume caused by auto-ducking.
- **WG-19847** Fixed: Possible crash in interactive music when a transition segment is not loaded when required.
- **WG-19847** Fixed: Inconsistent volume on transition segments when the segment is in a separate music hierachy.
- **WG-19852** Fixed: Memory access out of bounds in MixN job on PS3.
- **WG-19854** Fixed: Audio intermittently sent to wrong environment when sending multiple sounds to multiple environments on PS3.
- **WG-19855** Fixed: Possible crash in low memory condition when seeking in XMA file on Xbox 360.
- **WG-19858** Fixed: Possible crash with continuous switch container when game object is unregistered when playing silent switch.
- **WG-19864** Fixed: SetVolume actions on master bus may not work if no sound is playing, on Wii and 3DS.
- **WG-19866** Fixed: Unloading bank containing Convolution IR on a playing Environmental FX is not returning immediately.
- **WG-19871** Fixed: Crash during Sound Engine initialization when failing to allocate system resources on PS3.