# AkAutoStmBufSettings

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_auto_stm_buf_settings-members.html) |
[Public 属性](#pub-attribs)

AkAutoStmBufSettings结构体 参考

Automatic streams buffer settings/constraints.
[更多...](struct_ak_auto_stm_buf_settings.html#details)

`#include <IAkStreamMgr.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uBufferSize](struct_ak_auto_stm_buf_settings_af03eccfc7bb94c260b867e4258b11500.html#af03eccfc7bb94c260b867e4258b11500) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMinBufferSize](struct_ak_auto_stm_buf_settings_ad42730405a09edb0a1b6f4794d441e27.html#ad42730405a09edb0a1b6f4794d441e27) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uBlockSize](struct_ak_auto_stm_buf_settings_aef1c205a77091fbc6c9ded22fb531dfb.html#aef1c205a77091fbc6c9ded22fb531dfb) |
|  | Hard user constraint: When non-zero, buffer size will be a multiple of that number, and returned addresses will always be aligned on multiples of this value. [更多...](struct_ak_auto_stm_buf_settings_aef1c205a77091fbc6c9ded22fb531dfb.html#aef1c205a77091fbc6c9ded22fb531dfb) |
|  | |

## 详细描述

Automatic streams buffer settings/constraints.

在文件 [IAkStreamMgr.h](_i_ak_stream_mgr_8h_source.html) 第 [107](_i_ak_stream_mgr_8h_source.html#l00107) 行定义.