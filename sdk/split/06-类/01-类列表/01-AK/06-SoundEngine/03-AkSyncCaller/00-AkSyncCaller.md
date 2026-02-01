# AkSyncCaller

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [SoundEngine](namespace_a_k_1_1_sound_engine.html)
- [AkSyncCaller](class_a_k_1_1_sound_engine_1_1_ak_sync_caller.html)

[所有成员列表](class_a_k_1_1_sound_engine_1_1_ak_sync_caller-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AK::SoundEngine::AkSyncCaller类 参考

`#include <AkSyncCaller.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [Init](class_a_k_1_1_sound_engine_1_1_ak_sync_caller_a2fd14d40dd4b4e7f09a6f334a5fb24fc.html#a2fd14d40dd4b4e7f09a6f334a5fb24fc) () |
|  | |
| bool | [IsDone](class_a_k_1_1_sound_engine_1_1_ak_sync_caller_ab978de5f4002968ac8e3414436194fef.html#ab978de5f4002968ac8e3414436194fef) () |
|  | |
| void | [Done](class_a_k_1_1_sound_engine_1_1_ak_sync_caller_a795a3522eca80570f3a05844e93f740c.html#a795a3522eca80570f3a05844e93f740c) () |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [m\_eResult](class_a_k_1_1_sound_engine_1_1_ak_sync_caller_a0cbc8053c69f9569f70f226e57ea628e.html#a0cbc8053c69f9569f70f226e57ea628e) |
|  | Operation result [更多...](class_a_k_1_1_sound_engine_1_1_ak_sync_caller_a0cbc8053c69f9569f70f226e57ea628e.html#a0cbc8053c69f9569f70f226e57ea628e) |
|  | |

## 详细描述

AkSyncLoader: Init to create a sync event, call the asynchronous method, passing it the address of this object as the cookie, then call Wait.

在文件 [AkSyncCaller.h](_ak_sync_caller_8h_source.html) 第 [43](_ak_sync_caller_8h_source.html#l00043) 行定义.