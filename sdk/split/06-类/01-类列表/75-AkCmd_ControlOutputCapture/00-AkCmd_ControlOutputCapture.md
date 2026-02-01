# AkCmd_ControlOutputCapture

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___control_output_capture-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_ControlOutputCapture结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [isEnabled](struct_ak_cmd___control_output_capture_ab8b512bd8a350cbed512781c92ff836a.html#ab8b512bd8a350cbed512781c92ff836a) |
|  | Whether the Sound Engine should capture the audio output to a file. [更多...](struct_ak_cmd___control_output_capture_ab8b512bd8a350cbed512781c92ff836a.html#ab8b512bd8a350cbed512781c92ff836a) |
|  | |

## 详细描述

Starts or stops recording the sound engine audio output.

The capture system outputs a wav file per current output device of the sound engine. If more than one device is active, the system will create multiple files in the same output directory and will append numbers at the end of the provided filename.

If no device is running yet, the command will return success AK\_Success despite doing nothing. Use [AK::SoundEngine::RegisterAudioDeviceStatusCallback](namespace_a_k_1_1_sound_engine_a3f31beb89a4f3ef42475b0849020abe3.html#a3f31beb89a4f3ef42475b0849020abe3) to get notified when devices are created/destructed.

备注
:   The sound engine opens a stream for writing using `AK::IAkStreamMgr::CreateStd()`. If you are using the default implementation of the Stream Manager, file opening is executed in your implementation of the Low-Level IO interface `AK::StreamMgr::IAkLowLevelIOHook::BatchOpen()`. The following [AkFileSystemFlags](struct_ak_file_system_flags.html "File system flags for file descriptors mapping.") are passed: uCompanyID = AKCOMPANYID\_AUDIOKINETIC and uCodecID = AKCODECID\_PCM, and the AkOpenMode is AK\_OpenModeWriteOvrwr. See [文件位置解析](streamingmanager_lowlevel.html#streamingmanager_lowlevel_location) for more details on managing the deployment of your Wwise generated data.

When `isEnabled` is set, the Sound Engine expects a string to follow the command representing the name of the file to write. For example:

```
auto cmd = (AkCmd_ControlOutputCapture*)AK_CommandBuffer_Add(buffer, AkCommand_ControlOutputCapture);
cmd->isEnabled = 1;
AK_CommandBuffer_AddString(buffer, "myrecording.wav");
```

This command can fail for the following reasons:

- `AK_InvalidParameter` if no valid file name follows the command when starting output capture.

  参见
- [AK::SoundEngine::StartOutputCapture](namespace_a_k_1_1_sound_engine_acad2fdfa60860a790b678fa4bd078540.html#acad2fdfa60860a790b678fa4bd078540)
- [AK::SoundEngine::StopOutputCapture](namespace_a_k_1_1_sound_engine_a6dd95ae4196e90674edf3a0ee21b3974.html#a6dd95ae4196e90674edf3a0ee21b3974)
- [AK::StreamMgr::SetFileLocationResolver](namespace_a_k_1_1_stream_mgr_ab5c2340963ac5ff81e49969b74ef2520.html#ab5c2340963ac5ff81e49969b74ef2520)
- [流播放/流管理器](streamingdevicemanager.html)
- [文件位置解析](streamingmanager_lowlevel.html#streamingmanager_lowlevel_location)
- [AK::SoundEngine::RegisterAudioDeviceStatusCallback](namespace_a_k_1_1_sound_engine_a3f31beb89a4f3ef42475b0849020abe3.html#a3f31beb89a4f3ef42475b0849020abe3)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1155](_ak_command_types_8h_source.html#l01155) 行定义.