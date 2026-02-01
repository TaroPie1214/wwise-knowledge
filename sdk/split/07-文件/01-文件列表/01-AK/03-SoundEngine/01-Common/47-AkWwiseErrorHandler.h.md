# AkWwiseErrorHandler.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes)

AkWwiseErrorHandler.h 文件参考

`#include <AK/SoundEngine/Common/AkSoundEngine.h>`  
`#include <AK/SoundEngine/Common/AkSoundEngineExport.h>`

[浏览源代码.](_ak_wwise_error_handler_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| class | [AkWwiseErrorHandler](class_ak_wwise_error_handler.html) |
|  | |

## 详细描述

Contains the wwiseErrorHandler Has a static callback function that can recieved an error message from the sound engine. Has a translator used to translate the message coming from the sound engine. The translator can be a combination of multiple different type of translators. (See AddTranslator) The translated message is then send back to the sound engine through another callback function.

在文件 [AkWwiseErrorHandler.h](_ak_wwise_error_handler_8h_source.html) 中定义.