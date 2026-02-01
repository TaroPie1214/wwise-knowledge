# AkCmd_SetSpeakerAngles

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___set_speaker_angles-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SetSpeakerAngles结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [numAngles](struct_ak_cmd___set_speaker_angles_a7962ed5dc893e8a2a48fbae01dd09a2e.html#a7962ed5dc893e8a2a48fbae01dd09a2e) |
|  | Number of elements in in\_pfSpeakerAngles. It must correspond to AK::GetNumberOfAnglesForConfig( AK\_SPEAKER\_SETUP\_DEFAULT\_PLANE ) (the value returned by [GetSpeakerAngles()](namespace_a_k_1_1_sound_engine_a02ad46cabd64c04e8be198bfdc44be6b.html#a02ad46cabd64c04e8be198bfdc44be6b)). [更多...](struct_ak_cmd___set_speaker_angles_a7962ed5dc893e8a2a48fbae01dd09a2e.html#a7962ed5dc893e8a2a48fbae01dd09a2e) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [heightAngle](struct_ak_cmd___set_speaker_angles_ad14c0d8dd1b9c6c46642cc80c22e8bcf.html#ad14c0d8dd1b9c6c46642cc80c22e8bcf) |
|  | Elevation of the height layer, in degrees relative to the plane [-90,90], but it cannot be 0. [更多...](struct_ak_cmd___set_speaker_angles_ad14c0d8dd1b9c6c46642cc80c22e8bcf.html#ad14c0d8dd1b9c6c46642cc80c22e8bcf) |
|  | |
| [AkOutputDeviceID](_ak_typedefs_8h_ab608859e8c575f46ce18433e32aa2ccd.html#ab608859e8c575f46ce18433e32aa2ccd) | [outputID](struct_ak_cmd___set_speaker_angles_ae9aee1e39b47ffb1ddb1a3e9c91553b8.html#ae9aee1e39b47ffb1ddb1a3e9c91553b8) |
|  | Output ID to set the panning rule on. This can be obtained from [AK\_SoundEngine\_GetOutputID](_ak_command_buffer_8h_abcca2351f34551ab1d705e13154b42d1.html#abcca2351f34551ab1d705e13154b42d1). Set to 0 for primary output. [更多...](struct_ak_cmd___set_speaker_angles_ae9aee1e39b47ffb1ddb1a3e9c91553b8.html#ae9aee1e39b47ffb1ddb1a3e9c91553b8) |
|  | |

## 详细描述

Sets speaker angles of the specified device. Speaker angles are used for 3D positioning of sounds over standard configurations. Note that the current version of Wwise only supports positioning on the plane.

The Sound Engine expects an array of loudspeaker pair angles after the command (in degrees relative to azimuth ]0,180]). For example:

```
auto cmd = (AkCmd_SetSpeakerAngles*)AK_CommandBuffer_Add(buffer, AkCommand_SetSpeakerAngles);
cmd->idOutput = 0;
cmd->fHeightAngle = 30.0f;
cmd->uNumAngles = myAngles.size();
AK_CommandBuffer_AddArray(buffer, sizeof(AkReal32), myAngles.size(), myAngles.data());
```

The speaker angles are expressed as an array of loudspeaker pairs, in degrees, relative to azimuth ]0,180], for a 7.1 speaker configuration. Supported loudspeaker setups are always symmetric; the center speaker is always in the middle and thus not specified by angles. Angles must be set in ascending order.

|  |  |
| --- | --- |
|  | **备注:**  - This command requires the minimum speaker angle between any pair of speakers to be at least 5 degrees. - When setting angles for a 5.1 speaker layout, we recommend that you select an angle for the SL and SR channels, then subtract 15 degrees for in\_pfSpeakerAngles[1] and add 15 degrees for in\_pfSpeakerAngles[2] to set the arc appropriately. |

Typical usage:

- Initialize the sound engine and/or add secondary output(s).
- Get number of speaker angles and their value into an array using [GetSpeakerAngles()](namespace_a_k_1_1_sound_engine_a02ad46cabd64c04e8be198bfdc44be6b.html#a02ad46cabd64c04e8be198bfdc44be6b).
- Modify the angles and call [SetSpeakerAngles()](namespace_a_k_1_1_sound_engine_afaf319902f00bbf38fbff9129086d912.html#afaf319902f00bbf38fbff9129086d912).

  警告
  :   This command only applies to configurations (or subset of these configurations) that are standard and whose speakers are on the plane (2D).

  This command can fail for the following reasons:
- `AK_InvalidParameter` when one of the angle values is NaN or Inf, or if one of the parameter is invalid. Check the debug log.
- `AK_IDNotFound` if `outputID` refers to a non-existent device
- `AK_InsufficientMemory` if there is not enough memory to complete the operation.

参见
:   - [AkCommand\_SetSpeakerAngles](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaa41934308a8d68a347574bdc560648c4 "See AkCmd_SetSpeakerAngles")
    - [AK::SoundEngine::SetSpeakerAngles](namespace_a_k_1_1_sound_engine_afaf319902f00bbf38fbff9129086d912.html#afaf319902f00bbf38fbff9129086d912)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1117](_ak_command_types_8h_source.html#l01117) 行定义.