# What&#39;s New in 2013.2.1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2013.2.1

2013.2.1 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2013.2 and version 2013.2.1.

# 新功能

- (Xbox One) WASAPI/XAudio2 choice can now be made at initialization time

# 漏洞修复

- **WG-23430** (Xbox One) WASAPI now detects output channel configuration
- **WG-23756 WG-23757 WG-23796** (Xbox One) multiple stability fixes in XMA playback
- **WG-23760** (Xbox One) fixed: XMA seeking not always working properly
- **WG-23784** Fixed: crash when exceeding maximum number of transitions (AkInitSettings::uMaxNumTransitions)
- **WG-23785** Fixed: [AkSpeakerVolumeMatrixCallbackInfo](struct_ak_speaker_volume_matrix_callback_info.html) is placing game-defined attenuation in user-defined attenuation field
- **WG-23786** Fixed: rare crash when using user-defined sends and running out of memory in the Lower pool
- **WG-23787** Fixed: crash in Mixing Desk when right-clicking the attenuation box on a bus
- **WG-23791** Fixed: crash when using motion on game object with send values
- **WG-23836** Fixed: crash or audio corruption when using zero latency stream files and seeking at beginning (for e.g. within interactive music), with channel downmix audio file conversion, HDR envelopes or loudness normalization