# AkFXTailHandler

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_f_x_tail_handler-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 属性](#pro-attribs)

AkFXTailHandler类 参考

`#include <AkFXTailHandler.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkFXTailHandler](class_ak_f_x_tail_handler_abb17a456c59dc6cd8a75e5b20d1d8541.html#abb17a456c59dc6cd8a75e5b20d1d8541) () |
|  | Constructor [更多...](class_ak_f_x_tail_handler_abb17a456c59dc6cd8a75e5b20d1d8541.html#abb17a456c59dc6cd8a75e5b20d1d8541) |
|  | |
| void | [HandleTail](class_ak_f_x_tail_handler_a3a33b37c47bbcda9fdaac7294cba3bcd.html#a3a33b37c47bbcda9fdaac7294cba3bcd) ([AkAudioBuffer](class_ak_audio_buffer.html) \*io\_pBuffer, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uTotalTailFrames) |
|  | Handle FX tail and zero pads [AkAudioBuffer](class_ak_audio_buffer.html) if necessary [更多...](class_ak_f_x_tail_handler_a3a33b37c47bbcda9fdaac7294cba3bcd.html#a3a33b37c47bbcda9fdaac7294cba3bcd) |
|  | |
| bool | [HasTailRemaining](class_ak_f_x_tail_handler_a77ad0b2d77351bef12f5ecf3c00f0e31.html#a77ad0b2d77351bef12f5ecf3c00f0e31) () |
|  | |

|  |  |
| --- | --- |
| Protected 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uTailFramesRemaining](class_ak_f_x_tail_handler_a99f9fd1ce02ec44ce41c0a2f53842764.html#a99f9fd1ce02ec44ce41c0a2f53842764) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uTotalTailFrames](class_ak_f_x_tail_handler_addbdb1857ba150e6ac7bf105e3fa6126.html#addbdb1857ba150e6ac7bf105e3fa6126) |
|  | |

## 详细描述

Effect tail handling utility class. Handles varying number of tail frames from frame to frame (i.e. based on RTPC parameters). Handles effect revived (quit tail) and reenters etc.

在文件 [AkFXTailHandler.h](_ak_f_x_tail_handler_8h_source.html) 第 [40](_ak_f_x_tail_handler_8h_source.html#l00040) 行定义.