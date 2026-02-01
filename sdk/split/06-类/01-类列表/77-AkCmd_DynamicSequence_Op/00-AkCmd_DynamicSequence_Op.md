# AkCmd_DynamicSequence_Op

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___dynamic_sequence___op-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_DynamicSequence\_Op结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) | [playingID](struct_ak_cmd___dynamic_sequence___op_af7881824d77695e7a0e8b14b7f2a492d.html#af7881824d77695e7a0e8b14b7f2a492d) |
|  | Playing ID that was used to open the dynamic sequence [更多...](struct_ak_cmd___dynamic_sequence___op_af7881824d77695e7a0e8b14b7f2a492d.html#af7881824d77695e7a0e8b14b7f2a492d) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [operation](struct_ak_cmd___dynamic_sequence___op_aeec0033aad6858e98fedba55133f1d8f.html#aeec0033aad6858e98fedba55133f1d8f) |
|  | Operation to execute the dynamic sequence [更多...](struct_ak_cmd___dynamic_sequence___op_aeec0033aad6858e98fedba55133f1d8f.html#aeec0033aad6858e98fedba55133f1d8f) |
|  | |
| [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) | [transitionTime](struct_ak_cmd___dynamic_sequence___op_a29f13fc43cd54b2d33e43f35f2fd211d.html#a29f13fc43cd54b2d33e43f35f2fd211d) |
|  | (optional) Duration of transition in milliseconds [更多...](struct_ak_cmd___dynamic_sequence___op_a29f13fc43cd54b2d33e43f35f2fd211d.html#a29f13fc43cd54b2d33e43f35f2fd211d) |
|  | |
| [AkCurveInterpolation\_t](_ak_enums_8h_ae3bffd4844b52da6ff4566554af4b176.html#ae3bffd4844b52da6ff4566554af4b176) | [fadeCurve](struct_ak_cmd___dynamic_sequence___op_a765b53a88b208004cfea0283bc5494bc.html#a765b53a88b208004cfea0283bc5494bc) |
|  | (optional) Curve type to be used for the transition, see [AkCurveInterpolation](_ak_enums_8h_a77872044bca52a4d20324739154f2399.html#a77872044bca52a4d20324739154f2399) [更多...](struct_ak_cmd___dynamic_sequence___op_a765b53a88b208004cfea0283bc5494bc.html#a765b53a88b208004cfea0283bc5494bc) |
|  | |

## 详细描述

Execute an operation on a dynamic sequence.

Refer to [AkDynamicSequenceOp](_ak_enums_8h_aa09f7f4663d4cee83811bcaa5bbe1b9d.html#aa09f7f4663d4cee83811bcaa5bbe1b9d) to learn the possible operations.

This command can fail for the following reasons:

- AK\_InvalidParameter: `playingID` is an invalid ID, or `operation` is not a valid dynamic sequence operation, or `fadeCurve` is not a valid curve type.
- AK\_IDNotFound: `playingID` is valid but does not refer to an active dynamic sequence

参见
:   - [AkCommand\_DynamicSequence\_Op](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdab920c51e91c01699883765d7db7553da "See AkCmd_DynamicSequence_Op")
    - [AkCmd\_DynamicSequence\_Open](struct_ak_cmd___dynamic_sequence___open.html)
    - [AkDynamicSequenceOp](_ak_enums_8h_aa09f7f4663d4cee83811bcaa5bbe1b9d.html#aa09f7f4663d4cee83811bcaa5bbe1b9d)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [819](_ak_command_types_8h_source.html#l00819) 行定义.