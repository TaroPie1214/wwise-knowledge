# AkCmd_AddOutputCaptureMarker

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___add_output_capture_marker-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_AddOutputCaptureMarker结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [markerDataSize](struct_ak_cmd___add_output_capture_marker_ab6782014729f02127350e352f09adeec.html#ab6782014729f02127350e352f09adeec) |
|  | Size (in bytes) of the data following the command. For text markers, must include the null byte. [更多...](struct_ak_cmd___add_output_capture_marker_ab6782014729f02127350e352f09adeec.html#ab6782014729f02127350e352f09adeec) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [samplePos](struct_ak_cmd___add_output_capture_marker_adaefa5547eed335e18b1e2822d4b4893.html#adaefa5547eed335e18b1e2822d4b4893) |
|  | Sample position to attach the marker to. If set to AK\_INVALID\_SAMPLE\_POS, marker is added at the current recording time. [更多...](struct_ak_cmd___add_output_capture_marker_adaefa5547eed335e18b1e2822d4b4893.html#adaefa5547eed335e18b1e2822d4b4893) |
|  | |

## 详细描述

Adds text or binary marker in captured audio output file.

The Sound Engine expects either a string or binary data to follow this command. For example, to add a text marker:

```
auto cmd = (AkCmd_AddOutputCaptureMarker*)AK_CommandBuffer_Add(buffer, AkCommand_AddOutputCaptureMarker);
cmd->samplePos = AK_INVALID_SAMPLE_POS;
cmd->markerDataSize = strlen("my marker") + 1;
AK_CommandBuffer_AddString(buffer, "my marker");
```

To add a binary data marker:

```
auto cmd = (AkCmd_AddOutputCaptureMarker*)AK_CommandBuffer_Add(buffer, AkCommand_AddOutputCaptureMarker);
cmd->samplePos = AK_INVALID_SAMPLE_POS;
cmd->markerDataSize = sizeof(data);
AK_CommandBuffer_AddArray(buffer, sizeof(data), 1, data);
```

This command can fail for the following reasons:

- `AK_InvalidParameter` if `markerDataSize` is 0 or there is no marker data following the command

参见
:   - [AkCommand\_AddOutputCaptureMarker](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda32b68ae6b1020f48263203dd7c413de4 "See AkCmd_AddOutputCaptureMarker")
    - [AK::SoundEngine::AddOutputCaptureMarker](namespace_a_k_1_1_sound_engine_a3d481445752b1fb91e9a1ac4ae815342.html#a3d481445752b1fb91e9a1ac4ae815342)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1182](_ak_command_types_8h_source.html#l01182) 行定义.