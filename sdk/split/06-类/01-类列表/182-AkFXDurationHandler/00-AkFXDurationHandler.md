# AkFXDurationHandler

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_f_x_duration_handler-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 属性](#pro-attribs)

AkFXDurationHandler类 参考

`#include <AkFXDurationHandler.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| void | [Setup](class_ak_f_x_duration_handler_a7dcea0ad772ee3393b9ebdc6d4428920.html#a7dcea0ad772ee3393b9ebdc6d4428920) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fDuration, [AkInt16](_ak_numeral_types_8h_a20960d2f96e0ecd7debd52d6633ecaac.html#a20960d2f96e0ecd7debd52d6633ecaac) in\_iLoopingCount, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uSampleRate) |
|  | Setup duration handler [更多...](class_ak_f_x_duration_handler_a7dcea0ad772ee3393b9ebdc6d4428920.html#a7dcea0ad772ee3393b9ebdc6d4428920) |
|  | |
| void | [Reset](class_ak_f_x_duration_handler_ac04dbf110c2ac073df56624c96a7d959.html#ac04dbf110c2ac073df56624c96a7d959) () |
|  | Reset looping and frame counters and start again. [更多...](class_ak_f_x_duration_handler_ac04dbf110c2ac073df56624c96a7d959.html#ac04dbf110c2ac073df56624c96a7d959) |
|  | |
| void | [SetLooping](class_ak_f_x_duration_handler_a6596c6bab0d15ef166636045034e14a5.html#a6596c6bab0d15ef166636045034e14a5) ([AkInt16](_ak_numeral_types_8h_a20960d2f96e0ecd7debd52d6633ecaac.html#a20960d2f96e0ecd7debd52d6633ecaac) in\_iNumLoops) |
|  | Change number of loop iterations (0 == infinite). [更多...](class_ak_f_x_duration_handler_a6596c6bab0d15ef166636045034e14a5.html#a6596c6bab0d15ef166636045034e14a5) |
|  | |
| void | [SetDuration](class_ak_f_x_duration_handler_a5b87d61151150560aac6adf984269068.html#a5b87d61151150560aac6adf984269068) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fDuration) |
|  | Set current duration per iteration (in secs). [更多...](class_ak_f_x_duration_handler_a5b87d61151150560aac6adf984269068.html#a5b87d61151150560aac6adf984269068) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [GetDuration](class_ak_f_x_duration_handler_a2fc7819453bc98430b0cfe0eb7c922ce.html#a2fc7819453bc98430b0cfe0eb7c922ce) () const |
|  | Return current total duration (considering looping) in secs. [更多...](class_ak_f_x_duration_handler_a2fc7819453bc98430b0cfe0eb7c922ce.html#a2fc7819453bc98430b0cfe0eb7c922ce) |
|  | |
| void | [ProduceBuffer](class_ak_f_x_duration_handler_a9a66c33b5af1479b80fd5ee1a525de0a.html#a9a66c33b5af1479b80fd5ee1a525de0a) ([AkAudioBuffer](class_ak_audio_buffer.html) \*io\_pBuffer) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [ProduceBuffer](class_ak_f_x_duration_handler_a85d9471ce728a6fc0e7173dad778d2db.html#a85d9471ce728a6fc0e7173dad778d2db) ([AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) in\_uMaxFrames, [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) &out\_uValidFrames) |
|  | |

|  |  |
| --- | --- |
| Protected 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [m\_uIterationFrame](class_ak_f_x_duration_handler_a0ede1d7249ed9ad714f2f26b73d669b5.html#a0ede1d7249ed9ad714f2f26b73d669b5) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [m\_uFrameCount](class_ak_f_x_duration_handler_a7e919d9247340a2ef870d2f73e86a7aa.html#a7e919d9247340a2ef870d2f73e86a7aa) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [m\_uSampleRate](class_ak_f_x_duration_handler_aa7acbf0695b14d1f800e941296cb81ae.html#aa7acbf0695b14d1f800e941296cb81ae) |
|  | |
| [AkInt16](_ak_numeral_types_8h_a20960d2f96e0ecd7debd52d6633ecaac.html#a20960d2f96e0ecd7debd52d6633ecaac) | [m\_iNumLoops](class_ak_f_x_duration_handler_aa705751876d0a3cead811fd58f7bb600.html#aa705751876d0a3cead811fd58f7bb600) |
|  | |

## 详细描述

Duration handler service for source plug-in. Duration may change between different execution

在文件 [AkFXDurationHandler.h](_ak_f_x_duration_handler_8h_source.html) 第 [34](_ak_f_x_duration_handler_8h_source.html#l00034) 行定义.